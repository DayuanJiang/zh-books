"""Term statistics before translating (see review/terms/README.md).

    uv run --with spacy==3.8.7 --with <en_core_web_sm 3.8.0 wheel> python -I \
        books/fooled-by-randomness/tools/term_stats.py candidates.json
    python3 -I books/fooled-by-randomness/tools/term_stats.py --evidence

candidates.json comes from en-zh-translation-polish's terms.py, run on the English text without footnote definitions
and without the references (the bibliography stays in English).
This book has no print index, so people and named entities come from spaCy's named entity recognizer, to be checked
by hand (people-zh.tsv is the checked list). Taleb introduces many of his terms in italics, so italic phrases are
listed too.
Writes review/terms/: candidates.tsv, people.tsv, named-entities.tsv, italics.tsv, definitions.tsv, headings.tsv.
With --evidence (after glossary.md is written): counts every core term of glossary.md, fills in its first chapter and
count columns, and writes glossary-evidence.tsv with the first sentence that has the term.
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
OUT = BOOK / "review" / "terms"
SKIP = {"references"}  # stays in English
DEFINITION = re.compile(
    r"\b(I call|I called|I will call|we call|what (?:I|we|he|she|they|people|economists|traders|scientists|"
    r"philosophers|psychologists|statisticians|journalists) (?:call|calls|called|refer to)|called|known as|"
    r"dubbed|coined|the term|termed|so-called|referred to as|I refer to|a\.k\.a\.?|nicknamed|stands for|"
    r"short for|the expression|the word|the phrase|the name|is defined|definition|means that|meaning)\b", re.I)
NAMED = ("ORG", "GPE", "LOC", "FAC", "PRODUCT", "NORP", "EVENT", "WORK_OF_ART", "LAW")

# Core terms of glossary.md (the English column, exactly): pattern, case sensitive. Rows not listed here are counted
# from the English column itself (each "/" alternative, optional plural).
EVIDENCE_PATTERNS = {
    "randomness / random": (r"\brandom(?:ness)?\b", False),
    "luck / lucky": (r"\bluck(?:y|ily|ier|iest)?\b", False),
    "chance": (r"\bchances?\b", False),
    "skill / skills / nonluck": (r"\bskill(?:s|ed|ful)?\b|\bnonluck\b", False),
    "determinism / deterministic": (r"\bdeterminis", False),
    "fool of randomness / randomness fool": (r"\bfools? of (?:all fools|randomness)\b|\brandomness fool", False),
    "fooled by randomness": (r"\bfooled by randomness\b", False),
    "Table of Confusion / Table P.1": (r"Table P\.1|Table of Confusion", True),
    "noise": (r"\bnoise\b", False),
    "signal": (r"\bsignals?\b", False),
    "black swan / black swan problem": (r"\bblack swans?\b", False),
    "rare event / rare-event fallacy": (r"\brare[- ]events?\b", False),
    "skewness / skewed": (r"\bskew(?:ness|ed)?\b", False),
    "asymmetry / asymmetric": (r"\basymmetr", False),
    "alternative histories / alternative history": (r"\balternative histor(?:y|ies)\b", False),
    "visible history / invisible histories": (r"\b(?:in)?visible histor(?:y|ies)\b", False),
    "possible worlds": (r"\bpossible worlds?\b", False),
    "Monte Carlo": (r"\bMonte Carlo\b", True),
    "sample path / random run": (r"\bsample paths?\b|\brandom runs?\b", False),
    "survivorship bias / survivors": (r"\bsurvivorship\b|\bsurvivors?\b", False),
    "monkeys on typewriters / monkey": (r"\bmonkeys?\b", False),
    "track record / past performance": (r"\btrack records?\b|\bpast performance\b", False),
    "hindsight bias": (r"\bhindsight\b", False),
    "heuristics and biases / heuristic": (r"\bheuristics?\b", False),
    "affect heuristic / availability heuristic / anchoring": (r"\baffect heuristic\b|\bavailability\b|\banchoring\b", False),
    "bounded rationality / satisficing": (r"\bbounded rationality\b|\bsatisfic", False),
    "System 1 / System 2": (r"\bSystem [12]\b", True),
    "probability / probabilistic / probability blind": (r"\bprobabilit(?:y|ies)\b|\bprobabilistic", False),
    "expectation / expected value": (r"\bexpectations?\b|\bexpected values?\b", False),
    "mean / median": (r"\bmedian\b|\bthe mean\b|\bmean (?:of|is|return)\b", False),
    "conditional probability / conditional information": (r"\b(?:un)?conditional\b", False),
    "prior": (r"\bprior\b(?! to)", False),
    "ergodicity": (r"\bergodic", False),
    "data mining / data snooping": (r"\bdata[- ](?:mining|snooping)\b", False),
    "backtester / backtesting": (r"\bbacktest", False),
    "nonlinearity / nonlinear": (r"\bnonlinear", False),
    "path dependence / path dependent": (r"\bpath[- ]dependen", False),
    "sandpile effect / critical point": (r"\bsand-?pile\b|\bcritical points?\b", False),
    "network externalities / informational cascades": (r"\bnetwork externalit|\binformational cascade", False),
    "winner-take-all / loser takes all": (r"\bwinner[- ]takes?[- ]all\b|\bloser takes all\b", False),
    "Buridan’s donkey": (r"\bBuridan", True),
    "problem of induction / induction / inductive": (r"\binducti(?:on|ve)\b", False),
    "deduction / deductive": (r"\bdeducti(?:on|ve)\b", False),
    "falsification / falsifiable / falsificationism": (r"\bfalsif", False),
    "empiricism / empiricist": (r"\bempiric(?:ism|ist|ists|al)\b", False),
    "skepticism / skeptic": (r"\bskeptic", False),
    "epistemology / epistemologist": (r"\bepistemolog", False),
    "problem of demarcation": (r"\bdemarcation\b", False),
    "positivism / logical positivists / Vienna Circle": (r"\bpositivis|\bVienna Circle\b", False),
    "fallibilism / fallibility": (r"\bfallibili", False),
    "epiphenomena / epiphenomenalism": (r"\bepiphenomen", False),
    "denigration of history / historical determinism": (r"\bdenigration of history\b|\bhistorical determinism\b", False),
    "stationarity / Lucas critique / peso problem": (r"\bstationarity\b|\bLucas critique\b|\bpeso problem\b", False),
    "scientific intellectual / literary intellectual": (r"\b(?:scientific|literary) intellectuals?\b", False),
    "pseudoscience / charlatan": (r"\bpseudo-?scien|\bpseudothink|\bcharlatan", False),
    "Utopian Vision / Tragic Vision": (r"\bUtopian\b|\bTragic (?:Vision|category)\b", False),
    "reverse Turing test / exquisite cadaver / Dada Engine": (r"\breverse Turing test\b|\bexquisite cadaver|\bcadavres exquis\b|\bDada Engine\b", False),
    "Darwinism / naive Darwinism": (r"\bDarwinis", False),
    "stoicism / stoic": (r"\bstoic", False),
    "personal elegance / dignity": (r"\belegan(?:ce|t)\b|\bdignity\b", False),
    "gamblers’ ticks": (r"\bgamblers’ ticks\b|\bticks\b", False),
    "superstition": (r"\bsuperstitio", False),
    "Skinner pigeon experiment": (r"\bpigeons?\b", False),
    "wax in my ears": (r"\bwax\b", False),
    "work ethics": (r"\bwork ethics?\b", False),
    "empty suit": (r"\bempty suits?\b", False),
    "inverse rule / corporate political skill": (r"\binverse rule\b|\bcorporate political skill\b", False),
    "trader / trading": (r"\btrad(?:er|ers|ing)\b", False),
    "blow up": (r"\bblow(?:s|ing|n)? up\b|\bblew up\b|\bblowups?\b", False),
    "stop loss": (r"\bstop[- ]loss(?:es)?\b", False),
    "option / option seller / premium seller": (r"\boptions?\b", False),
    "volatility / long volatility": (r"\bvolatility\b", False),
    "high-yield / emerging markets": (r"\bhigh-yield\b|\bemerging[- ]markets?\b", False),
    "averaging down / lines in the sand": (r"\baveraging down\b|\blines? in the sand\b", False),
    "quant": (r"\bquants?\b", False),
    "hedge fund / leverage / shorting": (r"\bhedge funds?\b|\bleverag|\bshort(?:ing|ed)\b", False),
    "bull / bear / bullish / bearish": (r"\bbull(?:s|ish)?\b|\bbear(?:s|ish)?\b", False),
    "statistical significance / confidence level": (r"\bstatistical(?:ly)? significan|\bconfidence levels?\b", False),
    "bell curve / standard deviation": (r"\bbell[- ]curve|\bbell-shaped\b|\bstandard deviations?\b", False),
    "time series / econometrics": (r"\btime series\b|\beconometric", False),
    "sampling theory / sample size / law of large numbers": (r"\bsampl(?:e|ing) (?:theory|size)\b|\blaw of large numbers\b", False),
    "type I and type II errors": (r"\btype I\b", False),
    "behavioral finance / behavioral economics": (r"\bbehavioral (?:finance|econom)", False),
    "neoclassical economics / efficient markets / homo economicus": (r"\bneoclassical\b|\befficient markets?\b|\bhomo economicus\b", False),
    "endowment effect / attribution bias / overconfidence": (r"\bendowment effect\b|\battribution bias\b|\boverconfiden", False),
    "flow": (r"\bflow\b", False),
    "emotional brain / limbic system / neocortex": (r"\bemotional brain\b|\blimbic\b|\bneocort", False),
    "state space / scenario analysis": (r"\bstate space\b|\bscenario analysis\b", False),
    "cross-sectional problem / temporal aggregation": (r"\bcross-sectional\b|\btemporal aggregation\b", False),
    "spontaneous remission / cancer clusters": (r"\bspontaneous remission\b|\bcancer clusters?\b", False),
    "funds of funds": (r"\bfunds? of funds\b", False),
    "Zorglubs": (r"\bZorglubs?\b", True),
    "risk taking / risk taker / risk manager": (r"\brisk[- ]tak(?:ing|ers?)\b|\brisk[- ]manag", False),
    "Masters of the Universe": (r"\bMasters? of the Universe\b", False),
    "nonsense": (r"\bnonsense\b", False),
    "practitioner": (r"\bpractitioners?\b", False),
}


def chapters():
    return json.loads((BOOK / "book.json").read_text())["chapters"]


def body_sections():
    """[(chapter id, text without footnote definitions)] in book order, without the references."""
    out = []
    for c in chapters():
        if c["id"] in SKIP:
            continue
        text = (BOOK / "en" / c["file"]).read_text()
        text = re.sub(r"(?m)^\[\^\d+\]: .*\n?", "", text)
        out.append((c["id"], re.sub(r"\[\^\d+\]", "", text)))
    return out


def paragraphs(text, marks=False):
    """Body blocks without headings and Markdown marks (italics kept when marks is true)."""
    for block in text.split("\n\n"):
        block = block.strip()
        if not block or block.startswith("#") or block == "---":
            continue
        block = re.sub(r"(?m)^(?:> ?|\d+\.\s+|[-*]\s+)", "", block)
        if not marks:
            block = block.replace("*", "")
        yield " ".join(block.split())


def sentences(block):
    return re.split(r"(?<=[.?!”])\s+(?=[A-Z“])", block)


def occurrences(pattern, sections, flags=0):
    rx = re.compile(pattern, flags)
    counts = [(cid, len(rx.findall(text.replace("*", "")))) for cid, text in sections]
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
    groups = defaultdict(list)
    for name in people:
        groups[name.split()[-1]].append(name)
    rows = []
    for surname, names in groups.items():
        names.sort(key=lambda n: (-len(n.split()), -sum(people[n].values())))
        ner = sum(sum(people[n].values()) for n in names)
        n, count, where = occurrences(rf"\b{re.escape(surname)}\b", sections)
        forms = ", ".join(f"{x} {sum(people[x].values())}" for x in names[:5])
        first = where or min((c for x in names for c in people[x]), key=order.index)
        rows.append((names[0], forms, ner, n, count, first))
    rows.sort(key=lambda r: r[0].split()[-1].lower())
    tsv("people.tsv", ("name", "NER forms", "NER mentions", "surname in text", "chapters", "first"), rows)

    rows = []
    for (label, name), per in named.items():
        rows.append((name, label, sum(per.values()), len(per), min(per, key=order.index)))
    rows.sort(key=lambda r: (-r[2], r[0]))
    tsv("named-entities.tsv", ("entity", "NER label", "mentions", "chapters", "first"), rows)


def write_italics(sections):
    """Italic phrases: Taleb's terms, foreign words, book titles."""
    found = defaultdict(Counter)
    for cid, text in sections:
        for block in paragraphs(text, marks=True):
            for phrase in re.findall(r"(?<!\*)\*([^*]+?)\*(?!\*)", block):
                phrase = phrase.strip(" ,.;:“”")
                if phrase:
                    found[phrase.lower()][(cid, phrase)] += 1
    order = [cid for cid, _ in sections]
    rows = []
    for key, per in found.items():
        cids = {cid for cid, _ in per}
        first = min(cids, key=order.index)
        form = Counter({p: n for (_, p), n in per.items()}).most_common(1)[0][0]
        n, chapters_with, _ = occurrences(rf"(?<!\w){re.escape(key)}(?!\w)", sections, re.I)
        rows.append((form, sum(per.values()), n, chapters_with, first, len(key.split())))
    rows.sort(key=lambda r: (-r[1], -r[2], r[0].lower()))
    tsv("italics.tsv", ("italic phrase", "in italics", "in text", "chapters", "first", "words"), rows)


def write_definitions(sections):
    defs = []
    for cid, text in sections:
        for block in paragraphs(text):
            for sentence in sentences(block):
                found = DEFINITION.search(sentence)
                if found:
                    defs.append((cid, found.group(0), sentence))
    tsv("definitions.tsv", ("chapter", "signal", "sentence"), defs)


def write_headings():
    heads = []
    for c in chapters():
        for line in (BOOK / "en" / c["file"]).read_text().split("\n"):
            if re.match(r"#{1,3} ", line):
                level, title = line.split(" ", 1)
                heads.append((c["id"], len(level), title))
    tsv("headings.tsv", ("chapter", "level", "heading"), heads)


def term_pattern(term):
    """Regex for a glossary row: its own pattern, or the English alternatives with optional plural."""
    if term in EVIDENCE_PATTERNS:
        return EVIDENCE_PATTERNS[term]
    parts = [re.sub(r"\s*\(.*?\)", "", p).strip() for p in term.split(" / ")]
    alts = [re.escape(p).replace("\\ ", " ").replace(" ", r"[\s-]") + r"(?:s|es)?" for p in parts if p]
    case = any(p[:1].isupper() and not p.isupper() for p in parts) and all(p[:1].isupper() for p in parts)
    return r"(?<![\w-])(?:" + "|".join(alts) + r")(?![\w])", case


def write_evidence():
    """Count the core terms of glossary.md, fill in its columns and write glossary-evidence.tsv."""
    sections = body_sections()
    path = BOOK / "glossary.md"
    lines = path.read_text().split("\n")
    start = lines.index("## 核心概念")
    header = [c.strip() for c in lines[start + 2].strip("|").split("|")]
    col_first, col_count = header.index("首次出现"), header.index("出现次数")
    rows = []
    for i in range(start + 4, len(lines)):
        if not lines[i].startswith("|"):
            break
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        term, chinese = cells[0], cells[1]
        rx, case = term_pattern(term)
        n, _, first = occurrences(rx, sections, 0 if case else re.I)
        compiled = re.compile(rx, 0 if case else re.I)
        example = ""
        for cid, text in sections:
            if cid != first:
                continue
            heads = [line.lstrip("# ") for line in text.split("\n") if line.startswith("#")]
            example = next((s for b in paragraphs(text) for s in sentences(b) if compiled.search(s)), "")
            example = example or next((h for h in heads if compiled.search(h)), "")
            break
        if n == 0:
            print(f"warning: no occurrence of {term!r}")
        cells[col_first], cells[col_count] = first or "-", str(n)
        lines[i] = "| " + " | ".join(cells) + " |"
        rows.append((term, chinese, first, n, example, "Claude（初定）"))
    path.write_text("\n".join(lines))
    tsv("glossary-evidence.tsv", ("term", "chinese", "first", "count", "example", "decided by"), rows)


def main(args):
    OUT.mkdir(parents=True, exist_ok=True)
    if args == ["--evidence"]:
        write_evidence()
        return
    sections = body_sections()
    write_candidates(args[0], sections)
    write_entities(sections)
    write_italics(sections)
    write_definitions(sections)
    write_headings()


if __name__ == "__main__":
    main(sys.argv[1:])
