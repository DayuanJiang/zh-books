"""Term statistics before translating (see review/terms/README.md).

    $PY -I books/never-split-the-difference/tools/term_stats.py candidates.json

$PY is a Python with spaCy 3.8 and en_core_web_sm (the environment for en-zh-translation-polish's terms.py).
candidates.json comes from terms.py, run on a copy of en/ without footnote definitions (this book has none).

The EPUB has no print index (the print edition's index and notes are missing from it), so there is no
index-terms.tsv. Names come from spaCy's named entities (entities.tsv) and a full read of the book, checked by
hand into people-zh.tsv; people.tsv counts each person in the text.
Writes review/terms/: candidates.tsv, entities.tsv, people.tsv, definitions.tsv, headings.tsv, italics.tsv,
repeats.tsv, glossary-evidence.tsv. Fills the 首次出现 and 出现次数 columns of the core table in glossary.md.
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
    r"\b(we call|I call|what I call|what we call|is called|are called|called|known as|refer to|referred to as|"
    r"so-called|the term|the phrase|stands for|short for|i\.e\.|in other words|is defined as|by definition|"
    r"is when|it’s when|that is,|technique|tactic|principle|rule|model|effect|theory|calls? (?:them|it|this)|"
    r"(?:\w+ )?(?:kinds|types) of|what (?:he|she|they|psychologists|researchers|economists) call(?:ed|s)?)(?!\w)", re.I)
# "called" as in a phone call, not a name: such sentences are dropped when "called" is their only signal.
PHONE_CALL = re.compile(r"\bcalled (?:me|him|her|us|them|back|within|to|and|yet|in|off|away|an agent|the broker|"
                        r"Benjie|Ryan|Dominick|American|my colleague)\b|\b(?:has|had|have|n’t|no one) called\b", re.I)
ENTITY_LABELS = {"PERSON", "ORG", "GPE", "LOC", "NORP", "PRODUCT", "WORK_OF_ART", "EVENT", "FAC", "LAW", "LANGUAGE"}

# Names that share a given name or surname with someone else, or that the text writes in another way:
# name in people-zh.tsv -> (pattern, chapters it is limited to, or None for the whole book).
PATTERNS = {
    "Chris Voss": (r"\bVoss\b|\bChris\b(?! Watts)", None),  # ch02 "Where's Chris? Take me to Chris." is Watts
    "Chris Watts": (r"\bChris Watts\b|\bWatts\b", None),
    "Robert Mnookin": (r"\bMnookin\b|\bRobert\b(?! Mnookin)|\bBob\b", ("ch01",)),
    "George Giffe Jr.": (r"\bGiffe\b", None),
    "Richard Nixon": (r"(?<!Jim )\bNixon\b", None),
    "Joe": (r"\bJoe\b", ("ch02",)),
    "George A. Miller": (r"\bMiller\b", ("ch02",)),
    "Omar Abdel-Rahman": (r"\bBlind Sheikh\b", None),
    "Sun Tzu": (r"\bSun Tzu\b", None),
    "Mark": (r"\bMark\b(?! Cuban)", ("ch03",)),
    "Ryan B.": (r"\bRyan\b", None),
    "Martin": (r"\bMartin\b", ("ch04",)),
    "Jim Camp": (r"\bCamp\b", ("ch04",)),
    "Joe Businessman": (r"\bJoe\b", ("ch04",)),
    "Jim Snyder": (r"\bJim\b(?! Camp)|\bSnyder\b", ("ch04",)),
    "Mark Cuban": (r"\bCuban\b", None),
    "Jim Nixon": (r"\bJim Nixon\b", None),
    "Abu Sabaya": (r"\bSabaya\b", None),
    "Brandon Voss": (r"\bBrandon\b", None),
    "Phillip Snyder": (r"\bPhillip Snyder\b", None),
    "Don A. Moore": (r"\bMoore\b", ("ch06",)),
    "Pablo Picasso": (r"\bPicasso\b", None),
    "René Descartes": (r"\bDescartes\b", None),
    "Martin Burnham": (r"\bMartin\b|(?<!Gracia )\bBurnham\b", ("ch07", "ch08")),
    "Gracia Burnham": (r"\bGracia\b", None),
    "Gloria Macapagal-Arroyo": (r"\bArroyo\b", None),
    "Kevin Dutton": (r"\bDutton\b", None),
    "Kevin Rust": (r"\bKevin\b|\bRust\b", ("ch08",)),
    "W. C. Fields": (r"\bW\. C\. Fields\b", None),
    "Jesus Bueno": (r"\bJesus\b(?! Christ)|\bBueno\b", None),
    "Mike Tyson": (r"\bTyson\b", None),
    "Mike Ackerman": (r"\bMike\b(?! Tyson)|\bAckerman\b(?! (?:model|system|plan|process|offers?|[Bb]argaining|guys))",
                      None),
    "Clint Van Zandt": (r"\bVan Zandt\b|\bClint\b", None),
    "Margaret Moore": (r"\bMoore\b", ("ch10",)),
    "Winnie Miller": (r"\bWinnie\b", None),
    "Jesus Christ": (r"\bChrist\b", None),
}

# (label in glossary.md, English pattern, case sensitive): the counts in the core table come from these.
COUNTS = [
    # Negotiation in general
    ("negotiation / negotiate / negotiator", r"\bnegotiat\w*", False),
    ("counterpart", r"\bcounterparts?\b", False),
    ("the other side / the other party", r"\bthe other (?:side|party)\b", False),
    ("adversary / opponent", r"\badversar(?:y|ies)\b|\bopponents?\b", False),
    ("hostage negotiation / hostage negotiator", r"\bhostage negotiat\w*", False),
    ("lead international kidnapping negotiator", r"\blead international (?:kidnapping|hostage) negotiator\b", False),
    ("hostage-taker / kidnapper", r"\bhostage-takers?\b|\bkidnappers?\b", False),
    ("bad guys", r"\bbad guys?\b", False),
    ("crisis negotiation / crisis intervention", r"\bcrisis (?:negotiation|intervention)s?\b", False),
    ("deal / deal making", r"\bdeals?\b|\bdeal[- ]making\b", False),
    ("No deal is better than a bad deal", r"\bno deal is better than a bad deal\b", False),
    ("win-win / win-lose / wimp-win deal", r"\bwin-win\b|\bwin-lose\b|\bwimp-win\b", False),
    ("compromise / split the difference", r"\bcompromis\w*|\bsplit(?:ting)? the difference\b", False),
    ("never split the difference", r"\bnever split the difference\b", False),
    ("bargaining / haggling", r"\bbargain\w*|\bhaggl\w*", False),
    ("bare-knuckle bargaining", r"\bbare-knuckle\b", False),
    ("brass tacks", r"\bbrass tacks\b", False),
    ("problem solving / problem solver", r"\bproblem[- ]solv\w*", False),
    ("BATNA", r"\bBATNA\b", True),
    ("ZOPA", r"\bZOPA\b", True),
    ("implementation / execution", r"\bimplement\w*|\bexecution\b", False),
    # Listening and empathy
    ("Tactical Empathy", r"\btactical empathy\b", False),
    ("empathy / empathize / empathic", r"\bempath\w*", False),
    ("sympathy", r"\bsympath\w*", False),
    ("forced empathy", r"\bforced empathy\b", False),
    ("emotional intelligence", r"\bemotional intelligence\b", False),
    ("active listening", r"\bactive listening\b", False),
    ("Behavioral Change Stairway Model (BCSM)", r"\bBehavioral Change Stairway\b|\bBCSM\b", False),
    ("rapport", r"\brapport\b", False),
    ("unconditional positive regard", r"\bunconditional positive regard\b", False),
    ("Late-Night FM DJ Voice", r"\bFM DJ\b|\bDJ(?:’s)? voice\b", False),
    ("positive/playful voice / direct or assertive voice", r"\bplayful voice\b|\bassertive voice\b", False),
    ("downward / upward inflection", r"\binflect\w*", False),
    ("mirroring / mirror", r"\bmirror\w*", False),
    ("isopraxism", r"\bisopraxism\b", False),
    ("labeling / label", r"\b(?:mis)?label\w*", False),
    ("It seems like … / It sounds like … / It looks like …", r"\bit (?:seems|sounds|looks) like\b", False),
    ("accusation audit", r"\baccusation audits?\b", False),
    ("taking the sting out", r"\btaking the sting out\b", False),
    ("presenting / underlying (behavior, emotion)", r"\bpresenting\b|\bunderlying\b", False),
    ("dynamic", r"\bdynamics?\b", False),
    ("neural resonance", r"\bneural resonance\b", False),
    ("words, music, and dance", r"\bwords, music, and dance\b", False),
    ("Effective Pauses / Minimal Encouragers", r"\beffective pauses?\b|\bminimal encouragers?\b", False),
    ("paraphrase / paraphrasing", r"\bparaphras\w*", False),
    ("summary / summarize", r"\bsummar\w*", False),
    ("“That’s right”", r"\bthat’s right\b", False),
    ("“You’re right”", r"\byou’re right\b", False),
    ("assumptions / hypotheses", r"\bassum\w*|\bhypothes[ie]s\b", False),
    ("state of schizophrenia / the voice in their head",
     r"\bschizophreni\w*|\bvoices? in (?:their|your|his|my) (?:own )?head\b", False),
    ("people mover", r"\bpeople mover\b", False),
    ("vomiting information", r"\bvomiting (?:more )?information\b", False),
    ("proof of life", r"\bproofs?[- ]of[- ]life\b", False),
    ("closer", r"\bclosers?\b", False),
    ("Making Shit Up (MSU)", r"\bMSU\b", True),
    ("drive-bys", r"\bdrive-bys?\b", False),
    ("“sixty seconds or she dies”", r"\bsixty seconds or she dies\b", False),
    ("“Big Bad Prime” / prime contractor", r"\bBig Bad Prime\b|\bprime contractor\b", False),
    ("frequent callers / energy vampires", r"\bfrequent callers?\b|\benergy vampires?\b", False),
    ("CareFronting / CareFrontation", r"\bCareFront\w*", False),
    # "Yes" and "No"
    ("“Yes” / “No” (as words)", r"[“\"](?:Yes|No)\b", False),
    ("Counterfeit / Confirmation / Commitment “Yes”", r"\b(?:counterfeit|confirmation|commitment) [“\"]?yes\b", False),
    ("“No”-oriented question / “Yes pattern”", r"[“\"]No[”\"]-oriented\b|\bYes pattern\b", False),
    ("the right to veto", r"\bright to veto\b", False),
    ("autonomy", r"\bautonomy\b", False),
    ("niceness", r"\bniceness\b", False),
    ("“Is now a bad time to talk?”", r"\bIs now a bad time to talk\b", False),
    ("“Have you given up on this project?”", r"\bHave you given up on\b", False),
    ("“Yes” is nothing without “How”", r"\bnothing without [“\"]?how\b", False),
    ("“I’ll try”", r"[“\"]I’ll try\b", False),
    # Calibrated questions and execution
    ("calibrated questions / calibrate", r"\bcalibrat\w*", False),
    ("open-ended / closed-ended questions", r"\bopen-ended\b|\bclosed?-ended\b", False),
    ("“How am I supposed to do that?”", r"\bhow (?:am I|are we|was I) supposed to\b", False),
    ("“How” questions / How/No", r"[“\"]How[”\"]? questions?\b|\bHow/No\b", False),
    ("“Why” questions", r"[“\"]why[”\"]", False),
    ("illusion of control", r"\billusion of control\b", False),
    ("unbelief / suspend unbelief", r"\bunbelie\w*", False),
    ("showdown", r"\bshowdowns?\b", False),
    ("hostage mentality", r"\bhostage mentality\b", False),
    ("fight-or-flight / reptilian brain / limbic system / neocortex",
     r"\bfight-or-flight\b|\breptilian brain\b|\blimbic system\b|\bneocortex\b", False),
    ("reciprocity", r"\breciproc\w*", False),
    ("behind the table / Level II players", r"\bbehind the table\b|\bLevel II\b", False),
    ("deal makers / deal killers", r"\bdeal (?:makers?|killers?|breakers?)\b", False),
    ("decision architects / decision makers", r"\bdecision (?:architects?|makers?)\b", False),
    ("7-38-55 Percent Rule", r"\b7-38-55\b", False),
    ("verbal / paraverbal / nonverbal / body language", r"\bparaverbal\b|\bnonverbal\b|\bbody language\b", False),
    ("Rule of Three", r"\bRule of Three\b", False),
    ("Pinocchio Effect", r"\bPinocchio\b", False),
    ("pronouns", r"\bpronouns?\b", False),
    ("the Chris discount", r"\bChris discount\b", False),
    ("bid against themselves", r"\bbid(?:ding)? against (?:themselves|himself|herself|yourself)\b", False),
    ("“the art of letting someone else have your way”", r"\bart of letting someone else have your way\b", False),
    ("listener’s judo / psychological judo", r"\bjudo\b", False),
    # Psychology and behavioral economics
    ("behavioral economics / rational actors", r"\bbehavioral economics\b|\brational actors?\b", False),
    ("System 1 / System 2", r"\bSystem [12]\b", True),
    ("Cognitive Bias", r"\bcognitive bias(?:es)?\b", False),
    ("Framing Effect / framing", r"\bframing effect\b|\bfram(?:e|ed|es|ing)\b", False),
    ("Prospect Theory", r"\bprospect theory\b", False),
    ("Certainty Effect", r"\bcertainty effect\b", False),
    ("Loss Aversion", r"\bloss aversion\b|\baversion to loss\b", False),
    ("amygdala", r"\bamygdala\b", False),
    ("Ultimatum Game / proposer / accepter", r"\bUltimatum Game\b|\bproposers?\b|\baccepters?\b", False),
    ("winner’s curse / buyer’s remorse", r"\bwinner’s curse\b|\bbuyer’s remorse\b", False),
    ("similarity principle / in-group", r"\bsimilarity principle\b|\bin-group\b", False),
    ("paradox of power", r"\bparadox of power\b", False),
    # Deadlines, fairness and anchors (chapter 6)
    ("deadline", r"\bdeadlines?\b", False),
    ("fair / fairness / unfair", r"\bfair(?:ness|ly)?\b|\bunfair\w*", False),
    ("the F-word / F-bomb", r"\bF-(?:word|bomb)\b|[“\"]F[”\"]", False),
    ("anchor / anchoring / extreme anchor", r"\banchor\w*", False),
    ("“anchor and adjustment” effect", r"\banchor and adjustment\b", False),
    ("range / bolstering range", r"\branges?\b", False),
    ("nonmonetary terms / pivot to terms",
     r"\bnon-?monetary\b|\bnonsalary\b|\bnonfinancial\b|\bpivot\w* to (?:nonmonetary )?terms\b", False),
    ("odd numbers / nonround numbers", r"\bnon-?round\b|\bodd (?:ones|numbers?)\b", False),
    ("pleasant persistence", r"\bpleasant(?:ly)? persist\w*", False),
    ("unofficial mentor", r"\bunofficial mentor\b", False),
    ("rainmaker", r"\brainmakers?\b|\bmake it rain\b", False),
    # Bargaining (chapter 9)
    ("negotiation style / Analyst / Accommodator / Assertive",
     r"\bAnalysts?\b|\bAccommodators?\b|\bAssertives?\b|(?i:\bnegotiati(?:on|ng) styles?\b)", True),
    ("“I am normal” paradox", r"\bI am normal\b", False),
    ("Golden Rule / Black Swan rule", r"\bGolden Rule\b|\bBlack Swan rule\b", False),
    ("taking a punch / punching back", r"\bpunch\w*", False),
    ("strategic umbrage", r"\bstrategic umbrage\b", False),
    ("“I” messages", r"[“\"]I[”\"] messages?\b", False),
    ("no neediness / ready-to-walk mindset", r"\bneediness\b|\bneedy\b|\bready-to-walk\b", False),
    ("tough love", r"\btough love\b", False),
    ("Ackerman model / Ackerman bargaining", r"\bAckerman\b(?! guys)", False),
    ("target price / first offer / counteroffer", r"\btarget price\b|\bfirst offer\b|\bcounter-?offers?\b", False),
    # Black Swans and leverage (chapter 10)
    ("Black Swan", r"\bBlacks? Swans?\b(?! Group| rule| theory)", True),
    ("Black Swan theory", r"\bBlack Swan theory\b", True),
    ("known knowns / known unknowns / unknown unknowns", r"\b(?:known|unknown) (?:knowns?|unknowns?)\b", False),
    ("leverage", r"\bleverage\b", False),
    ("positive / negative / normative leverage", r"\b(?:positive|negative|normative) leverage\b", False),
    ("religion", r"\breligio\w*", False),
    ("worldview", r"\bworldviews?\b", False),
    ("reason for being", r"\breasons? for being\b", False),
    ("“They’re crazy!”", r"\bThey’re crazy\b", False),
    ("ill-informed / constrained / other interests",
     r"\bill-informed\b|\bconstrain\w*|\bother interests\b|\bhidden interests?\b", False),
    ("face time", r"\bface time\b", False),
    ("unguarded moments", r"\bunguarded\b", False),
    ("backup listeners", r"\bbackup listeners?\b", False),
    ("suicide by cop", r"\bsuicide-by-cop\b", False),
    ("stewardship", r"\bsteward\w*", False),
    ("Dawn of the Third Day", r"\bDawn of the Third Day\b", False),
    ("GIGO (Garbage In, Garbage Out)", r"\bGIGO\b", True),
    ("cap rate / cash cow / due diligence", r"\bcap rate\b|\bcash cow\b|\bdue diligence\b", False),
    # Book structure
    ("Key Lessons", r"\bKey Lessons\b", True),
    ("Negotiation One Sheet", r"\bNegotiation One Sheet\b", False),
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
        for line in block.split("\n") if re.match(r"\s*([-*]|\d+\.|>) ", block) else [block]:
            for sentence in re.split(r"(?<!\bMr\.)(?<!\bMrs\.)(?<!\bDr\.)(?<!\bvs\.)(?<=[.?!”])\s+(?=[A-Z“*])", line):
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
            name = re.sub(r"’s$", "", " ".join(ent.text.split()).strip("“”\"'’ "))
            if ent.label_ not in ENTITY_LABELS or not re.search(r"[A-Za-z]", name):
                continue
            row = found.setdefault((name, ent.label_), [0, [], cid])
            row[0] += 1
            if cid not in row[1]:
                row[1].append(cid)
    rows = [(name, label, n, len(chs), first) for (name, label), (n, chs, first) in found.items()]
    rows.sort(key=lambda r: (r[1], -r[2], r[0]))
    tsv("entities.tsv", ("entity", "label", "count", "chapters", "first"), rows)


def person_pattern(name, names):
    """(pattern, chapters or None) for counting a person: PATTERNS if listed there; otherwise the full name, the
    surname, or a given name no one else in the list has. Single names must not be followed by a capitalized word."""
    if name in PATTERNS:
        return PATTERNS[name]
    parts = re.sub(r"^(?:Mr\.|Mrs\.|Dr\.) ", "", name).split()
    if len(parts) == 1:
        return rf"\b{re.escape(parts[0])}\b(?! [A-Z][a-z])", None
    givens = Counter(n.split()[0] for n in names)
    options = [re.escape(name), re.escape(parts[-1])]
    if givens[parts[0]] == 1:
        options.append(re.escape(parts[0]))
    return r"\b(?:" + "|".join(options) + r")\b", None


def people(sections):
    names = [row["name"] for row in csv.DictReader((OUT / "people-zh.tsv").open(), delimiter="\t")]
    rows = []
    for name in names:
        pattern, chapters = person_pattern(name, names)
        n, count, first = occurrences(re.compile(pattern), [s for s in sections if not chapters or s[0] in chapters])
        rows.append((name, pattern, ", ".join(chapters or ()), n, count, first))
    tsv("people.tsv", ("name", "pattern", "only in", "mentions", "chapters", "first"), rows)


def definitions(sections):
    rows = []
    for cid, text in sections:
        for sentence in sentences(text):
            signals = [m.group(0) for m in DEFINITION.finditer(sentence)]
            if not signals or sentence.startswith("#"):
                continue
            if all(s.lower() == "called" for s in signals) and PHONE_CALL.search(sentence):
                continue
            rows.append((cid, signals[0], plain(sentence).strip()))
    tsv("definitions.tsv", ("chapter", "signal", "sentence"), rows)


def headings(sections):
    """Every heading with its level, and the chapter subtitle (the italic paragraph under the # heading)."""
    rows = []
    for cid, text in sections:
        for m in re.finditer(r"(?m)^(#{1,6}) (.+)$", text):
            rows.append((cid, len(m.group(1)), m.group(2)))
            subtitle = re.match(r"\n\n\*([^*\n]+)\*\n", text[m.end():]) if len(m.group(1)) == 1 else None
            if subtitle:
                rows.append((cid, "subtitle", subtitle.group(1)))
    tsv("headings.tsv", ("chapter", "level", "heading"), rows)


def italics(sections):
    """Italic phrases of two words or more, and capitalized single words: titles of works, terms, quoted lines."""
    found = {}
    for cid, text in sections:
        for m in re.finditer(r"(?<![*\w])\*([^*\n]+?)\*(?![*\w])", text):
            phrase = m.group(1).strip()
            if len(phrase.split()) < 2 and not phrase[:1].isupper():
                continue
            row = found.setdefault(phrase, [0, [], cid])
            row[0] += 1
            if cid not in row[1]:
                row[1].append(cid)
    order = {cid: i for i, (cid, _) in enumerate(sections)}
    rows = sorted(((p, n, len(chs), first) for p, (n, chs, first) in found.items()), key=lambda r: (order[r[3]], -r[1]))
    tsv("italics.tsv", ("phrase", "count", "chapters", "first"), rows)


def repeats(sections):
    """Paragraphs, quotes and list items that occur more than once: translate them the same way every time."""
    seen = {}
    for cid, text in sections:
        for block in text.split("\n\n"):
            lines = block.split("\n") if re.match(r"\s*([-*]|\d+\.|>) ", block) else [block]
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
    italics(sections)
    repeats(sections)
    glossary(sections)


if __name__ == "__main__":
    main(sys.argv[1])
