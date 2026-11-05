"""Make a copy of the EPUB that the importer can turn into this book's structure (see review/source.md).

    uv run --project framework/tools python books/empire-of-ai/tools/prepare_epub.py book.epub prepared.epub
    python3 scripts/site.py import-epub empire-of-ai prepared.epub --force
    uv run --project framework/tools python books/empire-of-ai/tools/curate_source.py

Two things are lost in a plain import:
- Italic and bold are CSS classes here, so they become <i> and <b>; the few superscript
  exponents become superscript digits.
- The endnotes only link back to an empty anchor in the text. Each anchor gets a marker ZZNOTE<k>ZZ,
  k being the note's position in the notes files, so curate_source.py can put a footnote there.
"""

import re
import sys
import zipfile

NOTES = re.compile(r"OEBPS/c238_split_\d+\.xhtml")
BACK_LINK = re.compile(r'<a href="(c\w+\.xhtml)(?:#([\w-]+))?"[^>]*>GO TO NOTE REFERENCE IN TEXT</a>')
ITALIC = ("class_s5n3", "class_s5pt")
BOLD = ("class_s5n5",)
SUPERSCRIPT = "class_s65z"  # the exponents in 10^26 and 10^25
SUPER_DIGITS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
BLOCKS = {"p", "div", "li", "h1", "h2", "h3", "blockquote"}


def note_targets(epub):
    """[(file, anchor id or None)] for every note, in the order of the notes files."""
    targets = []
    for name in sorted(n for n in epub.namelist() if NOTES.fullmatch(n)):
        targets += BACK_LINK.findall(epub.read(name).decode())
    return [(file, anchor or None) for file, anchor in targets]


def styled(html):
    for cls in ITALIC:
        html = re.sub(rf'<span class="{cls}">(.*?)</span>', r"<i>\1</i>", html, flags=re.S)
    for cls in BOLD:
        html = re.sub(rf'<span class="{cls}">(.*?)</span>', r"<b>\1</b>", html, flags=re.S)
    return re.sub(rf'<span class="{SUPERSCRIPT}">(\d+)</span>', lambda m: m.group(1).translate(SUPER_DIGITS), html)


def mark(html, anchor, marker):
    """Put the marker text at the anchor: inside a block that carries the id, after an empty inline anchor."""
    found = re.search(rf'<(\w+)\b[^>]*\bid="{re.escape(anchor)}"[^>]*>', html)
    if not found:
        raise SystemExit(f"error: anchor {anchor} not found")
    tag, end = found.group(1), found.end()
    if tag not in BLOCKS and html.startswith(f"</{tag}>", end):
        end += len(f"</{tag}>")
    return html[:end] + marker + html[end:]


def main(source, target):
    epub = zipfile.ZipFile(source)
    targets = note_targets(epub)
    pages = {}
    for k, (file, anchor) in enumerate(targets):
        if anchor:
            name = "OEBPS/" + file
            pages[name] = mark(pages.get(name) or epub.read(name).decode(), anchor, f"ZZNOTE{k}ZZ")
    with zipfile.ZipFile(target, "w") as out:
        for info in epub.infolist():
            data = epub.read(info.filename)
            if info.filename.endswith(".xhtml"):
                data = styled(pages.get(info.filename) or data.decode()).encode()
            kind = zipfile.ZIP_STORED if info.filename == "mimetype" else zipfile.ZIP_DEFLATED
            out.writestr(info, data, compress_type=kind)
    print(f"{len(targets)} notes, {sum(1 for _, a in targets if a)} with an anchor in the text -> {target}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
