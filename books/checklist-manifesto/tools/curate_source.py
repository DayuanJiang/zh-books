"""Turn the imported EPUB into this book's structure (see review/source.md for why each step exists).

Run after prepare_epub.py and the import (the commands are in prepare_epub.py):
- Drop the sections that are not text to translate: "also by" page, half titles, title page, copyright page.
  The cover from the EPUB becomes the bookshelf cover.
- Move every note of "Notes on Sources" into the chapter it belongs to as a footnote [^n], placed right after
  the phrase the note quotes, and drop the notes section. The print page number in front of each note goes.
- The asterisk note of the introduction has lost its text in this EPUB; the text from the print edition is put back.
- One level 1 heading per section in title case ("# 1. The Problem of Extreme Complexity").
- Fix what the conversion broke: spaces lost or added around dashes, quotes and colons, words split by hyphens.
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

DROP = {
    "section-1": "\"also by\" page", "section-2": "half title", "section-3": "author's name page",
    "title-page": "title page with the publisher's logo", "copyright-page": "copyright page with the FSC logo",
    "section-7": "second half title",
}
NOTES = "notes-on-sources"
TITLES = {
    "dedication": "Dedication", "introduction": "Introduction",
    "ch01": "1. The Problem of Extreme Complexity", "ch02": "2. The Checklist",
    "ch03": "3. The End of the Master Builder", "ch04": "4. The Idea", "ch05": "5. The First Try",
    "ch06": "6. The Checklist Factory", "ch07": "7. The Test", "ch08": "8. The Hero in the Age of Checklists",
    "ch09": "9. The Save", "acknowledgments": "Acknowledgments", "about-the-author": "About the Author",
}
# Note groups in "Notes on Sources", by their heading.
GROUPS = {"INTRODUCTION": "introduction", "1. THE PROBLEM OF EXTREME COMPLEXITY": "ch01", "2. THE CHECKLIST": "ch02",
          "3. THE END OF THE MASTER BUILDER": "ch03", "4. THE IDEA": "ch04", "5. THE FIRST TRY": "ch05",
          "6. THE CHECKLIST FACTORY": "ch06", "7. THE TEST": "ch07", "8. THE HERO IN THE AGE OF CHECKLISTS": "ch08"}
# The footnote of the introduction: the EPUB keeps the asterisk but not the note. Text from the print edition, p. 4.
STAR = ("stopped.\\*", "stopped.", "Identifying details were changed at John’s request.")
# Exact repairs of conversion errors: (section id, wrong, right, expected count).
FIXES = [
    ("ch01", "victimis", "victim is", 1),
    ("ch03", "line-byline", "line-by-line", 1),
    ("ch03", "O’Sulli-van", "O’Sullivan", 1),
    ("ch03", "PERSONNELONLY", "PERSONNEL ONLY", 1),
    ("ch04", "andmaintaining", "and maintaining", 1),
    ("ch04", "over whelmed", "overwhelmed", 1),
    ("ch04", "*Food and Wine*magazine", "*Food and Wine* magazine", 1),
    ("ch05", "onemillion", "one million", 1),
    ("ch05", "harmof", "harm of", 1),
    ("ch05", "Ghanawas", "Ghana was", 1),
    ("ch05", "howsick", "how sick", 1),
    ("ch05", "Sowh at", "So what", 1),
    ("ch05", "teambriefing", "team briefing", 1),
    ("ch06", "hima call", "him a call", 1),
    ("ch06", "philosophy.”When", "philosophy.” When", 1),
    ("ch06", "CAPTAIN:What", "CAPTAIN: What", 1),
    ("ch06", "ENGINEER:What", "ENGINEER: What", 1),
    ("ch06", "problemof", "problem of", 1),
    ("ch06", "getmissed", "get missed", 1),
    ("ch06", "rightmain", "right main", 1),
    ("ch06", "momentumand", "momentum and", 1),
    ("ch06", "nomatter", "no matter", 2),
    ("ch07", "themto", "them to", 1),
    ("ch07", "couldn’twork", "couldn’t work", 1),
    ("ch08", "formaking", "for making", 1),
    ("ch08", "asmuch", "as much", 1),
    ("ch08", "bymissed", "by missed", 1),
    ("ch09", "generallywell", "generally well", 1),
    ("ch09", "Hager-man", "Hagerman", 1),
    ("ch09", "side.”)We’ve", "side.”) We’ve", 1),
    ("acknowledgments", "Donald-son", "Donaldson", 1),
]
NOTE_FIXES = [
    ("New York:William", "New York: William"), ("eds.,*World", "eds., *World"), ("blog,*Wall", "blog, *Wall"),
    ("A-09-17-18,”Washington", "A-09-17-18,” Washington"), ("www .census.gov", "www.census.gov"),
    ("http:// www.slate.com", "http://www.slate.com"), ("middleseat/2009/02/ 09/", "middleseat/2009/02/09/"),
    ("Human- Computer", "Human-Computer"), ("Rose-grant", "Rosegrant"),
]
NOTE = re.compile(r"(\d+) (“.+?”)\s*:\s*(.+)")
IGNORE = set("*\\“”‘’\"'")
MARKER = re.compile(r"ZZNOTE(\d+)ZZ")


def tidy(text):
    """Repairs that apply everywhere: a space after an em dash (a print line break) and after a final f
    before a quote or apostrophe ("staff ’s", "half ”")."""
    text = re.sub(r"— (?=\S)", "—", text)
    return re.sub(r"f ([’”])", r"f\1", text)


def read_notes(text):
    """{section id: [(cue, note)]} from the notes section, in the order of the notes."""
    groups, current = {}, None
    for wrong, _ in NOTE_FIXES:
        if text.count(wrong) != 1:
            raise SystemExit(f"error: notes: expected 1 of {wrong!r}, found {text.count(wrong)}")
    for block in (b.strip() for b in text.split("\n\n")):
        if block.startswith("## "):
            current = GROUPS[block[3:]]
            groups[current] = []
        elif current and (m := NOTE.fullmatch(block)):
            cue, body = tidy(m[2]), m[3]
            for wrong, right in NOTE_FIXES:
                body = body.replace(wrong, right)
            groups[current].append((cue, f"{cue}: {body}"))
        elif current:
            raise SystemExit(f"error: not a note: {block[:80]}")
    return groups


def normalized(text):
    """Lowercase text without emphasis, escapes and quotes, single spaces; and the index of each kept character."""
    chars, where = [], []
    for i, c in enumerate(text):
        if c in IGNORE:
            continue
        if c.isspace():
            if chars and chars[-1] == " ":
                continue
            c = " "
        chars.append(c.lower())
        where.append(i)
    return "".join(chars), where


def place_notes(text, notes, report):
    """Insert a marker after the phrase each note quotes, searching forward from the previous note."""
    body_start = text.index("\n") + 1
    norm, where = normalized(text)
    start = len(normalized(text[:body_start])[0])
    inserts = []
    for k, (cue, _) in enumerate(notes):
        phrase = normalized(cue)[0].strip()
        found = norm.find(phrase, start)
        if found < 0:
            found = norm.find(phrase, len(normalized(text[:body_start])[0]))
            report.append(f"out of order: {cue}")
        if found < 0:
            raise SystemExit(f"error: phrase not found: {cue}")
        if norm.count(phrase) > 1:
            report.append(f"{norm.count(phrase)} matches, first after the previous note used: {cue}")
        end = where[found + len(phrase) - 1] + 1
        if text[end:end + 1] in tuple(",.;:?!") and text[end + 1:end + 2] in ("’", "”"):
            end += 1  # the quotation ends right after the phrase: the marker goes after the closing quote
        while end < len(text) and text[end] in "*’”":
            end += 1
        inserts.append((end, k))
        start = found + 1
    for end, k in sorted(inserts, reverse=True):
        text = text[:end] + f"ZZNOTE{k}ZZ" + text[end:]
    return text


def add_footnotes(text, notes):
    """Number the markers in reading order and append the definitions."""
    definitions = []

    def number(found):
        definitions.append(notes[int(found[1])][1])
        return f"[^{len(definitions)}]"

    text = MARKER.sub(number, text)
    if len(definitions) != len(notes):
        raise SystemExit(f"error: {len(notes)} notes but {len(definitions)} markers")
    return text.rstrip() + "\n\n" + "\n\n".join(f"[^{n}]: {d}" for n, d in enumerate(definitions, 1)) + "\n"


def fix(entry_id, text):
    for section, wrong, right, count in FIXES:
        if section == entry_id:
            if text.count(wrong) != count:
                raise SystemExit(f"error: {entry_id}: expected {count} of {wrong!r}, found {text.count(wrong)}")
            text = text.replace(wrong, right)
    return tidy(text)


def main(epub_path):
    config = book_config.load(BOOK)
    chapters = config["chapters"]
    ids = {c["id"] for c in chapters}
    if ids != set(DROP) | set(TITLES) | {NOTES}:
        raise SystemExit(f"error: unexpected sections {sorted(ids ^ (set(DROP) | set(TITLES) | {NOTES}))}")
    notes_entry = next(c for c in chapters if c["id"] == NOTES)
    groups = read_notes((EN / notes_entry["file"]).read_text())
    report, kept, placed = [], [], 0
    for entry in chapters:
        path = EN / entry["file"]
        if entry["id"] in DROP or entry["id"] == NOTES:
            path.unlink()
            continue
        text = path.read_text()
        text = f"# {TITLES[entry['id']]}\n" + text.partition("\n")[2]
        text = fix(entry["id"], text)
        notes = list(groups.get(entry["id"], []))
        if entry["id"] == "introduction":
            wrong, right, note = STAR
            if text.count(wrong) != 1:
                raise SystemExit("error: asterisk of the introduction not found")
            text = text.replace(wrong, right + f"ZZNOTE{len(notes)}ZZ")
            notes.append(("", note))
            text = place_notes(text, notes[:-1], report)
        elif notes:
            text = place_notes(text, notes, report)
        if notes:
            text = add_footnotes(text, notes)
            placed += len(notes)
        path.write_text(text)
        kept.append(entry)
    total = sum(len(g) for g in groups.values())
    if placed != total + 1:
        raise SystemExit(f"error: {total} notes and the asterisk note, {placed} placed")
    (BOOK / "assets" / "images").mkdir(parents=True, exist_ok=True)
    (BOOK / "assets" / "images" / "cover.jpg").write_bytes(
        zipfile.ZipFile(epub_path).read("OEBPS/images/9781847651877.jpg"))
    images = EN / "images"
    if images.is_dir():
        for image in images.iterdir():
            image.unlink()  # the publisher's logo and the FSC logo, used only on the dropped pages
        images.rmdir()
    source = Path(epub_path)
    config.update(chapters=kept, cover="assets/images/cover.jpg", start="introduction",
                  source={"epub": source.name, "sha256": hashlib.sha256(source.read_bytes()).hexdigest()})
    book_config.save(BOOK, config)
    print(f"{len(kept)} sections kept; {total} notes on sources and 1 asterisk note became footnotes")
    for line in report:
        print("  check:", line)


if __name__ == "__main__":
    main(sys.argv[1])
