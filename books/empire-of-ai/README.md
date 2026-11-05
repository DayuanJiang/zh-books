# AI 帝国

郝珂灵（Karen Hao）《Empire of AI: Dreams and Nightmares in Sam Altman's OpenAI》（Penguin Press，2025）的中英对照译本，从英文原文直接翻译。

## 来源与许可

- 原书版权归 Karen Hao 所有。这份译文没有获得授权，发布与否由用户决定。
- 英文原文来自用户提供的 EPUB（美国 Penguin Press 版）。导入和整理的过程见 [review/source.md](review/source.md)，电子书文件本身不放进仓库。

## 内容

献辞、题词、作者说明、序章、第 1 到 18 章、尾声、致谢、作者简介，共 25 节、1681 个块，中英逐块对应。原书的 798 条书末注释和 2 条星号注释改成了各章的脚注（共 800 条），放在注释引用的词句后面。序章、各章和尾声的正文之后有“本章小结与要点”（译者整理）。

## 怎样译的

1. **原文**：EPUB 先由 `tools/prepare_epub.py` 保留斜体和注释位置，导入后由 `tools/curate_source.py` 整理结构，逐节和 EPUB 核对词数，见 [review/source.md](review/source.md)。
2. **术语**：翻译前先做术语统计（候选词、纸质版索引、人名、定义句、标题），数据和方法在 [review/terms/](review/terms/)。[术语表](glossary.md) 有 87 条概念、各节标题和体例；280 个人名的译法在 `review/terms/people-zh.tsv`。状态都是“初定”，等用户确认。
3. **样章**：主会话翻译序章，作为全书的风格依据。
4. **其余各节**：每节依次经过三个独立的 agent：翻译并自检；双语审校，只报告问题；编辑核实审校意见并修改，再通读中文。双语审校一共提出 447 条意见，采纳 444 条；中文通读又改了 154 处。各章译完后，编辑提出的各章写法不一的地方统一定下来，写在术语表的“全书统一的写法”一节。
5. **第三轮**：GPT-6 Astra 通过 Codex 独立审校全部 25 节，提出 156 条意见，逐条核实后采纳 143 条；同一轮按“全书统一的写法”统一各节。
6. **一致性检查**：`tools/term_consistency.py` 逐块检查 38 个术语和全部人名的译法，共 4810 处，剩下的提示都是同姓不同人这类误报。
7. **每章小结与要点**：20 节，一个 agent 起草，另一个对照英文核实，核实改了 171 处，记录在 [review/recaps.md](review/recaps.md)。
8. **阅读器校样**：主会话在阅读器里打开全部 25 节，检查报错、注释、待译段落、破折号、小结卡片和手机版式。

每节的四项审校和第三轮审校记录在 `review/<章节 id>.md`。这些审校都由模型完成，没有经过专业人工审校。所有章节的状态都是 `review`，等用户认可后改为 `done` 才会在网站上发布。

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
tools/             导入 EPUB、术语统计和一致性检查的脚本
recaps/            每章的小结与要点
```

翻译和审校的流程见 [framework/README.md](../../framework/README.md)。
