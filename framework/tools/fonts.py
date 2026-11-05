"""Build a book's Chinese body face: Noto Serif SC, subset to the characters the book uses.

Run with: uv run --project framework/tools --with fonttools --with brotli python framework/tools/fonts.py books/<id>
The subset is written to books/<id>/assets/fonts/ and committed, so builds need no network access.
"""

import json
from pathlib import Path
import shutil
import subprocess
import sys

import book

CACHE = Path(__file__).resolve().parents[2] / ".cache" / "fonts"
SOURCE = "https://github.com/notofonts/noto-cjk/raw/main/Serif/"
FACES = ["NotoSerifSC-Regular", "NotoSerifSC-SemiBold"]


def fetch(url, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["curl", "-fsSL", "--retry", "2", url, "-o", str(target)], check=True)


def book_characters(root, chapters):
    """Every printable character in the book text, plus ASCII and the CJK punctuation blocks.

    chapters: the book.json entries to cover; their compiled units add the reader's own labels (译者注 and so on).
    """
    chars = {chr(c) for c in range(0x20, 0x7F)}
    chars |= {chr(c) for c in range(0x3000, 0x3040)}  # CJK symbols and punctuation
    chars |= {chr(c) for c in range(0xFF01, 0xFF5F)}  # fullwidth ASCII variants
    for folder in ("zh-cn", "recaps"):
        for path in (root / folder).rglob("*.md"):
            chars |= set(path.read_text())
    for entry in chapters:
        file = entry["file"]
        parent = Path(file).parent.as_posix()
        compiled = book.compile_chapter(entry["id"], (root / "en" / file).read_text(), (root / "zh-cn" / file).read_text(),
                                        "en/" + parent if parent != "." else "en", partial=entry["status"] != "done")
        chars |= set(json.dumps(compiled, ensure_ascii=False))
    return "".join(sorted(c for c in chars if c.isprintable()))


def missing_characters(root, chapters):
    """Characters the committed subset lacks; empty when the fonts are current."""
    charset = root / "assets" / "fonts" / "charset.txt"
    covered = set(charset.read_text()) if charset.exists() else set()
    return sorted(set(book_characters(root, chapters)) - covered)


def main():
    root = Path(sys.argv[1]).resolve()
    config = json.loads((root / "book.json").read_text())
    fonts = root / "assets" / "fonts"
    fonts.mkdir(parents=True, exist_ok=True)
    charset = fonts / "charset.txt"
    charset.write_text(book_characters(root, [c for c in config["chapters"] if c["status"] != "todo"]) + "\n")
    for name in FACES:
        source = CACHE / f"{name}.otf"
        if not source.exists():
            fetch(SOURCE + f"SubsetOTF/SC/{name}.otf", source)
        subprocess.run([
            sys.executable, "-m", "fontTools.subset", str(source),
            f"--text-file={charset}", "--flavor=woff2", "--desubroutinize",
            "--name-IDs=0,1,2,3,4,5,6,13,14",
            f"--output-file={fonts / (name + '.woff2')}",
        ], check=True)
    license_path = CACHE / "LICENSE"
    if not license_path.exists():
        fetch(SOURCE + "LICENSE", license_path)
    shutil.copyfile(license_path, fonts / "LICENSE.txt")
    sizes = ", ".join(f"{name}.woff2 {(fonts / (name + '.woff2')).stat().st_size // 1024} KB" for name in FACES)
    print(f"Subset {len(charset.read_text().rstrip(chr(10)))} characters: {sizes}.")


if __name__ == "__main__":
    main()
