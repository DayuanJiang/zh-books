"""Compare the English text in en/ with the PDF, word by word, section by section.

    uv run --with pymupdf python -I books/how-big-things-get-done/tools/verify_against_pdf.py books/how-big-things-get-done book.pdf

For each section in book.json the script reads the PDF pages of the section from the PDF outline and takes
every word in reading order, leaving out the section title (it comes from the outline) and the superscript note
numbers. On the Markdown side it takes the body without the first heading, footnote definitions, note markers,
image lines and Markdown syntax. Words are runs of letters and digits, so line breaks, hyphens and dashes do
not change the count. The notes are compared the same way: the notes the PDF prints under a chapter's heading
against the footnote definitions of that chapter, in order.

It prints the word counts and every place where the two word sequences differ. Differences that the curation
makes on purpose (fixed hyphens, the repeated table header, title case) show up here and are explained in
review/source.md.
"""

import difflib
import json
import re
import sys
from pathlib import Path

import pymupdf

WORD = re.compile(r"[A-Za-z0-9À-ÿ]+")


def fix_mojibake(text):
    try:
        return text.encode("cp1252").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text


def words(text):
    return [w.lower() for w in WORD.findall(text)]


def pdf_lines(doc, first, last):
    for pno in range(first, last + 1):
        for block in doc[pno].get_text("dict")["blocks"]:
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                spans = line["spans"]
                if any(s["text"].strip() for s in spans):
                    yield pno, line, spans


def is_title(spans):
    main = [s for s in spans if not s["flags"] & 1 and s["text"].strip()]
    return bool(main) and all("Sans" in s["font"] and s["size"] >= 16.8 for s in main)


def pdf_sections(doc):
    toc = doc.get_toc()
    out = []
    for n, (_, title, page) in enumerate(toc):
        last = (toc[n + 1][2] - 2) if n + 1 < len(toc) else doc.page_count - 1
        out.append((fix_mojibake(title), page - 1, last))
    return out


def body_words(doc, first, last):
    """Words of a section and the word positions where the PDF starts a new block.

    A block starts at a heading line that follows another kind of line, at the first line of italic lead text,
    at a body line that is indented or follows another kind of line, at a small-type line that starts a
    hanging indent, and at the first line of a table.
    """
    found, starts, previous = [], set(), None
    for _, line, spans in pdf_lines(doc, first, last):
        if is_title(spans):
            previous = "title"
            continue
        main = [s for s in spans if not s["flags"] & 1 and s["text"].strip()]
        size = max((s["size"] for s in main), default=0)
        x0 = line["bbox"][0]
        if main and all("Sans" in s["font"] for s in main):
            kind = "heading" if size >= 15 else "table"
        elif size >= 15:
            kind = "lead" if previous in ("title", None, "lead") and all(s["flags"] & 2 for s in main) else "body"
        else:
            kind = "small"
        new_words = words("".join(s["text"] for s in spans if not s["flags"] & 1))
        if new_words and (kind != previous or (kind == "body" and x0 > 85) or (kind == "small" and (x0 < 82 or x0 > 120))):
            starts.add(len(found))
        found += new_words
        if new_words:
            previous = kind
    return found, starts


def note_groups(doc, first, last):
    """Words of each note group (heading -> words) in a notes section, without note numbers."""
    groups, heading, previous_heading = {}, None, False
    for _, line, spans in pdf_lines(doc, first, last):
        if is_title(spans):
            continue
        main = [s for s in spans if not s["flags"] & 1 and s["text"].strip()]
        if main and all("Sans" in s["font"] for s in main):
            text = " ".join("".join(s["text"] for s in spans).split())
            heading = (heading + " " + text) if previous_heading else text
            previous_heading = True
            groups.setdefault(heading, [])
            continue
        if previous_heading:
            # A heading on two lines was stored under its first line too.
            for key in list(groups):
                if key != heading and heading.startswith(key) and not groups[key]:
                    del groups[key]
        previous_heading = False
        text = "".join(s["text"] for s in spans)
        if line["bbox"][0] < 82:
            text = re.sub(r"^\s*(\d{1,3}|\*)\s*\.?", "", text, count=1)
        groups[heading] += words(text)
    return groups


def markdown_parts(path):
    """Body words, note words and the word positions where a Markdown block starts."""
    text = path.read_text()
    clean = lambda s: re.sub(r"\[\^\w+\]", " ", s).replace("\\", "")
    body, notes, starts = [], [], set()
    for block in re.split(r"\n\s*\n", text.split("\n", 1)[1] if "\n" in text else ""):
        block_lines = []
        for line in block.splitlines():
            match = re.match(r"^\[\^\w+\]:\s*(.*)$", line)
            if match:
                notes += words(clean(match[1]))
            elif not line.startswith("!["):
                block_lines.append(line)
        block_text = re.sub(r"^\|?[-| ]+\|$", " ", clean("\n".join(block_lines)), flags=re.M)
        if re.match(r"\s*- ", block_text):
            items = re.split(r"(?m)^- ", block_text)
        else:
            items = [block_text]
        for item in items:
            item_words = words(item)
            if item_words:
                starts.add(len(body))
                body += item_words
    return body, notes, starts


def start_differences(pdf_words, pdf_starts, en_words, en_starts):
    """Block starts found on one side only, mapped through the word alignment."""
    mapping = {}
    for a, b, size in difflib.SequenceMatcher(None, pdf_words, en_words, autojunk=False).get_matching_blocks():
        for k in range(size):
            mapping[a + k] = b + k
    mapped = {mapping[i] for i in pdf_starts if i in mapping}
    out = []
    for i in sorted(mapped - en_starts):
        out.append(f"    block start only in PDF: {' '.join(en_words[max(0, i - 4):i])} | {' '.join(en_words[i:i + 6])}")
    for i in sorted(en_starts - mapped):
        out.append(f"    block start only in en: {' '.join(en_words[max(0, i - 4):i])} | {' '.join(en_words[i:i + 6])}")
    return out


def diff(a, b, limit=40):
    lines = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op != "equal":
            lines.append(f"    {op}: PDF [{' '.join(a[max(0, i1 - 3):i2 + 3])}] / en [{' '.join(b[max(0, j1 - 3):j2 + 3])}]")
    return lines[:limit]


def key(title):
    return re.sub(r"[^a-z0-9]", "", title.lower().replace("’", "'"))


def main():
    root, pdf = Path(sys.argv[1]), Path(sys.argv[2])
    config = json.loads((root / "book.json").read_text())
    doc = pymupdf.open(pdf)
    sections = pdf_sections(doc)
    groups = {}
    for title, first, last in sections:
        if title in ("Notes", "Footnotes"):
            groups.update(note_groups(doc, first, last))
    total_pdf = total_en = notes_pdf = notes_en = 0
    for entry in config["chapters"]:
        path = root / "en" / entry["file"]
        heading = path.read_text().splitlines()[0][2:]
        plain_heading = re.sub(r"\[\^\w+\]", "", heading).replace("*", "")
        match = None
        for title, first, last in sections:
            t = re.sub(r"^\d+\.\s*", "", title)
            if key(t) in key(plain_heading) or key(plain_heading) in key(t):
                match = (title, first, last)
                break
        if match is None:
            print(f"{entry['id']}: no PDF section for {heading!r}")
            continue
        title, first, last = match
        pdf_words, pdf_starts = body_words(doc, first, last)
        en_words, en_notes, en_starts = markdown_parts(path)
        group = next((g for name, g in groups.items() if key(re.sub(r"^\d+:\s*", "", name)) == key(title.split(". ", 1)[-1])), [])
        total_pdf += len(pdf_words)
        total_en += len(en_words)
        notes_pdf += len(group)
        notes_en += len(en_notes)
        status = "same" if pdf_words == en_words else "differs"
        print(f"{entry['id']:18} body PDF {len(pdf_words):6} en {len(en_words):6} {status}; "
              f"notes PDF {len(group):5} en {len(en_notes):5} {'same' if group == en_notes else 'differs'}")
        blocks = start_differences(pdf_words, pdf_starts, en_words, en_starts)
        print(f"{'':18} blocks PDF {len(pdf_starts):4} en {len(en_starts):4}")
        for line in diff(pdf_words, en_words) + diff(group, en_notes) + blocks:
            print(line)
    print(f"total body words: PDF {total_pdf}, en {total_en}; note words: PDF {notes_pdf}, en {notes_en}")


if __name__ == "__main__":
    main()
