"""Import the calibre PDF of How Big Things Get Done into en/ and book.json, in the EPUB importer's format.

    uv run --with pymupdf python -I books/how-big-things-get-done/tools/import_pdf.py books/how-big-things-get-done book.pdf [--force]

The PDF was made by calibre from the ebook: one column, no running headers or page numbers, and real text
with font names, sizes and flags. Its outline lists every section with its first page, and its internal links
connect each note reference with its note. The importer:

- Splits the book into the sections of the PDF outline (a section runs until the next one starts).
- Reads headings from fonts: the section title area uses sans serif type of 16.9 pt and more, headings inside
  a section are sans serif 15 pt (often on two lines), body text is serif 15 pt, notes and lists serif 11.2 pt.
- Rejoins paragraphs: a body paragraph starts with an indented line (x about 92) or after a heading, image
  or table; an unindented line continues the paragraph, also across pages. Small type uses hanging indents.
- Rejoins lines: lines are joined with a space, without one after a line that ends in a hyphen, dash or slash,
  before a line that starts with a dash, and inside a URL that runs on to the next line (both ends belong to
  the same URL link of the PDF). calibre does not hyphenate words, so a hyphen at the end of a
  line is part of the text.
- Keeps italics as *...*, turns superscript note references into [^n] (numbered per section in order of first
  reference) and puts the definitions, found through the PDF links, at the end of the section that cites them.
  A notes section whose notes all moved is not written.
- Turns the one table (Appendix A) into a Markdown table and saves the figures under en/images/.

The output is a first draft; curate_source.py turns it into the text to translate.
"""

import argparse
import hashlib
import re
import sys
from pathlib import Path

import pymupdf

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "framework" / "tools"))
import config as book_config  # noqa: E402

NUMBERED = re.compile(r"^(\d{1,3})\.\s")
TABLE_COLUMNS = (200, 280, 390)  # x centers that separate the four columns of the Appendix A table


def slug(text, limit=32):
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(value) > limit:
        value = value[:limit].rsplit("-", 1)[0]
    return value


def fix_mojibake(text):
    """The outline stores UTF-8 read as cp1252 ("Dreaminâ€™"); undo that when it applies."""
    try:
        return text.encode("cp1252").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text


class Line:
    def __init__(self, page, raw):
        self.page = page
        self.spans = [s for s in raw["spans"] if s["text"].strip("\n")]
        self.x0, self.y0, self.x1, self.y1 = raw["bbox"]
        main = [s for s in self.spans if s["text"].strip() and not s["flags"] & 1] or [s for s in self.spans if s["text"].strip()]
        self.size = round(max((s["size"] for s in main), default=0), 1)
        self.sans = bool(main) and all("Sans" in s["font"] for s in main)
        self.bold = bool(main) and all(s["flags"] & 16 for s in main)
        self.italic = bool(main) and all(is_italic(s) for s in main)
        self.text = "".join(s["text"] for s in self.spans).replace("\n", "").strip()

    def kind(self):
        if not self.text.strip("﻿ \xa0"):
            return "blank"
        if self.sans and self.size >= 16.9:
            return "title"
        if self.sans and self.size >= 15:
            return "heading"
        if self.sans:
            return "table"
        if self.size >= 15:
            return "body"
        return "small"


def is_italic(span):
    return bool(span["flags"] & 2) or "Italic" in span["font"]


def is_superscript(span):
    return bool(span["flags"] & 1) and span["text"].strip() != ""


def overlaps(a, b, pad=1.0):
    return a[0] < b[2] + pad and b[0] < a[2] + pad and a[1] < b[3] + pad and b[1] < a[3] + pad


class Book:
    def __init__(self, path):
        self.doc = pymupdf.open(path)
        self.items = []  # (page index, Line or image dict), in reading order
        self.links = {}  # page index -> list of links
        for index, page in enumerate(self.doc):
            self.links[index] = page.get_links()
            for block in page.get_text("dict")["blocks"]:
                if block["type"] == 1:
                    self.items.append((index, {"image": block}))
                    continue
                for raw in block["lines"]:
                    line = Line(index, raw)
                    if line.spans:
                        self.items.append((index, line))
        toc = self.doc.get_toc()
        self.sections = []
        for n, (_, title, page) in enumerate(toc):
            end = toc[n + 1][2] - 1 if n + 1 < len(toc) else self.doc.page_count
            self.sections.append({"title": fix_mojibake(title), "first": page - 1, "last": end - 1})

    def link_at(self, page, rect, kind):
        for link in self.links.get(page, []):
            if link["kind"] == kind and overlaps(tuple(link["from"]), rect):
                return link
        return None

    def section_items(self, section):
        return [(p, item) for p, item in self.items if section["first"] <= p <= section["last"]]


class Text:
    """A run of inline content built from lines: text pieces with italic flags and note references."""

    def __init__(self):
        self.runs = []  # ("text", str, italic) or ("ref", key)
        self.last = None  # (page, last span, line) of the previous line, for URL and dash joins

    def add_line(self, book, line, refs):
        spans = [s for s in line.spans if s["text"].strip() or not is_superscript(s)]
        if self.last is not None and self.runs:
            self.join(book, line)
        first = True
        for span in spans:
            text = span["text"].replace("\n", "")
            if first:
                text = text.lstrip()
            if is_superscript(span):
                link = book.link_at(line.page, span["bbox"], 1)
                if link is not None:
                    self.runs.append(("ref", (link["page"], link["to"].y), span["text"].strip(), (line.page, span["bbox"])))
                    refs.append(self.runs[-1])
                else:
                    self.runs.append(("text", sup_text(span["text"].strip()), False))
            elif text:
                self.runs.append(("text", text, is_italic(span)))
            first = False
        # Drop trailing whitespace of the line.
        while self.runs and self.runs[-1][0] == "text" and not self.runs[-1][1].strip():
            self.runs.pop()
        if self.runs and self.runs[-1][0] == "text":
            kind, value, italic = self.runs[-1]
            self.runs[-1] = (kind, value.rstrip(), italic)
        self.last = (line.page, spans[-1] if spans else None, line)

    def join(self, book, line):
        prev_text = self.plain().rstrip()
        next_text = line.text.lstrip()
        glue = " "
        if prev_text.endswith(("-", "—", "–", "/")) or next_text.startswith(("—", "–")):
            glue = ""
        page, span, _ = self.last
        if span is not None and line.spans:
            a = book.link_at(page, span["bbox"], 2)
            b = book.link_at(line.page, line.spans[0]["bbox"], 2)
            if a is not None and b is not None and a.get("uri") == b.get("uri"):
                glue = ""
        if glue:
            italic = self.runs[-1][0] == "text" and self.runs[-1][2]
            self.runs.append(("text", glue, italic))

    def plain(self):
        return "".join(r[1] for r in self.runs if r[0] == "text")


def sup_text(text):
    return text.translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))


def escape(text):
    return text.replace("\\", "\\\\").replace("*", "\\*")


def render(runs, numbers):
    """Markdown for a run list; numbers maps note keys to footnote numbers in this section."""
    # Merge neighbouring text runs with the same style.
    merged = []
    for run in runs:
        if run[0] == "text" and merged and merged[-1][0] == "text" and merged[-1][2] == run[2]:
            merged[-1] = ("text", merged[-1][1] + run[1], run[2])
        else:
            merged.append(run)
    # A space between two italic runs belongs to the italics ("*International Railway* *Journal,*").
    for i in range(1, len(merged) - 1):
        run = merged[i]
        if (run[0] == "text" and not run[2] and not run[1].strip() and merged[i - 1][0] == "text" and merged[i - 1][2]
                and merged[i + 1][0] == "text" and merged[i + 1][2]):
            merged[i] = ("text", run[1], True)
    joined = []
    for run in merged:
        if run[0] == "text" and joined and joined[-1][0] == "text" and joined[-1][2] == run[2]:
            joined[-1] = ("text", joined[-1][1] + run[1], run[2])
        else:
            joined.append(run)
    out = []
    for run in joined:
        if run[0] == "ref":
            out.append(f"[^{numbers[run[1]]}]")
        elif run[2]:
            value = run[1]
            lead = value[: len(value) - len(value.lstrip())]
            tail = value[len(value.rstrip()):]
            core = value.strip()
            out.append(lead + (f"*{escape(core)}*" if core else "") + tail)
        else:
            out.append(escape(run[1]))
    text = "".join(out).strip()
    text = re.sub(r" {2,}", " ", text)
    # Keep paragraph starts from reading as Markdown list items or headings.
    text = re.sub(r"^(\d{1,9})([.)]) ", r"\1\\\2 ", text)
    text = re.sub(r"^([-+#>]) ", r"\\\1 ", text)
    return text


def parse_notes(book, section):
    """Notes of a notes section: {(page, y): {"label", "runs", "refs", "heading", "page", "y"}} in order."""
    notes, current, heading, last_kind = {}, None, "", None
    for page, item in book.section_items(section):
        if not isinstance(item, Line):
            continue
        kind = item.kind()
        if kind in ("title", "blank"):
            continue
        if kind == "heading":
            heading = (heading + " " + item.text) if last_kind == "heading" else item.text
            current, last_kind = None, kind
            continue
        last_kind = kind
        first = item.spans[0]["text"].strip()
        if item.x0 < 82 and (re.fullmatch(r"\d{1,3}", first) or first == "*"):
            current = {"label": first, "runs": Text(), "refs": [], "heading": heading, "page": page, "y": item.y0}
            notes[(page, item.y0)] = current
            # The number is its own span, followed by ". " ("1" + ". Ticket price ...").
            rest = [dict(s) for s in item.spans[1:]]
            if rest:
                rest[0]["text"] = re.sub(r"^\.?\s*", "", rest[0]["text"])
            stub = Line.__new__(Line)
            stub.__dict__.update(item.__dict__)
            stub.spans = [s for s in rest if s["text"]]
            stub.text = "".join(s["text"] for s in stub.spans).strip()
            current["runs"].add_line(book, stub, current["refs"])
        elif current is not None:
            current["runs"].add_line(book, item, current["refs"])
    return notes


def find_note(notes, key):
    page, y = key
    for (note_page, note_y), note in notes.items():
        if note_page == page and abs(note_y - y) < 4:
            return note
    return None


def build_table(book, lines, refs):
    """Rows of cell runs from the table lines of Appendix A: a header, then one row per project type."""
    def column(line):
        center = (line.x0 + line.x1) / 2
        return sum(center > c for c in TABLE_COLUMNS)

    header = [Text() for _ in range(4)]
    rows, header_done = [], False
    for line in lines:
        col = column(line)
        if line.bold or re.fullmatch(r"\([ABC]\)", line.text):
            if not header_done:
                header[col].add_line(book, line, refs)
            continue  # a header repeated on the next page is skipped
        header_done = True
        if col == 0 and not (rows and rows[-1]["page"] == line.page and line.y0 - rows[-1]["y"] < 16):
            rows.append({"page": line.page, "y0": line.y0, "y": line.y0, "cells": [Text() for _ in range(4)]})
        row = rows[-1] if col == 0 else min((r for r in rows if r["page"] == line.page), key=lambda r: abs(r["y0"] - line.y0))
        if col == 0:
            row["y"] = line.y0
        row["cells"][col].add_line(book, line, refs)
    return [header] + [r["cells"] for r in rows]


def render_table(rows, numbers):
    cells = [[render(c.runs, numbers) for c in row] for row in rows]
    out = ["| " + " | ".join(cells[0]) + " |", "|" + "---|" * len(cells[0])]
    return "\n".join(out + ["| " + " | ".join(row) + " |" for row in cells[1:]])


def convert_section(book, section, notes, images_dir, image_names):
    """Blocks of one section as Markdown, plus the note keys it cites in order."""
    blocks, refs = [], []
    title_refs = []
    open_text, open_kind = None, None
    table_lines = []
    seen_body = False

    def close():
        nonlocal open_text, open_kind
        if open_text is not None and open_text.runs:
            blocks.append({"kind": open_kind, "runs": open_text.runs})
        open_text, open_kind = None, None

    def flush_table():
        if table_lines:
            close()
            blocks.append({"kind": "table", "rows": build_table(book, table_lines, refs)})
            table_lines.clear()

    prev_line = None
    for page, item in book.section_items(section):
        if not isinstance(item, Line):
            block = item["image"]
            if block["bbox"][3] - block["bbox"][1] < 60 or page == 0:
                continue  # rules under titles, the cover page, publisher logos
            flush_table()
            close()
            name = f"figure-{len(image_names) + 1}.{block['ext']}"
            image_names.append(name)
            (images_dir / name).write_bytes(block["image"])
            blocks.append({"kind": "image", "name": name})
            prev_line = None
            continue
        kind = item.kind()
        if kind == "blank":
            continue
        if kind == "table":
            table_lines.append(item)
            continue
        flush_table()
        if kind == "title":
            close()
            for span in item.spans:
                if is_superscript(span):
                    link = book.link_at(page, span["bbox"], 1)
                    if link is not None:
                        run = ("ref", (link["page"], link["to"].y), span["text"].strip(), (page, span["bbox"]))
                        title_refs.append(run)
                        refs.append(run)
            prev_line = None
            continue
        if kind == "heading":
            if open_kind == "heading" and prev_line is not None and prev_line.page == page and item.y0 - prev_line.y0 < 25:
                open_text.add_line(book, item, refs)
            else:
                close()
                open_text, open_kind = Text(), "heading"
                open_text.add_line(book, item, refs)
            prev_line = item
            continue
        if kind == "body":
            # Italic lines before the first paragraph of a section: a chapter's lead, a dedication.
            teaser = item.italic and not seen_body and page == section["first"]
            if teaser:
                if open_kind != "teaser":
                    close()
                    open_text, open_kind = Text(), "teaser"
                open_text.add_line(book, item, refs)
                prev_line = item
                continue
            seen_body = True
            new = (open_kind != "body" or item.x0 > 85
                   or (prev_line is not None and prev_line.page == page and item.y0 - prev_line.y0 > 30))
            if new:
                close()
                open_text, open_kind = Text(), "body"
            open_text.add_line(book, item, refs)
            prev_line = item
            continue
        # Small type: hanging indents (x 77 starts an entry, x 88 continues it).
        new = open_kind != "small" or item.x0 < 82 or item.x0 > 120
        if new:
            close()
            open_text, open_kind = Text(), "small"
        open_text.add_line(book, item, refs)
        prev_line = item
    flush_table()
    close()

    # Number the notes this section cites, in order of first reference.
    numbers = {}
    for run in refs:
        note = find_note(notes, run[1])
        if note is None:
            continue
        numbers.setdefault(run[1], len(numbers) + 1)
    lines = []
    for block in blocks:
        if block["kind"] == "image":
            lines.append(f"![](images/{block['name']})")
        elif block["kind"] == "table":
            lines.append(render_table(block["rows"], numbers))
        elif block["kind"] == "heading":
            lines.append("## " + render(block["runs"], numbers))
        elif block["kind"] == "teaser":
            runs = [(r[0], r[1], True) if r[0] == "text" else r for r in block["runs"]]
            lines.append(render(runs, numbers))
        else:
            lines.append(render(block["runs"], numbers))
    title_marks = "".join(f"[^{numbers[r[1]]}]" for r in title_refs if r[1] in numbers)
    text = f"# {section['title']}{title_marks}\n\n" + "\n\n".join(lines)
    return text, numbers, refs


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("book", type=Path)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    root = args.book
    config = book_config.load(root)
    if config.get("chapters") and not args.force:
        raise SystemExit("error: book.json already lists chapters; use --force to import again")
    for entry in config.get("chapters", []):
        if entry["status"] != "todo":
            raise SystemExit(f"error: {entry['id']} is already being translated")
        (root / "en" / entry["file"]).unlink(missing_ok=True)
    images_dir = root / "en" / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    for old in images_dir.iterdir():
        old.unlink()

    book = Book(args.pdf)
    note_sections = [s for s in book.sections if s["title"] in ("Notes", "Footnotes")]
    notes = {}
    for section in note_sections:
        notes.update(parse_notes(book, section))
    used = {}
    chapters, ids, image_names, report = [], set(), [], []
    for section in book.sections:
        if section in note_sections:
            continue
        text, numbers, refs = convert_section(book, section, notes, images_dir, image_names)
        definitions = []
        for key, n in numbers.items():
            note = find_note(notes, key)
            used.setdefault(id(note), []).append(section["title"])
            definitions.append(f"[^{n}]: {render(note['runs'].runs, {})}")
            label = note["label"]
            first_ref = next(r for r in refs if r[1] == key)
            if label != "*" and label != first_ref[2]:
                report.append(f"{section['title']}: reference {first_ref[2]} links to note {label}")
            if label != "*" and str(n) != label:
                report.append(f"{section['title']}: note {label} became [^{n}]")
        missing = [r for r in refs if find_note(notes, r[1]) is None]
        for r in missing:
            report.append(f"{section['title']}: reference {r[2]} on page {r[3][0] + 1} has no note")
        if definitions:
            text += "\n\n" + "\n".join(definitions)
        index = len(chapters) + 1
        title = section["title"]
        match = NUMBERED.match(title)
        entry = {}
        if match and f"ch{int(match[1]):02d}" not in ids:
            entry["id"], entry["number"] = f"ch{int(match[1]):02d}", int(match[1])
        else:
            key = slug(title) or f"s{index:02d}"
            while key in ids:
                key = f"{key}-{index}"
            entry["id"] = key
        ids.add(entry["id"])
        file = f"{index:02d}-{slug(title) or 'section'}.md"
        (root / "en" / file).write_text(text.rstrip() + "\n")
        entry.update({"file": file, "status": "todo"})
        chapters.append(entry)
    unused = [n for n in notes.values() if id(n) not in used]
    twice = [n for n in notes.values() if len(used.get(id(n), [])) > 1]
    for note in unused:
        report.append(f"note {note['label']} under {note['heading']} (page {note['page'] + 1}) is never cited")
    for note in twice:
        report.append(f"note {note['label']} under {note['heading']} is cited in {used[id(note)]}")
    if not image_names:
        images_dir.rmdir()
    config["chapters"] = chapters
    config["source"] = {"pdf": args.pdf.name, "sha256": hashlib.sha256(args.pdf.read_bytes()).hexdigest()}
    book_config.save(root, config)
    cited = sum(len(v) for v in used.values())
    print(f"Imported {len(chapters)} sections, {len(notes)} notes ({cited} cited) and {len(image_names)} images from {args.pdf.name}.")
    for line in report:
        print("  " + line)


if __name__ == "__main__":
    main()
