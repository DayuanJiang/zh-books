"""Compare en/ with the original EPUB, section by section (the results are in review/source.md).

    uv run --project framework/tools python -I books/checklist-manifesto/tools/check_source.py book.epub

- Words: runs of letters and digits, titles left out on both sides. The difference of each section must equal
  what the repairs in curate_source.py add or remove (a joined "harmof" becomes two words, "Hager-man" one).
- Paragraphs: the letters and digits of every paragraph must match the EPUB one for one, in the same order.
- Italics: the letters inside <i> in the EPUB and inside *...* in en/ must match.
- Notes: every note of "Notes on Sources", without its page number, must be exactly one footnote.
"""

import re
import sys
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
sys.path.insert(0, str(BOOK / "tools"))
import config as book_config  # noqa: E402
from curate_source import FIXES, NOTE_FIXES, STAR  # noqa: E402

FILES = {"dedication": 7, "introduction": 10, **{f"ch{n:02d}": 10 + n for n in range(1, 10)},
         "acknowledgments": 21, "about-the-author": 22}
NOTES_FILE = 20
FOOTNOTE = re.compile(r"^\[\^(\d+)\]: (.*)$", re.M)


def words(text):
    return re.findall(r"[A-Za-z0-9]+", text)


def letters(text):
    return "".join(words(text))


def source_page(epub, number):
    soup = BeautifulSoup(epub.read(f"OEBPS/text/content{number:03d}.xhtml"), "html.parser")
    paragraphs = [p for p in soup.body.find_all("p") if "h9" not in (p.get("class") or [])]
    italics = "".join(letters(i.get_text()) for i in soup.body.find_all("i"))
    breaks = sum(1 for p in paragraphs if p.get("class") == ["tx1"] and p.find("b"))
    return paragraphs, italics, breaks


def en_page(text):
    body = FOOTNOTE.sub("", text.partition("\n")[2])
    body = re.sub(r"\[\^\d+\]", "", body)
    paragraphs, rules = [], 0
    for block in (b.strip() for b in body.split("\n\n") if b.strip()):
        if block == "---":
            rules += 1
            continue
        lines = [re.sub(r"^> ?", "", line) for line in block.split("\n")]
        chunk = []
        for line in lines + [""]:
            if line.strip():
                chunk.append(line)
            elif chunk:
                paragraphs.append(" ".join(chunk))
                chunk = []
    italics = "".join(letters(m) for m in re.findall(r"\*([^*]+)\*", body))
    return paragraphs, italics, rules


def main(epub_path):
    epub = zipfile.ZipFile(epub_path)
    config = book_config.load(BOOK)
    footnotes = []
    problems = 0
    total_src = total_en = 0
    print(f"{'section':18} {'EPUB':>6} {'en/':>6} {'diff':>5}  paragraphs  breaks  footnotes")
    for entry in config["chapters"]:
        text = (BOOK / "en" / entry["file"]).read_text()
        footnotes += [(entry["id"], body) for _, body in FOOTNOTE.findall(text)]
        src_pars, src_it, src_breaks = source_page(epub, FILES[entry["id"]])
        en_pars, en_it, en_rules = en_page(text)
        src_words = sum(len(words(p.get_text())) for p in src_pars)
        en_words = sum(len(words(p)) for p in en_pars)
        total_src, total_en = total_src + src_words, total_en + en_words
        same = [letters(p.get_text()) for p in src_pars] == [letters(p) for p in en_pars]
        if not same:
            problems += 1
            for i, (a, b) in enumerate(zip([p.get_text() for p in src_pars], en_pars)):
                if letters(a) != letters(b):
                    print(f"  first difference in paragraph {i + 1}:\n    EPUB: {a[:120]}\n    en/:  {b[:120]}")
                    break
        if src_it != en_it:
            problems += 1
            print(f"  {entry['id']}: italics differ")
        if src_breaks != en_rules:
            problems += 1
        expected = sum(count * (len(words(right)) - len(words(wrong.replace("*", ""))))
                       for section, wrong, right, count in FIXES if section == entry["id"])
        if en_words - src_words != expected:
            problems += 1
            print(f"  {entry['id']}: {en_words - src_words} words more than the EPUB, the repairs explain {expected}")
        print(f"{entry['id']:18} {src_words:6} {en_words:6} {en_words - src_words:5}  "
              f"{len(src_pars):4}={len(en_pars):<4}{'' if same else ' DIFF'}  {src_breaks:2}={en_rules:<2}  "
              f"{len(FOOTNOTE.findall(text)):3}")
    print(f"{'total':18} {total_src:6} {total_en:6} {total_en - total_src:5}")

    # Notes: each EPUB note, without the page number, is one footnote.
    soup = BeautifulSoup(epub.read(f"OEBPS/text/content{NOTES_FILE:03d}.xhtml"), "html.parser")
    notes = [re.sub(r"^\d+ ", "", p.get_text()) for p in soup.find_all("p", class_="note")]
    left = [letters(body) for _, body in footnotes]
    missing = 0
    for note in notes:
        if left.count(letters(note)) != 1:
            missing += 1
            print(f"  note not found once: {note[:80]}")
        else:
            left.remove(letters(note))
    extra = [body for _, body in footnotes if letters(body) in left]
    note_words = sum(len(words(p.get_text())) for p in soup.find_all("p", class_="note"))
    footnote_words = sum(len(words(body)) for _, body in footnotes)
    print(f"notes: {len(notes)} in the EPUB ({note_words} words with page numbers), {len(footnotes)} footnotes "
          f"({footnote_words} words); not matched: {missing}; footnotes not from the notes: {extra}")
    expected = note_words - len(notes) + len(words(STAR[2])) + sum(
        len(words(right)) - len(words(wrong)) for wrong, right in NOTE_FIXES)
    if footnote_words != expected:
        problems += 1
        print(f"  footnotes have {footnote_words} words; page numbers, repairs and the restored note explain {expected}")
    problems += missing + (extra != [STAR[2]])
    leftovers = [entry["file"] for entry in config["chapters"]
                 if re.search(r"ZZNOTE|xhtml|\\\*|\*\*", (BOOK / "en" / entry["file"]).read_text())]
    if leftovers:
        problems += 1
        print(f"  markers, EPUB links or bold left in {leftovers}")
    print("OK" if not problems else f"{problems} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
