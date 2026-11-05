"""Compare en/ with the original EPUB: words per section, the word sequence, and every paragraph once.

    uv run --project framework/tools python -I books/the-mom-test/tools/check_source.py "Fitzpatrick - The Mom Test.epub"

- Words: whitespace-separated tokens that contain a letter or digit, counted in the text of the section's
  spine files and in the Markdown text of its en/ file (headings, paragraphs, list items, quotes).
- The chapter label "CHAPTER ONE" of the EPUB and the "1." the Markdown heading puts in its place are left out.
- Sequence: the letters and digits of both sides, in order, must be identical (nothing lost, added or moved).
- Paragraphs: every non-empty paragraph, heading and list item of the EPUB must match exactly one block of
  the Markdown, and the other way round.
"""

import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from prepare_epub import SECTIONS  # noqa: E402

CHAPTER = re.compile(r"^CHAPTER [A-Z]+$")


def words(text):
    return [t for t in text.split() if re.search(r"[A-Za-z0-9]", t)]


def key(text):
    """Letters and digits only, lowercased: the same words whatever the markup and punctuation."""
    return re.sub(r"[^a-z0-9]", "", text.lower())


def source_units(epub, numbers):
    units = []
    for number in numbers:
        body = BeautifulSoup(epub.read(f"OPS/body{number}.xhtml"), "html.parser").body
        for tag in body.find_all(["p", "li", "h2", "h3"]):
            text = " ".join(tag.get_text(" ").split())
            if text and not CHAPTER.match(text):
                units.append(text)
    return units


def markdown_units(path):
    tokens = MarkdownIt("commonmark").enable("table").parse(path.read_text())
    units = []
    for token in tokens:
        if token.type == "inline":
            text = "".join(c.content if c.type in ("text", "code_inline") else " " if "break" in c.type else ""
                           for c in token.children)
            units.append(" ".join(text.split()))
    units[0] = re.sub(r"^\d+\. ", "", units[0])  # the chapter number in the first heading
    return units


def main(epub_path):
    epub = zipfile.ZipFile(epub_path)
    files = [line for line in (BOOK / "book.json").read_text().splitlines() if '"file"' in line]
    names = [re.search(r'"file": "([^"]+)"', line)[1] for line in files]
    total_source = total_md = 0
    problems = 0
    print(f"{'section':42} {'EPUB':>6} {'en/':>6}  blocks")
    for (label, numbers), name in zip(SECTIONS, names):
        source, markdown = source_units(epub, numbers), markdown_units(BOOK / "en" / name)
        source_words = sum(len(words(u)) for u in source)
        md_words = sum(len(words(u)) for u in markdown)
        total_source, total_md = total_source + source_words, total_md + md_words
        same_sequence = key(" ".join(source)) == key(" ".join(markdown))
        unmatched = Counter(key(u) for u in source)
        unmatched.subtract(Counter(key(u) for u in markdown))
        extra = {k: v for k, v in unmatched.items() if v}
        flag = "" if source_words == md_words and same_sequence and not extra else "  <-- check"
        problems += bool(flag)
        print(f"{name:42} {source_words:6} {md_words:6}  {len(source)}/{len(markdown)}{flag}")
        for k, v in extra.items():
            print(f"    {'missing in en/' if v > 0 else 'extra in en/'} x{abs(v)}: {k[:80]}")
    notes = sum((BOOK / "en" / n).read_text().count("[^") for n in names)
    print(f"{'total':42} {total_source:6} {total_md:6}")
    print(f"footnote markers in en/: {notes}")
    print("all sections match" if not problems else f"{problems} sections to check")


if __name__ == "__main__":
    main(sys.argv[1])
