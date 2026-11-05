"""Term statistics before translating (see review/terms/README.md).

    uv run --with spacy==3.8.7 --with "click>=8.2,<9" --with "en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl" \
        python -I books/bad-blood/tools/term_stats.py candidates.json

candidates.json comes from en-zh-translation-polish's terms.py, run on the English text without footnotes.
The book has no print index. People come from review/terms/people-zh.tsv (checked by hand); spaCy's PERSON
entities are only used to list names that the table does not cover yet. Writes review/terms/: candidates.tsv,
people.tsv, definitions.tsv, headings.tsv, glossary-evidence.tsv, and fills the "首次出现" and "出现次数" columns
of the core-term table in glossary.md.
"""

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
OUT = BOOK / "review" / "terms"
# "called" as in phoning someone and "went by" as in time passing are left out; ", or CLSs" catches spelled-out acronyms.
DEFINITION = re.compile(
    r"\b(we call|known as|dubbed|coined|the term|so-called|referred to as|nicknamed|code[- ]?named?|"
    r"called(?! (?:me|him|her|them|us|back|in|into|out|up|off|to|it (?:to|up|quits)|attention|the (?:FBI|meeting|cops|first|local|next|description|story))\b)|"
    r"stands for|short for|went by(?= (?:the|[A-Z“\"]))|sobriquet|parlance|jargon|lingo|acronym|"
    r"what (?:he|she|they|it|some|many|people|employees|insiders) call(?:ed|s)?|a phrase|the phrase)\b"
    r"|(?-i:, or [A-Z]{2,}s?\b)", re.I)

# (English label in glossary.md, pattern, case sensitive): used to count each core term in the body text.
GLOSSARY = [
    ("Edison / Edisons", r"\bEdisons?\b", True),
    ("miniLab", r"\bminiLabs?\b", True),
    ("4S", r"\b4S\b", True),
    ("Theranos 1.0", r"\b(?:Theranos )?1\.0\b", True),
    ("gluebot / glue robot", r"\bgluebot\b|\bglue[- ]?(?:dispensing )?robot", False),
    ("nanotainer", r"\bnanotainers?\b", False),
    ("cartridge", r"\bcartridges?\b", False),
    ("reader", r"\breaders?\b", False),
    ("TheraPatch / patch", r"\bTheraPatch\b|\bpatch\b", False),
    ("six-blade", r"\bsix-blade\b", False),
    ("wellness center", r"\bwellness cent", False),
    ("Project T-Rex / Project Beta / Project Stanford", r"\bT-Rex\b|\bProject Beta\b|\bProject Stanford\b", True),
    ("Frat Pack / Therabros", r"\bFrat Pack\b|\bTherabros\b", True),
    ("Jurassic Park / Normandy", r"\bJurassic Park\b|\bNormandy\b", True),
    ("Eagle One / Eagle Two", r"\bEagle (?:One|Two)\b", True),
    ("extra-ordinary", r"\bextra-ordinary\b", False),
    ("blood test / blood testing", r"\bblood[- ]test(?:s|ing)?\b", False),
    ("test result", r"\btest results?\b", False),
    ("finger-stick / fingerstick", r"\bfinger[- ]?sticks?\b|\bfinger[- ]?prick", False),
    ("venous draw / venipuncture", r"\bvenous\b|\bvenipuncture\b|\bveins?\b", False),
    ("lab / laboratory", r"\blab(?:s|oratory|oratories)?\b", False),
    ("clinical lab / CLIA lab", r"\b(?:clinical|CLIA) lab(?:s|oratory|oratories)?\b", False),
    ("lab director / laboratory director", r"\blab(?:oratory)? directors?\b", False),
    ("assay", r"\bassays?\b", False),
    ("immunoassay", r"\bimmunoassays?\b", False),
    ("general chemistry", r"\bgeneral[- ]chemistry\b", False),
    ("analyzer", r"\banalyzers?\b", False),
    ("Siemens ADVIA", r"\bADVIAs?\b", True),
    ("spectrophotometer / cytometer", r"\bspectrophotomet|\bcytomet", False),
    ("pipette", r"\bpipett", False),
    ("microfluidics", r"\bmicrofluidic", False),
    ("dilute / dilution", r"\bdilut", False),
    ("reagent / antibody", r"\breagents?\b|\bantibod", False),
    ("proficiency testing", r"\bproficiency[- ]test", False),
    ("quality control", r"\bquality[- ]control\b|\bQC\b", False),
    ("validation", r"\bvalidat", False),
    ("coefficient of variation (CV)", r"\bcoefficients? of variation\b|\bCVs?\b(?= (?:calculation|of|for|was|were|is))|, or CV\b", True),
    ("sensitivity / equivocal zone", r"\bsensitivity\b|\bequivocal\b", False),
    ("reference range / normal range", r"\breference ranges?\b|\bnormal ranges?\b", False),
    ("hemolysis", r"\bhemoly", False),
    ("dead volume / throughput", r"\bdead volume\b|\bthroughput\b", False),
    ("pathologist", r"\bpathologists?\b", False),
    ("clinical laboratory scientist (CLS)", r"\bclinical laboratory scientists?\b|\bCLSs?\b", True),
    ("phlebotomist", r"\bphlebotom", False),
    ("lab associate", r"\blab associates?\b", False),
    ("CLIA", r"\bCLIA\b|Clinical Laboratory Improvement Amendments", True),
    ("CMS", r"\bCMS\b|Centers? for Medicare", True),
    ("FDA", r"\bFDA\b|Food and Drug Administration", True),
    ("laboratory-developed test (LDT)", r"\b[Ll]aboratory[- ]developed tests?\b|\bLDTs?\b", True),
    ("inspection / survey", r"\binspect(?:ion|ions|or|ors|ed)?\b|\bsurvey(?:s|ed|or|ors)?\b", False),
    ("deficiencies / sanctions", r"\bdeficienc|\bsanction", False),
    ("institutional review board (IRB)", r"\binstitutional review boards?\b|\bIRB\b", False),
    ("Medicare / Medicaid", r"\bMedicare\b|\bMedicaid\b", True),
    ("startup", r"\bstart-?ups?\b", False),
    ("founder / cofounder", r"\b(?:co-?)?founders?\b", False),
    ("venture capitalist / venture capital", r"\bventure capital(?:ist|ists)?\b|\bVCs?\b", False),
    ("funding round / Series B", r"\b(?:funding|fund-raising) rounds?\b|\bSeries [A-D]\b|\brounds? of funding\b", False),
    ("valuation", r"\bvaluations?\b", False),
    ("unicorn", r"\bunicorns?\b", False),
    ("hockey-stick forecast", r"\bhockey[- ]stick\b", False),
    ("vaporware", r"\bvaporware\b", False),
    ("stealth mode", r"\bstealth\b", False),
    ("board / director", r"\bboard(?: of directors)?\b|\bboard members?\b", False),
    ("general counsel", r"\bgeneral counsel\b", False),
    ("pharmaceutical company / drugmaker", r"\bpharmaceutical compan|\bdrugmakers?\b|\bdrug companies\b", False),
    ("secrecy / silo", r"\bsecre(?:cy|tive)\b|\bcompartmentali|\bsilos?\b", False),
    ("black turtleneck", r"\bturtleneck", False),
    ("patent / patent interference", r"\bpatent(?:s|ed|ing)?\b|\binterference\b", False),
    ("trade secrets", r"\btrade secrets?\b", False),
    ("confidentiality agreement / NDA", r"\bconfidentiality agreements?\b|\bnondisclosure\b|\bNDAs?\b", False),
    ("lawsuit / litigation", r"\blawsuits?\b|\blitigation\b", False),
    ("deposition", r"\bdeposition", False),
    ("affidavit", r"\baffidavit", False),
    ("anti-SLAPP", r"\banti-SLAPP\b", True),
    ("whistleblower", r"\bwhistle-?blow", False),
    ("source (journalism)", r"\bsources?\b", False),
    ("on the record / deep background", r"\b(?:on|off) the record\b|\bdeep background\b", False),
    ("tip", r"\btips?\b(?!-in)", False),
    ("No surprises", r"\bNo surprises\b", False),
    ("la mattanza", r"\bmattanza\b", False),
    ("Hippocratic Oath", r"\bHippocratic\b", True),
    ("the Journal", r"\bthe Journal\b|\bWall Street Journal\b", False),
    ("Silicon Valley / the Valley", r"\bSilicon Valley\b|\bthe Valley\b", False),
    ("fraud", r"\bfraud", False),
    ("H-1B visa", r"\bH-1B\b", True),
]


def body_sections():
    """[(chapter id, text without footnotes)] in book order."""
    config = json.loads((BOOK / "book.json").read_text())
    out = []
    for c in config["chapters"]:
        text = (BOOK / "en" / c["file"]).read_text()
        text = re.sub(r"(?m)^\[\^\d+\]: .*\n?", "", text)
        out.append((c["id"], re.sub(r"\[\^\d+\]", "", text).replace("*", "")))
    return out


def sentences(sections):
    for cid, text in sections:
        for block in text.split("\n\n"):
            if block.startswith("#") or block.strip() == "---":
                continue
            block = re.sub(r"(?m)^> ?", "", block)
            for sentence in re.split(r"(?<=[.?!”])\s+(?=[A-Z“])", block):
                yield cid, " ".join(sentence.split())


def occurrences(pattern, sections, flags=0):
    rx = re.compile(pattern, flags)
    counts = [(cid, len(rx.findall(text))) for cid, text in sections]
    hits = [(cid, n) for cid, n in counts if n]
    return sum(n for _, n in hits), len(hits), hits[0][0] if hits else ""


def tsv(name, header, rows):
    lines = ["\t".join(header)] + ["\t".join(str(x) for x in row) for row in rows]
    (OUT / name).write_text("\n".join(lines) + "\n")
    print(f"{name}: {len(rows)} rows")


def short_name(name):
    """'Ramesh “Sunny” Balwani' -> 'Balwani'; 'Christian Holmes II' -> 'Holmes'; 'Christian Holmes (brother)' -> 'Holmes'."""
    name = re.sub(r"\s*\(.*\)$", "", re.sub(r"[“\"][^”\"]*[”\"]", "", name)).split()
    name = [w for w in name if w not in ("II", "III", "IV", "Jr.", "Dr.")]
    if name and re.fullmatch(r"[A-Z]\.", name[-1]):  # 'Natalie M.'
        return name[0]
    return name[-1] if name else ""


def people(sections):
    """people.tsv: how often each name in people-zh.tsv occurs. Returns the English words of the names and notes."""
    rows, known = [], set()
    for row in csv.DictReader((OUT / "people-zh.tsv").open(), delimiter="\t"):
        name = row["name"]
        full = re.sub(r"^Dr\. |\s*\(.*\)$", "", name)
        # Other forms of a name (Don, Arne, Dr. J) are written in the note column.
        known.update(re.findall(r"[A-ZÀ-Ž][\w’'-]*", full.replace("“", " ").replace("”", " ") + " " + row["note"]))
        n_full, _, _ = occurrences(rf"(?<!\w){re.escape(full)}(?!\w)", sections) if " " in full else (0, 0, "")
        last = short_name(name)
        n, chapters, where = occurrences(rf"\b{re.escape(last)}\b", sections)
        rows.append((name, row["chinese"], n_full, n, chapters, where))
    tsv("people.tsv", ("name", "chinese", "full name in text", "short name in text", "chapters", "first"), rows)
    return known


def uncovered_persons(sections, known):
    """spaCy PERSON entities whose words are all missing from people-zh.tsv, to check by hand."""
    try:
        import spacy
    except ImportError:
        print("spaCy not installed: skipped the PERSON entity check")
        return
    nlp = spacy.load("en_core_web_sm")
    found = Counter()
    for cid, text in sections:
        for block in text.split("\n\n"):
            if block.startswith("#") or block.strip() == "---":
                continue
            for ent in nlp(" ".join(re.sub(r"[*_>]", "", block).split())).ents:
                if ent.label_ == "PERSON":
                    words = [re.sub(r"’s?$", "", w) for w in re.split(r"[\s.]+", ent.text) if w]
                    if not any(w in known for w in words):
                        found[ent.text] += 1
    print(f"PERSON entities not in people-zh.tsv ({len(found)}):", ", ".join(f"{k} {v}" for k, v in found.most_common()))


def glossary_table():
    """{English label: Chinese} from the core-term table of glossary.md."""
    out = {}
    for line in (BOOK / "glossary.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("| ") and len(cells) == 7 and cells[0] not in ("英文", "---"):
            out[cells[0]] = cells[1]
    return out


def fill_glossary(counts):
    """Write the computed first chapter and count into the core-term table of glossary.md."""
    path = BOOK / "glossary.md"
    lines = []
    for line in path.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("| ") and len(cells) == 7 and cells[0] in counts:
            n, first = counts[cells[0]]
            cells[4], cells[5] = first, str(n)
            line = "| " + " | ".join(cells) + " |"
        lines.append(line)
    path.write_text("\n".join(lines) + "\n")


def main(candidates_path):
    OUT.mkdir(parents=True, exist_ok=True)
    sections = body_sections()
    ids = {Path(c["file"]).name: c["id"] for c in json.loads((BOOK / "book.json").read_text())["chapters"]}

    data = json.loads(Path(candidates_path).read_text())["english"]
    rows = []
    for c in data:
        docs = {ids.get(Path(d).name, Path(d).name): n for d, n in c["documents"].items()}
        first = next((cid for cid, _ in sections if cid in docs), "")
        forms = ", ".join(f"{f} {n}" for f, n in sorted(c["forms"].items(), key=lambda x: -x[1])[:3])
        rows.append((c["candidate"], c["frequency"], len(docs), first, len(c["candidate"].split()), forms))
    rows.sort(key=lambda r: (-r[1], r[0]))
    tsv("candidates.tsv", ("candidate", "frequency", "chapters", "first", "words", "forms"), rows)

    known = people(sections)
    uncovered_persons(sections, known)

    defs = []
    for cid, sentence in sentences(sections):
        found = DEFINITION.search(sentence)
        if found:
            defs.append((cid, found.group(0).strip(", "), sentence))
    tsv("definitions.tsv", ("chapter", "signal", "sentence"), defs)

    heads = [(cid, line[2:]) for cid, text in sections for line in text.split("\n") if line.startswith("# ")]
    tsv("headings.tsv", ("chapter", "heading"), heads)

    chinese, counts, evidence = glossary_table(), {}, []
    all_sentences = list(sentences(sections))
    for label, pattern, case in GLOSSARY:
        flags = 0 if case else re.I
        n, chapters, first = occurrences(pattern, sections, flags)
        example = next((s for cid, s in all_sentences if cid == first and re.search(pattern, s, flags)), "")
        counts[label] = (n, first)
        evidence.append((label, chinese.get(label, ""), n, chapters, first, example, "Claude（初定）"))
    missing = [label for label in chinese if label not in counts]
    if missing:
        print("glossary.md terms without a pattern here:", "; ".join(missing))
    tsv("glossary-evidence.tsv", ("term", "chinese", "count", "chapters", "first", "example", "decided by"), evidence)
    fill_glossary(counts)


if __name__ == "__main__":
    main(sys.argv[1])
