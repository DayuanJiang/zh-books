import json
from pathlib import Path
import tempfile
import unittest
import zipfile

import book
import import_epub
import new_book

CONTAINER = """<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>"""
OPF = """<?xml version="1.0"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0">
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>
    <item id="intro" href="text/intro.xhtml" media-type="application/xhtml+xml"/>
    <item id="c1" href="text/c1.xhtml" media-type="application/xhtml+xml"/>
    <item id="c2" href="text/c2.xhtml" media-type="application/xhtml+xml"/>
    <item id="notes" href="text/notes.xhtml" media-type="application/xhtml+xml"/>
    <item id="img" href="images/fig.png" media-type="image/png"/>
  </manifest>
  <spine><itemref idref="cover"/><itemref idref="nav"/><itemref idref="intro"/><itemref idref="c1"/><itemref idref="c2"/><itemref idref="notes"/></spine>
</package>"""
PAGE = '<?xml version="1.0"?><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"><body>{}</body></html>'
FILES = {
    "OEBPS/nav.xhtml": PAGE.format('<nav epub:type="toc"><ol><li><a href="text/intro.xhtml">Introduction</a></li>'
                                   '<li><a href="text/c1.xhtml">1 The Characters of the Story</a></li>'
                                   '<li><a href="text/c2.xhtml#start">Chapter II. Attention</a></li></ol></nav>'),
    "OEBPS/cover.xhtml": PAGE.format('<div> </div>'),
    "OEBPS/text/intro.xhtml": PAGE.format('<h2>Introduction</h2><p>Every author hopes.<a epub:type="noteref" href="notes.xhtml#n1">1</a></p>'
                                          '<p><img src="../images/fig.png" alt="A figure"/></p>'),
    "OEBPS/text/c1.xhtml": PAGE.format('<h1>1 The Characters of the Story</h1><h2>Two Systems</h2>'
                                       '<p>System 1 operates automatically.<a epub:type="noteref" href="notes.xhtml#n2">2</a></p>'
                                       '<ul><li>fast</li><li>slow</li></ul>'),
    "OEBPS/text/c2.xhtml": PAGE.format('<h2 id="start">Chapter II. Attention<a href="#fn1" id="r1"><sup>[1]</sup></a></h2>'
                                       '<p>Effort is limited.</p>'
                                       '<p class="footnote"><a id="fn1"/><a href="#r1">[1]</a> A plain linked footnote.</p>'),
    "OEBPS/text/notes.xhtml": PAGE.format('<h1>Notes</h1><aside epub:type="endnote" id="n1"><p>1. First <em>endnote</em>.</p></aside>'
                                          '<aside epub:type="endnote" id="n2"><p>2. Second endnote.</p></aside>'),
}


class ImportEpubTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        base = Path(self.folder.name)
        self.epub = base / "fixture.epub"
        with zipfile.ZipFile(self.epub, "w") as archive:
            archive.writestr("mimetype", "application/epub+zip")
            archive.writestr("META-INF/container.xml", CONTAINER)
            archive.writestr("OEBPS/content.opf", OPF)
            archive.writestr("OEBPS/images/fig.png", b"\x89PNG fixture")
            for name, text in FILES.items():
                archive.writestr(name, text)
        self.root = base / "fixture-book"
        new_book.create(self.root, "测试书", "Fixture Book", "Someone")

    def tearDown(self):
        self.folder.cleanup()

    def test_sections_notes_numbers_and_images(self):
        message = import_epub.import_epub(self.root, self.epub)
        self.assertEqual(message, "Imported 3 sections, 3 notes and 1 images from fixture.epub.")
        config = json.loads((self.root / "book.json").read_text())
        self.assertEqual(config["chapters"], [
            {"id": "introduction", "file": "01-introduction.md", "status": "todo"},
            {"id": "ch01", "number": 1, "file": "02-1-the-characters-of-the-story.md", "status": "todo"},
            {"id": "ch02", "number": 2, "file": "03-chapter-ii-attention.md", "status": "todo"},
        ])
        self.assertEqual(len(config["source"]["sha256"]), 64)
        intro = (self.root / "en/01-introduction.md").read_text()
        self.assertTrue(intro.startswith("# Introduction\n"))
        self.assertIn("Every author hopes.[^1]", intro)
        self.assertIn("[^1]: First *endnote*.", intro)
        self.assertIn("![A figure](images/fig.png)", intro)
        self.assertTrue((self.root / "en/images/fig.png").exists())
        chapter = (self.root / "en/02-1-the-characters-of-the-story.md").read_text()
        self.assertIn("## Two Systems", chapter)
        self.assertIn("[^1]: Second endnote.", chapter)
        linked = (self.root / "en/03-chapter-ii-attention.md").read_text()
        self.assertTrue(linked.startswith("# Chapter II. Attention[^1]\n"))
        self.assertIn("[^1]: A plain linked footnote.", linked)
        self.assertNotIn("[1]", linked)
        # Every imported section parses into blocks the aligner understands, with each note defined once.
        for entry in config["chapters"]:
            blocks, notes = book.parse((self.root / "en" / entry["file"]).read_text())
            self.assertEqual(blocks[0].kind, "heading")
            self.assertEqual(list(notes), ["1"])

    def test_import_refuses_to_replace_started_work(self):
        import_epub.import_epub(self.root, self.epub)
        with self.assertRaisesRegex(ValueError, "--force"):
            import_epub.import_epub(self.root, self.epub)
        self.assertIn("Imported 3 sections", import_epub.import_epub(self.root, self.epub, force=True))
        config = json.loads((self.root / "book.json").read_text())
        config["chapters"][0]["status"] = "draft"
        (self.root / "zh-cn" / config["chapters"][0]["file"]).write_text("# 引言\n")
        (self.root / "book.json").write_text(json.dumps(config))
        with self.assertRaisesRegex(ValueError, "already being translated"):
            import_epub.import_epub(self.root, self.epub, force=True)


KINDLE_OPF = """<?xml version="1.0"?>
<package xmlns="http://www.idpf.org/2007/opf" version="2.0">
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="s0" href="split_000.html" media-type="application/xhtml+xml"/>
    <item id="s1" href="split_001.html" media-type="application/xhtml+xml"/>
    <item id="s2" href="split_002.html" media-type="application/xhtml+xml"/>
    <item id="s3" href="split_003.html" media-type="application/xhtml+xml"/>
  </manifest>
  <spine toc="ncx"><itemref idref="s0"/><itemref idref="s1"/><itemref idref="s2"/><itemref idref="s3"/></spine>
</package>"""
# The contents links point near the end of the previous file, as in books converted from Kindle files.
KINDLE_NCX = """<?xml version="1.0"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/"><navMap>
  <navPoint id="a"><navLabel><text>Introduction</text></navLabel><content src="split_001.html"/></navPoint>
  <navPoint id="b"><navLabel><text>1. The Characters of the Story</text></navLabel><content src="split_001.html#p9"/></navPoint>
  <navPoint id="c"><navLabel><text>2. Attention and Effort</text></navLabel><content src="split_002.html#p8"/></navPoint>
</navMap></ncx>"""
BOLD = '<p class="c2"><span class="c3"><span class="bold">{}</span></span></p>'
KINDLE = {
    "split_000.html": PAGE.format('<p><b>Contents</b></p>' + "".join(f'<p><a href="split_00{i}.html#x">Entry {i}</a></p>' for i in (1, 2, 3, 1, 2))),
    "split_001.html": PAGE.format(BOLD.format("Introduction") + "<p>Every author hopes.</p>"),
    "split_002.html": PAGE.format(BOLD.format("The Characters of the Story") + "<p>Glance at the image.</p>"
                                  + BOLD.format("Two Systems") + '<p>System 1 is fast.</p><p id="p8"> </p><p>“A quote after the anchor.”</p>'),
    "split_003.html": PAGE.format(BOLD.format("Attention and Effort") + "<p>System 2 is slow.</p>"),
}


class KindleEpubTests(unittest.TestCase):
    def test_bold_headings_and_contents_labels_matched_by_title(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            epub = base / "kindle.epub"
            with zipfile.ZipFile(epub, "w") as archive:
                archive.writestr("mimetype", "application/epub+zip")
                archive.writestr("META-INF/container.xml", CONTAINER.replace("OEBPS/content.opf", "content.opf"))
                archive.writestr("content.opf", KINDLE_OPF)
                archive.writestr("toc.ncx", KINDLE_NCX)
                for name, text in KINDLE.items():
                    archive.writestr(name, text)
            root = base / "kindle-book"
            new_book.create(root, "测试书", "Fixture Book", "Someone")
            self.assertEqual(import_epub.import_epub(root, epub), "Imported 3 sections, 0 notes and 0 images from kindle.epub.")
            config = json.loads((root / "book.json").read_text())
            self.assertEqual([(c["id"], c.get("number")) for c in config["chapters"]],
                             [("introduction", None), ("ch01", 1), ("ch02", 2)])
            chapter = (root / "en" / config["chapters"][1]["file"]).read_text()
            self.assertTrue(chapter.startswith("# 1. The Characters of the Story\n"))
            self.assertIn("\n## Two Systems\n", chapter)
            self.assertTrue((root / "en" / config["chapters"][2]["file"]).read_text().startswith("# 2. Attention and Effort\n"))


if __name__ == "__main__":
    unittest.main()
