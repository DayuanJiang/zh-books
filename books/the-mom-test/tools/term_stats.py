"""Term statistics before translating (see review/terms/README.md).

    $PY -I books/the-mom-test/tools/term_stats.py candidates.json

$PY is a Python with spaCy 3.8 and en_core_web_sm (the environment for en-zh-translation-polish's terms.py).
candidates.json comes from terms.py, run on a copy of en/ without footnote definitions.

The book has no print index. Names come from spaCy's named entities (entities.tsv), checked by hand into
people-zh.tsv; people.tsv counts each person in the text.
Writes review/terms/: candidates.tsv, entities.tsv, people.tsv, definitions.tsv, headings.tsv, repeats.tsv,
glossary-evidence.tsv. Fills the 首次出现 and 出现次数 columns of the core table in glossary.md.
"""

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
OUT = BOOK / "review" / "terms"
DEFINITION = re.compile(
    r"\b(we call|I call|what I call|is called|are called|called|known as|refer to|referred to as|so-called|"
    r"the term|the phrase|stands for|short for|aka|i\.e\.|e\.g\.|in other words|is the tendency|"
    r"is when|it’s when|means|the mnemonic|so to speak|calls? (?:them|it|this)|types of|comes? in (?:\d|two|three)|"
    r"key elements|has (?:\d|two|three) parts|the major currencies)(?!\w)", re.I)
LIST_DEFINITION = re.compile(r"^\s*[-*] (?:\*\*)?[A-Z][\w ]{2,30}(?:\*\*)? — ")
ENTITY_LABELS = {"PERSON", "ORG", "GPE", "LOC", "NORP", "PRODUCT", "WORK_OF_ART", "EVENT", "FAC", "LAW", "LANGUAGE"}
NOT_A_SURNAME = {"Read", "C"}  # "Read the news", "customer C"

# (label in glossary.md, English pattern, case sensitive): the counts in the core table come from these.
COUNTS = [
    ("The Mom Test", r"\bmom test\b", False),
    ("customer conversation", r"\bcustomer conversations?\b", False),
    ("Customer Development", r"\bCustomer Development\b", True),
    ("Lean Startup", r"\bLean Startup\b", True),
    ("Design Thinking / User Experience (UX)", r"\bDesign Thinking\b|\bUser Experience\b|\bUX\b", True),
    ("learning (n.) / customer learning", r"\blearnings?\b", False),
    ("bad data", r"\bbad data\b", False),
    ("compliment", r"\bcompliment", False),
    ("fishing for compliments", r"\bfish(?:ing)? for compliments\b", False),
    ("fluff / fluffy", r"\bfluff", False),
    ("generic / generics", r"\bgenerics?\b", False),
    ("hypothetical", r"\bhypothetical", False),
    ("specifics in the past", r"\bspecifics in the past\b", False),
    ("opinion", r"\bopinions?\b", False),
    ("idea", r"\bideas?\b", False),
    ("deflect", r"\bdeflect", False),
    ("anchor", r"\banchor", False),
    ("dig / dig beneath", r"\bdig(?:s|ging)?\b", False),
    ("feature request", r"\bfeature requests?\b", False),
    ("feature creep", r"\bfeature[- ]creep\b", False),
    ("killer feature / must-have", r"\bkiller feature\b|\bmust-have\b", False),
    ("approval / seeking approval", r"\bapproval", False),
    ("The Pathos Problem", r"\bPathos Problem\b", True),
    ("ego", r"\bego\b", False),
    ("pitch / pitching / pitch mode / pitchy", r"\bpitch", False),
    ("false positive / false negative", r"\bfalse (?:positive|negative)s?\b", False),
    ("signal", r"\bsignals?\b", False),
    ("lukewarm", r"\blukewarm\b", False),
    ("zoom / premature zoom", r"\bzoom", False),
    ("the elephant (in the room)", r"\belephant\b", False),
    ("failure point", r"\bfailure points?\b", False),
    ("de-risk", r"\bde-risk", False),
    ("product risk / market risk", r"\b(?:product|market) risks?\b", False),
    ("must-solve problem / nice-to-have", r"\bmust-solve\b|\bnice-to-have\b", False),
    ("painkiller / vitamin", r"\bpainkiller\b|\bvitamin\b", False),
    ("3 big questions / list of 3",
     r"\b(?:3|three) (?:big |most important )?questions\b|\blist of 3\b|\bbig 3\b|\bnext 3\b", False),
    ("Keeping it casual", r"\bkeep(?:ing|s)? it casual\b", False),
    ("The Meeting Anti-Pattern", r"\banti-pattern\b", False),
    ("meeting", r"\bmeetings?\b", False),
    ("formal / formality", r"\bformal\w*|\bover-formalise\b", False),
    ("commitment / commit", r"\bcommit", False),
    ("advancement / advance", r"\badvanc", False),
    ("promise", r"\bpromise", False),
    ("next steps", r"\bnext steps?\b", False),
    ("currency", r"\bcurrenc", False),
    ("reputation risk", r"\breputation", False),
    ("letter of intent / pre-order / deposit", r"\bletter of intent\b|\bpre-order|\bpre-purchase\b|\bdeposit\b", False),
    ("lead (n.) / zombie leads",
     r"\b(?:zombie|dead|real|cold|qualified|promising|sales|great|possible|your) leads?\b|\ba lead\b", False),
    ("friend-zoned", r"\bfriend-zone", False),
    ("funnel / pipeline", r"\bfunnel\b|\bpipeline\b", False),
    ("stalling tactic", r"\bstall", False),
    ("earlyvangelists", r"\bearlyvangelists?\b|\bearly evangelists?\b", False),
    ("first customers / early customers / crazy customers", r"\b(?:first|early|crazy) customers?\b(?! conversations?| meetings?)", False),
    ("customer segment / segment", r"\bsegments?\b", False),
    ("segmentation", r"\bsegmentation\b", False),
    ("Customer Slicing / slice", r"\bslic(?:e|es|ed|ing)\b", False),
    ("who-where pair", r"\bwho-where\b", False),
    ("demographic", r"\bdemographic", False),
    ("workaround", r"\bworkarounds?\b", False),
    ("makeshift / home-brew / duct-tape solution", r"\bmakeshift\b|\bhome-brew\b|\bduct-tape\b|\bcobbled together\b", False),
    ("pain", r"\bpains?\b", False),
    ("budget / budget owner", r"\bbudget", False),
    ("decision maker / stakeholders", r"\bdecision makers?\b|\bstakeholders?\b", False),
    ("purchasing process / buying criteria", r"\b(?:purchas|buy)ing (?:process|criteria)\b", False),
    ("enterprise / B2B / consumer", r"\benterprise\b|\bB2B\b|\bconsumers?\b", False),
    ("intro / warm intro", r"\bintros?\b", False),
    ("cold (calls, emails, conversations, approaches)", r"\bcold\b", False),
    ("serendipity / serendipitous", r"\bserendip", False),
    ("landing page", r"\blanding pages?\b", False),
    ("framing / frame", r"\bfram(?:e|ed|es|ing)\b", False),
    ("Vision / Framing / Weakness / Pedestal / Ask", r"\bpedestal\b|\bweakness\b|\bVery Few Wizards\b", False),
    ("advisor / the advisory flip", r"\badvis(?:or|ory)", False),
    ("opportunity cost", r"\bopportunity cost\b", False),
    ("learning bottleneck", r"\bbottleneck", False),
    ("prepping / reviewing", r"\bprep(?:ping|s)?\b|\breview(?:ing|s)?\b", False),
    ("notes / signal symbols", r"\bnotes?\b|\bsymbols?\b", False),
    ("job-to-be-done", r"\bjob-to-be-done\b", False),
    ("going through the motions", r"\bgoing through the motions\b", False),
    ("desk research", r"\bdesk research\b", False),
    ("validation / validate", r"\bvalidat", False),
    ("visionary leap", r"\bleap\b", False),
    ("Rule of thumb", r"\bRule of thumb\b", False),
    ("hack", r"\bhack(?:s|ed)?\b", False),
    ("founder / entrepreneur / startup", r"\bfounders?\b|\bentrepreneur\w*|\bstartups?\b", False),
    ("customer / user", r"\bcustomers?\b|\busers?\b", False),
    ("business", r"\bbusiness(?:es)?\b", False),
    ("industry expert", r"\bindustry experts?\b", False),
    ("dealflow", r"\bdealflow\b", False),
    ("case study / testimonial", r"\bcase stud(?:y|ies)\b|\btestimonial\b", False),
    ("trial / prototype / alpha users / beta keys", r"\btrials?\b|\bprototypes?\b|\balpha users\b|\bbeta keys\b", False),
    ("local maximum", r"\blocal maximum\b", False),
    ("thought experiment", r"\bthought experiments?\b", False),
    ("meetup / office hours / happy hour", r"\bmeet-?ups?\b|\boffice hours\b|\bhappy hour\b", False),
    ("mom-and-pop / SMEs / e-tailers / creative agencies",
     r"\bmom[- ](?:and|&)[- ]pop\b|\bSMEs\b|\be-tailers\b|\bcreative agenc", False),
    ("Inbox 0", r"\bInbox 0\b", False),
    ("7 degrees of separation", r"\b7 degrees\b", False),
    ("Gordian Knot", r"\bGordian Knot\b|(?<!double-)\bknot\b", False),
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


def plain(text):
    """Markdown to running text: no markers, emphasis, link targets or quote signs."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"(?m)^\s*(?:#+|>|[-*]|\d+\.)\s?", "", text)
    return text.replace("**", "").replace("*", "")


def sentences(text):
    for block in text.split("\n\n"):
        if block.startswith("#"):
            yield block.strip()
            continue
        for line in block.split("\n") if re.match(r"\s*([-*]|\d+\.) ", block) else [block]:
            for sentence in re.split(r"(?<!e\.g\.)(?<!i\.e\.)(?<=[.?!”])\s+(?=[A-Z“*])", line):
                if sentence.strip():
                    yield " ".join(sentence.split())


def occurrences(rx, sections):
    counts = [(cid, len(rx.findall(text))) for cid, text in sections]
    hits = [(cid, n) for cid, n in counts if n]
    return sum(n for _, n in hits), len(hits), hits[0][0] if hits else ""


def tsv(name, header, rows):
    lines = ["\t".join(header)] + ["\t".join(str(x) for x in row) for row in rows]
    (OUT / name).write_text("\n".join(lines) + "\n")
    print(f"{name}: {len(rows)} rows")


def person_pattern(name, names):
    """Full name, surname, or a given name no one else in the list has; single names not followed by a surname."""
    parts = re.sub(r"^(?:[A-Z]\. )+", "", name).split()
    if parts == [name]:
        return rf"\b{re.escape(name)}\b(?! [A-Z][a-z])"
    givens = Counter(n.split()[0] for n in names)
    options = [re.escape(name)]
    if parts[-1] not in NOT_A_SURNAME:
        options.append(re.escape(parts[-1]))
    if len(parts) > 1 and givens[parts[0]] == 1:
        options.append(re.escape(parts[0]))
    return r"\b(?:" + "|".join(options) + r")\b"


def candidates(path, sections, ids):
    data = json.loads(Path(path).read_text())["english"]
    rows = []
    for c in data:
        docs = {ids.get(Path(d).name, Path(d).name): n for d, n in c["documents"].items()}
        first = next((cid for cid, _ in sections if cid in docs), "")
        forms = ", ".join(f"{f} {n}" for f, n in sorted(c["forms"].items(), key=lambda x: -x[1])[:3])
        rows.append((c["candidate"], c["frequency"], len(docs), first, len(c["candidate"].split()), forms))
    rows.sort(key=lambda r: (-r[1], r[0]))
    tsv("candidates.tsv", ("candidate", "frequency", "chapters", "first", "words", "forms"), rows)


def entities(sections):
    import spacy

    nlp = spacy.load("en_core_web_sm")
    found = {}
    for cid, text in sections:
        for ent in nlp(plain(text)).ents:
            name = " ".join(ent.text.split()).strip("“”\"'’ ")
            if ent.label_ not in ENTITY_LABELS or not re.search(r"[A-Za-z]", name):
                continue
            row = found.setdefault((name, ent.label_), [0, [], cid])
            row[0] += 1
            if cid not in row[1]:
                row[1].append(cid)
    rows = [(name, label, n, len(chs), first) for (name, label), (n, chs, first) in found.items()]
    rows.sort(key=lambda r: (r[1], -r[2], r[0]))
    tsv("entities.tsv", ("entity", "label", "count", "chapters", "first"), rows)


def people(sections):
    names = [row["name"] for row in csv.DictReader((OUT / "people-zh.tsv").open(), delimiter="\t")]
    rows = []
    for name in names:
        rx = re.compile(person_pattern(name, names))
        n, chapters, first = occurrences(rx, sections)
        rows.append((name, rx.pattern, n, chapters, first))
    tsv("people.tsv", ("name", "pattern", "mentions", "chapters", "first"), rows)


def definitions(sections):
    rows = []
    for cid, text in sections:
        for line in text.split("\n"):
            if LIST_DEFINITION.match(line):
                rows.append((cid, "list item —", " ".join(plain(line).split())))
        for sentence in sentences(text):
            found = DEFINITION.search(sentence)
            if found and not sentence.startswith("#"):
                rows.append((cid, found.group(0), plain(sentence).strip()))
    tsv("definitions.tsv", ("chapter", "signal", "sentence"), rows)


def headings(sections):
    rows = [(cid, len(m.group(1)), m.group(2)) for cid, text in sections
            for m in re.finditer(r"(?m)^(#{1,6}) (.+)$", text)]
    tsv("headings.tsv", ("chapter", "level", "heading"), rows)


def repeats(sections):
    """Paragraphs, quotes and list items that occur more than once: translate them the same way every time."""
    seen = {}
    for cid, text in sections:
        for block in text.split("\n\n"):
            lines = block.split("\n") if re.match(r"\s*([-*]|\d+\.) ", block) else [block]
            for line in lines:
                key = " ".join(re.sub(r"^\s*(?:[-*]|\d+\.|>|#+)\s+", "", line).split())
                if len(key.split()) >= 2:
                    seen.setdefault(key, []).append(cid)
    rows = [(key, len(places), ", ".join(places)) for key, places in seen.items() if len(places) > 1]
    tsv("repeats.tsv", ("text", "count", "places"), rows)


def glossary(sections):
    """glossary-evidence.tsv, and the counts in the core table of glossary.md."""
    path = BOOK / "glossary.md"
    lines = path.read_text().split("\n")
    stats, rows = {}, []
    for label, pattern, case in COUNTS:
        rx = re.compile(pattern, 0 if case else re.I)
        n, chapters, first = occurrences(rx, sections)
        hits = [s for cid, text in sections if cid == first for s in sentences(text) if rx.search(s)]
        example = next((s for s in hits if not s.startswith("#")), hits[0] if hits else "")
        stats[label] = (n, first, plain(example).strip())
    in_core = False
    for i, line in enumerate(lines):
        if line.startswith("## "):
            in_core = line == "## 核心概念"
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not in_core or not line.startswith("| ") or len(cells) != 7 or cells[0] in ("英文", "---"):
            continue
        label = cells[0]
        if label not in stats:
            sys.exit(f"glossary.md: no pattern in COUNTS for {label!r}")
        n, first, example = stats.pop(label)
        cells[4], cells[5] = first, str(n)
        lines[i] = "| " + " | ".join(cells) + " |"
        rows.append((label, cells[1], first, example, "Claude（初定）"))
    if stats:
        sys.exit(f"COUNTS has labels missing from glossary.md: {sorted(stats)}")
    path.write_text("\n".join(lines))
    tsv("glossary-evidence.tsv", ("term", "chinese", "first", "example", "decided by"), rows)


def main(candidates_path):
    OUT.mkdir(parents=True, exist_ok=True)
    sections = body_sections()
    ids = {Path(c["file"]).name: c["id"] for c in json.loads((BOOK / "book.json").read_text())["chapters"]}
    candidates(candidates_path, sections, ids)
    entities(sections)
    people(sections)
    definitions(sections)
    headings(sections)
    repeats(sections)
    glossary(sections)


if __name__ == "__main__":
    main(sys.argv[1])
