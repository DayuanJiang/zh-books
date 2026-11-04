# Reader Dependencies

- Docsify 4.13.1 and its zoom-image plugin, MIT license. The existing v4 architecture is retained.
- Docsify Vue base CSS: its remote Google Fonts import and its rule that shrinks code inside prose are removed;
  the reader sets fonts and code sizes itself.
- Prism 1.29.0 language components (Python, Java, C, C++, Go), MIT license. They extend the Prism
  instance bundled inside Docsify so code examples are highlighted, including the Python rewrites.
- Noto Serif SC (思源宋体) Regular and SemiBold from notofonts/noto-cjk, SIL Open Font License 1.1, subset to the
  characters each book uses and stored as WOFF2 in `books/<id>/assets/fonts/` with the license. Rebuild with
  `python3 scripts/site.py fonts <id>`.
- `../reader-icons.svg` (interface sprite) and `framework/tools/icons.json` (icon paths used inside the generated
  chapter figures) are built from Lucide Static 0.468.0 icons. See the included license.

Reproduce with `uv run --project framework/tools python framework/tools/fetch_reader_assets.py`.
The reading surface uses local dependencies only. Full-text search is implemented in `../reader.js`
over the search index the build writes to each book's `assets/search-index.json`, which the browser downloads
on the first search.
