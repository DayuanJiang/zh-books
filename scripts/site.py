#!/usr/bin/env python3
"""One entry point for every book in the repository.

    python3 scripts/site.py list [--json]              books found under books/
    python3 scripts/site.py check <book>               the checks CI runs for one book
    python3 scripts/site.py build [--drafts]           all books and the bookshelf into _site/
    python3 scripts/site.py serve [--drafts] [--port]  build, then preview at http://127.0.0.1:8000/zh-books/
    python3 scripts/site.py new <book> --title ... --original-title ... --authors ...
    python3 scripts/site.py import-epub <book> <file.epub> [--force]
    python3 scripts/site.py status <book>              translation progress per chapter
    python3 scripts/site.py fonts <book>               rebuild the book's Chinese font subset
    python3 scripts/site.py sync-skill [--check]       copy your personal en-zh-translation-polish skill into the repo

A book is a folder books/<id>/ with a book.json. Books with "reader": "bilingual" use the shared reader in
framework/; books with "reader": "custom" bring their own build ("build", "output" and "checks" in book.json).
Site details (title, public URL, repository) are in site.json.
"""

import argparse
import functools
import html
import http.server
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit

REPO = Path(__file__).resolve().parents[1]
BOOKS = REPO / "books"
SITE = json.loads((REPO / "site.json").read_text())
PREFIX = urlsplit(SITE["url"]).path  # "/zh-books/"
TOOLS = ["uv", "run", "--quiet", "--project", str(REPO / "framework" / "tools")]
# The translation skill lives in the user's personal skills folder (the main copy) and is mirrored into the repo,
# where Codex reads .agents/skills/ and Claude Code reads .claude/skills/ (a link to the same folder).
SKILL = "en-zh-translation-polish"
SKILL_COPY = REPO / ".agents" / "skills" / SKILL
SKILL_SOURCES = [Path.home() / ".claude" / "skills" / SKILL, Path.home() / ".agents" / "skills" / SKILL]
SKILL_SKIP = {"__pycache__", ".pytest_cache", ".DS_Store"}


def books():
    """{id: book.json} for every book folder, in folder-name order."""
    return {path.parent.name: json.loads(path.read_text()) for path in sorted(BOOKS.glob("*/book.json"))}


def book_or_exit(key):
    found = books()
    if key not in found:
        raise SystemExit(f"error: no book {key}; books: {', '.join(found)}")
    return found[key]


def run(command, cwd=REPO, env=None):
    """Run a command (a list, or a shell string from book.json) and stop on failure."""
    shown = command if isinstance(command, str) else " ".join(command)
    print(f"$ {shown}", flush=True)
    result = subprocess.run(command, cwd=cwd, shell=isinstance(command, str), env={**os.environ, **(env or {})})
    if result.returncode:
        raise SystemExit(f"error: command failed ({result.returncode}): {shown}")


def tool(name, *args):
    run(TOOLS + ["python", str(REPO / "framework" / "tools" / name), *map(str, args)])


def links(key):
    return {"url": f"{SITE['url']}{key}/", "repo": f"{SITE['repo']}/tree/main/books/{key}"}


def custom_env(key):
    return {"BOOK_BASE": f"{PREFIX}{key}/", "BOOK_URL": links(key)["url"]}


def publishable(config, drafts):
    if config.get("reader") == "custom":
        return True
    return any(c["status"] == "done" or (drafts and c["status"] != "todo") for c in config.get("chapters", []))


def check(key):
    config = book_or_exit(key)
    folder = BOOKS / key
    if config.get("reader") == "custom":
        for command in config.get("checks", []) + config.get("build", []):
            run(command, cwd=folder, env=custom_env(key))
        return
    if not publishable(config, True):
        print(f"{key}: nothing translated yet, skipping the build check")
        return
    # A book with no finished chapter yet is checked as a draft build, the same way the site skips it.
    drafts = [] if publishable(config, False) else ["--drafts"]
    if drafts:
        print(f"{key}: no finished chapter yet, checking the draft build")
    with tempfile.TemporaryDirectory() as out:
        tool("build.py", folder, out, "--url", links(key)["url"], "--repo", links(key)["repo"], *drafts)
    if list((folder / "tools").glob("test_*.py")):
        run(TOOLS + ["--with", "pytest", "pytest", "-q", str(folder / "tools")])
    for command in config.get("checks", []):
        run(command, cwd=folder)


def skill_files(folder):
    """{relative path: bytes} of a skill folder, without caches and macOS metadata files."""
    files = {}
    for path in sorted(folder.rglob("*")):
        relative = path.relative_to(folder)
        if path.is_file() and not (set(relative.parts) & SKILL_SKIP) and not path.name.startswith("._"):
            files[relative.as_posix()] = path.read_bytes()
    return files


def sync_skill(check_only):
    source = next((s for s in SKILL_SOURCES if (s / "SKILL.md").exists()), None)
    if source is None:
        raise SystemExit(f"error: no personal copy of {SKILL} in {' or '.join(map(str, SKILL_SOURCES))}")
    new, old = skill_files(source.resolve()), skill_files(SKILL_COPY) if SKILL_COPY.exists() else {}
    changed = sorted(name for name in new if old.get(name) != new[name])
    removed = sorted(set(old) - set(new))
    for name in changed:
        print(f"{'update' if name in old else 'add'}: {name}")
    for name in removed:
        print(f"remove: {name}")
    if not changed and not removed:
        print(f"{SKILL_COPY.relative_to(REPO)} matches {source}")
        return
    if check_only:
        raise SystemExit(f"error: the repo copy differs from {source}; run: python3 scripts/site.py sync-skill")
    for name in changed:
        target = SKILL_COPY / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(new[name])
    for name in removed:
        (SKILL_COPY / name).unlink()
    print(f"Copied {len(changed)} files and removed {len(removed)} from {source}")


def card(key, config):
    """One bookshelf card from a book.json."""
    e = html.escape
    cover = (f'<a class="cover" href="{key}/" tabindex="-1" aria-hidden="true"><img src="{key}/{e(config["cover"])}" alt="" width="112"></a>'
             if config.get("cover") else f'<a class="cover placeholder" href="{key}/" tabindex="-1" aria-hidden="true"><span>{e(config["title"])}</span></a>')
    facts = "".join(f"<li>{e(fact)}</li>" for fact in config.get("facts", []))
    extra = "".join(f'<a href="{key}/{e(link["href"])}"' + (f' lang="{e(link["lang"])}"' if link.get("lang") else "") + f'>{e(link["label"])}</a>'
                    for link in config.get("links", []))
    authors = f" · {e(config['authors'])}" if config.get("authors") else ""
    return f"""      <article class="book">
        {cover}
        <div class="info">
          <h2><a href="{key}/">{e(config["title"])}</a></h2>
          <p class="original">{e(config["originalTitle"])}{authors}</p>
          <p class="summary">{e(config.get("summary", ""))}</p>
          <ul class="facts">{facts}</ul>
          <div class="actions">
            <a class="primary" href="{key}/">开始阅读</a>{extra}
            <a href="{e(links(key)["repo"])}">源文件</a>
          </div>
        </div>
      </article>"""


def build(drafts=False, out=REPO / "_site"):
    if out.exists():
        shutil.rmtree(out)
    out.mkdir()
    cards = []
    for key, config in books().items():
        if not publishable(config, drafts):
            print(f"skip {key}: no finished chapter yet (build with --drafts to include it)")
            continue
        folder = BOOKS / key
        print(f"== {config['title']} ({key})", flush=True)
        if config.get("reader") == "custom":
            for command in config["build"]:
                run(command, cwd=folder, env=custom_env(key))
            shutil.copytree(folder / config["output"], out / key)
        else:
            tool("build.py", folder, out / key, "--url", links(key)["url"], "--repo", links(key)["repo"], *(["--drafts"] if drafts else []))
        if config.get("listed", True):
            cards.append(card(key, config))
    page = (REPO / "site" / "shelf.html").read_text()
    for name, value in {"title": SITE["title"], "lead": SITE["lead"], "repo": SITE["repo"]}.items():
        page = page.replace("{{" + name + "}}", html.escape(value))
    (out / "index.html").write_text(page.replace("{{books}}", "\n\n".join(cards)))
    print(f"Site ready in {out.relative_to(REPO)}/ ({len(cards)} books on the shelf)")


def serve(port, drafts):
    build(drafts)
    root = (REPO / "_site").resolve()

    class Handler(http.server.SimpleHTTPRequestHandler):
        """Serve _site/ under the same path prefix as the public site."""

        def do_GET(self):
            if self.path in ("/", ""):
                body = f'<meta http-equiv="refresh" content="0; url={PREFIX}"><a href="{PREFIX}">{PREFIX}</a>'.encode()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            super().do_GET()

        def translate_path(self, path):
            if not path.startswith(PREFIX):
                return str(root / "__not_found__")
            return super().translate_path("/" + path[len(PREFIX):])

        def end_headers(self):
            self.send_header("Cache-Control", "no-store")
            super().end_headers()

    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(Handler, directory=str(root)))
    print(f"Preview: http://127.0.0.1:{port}{PREFIX}  (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list").add_argument("--json", action="store_true")
    sub.add_parser("check").add_argument("book")
    sub.add_parser("build").add_argument("--drafts", action="store_true")
    p = sub.add_parser("serve")
    p.add_argument("--drafts", action="store_true")
    p.add_argument("--port", type=int, default=8000)
    p = sub.add_parser("new")
    p.add_argument("book")
    p.add_argument("--title", required=True)
    p.add_argument("--original-title", required=True)
    p.add_argument("--authors", required=True)
    p.add_argument("--summary", default="")
    p = sub.add_parser("import-epub")
    p.add_argument("book")
    p.add_argument("epub", type=Path)
    p.add_argument("--force", action="store_true")
    sub.add_parser("status").add_argument("book")
    sub.add_parser("fonts").add_argument("book")
    p = sub.add_parser("roles", help="list whole-italic paragraphs for a model or person to judge (roles.json)")
    p.add_argument("book")
    p.add_argument("--all", action="store_true")
    sub.add_parser("sync-skill").add_argument("--check", action="store_true", help="only report differences")
    args = parser.parse_args()

    if args.command == "list":
        found = books()
        if args.json:
            print(json.dumps(list(found)))
        else:
            for key, config in found.items():
                print(f"{key}\t{config.get('reader', 'bilingual')}\t{config['title']}")
    elif args.command == "check":
        check(args.book)
    elif args.command == "build":
        build(args.drafts)
    elif args.command == "serve":
        serve(args.port, args.drafts)
    elif args.command == "new":
        tool("new_book.py", BOOKS / args.book, "--title", args.title, "--original-title", args.original_title,
             "--authors", args.authors, "--summary", args.summary)
    elif args.command == "import-epub":
        book_or_exit(args.book)
        tool("import_epub.py", BOOKS / args.book, args.epub.resolve(), *(["--force"] if args.force else []))
    elif args.command == "status":
        book_or_exit(args.book)
        tool("status.py", BOOKS / args.book)
    elif args.command == "sync-skill":
        sync_skill(args.check)
    elif args.command == "roles":
        book_or_exit(args.book)
        result = subprocess.run(TOOLS + ["python", str(REPO / "framework" / "tools" / "roles.py"), str(BOOKS / args.book),
                                         *(["--all"] if args.all else [])])
        return result.returncode
    elif args.command == "fonts":
        book_or_exit(args.book)
        run(TOOLS + ["--with", "fonttools", "--with", "brotli", "python", str(REPO / "framework" / "tools" / "fonts.py"), str(BOOKS / args.book)])


if __name__ == "__main__":
    sys.exit(main())
