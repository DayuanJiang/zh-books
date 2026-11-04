#!/usr/bin/env bash
# Build every book into _site/, the folder that GitHub Pages serves.
#
#   _site/index.html        bookshelf (copied from site/)
#   _site/aposd2e/          VuePress build of books/aposd2e
#   _site/swe-at-google/    tracked files of books/swe-at-google (Docsify renders them in the browser)
#
# Usage: bash scripts/build-site.sh
set -euo pipefail
cd "$(dirname "$0")/.."

OUT=_site
rm -rf "$OUT"
mkdir -p "$OUT"

echo "Bookshelf"
cp -R site/. "$OUT/"

echo "A Philosophy of Software Design (books/aposd2e)"
(
  cd books/aposd2e
  [ -d node_modules ] || npm ci --no-audit --no-fund
  npm run build
)
cp -R books/aposd2e/docs/.vuepress/dist "$OUT/aposd2e"

echo "Software Engineering at Google (books/swe-at-google)"
# Docsify needs no build step: publish the tracked files as they are, like the old repository's Pages site did.
git -C books/swe-at-google ls-files -z | rsync -a --from0 --files-from=- books/swe-at-google/ "$OUT/swe-at-google/"

echo "Site ready in $OUT/"
