"""Turn the imported EPUB into this book's structure (see review/source.md for why each step exists).

Run after prepare_epub.py and the import (the commands are in prepare_epub.py), with the original EPUB:
- Drop the sections that are not text to translate: cover, title page, copyright page, notes (after their
  move), publisher advertisement. The cover from the EPUB becomes the bookshelf cover.
- Move every endnote into the section that cites it as a footnote [^n], placed right after the phrase the
  note quotes. The note keeps that phrase as its lead-in, in bold (in the book it is the link back).
- One level 1 heading per section ("# 1. A Purposeful Life"), "—" scene breaks as rules, short ids,
  no zero-width or no-break spaces.
"""

import hashlib
import re
import shutil
import sys
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify

BOOK = Path(__file__).resolve().parents[1]
EN = BOOK / "en"
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import config as book_config  # noqa: E402

NOTES = "OEBPS/Carr_9781524731663_epub3_nts_r1.xhtml"
COVER = "OEBPS/images/Carr_9781524731663_epub3_001_cvi.jpg"
DROP = {
    "cover": "cover image", "title-page": "title page image", "copyright": "copyright page",
    "notes": "notes section, moved into the chapters as footnotes",
    "what-s-next-on-your-reading-list": "publisher advertisement",
}
RENAME = {"author-s-note": "authors-note"}
MARKER = re.compile(r"ZZNOTE(\d+)ZZ")
CLOSING = "?!’”*"


def render_notes(epub_path):
    """[(lead-in, body)] for every note in the notes file, in order, as Markdown."""
    page = BeautifulSoup(zipfile.ZipFile(epub_path).read(NOTES), "html.parser")
    notes = []
    for paragraph in page.find_all("p", class_="para-en"):
        links = [a for a in paragraph.find_all("a", href=True) if "#Y_" in a["href"]]
        key = " ".join("".join(a.get_text() for a in links).split())
        for link in links:
            link.unwrap()
        text = " ".join(markdownify(str(paragraph)).split())
        notes.append(split_note(text, key))
    return notes


def split_note(text, key):
    """Split 'She had just been profiled in *Inc.:* Jasmine ...' into its lead-in and its body."""
    i = j = 0
    while j < len(key):
        if i >= len(text):
            raise SystemExit(f"error: note lead-in {key!r} not found in {text[:80]!r}")
        if text[i] == key[j]:
            i, j = i + 1, j + 1
        elif text[i] in "*\\ ":  # emphasis, escapes, and spaces that sit between two links
            i += 1
        elif key[j] == " ":
            j += 1
        else:
            raise SystemExit(f"error: note lead-in {key!r} not found in {text[:80]!r}")
    colon = text.index(":", i)
    if text[i:colon].strip("*”’ "):
        raise SystemExit(f"error: no colon after the lead-in of {text[:80]!r}")
    lead, body = text[:colon], text[colon + 1:]
    while body.startswith("*"):  # an italic word closed after the colon: "*Inc.:*"
        lead, body = lead + "*", body[1:]
    return lead.strip(), body.strip()


def place(text, start, phrase):
    """Where the footnote goes: after the quoted phrase when the text right after the anchor matches it."""
    i, j = start, 0
    folded = phrase.replace("*", "").replace("\\", "").strip("“”\"' ").replace("’", "'").lower()
    while i < len(text) and text[i] in "“\"*":
        i += 1
    while j < len(folded) and i < len(text):
        c = text[i].replace("’", "'").lower()
        if c in "*\\":
            i += 1
        elif c == folded[j] or (c.isspace() and folded[j].isspace()):
            i, j = i + 1, j + 1
        else:
            return None
    if j < len(folded):
        return None
    while i < len(text) and text[i] in CLOSING:
        i += 1
    return i


def add_footnotes(text, notes, stats, missed):
    """Replace the markers of a section with [^1], [^2], ... and append the definitions."""
    definitions = []
    while found := MARKER.search(text):
        k = int(found.group(1))
        n = len(definitions) + 1
        lead, body = notes[k]
        rest = text[:found.start()] + text[found.end():]
        at = place(rest, found.start(), lead)
        if at is None:
            # After a drop cap word or a small-caps lead-in the anchor sits a word or two into the phrase.
            at = place(rest, rest.rfind("\n", 0, found.start()) + 1, lead)
            at = at if at is not None and at >= found.start() else None
            stats["phrase starts before the anchor"] += at is not None
        else:
            stats["after phrase"] += 1
        if at is None:
            stats["at anchor"] += 1
            missed.append((k, lead, rest[max(0, found.start() - 40):found.start() + 60]))
            at = found.start()
        text = rest[:at] + f"[^{n}]" + rest[at:]
        definitions.append(f"[^{n}]: **{lead}:** {body}")
    return text.rstrip() + ("\n\n" + "\n".join(definitions) if definitions else "") + "\n"


def tidy(entry, text):
    """One level 1 heading: '# | TWENTY-TWO |' and '# La Mattanza' become '# 22. La Mattanza'.

    The book sets the Italian title of chapter 22 in italics; the heading stays plain, because the reader
    shows a chapter title as plain text and would show the asterisks.
    """
    lines = text.split("\n")
    if entry.get("number"):
        number = entry["number"]
        if not re.fullmatch(r"# \| [A-Z-]+ \|", lines[0]) or not lines[2].startswith("# "):
            raise SystemExit(f"error: unexpected chapter headings in {entry['file']}: {lines[:3]}")
        lines[:3] = [f"# {number}. {lines[2][2:]}"]
    text = "\n".join(lines)
    # A scene break is a rule followed by a hidden "—" paragraph.
    text = re.sub(r"(?m)^---\n\n—$", "---", text)
    if re.search(r"(?m)^—$", text):
        raise SystemExit(f"error: a lone dash paragraph is left in {entry['file']}")
    return text


def plain_spaces(text):
    """Zero-width spaces (line-break hints inside web addresses) go; no-break spaces become spaces."""
    return text.replace("\u200b", "").replace("\xa0", " ")


def main(epub_path):
    config = book_config.load(BOOK)
    notes = render_notes(epub_path)
    stats = {"after phrase": 0, "phrase starts before the anchor": 0, "at anchor": 0}
    missed, kept = [], []
    for entry in config["chapters"]:
        path = EN / entry["file"]
        if entry["id"] in DROP:
            path.unlink()
            continue
        entry["id"] = RENAME.get(entry["id"], entry["id"])
        path.write_text(plain_spaces(add_footnotes(tidy(entry, path.read_text()), notes, stats, missed)))
        kept.append(entry)
    left = [p.name for p in EN.glob("*.md") if MARKER.search(p.read_text())]
    if left or sum(stats.values()) != len(notes):
        raise SystemExit(f"error: {len(notes)} notes, placed {stats}, markers left in {left}")
    shutil.rmtree(EN / "images")
    (BOOK / "assets" / "images").mkdir(parents=True, exist_ok=True)
    (BOOK / "assets" / "images" / "cover.jpg").write_bytes(zipfile.ZipFile(epub_path).read(COVER))
    source = Path(epub_path)
    config.update(chapters=kept, cover="assets/images/cover.jpg", start="prologue",
                  facts=["序章、24 章与尾声", "中英逐段对照", f"{len(notes)} 条注释"],
                  source={"epub": source.name, "sha256": hashlib.sha256(source.read_bytes()).hexdigest()})
    book_config.save(BOOK, config)
    for k, lead, context in missed:
        print(f"  note {k} at its anchor: {lead!r} | {context!r}")
    print(f"{len(kept)} sections kept; {len(notes)} endnotes became footnotes: {stats}")


if __name__ == "__main__":
    main(sys.argv[1])
