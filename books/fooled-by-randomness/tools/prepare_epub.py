"""Make a copy of the EPUB whose markup the importer understands (see review/source.md for why each step exists).

    uv run --project framework/tools python -I books/fooled-by-randomness/tools/prepare_epub.py book.epub prepared.epub
    python3 scripts/site.py import-epub fooled-by-randomness prepared.epub --force
    uv run --project framework/tools python -I books/fooled-by-randomness/tools/curate_source.py book.epub
    uv run --project framework/tools python -I books/fooled-by-randomness/tools/check_source.py book.epub

This EPUB is a Kindle conversion (Epubor eCore) of the Random House e-book. Its markup has no heading tags:
headings, block quotes and lists are paragraphs with CSS classes. The copy:
- joins the text the converter split after every inline tag (a newline plus a space before "," or "—"), and the
  drop cap letters ("T his" becomes "This");
- turns the heading classes into h1/h2/h3 (title case for the all-caps headings), chapter titles into "1. Title",
  indented quotations into <blockquote>, numbered paragraphs into <ol>, the run-in phrases of chapter 5 into bold;
- removes ornaments ("•"), the empty boxes left where the tables and figures were, and links to other files;
- marks the two asterisk notes of chapter 7 as note references, so they become footnotes;
- renames the table of contents entries after the new headings, so section ids and file names follow them.
"""

import re
import sys
import zipfile

from bs4 import BeautifulSoup, NavigableString

NUMBERS = {w: n for n, w in enumerate("One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen".split(), 1)}
SMALL_WORDS = {"a", "an", "the", "and", "but", "or", "nor", "for", "on", "in", "at", "to", "by", "of", "as", "via", "with", "from", "between"}
SPECIAL_WORDS = {"PALMPILOT": "PalmPilot", "CNBC": "CNBC", "O.’S": "O.’s", "DE": "de", "I": "I", "II": "II", "III": "III"}
# Drop caps that are a word of their own: "I start", "I used", "A couple".
SEPARATE_DROP_CAPS = {"text00008.html", "text00011.html", "text00023.html"}
SUBSCRIPTS = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
INLINE = r"(?:em|b|i|small|span|a|sup|sub)"


def title_case(text):
    """'IF YOU’RE SO RICH, WHY AREN’T YOU SO SMART?' -> 'If You’re So Rich, Why Aren’t You So Smart?'."""
    if text != text.upper():
        return text
    words, out = text.split(), []
    for i, word in enumerate(words):
        lead = i == 0 or out[-1].endswith((":", "—"))
        if word in SPECIAL_WORDS:
            out.append(SPECIAL_WORDS[word])
            continue
        parts = re.split(r"([-—(])", word)
        cased = []
        for j, part in enumerate(parts):
            if part in ("-", "—", "("):
                cased.append(part)
                continue
            plain = re.sub(r"\W", "", part).lower()
            first = j == 0 and lead or (j > 0 and parts[j - 1] in "—(")
            if plain in SMALL_WORDS and not first and j == 0:
                cased.append(part.lower())
            else:
                k = next((n for n, c in enumerate(part) if c.isalpha()), 0)
                cased.append(part[:k] + part[k:k + 1].upper() + part[k + 1:].lower())
        out.append("".join(cased))
    return " ".join(out)


def text_of(tag):
    return " ".join(tag.get_text(" ").split()).replace(" :", ":")


def clean_whitespace(html):
    """Undo the converter's line breaks: a newline is a space, except before punctuation and around dashes."""
    html = re.sub(r"\s*\n\s*", " ", html.replace("&#13;", "").replace("\r", ""))
    html = re.sub(r"<br/>\s+", "<br/>", html)
    html = re.sub(rf"(</{INLINE}>)\s+(?=[,.;:)\]’”?!—]|</{INLINE}>)", r"\1", html)
    html = re.sub(rf"(<{INLINE}>)\s+(?=<{INLINE}>)", r"\1", html)
    return re.sub(rf"—(</{INLINE}>)\s+", r"—\1", html)


def heading(soup, tag, level, text):
    """Replace a paragraph with a heading that holds plain text."""
    new = soup.new_tag(f"h{level}")
    new.string = text
    tag.replace_with(new)


def italic_paragraph(soup, tag, text):
    new, em = soup.new_tag("p"), soup.new_tag("em")
    em.string = text
    new.append(em)
    tag.replace_with(new)


def trim(tag):
    """Strip the spaces at the start and the end of a block."""
    texts = tag.find_all(string=True)
    if texts:
        first, last = texts[0], texts[-1]
        if first is last:
            first.replace_with(first.strip())
        else:
            first.replace_with(first.lstrip())
            last.replace_with(last.rstrip())


def depth(tag):
    """Heading level from the anchor id the table of contents links to: c01.1 is level 2, c01.1.1 level 3."""
    anchor = tag.find("a", id=True)
    return anchor["id"].count(".") + 1 if anchor else None


def section_title(soup, name, p):
    """Turn the title paragraphs of a file into one h1 and return its text."""
    if name == "text00003.html":  # PREFACE + TAKING KNOWLEDGE LESS SERIOUSLY
        title = "Preface: " + title_case(text_of(p("fmsh")[0]))
        p("fmsh")[0].decompose()
        heading(soup, p("fmh")[0], 1, title)
    elif name == "text00005.html":  # PROLOGUE + MOSQUES IN THE CLOUDS
        title = title_case(text_of(p("ct")[0])) + ": " + title_case(text_of(p("imp")[0]))
        p("imp")[0].decompose()
        heading(soup, p("ct")[0], 1, title)
    elif name == "text00028.html":  # A TRIP TO THE LIBRARY + Notes and Reading Recommendations
        title = title_case(text_of(p("ct")[0])) + ": " + text_of(p("fmh1")[0])
        p("fmh1")[0].decompose()
        heading(soup, p("ct")[0], 1, title)
    elif p("pn"):  # part pages: "Part I", "SOLON’S WARNING" and a subtitle
        title = text_of(p("pn")[0]) + ": " + title_case(text_of(p("pt")[0]))
        p("pn")[0].decompose()
        heading(soup, p("pt")[0], 1, title)
        italic_paragraph(soup, p("pst")[0], text_of(p("pst")[0]))
    elif p("cn"):  # chapters ("One" and the title), epilogue and postscript
        label, text = text_of(p("cn")[0]), title_case(text_of(p("ct")[0]))
        title = f"{NUMBERS[label]}. {text}" if label in NUMBERS else f"{label}: {text}"
        p("cn")[0].decompose()
        heading(soup, p("ct")[0], 1, title)
    elif p("fmh") or p("ct") or soup.body.find("h1"):
        first = (p("fmh") or p("ct") or [soup.body.find("h1")])[0]
        title = title_case(text_of(first))
        heading(soup, first, 1, title)
    else:
        return None  # the dedication and the list of other books have no heading
    return title


def prepare(name, html, titles):
    soup = BeautifulSoup(clean_whitespace(html), "html.parser")
    body = soup.body
    p = lambda cls: body.find_all("p", class_=cls)  # noqa: E731

    # Ornaments, the empty boxes of the missing tables and figures, line breaks between blocks.
    for tag in body.find_all("p"):
        if text_of(tag) == "•" or (tag.get("class") == ["atx"] and not text_of(tag)):
            tag.decompose()
    for tag in body.find_all("div", class_=re.compile("^figure_")) + body.find_all("hr"):
        tag.decompose()
    for br in body.find_all("br"):
        if br.parent.name in ("div", "body"):
            br.decompose()

    # Headings, while the anchors that give their level are still there.
    title = section_title(soup, name, p)
    if title:
        titles[name] = title
    for span in body.find_all("span", class_="dis"):  # chapter summaries: "ONE: IF YOU’RE SO RICH, ..."
        heading(soup, span.find_parent("p"), 2, title_case(text_of(span)))
    for tag in p("fmh1"):
        heading(soup, tag, 2, text_of(tag))
    for tag in p("imp"):
        heading(soup, tag, 2, title_case(text_of(tag)))
    for tag in p("atx") + p("epi"):
        text = text_of(tag)
        if not (text.startswith("Table") or "afflicted persons" in text):  # captions and a fraction stay paragraphs
            heading(soup, tag, depth(tag) or 3, title_case(text))
    if not body.find("h2"):
        for tag in body.find_all("h3"):
            tag.name = "h2"

    # Links: the two asterisk notes become note references; links to other files of the book become plain text.
    for link in body.find_all("a", href=True):
        if link["href"].startswith("text00030.html#"):
            link["epub:type"] = "noteref"
        elif not link["href"].startswith("http"):
            link.unwrap()
    for anchor in body.find_all("a", href=False):
        anchor.decompose()
    for cap in body.find_all("span", class_="ic"):
        after = cap.next_sibling
        if isinstance(after, NavigableString) and name not in SEPARATE_DROP_CAPS:
            after.replace_with(after.lstrip())
        cap.unwrap()
    for sub in body.find_all("sub"):
        sub.replace_with(sub.get_text().translate(SUBSCRIPTS))
    for span in body.find_all("span", class_="ls1"):  # run-in phrases in chapter 5
        span.name = "b"
    if name == "text00032.html":  # the author's name in small capitals
        for span in body.find_all("span", class_="small"):
            span.replace_with(span.get_text().lower())

    # Indented blocks: the chapter abstract, numbered lists, table captions, quotations.
    for box in body.find_all("div", class_="blockquote"):
        paragraphs = box.find_all("p")
        if box.find("p", class_="cepi") or all(text_of(t).startswith("Table") for t in paragraphs):
            box.unwrap()
        elif box.find("p", class_="nl"):
            items = soup.new_tag("ol")
            for number, tag in enumerate(paragraphs, 1):
                text = tag.contents[0]
                if not (isinstance(text, NavigableString) and text.startswith(f"{number}.")):
                    raise SystemExit(f"error: {name}: list item {number} does not start with its number")
                text.replace_with(text[len(f"{number}."):])
                tag.name = "li"
                items.append(tag.extract())
            box.replace_with(items)
        else:
            quote = soup.new_tag("blockquote")
            quote.extend([t.extract() for t in paragraphs])
            box.replace_with(quote)
    for div in body.find_all("div", class_="div"):
        div.unwrap()
    for tag in body.find_all(["p", "li", "h1", "h2", "h3"]):
        trim(tag)
    return str(soup)


def prepare_notes(html):
    """The footnotes file: drop the asterisk and the return link inside each note."""
    soup = BeautifulSoup(clean_whitespace(html), "html.parser")
    for tag in soup.find_all(["sup", "br"]):
        tag.decompose()
    for link in soup.find_all("a", class_="hlink"):
        link.decompose()
    for tag in soup.find_all("p"):
        trim(tag)
    return str(soup)


def retitle_toc(ncx, titles):
    """Name each table of contents entry after the new first heading of the file it opens."""
    def label(match):
        text = titles.get(match.group(4).split("#")[0], match.group(2))
        return match.group(1) + text.replace("&", "&amp;") + match.group(3) + match.group(4)
    return re.sub(r'(<navLabel>\s*<text>)([^<]*)(</text>\s*</navLabel>\s*<content src=")([^"]+)', label, ncx)


def main(source, target):
    epub = zipfile.ZipFile(source)
    titles, pages = {}, {}
    for info in epub.infolist():
        name = info.filename.rsplit("/", 1)[-1]
        if re.fullmatch(r"text000(0[3-9]|1\d|2\d|3[12])\.html", name):
            pages[info.filename] = prepare(name, epub.read(info.filename).decode(), titles)
        elif name == "text00030.html":
            pages[info.filename] = prepare_notes(epub.read(info.filename).decode())
    for info in epub.infolist():
        if info.filename.endswith("toc.ncx"):
            pages[info.filename] = retitle_toc(epub.read(info.filename).decode(), titles)
    with zipfile.ZipFile(target, "w") as out:
        for info in epub.infolist():
            data = pages[info.filename].encode() if info.filename in pages else epub.read(info.filename)
            kind = zipfile.ZIP_STORED if info.filename == "mimetype" else zipfile.ZIP_DEFLATED
            out.writestr(info, data, compress_type=kind)
    for name, title in sorted(titles.items()):
        print(f"{name}: {title}")
    print(f"{len(pages)} files rewritten -> {target}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
