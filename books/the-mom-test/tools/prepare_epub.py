"""Make a copy of the EPUB that the importer turns into this book's sections (see review/source.md).

    uv run --project framework/tools python -I books/the-mom-test/tools/prepare_epub.py book.epub prepared.epub
    python3 scripts/site.py import-epub the-mom-test prepared.epub --force
    uv run --project framework/tools python -I books/the-mom-test/tools/curate_source.py book.epub

The EPUB (v1.04, August 2013) was exported from a word processor ("Cocoa HTML Writer"). Every file has its
own stylesheet and the structure lives in paragraph classes, so a plain import loses most of it:

- Headings are paragraphs set at 164% (section) or 127% (subsection); chapter titles are a centred h3 at
  327% after an h2 "CHAPTER ONE". They become h1 "1. The Mom Test", h2 and h3.
- The EPUB is split at every table-of-contents entry, so one chapter is up to six files. The files of a
  chapter are joined into one section; the title page and the contents page are left out.
- In the example dialogues the speaker ("You:", "Mom:") is a monospace span; it becomes bold.
- Indented paragraphs are quotations (a sample email, a reply): they become block quotes. The two lists of
  questions to judge ("Good question / bad question", "Good meeting / bad meeting") become bullet lists.
- Lists the word processor broke in two (a second <ol> that restarts at 1) are joined again. The cheat
  sheet's "Mistakes and symptoms" becomes one numbered list with the symptoms nested under each mistake.
- The note-taking symbols (a symbol, a tab, its meaning) become bullet lists.
- Empty spacer paragraphs and empty list items are removed, spaces move out of italic and bold, and one
  quotation mark typed the wrong way round is turned.
"""

import re
import sys
import zipfile

from bs4 import BeautifulSoup, NavigableString

OPS = "OPS/"
NUMBERS = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8}
# (label in the table of contents, spine files of the section)
SECTIONS = [
    ("Introduction", [1, 2, 3]),
    ("1. The Mom Test", [4, 5, 6, 7, 8, 9]),
    ("2. Avoiding bad data", [10]),
    ("3. Asking important questions", [11, 12]),
    ("4. Keeping it casual", [13, 14]),
    ("5. Commitment and advancement", [15, 16, 17, 18, 19]),
    ("6. Finding conversations", [20, 21, 22, 23, 24]),
    ("7. Choosing your customers", [25]),
    ("8. Running the process", [26, 27, 28]),
    ("Conclusion and cheatsheet", [29, 30, 31]),
    ("Acknowledgements", [32]),
]
QUESTION_LISTS = {6, 15}  # indented paragraphs that are lists of questions to judge
JOIN_LISTS = {25}  # lists split in two by the word processor
CHEATSHEET = 30
TEXT_FIXES = [("could stay. “ <i>", "could stay.” <i>"),  # closing quote typed as an opening one
              ("☑</span><span class=\"s3\">＄♀☆", "☑</span> <span class=\"s3\">＄ ♀ ☆")]  # symbols run together


def class_traits(css):
    """Class name -> (font size in percent or None, indented, hanging indent, monospace)."""
    traits = {}
    for name, rules in re.findall(r"\w+\.(\w+) \{([^}]*)\}", css):
        size = re.search(r"font-size: (\d+)%", rules)
        indent = re.search(r"margin: 0\.0em 0\.0em [\d.]+em ([\d.]+)em", rules)
        traits[name] = (int(size[1]) if size else None, bool(indent and float(indent[1]) > 0),
                        "text-indent: -" in rules, "monospace" in rules)
    return traits


def squash(tag):
    """Collapse whitespace inside a block, move spaces out of italic and bold, drop empty emphasis."""
    for anchor in tag.find_all("a"):
        if not anchor.get("href"):
            anchor.unwrap()
    for br in tag.find_all("br"):
        br.decompose()
    for span in tag.find_all("span"):
        span.unwrap()
    for piece in list(tag.find_all(string=True)):
        piece.replace_with(re.sub(r"\s+", " ", str(piece)))
    for emphasis in tag.find_all(["i", "b"]):
        text = emphasis.get_text()
        if not text.strip():
            emphasis.replace_with(" " if text else "")
            continue
        strings = list(emphasis.find_all(string=True))
        if strings[-1] != strings[-1].rstrip():
            strings[-1].replace_with(strings[-1].rstrip())
            emphasis.insert_after(" ")
        strings = list(emphasis.find_all(string=True))
        if strings[0] != strings[0].lstrip():
            strings[0].replace_with(strings[0].lstrip())
            emphasis.insert_before(" ")
    html = re.sub(r"\s+", " ", tag.decode_contents()).strip()
    return html


def new(soup, name, html):
    tag = soup.new_tag(name)
    tag.append(BeautifulSoup(html, "html.parser"))
    return tag


def convert(number, html, css, first):
    """Clean block elements of one spine file. first: the file opens its section, so its first heading is h1."""
    traits = class_traits(css)
    soup = BeautifulSoup(html, "html.parser")
    out, group, mode = [], [], None
    chapter, mistakes = None, None

    def flush():
        nonlocal group, mode
        if not group:
            return
        if mode == "quote":
            block = soup.new_tag("blockquote")
            for item in group:
                block.append(new(soup, "p", item))
            out.append(block)
        else:
            block = soup.new_tag("ul")
            for item in group:
                block.append(new(soup, "li", item))
            if mode == "nest":
                mistakes.find_all("li", recursive=False)[-1].append(block)
            else:
                out.append(block)
        group, mode = [], None

    def heading(level, text):
        nonlocal first, chapter
        if first:
            level, first = 1, False
            if chapter:
                text = f"{chapter}. {text}"
        out.append(new(soup, f"h{level}", text))

    for element in soup.body.find_all(recursive=False):
        text = " ".join(element.get_text(" ").split())
        if not text:
            continue
        size, indented, hanging, _ = traits.get((element.get("class") or [""])[0], (None, False, False, False))
        if element.name == "h2" and text.startswith("CHAPTER "):
            chapter = NUMBERS[text.split()[1]]
            continue
        if element.name == "h3":
            flush()
            heading(1 if "327%" in element.get("style", "") else 2, text)
            continue
        if element.name in ("ol", "ul"):
            items = [squash(li) for li in element.find_all("li", recursive=False)]
            items = [item for item in items if item]
            if mistakes is not None:
                if element.name == "ol":
                    flush()
                    for item in items:
                        mistakes.append(new(soup, "li", item))
                else:
                    group += items
                    mode = "nest"
                    flush()
                continue
            flush()
            if number in JOIN_LISTS and out and out[-1].name == element.name:
                for item in items:
                    out[-1].append(new(soup, "li", item))
                continue
            out.append(soup.new_tag(element.name))
            for item in items:
                out[-1].append(new(soup, "li", item))
            continue
        # A paragraph.
        tabbed = number in (28, CHEATSHEET) and element.find("span", class_="Apple-tab-span") is not None
        if hanging:  # a line of dialogue: the monospace speaker label becomes bold
            label = element.find("span")
            if label is not None and traits.get((label.get("class") or [""])[0], (0, 0, 0, False))[3]:
                label.name, label.attrs = "b", {}
        body = squash(element)
        if size in (164, 127):
            flush()
            heading(2 if size == 164 else 3, " ".join(BeautifulSoup(body, "html.parser").get_text().split()))
            continue
        if tabbed:
            if mode != "symbols":
                flush()
            group.append(body)
            mode = "symbols"
            continue
        if indented and not hanging:
            if mistakes is not None:
                mode = "nest"
            elif mode is None:
                mode = "list" if number in QUESTION_LISTS else "quote"
            group.append(body)
            continue
        flush()
        if number == CHEATSHEET:
            label = re.fullmatch(r"<b>(.*)</b>", body)
            if mistakes is not None and label:
                mistakes = None
            if label and label[1] == "Mistakes and symptoms:":
                out.append(new(soup, "p", body))
                mistakes = soup.new_tag("ol")
                out.append(mistakes)
                continue
        out.append(new(soup, "p", body))
    flush()
    return "\n".join(str(block) for block in out)


def page(title, body):
    return ('<?xml version="1.0" encoding="utf-8"?>\n<html xmlns="http://www.w3.org/1999/xhtml">\n'
            f"<head><title>{title}</title></head>\n<body>\n{body}\n</body>\n</html>\n")


def main(source, target):
    epub = zipfile.ZipFile(source)
    files = {}
    for index, (label, numbers) in enumerate(SECTIONS, 1):
        parts = []
        for k, number in enumerate(numbers):
            html = epub.read(f"{OPS}body{number}.xhtml").decode()
            for old, fixed in TEXT_FIXES:
                html = html.replace(old, fixed)
            css = epub.read(OPS + re.search(r'href="(css/[^"]+)"', html)[1]).decode()
            parts.append(convert(number, html, css, k == 0))
        files[f"s{index:02d}.xhtml"] = (label, page(label, "\n".join(parts)))
    manifest = "\n".join(f'<item id="s{i:02d}" href="s{i:02d}.xhtml" media-type="application/xhtml+xml"/>'
                         for i in range(1, len(files) + 1))
    spine = "\n".join(f'<itemref idref="s{i:02d}"/>' for i in range(1, len(files) + 1))
    opf = ('<?xml version="1.0" encoding="UTF-8"?>\n<package xmlns="http://www.idpf.org/2007/opf" version="2.0" '
           'unique-identifier="id"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
           '<dc:title>The Mom Test</dc:title><dc:identifier id="id">prepared</dc:identifier><dc:language>en</dc:language>'
           f'</metadata>\n<manifest>\n<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>\n{manifest}\n'
           f'</manifest>\n<spine toc="ncx">\n{spine}\n</spine>\n</package>\n')
    points = "\n".join(f'<navPoint id="n{i}" playOrder="{i}"><navLabel><text>{label}</text></navLabel>'
                       f'<content src="{name}"/></navPoint>' for i, (name, (label, _)) in enumerate(files.items(), 1))
    ncx = ('<?xml version="1.0" encoding="UTF-8"?>\n<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
           f"<head/><docTitle><text>The Mom Test</text></docTitle><navMap>\n{points}\n</navMap></ncx>\n")
    container = epub.read("META-INF/container.xml")
    with zipfile.ZipFile(target, "w") as out:
        out.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        out.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        out.writestr(OPS + "content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
        out.writestr(OPS + "toc.ncx", ncx, compress_type=zipfile.ZIP_DEFLATED)
        for name, (_, html) in files.items():
            out.writestr(OPS + name, html, compress_type=zipfile.ZIP_DEFLATED)
    print(f"{len(files)} sections from {sum(len(n) for _, n in SECTIONS)} spine files -> {target}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
