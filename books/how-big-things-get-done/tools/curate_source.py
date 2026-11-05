"""Turn the imported PDF into this book's structure (see review/source.md for why each step exists).

    uv run --with pymupdf python -I books/how-big-things-get-done/tools/import_pdf.py books/how-big-things-get-done book.pdf --force
    uv run --with pymupdf python -I books/how-big-things-get-done/tools/curate_source.py book.pdf

Run it once on a fresh import:
- Drop the sections that are not text to translate: title page, contents, bibliography (the notes already give
  every source in full), print index (its entries are "ref1" links without page numbers), copyright page.
  The cover image of the PDF becomes the bookshelf cover.
- Give the sections short ids, "Dedication" as the dedication's heading, and the headings inside the
  sections title case (the PDF prints them in capitals).
- Fix the words the ebook conversion garbled (lost or stray hyphens, missing spaces and periods).
- Appendix A: move the note on the title into the first sentence, table header and source line in normal case.
- Appendix B: the reading list becomes a Markdown list.
"""

import re
import sys
from pathlib import Path

import pymupdf

BOOK = Path(__file__).resolve().parents[1]
EN = BOOK / "en"
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import config as book_config  # noqa: E402

DROP = {
    "title-page": "title page",
    "contents": "table of contents",
    "bibliography": "bibliography; every note already cites its source in full",
    "index": "print index; its entries are ref1, ref2 links without page numbers",
    "copyright-page": "copyright page",
}
RENAME = {
    "dedication-page": ("dedication", "02-dedication.md", "Dedication"),
    "introduction-california-dreamin": ("introduction", None, None),
    "coda-eleven-heuristics-for": ("coda", None, None),
    "appendix-a-base-rates-for-cost": ("appendix-a", None, None),
    "appendix-b-further-readings-by": ("appendix-b", None, None),
}

# Garbled words: (section id, text in the PDF, fixed text). Each must occur exactly once.
FIXES = [
    # A hyphen lost in a compound (the print edition broke the line there; the ebook dropped the hyphen).
    ("ch04", "string of eradefining movies", "string of era-defining movies"),
    ("ch04", "(CAD), computeraided manufacturing", "(CAD), computer-aided manufacturing"),
    ("ch05", "sketches, woodand-cardboard models", "sketches, wood-and-cardboard models"),
    ("ch06", "facing a fattailed distribution", "facing a fat-tailed distribution"),
    ("ch06", "comparable highspeed rail projects", "comparable high-speed rail projects"),
    ("ch06", "delays as lowerlevel employees", "delays as lower-level employees"),
    ("ch06", "it *is* realworld experience", "it *is* real-world experience"),
    ("ch07", "but also, to his surprise, lowfrequency sound", "but also, to his surprise, low-frequency sound"),
    ("ch08", "its crowded, rundown halls", "its crowded, run-down halls"),
    ("ch09", "an elegant twentysix-story Marriott", "an elegant twenty-six-story Marriott"),
    ("ch09", "with everbigger developments", "with ever-bigger developments"),
    ("ch09", "Without the governmentcreated framework", "Without the government-created framework"),
    ("ch09", "get to the ribboncutting ceremony", "get to the ribbon-cutting ceremony"),
    ("acknowledgments", "middle of us factchecking the", "middle of us fact-checking the"),
    # A line-break hyphen of the print edition left inside a word.
    ("ch01", "And a min-uscule 0.5 percent", "And a minuscule 0.5 percent"),
    ("ch05", "Administration is Domstols-styrelsen.", "Administration is Domstolsstyrelsen."),
    ("ch06", "herunder om økonomistyrings–model og", "herunder om økonomistyringsmodel og"),
    # Missing spaces and punctuation.
    ("ch09", "cannot possibly anticipate.That’s exactly", "cannot possibly anticipate. That’s exactly"),
    ("ch09", "every aspect of the business.The most", "every aspect of the business. The most"),
    ("ch09", "a role in development.“Without", "a role in development. “Without"),
    ("ch01", "over schedule, or both And 99.5 percent", "over schedule, or both. And 99.5 percent"),
    ("ch01", "But it almost never happens\n", "But it almost never happens.\n"),
    ("ch01", "Graphically, the Iron Law looks like this\n", "Graphically, the Iron Law looks like this:\n"),
]

ALT = {
    "figure-1.jpeg": "The Iron Law of Project Management: Over Budget, Over Time, Under Benefits, Over and Over Again",
    "figure-2.jpeg": "Project types arranged from fat tails to thin tails",
    "figure-3.jpeg": "New installed electricity capacity (MW), China, by technology and year",
}

SMALL = {"a", "an", "the", "and", "but", "or", "nor", "for", "to", "of", "in", "on", "at", "by", "from", "with",
         "into", "versus", "against", "as"}


def title_case(text):
    """Title case for a heading printed in capitals; italics, quotes and "A.M." stay as they are."""
    words = text.split(" ")
    out = []
    for i, word in enumerate(words):
        if re.fullmatch(r"[\W\d]*A\.M\.[\W]*", word):
            out.append(word)
            continue
        core = re.sub(r"[^A-Za-z’']", "", word).lower()
        first_or_last = i == 0 or i == len(words) - 1 or out[-1].endswith(":")
        def cap(part):
            return re.sub(r"[A-Za-z]", lambda m: m[0].upper(), part.lower(), count=1)
        if core in SMALL and not first_or_last:
            out.append(word.lower())
        else:
            out.append("".join(cap(p) for p in re.split(r"([-—])", word)))
    return " ".join(out)


def main():
    pdf = Path(sys.argv[1])
    config = book_config.load(BOOK)
    ids = {entry["id"] for entry in config["chapters"]}
    if "title-page" not in ids:
        raise SystemExit("error: run import_pdf.py --force first; this script works on a fresh import")
    chapters = []
    for entry in config["chapters"]:
        if entry["id"] in DROP:
            (EN / entry["file"]).unlink()
            continue
        if entry["id"] in RENAME:
            new_id, new_file, new_heading = RENAME[entry["id"]]
            if new_file:
                (EN / entry["file"]).rename(EN / new_file)
                entry["file"] = new_file
            if new_heading:
                path = EN / entry["file"]
                text = path.read_text()
                path.write_text(re.sub(r"^# .*", f"# {new_heading}", text, count=1))
            entry["id"] = new_id
        chapters.append(entry)
    config["chapters"] = chapters
    by_id = {entry["id"]: EN / entry["file"] for entry in chapters}

    # Headings inside sections: title case.
    for path in by_id.values():
        text = path.read_text()
        text = re.sub(r"(?m)^## (.+)$", lambda m: "## " + title_case(m[1]), text)
        path.write_text(text)

    for key, old, new in FIXES:
        path = by_id[key]
        text = path.read_text()
        if text.count(old) != 1:
            raise SystemExit(f"error: {key}: expected one {old!r}, found {text.count(old)}")
        path.write_text(text.replace(old, new))

    # Appendix A: the note on the title moves to the first sentence (a marker in the title would show in the
    # table of contents); header and source line in normal case.
    path = by_id["appendix-a"]
    text = path.read_text()
    old_head = "# Appendix A: Base Rates for Cost Risk[^1]\n"
    old_first = "The table on the next page shows cost overruns for"
    assert text.count(old_head) == 1 and text.count(old_first) == 1
    text = text.replace(old_head, "# Appendix A: Base Rates for Cost Risk\n")
    text = text.replace(old_first, "The table on the next page shows cost overruns[^1] for")
    old_header = ("| PROJECT TYPE | (A) MEAN COST OVERRUN (%)[^2] | (B) % OF PROJECTS IN TAIL (≥ 50% OVERRUN) |"
                  " (C) MEAN OVERRUN OF PROJECTS IN TAIL (%) |")
    new_header = ("| Project type | (A) Mean cost overrun (%)[^2] | (B) % of projects in tail (≥ 50% overrun) |"
                  " (C) Mean overrun of projects in tail (%) |")
    assert text.count(old_header) == 1 and text.count("\nSOURCE: FLYVBJERG DATABASE\n") == 1
    text = text.replace(old_header, new_header).replace("\nSOURCE: FLYVBJERG DATABASE\n", "\nSource: Flyvbjerg Database\n")
    path.write_text(text)

    # Appendix B: the citations after the opening paragraph become one list.
    path = by_id["appendix-b"]
    head, intro, *items = path.read_text().rstrip("\n").split("\n\n")
    assert intro.startswith("If you’re interested") and items
    path.write_text("\n\n".join([head, intro, "\n".join("- " + item for item in items)]) + "\n")

    # Figures: alt text.
    for path in by_id.values():
        text = path.read_text()
        for name, alt in ALT.items():
            text = text.replace(f"![](images/{name})", f"![{alt}](images/{name})")
        path.write_text(text)

    # Cover: the image on the first page of the PDF.
    doc = pymupdf.open(pdf)
    cover = next(b for b in doc[0].get_text("dict")["blocks"] if b["type"] == 1)
    assert cover["ext"] in ("jpeg", "jpg")
    (BOOK / "assets" / "images").mkdir(parents=True, exist_ok=True)
    (BOOK / "assets" / "images" / "cover.jpg").write_bytes(cover["image"])
    config["cover"] = "assets/images/cover.jpg"
    config["start"] = "introduction"
    config["facts"] = ["引言、9 章、结语与两篇附录", "中英逐段对照", "269 条注释"]
    book_config.save(BOOK, config)
    for path in by_id.values():
        for line in path.read_text().splitlines():
            if line.startswith("## "):
                print(f"{path.name[:24]:24} {line}")
    print(f"Curated {len(chapters)} sections.")


if __name__ == "__main__":
    main()
