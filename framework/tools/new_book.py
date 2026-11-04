"""Create a new bilingual book folder: book.json, en/, zh-cn/, a glossary and a README to fill in.

    uv run --project framework/tools python framework/tools/new_book.py books/<id> --title 中文书名 --original-title "English Title" --authors "Author"

Next steps are printed at the end and described in framework/README.md.
"""

import argparse
from pathlib import Path
import re

import config as book_config

README = """# {title}

《{original}》（{authors}）的中英对照译本。

## 来源与许可

- 原书：{original}，{authors}。
- 英文原文的来源和版本：待填写（EPUB 文件名、出版社、版次）。
- 原书版权与本译文的许可：待填写。公开发布之前必须确认有权发布原文和译文。

## 翻译进度

在仓库根目录运行：

```bash
python3 scripts/site.py status {id}
```

## 目录

```text
book.json          书的信息和章节列表，每章的状态：todo（只有英文）、draft、review、done（发布）
en/                英文原文，每章一个 Markdown 文件，图片在 en/images/
zh-cn/             中文译文，与 en/ 同名同结构，逐块对应
glossary.md        术语表
review/            审校记录：source.md 记原文核对，每章一份 <章节 id>.md 记四项审校
assets/            封面、字体、章首章末图的数据（diagrams/）、代码示例的改写（code-variants/）
```

翻译和审校的流程见 [framework/README.md](../../framework/README.md)。
"""

GLOSSARY = """# 术语表

每个核心术语一行。译法定下来之前，状态写“待定”；定下来以后全书统一使用，改动时回查已经译完的章节。

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 状态 |
| --- | --- | --- | --- | --- | --- |
"""


def create(root, title, original, authors, summary=""):
    root = Path(root)
    key = root.name
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", key):
        raise ValueError(f"Use lowercase letters, digits and hyphens for the folder name: {key}")
    if root.exists():
        raise ValueError(f"{root} already exists")
    for folder in ("en", "zh-cn", "review", "assets/images", "assets/diagrams/sections"):
        (root / folder).mkdir(parents=True)
        (root / folder / ".gitkeep").write_text("")
    config = {"title": title, "originalTitle": original, "authors": authors, "reader": "bilingual",
              "summary": summary, "facts": [], "cover": "", "listed": True, "chapterMaps": False, "chapters": []}
    book_config.save(root, config)
    (root / "README.md").write_text(README.format(title=title, original=original, authors=authors, id=key))
    (root / "glossary.md").write_text(GLOSSARY)
    return key


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("book", type=Path, help="new folder, for example books/thinking-fast-and-slow")
    parser.add_argument("--title", required=True, help="Chinese title")
    parser.add_argument("--original-title", required=True)
    parser.add_argument("--authors", required=True)
    parser.add_argument("--summary", default="", help="one or two sentences for the bookshelf card")
    args = parser.parse_args()
    try:
        key = create(args.book, args.title, args.original_title, args.authors, args.summary)
    except ValueError as error:
        raise SystemExit(f"error: {error}")
    print(f"Created {args.book}. Next steps:")
    print(f"  1. python3 scripts/site.py import-epub {key} path/to/book.epub")
    print(f"  2. Translate a chapter into zh-cn/ and set its status to draft in {args.book}/book.json")
    print(f"  3. python3 scripts/site.py serve --drafts")


if __name__ == "__main__":
    main()
