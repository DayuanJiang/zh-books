# 随机漫步的傻瓜

纳西姆·尼古拉斯·塔勒布（Nassim Nicholas Taleb）《Fooled by Randomness: The Hidden Role of Chance in Life and in the Markets》（Random House，第二版）的中英对照译本，从英文原文直接翻译。中文书名沿用中信出版社中译本的书名《随机漫步的傻瓜》。

## 来源与许可

- 原书版权归 Nassim Nicholas Taleb 所有。这份译文没有获得授权，发布与否由用户决定。
- 英文原文来自用户提供的 EPUB（Random House 电子书，eISBN 978-1-58836-767-9，正文是 2004 年的第二版）。导入和整理的过程见 [review/source.md](review/source.md)，电子书文件本身不放进仓库。
- 这个 EPUB 缺了原书的 5 张表和 3 张图，只留下图表的标题，详见 [review/source.md](review/source.md)。

## 内容

序言、章节概要、序章、三个部分的开头页、第 1 到 14 章、尾声、后记、献辞、两版致谢、书末注释、参考文献、作者简介，共 28 节、1294 个块。第 7 章的两条星号注释改成了脚注；作者为第二版写的书末注释没有对应到正文的位置，保留为单独的一节；239 条参考文献保留英文。

全书各节都已译完，依次经过翻译、双语审校、编辑通读，再由 GPT-6 Astra 独立审校第三轮；各章正文后附“本章小结与要点”。所有章节的状态都是 `review`，等用户认可后改为 `done` 才会在网站上发布。各节的审校记录在 `review/<章节 id>.md`。翻译前的术语统计已经做完，数据和说明在 [review/terms/](review/terms/README.md)，术语表见 [glossary.md](glossary.md)；样章定为第 1 章。

## 翻译进度

在仓库根目录运行：

```bash
python3 scripts/site.py status fooled-by-randomness
```

## 目录

```text
book.json          书的信息和章节列表，每章的状态：todo（只有英文）、draft、review、done（发布）
en/                英文原文，每节一个 Markdown 文件
zh-cn/             中文译文，与 en/ 同名同结构，逐块对应
glossary.md        术语表
review/            审校记录：source.md 记原文核对，每章一份 <章节 id>.md 记四项审校
review/terms/      翻译前的术语统计：候选词、定义句、斜体短语、人名表和术语表的依据
assets/            封面
tools/             整理 EPUB、核对原文、术语统计和译后术语一致性检查的脚本
```

翻译和审校的流程见 [framework/README.md](../../framework/README.md)。
