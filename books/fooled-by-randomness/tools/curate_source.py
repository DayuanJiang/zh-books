"""Turn the imported EPUB into this book's structure (see review/source.md for why each step exists).

Run after prepare_epub.py and the import (the commands are in prepare_epub.py):
- Drop the sections that are not text to translate: the copyright page (imported as "Title Page"), three
  advertising pages that the site the file came from inserted, the publisher's list of the author's books and its
  reading list advertisement, and the footnotes page once its two notes are footnotes of chapter 7.
- Give the sections short ids (preface, prologue, part1, ch01, ...).
- Fix what the conversion broke: words still split by a print hyphen, missing spaces after a closing
  parenthesis or quote, a few stray spaces. The references stay as they are.
- Use the EPUB cover as the bookshelf cover; record the original EPUB, not the prepared copy, as the source.
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
    "title-page": "copyright page (the empty title page before it was skipped by the importer)",
    "s11": "advertisement of the e-book site the file came from", "s23": "same advertisement",
    "s34": "same advertisement",
    "footnotes": "its two notes became footnotes of chapter 7",
    "other-books-by-this-author": "publisher's list of the author's books",
    "what-s-next-on-your-reading-list": "publisher's advertisement",
}
RENAME = {
    "preface-taking-knowledge-less": "preface", "chapter-summaries": "summaries",
    "prologue-mosques-in-the-clouds": "prologue", "part-i-solon-s-warning": "part1",
    "part-ii-monkeys-on-typewriters": "part2", "part-iii-wax-in-my-ears": "part3",
    "epilogue-solon-told-you-so": "epilogue", "postscript-three-afterthoughts": "postscript",
    "acknowledgments-for-the-first": "acknowledgments-first", "acknowledgments-for-the-updated": "acknowledgments-second",
    "a-trip-to-the-library-notes-and": "notes",
}
# Words still split by the hyphen of a print line break, broken letters and two other slips; each must occur as
# often as listed.
FIXES = {
    "ch01": [("aloof-ness", "aloofness", 1), ("out-comes", "outcomes", 2)],
    "ch04": [("non-sense", "nonsense", 1)],
    "ch07": [("empiri-cism", "empiricism", 1), ("in-dependently", "independently", 1),
             ("al-Ghazälï", "al-Ghazālī", 1)],  # macrons turned into diaereses
    "ch12": [("po¨tuit", "potuit", 1)],  # a stray diaeresis inside the Latin
    "references": [("al-Ghazl, 1989", "al-Ghazālī, 1989", 1)],  # the letters with macrons were lost
    "ch10": [("(like myself )", "(like myself)", 1)],
    "preface": [("Chapters13", "Chapters 13", 1)],
}
# Missing spaces: ")." or ")," before a capital, a closing quote before a letter, ";" before a letter, ",“".
SPACES = [(r"\)([.,])(?=[A-Z])", r")\1 "), (r"”(?=[A-Za-z])", "” "), (r";(?=[A-Za-z])", "; "), (r",“", ", “")]
KEEP_AS_IS = {"references"}


def fix(entry, text, log):
    for old, new, count in FIXES.get(entry["id"], []):
        if text.count(old) != count:
            raise SystemExit(f"error: {entry['id']}: expected {count} of {old!r}, found {text.count(old)}")
        text = text.replace(old, new)
        log.append(f"{entry['id']}: {old} -> {new} ({count})")
    if entry["id"] not in KEEP_AS_IS:
        for pattern, replacement in SPACES:
            for found in re.finditer(pattern, text):
                log.append(f"{entry['id']}: space added in {text[max(0, found.start() - 15):found.end() + 10]!r}")
            text = re.sub(pattern, replacement, text)
    text = re.sub(r"(?<=\S) {2,}(?=\S)", " ", text)  # stray double spaces; hard breaks end a line and stay
    return re.sub(r"  \n +", "  \n", text)  # spaces at the start of a line after a hard break


def main(epub_path):
    config = book_config.load(BOOK)
    log, kept = [], []
    chapter7 = (EN / next(c["file"] for c in config["chapters"] if c["id"] == "ch07")).read_text()
    if len(re.findall(r"(?m)^\[\^\d+\]: ", chapter7)) != 2 or "[^1]" not in chapter7 or "[^2]" not in chapter7:
        raise SystemExit("error: chapter 7 should have the two asterisk notes as footnotes")
    for entry in config["chapters"]:
        path = EN / entry["file"]
        if entry["id"] in DROP:
            path.unlink()
            continue
        entry["id"] = RENAME.get(entry["id"], entry["id"])
        path.write_text(fix(entry, path.read_text(), log))
        kept.append(entry)
    if (EN / "images").is_dir():
        raise SystemExit("error: this EPUB has no images in the text; en/images should not exist")
    epub = zipfile.ZipFile(epub_path)
    (BOOK / "assets" / "images").mkdir(parents=True, exist_ok=True)
    (BOOK / "assets" / "images" / "cover.jpg").write_bytes(epub.read("EPUB/Image00001.jpg"))
    config.update(chapters=kept, cover="assets/images/cover.jpg", start="prologue",
                  facts=["序章、14 章、尾声与后记", "中英逐段对照", "书末注释与参考文献"],
                  source={"epub": Path(epub_path).name,
                          "sha256": hashlib.sha256(Path(epub_path).read_bytes()).hexdigest(),
                          "prepared": "tools/prepare_epub.py"})
    book_config.save(BOOK, config)
    print("\n".join(log))
    print(f"{len(kept)} sections kept, {len(config['chapters'])} in book.json; {len(log)} fixes")


if __name__ == "__main__":
    main(sys.argv[1])
