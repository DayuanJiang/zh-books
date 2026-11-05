# 关于作者（about-the-author）审校记录

全节 2 个块，原文没有注释，中文没有加译者注；中英逐块对应（`site.py status` 显示 2/2）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 2 块（一级标题和一段简介），对照原文检查漏译、数字、人名、术语和格式。另外运行了 `python3 scripts/site.py status fooled-by-randomness`（2/2）；在 `/tmp` 的一份副本里把本节设成草稿后构建通过；`tools/term_consistency.py` 对本节没有提示。
- 发现并修改：没有需要改的地方。
- 译法上的选择：
  - 标题照术语表写“关于作者”。
  - “spent twenty-one years as a risk taker” 写“当了 21 年的冒险者”，risk taker 照术语表写“冒险者”，21 按 11 以上的确数用阿拉伯数字。
  - “a researcher in philosophical, mathematical, and mostly (very) practical problems with probability” 写“研究概率带来的哲学问题、数学问题，而主要是（非常）实际的问题”，保留括号里的“非常”。
- 人名：纳西姆·尼古拉斯·塔勒布（Nassim Nicholas Taleb），照 people-zh.tsv。
- 未决：
  - 双语审校、中文通读和阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 2 块（一级标题和一段简介），对照英文检查了数字、人名和术语。
- 发现：0 条；核实后采纳 0 条，不采纳 0 条。审校者对本节没有提出问题，确认 21 年的数字正确。
- 审校者的总体判断：十个分节逐块对照英文读完，总体质量很高，可以进入中文通读。人名和 people-zh.tsv 一致，术语用的都是术语表的译法，中英逐块对应。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：读了标题和简介，改动回查了英文。
- 发现并修改：
  - “a researcher in philosophical, mathematical, and mostly (very) practical problems with probability”：原译“研究概率带来的哲学问题、数学问题，而主要是（非常）实际的问题”，“带来的”把概率说成了这些问题的来源，原文的 problems with probability 指和概率有关的问题；“而主要是”接得也不顺。改为“研究概率方面的哲学问题、数学问题，其中主要是（非常）实际的问题”，括号里的“非常”保留。
- 核对过的地方：risk taker 照术语表写“冒险者”，21 年用阿拉伯数字；`site.py status` 仍显示 2/2。

## 状态

- 没有未解决的意义问题。
- 阅读器校样还没有做；`book.json` 里本节的状态由主会话修改。
