# 清单革命

阿图·葛文德（Atul Gawande）《The Checklist Manifesto: How to Get Things Right》（英国 Profile Books，2010；美国版由 Metropolitan Books 2009 年出版）的中英对照译本，从英文原文直接翻译。中文书名沿用简体中文版的译名《清单革命》。

## 来源与许可

- 原书版权归 Atul Gawande 所有。这份译文没有获得授权，发布与否由用户决定。
- 英文原文来自用户提供的 EPUB（英国 Profile Books 版）。导入和整理的过程见 [review/source.md](review/source.md)，电子书文件本身不放进仓库。

## 内容

献辞、引言、第 1 到 9 章、致谢、作者简介，共 13 节、666 个块。书末 Notes on Sources 的 82 条注释改成了各章的脚注，放在注释引用的词句后面；引言的星号注释在 EPUB 里缺了文字，按美国版补回。全书共 83 条脚注。

英文原文已经整理完毕，还没有开始翻译。下一步是术语统计和术语表，然后译样章。

## 原文怎样整理

EPUB 先由 `tools/prepare_epub.py` 标出标题、引文和章内分节，导入后由 `tools/curate_source.py` 删掉不需要翻译的页面、安放注释、修正转换造成的空格错误，最后由 `tools/check_source.py` 逐节和 EPUB 核对词数、段落、斜体和注释。过程和结果见 [review/source.md](review/source.md)。

## 翻译进度

在仓库根目录运行：

```bash
python3 scripts/site.py status checklist-manifesto
```

## 目录

```text
book.json          书的信息和章节列表，每章的状态：todo（只有英文）、draft、review、done（发布）
en/                英文原文，每章一个 Markdown 文件
zh-cn/             中文译文，与 en/ 同名同结构，逐块对应
glossary.md        术语表
review/            审校记录：source.md 记原文核对，每章一份 <章节 id>.md 记四项审校
tools/             整理和核对英文原文的脚本
assets/            封面（images/cover.jpg）、字体、章首章末图的数据
```

翻译和审校的流程见 [framework/README.md](../../framework/README.md)。
