# 怎样做成大事

傅以斌（Bent Flyvbjerg）、丹·加德纳（Dan Gardner）《How Big Things Get Done: The Surprising Factors Behind Every Successful Project, from Home Renovations to Space Exploration》（Macmillan，2023）的中英对照译本，从英文原文直接翻译。书名沿用已出版的中文版《怎样做成大事》（浙江科学技术出版社，2024）。

## 来源与许可

- 原书版权归 Connaught Street Inc. 和 Bent Flyvbjerg 所有。这份译文没有获得授权，发布与否由用户决定。
- 英文原文来自用户提供的 PDF（英国 Macmillan 2023 年电子版，ISBN 978-1-0350-1896-3，由 calibre 从电子书转成）。导入和整理的过程见 [review/source.md](review/source.md)，PDF 文件本身不放进仓库。

## 内容

献辞、引言、第 1 到 9 章、结语（十一条启发式）、附录 A（各类项目成本超支的基准比率）、附录 B（作者的延伸阅读书目）、致谢、作者简介，共 16 节、886 个块。原书的 267 条书末注释和附录 A 的 2 条星号注改成了各节的脚注（共 269 条），放在注释编号原来的位置。书名页、目录、参考文献、纸质版索引和版权页没有收入。

## 原文的整理

框架只能导入 EPUB，这本书的原文是 PDF，所以用本书自己的脚本处理：

1. `tools/import_pdf.py` 按字体和位置读出标题、段落、斜体、注释、表格和图片，输出和 EPUB 导入器相同的格式。
2. `tools/curate_source.py` 删去不需要翻译的节，定下各节的 id 和标题，修正电子书转换造成的 23 处错字（丢失或多余的连字符、缺少的空格和标点）。
3. `tools/verify_against_pdf.py` 逐节逐词对照 PDF，核对结果和每一处差异的原因写在 [review/source.md](review/source.md)。

第 1 章已译成样章，状态是 `draft`，等用户确认文风后再译其他各节；其余各节的状态都是 `todo`。样章的译者自检记录在 [review/ch01.md](review/ch01.md)。

## 术语

翻译前先做了术语统计：spaCy 候选词、纸质版索引的词条和人名、定义句和小节标题，数据和做法见 [review/terms/README.md](review/terms/README.md)。据此定下的译法写在 [glossary.md](glossary.md)，人名的译法在 [review/terms/people-zh.tsv](review/terms/people-zh.tsv)。样章选第 1 章。

## 翻译进度

在仓库根目录运行：

```bash
python3 scripts/site.py status how-big-things-get-done
```

## 目录

```text
book.json          书的信息和章节列表，每章的状态：todo（只有英文）、draft、review、done（发布）
en/                英文原文，每章一个 Markdown 文件，图片在 en/images/
zh-cn/             中文译文，与 en/ 同名同结构，逐块对应
glossary.md        术语表
review/            审校记录：source.md 记原文核对，terms/ 是术语统计，每章一份 <章节 id>.md 记四项审校
assets/            封面
tools/             导入 PDF、整理原文、对照 PDF 核对、术语统计（term_stats.py）和译后术语一致性检查（term_consistency.py）的脚本
```

翻译和审校的流程见 [framework/README.md](../../framework/README.md)。
