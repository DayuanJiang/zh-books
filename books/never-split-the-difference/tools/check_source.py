"""Compare en/ with the original EPUB: words per section, the word sequence, and every paragraph once.

    uv run --project framework/tools python -I books/never-split-the-difference/tools/check_source.py book.epub

- Words: whitespace-separated tokens that contain a letter or digit, counted in the text of the chapter's
  file in the EPUB and in the Markdown text of its en/ file (headings, paragraphs, list items, quotes).
- Left out on both sides: the label "CHAPTER 1" of the EPUB and the "1." the Markdown heading puts in its place.
- The chapter subtitle comes from the EPUB's table of contents; it is counted on its own line.
- The number of an ordered list item counts as text on both sides ("1." is a bold run in the EPUB).
- Sequence: the letters and digits of both sides, in order, must be identical (nothing lost, added or moved).
- Paragraphs: every non-empty paragraph and heading of the EPUB must match exactly one block or list item
  of the Markdown, and the other way round.
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
from prepare_epub import chapter_files  # noqa: E402

CHAPTER = re.compile(r"^CHAPTER \d+$")
# Differences in the word count that the curation makes on purpose: en/ words minus EPUB and TOC words.
EXPECTED = {"09-9-bargain-hard.md": (-1, 'the stray space in "http://info .blackswanltd.com" is removed')}


def words(text):
    return [t for t in text.split() if re.search(r"[A-Za-z0-9]", t)]


def key(text):
    """Letters and digits only, lowercased: the same words whatever the markup and punctuation."""
    return re.sub(r"[^a-z0-9]", "", text.lower())


def source_units(html):
    body = BeautifulSoup(html, "html.parser").body
    units = []
    for tag in body.find_all(["p", "h2"]):
        text = " ".join(tag.get_text().split())
        if text and not CHAPTER.match(text):
            units.append(text)
    return units


def markdown_units(path):
    tokens = MarkdownIt("commonmark").parse(path.read_text())
    units, number = [], None
    for token in tokens:
        if token.type == "list_item_open":
            number = f"{token.info}. " if token.info else ""
        if token.type == "inline":
            text = "".join(c.content if c.type in ("text", "code_inline") else " " if "break" in c.type else ""
                           for c in token.children)
            units.append((number or "") + " ".join(text.split()))
            number = None
    units[0] = re.sub(r"^\d+\. ", "", units[0])  # the chapter number in the first heading
    return units


def main(epub_path):
    epub = zipfile.ZipFile(epub_path)
    chapters = chapter_files(epub.read("nav.xhtml").decode())
    entries = [line for line in (BOOK / "book.json").read_text().splitlines() if '"file"' in line]
    names = [re.search(r'"file": "([^"]+)"', line)[1] for line in entries]
    total = Counter()
    problems = 0
    print(f"{'section':40} {'EPUB':>6} {'TOC':>4} {'en/':>6}  blocks")
    for (file, number, subtitle), name in zip(chapters, names):
        source = source_units(epub.read(file).decode())
        source.insert(1, subtitle)  # the subtitle follows the title in en/
        markdown = markdown_units(BOOK / "en" / name)
        source_words = sum(len(words(u)) for u in source) - len(words(subtitle))
        toc_words = len(words(subtitle))
        md_words = sum(len(words(u)) for u in markdown)
        total.update(source=source_words, toc=toc_words, md=md_words)
        same_sequence = key(" ".join(source)) == key(" ".join(markdown))
        unmatched = Counter(key(u) for u in source)
        unmatched.subtract(Counter(key(u) for u in markdown))
        extra = {k: v for k, v in unmatched.items() if v}
        expected, reason = EXPECTED.get(name, (0, ""))
        flag = "" if source_words + toc_words + expected == md_words and same_sequence and not extra else "  <-- check"
        problems += bool(flag)
        print(f"{name:40} {source_words:6} {toc_words:4} {md_words:6}  {len(source)}/{len(markdown)}{flag}")
        if expected:
            print(f"    {expected:+d} word: {reason}")
        if not same_sequence:
            print("    word sequence differs")
        for k, v in extra.items():
            print(f"    {'missing in en/' if v > 0 else 'extra in en/'} x{abs(v)}: {k[:80]}")
    notes = sum((BOOK / "en" / n).read_text().count("[^") for n in names)
    print(f"{'total':40} {total['source']:6} {total['toc']:4} {total['md']:6}")
    print(f"footnote markers in en/: {notes}")
    print("all sections match" if not problems else f"{problems} sections to check")


if __name__ == "__main__":
    main(sys.argv[1])
