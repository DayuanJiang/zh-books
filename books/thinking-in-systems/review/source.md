# 原文核对

## 来源

- 文件：用户提供的 EPUB（`Meadows - Thinking in Systems.epub`），SHA-256 记在 `book.json` 的 `source` 里。EPUB 本身不放进仓库。
- 版本：书名页和版权页都是美国 Chelsea Green Publishing 2008 年版《Thinking in Systems: A Primer》，Donella H. Meadows 著，Diana Wright 编辑，电子书 ISBN 978-1-60358-148-6。版权页写“First printing, December, 2008”，印次行最小的数字是 2，按惯例表示依据第二次印刷制作。EPUB 元数据的出版日期是 2008-12-20。
- 这个 EPUB 是从纸质版版式转出来的：章节标题、小标题、项目列表、页边摘要、灰色方框和引文都只是带 CSS 类的普通段落，没有标题、列表或引文标记。文字里有转换留下的错误（见下面的表格），没有大段乱码。
- 注释：67 条书末注释集中在一个注释文件里，按章分组，每章从 1 编号。正文里的注释号是上标链接，注释前面的编号链回正文。另有一条星号注释在第 1 章末尾（“Definitions of words in bold face can be found in the Glossary.”），正文第一个粗体词 system 后面的星号链到它。
- 图：正文 49 幅编号图（Figure 1 到 49），连同分图和附录的曲线图共 72 张图片。EPUB 里另有 10 张图片没有任何页面使用：7 张是所用图片的另一个版本（尺寸不同，或多一个、少一个图内标题），1 张是书名页上的出版社字样，2 张是出版社广告的整页图。附录“24 小时室外温度”曲线的两个版本里，EPUB 用的是没有图内标题的那张，这里照 EPUB 保留。

## 导入和整理

```bash
uv run --project framework/tools python -I books/thinking-in-systems/tools/prepare_epub.py book.epub prepared.epub
python3 scripts/site.py import-epub thinking-in-systems prepared.epub --force
uv run --project framework/tools python -I books/thinking-in-systems/tools/curate_source.py book.epub
uv run --project framework/tools python -I books/thinking-in-systems/tools/check_source.py book.epub
```

`tools/prepare_epub.py` 先复制一份 EPUB，把每个页面改成导入工具认得的结构，并改掉转换错误。改动都按段落的 id 或一段确切的原文指定，找不到或找到不止一处就报错停下。

| 原样 | 处理 | 原因 |
| --- | --- | --- |
| 章节标题是 `— ONE —` 加一段标题，目录写 `One. The Basics` | 每节一个一级标题，编号章写成 `# 1. The Basics`，目录用同样的标题 | 导入工具据此给出 `ch01` 和章号 |
| 引言的章内标题写 `The System Lens`，目录写 `The Systems Lens` | 用目录的 `Introduction: The Systems Lens` | 纸质版目录和书里其他地方都写 Systems Lens |
| 小标题、方框标题、附录和参考书目的分组标题都是普通段落 | 按 CSS 类和段落 id 改成二级、三级标题；标题里“破折号加空格”的断行痕迹去掉空格 | 让章内目录可用 |
| 页边的原理摘要（粗体开头的一句话，附录汇总的就是这些）| 改成引文块，留在 EPUB 里的位置 | 和正文区分开 |
| 灰色方框（Think About This、A Note on Language、八个 The Trap / The Way Out 等）| 改成引文块，方框标题是块里的粗体段落 | 同上 |
| 五篇 Interlude 故事 | `### Interlude • 标题`，故事段落照旧，故事后面加一条分隔线（在章末的两篇不加）| 让读者看出故事在哪里结束 |
| 章首题词 | 照旧是普通段落，后面是署名段 | 阅读器把它显示成题词 |
| 小节开头的题词、正文中单独成段的长引文（报纸、Hardin、Kennedy 等 34 组）| 改成引文块，署名段留在块外 | 和正文区分开 |
| 引言里三组“系统原理加一句俗语” | 每组一个引文块 | 原书把每组当作一个整体排出 |
| 两首诗（Swift、Boulding）每行一个段落 | 每首合成一段，行尾硬换行 | 一首诗一个翻译块 |
| 用“•”开头的段落 | 改成项目列表；第 5 章三条写在普通段落里的“•”问题也改成列表 | 列表结构 |
| 第 2 章方框里的 1 到 3、第 4 章开头的 1 到 3、附录 15 条生活准则 | 有序列表 | 编号从 1 往上数 |
| 附录“干预系统的位置”从 12 倒数到 1 | 一段，每项一行（硬换行） | Markdown 的有序列表不能倒数；分成 12 段时最后一项会被阅读器当成小标题 |
| 附录的模型方程，每行一个段落，有的行被并到上一行，有的句子被拆成两行 | 每组方程一段，每行一个硬换行；补回 15 处丢失的换行（如 `× dt` 后面的 `Initial stock value`），接回 6 处从句子中间断开的行 | 保留原书一行一个等式的排法 |
| 小型大写字母，如 `R<small>OBERT</small>` | 改成正常大小写 Robert | 否则成为 ROBERT 或拆成两个词 |
| 斜体和粗体在每个排版行断开 | 相邻的同类标记合并 | 书名、术语保持一段完整的斜体 |
| 链到目录页、链到图、注释里链到本书第 2 章的链接 | 去掉链接，保留文字 | 在阅读器里没有目标 |
| 注释正文以“1. ”开头，编号是链接 | 去掉编号后的句点 | 导入工具只去掉编号，会留下“. Russell Ackoff” |
| 第 4 章注释 7 的回链指向注释 8 的位置 | 改成指向注释 7 | 否则导入工具找不到这条注释 |
| 第 1 章的星号 | 改成脚注引用 | 星号注释成为第 1 章的脚注 |

转换造成的文字错误，改正后列在这里：

| 位置 | EPUB 原样 | 改为 | 依据 |
| --- | --- | --- | --- |
| 第 1 章 Tinbergen 署名 | `Jan Tinbergen, quoted in ibid, 44.economist` | `economist` | 注释号后面混进了注释开头的文字 |
| 第 2 章 | 注释 3 后 `Jay W. Forrester,`，注释 5 后 `Jay W. Forrester, 1989.` | 删去 | 同上 |
| 第 3 章 Swift 署名 | `Jonathan Swift, 18th century poet` | `18th century poet` | 同上 |
| 第 3 章 | 注释 5 后 `Paraphrased from Herbert Simon,` | 删去 | 同上 |
| 第 5 章 Ipsen 署名 | 注释 7 后 `Erik Ipsen,` | 删去 | 同上 |
| 第 6 章 | 注释 3 后 `World Bank,`，注释 7 后 `Ralph Waldo Emerson,`，注释 8 后 `Clyde Haberman,` | 删去 | 同上；这三处混进的是别的注释的开头 |
| 第 4 章 Boulding 的诗 | 缺第五行 | 补上 `Perceiving input-output pairs,` | 这首诗在其他引用里都有这一行，缺了它前后句不连 |
| 第 1 章 | 一段被灰色方框截成两半（`the Federal Reserve` / `Bank has done…`）| 两半接回一段，方框放在段后 | 后半段以小写的接续句开头 |
| 第 5 章 | “转移负担”方框后面的两段（If you are the intervenor…）在方框外 | 移进方框 | 附录同一个 The Way Out 包括这两段 |
| 第 1、2、3、5、6、7 章 | `goal— also`、`balancing- loop`、`meta-meta- resilience`、`alcohol- driven`、`success-to- the-successful`、`second to- highest`、`figuring- out`、`under stand`、`penal ties` | 去掉断行留下的空格（`second-to-highest` 补回连字符） | 纸质版的行末断字；`second-to-highest` 依据作者网站上同一篇文章 |
| 第 2 章 | `population.Its`、`loop.Both` | 句点后补空格 | 缺空格 |
| 第 2 章页边摘要 | `flowlimited` | `flow-limited` | 附录同一句写 flow-limited，前一条写 stock-limited |
| 第 5 章 | `success-to the-successful`（3 处） | `success-to-the-successful` | 全书写法统一；同一词另一处只是多了空格 |
| 第 1 章方框 | `A ) Can you` | `A) Can you` | 多余空格 |
| 引言 | `“what-if ” questions` | `“what-if” questions` | 多余空格 |
| 第 4 章插曲 | `eventually to explode again` 段末没有句点 | 补句点 | 缺标点 |
| 第 4 章注释 8 | 书名斜体里包了一个左括号 | 括号移到斜体外 | 否则 Markdown 的斜体不生效 |

`tools/curate_source.py` 再处理导入结果：

- 删掉不需要翻译的分节：封面图、半书名页、作者其他著作、书名页、版权页、目录页、两页出版社广告，以及注释移走后只剩分组标题的注释页。EPUB 的封面图改作书架封面 `assets/images/cover.jpg`，没有分节使用的图片从 `en/images/` 删掉。
- 分节 id 改短：`authors-note`、`editors-note`、`introduction`、`part1` 到 `part3`、`bibliography`、`acknowledgments`。
- 脚注引用紧跟在所属的词后面，后面接文字时留一个空格（EPUB 里有的署名在注释号前多一个空格，有的注释号后缺空格）。
- 检查每节的脚注从 1 连续编号、每条定义一次也引用一次，全书 68 条；没有留下指向 EPUB 文件的链接。

## 保留的结构

献辞、作者说明（1993）、编者说明（2008）、全书题词（Pirsig）、引言、三个部分页、第 1 到 7 章、附录、参考书目、编者致谢、作者简介，共 19 节。

- 部分页只有一个标题（如 `Part One: System Structure and Behavior`）。原书的三个部分有标题，所以保留成只有标题的小节。
- 附录一节包括术语表、系统原理汇总、系统陷阱与对策、干预系统的 12 个位置、15 条生活准则和模型方程，各部分是二级标题。
- 参考书目有说明文字和条目注解，保留。

给译者的几点说明：

- 脚注每节从 1 编号。第 1 章多一条星号注释，按出现顺序是第 2 条，所以第 1 章的脚注 3 到 6 对应原书注释 2 到 5。其余各章的编号和原书一致。
- 图题段落以 `Figure N.` 开头；分图上方的 `A: Growth` 这类标签是普通段落，要译。
- 附录“干预系统的位置”和模型方程的段落里，每行行尾有两个空格（硬换行），中文要照样保留，行数相同。
- 模型方程里斜体的是模型变量名（如 *water in tub*）。

## 完整性核对

`tools/check_source.py` 逐节把 EPUB 文件和 `en/` 下对应的文件按词比较：EPUB 一侧不算章节标题段落、注释号和段首的“•”，`en/` 一侧不算一级标题、图片和脚注定义，然后列出每一处不同的词。注释另行比较：注释文件里每条注释的文字，和该节脚注定义的文字逐条比较。

| 分节 | EPUB 词数 | en/ 词数 | 差 | 差在哪里 |
| --- | ---: | ---: | ---: | --- |
| dedication | 12 | 12 | 0 | |
| authors-note | 399 | 399 | 0 | 署名的大小写 |
| editors-note | 987 | 987 | 0 | 署名的大小写 |
| epigraph | 71 | 71 | 0 | 署名的大小写 |
| introduction | 2460 | 2459 | −1 | `what-if ”` 的多余空格 |
| part1、part2、part3 | 0 | 0 | 0 | 只有标题 |
| ch01 | 7421 | 7411 | −10 | Tinbergen 署名 −5，`A )` −1，四处“破折号加空格” −4；接回的半段和方框换了位置，词数不变 |
| ch02 | 9591 | 9585 | −6 | 两处混入的 Forrester −7，`balancing- loop` −1，两处补空格 +2 |
| ch03 | 3755 | 3748 | −7 | Swift −2，Simon −4，`meta-meta- resilience` −1 |
| ch04 | 8499 | 8502 | +3 | 补回的诗行 +3 |
| ch05 | 11043 | 11032 | −11 | 三处标题里的空格 −3，Ipsen −2，四处 success-to-the-successful −4，`alcohol- driven` −1，`penal ties` −1 |
| ch06 | 7814 | 7806 | −8 | World Bank −2，Emerson −3，Haberman −2，`second to- highest` −2，注释号后补空格 +1 |
| ch07 | 7156 | 7154 | −2 | `under stand`、`figuring- out`、标题里的空格各 −1，注释号后补空格 +1 |
| appendix | 3874 | 3874 | 0 | 只改了分行 |
| bibliography | 497 | 497 | 0 | |
| acknowledgments | 245 | 245 | 0 | |
| about-the-author | 194 | 194 | 0 | |
| 合计 | 64018 | 63976 | −42 | |

除了表里列出的改动，两边的词序列完全相同，所以没有漏掉或重复的段落。注释 68 条（67 条书末注释和 1 条星号注释）全部成为所在节的脚注，各在一处：66 条与注释文件逐词相同；第 5 章注释 16 只差在网址写成了 Markdown 的 `<网址>` 自动链接；星号注释去掉了开头的星号。49 个图题都在，72 张图片在各节里的顺序和 EPUB 相同。`en/` 全部 19 节共 65490 个英文词，其中脚注 1423 个词。

## 原文疑点

下面这些是原文本身的问题，`en/` 照原样保留，翻译时按正确的意思处理，必要时加译者注：

| 位置 | 原文 | 说明 |
| --- | --- | --- |
| 引言 | `That discussion will lead to us to look at` | 多了一个 to |
| 第 2 章图 45 图题 | `creates a patterns of overshoot` | 多了 a 或 s |
| 第 3 章 | `It is likely come up with whole new structures` | 少了 to |
| 第 4 章插曲末段 | `…never been seen before.”` | 有右引号，没有对应的左引号，可能是引 Holling 的话 |
| 第 5 章 | `I think the investment tax credit…,” said Joseph W. Duncan` | 引文缺左引号 |
| 第 5 章 | `it’s an worth looking for` | 多了 an |
| 第 5 章 | `Rather than examine the farming the monocultures` | 少了一个词，可能是 farming of the monocultures |
| 第 6 章 | `a story a friend sent me over the Internet to makes that point` | makes 应为 make |
| 附录术语表 | `also know as` | 应为 also known as |
| 附录模型方程 | 恒温器模型写 `For Figures 14–20` | 恒温器的图是 15 到 20，图 14 是资本再投资 |
| 附录模型方程 | 不可再生资源模型写 `for Figures 30–40` | 这个模型的图是 37 到 41，大概指图 38 到 41：同一行后半句说图 40 另取 6%、8%、10%、12% 做四次对比运行，第 2 章正文又拿图 41 和价格不变的图 38 比较，可见图 41 的增长目标也是 10% |
| 参考书目 | `Stat University of New York Press` | 应为 State |

## 框架的问题

框架有三处在这本书上出了问题。前两处在 EPUB 导入工具里，已经在 `tools/prepare_epub.py` 里绕过；第三处在阅读器里，没有绕过。框架本身没有改。

1. 注释前的编号是链接、后面跟句点（“1. Russell Ackoff”）时，导入工具去掉编号链接，留下开头的“. ”。
2. 一条注释的回链指向别的注释号时，这条注释被静默丢掉，注释页也因为还剩这条注释而留下来。导入时只报告 66 条注释，没有警告。
3. 阅读器只把 `Figure 1-2`、`Figure 1.2` 这种编号的段落认作图题，这本书的 `Figure 1.` 图题不会得到图题样式。
