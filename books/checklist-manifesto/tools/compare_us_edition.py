"""Compare en/ with the US edition EPUB (unpacked from the user's MOBI), section by section and block by block.

    uv run --project framework/tools python -I books/checklist-manifesto/tools/compare_us_edition.py new.epub

The results are in review/source.md, "用更好的来源补全（2026-11-05）". For every section the script prints:
- words (runs of letters and digits, titles left out) on both sides, paragraphs and section breaks;
- every place where the text differs, as word and punctuation tokens, with a few tokens of context; whitespace,
  emphasis marks and footnote markers are ignored, so pure formatting does not show up. "¶" ends a paragraph
  and "§" is a section break, so a paragraph split or joined on one side, or a lost break, shows up the same way;
- italic runs that differ.
Then the notes: each note of "Notes on Sources" against the footnote in the same place, the asterisk note,
the 22 run-together words that curate_source.py split by guesswork, the appendix images, and the other parts
of the US EPUB.

The XHTML that the MOBI unpacker writes puts a line break and a space after many tags. Between two letters or
digits that is a word space ("It was a</span>\n bright"); next to punctuation it is not ("patient<span/>\n .").
"""

import difflib
import re
import sys
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
sys.path.insert(0, str(BOOK / "tools"))
import config as book_config  # noqa: E402
from curate_source import FIXES  # noqa: E402

PARTS = {"dedication": 4, "introduction": 5, **{f"ch{n:02d}": 5 + n for n in range(1, 10)},
         "acknowledgments": 21, "about-the-author": 24}
EXTRA = {3: "contents (dropped)", 15: "appendix, list of the four checklists (en/ appendix)",
         16: "appendix image 1 (en/images/)", 17: "appendix image 2 (en/images/)", 18: "appendix image 3 (en/images/)",
         19: "appendix image 4 (en/images/)", 20: "notes on sources (footnotes)", 22: "additional praise (dropped)",
         23: "also by (dropped)", 25: "copyright (dropped)", 26: "asterisk note (introduction, footnote 1)",
         27: "more from the author (dropped)"}
NOTES_PART, STAR_PART = 20, 26
TITLE_CLASSES = {"class32", "class134", "class1068-0"}
BREAK_CLASS = "class86"
ITALIC = {"class1187-0", "class1187-1", "class871", "class1207", "class1220", "class1229", "class1135"}
GROUPS = {"INTRODUCTION": "introduction", **{t: f"ch{n:02d}" for n, t in enumerate(
    ["1. THE PROBLEM OF EXTREME COMPLEXITY", "2. THE CHECKLIST", "3. THE END OF THE MASTER BUILDER", "4. THE IDEA",
     "5. THE FIRST TRY", "6. THE CHECKLIST FACTORY", "7. THE TEST", "8. THE HERO IN THE AGE OF CHECKLISTS"], 1)}}
FOOTNOTE = re.compile(r"^\[\^(\d+)\]: (.*)$", re.M)
TOKEN = re.compile(r"[A-Za-z0-9]+|[^\sA-Za-z0-9]")
GAP = "\x00"
BREAK, PARA = "§", "¶"


def words(text):
    return re.findall(r"[A-Za-z0-9]+", text)


def tokens(text):
    return TOKEN.findall(text)


def settle(text):
    """Resolve the unpacker's line breaks: a space between two letters or digits, nothing elsewhere."""
    text = re.sub(r"\n\s*", GAP, text)
    text = re.sub(rf"(?<=[A-Za-z0-9]){GAP}+(?=[A-Za-z0-9])", " ", text)
    return re.sub(r" ?\x00+ ?", lambda m: " " if m[0].startswith(" ") or m[0].endswith(" ") else "", text)


def div_text(div):
    """Text of one block, and its italic runs."""
    parts, italics = [], []
    for node in div.descendants:
        if isinstance(node, NavigableString):
            parts.append(str(node))
            parent = node.parent
            while parent is not div and parent is not None:
                if ITALIC & set(parent.get("class") or []):
                    italics.append(str(node))
                    break
                parent = parent.parent
    if ITALIC & set(div.get("class") or []):
        italics = ["".join(parts)]
    return settle("".join(parts)).strip(), ["".join(words(i)) for i in italics if words(i)]


def us_section(epub, part):
    """Paragraphs in order, "§" for a section break, and the italic runs."""
    soup = BeautifulSoup(epub.read(f"OEBPS/Text/part{part:04d}.xhtml"), "html.parser")
    blocks, italics = [], []
    for div in soup.body.find_all("div", recursive=False):
        classes = set(div.get("class") or [])
        if classes & TITLE_CLASSES:
            continue
        if BREAK_CLASS in classes:
            blocks.append(BREAK)
            continue
        text, runs = div_text(div)
        if text:
            blocks.append(text)
            italics += runs
    return blocks, italics


def en_section(text):
    """The same for an en/ file: footnote markers, emphasis and escapes removed, images skipped."""
    body = FOOTNOTE.sub("", text.partition("\n")[2])
    body = re.sub(r"\[\^\w+\]", "", body)
    blocks = []
    for block in (b.strip() for b in body.split("\n\n") if b.strip()):
        if block == "---":
            blocks.append(BREAK)
            continue
        if block.startswith("![") or block.startswith("#"):
            continue
        lines = [re.sub(r"^> ?", "", line) for line in block.split("\n")]
        chunk = []
        for line in lines + [""]:
            if line.strip():
                chunk.append(line)
            elif chunk:
                blocks.append(" ".join(chunk))
                chunk = []
    italics = ["".join(words(m)) for m in re.findall(r"\*([^*]+)\*", body)]
    return [b.replace("*", "").replace("\\", "") for b in blocks], [i for i in italics if i]


def stream(blocks):
    """Tokens of a section, with "¶" at the end of every paragraph and "§" for a section break."""
    out = []
    for block in blocks:
        out += [BREAK] if block == BREAK else tokens(block) + [PARA]
    return out


def show(seq):
    out = ""
    for t in seq:
        out += t if not out or not re.match(r"[A-Za-z0-9“‘(—$]", t) or out[-1] in "“‘(—$" else " " + t
    return out


def token_diff(us, en, context=6):
    """Every differing run of tokens, with context, as (us text, en text)."""
    found = []
    matcher = difflib.SequenceMatcher(None, us, en, autojunk=False)
    for op, a1, a2, b1, b2 in matcher.get_opcodes():
        if op == "equal":
            continue
        before = show(us[max(0, a1 - context):a1])
        found.append((op, before, show(us[a1:a2]), show(en[b1:b2]), show(us[a2:a2 + context])))
    return found


def print_diffs(label, us, en):
    diffs = token_diff(us, en)
    for op, before, a, b, after in diffs:
        print(f"  {label} {op}: …{before} [US: {a!r} | en: {b!r}] {after}…")
    return len(diffs)


def main(epub_path):
    epub = zipfile.ZipFile(epub_path)
    config = book_config.load(BOOK)
    en_text = {c["id"]: (BOOK / "en" / c["file"]).read_text() for c in config["chapters"]}
    total_us = total_en = 0
    print(f"{'section':18} {'US':>6} {'en/':>6} {'diff':>5}  paragraphs  breaks")
    for key, part in PARTS.items():
        us_blocks, us_it = us_section(epub, part)
        en_blocks, en_it = en_section(en_text[key])
        us_pars = [b for b in us_blocks if b != BREAK]
        en_pars = [b for b in en_blocks if b != BREAK]
        us_words = sum(len(words(p)) for p in us_pars)
        en_words = sum(len(words(p)) for p in en_pars)
        total_us, total_en = total_us + us_words, total_en + en_words
        print(f"{key:18} {us_words:6} {en_words:6} {en_words - us_words:5}  {len(us_pars):4} {len(en_pars):4}  "
              f"{us_blocks.count(BREAK):3} {en_blocks.count(BREAK):3}")
        print_diffs("text", stream(us_blocks), stream(en_blocks))
        if us_it != en_it:
            for op, before, a, b, after in token_diff(us_it, en_it, 2):
                print(f"  italics {op}: US {a!r} | en {b!r} (after {before!r})")
    print(f"{'total':18} {total_us:6} {total_en:6} {total_en - total_us:5}")

    print("\nNotes on Sources against the footnotes")
    soup = BeautifulSoup(epub.read(f"OEBPS/Text/part{NOTES_PART:04d}.xhtml"), "html.parser")
    groups, current, us_note_words = {}, None, 0
    for div in soup.body.find_all("div", recursive=False):
        classes = set(div.get("class") or [])
        if "class873" in classes:
            current = GROUPS[div.get_text(strip=True)]
            groups[current] = []
        elif classes & {"class875", "class881"}:
            text = div_text(div)[0]
            groups[current].append(text)
            us_note_words += len(words(text))
        elif not classes & TITLE_CLASSES:
            print(f"  not a note: {div.get_text(' ', strip=True)}")
    en_note_words = 0
    for key, notes in groups.items():
        footnotes = [body for _, body in FOOTNOTE.findall(en_text[key])]
        if key == "introduction":
            footnotes = footnotes[1:]  # the asterisk note, compared below
        en_note_words += sum(len(words(f)) for f in footnotes)
        print(f"  {key}: {len(notes)} notes, {len(footnotes)} footnotes")
        for n, (note, footnote) in enumerate(zip(notes, footnotes), 1):
            print_diffs(f"note {n}", tokens(note), tokens(footnote.replace("*", "")))
    print(f"  words: {us_note_words} in the US notes, {en_note_words} in the footnotes")

    star = BeautifulSoup(epub.read(f"OEBPS/Text/part{STAR_PART:04d}.xhtml"), "html.parser").body.get_text(" ", strip=True)
    first = FOOTNOTE.findall(en_text["introduction"])[0][1]
    print(f"\nAsterisk note: US {star!r}\n  en/ footnote 1: {first!r} -> "
          f"{'same' if words(star) == words(first) else 'DIFFERENT'}")
    marker = re.search(r".{40}\*", " ".join(us_section(epub, PARTS["introduction"])[0]))
    print(f"  the asterisk in the US text: …{marker[0] if marker else 'not found'}")

    print("\nRepairs of curate_source.py (22 run-together words and the others), checked against the US text")
    us_all = {key: tokens(" ".join(b for b in us_section(epub, part)[0] if b != BREAK)) for key, part in PARTS.items()}
    for section, wrong, right, count in FIXES:
        want, text = tokens(right.replace("*", "")), us_all[section]
        found = sum(text[i:i + len(want)] == want for i in range(len(text)))
        print(f"  {section:16} {wrong!r:26} -> {right!r:26} in the US text: {found} (en/ has {count})")

    print("\nThe appendix: its images in en/ against the US EPUB")
    appendix = next((c for c in config["chapters"] if c["id"] == "appendix"), None)
    if appendix:
        text = en_text["appendix"]
        for src in re.findall(r"\]\((images/[^)]+)\)", text):
            same = [m for m in epub.namelist() if m.startswith("OEBPS/Images/") and
                    epub.read(m) == (BOOK / "en" / src).read_bytes()]
            print(f"  {src}: {'same bytes as ' + same[0] if same else 'NOT in the US EPUB'}")
    else:
        print("  en/ has no appendix yet")

    print("\nThe other parts of the US EPUB, and what en/ does with them")
    for part, name in EXTRA.items():
        soup = BeautifulSoup(epub.read(f"OEBPS/Text/part{part:04d}.xhtml"), "html.parser")
        text = " ".join(soup.body.get_text(" ", strip=True).split())
        images = [img["src"] for img in soup.find_all("img")]
        print(f"  part{part:04d} {name}: {len(words(text))} words, images {images}: {text[:90]}")


if __name__ == "__main__":
    main(sys.argv[1])
