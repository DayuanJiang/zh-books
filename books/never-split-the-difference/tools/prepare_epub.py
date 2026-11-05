"""Make a copy of the EPUB that the importer turns into this book's sections (see review/source.md).

    uv run --project framework/tools python -I books/never-split-the-difference/tools/prepare_epub.py book.epub prepared.epub
    python3 scripts/site.py import-epub never-split-the-difference prepared.epub --force
    uv run --project framework/tools python -I books/never-split-the-difference/tools/curate_source.py book.epub

The EPUB is a calibre repackaging of the HarperCollins e-book with only the ten chapters, one file each.
The structure lives in paragraph classes, so a plain import loses most of it:

- Each chapter opens with two h2 headings, "CHAPTER 1" and "THE NEW RULES". They become one h1
  "1. The New Rules", followed by the chapter's subtitle, which only the table of contents carries.
- Section headings are bold paragraphs of class "image", subsection headings are paragraphs whose whole
  text is bold capitals. They become h2 and h3, in title case (the EPUB sets them in capitals).
  The dateline "September 30, 1993" at the start of chapter 2 has the same class and stays a paragraph.
- The bold drop cap at the start of each chapter becomes a plain letter.
- Paragraphs of class "bl" are list items: "■" items become bullet lists, "1." items numbered lists.
- Paragraphs of class "email" (quoted emails) and "di" (a fund-raising call script) become block quotes.
- Bold phrases that the conversion split into one bold run per word are joined again.
- One URL has a stray space in it ("http://info .blackswanltd.com"); in chapter 8 a closing quotation mark
  is typed as an opening one after a space ("the Counterfeit “Yes. “").
- Four italic phrases end in a dash that runs into the next word ("*Labeling—*that"); Markdown cannot close
  an italic there, so the dash moves out of the italic.
- The table of contents labels ("Chapter 1 | the New Rules") become "1. The New Rules", so the importer
  names the files 01-1-the-new-rules.md and gives the ids ch01 to ch10.
"""

import re
import sys
import zipfile

from bs4 import BeautifulSoup, NavigableString

TITLES = {
    1: "The New Rules",
    2: "Be a Mirror",
    3: "Don’t Feel Their Pain, Label It",
    4: "Beware “Yes”—Master “No”",
    5: "Trigger the Two Words That Immediately Transform Any Negotiation",
    6: "Bend Their Reality",
    7: "Create the Illusion of Control",
    8: "Guarantee Execution",
    9: "Bargain Hard",
    10: "Find the Black Swan",
}
DATELINE = "September 30, 1993"
TEXT_FIXES = [("http://info .blackswanltd.com", "http://info.blackswanltd.com"),  # stray space in a URL
              ("the Counterfeit “Yes. “", "the Counterfeit “Yes.”")]  # closing quote typed as an opening one
# Chicago style: articles, coordinating conjunctions and prepositions stay lowercase inside a title.
SMALL = {"a", "an", "the", "and", "but", "or", "nor", "as", "at", "by", "for", "from", "in", "into", "of",
         "on", "to", "with", "without", "behind", "before", "after", "against", "vs"}
KEEP = {"FBI", "DJ", "FM"}


def title_case(text):
    """'THE F-WORD: WHY IT’S SO POWERFUL' -> 'The F-Word: Why It’s So Powerful'."""
    words = [w for w in re.split(r"(\s+|—)", text) if w and not w.isspace()]
    result = []
    for k, word in enumerate(words):
        if word == "—":
            result.append(word)
            continue
        first = k == 0 or re.search(r"[:.?]$", words[k - 1])
        last = k == len(words) - 1
        parts = []
        for j, part in enumerate(word.split("-")):
            core = re.sub(r"^[“‘\"(#]+|[”’\",.:?!)…]+$", "", part)
            lead = part[:part.find(core)] if core else part
            tail = part[len(lead) + len(core):]
            if core.upper() in KEEP:
                core = core.upper()
            elif core.lower() in SMALL and (j > 0 or not (first or last or lead)):
                core = core.lower()
            else:
                core = core[:1].upper() + core[1:].lower()
            parts.append(lead + core + tail)
        result.append("-".join(parts))
    return re.sub(r" ?— ?", "—", " ".join(result))


def blocks_after(tag):
    """The block siblings after a tag, skipping whitespace."""
    node = tag.next_sibling
    while node is not None:
        if not (isinstance(node, NavigableString) and not node.strip()):
            yield node
        node = node.next_sibling


def bold_only(p):
    pieces = [s for s in p.find_all(string=True) if s.strip()]
    return pieces and all(s.find_parent("b") is not None for s in pieces)


def group(soup, cls, kind):
    """Wrap runs of consecutive paragraphs of a class in a new element; kind(p) names the wrapper tag."""
    count = 0
    for p in soup.find_all("p", class_=cls):
        if p.parent is None or p.parent.name in ("ul", "ol", "blockquote"):
            continue
        run = [p]
        for node in blocks_after(p):
            if node.name == "p" and cls in (node.get("class") or []) and kind(node) == kind(p):
                run.append(node)
            else:
                break
        wrapper = soup.new_tag(kind(p))
        p.insert_before(wrapper)
        for item in run:
            wrapper.append(item.extract())
        count += 1
    return count


def list_kind(p):
    return p["data-list"]


def prepare_chapter(html, number, subtitle):
    for wrong, right in TEXT_FIXES:
        html = html.replace(wrong, right)
    html = re.sub(r'</b>(\s+)<b class="calibre3">', r"\1", html)  # one bold run per word
    html = html.replace("—</i>", "</i>—")
    soup = BeautifulSoup(html, "html.parser")
    body = soup.body
    soup.find("h2", class_="cn").decompose()
    title = soup.find("h2", class_="ct")
    heading = soup.new_tag("h1")
    heading.string = f"{number}. {TITLES[number]}"
    title.replace_with(heading)
    line = soup.new_tag("p")
    line.append(soup.new_tag("i"))
    line.i.string = subtitle
    heading.insert_after(line)
    for cap in body.find_all("span", class_="dropcap"):
        cap.replace_with(cap.get_text())
    for p in body.find_all("p", class_="_section-break"):
        if not p.get_text(strip=True):
            p.decompose()
    for p in body.find_all("p", class_="image"):
        text = " ".join(p.get_text().split())
        if text == DATELINE:
            continue
        cased = title_case(text)
        for em in p.find_all(["i", "span"]):
            if em.name == "i" or "bold_italic" in em.get("class", []):
                word = title_case(f"x {em.get_text(strip=True)} x").split()[1]
                cased = cased.replace(word, f"<i>{word}</i>", 1)
        heading = BeautifulSoup(f"<h2>{cased}</h2>", "html.parser").h2
        p.replace_with(heading)
    for p in body.find_all("p", class_="noindent"):
        text = " ".join(p.get_text().split())
        if bold_only(p) and not re.search(r"[a-z]", text):
            heading = soup.new_tag("h3")
            heading.string = title_case(text)
            p.replace_with(heading)
    for p in body.find_all("p", class_="bl"):
        first = p.find(string=True)
        p["data-list"] = "ul" if p.get_text().lstrip().startswith("■") else "ol"
        if p["data-list"] == "ul":
            first.replace_with(first.replace("■", "", 1).lstrip())
        else:
            marker = p.find("b")
            if not marker or not re.fullmatch(r"\d+\.", marker.get_text(strip=True)):
                raise SystemExit(f"error: chapter {number}: list item without a marker: {p.get_text()[:60]}")
            marker.decompose()
            first = p.find(string=True)
            first.replace_with(first.lstrip())
    lists = group(soup, "bl", list_kind)
    for span in body.find_all("span", class_="smallcaps"):
        span.unwrap()
    quotes = group(soup, "email", lambda p: "blockquote") + group(soup, "di", lambda p: "blockquote")
    for wrapper in body.find_all(["ul", "ol"]):
        for p in wrapper.find_all("p", recursive=False):
            p.name = "li"
            p.attrs = {}
    return str(soup), lists, quotes


def chapter_files(nav_html):
    """[(file, number, subtitle)] from the table of contents: 'Chapter 1 | the New Rules' and its child entry."""
    nav = BeautifulSoup(nav_html, "html.parser").find("nav")
    found = []
    for item in nav.ol.find_all("li", recursive=False):
        label = item.a.get_text(" ", strip=True)
        number = int(re.match(r"Chapter (\d+) \|", label)[1])
        found.append((item.a["href"], number, item.ol.a.get_text(" ", strip=True)))
    return found


def new_nav(chapters):
    entries = "\n".join(f'    <li><a href="{file}">{n}. {TITLES[n]}</a></li>' for file, n, _ in chapters)
    return ('<?xml version="1.0" encoding="utf-8"?>\n<html xmlns="http://www.w3.org/1999/xhtml" '
            'xmlns:epub="http://www.idpf.org/2007/ops"><head><title>Navigation</title></head><body>\n'
            f'<nav epub:type="toc"><ol>\n{entries}\n</ol></nav></body></html>\n')


def main(source, target):
    epub = zipfile.ZipFile(source)
    chapters = chapter_files(epub.read("nav.xhtml").decode())
    if [n for _, n, _ in chapters] != list(range(1, 11)):
        raise SystemExit(f"error: unexpected chapters {chapters}")
    pages, stats = {}, []
    for file, number, subtitle in chapters:
        pages[file], lists, quotes = prepare_chapter(epub.read(file).decode(), number, subtitle)
        stats.append(f"ch{number:02d}: {lists} lists, {quotes} quotes")
    with zipfile.ZipFile(target, "w") as out:
        for info in epub.infolist():
            data = epub.read(info.filename)
            if info.filename in pages:
                data = pages[info.filename].encode()
            elif info.filename == "nav.xhtml":
                data = new_nav(chapters).encode()
            kind = zipfile.ZIP_STORED if info.filename == "mimetype" else zipfile.ZIP_DEFLATED
            out.writestr(info, data, compress_type=kind)
    print("\n".join(stats))
    print(f"{len(chapters)} chapters -> {target}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
