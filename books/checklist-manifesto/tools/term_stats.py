"""Term statistics before translating (see review/terms/README.md).

    uv run --with spacy==3.8.7 --with <en_core_web_sm 3.8.0 wheel> python -I \
        books/checklist-manifesto/tools/term_stats.py candidates.json

candidates.json comes from en-zh-translation-polish's terms.py, run on the English text without footnotes.
This book has no print index, so people and named entities come from spaCy's named entity recognizer instead;
people-zh.tsv is the list checked by hand, and people.tsv shows which of its rows each recognized name belongs to.
Writes review/terms/: candidates.tsv, people.tsv, named-entities.tsv, definitions.tsv, headings.tsv and
glossary-evidence.tsv, and fills in the "首次出现" and "出现次数" columns of the core terms in glossary.md.
"""

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
OUT = BOOK / "review" / "terms"
GLOSSARY = BOOK / "glossary.md"
DEFINITION = re.compile(
    r"\b(we call|called|calls|known as|dubbed|coined|the term|so-called|referred to as|nicknamed|stands for|"
    r"short for|what (?:he|she|they|it|we|you|some|many|people|pilots|surgeons|engineers) call(?:ed|s)?|"
    r"a phrase|the phrase|the word|is defined|definition|means that|meaning)\b", re.I)
NAMED = ("ORG", "GPE", "LOC", "FAC", "PRODUCT", "NORP", "EVENT", "WORK_OF_ART", "LAW")
# Names the recognizer took for people: (name as recognized, what it is).
NOT_PEOPLE = {
    "Jet A-1": "航空燃油型号", "Helsinki Accord": "作者的戏称（“赫尔辛基协定”）", "Asystole": "心搏停止（医学名词）",
    "Briton": "英国人（泛指）", "James Beard Foundation Best Chef": "奖项名", "John Moriarty": "公司名的一部分",
    "Debris": "碎片（普通名词）", "Detail": "Detail men（医药代表）", "Discipline": "纪律（普通名词）",
    "Douglas": "道格拉斯公司", "Fahrenheit": "华氏度", "Foley": "Foley 导尿管", "Van Halen": "范·海伦乐队",
    "Berkshire Hathaway": "伯克希尔·哈撒韦公司", "Cort": "Cort 家具公司", "Denham": "达尔齐勋爵封号里的地名",
    "Jefferson Parish": "杰斐逊堂区（地名）", "Morale": "士气（普通名词）", "Orwellian": "奥威尔式的（形容词）",
    "Oscar": "奥斯卡奖", "Oxygen": "氧气（清单条目）", "Physician": "医生（普通名词）", "Problem": "问题（普通名词）",
    "Russia Wharf": "俄罗斯码头大楼", "Safeguard": "舒肤佳香皂", "Sumner Shane": "公司名",
    "Taylorized": "泰勒制的（形容词）", "Thoracic Surgery": "期刊名的一部分", "Der Held von": "德语报纸标题",
    "Worldwide": "全世界（普通词）", "Jordan": "约旦（国名）",
}

# The core terms of glossary.md: English column -> (pattern, case sensitive). Counts are of the English body text
# without footnotes and headings, so a word's ordinary uses are counted too.
TERMS = {
    "checklist": (r"\bchecklists?\b", False),
    "check / checks": (r"\bchecks?\b", False),
    "failure / avoidable failure": (r"\bfailures?\b", False),
    "ignorance / ineptitude": (r"\bignorance\b|\bineptitude\b", False),
    "necessary fallibility / fallibility": (r"\bfallib\w+", False),
    "eptitude": (r"(?<!in)\beptitude\b", False),
    "complexity / extreme complexity": (r"\bcomplexit(?:y|ies)\b", False),
    "complicated": (r"\bcomplicated\b", False),
    "complex": (r"\bcomplex\b", False),
    "know-how / expertise / experts": (r"\bknow-how\b|\bexpertise\b|\bexperts?\b", False),
    "specialization / superspecialization": (r"\b(?:super-?|ultra|sub)?speciali[sz]\w*|\bsubspecialty\b", False),
    "Master Builder / Master Physician": (r"\bMaster (?:Builder|Physician)s?\b", True),
    "cognitive net": (r"\bcognitive net\b", False),
    "forcing function": (r"\bforcing functions?\b", False),
    "all-or-none process": (r"\ball-or-none\b", False),
    "stupid stuff / dumb stuff": (r"\b(?:stupid|dumb) (?:but critical )?stuff\b", False),
    "construction schedule / submittal schedule": (r"\b(?:construction|submittal) schedules?\b", False),
    "communication checks": (r"\bcommunication (?:checks?|checklists?|tasks)\b", False),
    "power": (r"\bpower\b", False),
    "command-and-control": (r"\bcommand-and-control\b", False),
    "pause point": (r"\bpause points?\b", False),
    "checkpoint": (r"\bcheckpoints?\b", False),
    "DO-CONFIRM / READ-DO": (r"\bDO-CONFIRM\b|\bREAD-DO\b", True),
    "killer items": (r"\bkiller items?\b", False),
    "normal / non-normal checklists": (r"“normal” checklists|\bnon-normal\b", False),
    "briefing / team briefing": (r"\bbriefings?\b", False),
    "activation phenomenon": (r"\bactivation phenomenon\b", False),
    "teamwork": (r"\bteamwork\b", False),
    "discipline": (r"\bdiscipline\b", False),
    "professionalism / selflessness / skill / trustworthiness":
        (r"\bprofessionalism\b|\bselflessness\b|\btrustworthiness\b|\bcode of conduct\b", False),
    "autonomy / collegiality": (r"\bautonomy\b|\bcollegiality\b", False),
    "protocol / judgment / craft": (r"\bprotocols?\b|\bjudgment\b|\bcraft\b", False),
    "procedure": (r"\bprocedures?\b", False),
    "hero / heroism": (r"\bhero(?:es|ism|ic)?\b", False),
    "expert audacity / the right stuff": (r"\bexpert audacity\b|\bright stuff\b", False),
    "too much airplane for one man to fly": (r"\btoo much airplane\b", False),
    "save / great saves": (r"\bsaves?\b", False),
    "error / mistake": (r"\berrors?\b|\bmistakes?\b", False),
    "leverage": (r"\bleverage\w*", False),
    "behavior-change delivery vehicle": (r"\bdelivery vehicle\b", False),
    "pilot study / pilot sites": (r"\bpilot (?:study|hospitals?|sites?)\b|\beight-city pilot\b", False),
    "pilot / test pilot / copilot": (r"\b(?:co|test )?pilots?\b(?! (?:study|hospitals?|sites?)\b)", False),
    "pilot flying / pilot not flying": (r"\bpilot (?:not )?flying\b", False),
    "crew": (r"\bcrews?\b", False),
    "simulator": (r"\bsimulators?\b", False),
    "cockpit voice recorder": (r"\bcockpit voice recorder\b", False),
    "ditching": (r"\bditch(?:ing)?\b", False),
    "bird strike": (r"\bbird strikes?\b", False),
    "fly-by-wire": (r"\bfly-by-wire\b", False),
    "uncommanded rollback": (r"\brollback\b|\brolled back\b", False),
    "safe surgery checklist": (r"\b(?:safe )?surgery checklists?\b|\bsurgical checklists?\b", False),
    "Safe Surgery Saves Lives": (r"\bSafe Surgery Saves Lives\b", True),
    "before anesthesia / before incision / sign-out / time-out":
        (r"\bbefore (?:anesthesia|incision|leaving the OR)\b|\bsign-out\b|\btime-out\b", False),
    "Cleared for Takeoff": (r"\bCleared for Take ?off\b", False),
    "Keystone Initiative": (r"\bKeystone Initiative\b", True),
    "pay-for-performance": (r"\bpay-for-performance\b", False),
    "Hawthorne effect": (r"\bHawthorne effect\b", False),
    "vital signs": (r"\bvital signs?\b|\bvitals\b", False),
    "Code Blue": (r"\bCode Blue\b", True),
    "central line / line infection": (r"\bcentral lines?\b|\bline infections?\b|\bline-infection\b", False),
    "ICU / intensive care / critical care": (r"\bICUs?\b|(?i:\bintensive care\b|\bcritical care\b|\bintensivists?\b|\blife support\b)", True),
    "operating room / OR / operating theater": (r"\bORs?\b|(?i:\boperating rooms?\b|\boperating theaters?\b)", True),
    "anesthesiologist / anesthetist": (r"\banesthesiologists?\b|\banesthetists?\b", False),
    "circulating nurse / scrub nurse": (r"\bcirculating nurses?\b|\bscrub (?:nurse|tech)s?\b", False),
    "resident / attending / fellowship": (r"\bresidents?\b|\bresidenc(?:y|ies)\b|\battending\b|\bfellow(?:s|ships?)?\b", False),
    "general surgery / general surgeon": (r"\bgeneral surg\w+", False),
    "complication": (r"\bcomplications?\b", False),
    "incision": (r"\bincisions?\b", False),
    "surgical fire": (r"\bsurgical fires?\b|\boperating room fires\b", False),
    "value investor / margin of safety": (r"\bvalue investors?\b|\bmargin of safety\b", False),
    "cocaine brain / greed mode / fear mode": (r"\bcocaine brain\b|\bgreed mode\b|\bfear mode\b", False),
    "mental checklist / Day Three Checklist": (r"\bmental checklist\b|\bDay Three Checklist\b|\bthree-day (?:list|check)\b", False),
    "venture capitalists and their styles":
        (r"(?i:\bventure capitalists?\b)|\bArt Critics?\b|\bSponges\b|\bProsecutors\b|\bSuitors\b|\bTerminators\b|\bAirline Captains?\b", True),
    "trades / tradesmen": (r"\btrades\b|\btradesmen\b", False),
    "general contractor / subcontractor": (r"\b(?:sub)?contractors?\b", False),
    "structural engineer / structural engineering": (r"\bstructural engineer\w*", False),
    "project executive / field office": (r"\bproject executive\b|\bfield office\b|\bfield bosses\b", False),
    "building failure": (r"\bbuilding failures?\b", False),
    "tuned mass damper": (r"\btuned mass damper\b", False),
    "recipe": (r"\brecipes?\b", False),
    "sous chef / line cooks / pow wow / read-back": (r"\bsous chefs?\b|\bline cooks?\b|\bpow wow\b|\bread-back\b", False),
    "system": (r"\bsystems?\b", False),
    "patient safety": (r"\bpatient safety\b", False),
    "case": (r"\bcases?\b", False),
}


def chapters():
    return json.loads((BOOK / "book.json").read_text())["chapters"]


def body_sections():
    """[(chapter id, text without footnotes)] in book order."""
    out = []
    for c in chapters():
        text = (BOOK / "en" / c["file"]).read_text()
        text = re.sub(r"(?m)^\[\^\d+\]: .*\n?", "", text)
        out.append((c["id"], re.sub(r"\[\^\d+\]", "", text)))
    return out


def paragraphs(text):
    """Body blocks without headings, rules and Markdown marks."""
    for block in text.split("\n\n"):
        block = block.strip()
        if not block or block.startswith("#") or block == "---":
            continue
        block = re.sub(r"(?m)^> ?", "", block)
        yield " ".join(block.replace("*", "").split())


def sentences(text):
    for block in paragraphs(text):
        yield from re.split(r"(?<=[.?!”])\s+(?=[A-Z“])", block)


def occurrences(pattern, sections, flags=0):
    rx = re.compile(pattern, flags)
    counts = [(cid, len(rx.findall(text))) for cid, text in sections]
    hits = [(cid, n) for cid, n in counts if n]
    return sum(n for _, n in hits), len(hits), hits[0][0] if hits else ""


def tsv(name, header, rows):
    lines = ["\t".join(header)] + ["\t".join(str(x) for x in row) for row in rows]
    (OUT / name).write_text("\n".join(lines) + "\n")
    print(f"{name}: {len(rows)} rows")


def write_candidates(candidates_path, sections):
    ids = {Path(c["file"]).name: c["id"] for c in chapters()}
    rows = []
    for c in json.loads(Path(candidates_path).read_text())["english"]:
        docs = {ids.get(Path(d).name, Path(d).name): n for d, n in c["documents"].items()}
        first = next((cid for cid, _ in sections if cid in docs), "")
        forms = ", ".join(f"{f} {n}" for f, n in sorted(c["forms"].items(), key=lambda x: -x[1])[:3])
        rows.append((c["candidate"], c["frequency"], len(docs), first, len(c["candidate"].split()), forms))
    rows.sort(key=lambda r: (-r[1], r[0]))
    tsv("candidates.tsv", ("candidate", "frequency", "chapters", "first", "words", "forms"), rows)


def clean_entity(text):
    text = re.sub(r"[’']s$", "", text.strip(" “”\"‘’.,;:()"))
    return " ".join(text.split())


def name_tokens(name):
    """'Chesley B. “Sully” Sullenberger III' -> {'Chesley', 'Sully', 'Sullenberger'}."""
    return {t for t in re.findall(r"[A-Z][\w’'-]+", name.replace("“", " ").replace("”", " ")) if t not in ("III", "Mr", "Lord", "Sir")}


def checked_people():
    path = OUT / "people-zh.tsv"
    if not path.exists():
        return []
    return [row["name"] for row in csv.DictReader(path.open(), delimiter="\t")]


def write_entities(sections):
    """people.tsv (PERSON, grouped by surname) and named-entities.tsv (organizations, places, works...)."""
    import spacy

    nlp = spacy.load("en_core_web_sm")
    people, named = defaultdict(Counter), defaultdict(Counter)
    for cid, text in sections:
        for doc in nlp.pipe(paragraphs(text)):
            for ent in doc.ents:
                name = clean_entity(ent.text)
                if not name or not re.search(r"[A-Z]", name):
                    continue
                if ent.label_ == "PERSON":
                    people[name][cid] += 1
                elif ent.label_ in NAMED:
                    named[(ent.label_, name)][cid] += 1

    order = [cid for cid, _ in sections]
    checked = checked_people()
    groups = defaultdict(list)
    for name in people:
        groups[name.split()[-1]].append(name)
    rows = []
    for surname, names in groups.items():
        names.sort(key=lambda n: (-len(n.split()), -sum(people[n].values())))
        ner = sum(sum(people[n].values()) for n in names)
        n, count, where = occurrences(rf"\b{re.escape(surname)}\b", sections)
        forms = ", ".join(f"{x} {sum(people[x].values())}" for x in names[:5])
        if names[0] in NOT_PEOPLE:
            match = f"not a person: {NOT_PEOPLE[names[0]]}"
        else:
            # a recognized form belongs to a checked person when all its name words are in that person's name
            forms_tokens = [{t for t in name_tokens(x) if len(t) > 1} for x in names]
            found = [p for p in checked if any(ft and ft <= name_tokens(p) for ft in forms_tokens)]
            match = "; ".join(found) or "MISSING"
        first = where or min((c for x in names for c in people[x]), key=order.index)
        rows.append((names[0], forms, ner, n, count, first, match))
    rows.sort(key=lambda r: r[0].split()[-1].lower())
    tsv("people.tsv", ("name", "NER forms", "NER mentions", "surname in text", "chapters", "first", "people-zh.tsv"), rows)
    missing = [r[0] for r in rows if r[-1] == "MISSING"]
    if checked and missing:
        print("recognized names not in people-zh.tsv:", ", ".join(missing))

    rows = []
    for (label, name), per in named.items():
        first = min(per, key=order.index)
        rows.append((name, label, sum(per.values()), len(per), first))
    rows.sort(key=lambda r: (-r[2], r[0]))
    tsv("named-entities.tsv", ("entity", "NER label", "mentions", "chapters", "first"), rows)


def write_definitions(sections):
    defs = []
    for cid, text in sections:
        for sentence in sentences(text):
            found = DEFINITION.search(sentence)
            if found:
                defs.append((cid, found.group(0), sentence))
    tsv("definitions.tsv", ("chapter", "signal", "sentence"), defs)


def write_headings(sections):
    heads = [(cid, line[2:]) for cid, text in sections for line in text.split("\n") if line.startswith("# ")]
    tsv("headings.tsv", ("chapter", "heading"), heads)


def fill_glossary(sections):
    """Count every core term of glossary.md, write its first chapter and count into the table, and list the
    first sentence it appears in (glossary-evidence.tsv)."""
    body = [(cid, "\n\n".join(paragraphs(text))) for cid, text in sections]
    lines = GLOSSARY.read_text().split("\n")
    start = lines.index("## 核心概念")
    header = [c.strip() for c in lines[start + 2].strip("|").split("|")]
    first_col, count_col = header.index("首次出现"), header.index("出现次数")
    evidence, seen = [], set()
    for i in range(start + 4, len(lines)):
        if not lines[i].startswith("|"):
            break
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        label = cells[0]
        if label not in TERMS:
            raise SystemExit(f"glossary.md: no pattern in TERMS for {label!r}")
        seen.add(label)
        pattern, case = TERMS[label]
        n, _, first = occurrences(pattern, body, 0 if case else re.I)
        if not n:
            raise SystemExit(f"{label!r}: pattern {pattern!r} finds nothing")
        cells[first_col], cells[count_col] = first, str(n)
        lines[i] = "| " + " | ".join(cells) + " |"
        rx = re.compile(pattern, 0 if case else re.I)
        example = next(s for s in sentences(dict(sections)[first]) if rx.search(s))
        evidence.append((label, cells[1], first, n, example, "Claude（初定）"))
    unused = set(TERMS) - seen
    if unused:
        raise SystemExit(f"TERMS not in glossary.md: {sorted(unused)}")
    GLOSSARY.write_text("\n".join(lines))
    tsv("glossary-evidence.tsv", ("term", "chinese", "first", "count", "example", "decided by"), evidence)


def main(candidates_path):
    OUT.mkdir(parents=True, exist_ok=True)
    sections = body_sections()
    write_candidates(candidates_path, sections)
    write_entities(sections)
    write_definitions(sections)
    write_headings(sections)
    if "## 核心概念" in GLOSSARY.read_text():
        fill_glossary(sections)


if __name__ == "__main__":
    main(sys.argv[1])
