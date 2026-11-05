"""Bring en/ up to date with the US edition (the user's MOBI of the Picador paperback), after curate_source.py.

    uv run --project framework/tools python -I books/checklist-manifesto/tools/apply_us_edition.py new.epub

The findings come from compare_us_edition.py and are explained in review/source.md, "用更好的来源补全（2026-11-05）".
- Repairs are exact replacements with an expected count, like FIXES in curate_source.py. A repair that is
  already in place is skipped, so the script can run again; any other count stops it.
- The appendix with the four example checklists is written to en/, its images are copied from the US EPUB,
  and the section is added to book.json after chapter 9, as in the US edition.
zh-cn/ is translated by hand and is not touched here.
"""

import sys
import zipfile
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
EN = BOOK / "en"
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import config as book_config  # noqa: E402

# (section id, old text, new text, expected count of the old text)
REPAIRS = [
    # Words split by a space or a kept hyphen at a print line break of the old EPUB.
    ("introduction", "years of sixty, seventy-", "years of sixty-, seventy-", 1),
    ("ch01", "shifted to super-specialists.", "shifted to superspecialists.", 1),
    ("ch02", "Seattle newspaper man", "Seattle newspaperman", 1),
    ("ch03", "the fire proofing", "the fireproofing", 1),
    ("ch03", "explained tome,", "explained to me,", 1),
    ("ch05", "*Cleared for Take off*", "*Cleared for Takeoff*", 1),
    ("ch05", "button holed", "buttonholed", 1),
    ("ch05", "Effect of Hand-washing", "Effect of Handwashing", 1),
    ("ch06", "door in mid-flight", "door in midflight", 1),
    ("ch07", "my hall way", "my hallway", 1),
    ("ch08", "in under recognized", "in underrecognized", 1),
    # A typo of the old edition.
    ("ch04", "tomato soap", "tomato soup", 1),
    # Paragraphs the old EPUB split at a print page break: each falls on a page break of the US edition.
    ("ch02", "for themselves.\n\nWith all", "for themselves. With all", 1),
    ("ch02", "primitive insights.\n\nPronovost", "primitive insights. Pronovost", 1),
    ("ch02", "no saves.\n\nSo he", "no saves. So he", 1),
    ("ch05", "teamwork was\n\nmostly", "teamwork was mostly", 1),
    ("ch05", "good news.\n\nThe problem", "good news. The problem", 1),
    ("ch07", "surgical personnel.\n\nWe supplied", "surgical personnel. We supplied", 1),
    ("ch08", "missed the\n\nfact that", "missed the fact that", 1),
    ("ch08", "“weak” pilot.\n\nInstead", "“weak” pilot. Instead", 1),
    ("acknowledgments", "more coherence.\n\nLaura", "more coherence. Laura", 1),
    # Paragraphs the old EPUB ran together.
    ("ch02", "daily checklists? Tom", "daily checklists?\n\nTom", 1),
    ("ch04", "said the grill chef. As in", "said the grill chef.\n\nAs in", 1),
    ("ch07", "percentage drop. This thing", "percentage drop.\n\nThis thing", 1),
    # The section break the old EPUB lost at the top of a print page.
    ("ch03", "they get things right.\n\nTo show me", "they get things right.\n\n---\n\nTo show me", 1),
    # Factual errors of the old edition that the US edition corrects (see the translator notes they replace).
    ("ch01", "into her femoral artery to take the blood out of her, then another into her femoral vein to send",
     "into her femoral vein to take the blood out of her, then another into her femoral artery to send", 1),
    ("ch08", "flight taking off in the opposite direction on the same runway.",
     "flight still taxiing on the same runway.", 1),
]

APPENDIX = {"id": "appendix", "file": "18-appendix-example-checklists.md", "status": "review"}
# (image in the US EPUB, file in en/images/, name in the appendix's list of checklists)
FIGURES = [
    ("OEBPS/Images/image00102.jpeg", "appendix-1-door-fwd-cargo.jpeg", "DOOR FWD CARGO"),
    ("OEBPS/Images/image00103.jpeg", "appendix-2-engine-failure-during-flight.jpeg", "Engine Failure During Flight"),
    ("OEBPS/Images/image00104.jpeg", "appendix-3-surgical-safety-checklist.jpeg", "Surgical Safety Checklist (WHO)"),
    ("OEBPS/Images/image00105.jpeg", "appendix-4-checklist-for-checklists.jpeg", "A Checklist for Checklists"),
]


def repair(files):
    applied = skipped = 0
    for section, old, new, count in REPAIRS:
        path = EN / files[section]
        text = path.read_text()
        found = text.count(old)
        if found == 0 and text.count(new) >= count:
            skipped += 1
            continue
        if found != count:
            raise SystemExit(f"error: {section}: expected {count} of {old!r}, found {found}")
        path.write_text(text.replace(old, new))
        applied += 1
    return applied, skipped


def appendix(epub, config):
    images = EN / "images"
    images.mkdir(exist_ok=True)
    blocks = ["# Appendix: Example Checklists"]
    for member, name, title in FIGURES:
        (images / name).write_bytes(epub.read(member))
        blocks += [f"**{title}**", f"![{title}](images/{name})"]
    (EN / APPENDIX["file"]).write_text("\n\n".join(blocks) + "\n")
    chapters = config["chapters"]
    if not any(c["id"] == APPENDIX["id"] for c in chapters):
        after = next(i for i, c in enumerate(chapters) if c["id"] == "ch09")
        chapters.insert(after + 1, dict(APPENDIX))
        book_config.save(BOOK, config)


def main(epub_path):
    config = book_config.load(BOOK)
    files = {c["id"]: c["file"] for c in config["chapters"]}
    applied, skipped = repair(files)
    appendix(zipfile.ZipFile(epub_path), config)
    print(f"{applied} repairs applied, {skipped} already in place; appendix with {len(FIGURES)} figures written")


if __name__ == "__main__":
    main(sys.argv[1])
