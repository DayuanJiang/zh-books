# 附录 B 傅以斌著作延伸阅读（appendix-b）审校记录

全节 3 个块，没有注释，中英逐块对应（`site.py status` 显示 3/3）。3 个块是标题、说明段落和书目列表；书目列表有 37 项，中英两边项数相同。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：标题、说明段落和书目列表的全部 37 项，对照英文检查漏译、增译、书目是否原样保留，以及三处说明句的意思。用 `diff` 核对过：去掉三处说明句后，中文文件的 37 项书目和英文逐字相同。
- 处理：
  - 标题照术语表写“附录 B 傅以斌著作延伸阅读”。
  - 说明段落译成中文。Social Science Research Network (SSRN) 写“社会科学研究网络（SSRN）”，Google Scholar 写“谷歌学术（Google Scholar）”；ResearchGate、Academia、arXiv 是网站名，照写原名。
  - 书目照体例按出处处理：作者、篇名、刊名、卷期、日期、页码和网址都保留英文原样，人名照写英文。第 1 项的 under review 是出处的一部分，照写英文，和第 6 章注释 9 的处理一致。
  - 三处附在书目后面的说明句译成中文，句中的刊名照注释的做法保留英文斜体：
    - 第 19 项 “This article was awarded the *PMI Project Management Journal* 2015 Paper of the Year Award.” 译“这篇文章获得了 *PMI Project Management Journal* 2015 年度最佳论文奖。”
    - 第 23 项 “This article was selected by *Harvard Business Review* as the leading article for its “Ideas Watch” section, featuring the most important new ideas in business and management.” 译“这篇文章被 *Harvard Business Review* 选为“Ideas Watch”栏目的头条文章，这个栏目介绍商业和管理领域最重要的新思想。”栏目名照写英文。
    - 第 27 项 “This article was awarded the Association of European Schools of Planning (AESOP) Prize for Best Published Paper, July 2008.” 译“这篇文章于 2008 年 7 月获得欧洲规划院校协会（AESOP）最佳发表论文奖。”
- 发现并修改：
  - 初稿里三处说明句紧贴在网址末尾的英文句点后面（例如 “abstract_id=2424835.这篇文章”），网址和中文连在一起，阅读器或读者容易把汉字当成网址的一部分。在句点后加了一个空格。
- 检查：`python3 scripts/site.py status how-big-things-get-done` 显示 appendix-b 为 3/3；在 `/tmp` 下的副本里把本节设成草稿，用 `framework/tools/build.py --drafts` 构建通过。中文说明段落和三处说明句里没有破折号，也没有体例禁用的对比句式；书目里的连接号都在照写的英文出处里。`tools/term_consistency.py` 对这一块报了 32 处术语和人名“没有用约定的译法”，全部来自照写英文的书目，属于误判。
- 未决：
  - 第 19 项的 Paper of the Year Award 译“年度最佳论文奖”，“最佳”是按中文的习惯说法补的；也可以直译“年度论文奖”。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 6 项 | *Harvard Business Review* 99, no.6 | no. 后面少一个空格，其他各项都写 no. 加空格。书目照原文保留 |
| 第 27 项 | *Environment and Planning B: Planning and Design* 34, no. 4 (2007), 578–97 | 卷期后面用逗号接页码，其他各项都用冒号。书目照原文保留 |
| 第 23 项 | *Harvard Business Review* 89, no. 9 (2011): 23–25 | 第 1 章注释 9 引同一篇文章写 (September 2011)，这里只有年份。书目照原文保留 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：标题、说明段落和 37 项书目，对照英文核对意义、书目是否原样保留和三处说明句。审校者用 `diff` 比对过：除三处说明句以外，中文的 37 项书目和英文逐字相同；说明句译成了中文，句中刊名照全书注释的做法保留英文斜体。审校者没有改文件。
- 发现：0 条；核实后采纳 0 条，不采纳 0 条。
- 审校者的总体判断：没有发现意义错误、漏译、增译或否定用反的地方，原文疑点没有需要补记的；`site.py status` 显示 3/3。五节整体译文忠实、准确。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：只看中文读完标题、说明段落和三处说明句，书目照写英文，没有作为中文通读的对象。读后回查了英文。
- 发现并修改：没有修改。说明段落三句顺序清楚：先说清单的用途，再说去哪里免费下载，最后说哪些文章附了 SSRN 链接。三处说明句都以“这篇文章”开头，指的是紧挨着的那一项，读者不会弄错。
- 检查：`python3 scripts/site.py status how-big-things-get-done` 显示 appendix-b 为 3/3；中文说明段落和说明句里没有破折号，也没有体例禁用的对比句式。

## 状态

- 没有未解决的意义问题。原文疑点仍是上面表格里的三条，审校者认为不需要补记。
- 译者自检的未决项（Paper of the Year Award 译“年度最佳论文奖”还是“年度论文奖”）仍留给主会话，审校者没有提出改动。
- 还没做的：第 4 项阅读器校样。
