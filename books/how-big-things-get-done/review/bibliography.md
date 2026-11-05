# 参考文献（bibliography）审校记录

全节 2 个块：标题和一个 580 项的书目列表，没有注释，中英逐块对应（`site.py status` 显示 2/2）。这一节在 2026-11-05 从用户提供的 EPUB 补入，来源和对照方法见 [source.md](source.md) 的“用更好的来源补全（2026-11-05）”。

## 1. 译者自检

- 执行者：Claude（Opus 5.5），补入这一节的 agent。
- 范围：标题和列表的全部 580 项，对照 EPUB 的 Bibliography 一节（`bib.xhtml`）。
- 处理：
  - 标题 Bibliography 译“参考文献”，写进术语表的“各节标题”，“体例”里也加了一条。
  - 书目照全书注释里出处的体例，全部照录英文：作者、年份、篇名、书名或刊名（斜体）、出版地和出版社、卷期、页码和网址都不翻译，人名照写英文。中文文件里的列表和英文逐字相同，做法和附录 B 的书目一样。
  - EPUB 里每条书目是一个段落，没有按字母分组的小标题。这里写成一个列表，和附录 B 的书目一致，次序照 EPUB。
  - EPUB 里的 52 个网址是链接，照注释的做法写成网址的纯文字。只有两处链接地址和显示的文字不同（链接是 http://Phys.org，文字是 Phys.org），照显示的文字写。
- 发现并修改：EPUB 原文有两处缺空格，补上了，和正文 23 处错字的修正是同一类：
  - 第 6 项：“*Harvard Business Review*17 (1)”改为“*Harvard Business Review* 17 (1)”。
  - 第 231 项：“Genus,Audley.1997.“Managing”改为“Genus, Audley. 1997. “Managing”。
- 检查：
  - `diff en/18-bibliography.md zh-cn/18-bibliography.md` 只有标题一行不同。
  - `tools/compare_epub.py` 对这一节只报告上面两处补的空格。
  - 用词频表（wordfreq）查了不成词、拆开后是两个常见词的写法，查出来的都是人名、网址片段或者正常的合成词，没有要改的。
  - `python3 scripts/site.py check how-big-things-get-done` 通过；书目里的 ç、ê、û、ć 原来不在字体子集里，重新生成了子集。
  - 在 `/tmp` 下用 `build.py --drafts` 构建，在无头浏览器里打开这一节：标题和列表正常显示，斜体的书名和刊名、长网址都没有问题，没有脚本错误。
- 未决：无。双语审校、中文通读和阅读器校样（第 2 到 4 项）还没有做；这一节要译的只有标题。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 578 项 | Young, H. Kwak, John Waleski, Dana Sleeper, and Hessam Sadatsafavi. 2014. | 第一作者是 Young Hoon Kwak，引言的注释写作 “Young Hoon Kwak et al.”；书目把名 Young 当成了姓，所以排在 Y 下面。照原文保留 |
| 第 6 项 | *Harvard Business Review*17 (1): 97–108（1993 年） | 除了缺空格，卷号也可疑：1993 年的《哈佛商业评论》是第 71 卷。第 8 章注释 8 引的是同一篇文章，写作 *Harvard Business Review* 71, no. 1 (January–February 1993)。卷号照原文保留 |
| 第 42 项 | Bak, Per, Chao Tang, and Kurt Wiesenfeld. 1988. “Self-Organized Criticality: An Explanation of the 1/f Noise.” *Physical Review Letters* 59 (4): 381. | 这篇文章刊在《物理评论快报》1987 年 7 月 27 日出版的第 59 卷第 4 期，年份应为 1987。下一项同一组作者在 *Physical Review A* 发表的文章确是 1988 年。年份照原文保留（双语审校补记） |
| 第 104、105 项 | Carreyrou, John. 2018. / Caro, Robert. 1975. | Carreyrou 排在 Caro 前面，不合字母顺序，EPUB 也是这样。次序照原文保留（双语审校补记） |

## 2. 双语审校（补全部分）

- 执行者：agent（Opus 5.5），独立的审校者兼编辑，没有参与补入这一节。日期 2026-11-05。
- 范围：本节的 2 个块，也就是标题和 580 项的书目列表。审校者另写了一个小脚本，把 EPUB 的 `bib.xhtml` 逐项转成文字，斜体单独标出，再和 en、zh-cn 的列表逐项比较；又用 `framework/tools/build.py --drafts` 构建到任务的临时目录，把阅读器数据里这一节渲染出来的 580 个列表项和 EPUB 逐项比较。另外核对了标题的译名、书目里的数字和人名、Markdown 的显示和本节的体例。
- 核对结果：
  - 标题 Bibliography 译“参考文献”，和术语表“各节标题”一致，EPUB 目录里这一节也叫 Bibliography。
  - zh-cn 的列表和 en 逐字相同，和附录 B 的书目、各章注释里的出处做法一致。书目里 Translated by、Originally published in、correction printed in、Under review、Undated 这类著录用语，各章注释里也照写英文（例如第 2 章注释 33 的 originally published in），这里同样照写。
  - 580 项的条数和次序都和 EPUB 相同。渲染出来的文字和 EPUB 相比，不同的只有译者自检里写的两处补空格（第 6 项和第 231 项）。斜体共 563 处，和 EPUB 的 `<i>` 标记一样多；渲染后没有残留的星号，网址里的下划线也没有被当成斜体。
  - 有三处空格的位置和 EPUB 不同，译者自检里没有写：第 253 项（*Simple Heuristics That Make Us Smart,* eds.）、第 544 项（*Aviation Pros.*）、第 577 项（*World Nuclear News,* December 22）。EPUB 把斜体后面的空格放在斜体标记里面，Markdown 的斜体不能以空格结尾，所以空格挪到了星号外面。显示出来的文字相同，不用改。
  - 中文部分只有标题，没有破折号，也没有体例禁用的对比句式。书目里页码之间的连接号（例如 97–108）属于英文原样，照写。
- 发现：4 条，都是记录上的补充，正文和列表不用改。
  1. 第 42 项 Bak、Tang、Wiesenfeld 的 “Self-Organized Criticality: An Explanation of the 1/f Noise” 写作 1988 年。这篇文章刊在《物理评论快报》1987 年 7 月 27 日出版的第 59 卷第 4 期（查了美国物理学会的原文页面），年份应为 1987。照原文保留，补进上面的原文疑点表。
  2. 第 104、105 项 Carreyrou 排在 Caro 前面，不合字母顺序，EPUB 也是这样。照原文保留，补进原文疑点表。
  3. 第 6 项卷号 17 应为 71，书里还有一条内证：第 8 章注释 8 引的是同一篇文章，写作 *Harvard Business Review* 71, no. 1 (January–February 1993)。补进原文疑点表的同一行。
  4. 字体：书目里的 ć 已经写进 `assets/fonts/charset.txt`，但 Noto Serif SC 本身没有这个字形，生成的子集里也就没有（用 fontTools 查过两个 woff2 文件的字符表；第 1 章注释 8 的 ₐ、ₑ 也是这样）。阅读器会改用系统里带这个字形的字体显示，这是框架对缺字的正常处理，不用改文件。
- 修改：原文疑点表补了第 42 项、第 104 和 105 项两行，第 6 项一行补了第 8 章注释 8 的内证。en 和 zh-cn 的文件没有改动。
- 检查：`python3 scripts/site.py status how-big-things-get-done` 显示 17 节、888/888 个块、269 条脚注全部译出，本节 2/2；`python3 scripts/site.py check how-big-things-get-done` 草稿构建通过，没有警告。
- 未决：无。中文通读和阅读器校样（第 3、4 项）还没有做。
