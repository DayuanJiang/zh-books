"""Make a copy of the EPUB that the importer can turn into this book's structure (see review/source.md).

    uv run --project framework/tools python -I books/bad-blood/tools/prepare_epub.py book.epub prepared.epub
    python3 scripts/site.py import-epub bad-blood prepared.epub --force
    uv run --project framework/tools python -I books/bad-blood/tools/curate_source.py book.epub
    uv run --project framework/tools python -I books/bad-blood/tools/check_source.py book.epub

What a plain import would lose or garble:
- The endnotes only link back to an empty anchor in the text. Each anchor gets a marker ZZNOTE<k>ZZ,
  k being the note's position in the notes file, so curate_source.py can put a footnote there.
- The first words after each scene break are set in small caps, which the EPUB stores as capital letters
  ("THE TERM “VAPORWARE” was coined"). They go back to normal case; names keep their capital.
- Vitamin B<sub>12</sub> would become B12; it becomes B₁₂.
- Two short runs of lines inside a <div> would become one paragraph per line: Fuisz's jotted notes become
  a list, the address on Erika Cheung's envelope one paragraph with line breaks.
"""

import re
import sys
import zipfile

NOTES = "OEBPS/Carr_9781524731663_epub3_nts_r1.xhtml"
NOTE = re.compile(r'<p class="para-en list0">(.*?)</p>', re.S)
TARGET = re.compile(r'href="(Carr_\w+\.xhtml)#(Y_[\w-]+)"')
LEAD_IN = re.compile(r'(<span class="char-first cso_10">(?:<span id="[^"]+"/>(?:ZZNOTE\d+ZZ)?)?<span class="smallcaps">)([^<]+)(</span>)')
SMALL_CAPS_ITALIC = re.compile(r'(<span class="smallcaps italic">)([^<]+)(</span>)')
# "J" + small caps "OHN", "C" + small caps "ARREYROU" on the About the Author page.
AFTER_CAPITAL = re.compile(r'(<span class="roman char-r">[A-Z]</span><span class="smallcaps char-sc">)([^<]+)(</span>)')
SUB_DIGITS = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
# Words of the small-caps lead-ins that keep a capital letter: names, places, months, the pronoun I.
PROPER = """Elizabeth Mosley Ed Avie Don Lucas Theranos Chris Noel Holmes Fuisz Sunny Chelsea Centocor
    Walgreens Chicago Greg Safeway Shoemaker David Boies Ian April Rochelle Patrick June Anjali Laghari
    Mike Barsanti November Tyler Erika Julia Love Parloff Alan I Anders California Cheung May Fortune""".split()
PROPER = {word.lower(): word for word in PROPER}


def note_targets(epub):
    """[(file, anchor id)] for every note, in the order of the notes file."""
    targets = []
    for body in NOTE.findall(epub.read(NOTES).decode()):
        found = set(TARGET.findall(body))
        if len(found) != 1:
            raise SystemExit(f"error: a note links to {len(found)} places: {body[:120]}")
        targets.append(found.pop())
    return targets


def normal_case(text, first):
    """'ELIZABETH’S EARLY YEARS ' -> 'Elizabeth’s early years '; the first word of a paragraph gets a capital."""
    def word(match):
        core = match.group(0)
        stem, s = (core[:-2], core[-2:]) if core.upper().endswith("’S") else (core, "")
        return PROPER.get(stem.lower(), stem.lower()) + s.lower()
    text = re.sub(r"[A-Z][A-Z.’]*", word, text)
    if first:
        text = re.sub(r"[A-Za-z]", lambda m: m.group(0).upper(), text, count=1)
    return text


def mark(html, anchor, marker):
    """Put the marker text right after the empty anchor <span id="..."/>."""
    tag = f'<span id="{anchor}"/>'
    if html.count(tag) != 1:
        raise SystemExit(f"error: anchor {anchor} found {html.count(tag)} times")
    return html.replace(tag, tag + marker)


def lines_to_list(html):
    """Fuisz's notepad lines (chapter 18) as a bulleted list."""
    block = re.search(r'<div>\s*(?:<span epub:type="pagebreak"[^>]*/>\s*)?(<p class="para-ulf">.*?)</div>', html, re.S)
    items = re.findall(r'<p class="para-ul[fl]?">(.*?)</p>', block.group(1), re.S)
    return html[:block.start()] + "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>" + html[block.end():]


def lines_to_paragraph(html):
    """The address on the envelope (chapter 21) as one paragraph with line breaks."""
    block = re.search(r'<div>\s*(<p class="para-ulf">.*?)</div>', html, re.S)
    items = re.findall(r'<p class="para-ul[fl]?">(.*?)</p>', block.group(1), re.S)
    return html[:block.start()] + "<p>" + "<br/>".join(items) + "</p>" + html[block.end():]


def styled(name, html):
    html = LEAD_IN.sub(lambda m: m.group(1) + normal_case(m.group(2), True) + m.group(3), html)
    html = SMALL_CAPS_ITALIC.sub(lambda m: m.group(1) + normal_case(m.group(2), False) + m.group(3), html)
    html = AFTER_CAPITAL.sub(lambda m: m.group(1) + m.group(2).lower() + m.group(3), html)
    html = re.sub(r'<sub class="char-sub">(\d+)</sub>', lambda m: m.group(1).translate(SUB_DIGITS), html)
    if name.endswith("c019_r1.xhtml"):
        html = lines_to_list(html)
    if name.endswith("c022_r1.xhtml"):
        html = lines_to_paragraph(html)
    return html


def main(source, target):
    epub = zipfile.ZipFile(source)
    targets = note_targets(epub)
    pages = {}
    for k, (file, anchor) in enumerate(targets):
        name = "OEBPS/" + file
        pages[name] = mark(pages.get(name) or epub.read(name).decode(), anchor, f"ZZNOTE{k}ZZ")
    with zipfile.ZipFile(target, "w") as out:
        for info in epub.infolist():
            data = epub.read(info.filename)
            if info.filename.endswith(".xhtml") and info.filename != NOTES:
                data = styled(info.filename, pages.get(info.filename) or data.decode()).encode()
            kind = zipfile.ZIP_STORED if info.filename == "mimetype" else zipfile.ZIP_DEFLATED
            out.writestr(info, data, compress_type=kind)
    print(f"{len(targets)} notes marked in the text -> {target}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
