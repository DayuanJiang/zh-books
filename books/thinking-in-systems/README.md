# 系统之美

德内拉·梅多斯（Donella H. Meadows）《Thinking in Systems: A Primer》（Chelsea Green Publishing，2008，Diana Wright 编辑）的中英对照译本，从英文原文直接翻译。书名沿用中文版《系统之美》。

## 来源与许可

- 原书版权归 Sustainability Institute 所有（版权页：Copyright © 2008 by Sustainability Institute）。这份译文没有获得授权，发布与否由用户决定。
- 英文原文来自用户提供的 EPUB（Chelsea Green 2008 年版，电子书 ISBN 978-1-60358-148-6）。导入和整理的过程、逐节的核对结果见 [review/source.md](review/source.md)，电子书文件本身不放进仓库。

## 内容

献辞、作者说明、编者说明、全书题词、引言、三个部分页、第 1 到 7 章、附录、参考书目、编者致谢、作者简介，共 19 节，1115 个待译块。原书 67 条书末注释和第 1 章的 1 条星号注释改成了各节的脚注（共 68 条），放在原来的注释号处。49 幅编号图和图题都保留，图片只放在英文一侧。

附录包括术语表、系统原理汇总、八个系统陷阱与对策、干预系统的 12 个位置、15 条生活准则和模型方程。

全书各节都已译完，依次经过翻译、双语审校、编辑通读，再由 GPT-6 Astra 独立审校第三轮；各章正文后附“本章小结与要点”。所有章节的状态都是 `review`，等用户认可后改为 `done` 才会在网站上发布。各节的审校记录在 `review/<章节 id>.md`。

## 翻译进度

在仓库根目录运行：

```bash
python3 scripts/site.py status thinking-in-systems
```

## 目录

```text
book.json          书的信息和章节列表，每章的状态：todo（只有英文）、draft、review、done（发布）
en/                英文原文，每节一个 Markdown 文件，图片在 en/images/；书末注释已改成各节的脚注
zh-cn/             中文译文，与 en/ 同名同结构，逐块对应
glossary.md        术语表：体例、各节标题、核心概念、机构和地名的译法
review/            审校记录：source.md 记原文核对，terms/ 是翻译前的术语统计，每章一份 <章节 id>.md 记四项审校
assets/            封面
tools/             整理 EPUB（prepare_epub.py、curate_source.py）、逐节核对原文（check_source.py）、术语统计（term_stats.py）和译完后的术语一致性检查（term_consistency.py）的脚本
```

翻译和审校的流程见 [framework/README.md](../../framework/README.md)。
