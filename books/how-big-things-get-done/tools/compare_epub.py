"""Compare en/ with the EPUB of the same edition, section by section and block by block.

    uv run --with beautifulsoup4 python -I books/how-big-things-get-done/tools/compare_epub.py books/how-big-things-get-done path/to/book.epub
    uv run --with beautifulsoup4 python -I books/how-big-things-get-done/tools/compare_epub.py books/how-big-things-get-done path/to/book.epub --bibliography out.md

The EPUB is the Pan Macmillan 2023 ebook, the edition the calibre PDF of the first import was made from. The
script reads each spine document of the EPUB that belongs to a section of en/ (SECTIONS below) and turns it into
blocks in this repository's Markdown: subsection headings, paragraphs (the chapter lead is an italic paragraph),
images, the Appendix A table and the Appendix B list. Italics become *...*, note references become [^n]
(numbered per section in order, as en/ does), and the notes of the Notes and Footnotes documents become the
footnote definitions of the section that cites them; a note that runs over several paragraphs is joined with
spaces, as en/ does.

It then lines up the EPUB blocks with the blocks of the en/ file and prints, for each section:

- blocks that only one side has (missing or extra paragraphs, headings, images, tables);
- blocks whose words differ, with the changed words;
- blocks whose words are the same but whose italics or note markers differ;
- headings that differ only in letter case (the EPUB prints subsection headings in capitals);
- the same for every footnote definition, note by note;
- images that are not byte-for-byte the same file.

Spaces, line breaks and the Markdown of lists and tables are ignored. The EPUB documents that are not sections
of en/ (cover, title page, contents, praise, index, copyright) are listed at the end with their word counts.
With --bibliography the script also writes the Bibliography document as a Markdown section (title and one list).
"""

import argparse
import difflib
import hashlib
import json
import posixpath
import re
import sys
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

SECTIONS = {
    "did.xhtml": "dedication", "intro.xhtml": "introduction",
    **{f"chapter{n:03d}.xhtml": f"ch{n:02d}" for n in range(1, 10)},
    "chapter010.xhtml": "coda", "app.xhtml": "appendix-a", "appb.xhtml": "appendix-b",
    "ack.xhtml": "acknowledgments", "bib.xhtml": "bibliography", "author.xhtml": "about-the-authors",
}
NOTE_DOCUMENTS = {"notes.xhtml", "footnotes.xhtml"}
SUB = dict(zip("aeox0123456789", "ₐₑₒₓ₀₁₂₃₄₅₆₇₈₉"))
SUP = dict(zip("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
WORD = re.compile(r"\S+")


def is_pagebreak(tag):
    return tag.name == "span" and "pagebreak" in (tag.get("epub:type") or "")


def inline(node, notes):
    """Markdown of the inline content of node. notes collects the note targets in reference order."""
    out = []
    for child in node.children:
        if isinstance(child, NavigableString):
            if child.__class__.__name__ == "Comment":
                continue
            out.append(str(child))
            continue
        if not isinstance(child, Tag) or is_pagebreak(child):
            continue
        link = child.find("a", href=True) if child.name == "sup" else None
        if child.name == "sup" and link is not None and link["href"].split("#")[0] in NOTE_DOCUMENTS:
            notes.append(link["href"])
            out.append(f"[^{len(notes)}]")
        elif child.name == "sup":
            text = child.get_text()
            out.append("".join(SUP.get(c, c) for c in text) if all(c in SUP for c in text) else f"^{text}^")
        elif child.name == "sub":
            text = child.get_text()
            out.append("".join(SUB.get(c, c) for c in text) if all(c in SUB for c in text) else f"_{text}_")
        elif child.name in ("i", "em"):
            inner = inline(child, notes)
            lead, core, trail = re.match(r"^(\s*)(.*?)(\s*)$", inner, re.S).groups()
            out.append(f"{lead}*{core}*{trail}" if core else inner)
        elif child.name == "br":
            out.append(" ")
        else:
            out.append(inline(child, notes))
    return "".join(out)


def clean(text):
    text = " ".join(text.replace("﻿", "").split())
    return text.replace("**", "")  # two italic runs next to each other: *a**b* is *ab*


def epub_blocks(page, notes):
    """(kind, text) blocks of one section document; the section title is left out."""
    blocks, items = [], None
    body = page.find("section") or page.body
    for tag in body.find_all(["h2", "h3", "p", "table"]):
        if tag.find_parent(["table", "p"]) is not None:
            continue
        if tag.name == "h2" or (tag.name == "h3" and "books-by-subtitle" in (tag.get("class") or [])):
            if tag.name == "h2" and "chapter-title" in tag.get("class", []):
                inline(tag, notes)  # the Appendix A title carries a note reference
            continue
        classes = tag.get("class") or []
        image = tag.find("img")
        if image is not None and not tag.get_text(strip=True):
            if (image.get("alt") or "") == "line image":
                continue
            blocks.append(("image", image["src"]))
            continue
        if tag.name == "table":
            rows = []
            for row in tag.find_all("tr"):
                rows.append(" | ".join(clean(inline(cell, notes)) for cell in row.find_all(["th", "td"])))
            blocks.append(("table", "\n".join(rows)))
            continue
        text = clean(inline(tag, notes))
        if tag.name == "h3":
            blocks.append(("heading", text))
        elif "bibliography" in classes:
            if items is None:
                items = []
                blocks.append(("list", items))
            items.append(text)
            continue
        else:
            blocks.append(("paragraph", text))
        items = None
    return [(kind, "\n".join(text) if kind == "list" else text) for kind, text in blocks]


def note_texts(pages):
    """Markdown of every note body, by "document#id" of its anchor; continuation paragraphs are joined on."""
    found = {}
    for name in NOTE_DOCUMENTS:
        current = None
        for p in pages[name].find_all("p"):
            classes = p.get("class") or []
            if "footnote-flush-left" in classes:
                anchor = p.find("a", id=True)
                current = f"{name}#{anchor['id']}"
                anchor_text = anchor.get_text()
                anchor.decompose()
                sup = p.find("sup")
                if sup is not None and not sup.get_text(strip=True):
                    sup.decompose()
                text = clean(inline(p, []))
                text = re.sub(r"^\.\s*", "", text) if anchor_text != "*" else text
                found[current] = text
            elif "footnote-flush-left-indented" in classes and current:
                found[current] += " " + clean(inline(p, []))
    return found


def md_blocks(path):
    """(kind, text) blocks of an en/ file without its first heading, and its footnote definitions."""
    text = path.read_text()
    notes = {}
    body = []
    for line in text.splitlines():
        match = re.match(r"^\[\^(\w+)\]:\s*(.*)$", line)
        if match:
            notes[match[1]] = match[2]
        else:
            body.append(line)
    blocks = []
    for chunk in re.split(r"\n\s*\n", "\n".join(body).strip()):
        lines = chunk.strip().splitlines()
        if not lines:
            continue
        first = lines[0]
        if first.startswith("# "):
            continue
        if first.startswith("#"):
            blocks.append(("heading", clean(first.lstrip("#"))))
        elif first.startswith("!["):
            blocks.append(("image", re.search(r"\]\(([^)]+)\)", first)[1]))
        elif first.startswith("|"):
            rows = [l for l in lines if not re.fullmatch(r"[|\s:-]+", l)]
            blocks.append(("table", "\n".join(" | ".join(clean(c) for c in l.strip().strip("|").split("|")) for l in rows)))
        elif first.startswith("- "):
            blocks.append(("list", "\n".join(clean(l[2:]) for l in lines)))
        elif first.strip() == "---":
            blocks.append(("rule", "---"))
        else:
            blocks.append(("paragraph", clean(" ".join(lines))))
    return blocks, notes


def plain(text):
    """Words without italics and note markers, for matching blocks."""
    return " ".join(re.sub(r"\[\^\w+\]|\*", "", text).split())


def word_diff(a, b):
    """The changed words between two texts, as '-old +new' pieces with a little context."""
    wa, wb = WORD.findall(a), WORD.findall(b)
    pieces = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, wa, wb, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        before = " ".join(wa[max(0, i1 - 3):i1])
        after = " ".join(wa[i2:i2 + 3])
        old, new = " ".join(wa[i1:i2]), " ".join(wb[j1:j2])
        pieces.append(f"…{before} [-{old}-] {{+{new}+}} {after}…")
    return pieces


def compare_pair(label, en_text, epub_text, out):
    if en_text == epub_text:
        return 0
    if plain(en_text) == plain(epub_text):
        kind = "markup"
        if en_text.lower() == epub_text.lower():
            kind = "case"
        out.append(f"  {label}: {kind} differs")
        for piece in word_diff(en_text, epub_text)[:6]:
            out.append(f"      {piece}")
        return 1
    if plain(en_text).lower() == plain(epub_text).lower():
        out.append(f"  {label}: case differs: en {en_text!r} / epub {epub_text!r}")
        return 1
    out.append(f"  {label}: words differ")
    for piece in word_diff(plain(en_text), plain(epub_text)):
        out.append(f"      {piece}")
    return 1


def compare_section(sid, en_path, epub_name, pages, notes_by_id, zip_file, en_root):
    out = []
    refs = []
    epub = epub_blocks(pages[epub_name], refs)
    en, en_notes = md_blocks(en_path)
    keys_en = [(k, plain(t).lower()) for k, t in en]
    keys_epub = [(k, plain(t).lower()) for k, t in epub]
    matcher = difflib.SequenceMatcher(None, keys_en, keys_epub, autojunk=False)
    differences = 0
    for op, i1, i2, j1, j2 in matcher.get_opcodes():
        if op == "equal":
            for i, j in zip(range(i1, i2), range(j1, j2)):
                if en[i][0] == "image":
                    continue
                differences += compare_pair(f"block {i + 1} ({en[i][0]})", en[i][1], epub[j][1], out)
            continue
        pairs = []
        left, right = list(range(i1, i2)), list(range(j1, j2))
        for i in left:
            best = max(right, key=lambda j: difflib.SequenceMatcher(None, keys_en[i][1], keys_epub[j][1]).ratio(), default=None)
            if best is not None and en[i][0] == epub[best][0] and \
                    difflib.SequenceMatcher(None, keys_en[i][1], keys_epub[best][1]).ratio() > 0.6:
                pairs.append((i, best))
                right.remove(best)
        for i, j in pairs:
            left.remove(i)
            if en[i][0] == "image":
                continue
            differences += compare_pair(f"block {i + 1} ({en[i][0]})", en[i][1], epub[j][1], out)
        for i in left:
            if en[i][0] == "image":
                continue
            differences += 1
            out.append(f"  block {i + 1} ({en[i][0]}) only in en: {en[i][1][:120]!r}")
        for j in right:
            if epub[j][0] == "image":
                continue
            differences += 1
            out.append(f"  EPUB block {j + 1} ({epub[j][0]}) missing from en: {epub[j][1][:160]!r}")
    # Images: same files in the same order.
    en_images = [t for k, t in en if k == "image"]
    epub_images = [t for k, t in epub if k == "image"]
    if len(en_images) != len(epub_images):
        differences += 1
        out.append(f"  images: en has {len(en_images)}, EPUB has {len(epub_images)}")
    for mine, theirs in zip(en_images, epub_images):
        source = posixpath.normpath(posixpath.join("OEBPS/xhtml", theirs))
        same = hashlib.sha256((en_root / mine).read_bytes()).digest() == hashlib.sha256(zip_file.read(source)).digest()
        if not same:
            differences += 1
            out.append(f"  image {mine} differs from {source}")
    # Notes, in order.
    epub_notes = [notes_by_id[f"{posixpath.basename(href.split('#')[0])}#{href.split('#')[1]}"] for href in refs]
    en_keys = [k for k in en_notes if k.isdigit()]
    if len(en_keys) != len(epub_notes):
        differences += 1
        out.append(f"  notes: en has {len(en_keys)}, EPUB has {len(epub_notes)}")
    for n, theirs in enumerate(epub_notes, 1):
        mine = en_notes.get(str(n))
        if mine is None:
            differences += 1
            out.append(f"  note {n} missing from en: {theirs[:160]!r}")
            continue
        differences += compare_pair(f"note {n}", clean(mine), theirs, out)
    words_en = sum(len(WORD.findall(plain(t))) for k, t in en if k != "image")
    words_epub = sum(len(WORD.findall(plain(t))) for k, t in epub if k != "image")
    note_words_en = sum(len(WORD.findall(plain(t))) for k, t in en_notes.items() if k.isdigit())
    note_words_epub = sum(len(WORD.findall(plain(t))) for t in epub_notes)
    head = (f"{sid}: {len(en)} en blocks / {len(epub)} EPUB blocks, {len(en_keys)} / {len(epub_notes)} notes, "
            f"words {words_en} / {words_epub}, note words {note_words_en} / {note_words_epub}, {differences} differences")
    return head, out, (words_en, words_epub, note_words_en, note_words_epub)


def bibliography_markdown(page):
    blocks = epub_blocks(page, [])
    items = next(text for kind, text in blocks if kind == "list").split("\n")
    return "# Bibliography\n\n" + "\n".join(f"- {item}" for item in items) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("book", type=Path)
    parser.add_argument("epub", type=Path)
    parser.add_argument("--bibliography", type=Path, help="write the Bibliography document as Markdown to this file")
    args = parser.parse_args()
    config = json.loads((args.book / "book.json").read_text())
    files = {c["id"]: c["file"] for c in config["chapters"]}
    zip_file = zipfile.ZipFile(args.epub)
    pages = {}
    for name in zip_file.namelist():
        if name.startswith("OEBPS/xhtml/") and name.endswith(".xhtml"):
            pages[posixpath.basename(name)] = BeautifulSoup(zip_file.read(name), "html.parser")
    notes_by_id = note_texts(pages)
    totals = [0, 0, 0, 0]
    for epub_name, sid in SECTIONS.items():
        if sid not in files:
            refs = []
            blocks = epub_blocks(pages[epub_name], refs)
            words = sum(len(WORD.findall(plain(t))) for k, t in blocks)
            print(f"{sid}: not in book.json; EPUB {epub_name} has {len(blocks)} blocks, {words} words")
            continue
        head, out, counts = compare_section(sid, args.book / "en" / files[sid], epub_name, pages, notes_by_id,
                                            zip_file, args.book / "en")
        totals = [a + b for a, b in zip(totals, counts)]
        print(head)
        for line in out:
            print(line)
    print(f"total words en / EPUB: body {totals[0]} / {totals[1]}, notes {totals[2]} / {totals[3]}")
    others = sorted(set(pages) - set(SECTIONS) - NOTE_DOCUMENTS)
    for name in others:
        text = " ".join(pages[name].get_text(" ").split())
        print(f"not compared: {name} ({len(WORD.findall(text))} words): {text[:80]!r}")
    if args.bibliography:
        args.bibliography.write_text(bibliography_markdown(pages["bib.xhtml"]))
        print(f"wrote {args.bibliography}")


if __name__ == "__main__":
    sys.exit(main())
