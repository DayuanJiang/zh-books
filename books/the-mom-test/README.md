# 妈妈测试

罗布·菲茨帕特里克（Rob Fitzpatrick）《The Mom Test: how to talk to customers and learn if your business is a good idea when everybody is lying to you》（作者自行出版，v1.04，2013 年 8 月）的中英对照译本，从英文原文直接翻译。现在英文原文已经导入并核对完，术语统计和术语表已经初定。第 1 章已经译成样章（状态 draft，自检记录见 [review/ch01.md](review/ch01.md)），等用户认可译文风格后再译其他章节。

## 来源与许可

- 原书版权归 Rob Fitzpatrick 所有。这份译文没有获得授权，发布与否由用户决定。
- 英文原文来自用户提供的 EPUB（作者自己出版的 v1.04 版）。导入和整理的过程见 [review/source.md](review/source.md)，电子书文件本身不放进仓库。

## 内容

引言、第 1 到 8 章、结语（含速查表和作者的结束语）、致谢，共 11 节、873 个块。书里有大量示例对话、经验法则和清单，`en/` 保留了这些结构：对话每句一段，说话人加粗，作者的旁白用斜体。原书没有注释和插图，EPUB 里也没有封面图。

## 翻译进度

全书各节都已译完，依次经过翻译、双语审校、编辑通读，再由 GPT-6 Astra 独立审校第三轮；各章正文后附“本章小结与要点”。2026 年 11 月 5 日用户确认后，所有章节都改为 `done`，在书架网站上发布。各节的审校记录在 `review/<章节 id>.md`。

查看各节进度，在仓库根目录运行：

```bash
python3 scripts/site.py status the-mom-test
```

## 目录

```text
book.json          书的信息和章节列表，每章的状态：todo（只有英文）、draft、review、done（发布）
en/                英文原文，每节一个 Markdown 文件
zh-cn/             中文译文，与 en/ 同名同结构，逐块对应
glossary.md        术语表（体例、章节标题、核心概念、机构与地名）
review/            审校记录：source.md 记原文核对，每章一份 <章节 id>.md 记四项审校；terms/ 是翻译前的术语统计
assets/            字体、章首章末图的数据（diagrams/）
tools/             整理 EPUB、导入后修改和核对原文的脚本，术语统计（term_stats.py）和译后术语一致性检查（term_consistency.py）
```

翻译和审校的流程见 [framework/README.md](../../framework/README.md)。
