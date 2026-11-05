"""Term statistics before translating (see review/terms/README.md).

    uv run --project framework/tools python books/empire-of-ai/tools/term_stats.py book.epub candidates.json

candidates.json comes from en-zh-translation-polish's terms.py, run on the English text without footnotes.
Writes review/terms/: candidates.tsv, index-terms.tsv, people.tsv, definitions.tsv, headings.tsv.
"""

import html
import json
import re
import sys
import zipfile
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
OUT = BOOK / "review" / "terms"
INDEX_FILES = ("OEBPS/c3P9_split_000.xhtml", "OEBPS/c3P9_split_001.xhtml")
DEFINITION = re.compile(
    r"\b(we call|called|known as|dubbed|coined|the term|so-called|referred to as|nicknamed|code[- ]?named?|"
    r"stands for|short for|what (?:he|she|they|it|some|many|people|researchers) call(?:ed|s)?|a phrase|the phrase)\b", re.I)


def body_sections():
    """[(chapter id, text without footnotes)] in book order."""
    config = json.loads((BOOK / "book.json").read_text())
    out = []
    for c in config["chapters"]:
        text = (BOOK / "en" / c["file"]).read_text()
        text = re.sub(r"(?m)^\[\^\d+\]: .*\n?", "", text)
        out.append((c["id"], re.sub(r"\[\^\d+\]", "", text)))
    return out


def index_entries(epub):
    """[(heading, number of page references, sub entries)] from the print index."""
    entries = []
    for name in INDEX_FILES:
        page = epub.read(name).decode()
        for p in re.findall(r'<p class="(class_s3ps|class_s3pt|class_s3pu)">(.*?)</p>', page, flags=re.S):
            text = html.unescape(re.sub(r"<[^>]+>", "", p[1])).strip()
            refs = len(re.findall(r"<a ", p[1]))
            head = re.split(r",\s*(?=\d|see\b|See\b)", text)[0].strip().rstrip(",")
            if p[0] == "class_s3ps":
                entries.append([head, refs, []])
            elif entries:
                entries[-1][2].append(head)
    return entries


def is_person(head):
    """'Abbeel, Pieter' is a person; 'acceleration risk' and 'Abu Dhabi' are not."""
    found = re.fullmatch(r"([A-ZÀ-Ž][\w’'.-]+(?: [A-ZÀ-Ž][\w’'.-]+)*), ([A-ZÀ-Ž][\w’'.]+(?: [\w’'.]+)*)(?: \(.*\))?", head)
    return bool(found) and not re.search(r"\b(Inc|LLC|Corporation|University|Company|The)\b", head)


def occurrences(pattern, sections, flags=0):
    rx = re.compile(pattern, flags)
    counts = [(cid, len(rx.findall(text))) for cid, text in sections]
    hits = [(cid, n) for cid, n in counts if n]
    return sum(n for _, n in hits), len(hits), hits[0][0] if hits else ""


def tsv(name, header, rows):
    lines = ["\t".join(header)] + ["\t".join(str(x) for x in row) for row in rows]
    (OUT / name).write_text("\n".join(lines) + "\n")
    print(f"{name}: {len(rows)} rows")


def main(epub_path, candidates_path):
    OUT.mkdir(parents=True, exist_ok=True)
    sections = body_sections()
    ids = {Path(p).name: cid for cid, p in ((c["id"], c["file"]) for c in json.loads((BOOK / "book.json").read_text())["chapters"])}

    data = json.loads(Path(candidates_path).read_text())["english"]
    rows = []
    for c in data:
        docs = {ids.get(Path(d).name, Path(d).name): n for d, n in c["documents"].items()}
        first = next((cid for cid, _ in sections if cid in docs), "")
        forms = ", ".join(f"{f} {n}" for f, n in sorted(c["forms"].items(), key=lambda x: -x[1])[:3])
        rows.append((c["candidate"], c["frequency"], len(docs), first, len(c["candidate"].split()), forms))
    rows.sort(key=lambda r: (-r[1], r[0]))
    tsv("candidates.tsv", ("candidate", "frequency", "chapters", "first", "words", "forms"), rows)

    epub = zipfile.ZipFile(epub_path)
    people, terms = [], []
    for head, refs, subs in index_entries(epub):
        if is_person(head):
            last, first = head.split(", ", 1)
            first = re.sub(r" \(.*\)$", "", first)
            n, chapters, where = occurrences(rf"\b{re.escape(last)}\b", sections)
            people.append((f"{first} {last}", head, refs, n, chapters, where))
        else:
            key = re.sub(r" \(.*\)$", "", head)
            named = key[:1].isupper()
            n, chapters, where = occurrences(rf"\b{re.escape(key)}\b", sections, 0 if named else re.I)
            terms.append((head, "named" if named else "concept", refs, n, chapters, where, "; ".join(subs[:6])))
    tsv("people.tsv", ("name", "index heading", "index refs", "surname in text", "chapters", "first"), people)
    tsv("index-terms.tsv", ("index heading", "kind", "index refs", "in text", "chapters", "first", "sub entries"), terms)

    defs = []
    for cid, text in sections:
        for block in text.split("\n\n"):
            for sentence in re.split(r"(?<=[.?!”])\s+(?=[A-Z“])", block):
                if DEFINITION.search(sentence) and not sentence.startswith("#"):
                    defs.append((cid, DEFINITION.search(sentence).group(0), " ".join(sentence.split())))
    tsv("definitions.tsv", ("chapter", "signal", "sentence"), defs)

    heads = [(cid, line[2:]) for cid, text in sections for line in text.split("\n") if line.startswith("# ")]
    tsv("headings.tsv", ("chapter", "heading"), heads)


if __name__ == "__main__":
    main(*sys.argv[1:3])
