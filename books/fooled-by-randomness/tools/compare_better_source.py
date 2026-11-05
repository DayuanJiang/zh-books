"""Compare en/ with the better source (the Random House e-book unpacked from the user's MOBI), block by block.

    uv run --project framework/tools python -I books/fooled-by-randomness/tools/compare_better_source.py new.epub
    uv run --project framework/tools python -I books/fooled-by-randomness/tools/compare_better_source.py new.epub \
        --places books/fooled-by-randomness/review/note-places.tsv

The imported text came from an Epubor conversion of an earlier revision of the same e-book (see review/source.md).
This script reads the better EPUB directly from the zip file and prints, for every section of book.json:

- word differences: words are lowercased and compared in order without punctuation, as in check_source.py,
  so missing, extra or changed words show up together with the en/ line they belong to;
- character differences: paragraphs with the same words but different characters (punctuation, accents),
  after removing Markdown emphasis; heading case and the chapter number words are ignored;
- figures and tables: every image of the better source, with its caption and whether en/ has an image or a
  Markdown table there. Tables rebuilt from images are left out of the word comparison;
- notes: the better source links each note of "A Trip to the Library" to a place in the text (an empty
  <span id="nts_NNN">); the place is printed as the en/ file and line of the paragraph that holds it, and
  written to a TSV file with --places.

Differences that en/ keeps on purpose are listed in KEPT_WORDS and KEPT_CHARS (reasons in review/source.md)
and printed as "kept"; anything else is printed as "CHECK" and counted at the end.
"""

import difflib
import re
import sys
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import config as book_config  # noqa: E402

SOURCE = {
    "preface": 3, "summaries": 4, "prologue": 5, "part1": 6, "ch01": 7, "ch02": 8, "ch03": 9, "ch04": 10, "ch05": 11,
    "ch06": 12, "ch07": 13, "part2": 14, "ch08": 15, "ch09": 16, "ch10": 17, "ch11": 18, "part3": 19, "ch12": 20,
    "ch13": 21, "ch14": 22, "epilogue": 23, "postscript": 24, "dedication": 25, "acknowledgments-first": 26,
    "acknowledgments-second": 27, "notes": 28, "references": 29, "about-the-author": 32,
}
SKIPPED = {0: "title page", 1: "copyright", 2: "contents", 30: "footnotes (compared with chapter 7)",
           31: "other books by this author", 33: "publisher advertisement"}
# Two tiny images stand for letters with a macron in "al-Ghazālī".
LETTER_IMAGES = {"image00209.jpeg": "ā", "image00210.jpeg": "ī"}
DECORATION = {"image00199.jpeg": "title page", "cover00200.jpeg": "cover", "image00213.jpeg": "publisher logo"}
NUMBER_WORDS = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen".split()
SUBSCRIPTS = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
WORD = re.compile(r"[^\W_]+(?:[-’'.][^\W_]+)*")
MD = MarkdownIt("commonmark").enable("table")

# Word differences en/ keeps: (old words, new words) as printed, per section.
KEPT_WORDS = {f"ch{n:02d}": [(word, str(n))] for n, word in enumerate(NUMBER_WORDS, 1)}  # "One" -> "1."
KEPT_WORDS["preface"] = [("chapters13", "chapters 13")]                  # missing space in the source
KEPT_WORDS["ch01"] += [("aloof-ness", "aloofness")] + [("out-comes", "outcomes")] * 2  # print line-break hyphens
KEPT_WORDS["ch04"] += [("non-sense", "nonsense")]
KEPT_WORDS["ch06"] += [("themagnitude", "the magnitude")]                # missing space in the source
KEPT_WORDS["ch07"] += [("to return to the corresponding text click on the reference number or return to text", ""),
                       ("empiri-cism", "empiricism"), ("al-ghazälï", "al-ghazālī"), ("in-dependently", "independently")]
KEPT_WORDS["ch12"] += [("po tuit", "potuit")]                            # a stray diaeresis in the source
KEPT_WORDS["ch13"] += [("al-ghazāalīi", "al-ghazālī")]                   # letters doubled around the macron images
KEPT_WORDS["dedication"] = [("", "dedication")]                          # headings the importer added
KEPT_WORDS["about-the-author"] = [("", "about the author")]
KEPT_WORDS["acknowledgments-second"] = [("pre-and", "pre and")]          # "pre- and post-Fooled"
# Character differences en/ keeps: (old, new) pieces; a missing space after punctuation is always kept.
KEPT_CHARS = {
    "ch01": [("-", "")] * 3, "ch04": [("-", "")], "ch10": [(" ", "")],
    "ch07": [("*", "")] * 4 + [("-", ""), ("ä", "ā"), ("ï", "ī"), ("-", "")],  # asterisk markers became [^1], [^2]
    "ch13": [("a", ""), ("i", "")],
    "about-the-author": [("ASSIM", "assim"), ("ICHOLAS", "icholas"), ("ALEB", "aleb")],  # small capitals
}


def words(text):
    return WORD.findall(text.lower().translate(SUBSCRIPTS))


def squash(text):
    return " ".join(text.split())


# ---------------------------------------------------------------- better source

def source_units(html):
    """Paragraph-sized units of one XHTML file: text, note anchors in it, image file or None."""
    html = re.sub(r'<span class="ic">(\w)</span>', r"\1", html)
    soup = BeautifulSoup(html, "html.parser")
    for img in soup.find_all("img"):
        name = img["src"].rsplit("/", 1)[-1]
        if name in LETTER_IMAGES:
            img.replace_with(LETTER_IMAGES[name])
    for link in soup.find_all("a", class_="hlink", string=re.compile("Return to text")):
        link.decompose()
    for br in soup.find_all("br"):
        br.replace_with(" ")
    units = []
    for tag in soup.body.find_all(["p", "li", "img"]):
        if tag.find_parent(["p", "li"]):
            continue
        if tag.name == "img":
            units.append({"text": "", "anchors": [], "image": tag["src"].rsplit("/", 1)[-1]})
            continue
        text = squash(tag.get_text())
        anchors = [s["id"] for s in tag.find_all("span", id=re.compile(r"^nts_"))]
        if tag.find("img"):
            units.append({"text": "", "anchors": [], "image": tag.find("img")["src"].rsplit("/", 1)[-1]})
        if not text or text == "•":
            if anchors and units:
                units[-1]["anchors"] += anchors
            continue
        if "nl" in (tag.get("class") or []):
            text = re.sub(r"^\d+\.\s+", "", text)
        units.append({"text": text, "anchors": anchors, "image": None})
    return units


def note_topics(html):
    """(file number, anchor id) -> the bold topic phrase that links to it in the notes file."""
    soup = BeautifulSoup(html, "html.parser")
    topics = {}
    for link in soup.find_all("a", href=re.compile(r"#nts_\d+")):
        page, anchor = link["href"].split("#")
        topics[(int(re.search(r"\d+", page)[0]), anchor)] = squash(link.get_text())
    return topics


# ---------------------------------------------------------------- en/

def markdown_units(text):
    """Paragraph-sized units of a section file: every heading, paragraph, list item, image and table on its own."""
    lines = text.splitlines()
    body = [n for n, line in enumerate(lines) if not re.match(r"^\[\^\w+\]:", line)]
    tokens = MD.parse("\n".join(lines[n] for n in body))
    units = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        line = body[token.map[0]] + 1 if token.map else None
        if token.type == "table_open":
            j = i
            while tokens[j].type != "table_close":
                j += 1
            cells = [squash("".join(c.content for c in t.children if c.type == "text")) for t in tokens[i:j] if t.type == "inline"]
            units.append({"text": "", "line": line, "image": None, "table": squash(" ".join(cells))})
            i = j
        elif token.type == "inline":
            line = body[token.map[0]] + 1
            plain = [c.content if c.type in {"text", "code_inline"} else " " for c in token.children
                     if c.type in {"text", "code_inline", "softbreak", "hardbreak"}]
            images = [c for c in token.children if c.type == "image"]
            if images:
                units.append({"text": "", "line": line, "image": images[0].attrs.get("src")})
            text = squash(re.sub(r"\[\^\w+\]", "", "".join(plain)))
            if text:
                units.append({"text": text, "line": line, "image": None, "heading": tokens[i - 1].type == "heading_open"})
        i += 1
    for n, line in enumerate(lines):
        if re.match(r"^\[\^\w+\]:", line):
            units.append({"text": squash(re.sub(r"\*", "", line.split(":", 1)[1])), "line": n + 1, "image": None})
    return units


# ---------------------------------------------------------------- comparison

def comparable(text, heading=False):
    """Text for the character comparison; headings without case and chapter numbers."""
    text = squash(text.translate(SUBSCRIPTS))
    if heading:
        text = " ".join(w for w in words(text) if w not in NUMBER_WORDS and not w.isdigit())
    return text


def char_pieces(a, b):
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op != "equal":
            start, end = max(0, i1 - 25), min(len(a), i2 + 25)
            yield a[i1:i2], b[j1:j2], f"…{a[start:i1]}[-{a[i1:i2]}-]{{+{b[j1:j2]}+}}{a[i2:end]}…"


def compare_section(source, english):
    """Word and character differences between the units of one section: (kind, line, old, new, text)."""
    s_words, s_owner, e_words, e_owner = [], [], [], []
    for n, unit in enumerate(source):
        for w in words(unit["text"]):
            s_words.append(w)
            s_owner.append(n)
    for n, unit in enumerate(english):
        for w in words(unit["text"]):
            e_words.append(w)
            e_owner.append(n)
    found, pairs = [], {}
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, s_words, e_words, autojunk=False).get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                pairs.setdefault(e_owner[j1 + k], set()).add(s_owner[i1 + k])
            continue
        line = english[e_owner[min(j1, len(e_owner) - 1)]]["line"] if e_owner else None
        old, new = " ".join(s_words[i1:i2]), " ".join(e_words[j1:j2])
        found.append(("words", line, old, new, f"…{' '.join(s_words[max(0, i1 - 6):i1])} [-{old}-]{{+{new}+}}"))
    # Characters: an en unit whose words all come from one source unit with the same number of words.
    for e_index, owners in sorted(pairs.items()):
        unit, other = english[e_index], source[next(iter(owners))]
        if len(owners) != 1 or len(words(unit["text"])) != len(words(other["text"])):
            continue
        heading = unit.get("heading")
        a, b = comparable(other["text"], heading), comparable(unit["text"], heading)
        if heading:
            a, b = a.lower(), b.lower()
        for old, new, text in char_pieces(a, b):
            found.append(("chars", unit["line"], old, new, text))
    return found, pairs, len(s_words), len(e_words)


def classify(key, found):
    """Mark each difference as kept on purpose or to check."""
    words_left = list(KEPT_WORDS.get(key, []))
    chars_left = list(KEPT_CHARS.get(key, []))
    out = []
    for kind, line, old, new, text in found:
        if kind == "words" and (old, new) in words_left:
            words_left.remove((old, new))
            out.append(("kept", kind, line, text))
        elif kind == "chars" and (old, new) in chars_left:
            chars_left.remove((old, new))
            out.append(("kept", kind, line, text))
        elif kind == "chars" and old == "" and new == " ":
            out.append(("kept", "space", line, text))
        else:
            out.append(("CHECK", kind, line, text))
    missing = [("CHECK", "kept difference not found", None, repr(d)) for d in words_left + chars_left]
    return out + missing


def main(epub_path, places_path=None):
    epub = zipfile.ZipFile(epub_path)
    read = lambda n: epub.read(f"OEBPS/Text/part{n:04d}.xhtml").decode()  # noqa: E731
    config = book_config.load(BOOK)
    topics = note_topics(read(28))
    total_source = total_en = unexplained = 0
    figures, places = [], []
    print("Files of the better source that en/ does not keep:")
    for number, what in SKIPPED.items():
        print(f"  part{number:04d}: {what}")
    numbers = sorted({int(m[1]) for m in re.finditer(r"part(\d{4})\.xhtml", "\n".join(epub.namelist()))})
    for number in numbers:
        if number not in SOURCE.values() and number not in SKIPPED:
            print(f"  part{number:04d}: CHECK, not handled")
            unexplained += 1
    print()
    for entry in config["chapters"]:
        key, number = entry["id"], SOURCE[entry["id"]]
        source = source_units(read(number))
        if key == "ch07":  # the two asterisk notes live in the footnotes file
            source += [u for u in source_units(read(30)) if u["text"] and not u["text"].startswith(("Footnotes", "Chapter"))]
        english = markdown_units((BOOK / "en" / entry["file"]).read_text())
        found, pairs, n_source, n_en = compare_section(source, english)
        total_source += n_source
        total_en += n_en
        print(f"{key:<24} source {n_source:>6} words  en {n_en:>6} words  difference {n_en - n_source:+d}")
        for verdict, kind, line, text in classify(key, found):
            unexplained += verdict == "CHECK"
            print(f"  {verdict:<5} {kind:<6} line {line}: {text}")
        source_to_en = {}
        for e_index, owners in pairs.items():
            for s_index in owners:
                source_to_en.setdefault(s_index, e_index)
        for s_index, unit in enumerate(source):
            if unit["image"] and unit["image"] not in DECORATION:
                caption = next((source[k]["text"] for k in (s_index + 1, s_index - 1, s_index + 2, s_index - 2)
                                if 0 <= k < len(source) and len(source[k]["text"]) < 120
                                and re.match(r"^(Table|Figure) [P\d]+\.\d+(\s|$)", source[k]["text"])), "(none)")
                # The en units between the caption and the next paragraph of text.
                before = max((source_to_en[k] for k in range(s_index) if k in source_to_en), default=-1)
                after = min((source_to_en[k] for k in range(s_index + 1, len(source)) if k in source_to_en), default=len(english))
                near = english[before + 1:after] + english[max(0, before):before + 1]
                found_here = [("image " + u["image"]) if u["image"] else f"table ({len(u['table'].split())} words)"
                              for u in near if u["image"] or u.get("table")]
                if not found_here:
                    unexplained += 1
                figures.append(f"  {'ok   ' if found_here else 'CHECK'} {key:<6} {unit['image']:<16} {caption[:58]!r:<60} "
                               f"en: {', '.join(found_here) or 'nothing'}")
            for anchor in unit["anchors"]:
                if (number, anchor) not in topics:
                    continue  # the same id also exists in another file; the note links to that one
                e_index = source_to_en.get(s_index)
                line = english[e_index]["line"] if e_index is not None else None
                places.append((anchor, key, entry["file"], line, topics[(number, anchor)], unit["text"][:80]))
    print(f"\ntotal: source {total_source} words, en {total_en} words (tables rebuilt from images not counted)")
    print("\nFigures and tables of the better source:")
    print("\n".join(figures))
    linked = {anchor for _, anchor in topics}
    placed = {p[0] for p in places}
    print(f"\nNotes: {len(topics)} link to the text, {len(placed)} anchors found in kept sections; "
          f"without an anchor: {sorted(linked - placed)}; anchors without a note: {sorted(placed - linked)}")
    if places_path:
        with open(places_path, "w") as out:
            out.write("anchor\tsection\tfile\tline\tnote\tparagraph_start\n")
            for row in sorted(places):
                out.write("\t".join(str(x) for x in row) + "\n")
        print(f"note places written to {places_path}")
    print(f"\ndifferences to check: {unexplained}")
    return 1 if unexplained else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    places = args[args.index("--places") + 1] if "--places" in args else None
    sys.exit(main(args[0], places))
