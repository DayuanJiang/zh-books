# AI 帝国

凯伦·郝（Karen Hao）《Empire of AI: Dreams and Nightmares in Sam Altman's OpenAI》（Penguin Press，2025）的中英对照译本，从英文原文直接翻译。

## 来源与许可

- 原书版权归 Karen Hao 所有。这份译文没有获得授权，发布与否由用户决定。
- 英文原文来自用户提供的 EPUB（美国 Penguin Press 版）。导入和整理的过程见 [review/source.md](review/source.md)，电子书文件本身不放进仓库。

## 翻译进度

在仓库根目录运行：

```bash
python3 scripts/site.py status empire-of-ai
```

## 目录

```text
book.json          书的信息和章节列表，每章的状态：todo（只有英文）、draft、review、done（发布）
en/                英文原文，每章一个 Markdown 文件；书末注释已改成各章的脚注
zh-cn/             中文译文，与 en/ 同名同结构，逐块对应
glossary.md        术语表
review/            审校记录：source.md 记原文核对，每章一份 <章节 id>.md 记四项审校
assets/            封面和字体
tools/             导入 EPUB 时用的两个脚本
```

翻译和审校的流程见 [framework/README.md](../../framework/README.md)。
