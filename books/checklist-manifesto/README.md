# 清单革命

阿图·葛文德（Atul Gawande）《The Checklist Manifesto: How to Get Things Right》（英国 Profile Books，2010；美国版由 Metropolitan Books 2009 年出版）的中英对照译本，从英文原文直接翻译。中文书名沿用简体中文版的译名《清单革命》。

## 来源与许可

- 原书版权归 Atul Gawande 所有。这份译文没有获得授权，发布与否由用户决定。
- 英文原文来自用户提供的 EPUB（英国 Profile Books 版）。2026 年 11 月又按用户提供的美国 Picador 平装版 MOBI 补上附录，改正了转换错误和两处史实。导入、整理和补全的过程见 [review/source.md](review/source.md)，电子书文件本身不放进仓库。

## 内容

献辞、引言、第 1 到 9 章、附录、致谢、作者简介，共 14 节、665 个块。附录是美国版的四张清单示例图，图里的文字译在译者注里。书末 Notes on Sources 的 82 条注释改成了各章的脚注，放在注释引用的词句后面；引言的星号注释在英国 EPUB 里缺了文字，按美国版补回。全书共 83 条脚注。

全书已经译完，各节的状态都是 review。

## 原文怎样整理

EPUB 先由 `tools/prepare_epub.py` 标出标题、引文和章内分节，导入后由 `tools/curate_source.py` 删掉不需要翻译的页面、安放注释、修正转换造成的空格错误，再由 `tools/check_source.py` 逐节和 EPUB 核对词数、段落、斜体和注释。之后 `tools/compare_us_edition.py` 拿美国版逐块比较，`tools/apply_us_edition.py` 按比较结果改正 `en/`、写出附录。过程和结果见 [review/source.md](review/source.md)。

## 翻译进度

全书各节都已译完，依次经过翻译、双语审校、编辑通读，再由 GPT-6 Astra 独立审校第三轮；各章正文后附“本章小结与要点”。2026 年 11 月 5 日用户确认后，所有章节都改为 `done`，在书架网站上发布。各节的审校记录在 `review/<章节 id>.md`。

查看各节进度，在仓库根目录运行：

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
