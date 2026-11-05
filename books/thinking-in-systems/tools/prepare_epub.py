"""Make a copy of the EPUB in plain HTML structure, so the importer gets this book right (see review/source.md).

    uv run --project framework/tools python -I books/thinking-in-systems/tools/prepare_epub.py book.epub prepared.epub
    python3 scripts/site.py import-epub thinking-in-systems prepared.epub --force
    uv run --project framework/tools python -I books/thinking-in-systems/tools/curate_source.py book.epub

The EPUB is a conversion that marks everything with CSS classes: chapter titles, headings, bullet lists,
margin notes, boxes and quotations are all styled paragraphs. This script rewrites each document with real
<h1>/<h2>/<h3>, <ul>/<ol>, <blockquote> and <hr>, so the Markdown the importer writes has the book's structure:

- Each section starts with one <h1>; the table of contents gets the same titles ("1. The Basics").
- Margin notes (the principles printed in the margin) and the grey boxes become block quotes; the five
  "Interlude" stories become a level 3 heading, their paragraphs and a rule.
- Quotations set off from the text become block quotes. Chapter epigraphs stay plain paragraphs, which the
  reader shows as epigraphs; attributions ("—Name") stay plain paragraphs after the quote.
- Small capitals ("R<small>OBERT</small>") become normal case, split italics are joined, links into the
  table of contents and to figures are removed.
- Conversion errors: the first words of a note pasted after nine note references, a line missing from the
  Boulding poem, one note whose back link points at the wrong reference, words split by a stray space, and
  the Model Equations whose lines were run together or broken in the middle.
"""

import re
import sys
import zipfile

from bs4 import BeautifulSoup, NavigableString

ROOT = "OEBPS/"

# Section titles by spine document. Documents without a title (cover, title pages, contents, ads) are
# imported as they are and dropped by curate_source.py.
TITLES = {
    "chap6": "Dedication",
    "chap8": "A Note from the Author",
    "chap9": "A Note from the Editor",
    "chap10": "Epigraph",
    "chap11": "Introduction: The Systems Lens",
    "chap12": "Part One: System Structure and Behavior",
    "chap13": "1. The Basics",
    "chap14": "2. A Brief Visit to the Systems Zoo",
    "chap15": "Part Two: Systems and Us",
    "chap16": "3. Why Systems Work So Well",
    "chap17": "4. Why Systems Surprise Us",
    "chap18": "5. System Traps . . . and Opportunities",
    "chap19": "Part Three: Creating Change—in Systems and in Our Philosophy",
    "chap20": "6. Leverage Points—Places to Intervene in a System",
    "chap21": "7. Living in a World of Systems",
    "chap22": "Appendix",
    "chap23": "Notes",
    "chap24": "Bibliography of Systems Resources",
    "chap25": "Editor’s Acknowledgments",
    "chap26": "About the Author",
}
PART_PAGES = {"chap12", "chap15", "chap19"}  # only the part title, nothing else

H2_CLASSES = {"h8", "h17", "h191", "h20"}
H3_CLASSES = {"tx9", "tx55"}
H3_IDS = {
    # chapter 2: two of the system "animals" are set as body paragraphs
    "d411522741", "d411528971",
    # appendix: groups of the summary of principles, the two chapters of the model equations
    "d411588011", "d411588221", "d411588561", "d411588911", "d411589061", "d411589221", "d411589391",
    "d411589611", "d411589981", "d411592801", "d411595251",
    # bibliography
    "d48501", "d4115111671",
}
BOX_TITLES = {"h5", "h14", "h16", "h18"}

# Quotations set off from the text, each group one block quote (ids of its paragraphs, in order).
QUOTES = [
    # introduction: a systems principle with the proverb that says the same
    ["d41155911", "d41155931"], ["d41155991", "d41156011", "d41156012"], ["d41156161", "d41156181"],
    # chapter 1
    ["d41159641"], ["d411512091"], ["d411515121"], ["d411517541"], ["d411517731"],
    # chapter 3
    ["d18431"], ["d411534841"], ["d411535961"],
    # chapter 4
    ["d411538281"], ["d411540101", "d411540102"], ["d411542281"], ["d411547191", "d411547211"], ["d411548311"],
    # chapter 5
    ["d411551541", "d411551591"], ["d411553481"], ["d411553631", "d411553731", "d411553732"],
    ["d411555851", "d411555951", "d411556081"], ["d28781"], ["d411558601"], ["d411560161", "d411560231"],
    ["d411560381", "d411560401", "d411560402"],
    ["d411562231", "d411562232", "d411562233", "d411562234", "d411562235"],
    ["d411563361", "d411563381", "d411563382"], ["d411563781"], ["d411563871"],
    # chapter 6
    ["d411567521", "d411567591", "d411567611"], ["d411574771"],
    # chapter 7
    ["d411580191"], ["d411581071"], ["d411581111"], ["d411584771"], ["d411584841"], ["d411585541"], ["d411586491"],
]
# Poems printed one line per paragraph: one paragraph with line breaks, kept under the first line's id.
VERSE = [
    ["d411535961", "d411535962", "d411535963", "d411535964"],
    ["d411538281", "d411538282", "d411538283", "d411538284", "restored-boulding", "d411538285", "d411538286",
     "d411538287", "d411538288", "d411538531", "d411538532", "d411538533"],
]
# A paragraph of chapter 1 that the EPUB splits around a box: the second half joins the first, the box follows.
JOINS = [("d411518971", "d411519271")]
# Two paragraphs of the Way Out for shifting the burden follow the box in the EPUB; the appendix has them in it.
INTO_BOX = ["d411562101", "d411562151"]
# Bullets written into ordinary paragraphs (chapter 5).
BULLETS = {"d411561791", "d411561831", "d411561871"}
# Numbered paragraphs that are lists counting up from 1.
NUMBERED = [
    ["d411524561", "d411524562", "d411524563"],
    ["d411537791", "d411537901", "d411537921"],
    ["d411592091", "d411592111", "d411592131", "d411592151", "d411592171", "d411592191", "d411592221",
     "d411592241", "d411592261", "d411592281", "d411592331", "d411592351", "d411592371", "d411592391", "d411592411"],
]
# The twelve places to intervene count down from 12: one paragraph with a line per place.
LINES = [["d411591541", "d411591581", "d411591621", "d411591661", "d411591701", "d411591751", "d411591791",
          "d411591831", "split-self-organization", "d45441", "d43031", "d43061"]]

# The first words of a note, pasted by the conversion right after the reference to another (or the same) note.
LEAKS = {
    ("chap13", "5"): "Jan Tinbergen, quoted in ibid, 44.",
    ("chap14", "3"): "Jay W. Forrester,",
    ("chap14", "5"): "Jay W. Forrester, 1989.",
    ("chap16", "4"): "Jonathan Swift,",
    ("chap16", "5"): "Paraphrased from Herbert Simon,",
    ("chap18", "7"): "Erik Ipsen,",
    ("chap20", "3"): "World Bank,",
    ("chap20", "7"): "Ralph Waldo Emerson,",
    ("chap20", "8"): "Clyde Haberman,",
}

# Exact passages of the HTML, replaced before parsing: (document, passage, replacement[, times it occurs]).
FIXES = [
    # The back link of note 7 in chapter 4 points at the reference of note 8.
    ("chap23", 'part17.html#d4115106641a" id="d4115106531"', 'part17.html#d4115106531a" id="d4115106531"'),
    # An opening parenthesis inside the italics of a book title (note 8 of chapter 4).
    ("chap23", "<i>Dynamics of Commodity Production Cycles, (</i>Cambridge", "<i>Dynamics of Commodity Production Cycles,</i> (Cambridge"),
    # The Boulding poem lacks its fifth line, which the poem has wherever it is quoted.
    ("chap17", '<p class="pub" id="d411538285">',
     '<p class="pub" id="restored-boulding">Perceiving input-output pairs,</p>\n<p class="pub" id="d411538285">'),
    # Words split by a space where the print edition broke the line.
    ("chap13", "system-defined goal— also", "system-defined goal—also"),
    ("chap14", "reinforcing-loop-plus-balancing- loop", "reinforcing-loop-plus-balancing-loop"),
    ("chap16", "meta-meta- resilience", "meta-meta-resilience"),
    ("chap18", "the alcohol- driven chaos", "the alcohol-driven chaos"),
    ("chap18", "success-to- the-successful", "success-to-the-successful"),
    ("chap20", "not second to- highest", "not second-to-highest"),
    ("chap21", "my figuring- out rationality", "my figuring-out rationality"),
    ("chap21", "it’s one thing to under stand how", "it’s one thing to understand how"),
    ("chap18", "strong penal ties.", "strong penalties."),
    ("chap11", "ask “what-if ” questions", "ask “what-if” questions"),
    # Hyphens missing: the book writes success-to-the-successful elsewhere, and flow-limited in the appendix.
    ("chap18", "success-to the-successful", "success-to-the-successful", 3),
    ("chap14", "<b><i>flow</i></b><b>limited. </b>", "<b><i>flow</i></b><b>-limited. </b>"),
    ("chap13", "A ) Can you identify parts?", "A) Can you identify parts?"),
    ("chap14", "people in the population.Its mortality", "people in the population. Its mortality"),
    ("chap14", "a balancing death loop.Both also", "a balancing death loop. Both also"),
    # A paragraph of the budworm interlude lacks its full stop.
    ("chap17", "eventually to explode again</p>", "eventually to explode again.</p>"),
    # The asterisk after the first bold word points to a note at the end of chapter 1: a footnote reference.
    ("chap13", '<b>system</b><b><a href="chap13_thinking_9781603581486_epub_part13.html#d411519681">*</a></b><b> </b>is',
     '<b>system</b><sup><a epub:type="noteref" href="#d411519681">*</a></sup> is'),
    # Places to intervene 5 and 4 share a paragraph.
    ("chap22", "constraints <b>4. Self-Organization: </b>",
     'constraints</p>\n<p class="tx12a" id="split-self-organization"><b>4. Self-Organization: </b>'),
    # Model equations: a title run together with its first line.
    ("chap22", "—for Figures 37–41 Stock: ", '—for Figures 37–41</p>\n<p class="tx12a" id="split-nonrenewable">Stock: '),
]
# Model equations: line breaks lost inside a line (a break goes back in; the second passage occurs twice).
BR = "<br/>"
FIXES += [("chap22", before, before.replace(at, BR + at, 1)) for before, at in [
    ("<i>dt </i>Initial stock value: <i>water in tub", "Initial"),
    ("<i>dt) </i>Initial stock value: <i>coffee temperature", "Initial"),
    ("= years <i>dt </i>= 1 year", "<i>dt"),
    ("= 18°C <i>discrepancy between desired", "<i>discrepancy"),
    ("or 0 <i>discrepancy between inside", "<i>discrepancy"),
    ("(Figures 19 and 20) <i>24-hour outside temp </i>ranges", "<i>24-hour"),
    ("<i>dt </i>Initial stock value: <i>population", "Initial"),
    ("<i>dt </i>Initial stock value: <i>capital stock", "Initial"),
    ("<i>output per unit capital </i><i>capital lifetime </i>= 10 years", "<i>capital lifetime"),
    ("<i>dt </i>Initial stock values: <i>inventory", "Initial"),
    ("in Figure 39 Outflow: <i>extraction", "Outflow"),
    ("<i>capital </i>= 5 Inflow: <i>investment", "Inflow"),
    ("× 10%) <i>growth goal", "<i>growth goal"),
]]
FIXES.append(("chap22", "</i><i>room temperature </i>= 18°C", "</i><br/><i>room temperature </i>= 18°C", 2))
# ... and lines broken in the middle of a sentence (ids of the continuation lines).
EQUATION_JOINS = ["d411599008", "d41151005611g", "d4115101961", "d4115103195", "d4115103196", "d4115103512"]
# Paragraphs after the Model Equations heading that are prose, not equation lines.
EQUATION_PROSE = {"d411592501", "d411592671"}
MODEL_EQUATIONS = "d411592461"


def key(name):
    return name.rsplit("/", 1)[-1].split("_", 1)[0]


def fix_html(name, html):
    for document, before, after, *count in FIXES:
        if document == key(name):
            if html.count(before) != (count[0] if count else 1):
                raise SystemExit(f"error: {document}: passage not found {count[0] if count else 1} time(s): {before!r}")
            html = html.replace(before, after)
    # Italic and bold split into pieces at every line of the print edition.
    for tag in ("i", "b"):
        html = re.sub(rf"</{tag}>(\s*)<{tag}>", r"\1", html)
    if key(name) == "chap23":
        html = re.sub(r"(<a [^>]*>\d+</a>)\. ", r"\1 ", html)  # "1. Russell Ackoff" -> the number is the link
    return html


def text_of(tag):
    return " ".join(tag.get_text().split())


def small_caps(soup):
    """R<small>OBERT</small> is Robert in small capitals; other <small> and <big> only change the size."""
    for tag in soup.find_all("small"):
        if tag.parent is None or tag.find_parent("small"):
            continue
        before = tag.previous_sibling
        text = tag.get_text()
        if isinstance(before, NavigableString) and re.search(r"[A-Z]$", before) and text.isupper():
            tag.replace_with(text.lower())
    for tag in soup.find_all(["small", "big"]):
        tag.unwrap()


def unlink(soup):
    """Links into the table of contents, to figures and from the notes to a chapter carry no meaning here."""
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "part23.html" in href or link.find_parent("p", class_="tx12a") and link.get("id"):
            continue  # note references and back links
        if href.startswith("http"):
            continue
        if "#d411519681" in href:
            continue  # the asterisk that points to the glossary note
        link.unwrap()


def heading(soup, tag, level):
    text = text_of(tag).replace("— ", "—").replace("Self- Organization", "Self-Organization")
    new = soup.new_tag(f"h{level}")
    new.string = text
    tag.replace_with(new)
    return new


def by_id(soup, ident):
    found = soup.find(id=ident)
    if found is None:
        raise SystemExit(f"error: no element {ident}")
    return found


def trim(tag):
    """No whitespace at the start or end of a paragraph's text."""
    strings = [s for s in tag.find_all(string=True)]
    if strings:
        strings[0].replace_with(strings[0].lstrip())
        strings = [s for s in tag.find_all(string=True)]
        strings[-1].replace_with(strings[-1].rstrip())


def append(soup, first, other, separator):
    """Move the content of paragraph other to the end of paragraph first."""
    trim(first)
    trim(other)
    first.append(soup.new_tag("br") if separator == "br" else separator)
    for child in list(other.contents):
        first.append(child)
    other.decompose()


def merge_lines(soup, ids, separator="br"):
    """Join paragraphs into the first one, separated by line breaks."""
    first = by_id(soup, ids[0])
    for ident in ids[1:]:
        append(soup, first, by_id(soup, ident), separator)
    return first


def wrap(soup, elements, name):
    for one, two in zip(elements, elements[1:]):
        if one.find_next_sibling(True) is not two:
            raise SystemExit(f"error: {one.get('id')} and {two.get('id')} are not next to each other")
    new = soup.new_tag(name)
    elements[0].insert_before(new)
    for element in elements:
        new.append(element.extract())
    return new


def strip_lead(tag, pattern):
    """Remove a leading bullet or number from a paragraph."""
    for piece in tag.find_all(string=True):
        if piece.strip():
            piece.replace_with(re.sub(pattern, "", piece, count=1))
            return


def lists(soup):
    for ids in NUMBERED:
        if not soup.find(id=ids[0]):
            continue
        items = [by_id(soup, i) for i in ids]
        for item in items:
            strip_lead(item, r"^\s*\d+\.\s*")
            item.name, item.attrs = "li", {}
        wrap(soup, items, "ol")
    run = []
    for p in soup.find_all("p"):
        if not ("pub" in (p.get("class") or []) or p.get("id") in BULLETS) or not text_of(p).startswith("•"):
            continue
        strip_lead(p, r"^\s*•\s*")
        p.name = "li"
        if run and run[-1].find_next_sibling(True) is not p:
            wrap(soup, run, "ul")
            run = []
        run.append(p)
    if run:
        wrap(soup, run, "ul")
    for li in soup.find_all("li"):
        li.attrs = {}


def boxes(soup, last_element):
    for div in soup.find_all("div", class_="a2"):
        if div.parent is None:
            continue
        first = div.find("p")
        if first is not None and text_of(first).startswith("INTERLUDE"):
            title = "Interlude • " + text_of(first).split("•", 1)[1].strip().replace("— ", "—")
            h3 = soup.new_tag("h3")
            h3.string = title
            first.replace_with(h3)
            for hr in div.find_all("hr"):
                hr.decompose()
            for inner in div.find_all("div", class_="a2"):
                inner.name, inner.attrs = "blockquote", {}
            if div is not last_element:
                div.append(soup.new_tag("hr"))
            div.unwrap()
        else:
            div.name, div.attrs = "blockquote", {}
    for div in soup.find_all("div", class_="a1"):
        if div.find("table"):
            div.unwrap()
            continue
        for p in div.find_all("p", class_=list(BOX_TITLES)):
            bold = soup.new_tag("b")
            bold.string = text_of(p)
            p.clear()
            p.append(bold)
        div.name, div.attrs = "blockquote", {}


def model_equations(soup):
    """One paragraph per group of equation lines, the lines separated by line breaks.

    Groups end at the blank paragraphs the EPUB puts between them, at titles ("Bathtub—for Figures 5, 6
    and 7", "Cooling"), at labels ("Figure 22:") and at a new stock; a label keeps the lines after it.
    """
    for div in soup.body.find_all("div"):
        div.unwrap()
    start = by_id(soup, MODEL_EQUATIONS)
    by_id(soup, "d411510056111").decompose()  # the blank that separated the title from the first line
    for ident in EQUATION_JOINS:
        line = by_id(soup, ident)
        append(soup, line.find_previous_sibling("p"), line, " ")
    groups, group = [], []

    def close():
        nonlocal group
        if group:
            groups.append(group)
        group = []

    for element in list(start.find_next_siblings(True)):
        text = text_of(element)
        if element.name == "br" or (element.name == "p" and not text and not element.find("img")):
            if not (len(group) == 1 and text_of(group[0]).endswith(":")):
                close()
            continue
        if element.name != "p" or element.find("img") or element.get("id") in EQUATION_PROSE or "tx11" in element["class"]:
            close()
            continue
        lead = next(c for c in element.contents if not (isinstance(c, NavigableString) and not c.strip()))
        italic = element.find_all("i")
        if getattr(lead, "name", None) == "b" or (len(italic) == 1 and text == text_of(italic[0])):
            close()  # a title or a label in italics: a paragraph of its own
            continue
        if text.startswith("Stock:") or (text.endswith(":") and len(text) < 30):
            close()
        group.append(element)
    close()
    for group in groups:
        for other in group[1:]:
            append(soup, group[0], other, "br")
    return len(groups)


def prepare(name, html):
    doc = key(name)
    soup = BeautifulSoup(fix_html(name, html), "html.parser")
    body = soup.body
    small_caps(soup)
    unlink(soup)
    for (document, number), leaked in LEAKS.items():
        if document != doc:
            continue
        link = next(a for a in soup.find_all("a", href=re.compile("part23")) if a.get_text(strip=True) == number)
        after = (link.find_parent("sup") or link).next_sibling
        if not isinstance(after, NavigableString) or not after.strip().startswith(leaked):
            raise SystemExit(f"error: {doc} note {number}: expected {leaked!r} after the reference, found {after!r}")
        rest = after.lstrip()[len(leaked):].lstrip()
        after.replace_with(" " + rest if rest.strip() else "")
    if doc not in TITLES:
        return str(soup)
    # Title elements: the chapter number and title paragraphs and the rules under them.
    for p in body.find_all("p", class_=["h9", "h7", "h13"]):
        p.decompose()
    if doc in PART_PAGES:
        for child in list(body.children):
            child.extract()
    if doc == "chap22":
        model_equations(soup)
    # Empty paragraphs and bare line breaks only make space; underscores are a printed rule.
    for p in body.find_all("p"):
        if not text_of(p).strip("_ ") and not p.find("img"):
            p.decompose()
    for br in body.find_all("br"):
        if br.parent is not None and br.parent.name in ("div", "body"):
            br.decompose()
    if doc == "chap13":
        star = by_id(soup, "d411519681")  # "* Definitions of words in bold face can be found in the Glossary."
        strip_lead(star, r"^\s*\*\s*")
        star["epub:type"] = "footnote"
    for p in body.find_all("p", class_=list(H2_CLASSES)):
        heading(soup, p, 2)
    for p in body.find_all("p"):
        if (set(p.get("class") or []) & H3_CLASSES) or p.get("id") in H3_IDS:
            heading(soup, p, 3)
    for ident in INTO_BOX:
        if soup.find(id=ident):
            paragraph = by_id(soup, ident)
            box = paragraph.find_previous_sibling(True)
            if box.name != "div" or "a1" not in box["class"]:
                raise SystemExit(f"error: no box before {ident}")
            box.append(paragraph.extract())
    for first, second in JOINS:
        if soup.find(id=first):
            append(soup, by_id(soup, first), by_id(soup, second), " ")
    for ids in VERSE:
        if soup.find(id=ids[0]):
            merge_lines(soup, ids)
    for ids in LINES:
        if soup.find(id=ids[0]):
            merge_lines(soup, ids)
    for ids in QUOTES:
        if soup.find(id=ids[0]):
            wrap(soup, [by_id(soup, i) for i in ids], "blockquote")
    lists(soup)
    content = [c for c in body.find_all(True, recursive=True) if c.name in ("p", "blockquote", "div", "h2", "h3", "ul", "ol", "table")]
    boxes(soup, content[-1].find_parent("div", class_="a2") if content else None)
    for div in body.find_all("div"):
        div.unwrap()
    title = soup.new_tag("h1")
    title.string = TITLES[doc]
    body.insert(0, title)
    return str(soup)


def toc(epub):
    """A table of contents with one entry per titled document, in spine order."""
    points = []
    for n, name in enumerate(sorted((n for n in epub.namelist() if key(n) in TITLES),
                                    key=lambda n: float(key(n)[4:])), 1):
        points.append(f'<navPoint id="p{n}" playOrder="{n}"><navLabel><text>{TITLES[key(name)]}</text></navLabel>'
                      f'<content src="{name[len(ROOT):]}"/></navPoint>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
            '<head></head><docTitle><text>Thinking in Systems</text></docTitle><navMap>' + "".join(points) + "</navMap></ncx>")


def main(source, target):
    epub = zipfile.ZipFile(source)
    with zipfile.ZipFile(target, "w") as out:
        for info in epub.infolist():
            data = epub.read(info.filename)
            if info.filename.endswith(".html"):
                data = prepare(info.filename, data.decode()).encode()
            elif info.filename == ROOT + "toc.ncx":
                data = toc(epub).encode()
            kind = zipfile.ZIP_STORED if info.filename == "mimetype" else zipfile.ZIP_DEFLATED
            out.writestr(info, data, compress_type=kind)
    print(f"prepared {target}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
