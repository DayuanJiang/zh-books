"""Term statistics before translating (see review/terms/README.md).

    uv run --project framework/tools python -I books/thinking-in-systems/tools/term_stats.py candidates.json

candidates.json comes from en-zh-translation-polish's terms.py, run on the English text without footnotes.
This EPUB has no print index. In its place the script reads the author's own glossary in the appendix, the
bold-face terms of the chapters (the book's asterisk note says they are defined in that glossary) and the bold
margin principles, which the appendix repeats in "Summary of Systems Principles". People come from the PEOPLE
list below, checked by hand against the text; every PERSON entity spaCy finds must belong to one of them or be
listed in NOT_PEOPLE, and every PEOPLE name must have a row in people-zh.tsv.
Writes review/terms/: candidates.tsv, book-glossary.tsv, principles.tsv, people.tsv, named-entities.tsv,
definitions.tsv, headings.tsv and glossary-evidence.tsv, and fills in the "首次出现" and "出现次数" columns of the
core terms in glossary.md.
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
    r"\b(we call|I call|I’ll call|I will call|is called|are called|called|calls|known as|so-called|the term|"
    r"the word|the phrase|is defined|defined as|definition|referred to as|refer to|stands for|know as|"
    r"what (?:he|she|they|we|you|some|many|people|economists|ecologists|engineers|systems (?:people|thinkers|analysts)) "
    r"call(?:ed|s)?|jargon|in systems terms|systems language)\b", re.I)

# Every person named in the body text: (name as written in the book, surname pattern used for counting).
# Checked by hand against the text and the PERSON entities spaCy found; fictional characters are included,
# because their names have to stay the same across chapters.
PEOPLE = [
    ("Donella H. Meadows", r"\bDonella(?: H\.)?(?: \(Dana\))?(?: Meadows)?\b|\bDana(?: Meadows)?\b|\bDANA\b|(?<!Dennis )\bMeadows\b"), ("Dennis Meadows", r"\bDennis Meadows\b"),
    ("Diana Wright", r"\bDiana Wright\b"), ("Jay W. Forrester", r"\b(?:Jay (?:W\. )?)?Forrester\b|\bJay\b"),
    ("Ed Roberts", r"\bRoberts\b"), ("Jack Pugh", r"\bPugh\b"), ("Hartmut Bossel", r"\bHartmut(?: Bossel)?\b|\bBossel, Hartmut\b"),
    ("Rike Bossel", r"\bRike\b"), ("Barry Richmond", r"\bRichmond\b"), ("Peter Senge", r"\bSenge\b"),
    ("John D. Sterman", r"\bSterman\b"), ("Peter Allen", r"\bPeter Allen\b"), ("Gregory Bateson", r"\bBateson\b"),
    ("Kenneth Boulding", r"\bBoulding\b"), ("Herman Daly", r"\bDaly\b"), ("Albert Einstein", r"\bEinstein\b"),
    ("Garrett Hardin", r"\bHardin\b"), ("Václav Havel", r"\bHavel\b"), ("Lewis Mumford", r"\bMumford\b"),
    ("Gunnar Myrdal", r"\bMyrdal\b"), ("E.F. Schumacher", r"\bSchumacher\b"), ("Nelson Mandela", r"\bMandela\b"),
    ("Lech Walesa", r"\bWalesa\b"), ("Robert Pirsig", r"\bPirsig\b"), ("Russell Ackoff", r"\bAckoff\b"),
    ("Poul Anderson", r"\bPoul Anderson\b"), ("Ramon Margalef", r"\bMargalef\b"), ("Honoré Balzac", r"\bBalzac\b"),
    ("Jan Tinbergen", r"\bTinbergen\b"), ("Leonid Brezhnev", r"\bBrezhnev\b"), ("Mikhail Gorbachev", r"\bGorbachev\b"),
    ("Jimmy Carter", r"\bCarter\b"), ("Ronald Reagan", r"\bReagan\b"), ("Aldo Leopold", r"\bLeopold\b"),
    ("C. S. Holling", r"\bHolling\b"), ("Ludwig von Bertalanffy", r"\bBertalanffy\b"),
    ("Jonathan Swift", r"\bSwift\b"), ("Herbert Simon", r"\bSimon\b"),
    ("Hora", r"\bHora\b"), ("Tempus", r"\bTempus\b"), ("James Gleick", r"\bGleick\b"),
    ("Gordon Baskerville", r"\bBaskerville\b"), ("Justus von Liebig", r"\bLiebig\b"), ("Adam Smith", r"\bAdam Smith\b"),
    ("Philip Zimbardo", r"\bZimbardo\b"), ("Wendell Berry", r"\bWendell Berry\b|\bBerry calls\b"),
    ("John Ralston Saul", r"\bRalston Saul\b"), ("Joseph W. Duncan", r"\bDuncan\b"),
    ("John H. Cushman, Jr.", r"\bCushman\b"), ("Nicolae Ceausescu", r"\bCeausescu\b"), ("Helmut Kohl", r"\bKohl\b"),
    ("Lord Peston", r"\bPeston\b"), ("Erik Ipsen", r"\bIpsen\b"), ("Clyde Haberman", r"\bHaberman\b"),
    ("Karl Marx", r"\bMarx\b"), ("Sylvia Nasar", r"\bNasar\b"), ("Bill Clinton", r"\bClinton\b"),
    ("Keith B. Richburg", r"\bRichburg\b"), ("Abdukadr Mahmoud Farah", r"\bFarah\b"), ("Calvin", r"\bCALVIN\b"),
    ("Hobbes", r"\bHobbes\b|\bHOBBES\b"), ("Susie", r"\bSusie\b"), ("Lawrence Malkin", r"\bMalkin\b"),
    ("John K. Akers", r"\bAkers\b"), ("George Bush", r"\bBush\b"), ("Genghis Khan", r"\bGenghis Khan\b"),
    ("John Kenneth Galbraith", r"\bGalbraith\b"), ("Amory Lovins", r"\bAmory Lovins\b"),
    ("Ralph Waldo Emerson", r"\bEmerson\b"), ("Nicolaus Copernicus", r"\bCopernicus\b"),
    ("Johannes Kepler", r"\bKepler\b"), ("Thomas Kuhn", r"\bKuhn\b"), ("G. K. Chesterton", r"\bChesterton\b"),
    ("Fred Kofman", r"\bKofman\b"), ("Nathan Gray", r"\bNathan\b"), ("Buckminster Fuller", r"\bBuckminster Fuller\b"),
    ("Don Michael", r"\bDon Michael\b"), ("Joseph Wood Krutch", r"\bKrutch\b"), ("Ervin Laszlo", r"\bLaszlo\b"),
    ("George P. Richardson", r"\bRichardson\b"), ("Linda B. Sweeney", r"\bSweeney\b"),
    ("Dennis Sherwood", r"\bSherwood\b"), ("Andrew Ford", r"\bFord, Andrew\b"), ("Joanna Macy", r"\bMacy\b"),
    ("Ian Baldwin", r"\bIan\b"), ("Margo Baldwin", r"\bMargo\b"), ("Ann Zulliger", r"\bAnn and Hans\b"),
    ("Hans Zulliger", r"\bZulliger\b"), ("Tom Fiddaman", r"\bFiddaman\b"), ("Chris Soderquist", r"\bSoderquist\b"),
    ("Phil Rice", r"\bPhil Rice\b"), ("Beth Sawin", r"\bSawin\b"), ("Helen Whybrow", r"\bWhybrow\b"),
    ("Jim Schley", r"\bSchley\b"), ("Peter Stein", r"\bPeter Stein\b"), ("Bert Cohen", r"\bBert Cohen\b"),
    ("Hunter Lovins", r"\bHunter Lovins\b"),
]
# Bibliography entries are "Surname, Given name.", so the recognizer sometimes keeps only the given name.
ALIASES = {"Ervin": "Ervin Laszlo", "Peter": "Peter Senge", "Andrew": "Andrew Ford", "Joanna": "Joanna Macy",
           "Ann": "Ann Zulliger", "Linda B. and": "Linda B. Sweeney", "George P. Feedback": "George P. Richardson",
           "John D. Business Dynamics: Systems Thinking": "John D. Sterman",
           "Donella H. The Global Citizen": "Donella H. Meadows", "Meadows": "Donella H. Meadows"}
# Words the recognizer took for people: (text as recognized, what it is).
NOT_PEOPLE = {
    "Slinky": "弹簧圈（玩具）", "Trap": "附录的 *Trap*: 标签", "The Tragedy of": "公地悲剧（标题）",
    "Mark 4:25": "《马可福音》4:25", "Beyond Ghor": "地名古尔", "an Oil Economy": "石油经济（标题）",
    "Firs": "冷杉（插曲标题）", "Sevin": "西维因（杀虫剂）", "balsam fir": "香脂冷杉", "Balsam": "香脂冷杉",
    "Waikiki": "怀基基（地名）", "Near Amsterdam": "阿姆斯特丹附近（地名）", "Joneses": "keeping up with the Joneses（俗语）",
    "Gift": "普通词", "Stay Humble": "第 7 章标题", "Learner": "第 7 章标题", "Mardi Gras": "狂欢节",
    "Geiger": "盖革计数器", "Koch": "科赫雪花（Koch snowflake）", "Irwin McGraw Hill": "出版社",
    "Nicholas Brealey Publishing": "出版社", "Trap:": "附录标签", "GNP": "国民生产总值",
}


def body_sections():
    """[(chapter id, text without footnotes)] in book order."""
    config = json.loads((BOOK / "book.json").read_text())
    out = []
    for c in config["chapters"]:
        text = (BOOK / "en" / c["file"]).read_text()
        text = re.sub(r"(?m)^\[\^\d+\]: .*\n?", "", text)
        out.append((c["id"], re.sub(r"\[\^\d+\]", "", text)))
    return out


def paragraphs(text):
    """Text blocks without headings and images, with block quote and list markers removed."""
    out = []
    for block in text.split("\n\n"):
        block = re.sub(r"(?m)^> ?", "", block).strip()
        if not block or block.startswith("#") or block.startswith("!["):
            continue
        out.append(re.sub(r"(?m)^(?:- |\d+\. )", "", block))
    return out


def sentences(text):
    return [" ".join(s.split()) for p in paragraphs(text) for s in re.split(r"(?<=[.?!”])\s+(?=[A-Z“*])", p)]


def occurrences(pattern, sections, flags=0):
    rx = re.compile(pattern, flags)
    counts = [(cid, len(rx.findall(text))) for cid, text in sections]
    hits = [(cid, n) for cid, n in counts if n]
    return sum(n for _, n in hits), len(hits), hits[0][0] if hits else ""


def tsv(name, header, rows):
    lines = ["\t".join(header)] + ["\t".join(str(x) for x in row) for row in rows]
    (OUT / name).write_text("\n".join(lines) + "\n")
    print(f"{name}: {len(rows)} rows")


def plain(text):
    return re.sub(r"[*_]", "", text)


def term_pattern(term):
    """'Feedback loop' -> a pattern that also finds 'feedback loops'; hyphen and space count as the same."""
    words = [re.escape(w) for w in re.split(r"[- ]", term.lower())]
    return r"\b" + r"[- ]".join(words) + r"(?:s|es)?\b"


def write_candidates(candidates_path, sections):
    ids = {Path(c["file"]).name: c["id"] for c in json.loads((BOOK / "book.json").read_text())["chapters"]}
    rows = []
    for c in json.loads(Path(candidates_path).read_text())["english"]:
        docs = {ids.get(Path(d).name, Path(d).name): n for d, n in c["documents"].items()}
        first = next((cid for cid, _ in sections if cid in docs), "")
        # Hard line breaks (model equations, poems) leave newlines inside some candidates and forms.
        forms = ", ".join(f"{' '.join(f.split())} {n}" for f, n in sorted(c["forms"].items(), key=lambda x: -x[1])[:3])
        name = " ".join(c["candidate"].split())
        rows.append((name, c["frequency"], len(docs), first, len(name.split()), forms))
    rows.sort(key=lambda r: (-r[1], r[0]))
    tsv("candidates.tsv", ("candidate", "frequency", "chapters", "first", "words", "forms"), rows)


def write_book_glossary(sections):
    """The appendix glossary, with where each term is set in bold in the chapters and how often it occurs."""
    appendix = dict(sections)["appendix"]
    part = appendix.split("## System Definitions: A Glossary", 1)[1].split("\n## ", 1)[0]
    chapters = [(cid, text) for cid, text in sections if cid != "appendix"]
    body = [(cid, "\n\n".join(paragraphs(text))) for cid, text in chapters]
    rows = []
    for term, definition in re.findall(r"(?m)^\*\*([^*]+):\*\* (.+)$", part):
        bold = [cid for cid, text in chapters if re.search(r"\*\*" + term_pattern(term) + r"\*\*", text, re.I)]
        n, spread, first = occurrences(term_pattern(term), body, re.I)
        rows.append((term, ", ".join(bold), n, spread, first, definition))
    tsv("book-glossary.tsv", ("term", "bold in", "in text", "chapters", "first", "definition"), rows)

    # Bold terms in the chapters that the appendix glossary does not define.
    defined = {t.lower() for t, *_ in rows}
    extra = []
    for cid, text in chapters:
        for b in re.findall(r"\*\*(.+?)\*\*", text):
            if len(b.split()) <= 4 and b[:1].islower() and b.lower() not in defined and not b.endswith("."):
                extra.append((cid, b))
    if extra:
        print("bold terms not in the appendix glossary:", extra)


def write_principles(sections):
    """Bold sentences of the chapters (margin principles), checked against the appendix summary of principles."""
    appendix = dict(sections)["appendix"]
    part = appendix.split("## Summary of Systems Principles", 1)[1].split("\n## ", 1)[0]
    summary = [" ".join(s.split()) for s in re.findall(r"(?m)^- (.+)$", part)]

    def norm(s):
        return re.sub(r"[^a-z]+", " ", s.lower().replace("de-coupled", "decoupled")).strip()

    keys = {norm(s): s for s in summary}
    rows, matched = [], set()
    for cid, text in sections:
        if cid == "appendix":
            continue
        for block in text.split("\n\n"):
            pieces = [plain(b) for b in re.findall(r"\*\*(.+?)\*\*", block) if len(b.split()) >= 4 and not b.isupper()]
            # A principle split by an aside in plain type ("may** (or may not, …) **make") is one principle.
            joined = []
            for b in pieces:
                if joined and b[:1].islower() and not joined[-1].endswith("."):
                    joined[-1] += " … " + b
                else:
                    joined.append(b)
            for b in joined:
                k = norm(b.replace(" … ", " "))
                if len(k.split()) < 4 or b == "How to read stock-and-flow diagrams.":  # the second is a box title
                    continue
                if k in keys:
                    match = "same"
                    matched.add(k)
                else:
                    near = [kk for kk in keys if kk[:30] in k or k[:30] in kk]
                    match = "differs: " + keys[near[0]] if near else "not in summary"
                    matched.update(near[:1])
                rows.append((cid, " ".join(b.split()), match))
    for k, s in keys.items():
        if k not in matched:
            rows.append(("appendix", s, "summary only"))
    tsv("principles.tsv", ("chapter", "principle", "appendix summary"), rows)


def clean_entity(text):
    return re.sub(r"’s$", "", re.sub(r"^[—\s]+", "", " ".join(text.split())))


def recognized(sections):
    """spaCy entities in the body text: {label: Counter((text, chapter))}."""
    import spacy
    nlp = spacy.load("en_core_web_sm")
    found = defaultdict(Counter)
    for cid, text in sections:
        for para in paragraphs(text):
            para = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", plain(para))
            for e in nlp(" ".join(para.split())).ents:
                found[e.label_][(clean_entity(e.text), cid)] += 1
    return found


def write_people(sections, entities):
    """PEOPLE with their counts, and which recognized PERSON entities belong to each."""
    listed = {row["name"] for row in csv.DictReader((OUT / "people-zh.tsv").open(), delimiter="\t")}
    missing = [name for name, _ in PEOPLE if name not in listed] + [n for n in listed if n not in dict(PEOPLE)]
    if missing:
        raise SystemExit(f"PEOPLE and people-zh.tsv differ: {missing}")
    forms, unknown = defaultdict(Counter), Counter()
    for (text, _), n in entities["PERSON"].items():
        owner = ALIASES.get(text) or next((name for name, rx in PEOPLE if re.search(rx, text)), None)
        if owner:
            forms[owner][text] += n
        elif text not in NOT_PEOPLE:
            unknown[text] += n
    if unknown:
        print("recognized as people but not in PEOPLE or NOT_PEOPLE:", dict(unknown))
    body = [(cid, "\n\n".join(paragraphs(text))) for cid, text in sections]
    rows = []
    for name, pattern in PEOPLE:
        n, spread, first = occurrences(pattern, body)
        if not n:
            raise SystemExit(f"{name}: pattern {pattern!r} finds nothing")
        seen = ", ".join(f"{t} {k}" for t, k in forms[name].most_common())
        rows.append((name, pattern, n, spread, first, seen))
    tsv("people.tsv", ("name", "pattern", "in text", "chapters", "first", "recognized as"), rows)
    others = sorted({t for (t, _) in entities["PERSON"] if t in NOT_PEOPLE})
    print("PERSON entities that are not people:", len(others))


def write_entities(sections, entities):
    """Organizations, places, works and other named entities, to check the table of names in glossary.md."""
    order = [cid for cid, _ in sections]
    rows = []
    for label in ("ORG", "GPE", "LOC", "NORP", "FAC", "EVENT", "WORK_OF_ART", "PRODUCT", "LAW"):
        per = defaultdict(Counter)
        for (text, cid), n in entities[label].items():
            per[text][cid] += n
        for text, cids in per.items():
            where = sorted(cids, key=order.index)
            rows.append((label, text, sum(cids.values()), len(where), where[0], ", ".join(where)))
    rows.sort(key=lambda r: (r[0], -r[2], r[1]))
    tsv("named-entities.tsv", ("label", "entity", "count", "chapters", "first", "sections"), rows)


def write_definitions(sections):
    """Sentences with a definition signal, and the sentences where a term is set in bold (outside the appendix)."""
    defs = []
    for cid, text in sections:
        for sentence in sentences(text):
            found = DEFINITION.search(sentence)
            bold = cid != "appendix" and any(len(b.split()) <= 4 and b[:1].islower()
                                             for b in re.findall(r"\*\*(.+?)\*\*", sentence))
            signals = [found.group(0)] if found else []
            signals += ["bold"] if bold else []
            if signals:
                defs.append((cid, "; ".join(signals), sentence))
    tsv("definitions.tsv", ("chapter", "signal", "sentence"), defs)


def write_headings(sections):
    heads = [(cid, len(m.group(1)), m.group(2)) for cid, text in sections
             for m in re.finditer(r"(?m)^(#{1,4}) (.+)$", text)]
    tsv("headings.tsv", ("chapter", "level", "heading"), heads)


# The core terms of glossary.md: English column -> (pattern, case sensitive). Counts are of the English body
# text without footnotes and headings, so ordinary uses of a word are counted too.
TERMS = {
    "system / systems": (r"\bsystems?\b", False),
    "element": (r"\belements?\b", False),
    "interconnection / interconnected": (r"\binterconnect\w*", False),
    "function / purpose": (r"\bfunctions?\b|\bpurposes?\b", False),
    "goal": (r"\bgoals?\b", False),
    "structure / system structure": (r"\bstructur\w*", False),
    "behavior / behavior over time": (r"\bbehaviou?rs?\b", False),
    "event": (r"\bevents?\b", False),
    "surprise / system surprises": (r"\bsurpris\w+", False),
    "subsystem": (r"\bsubsystems?\b", False),
    "systems thinking / systems thinker": (r"\bsystems? think(?:ing|ers?)\b", False),
    "system dynamics": (r"\bsystems? dynamics\b", False),
    "systems analysis / systems analyst": (r"\bsystems? analys[ie]s\b|\bsystems? analysts?\b", False),
    "systems zoo / zoo animal": (r"\bzoo\b", False),
    "stock": (r"\bstocks?\b", False),
    "flow / inflow / outflow": (r"\b(?:in|out)?flows?\b", False),
    "stock-and-flow diagram / structure": (r"\bstock-and-flow\b", False),
    "cloud": (r"\bclouds?\b", False),
    "bathtub / faucet / drain": (r"\bbathtubs?\b|\bfaucets?\b|\bdrains?\b", False),
    "dynamic equilibrium": (r"\bdynamic equilibrium\b", False),
    "dynamics / dynamic": (r"(?<!system )(?<!systems )\bdynamics?\b", False),
    "decoupled / de-coupled": (r"\bde-?coupl\w+", False),
    "inventory": (r"\binventor(?:y|ies)\b", False),
    "capital / capital stock": (r"\bcapital\b", False),
    "depreciation / lifetime": (r"\bdepreciat\w+|\blifetimes?\b", False),
    "renewable / nonrenewable resource": (r"\b(?:non)?renewable\b", False),
    "stock-limited / flow-limited": (r"\b(?:stock|flow)\*?-limited\b", False),
    "regeneration / extraction / harvest rate": (r"\b(?:regeneration|extraction|harvest) rates?\b", False),
    "carrying capacity": (r"\bcarrying capacit\w+", False),
    "feedback / feedback loop": (r"\bfeedbacks?\b", False),
    "balancing feedback loop / balancing loop": (r"\bbalancing (?:feedback )?loops?\b", False),
    "reinforcing feedback loop / reinforcing loop": (r"\breinforcing (?:feedback )?loops?\b", False),
    "negative / positive feedback loop": (r"\b(?:negative|positive) feedback\b", False),
    "stabilizing / runaway": (r"\bstabiliz\w+|\brunaway\b", False),
    "vicious cycle / virtuous circle": (r"\bvicious (?:cycles?|circles?)\b|\bvirtuous (?:cycles?|circles?)\b", False),
    "goal-seeking": (r"\bgoal-seeking\b", False),
    "discrepancy": (r"\bdiscrepanc(?:y|ies)\b", False),
    "exponential growth / doubling time": (r"\bexponential\w*|\bdoubling time\b", False),
    "shifting dominance": (r"\bdominan(?:ce|t)\b", False),
    "delay": (r"\bdelay(?:s|ed)?\b", False),
    "perception / response / delivery delay": (r"\b(?:perception|response|delivery) delays?\b", False),
    "oscillation": (r"\boscillat\w+", False),
    "overshoot": (r"\bovershoot\w*", False),
    "threshold": (r"\bthresholds?\b", False),
    "gain": (r"\bgain of driving loops\b", False),
    "self-correcting / self-reinforcing / self-enhancing": (r"\bself-(?:correct|reinforc|enhanc)\w*", False),
    "model": (r"\bmodel(?:s|ed|ing|ers?)?\b", False),
    "mental model": (r"\bmental models?\b", False),
    "simulation / scenario": (r"\bsimulat\w+|\bscenarios?\b", False),
    "converter": (r"\bconverters?\b", False),
    "resilience / resilient": (r"\bresilien\w+", False),
    "meta-resilience": (r"\bmeta-(?:meta-)?resilience\b", False),
    "stability / stable": (r"\bstab(?:le|ility)\b", False),
    "self-organization": (r"\bself-organi[sz]\w+", False),
    "hierarchy / hierarchical": (r"\bhierarch\w+", False),
    "suboptimization": (r"\bsuboptimi[sz]\w+", False),
    "Koch snowflake / fractal": (r"\bKoch snowflake\b|\bfractal\w*", False),
    "linear / nonlinear relationship": (r"\b(?:non)?linear\w*", False),
    "boundary": (r"\bboundar(?:y|ies)\b", False),
    "limiting factor": (r"\blimiting factors?\b", False),
    "law of the minimum": (r"\blaw of the minimum\b", False),
    "limits to growth": (r"\blimits to growth\b", False),
    "bounded rationality": (r"\bbounded rationality\b", False),
    "invisible hand / invisible foot": (r"\binvisible (?:hand|foot)\b", False),
    "archetype": (r"\barchetyp\w+", False),
    "system trap / trap": (r"\btraps?\b", False),
    "the way out": (r"(?<!on the )\bway out\b", False),
    "policy resistance": (r"\bpolicy resistance\b", False),
    "fixes that fail": (r"\bfixes that fail\b", False),
    "tragedy of the commons / commons": (r"\bcommons\b", False),
    "mutual coercion, mutually agreed upon": (r"\bmutual coercion\b", False),
    "drift to low performance": (r"\bdrift\w* (?:to|toward) low performance\b", False),
    "performance standard": (r"\bperformance standards?\b", False),
    "eroding goals": (r"\beroding goals?\b", False),
    "boiled frog syndrome": (r"\bboiled frog\b", False),
    "escalation": (r"\bescalat\w+", False),
    "success to the successful": (r"\bsuccess[- ]to[- ]the[- ]successful\b", False),
    "competitive exclusion principle": (r"\bcompetitive exclusion\b", False),
    "shifting the burden / intervenor": (r"\bshifting the burden\b|\bintervenors?\b", False),
    "addiction": (r"\baddict\w*", False),
    "rule beating": (r"\brule[- ]beat\w*", False),
    "seeking the wrong goal": (r"\bwrong goals?\b", False),
    "leverage point": (r"\bleverage points?\b", False),
    "places to intervene": (r"\bplaces? to intervene\b", False),
    "intervene / intervention": (r"\binterven(?:e|es|ed|ing|tions?)\b", False),
    "parameter / constant / numbers": (r"\bparameters?\b|\bconstants?\b", False),
    "buffer": (r"\bbuffers?\b", False),
    "information flow": (r"\binformation flows?\b", False),
    "rule": (r"\brules?\b", False),
    "paradigm / transcending paradigms": (r"\bparadigm\w*", False),
    "mind-set": (r"\bmind-?sets?\b", False),
    "intrinsic responsibility": (r"\bintrinsic responsibility\b", False),
    "time horizon": (r"\btime horizons?\b", False),
    "error-embracing": (r"\berror-embracing\b", False),
    "tyrannese": (r"\btyrannese\b", False),
    "Slinky": (r"\bSlink(?:y|ies)\b", True),
    "mess": (r"\bmess(?:es)?\b", False),
    "holistic / reductionist": (r"\b(?:un)?holistic\b|\breductionis\w+", False),
    "sustainability / sustainable": (r"\bsustainab\w+", False),
    "GNP": (r"\bGNP\b", True),
    "thermostat / furnace": (r"\bthermostats?\b|\bfurnaces?\b", False),
}


def fill_glossary(sections):
    """Count every core term of glossary.md, write its first chapter and count into the table, and list the
    first sentence it appears in (glossary-evidence.tsv)."""
    body = [(cid, "\n\n".join(paragraphs(text))) for cid, text in sections]
    lines = GLOSSARY.read_text().split("\n")
    start = lines.index("## 核心概念")
    header_at = next(i for i in range(start, len(lines)) if lines[i].startswith("|"))
    header = [c.strip() for c in lines[header_at].strip("|").split("|")]
    first_col, count_col = header.index("首次出现"), header.index("出现次数")
    evidence, seen = [], set()
    for i in range(header_at + 2, len(lines)):
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
        example = plain(next(s for s in sentences(dict(sections)[first]) if rx.search(s)))
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
    write_book_glossary(sections)
    write_principles(sections)
    entities = recognized(sections)
    write_people(sections, entities)
    write_entities(sections, entities)
    write_definitions(sections)
    write_headings(sections)
    if "## 核心概念" in GLOSSARY.read_text():
        fill_glossary(sections)


if __name__ == "__main__":
    main(sys.argv[1])
