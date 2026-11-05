"""Turn the imported EPUB into this book's structure (see review/source.md for why each step exists).

Run after prepare_epub.py and the import (the commands are in prepare_epub.py):
- Drop the sections that are not text to translate: title page, copyright page, part pages, print index,
  publisher advertisement. The cover from the EPUB becomes the bookshelf cover.
- Move every endnote into the section that cites it as a footnote [^n], placed right after the phrase the
  note quotes, and drop the notes sections.
- One level 1 heading per section ("# 1. Divine Right"), "—" scene breaks as rules, emoji images as emoji.
"""

import re
import shutil
import sys
import zipfile
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
EN = BOOK / "en"
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import config as book_config  # noqa: E402

DROP = {
    "title-page": "title page image",
    "copyright": "copyright page",
    "part-i": "part page without a title", "part-ii": "part page without a title",
    "part-iii": "part page without a title", "part-iv": "part page without a title",
    "index": "print index whose page numbers do not apply", "m": "second half of the print index",
    "what-s-next-on-your-reading-list": "publisher advertisement",
}
RENAME = {"author-s-note": "authors-note", "prologue-a-run-for-the-throne": "prologue",
          "epilogue-how-the-empire-falls": "epilogue"}
EMOJI = {"Turkey emoji": "🦃", "Parrot emoji": "🦜", "counterclockwise arrows button": "🔄"}
# A stray opening quote follows two of the emoji in the EPUB.
QUOTES = {"🦜“”": "🦜”", "🔄“,”": "🔄,”"}
MARKER = re.compile(r"ZZNOTE(\d+)ZZ")
# Two author's notes marked with an asterisk sit at the end of their chapter, after a "Skip Notes" link.
STAR_REF = re.compile(r"\[\[\\\*\]\]\(c\w+\.xhtml#\w+\)")
STAR_NOTE = re.compile(r"(?m)^\[\\\*\]\(c\w+\.xhtml#\w+\) (.*)\n?")
SKIP = re.compile(r"(?m)^\[Skip Notes\]\(c\w+\.xhtml\)\n?")
BACK_LINK = re.compile(r"\[GO TO NOTE REFERENCE IN TEXT\]\((c\w+\.xhtml)(?:#([\w-]+))?\)")
CLOSING = "?!’”*"


def is_notes(entry):
    return entry["id"] == "notes" or entry["id"].startswith("chapter-")


def collect_notes(chapters):
    """Note texts in the order of the notes files: the paragraph before each back link."""
    notes = []
    for entry in chapters:
        if is_notes(entry):
            blocks = [b.strip() for b in (EN / entry["file"]).read_text().split("\n\n") if b.strip()]
            notes += [blocks[i - 1] for i, b in enumerate(blocks) if BACK_LINK.fullmatch(b)]
    return notes


def cue(note):
    """The phrase a note quotes from the text: its lead-in up to the colon, without emphasis and quotes."""
    bold = note.find("**")
    colon = note.find(":", bold)
    return note[:colon].replace("*", "").replace("\\", "").strip("“”\"' ") if bold >= 0 and colon > 0 else ""


def place(text, start, phrase):
    """Where the footnote goes: after the quoted phrase when the text right after the anchor matches it."""
    i, j, folded = start, 0, phrase.replace("’", "'").lower()
    while i < len(text) and text[i] in "“\"*":
        i += 1
    while j < len(folded) and i < len(text):
        c = text[i].replace("’", "'").lower()
        if c in "*\\":
            i += 1
        elif c == folded[j]:
            i, j = i + 1, j + 1
        else:
            return None
    if j < len(folded):
        return None
    while i < len(text) and text[i] in CLOSING:
        i += 1
    return i


def star_notes(text, notes):
    """Turn the asterisk notes into markers too; their text is appended to notes."""
    bodies = STAR_NOTE.findall(text)
    refs = STAR_REF.findall(text)
    if len(bodies) != len(refs):
        raise SystemExit(f"error: {len(refs)} asterisk references but {len(bodies)} asterisk notes")
    text = SKIP.sub("", STAR_NOTE.sub("", text))
    for body in bodies:
        text = STAR_REF.sub(f"ZZNOTE{len(notes)}ZZ", text, count=1)
        notes.append(body)
    return text


def add_footnotes(text, notes, stats):
    """Replace the markers of a section with [^1], [^2], ... and append the definitions."""
    definitions = []
    while found := MARKER.search(text):
        k = int(found.group(1))
        n = len(definitions) + 1
        rest = text[:found.start()] + text[found.end():]
        at = place(rest, found.start(), cue(notes[k]))
        stats["after phrase" if at is not None else "at anchor"] += 1
        at = found.start() if at is None else at
        text = rest[:at] + f"[^{n}]" + rest[at:]
        definitions.append(f"[^{n}]: {notes[k]}")
    return text.rstrip() + ("\n\n" + "\n\n".join(definitions) if definitions else "") + "\n"


def tidy(entry, text):
    lines = text.split("\n")
    title = lines[0][2:]
    if entry.get("number"):
        title = f"{entry['number']}. " + title.split(": ", 1)[1]
    lines[0] = "# " + title
    # The chapter's own title heading repeats the end of the TOC label.
    second = next((i for i, line in enumerate(lines[1:], 1) if line.strip()), None)
    if second and lines[second].startswith("# ") and lines[0].endswith(lines[second][2:]):
        del lines[second:second + 2]
    text = "\n".join(lines)
    return re.sub(r"(?m)^—$", "---", text)


def emoji(text):
    for alt, char in EMOJI.items():
        text = re.sub(rf"!\[{re.escape(alt)}\]\(images/[^)]+\)", char, text)
    for wrong, right in QUOTES.items():
        text = text.replace(wrong, right)
    return text


def main(epub_path):
    config = book_config.load(BOOK)
    chapters = config["chapters"]
    notes = collect_notes(chapters)
    if entry := next((c for c in chapters if c["id"] == "epigraph"), None):
        path = EN / entry["file"]
        # The first epigraph's note has no anchor in the EPUB: it goes on the quote it names.
        path.write_text(path.read_text().replace("\nIt is said that", "\nZZNOTE0ZZIt is said that", 1))
    stats = {"after phrase": 0, "at anchor": 0}
    kept = []
    for entry in chapters:
        path = EN / entry["file"]
        if entry["id"] in DROP or is_notes(entry):
            path.unlink()
            continue
        entry["id"] = RENAME.get(entry["id"], entry["id"])
        path.write_text(emoji(add_footnotes(star_notes(tidy(entry, path.read_text()), notes), notes, stats)))
        kept.append(entry)
    left = [p.name for p in EN.glob("*.md") if MARKER.search(p.read_text())]
    if left or sum(stats.values()) != len(notes):
        raise SystemExit(f"error: {len(notes)} notes, placed {stats}, markers left in {left}")
    shutil.rmtree(EN / "images")
    (BOOK / "assets" / "images").mkdir(parents=True, exist_ok=True)
    (BOOK / "assets" / "images" / "cover.jpg").write_bytes(zipfile.ZipFile(epub_path).read("cover1.jpeg"))
    config.update(chapters=kept, cover="assets/images/cover.jpg", start="prologue")
    book_config.save(BOOK, config)
    print(f"{len(kept)} sections kept; {len(notes)} notes (endnotes and asterisk notes) became footnotes: {stats}")


if __name__ == "__main__":
    main(sys.argv[1])
