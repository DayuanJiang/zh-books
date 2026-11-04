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


if __name__ == "__main__":
    unittest.main()
