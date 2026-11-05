"""Turn the imported EPUB into this book's sections (see review/source.md for why each step exists).

Run after prepare_epub.py and the import (the commands are in prepare_epub.py):
- Drop the sections that are not text to translate: cover, half title, list of the author's other books,
  title page, copyright page, table of contents, the emptied notes section and two publisher advertisements.
  The cover image of the EPUB becomes the bookshelf cover; images no section uses are deleted.
- Short section ids (introduction, part1, ch01, ...).
- Footnote references sit right after the word they follow, with a space before the next word.
- Checks: every footnote is defined once and referenced once, no links into the EPUB's files are left.
"""

import hashlib
import re
import sys
import zipfile
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
EN = BOOK / "en"
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import config as book_config  # noqa: E402

# id given by the importer -> (start of the section's text, why it goes)
DROP = {
    "section-1": ("# Section 1\n\n![cover]", "cover image (used as the bookshelf cover instead)"),
    "section-2": ("# Section 2\n\nThinking in Systems", "half title page"),
    "section-3": ("# Section 3\n\nOther Books BY", "list of the author's other books"),
    "thinking-in-systems": ("# Thinking in Systems\n\n*—— A Primer ——*", "title page"),
    "section-5": ("# Section 5\n\nCopyright ©", "copyright page"),
    "part-one-system-structure-and": ("# Part One: System Structure and Behavior\n\nContents", "table of contents"),
    "notes": ("# Notes\n\n**Introduction**", "notes section: all 67 notes moved to the sections that cite them"),
    "section-27": ("# Section 27\n\nthe politics and practice", "publisher advertisement"),
    "section-28": ("# Section 28\n\nthe politics and practice", "publisher advertisement"),
}
RENAME = {
    "a-note-from-the-author": "authors-note",
    "a-note-from-the-editor": "editors-note",
    "introduction-the-systems-lens": "introduction",
    "part-one-system-structure-and-12": "part1",
    "part-two-systems-and-us": "part2",
    "part-three-creating-change-in": "part3",
    "bibliography-of-systems": "bibliography",
    "editor-s-acknowledgments": "acknowledgments",
}
EXPECTED = ["dedication", "authors-note", "editors-note", "epigraph", "introduction", "part1", "ch01", "ch02",
            "part2", "ch03", "ch04", "ch05", "part3", "ch06", "ch07", "appendix", "bibliography",
            "acknowledgments", "about-the-author"]
NOTES = 68  # 67 endnotes and the asterisk note of chapter 1


def tidy(text):
    """[^n] right after the word it belongs to, then a space before a following word."""
    text = re.sub(r"[ \t]+(\[\^\d+\])(?!:)", r"\1", text)
    text = re.sub(r"(\[\^\d+\])(?=\w)", r"\1 ", text)
    return text


def main(epub_path):
    config = book_config.load(BOOK)
    chapters = config["chapters"]
    if any(c["id"] == "introduction" for c in chapters):
        raise SystemExit("already curated; import again first")
    kept = []
    for entry in chapters:
        path = EN / entry["file"]
        text = path.read_text()
        if entry["id"] in DROP:
            start, _ = DROP[entry["id"]]
            if not text.startswith(start):
                raise SystemExit(f"error: {entry['id']} does not start with {start!r}")
            path.unlink()
            continue
        entry["id"] = RENAME.get(entry["id"], entry["id"])
        path.write_text(tidy(text))
        kept.append(entry)
    if [c["id"] for c in kept] != EXPECTED:
        raise SystemExit(f"error: unexpected sections {[c['id'] for c in kept]}")

    # Check the notes and the links.
    total = 0
    for entry in kept:
        text = (EN / entry["file"]).read_text()
        defined = re.findall(r"(?m)^\[\^(\d+)\]:", text)
        body = re.sub(r"(?m)^\[\^\d+\]:.*$", "", text)
        used = re.findall(r"\[\^(\d+)\]", body)
        if sorted(defined, key=int) != sorted(used, key=int) or len(set(used)) != len(used):
            raise SystemExit(f"error: {entry['id']}: notes defined {defined}, referenced {used}")
        if defined != [str(n) for n in range(1, len(defined) + 1)]:
            raise SystemExit(f"error: {entry['id']}: notes not numbered 1 to {len(defined)}")
        if re.search(r"\]\((?!https?:|images/)", text) or "ZZNOTE" in text or ".html" in text:
            raise SystemExit(f"error: {entry['id']}: a link into the EPUB is left")
        total += len(defined)
    if total != NOTES:
        raise SystemExit(f"error: {total} notes, expected {NOTES}")

    # Images: the cover goes to assets/, images no section shows are deleted.
    used = set()
    for entry in kept:
        used.update(re.findall(r"\]\(images/([^)]+)\)", (EN / entry["file"]).read_text()))
    for image in (EN / "images").iterdir():
        if image.name not in used:
            image.unlink()
    (BOOK / "assets" / "images").mkdir(parents=True, exist_ok=True)
    (BOOK / "assets" / "images" / "cover.jpg").write_bytes(zipfile.ZipFile(epub_path).read("OEBPS/images/cover.jpg"))

    # Record the original EPUB, not the prepared copy the importer saw.
    source = {"epub": "Meadows - Thinking in Systems.epub", "sha256": hashlib.sha256(Path(epub_path).read_bytes()).hexdigest()}
    config.update(chapters=kept, cover="assets/images/cover.jpg", start="introduction", source=source,
                  facts=["引言、7 章与附录", "中英逐段对照", "49 幅图"])
    book_config.save(BOOK, config)
    print(f"{len(kept)} sections kept, {total} notes, {len(used)} images")


if __name__ == "__main__":
    main(sys.argv[1])
