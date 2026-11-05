"""Term statistics before translating (see review/terms/README.md).

    uv run --with pymupdf python -I books/how-big-things-get-done/tools/term_stats.py book.pdf candidates.json
    uv run --with pymupdf python -I books/how-big-things-get-done/tools/term_stats.py --glossary

candidates.json comes from en-zh-translation-polish's terms.py, run on the English text without footnotes.
The first form writes review/terms/: candidates.tsv, index-terms.tsv, people.tsv, definitions.tsv, headings.tsv.
The print index is read from the PDF (pp. 243 to 258): calibre kept its entries but turned the page numbers
into links named ref1, ref2, ...; each link points at the page it refers to, so the script counts the links
and maps their target pages to sections through the PDF outline.

The second form (--glossary) counts the glossary terms listed in GLOSSARY below, writes
review/terms/glossary-evidence.tsv and fills the columns 首次出现 and 出现次数 of the tables in glossary.md.
"""

import csv
import json
import re
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
OUT = BOOK / "review" / "terms"
INDEX_PAGES = range(242, 258)  # 0-based pages of the print index
MAIN_X, SUB_X = 77, 88  # x of an index heading and of a sub entry or continuation line
DEFINITION = re.compile(
    r"\b(?:call(?:s|ed|ing)?\b[^.?!]{0,100}[“‘]|known as|dubbed|coined|the term|a term|so-called|referred to as|nicknamed|"
    r"named after|stands for|short for|the phrase|defined as|invented “|propose ‘|what (?:\w+ )?calls?\b)")
# Index headings with a comma that are places or things, not "Surname, Given names".
NOT_PEOPLE = re.compile(
    r"\b(Agency|Airport|Authority|Building|Center|Concert|Department|Fish|Games|hotel|House|Museum|nightclub|"
    r"Partners|Project|project|Railway|Service|Stadium|Street|Studios|System|system|Terminal|Tower|Tunnel|tunnel|"
    r"Barrier|Mahal|Colosseum|Capitol|Parliament|Planet|Vestas|SNCF|DONG|MTR|XRL|HS2|BPEP|Association|"
    r"Inc|LLC|Corporation|University|Company|The)\b")
PLACES = {"Japan", "Australia", "San Francisco", "Nepal", "Spain", "Nigeria", "Massachusetts", "Germany", "China",
          "California", "Washington", "Washington, D.C.", "DC", "D.C.", "New York", "New York City", "Rome", "Paris",
          "United Kingdom", "Denmark", "Hong Kong", "Switzerland", "Barcelona", "Scotland", "Colombia", "France",
          "India", "Seattle", "Los Angeles", "North Carolina", "Olympic Games in", "US Department of"}
# People the index lists under one name, without a comma.
SINGLE_NAMES = {"Adele", "Aristotle", "Jay-Z"}

# Glossary terms: (English label as written in the first column of glossary.md, pattern, case sensitive).
# Counts are matches in the text without footnotes, headings included; first is the first section with a match.
GLOSSARY = [
    ("megaproject", r"\bmegaprojects?\b", False),
    ("big project / big thing", r"\bbig projects?\b|\bbig things?\b", False),
    ("Iron Law of Megaprojects / Iron Law", r"\bIron Law\b", True),
    ("over budget, over time, under benefits, over and over again", r"\bover budget, over time\b", False),
    ("on budget / on time / on benefits", r"\bon (?:budget|time|benefits?)\b", False),
    ("cost overrun / schedule overrun", r"\boverruns?\b", False),
    ("benefit shortfall", r"\bbenefits? shortfalls?\b|\bunder benefits\b", False),
    ("estimate / forecast", r"\bestimat(?:e|es|ed|ing|ion)\b|\bforecast(?:s|ed|ing|er|ers)?\b", False),
    ("think slow, act fast / think fast, act slow", r"\bthink (?:slow|fast), act (?:fast|slow)\b", False),
    ("planning / delivery", r"\bplanning\b|\bdelivery\b", False),
    ("plan / planner", r"\bplans?\b|\bplanners?\b", False),
    ("window of doom / window", r"\bwindow of doom\b|\b(?:open|time) window\b|\bthe window\b", False),
    ("Make haste slowly / festina lente", r"\bhaste\W+slowly\b|\bfestina lente\b", False),
    ("Projects don’t go wrong, they start wrong", r"\bstart(?:s|ed)?\*? wrong\b", False),
    ("honest numbers", r"\bhonest numbers\b", False),
    ("black swan / black swan management", r"\bblack swans?\b", False),
    ("normal distribution / bell curve", r"\bnormal distributions?\b|\bbell curves?\b|\bGaussian\b", False),
    ("fat tail / fat-tailed", r"\bfat[- ]tail(?:s|ed)?\b", False),
    ("thin-tailed", r"\bthin[- ]tail(?:s|ed)?\b", False),
    ("tail", r"\btails?\b", False),
    ("regression to the mean / regression to the tail", r"\bregression to the (?:mean|tail)\b", False),
    ("power law", r"\bpower[- ]laws?\b", False),
    ("normal accidents", r"\bnormal accidents?\b", False),
    ("break-fix cycle", r"\bbreak-fix\b", False),
    ("commitment fallacy", r"\bcommitment fallacy\b", False),
    ("lock-in / lock in", r"\block(?:s|ed|ing)?[- ]in\b", False),
    ("escalation of commitment", r"\bescalation of commitment\b", False),
    ("rush to commit", r"\brush to commit", False),
    ("Commit to not commit", r"\bcommit to not commit", False),
    ("optimism / optimism bias", r"\boptimis(?:m|t|ts|tic|tically)\b", False),
    ("planning fallacy / planning fallacy writ large", r"\bplanning fallacy\b", False),
    ("Hofstadter’s Law", r"\bHofstadter’s Law\b", False),
    ("bias for action / bias against thinking", r"\bbias (?:for action|against thinking)\b", False),
    ("strategic misrepresentation", r"\bstrategic(?:ally)? misrepresent", False),
    ("psychology and power", r"\bpsychology and power\b|\bpsychology (?:and|or) politics\b|\b(?:power|political) bias\b", False),
    ("bias / cognitive bias / behavioral bias", r"\bbias(?:es|ed)?\b", False),
    ("System One / System Two", r"\bSystems? (?:One|Two|1|2)\b", True),
    ("WYSIATI (What You See Is All There Is)", r"\bWYSIATI\b", True),
    ("snap judgment / intuitive judgment", r"\b(?:snap|intuitive) judgments?\b", False),
    ("sunk cost / sunk-cost fallacy", r"\bsunk[- ]costs?\b", False),
    ("Start digging a hole", r"\bstart digging a hole\b", False),
    ("Driving into the Blizzard", r"\bblizzard\b", False),
    ("Somervell’s Spiral", r"\bSomervell’s Spiral\b|\bspiral downward\b", False),
    ("think from right to left", r"\bright to left\b", False),
    ("the box on the right", r"\bbox(?:es)? on the (?:right|left)\b", False),
    ("Why?", r"\bwhy\?", False),
    ("means and ends", r"\bmeans and ends\b|\bends and means\b", False),
    ("backcasting", r"\bbackcasting\b", False),
    ("working backwards / PR/FAQ", r"\bwork(?:ing|s|ed)? backwards?\b|\bPR/FAQs?\b|\bPR and FAQ\b", False),
    ("Pixar planning", r"\bPixar planning\b", False),
    ("experiri", r"\bexperiri\b", False),
    ("experience / experienced", r"\bexperience[ds]?\b", False),
    ("experiment / experimentation / testing", r"\bexperiment(?:s|ed|ing|ation|al)?\b|\btest(?:s|ed|ing)?\b", False),
    ("experiential learning", r"\bexperiential learning\b", False),
    ("iteration / iterate", r"\biterat(?:e|es|ed|ing|ion|ions|ive)\b", False),
    ("simulation / simulate", r"\bsimulat(?:e|es|ed|ing|ion|ions)\b", False),
    ("digital twin / CATIA", r"\bdigital twins?\b|\bCATIA\b", False),
    ("maximum virtual product", r"\bmaximum virtual product\b", False),
    ("minimum viable product (MVP) / lean startup", r"\bminimum viable products?\b|\bMVP\b|\blean startup\b", False),
    ("brain trust", r"\bbrain ?trust\b", False),
    ("illusion of explanatory depth", r"\billusion of explanatory depth\b", False),
    ("learning curve / positive learning / negative learning", r"\blearning curves?\b|\b(?:positive|negative) learning\b", False),
    ("uniqueness bias / unique", r"\buniqueness\b|\bunique\b", False),
    ("Eternal Beginner Syndrome", r"\bEternal Beginner\b", False),
    ("frozen experience / unfrozen", r"\b(?:un)?frozen\b", False),
    ("tacit knowledge", r"\btacit\b", False),
    ("phronesis / practical wisdom", r"\bphronesis\b|\bpractical wisdom\b", False),
    ("masterbuilder", r"\bmasterbuilders?\b", False),
    ("one-building architect", r"\bone-building architect\b", False),
    ("reference-class forecasting (RCF)", r"\breference[- ]class forecast(?:s|ing)?\b|\bRCF\b", False),
    ("reference class", r"\breference class(?:es)?\b", False),
    ("outside view / inside view", r"\b(?:outside|inside) view\b", False),
    ("one of those", r"\bone of those\b", False),
    ("anchoring and adjustment / anchor", r"\banchor(?:s|ed|ing)?\b", False),
    ("base rate", r"\bbase rates?\b", False),
    ("availability bias", r"\bavailability\b", False),
    ("survivorship bias", r"\bsurvivorship\b", False),
    ("mean / average", r"\bmean (?:cost|overrun|risk|of|for|is|was|value)\b|\baverages?\b", False),
    ("unknown unknowns", r"\bunknown unknowns?\b", False),
    ("risk mitigation / mitigate", r"\bmitigat(?:e|es|ed|ing|ion)\b", False),
    ("contingency / reserve", r"\bcontingenc(?:y|ies)\b|\breserves?\b", False),
    ("buffer", r"\bbuffers?\b", False),
    ("in real terms / final investment decision / business case", r"\bin real terms\b|\bfinal investment decision\b|\bbusiness cases?\b", False),
    ("nuclear storage / water projects", r"\bnuclear storage\b|\bwater projects?\b", False),
    ("inchstone / milestone", r"\binchstones?\b|\bmilestones?\b", False),
    ("Hiding Hand / providential ignorance", r"\bHiding Hand\b|\bprovidential ignorance\b", False),
    ("ignorance / ignorant", r"\bignoran(?:ce|t)\b", False),
    ("Hero’s Journey", r"\bHero’s Journey\b", False),
    ("opportunity cost", r"\bopportunity costs?\b", False),
    ("single, determined organism", r"\bdetermined organism\b", False),
    ("team / integrated team", r"\bteams?\b", False),
    ("psychological safety", r"\bpsychological safety\b", False),
    ("design for manufacture and assembly", r"\bdesign for manufactur", False),
    ("modularity / modular", r"\bmodular(?:ity)?\b", False),
    ("Lego", r"\bLegos?\b", True),
    ("scale-free scalability / scale up", r"\bscale-free\b|\bscal(?:e|ed|es|ing) up\b|\bscalab", False),
    ("one huge thing / many small things", r"\bone huge thing\b|\bmany small things\b", False),
    ("repetition / repeat", r"\brepeat(?:s|ed|ing)?\b|\brepetitions?\b", False),
    ("bespoke / bespokeness", r"\bbespoke(?:ness)?\b", False),
    ("heuristic", r"\bheuristics?\b", False),
    ("leadership / project leader", r"\bleadership\b|\bproject leaders?\b", False),
    ("climate crisis / climate change", r"\bclimate (?:crisis|change|mitigation)\b", False),
    ("renewable energy / wind power / solar power", r"\brenewables?\b|\bwind (?:power|farms?|turbines?|energy)\b|\bsolar\b", False),
    ("high-speed rail", r"\bhigh-speed rail\b", False),
    ("IT project", r"\bIT projects?\b", True),
    ("tunnel-boring machine", r"\bboring machines?\b|\bborers?\b", False),
    ("contractor", r"\bcontractors?\b", False),
    ("Flyvbjerg Database", r"\bFlyvbjerg Database\b|\bmy database\b|\bour database\b", False),
    ("Empty State Building", r"\bEmpty State\b", False),
]


def body_sections():
    """[(chapter id, text without footnotes)] in book order."""
    config = json.loads((BOOK / "book.json").read_text())
    out = []
    for c in config["chapters"]:
        text = (BOOK / "en" / c["file"]).read_text()
        text = re.sub(r"(?m)^\[\^\d+\]: .*\n?", "", text)
        out.append((c["id"], re.sub(r"\[\^\d+\]", "", text)))
    return out


def fix_mojibake(text):
    try:
        return text.encode("cp1252").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text


def page_sections(doc):
    """0-based page number -> chapter id (or the name of a dropped section), from the PDF outline."""
    config = json.loads((BOOK / "book.json").read_text())
    heads = {}
    for c in config["chapters"]:
        first = (BOOK / "en" / c["file"]).read_text().split("\n", 1)[0]
        heads[first[2:].strip()] = c["id"]
    starts = []
    for _, title, page in doc.get_toc():
        title = fix_mojibake(title)
        cid = heads.get(title) or next((v for k, v in heads.items() if title.startswith(k)), None)
        starts.append((page - 1, cid or title.lower()))
    out = {}
    for i, (start, cid) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else doc.page_count
        for p in range(start, end):
            out[p] = cid
    return out


def index_entries(pdf_path):
    """[(heading, [target sections of its page links], sub entries, see also)] from the print index."""
    import pymupdf

    doc = pymupdf.open(pdf_path)
    sections = page_sections(doc)
    entries, current, last_open = [], None, False
    for pno in INDEX_PAGES:
        page = doc[pno]
        links = [k for k in page.get_links() if k.get("kind") == pymupdf.LINK_GOTO]
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                text = "".join(s["text"] for s in line["spans"]).strip()
                x = round(line["bbox"][0])
                if not text or text == "INDEX":
                    continue
                box = pymupdf.Rect(line["bbox"])
                targets = [sections.get(k["page"], "?") for k in links
                           if box.y0 <= (k["from"].y0 + k["from"].y1) / 2 <= box.y1]
                see = re.search(r"\(see (?:also )?(.*)\)$", text)
                if see:  # a cross reference: its link points at another index entry, not at the text
                    targets, text = [], text[:see.start()].strip()
                head = re.split(r",\s*ref\d", text)[0].strip().rstrip(",")
                more_refs = bool(re.match(r"ref\d", text))
                if (more_refs or last_open) and current is not None:
                    target = current[2][-1] if current[2] and x > SUB_X else None
                    if not more_refs:
                        (target if target is not None else current)[0] += " " + head
                    (target[1] if target is not None else current[1]).extend(targets)
                elif see and not text:
                    current[3].append(see[1])
                elif x <= MAIN_X:
                    current = [head, targets, [], [see[1]] if see else []]
                    entries.append(current)
                else:
                    current[2].append([head, targets])
                last_open = bool(text) and not see and not re.search(r"ref\d+,?$|\)$", text)
    out = []
    for head, targets, subs, see in entries:
        refs = targets + [t for _, ts in subs for t in ts]
        out.append((head, refs, [s for s, _ in subs], see))
    return out


def person(head):
    """'Auken, Svend' -> 'Svend Auken'; 'Bilbao, Spain' and 'airports' -> None."""
    head = re.sub(r", further readings by$", "", head)
    if head in SINGLE_NAMES:
        return head
    found = re.fullmatch(r"([A-ZÀ-ÞØ][\w’'.-]+(?: (?:[A-ZÀ-ÞØ][\w’'.-]+|del|de|von|van))*), "
                         r"((?:Sir |Emperor|Queen)?[A-ZÀ-ÞØ][\w’'.-]*(?: [\w’'.-]+)*)", head)
    if not found or NOT_PEOPLE.search(found[1]) or found[2] in PLACES or found[2] == "The":
        return None
    last, first = found.groups()
    if first.startswith(("Emperor", "Queen")):  # "Caesar Augustus, Emperor", "Elizabeth II, Queen of England"
        return last
    if " " in first and first.split()[-1] in ("von", "van", "de"):
        return f"{first.rsplit(' ', 1)[0]} {first.split()[-1]} {last}"
    return f"{first} {last}"


def occurrences(pattern, sections, flags=0):
    rx = re.compile(pattern, flags)
    counts = [(cid, len(rx.findall(text))) for cid, text in sections]
    hits = [(cid, n) for cid, n in counts if n]
    return sum(n for _, n in hits), len(hits), hits[0][0] if hits else ""


def tsv(name, header, rows):
    lines = ["\t".join(header)] + ["\t".join(str(x) for x in row) for row in rows]
    (OUT / name).write_text("\n".join(lines) + "\n")
    print(f"{name}: {len(rows)} rows")


def in_order(targets, order):
    seen = [t for t in order if t in targets]
    other = sorted({t for t in targets if t not in order})
    return ", ".join(seen + other)


def main(pdf_path, candidates_path):
    OUT.mkdir(parents=True, exist_ok=True)
    sections = body_sections()
    order = [cid for cid, _ in sections]
    ids = {Path(c["file"]).name: c["id"] for c in json.loads((BOOK / "book.json").read_text())["chapters"]}

    data = json.loads(Path(candidates_path).read_text())["english"]
    rows = []
    for c in data:
        docs = {ids.get(Path(d).name, Path(d).name): n for d, n in c["documents"].items()}
        first = next((cid for cid in order if cid in docs), "")
        forms = ", ".join(f"{f} {n}" for f, n in sorted(c["forms"].items(), key=lambda x: -x[1])[:3])
        rows.append((c["candidate"], c["frequency"], len(docs), first, len(c["candidate"].split()), forms))
    rows.sort(key=lambda r: (-r[1], r[0]))
    tsv("candidates.tsv", ("candidate", "frequency", "chapters", "first", "words", "forms"), rows)

    people, terms = [], []
    for head, refs, subs, see in index_entries(pdf_path):
        name = person(head)
        where = in_order(refs, order)
        if name:
            last = name.split()[-1]
            n, chapters, first = occurrences(rf"\b{re.escape(last)}\b", sections)
            people.append((name, head, len(refs), where, n, chapters, first))
        else:
            key = re.sub(r" \([^)]*\)$", "", head).strip("“”").rstrip(",")
            inverted = re.fullmatch(r"([^,]+), ([a-z][^,]* (?:of|from|to)|ending)", key)  # "commitment, escalation of"
            key = f"{inverted[2]} {inverted[1]}" if inverted else key.split(", ")[0]
            named = key[:1].isupper() or key[:1].isdigit()
            n, chapters, first = occurrences(rf"\b{re.escape(key)}\b", sections, 0 if named else re.I)
            terms.append((head, "named" if named else "concept", len(refs), where, n, chapters, first,
                          "; ".join(subs), "; ".join(see)))
    tsv("people.tsv", ("name", "index heading", "index refs", "ref sections", "surname in text", "chapters",
                       "first"), people)
    tsv("index-terms.tsv", ("index heading", "kind", "index refs", "ref sections", "in text", "chapters", "first",
                            "sub entries", "see also"), terms)

    defs = []
    for cid, text in sections:
        for block in text.split("\n\n"):
            if block.startswith("#") or block.startswith("!["):
                continue
            for sentence in re.split(r"(?<=[.?!”])\s+(?=[A-Z“])", block):
                found = DEFINITION.search(sentence)
                if found:
                    defs.append((cid, found.group(0), " ".join(sentence.split())))
    tsv("definitions.tsv", ("chapter", "signal", "sentence"), defs)

    heads = [(cid, len(line.split(" ", 1)[0]), line.split(" ", 1)[1])
             for cid, text in sections for line in text.split("\n") if re.match(r"#{1,3} ", line)]
    tsv("headings.tsv", ("chapter", "level", "heading"), heads)


def glossary():
    """Count GLOSSARY in the body text and headings; write glossary-evidence.tsv and fill 首次出现 and 出现次数."""
    sections = body_sections()
    path = BOOK / "glossary.md"
    lines = path.read_text().split("\n")
    rows = {}
    header = None
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("|") else None
        if cells and "首次出现" in cells:
            header = cells
        elif not cells:
            header = None
        elif header and not set(cells[0]) <= set("- ") and cells[0]:
            rows[cells[0]] = (i, cells, header)
    evidence = []
    for label, pattern, case in GLOSSARY:
        rx = re.compile(pattern, 0 if case else re.I)
        n, chapters, first = occurrences(pattern, sections, 0 if case else re.I)
        example = heading = ""
        for cid, text in sections:
            if cid != first:
                continue
            for block in text.split("\n\n"):
                if not rx.search(block):
                    continue
                if block.startswith("#"):
                    heading = heading or block.lstrip("# ")
                    continue
                sentences = re.split(r"(?<=[.?!”])\s+(?=[A-Z“])", block)
                example = next((s for s in sentences if rx.search(s)), block)
                break
        example = " ".join((example or heading).split())
        if label not in rows:
            print(f"not in glossary.md: {label}")
            continue
        i, cells, head = rows.pop(label)
        cells[head.index("首次出现")] = first or "无"
        cells[head.index("出现次数")] = str(n)
        lines[i] = "| " + " | ".join(cells) + " |"
        evidence.append((label, cells[1], first, n, chapters, example, cells[head.index("状态")] if "状态" in head else ""))
    for label in rows:
        print(f"no pattern for glossary row: {label}")
    path.write_text("\n".join(lines))
    with (OUT / "glossary-evidence.tsv").open("w", newline="") as f:
        out = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar="\\")
        out.writerow(("term", "chinese", "first", "count", "chapters", "example", "decided by"))
        for label, chinese, first, n, chapters, example, status in evidence:
            out.writerow((label, chinese, first, n, chapters, example, f"Claude（{status or '初定'}）"))
    print(f"glossary-evidence.tsv: {len(evidence)} rows")


if __name__ == "__main__":
    if sys.argv[1:2] == ["--glossary"]:
        glossary()
    else:
        main(*sys.argv[1:3])
