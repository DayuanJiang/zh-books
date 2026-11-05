# 原文核对

## 来源

- 文件：用户提供的 EPUB（`book.epub`，385 KB），SHA-256 记在 `book.json` 的 `source` 里。EPUB 本身不放进仓库。
- 版本：版权页写的是 Random House 出版的《Fooled by Randomness: The Hidden Role of Chance in Life and in the Markets》，Copyright © 2004，电子书 ISBN 978-1-58836-767-9，电子书版本号 v3.0_r8。原书 2004 年由 TEXERE 出精装本，2005 年由 Random House 出平装本。EPUB 元数据的书名是 “Fooled by Randomness (Incerto)”，日期是 2008 年 10 月 5 日，也就是这个电子书最初上架的日期。书末的作者书目列到了 2018 年的《Skin in the Game》，说明文件是 2018 年以后更新过的版本。正文是第二版（作者在序言里说，这一版增加了书末注释，各章都有新内容，第 11 章增加最多，全书扩充了三分之一以上）。
- 文件的来历：这个 EPUB 是用 Epubor eCore 从 Kindle 格式转出来的，元数据里的作者和出版者字段写着一个中文电子书网站（chenjin5.com），这个网站还在书里插了三页中文广告。正文本身没有被改动的迹象。
- 结构：书的内容是 34 个 HTML 文件，另有 3 个插入的广告页。没有任何标题标签，标题、引文和列表都是带 CSS 类的普通段落；目录在 `toc.ncx` 里。转换工具在每个行内标签（斜体、链接、首字下沉）后面加了一个换行和一个空格，所以逗号、句号前面会多出空格，首字下沉的字母和后面的字母被拆开（“T his”）。
- 图表缺失：原书的 5 张表和 3 张图在这个 EPUB 里都只剩一个空的方框，没有图片文件。缺的是序章的表 P.1（混淆表，全书的核心区分）、第 3 章的表 3.1（不同时间尺度上的成功概率）、第 6 章的表 6.1、表 6.2 和图 6.1、第 11 章的表 11.1（交易员和科学研究对照）、图 11.1 和图 11.2。图表的标题都还在，正文也照常引用这些图表。EPUB 里只有两张图片：封面，和一张没有被引用的封面缩略图。

## 导入和整理

```bash
uv run --project framework/tools python -I books/fooled-by-randomness/tools/prepare_epub.py book.epub prepared.epub
python3 scripts/site.py import-epub fooled-by-randomness prepared.epub --force
uv run --project framework/tools python -I books/fooled-by-randomness/tools/curate_source.py book.epub
uv run --project framework/tools python -I books/fooled-by-randomness/tools/check_source.py book.epub
```

直接导入时，导入工具认不出这本书的标题，每一节只有一个一级标题，其余全是段落，链接文字后面的逗号前多了空格，两条星号注释也没有变成脚注。所以先由 `tools/prepare_epub.py` 复制一份 EPUB，把标记改成导入工具认识的样子：

| 问题 | 处理 |
| --- | --- |
| 行内标签后面多出的换行和空格 | 换行一律当作空格；标点和破折号前面的空格去掉 |
| 首字下沉的字母单独放在一个标签里 | 和后面的字母连起来。三处首字本身就是一个词（第 2 章 “I start”、第 5 章 “I used”、尾声 “A couple”），保留空格 |
| 章节标题是三个段落：章号（“One”）、装饰符号 “•”、全大写的标题 | 合成一个一级标题，编号章节写成 “# 1. If You’re So Rich, Why Aren’t You So Smart?”，大写标题改成标题式大小写；装饰符号删除 |
| 序言、序章、三个部分、尾声、后记、书末注释的标题都分成主标题和副标题 | 合成一个一级标题，例如 “Preface: Taking Knowledge Less Seriously”、“Part I: Solon’s Warning”。三个部分的副标题（例如 “Skewness, Asymmetry, Induction”）保留为斜体段落 |
| 小节标题是两种段落：全大写的一级小节和斜体的二级小节 | 按目录链接的锚点层级改成二级和三级标题（`c01.1` 是二级，`c01.1.1` 是三级）。第 7 章的 “From Bacon to Hume” 用的是三级的样式，目录里是二级，按目录处理。尾声只有一个小节，用二级标题 |
| “章节概要”里每章的标题是加粗的小型大写段落 | 改成二级标题 |
| 缩进的引文是两层 `div` 里的段落 | 改成引用块；每章开头的斜体内容提要也在这种缩进里，改成普通的斜体段落 |
| 第 3 章和第 7 章的编号段落（“1.  Over a short time increment…”） | 改成有序列表 |
| 第 5 章列举交易员通病的七段，开头的短语用无衬线粗体标出 | 改成粗体，七段放在一个引用块里，和原书的缩进一致 |
| 第 6 章的下标（W<sub>0</sub>、W<sub>1</sub>、W<sub>2</sub>） | 换成下标字符 W₀、W₁、W₂ |
| 图表留下的空方框和空段落 | 删除；图表标题保留为段落 |
| 指向书内其他文件的链接（“Chapter 11”“Table P.1” 等） | 保留文字，去掉链接。指向网站的链接保留 |
| 第 7 章的两条星号注释放在单独的 “Footnotes” 文件里，回链 “Return to text.” 在注释末尾，导入工具认不出来 | 把正文的星号链接标成注释引用，删去注释里的星号和回链，导入后成为第 7 章的脚注 `[^1]`、`[^2]`，位置就是星号原来的位置 |
| 目录里的条目名是 “Chapter One” 这类 | 改成新的一级标题，章节的 id 和文件名随之按标题生成 |

导入后由 `tools/curate_source.py` 处理：

| 问题 | 处理 |
| --- | --- |
| 版权页（导入工具把它叫作 “Title Page”，因为真正的书名页是空的，目录链接被转到了下一页）、中文网站插入的三页广告、出版社的作者书目、出版社的推荐书目广告、已经挪进第 7 章的 “Footnotes” 页 | 删除。EPUB 的封面图改作书架封面 |
| 章节 id 太长 | 改成 preface、summaries、prologue、part1 到 part3、ch01 到 ch14、epilogue、postscript、dedication、acknowledgments-first、acknowledgments-second、notes、references、about-the-author |
| 纸质版换行留下的连字符：aloof-ness、out-comes（两处）、non-sense、第 7 章脚注里的 empiri-cism 和 in-dependently | 连成一个词 |
| 转换造成的乱码字母：第 7 章脚注的 al-Ghazälï、参考文献的 al-Ghazl（长音符号变成了分音符，或者带长音符号的字母丢了） | 改成 al-Ghazālī |
| 第 12 章拉丁文 “po¨tuit” 中间多了一个分音符 | 改成 potuit |
| 漏掉的空格：右括号加句号后紧跟下一句（“reason).Then”）、右引号后紧跟下一个词（“losses,”he says”）、分号后紧跟下一个词、逗号后紧跟左引号，以及序言的 “Chapters13” | 补上空格，共 24 处，分布在序言、序章、第 1、2、3、5、6、9、11、13 章、第三部分、后记和书末注释里，每一处都打印在 `curate_source.py` 的输出里 |
| 第 10 章 “(like myself )” 多一个空格；书末注释里 “Les gommes:” 等三处粗斜体后多一个空格 | 去掉 |

参考文献里也有不少漏掉的空格（例如 “vol.2,69–74,London”），这一节按要求保留英文原样，只改了 al-Ghazālī 一处乱码。

## 保留的结构

共 28 节：序言、章节概要、序章、第一部分、第 1 到 7 章、第二部分、第 8 到 11 章、第三部分、第 12 到 14 章、尾声、后记、献辞、第一版致谢、第二版致谢、书末注释（“A Trip to the Library: Notes and Reading Recommendations”）、参考文献、作者简介。阅读顺序和 EPUB 一致，献辞在这个电子书里排在后记之后，照原样保留。三个部分的开头页都有几段正文，所以单独成节。阅读器第一次打开时进入序章（`start` 设为 prologue）。

- **书末注释**：作者在第二版加的注释按章分组，每条用一个粗体的主题词开头（例如 “Hindsight bias:”），正文里没有注释编号，也没有链接，主题词也不是正文里的原话，无法可靠地对应到正文的具体位置。所以保留为单独的一节，按原书分成 18 个二级标题（开头的说明、序言、序章、第 1 到 14 章、后记），共 154 个块。
- **参考文献**：239 条，保留为单独的一节，条目保留英文。
- **脚注**：只有第 7 章的两条星号注释，已经放回正文。

## 完整性核对

`tools/check_source.py` 把每一节的英文和它来自的 EPUB 文件逐词比较（转成小写，不计标点；词里的连字符、撇号和点算作词的一部分；首字下沉的字母和后面的字母算一个词；脚注定义和 “Footnotes” 文件比较）。比较的是整个词序列，所以段落的遗漏、重复和错位都会显示出来。结果：保留的 28 节对应的 EPUB 文件共 98,341 个词（含第 7 章的两条脚注），`en/` 共 98,342 个词，所有差异都在下表里，没有其他差异。

| 章节 | 差异 | 原因 |
| --- | --- | --- |
| 第 1 到 14 章 | 章号 “One” 到 “Fourteen” 换成 “1.” 到 “14.” | 编号章节的标题写法 |
| 第 1、4 章，第 7 章脚注 | 六处拆开的词连成一个（aloofness、outcomes 两处、nonsense、empiricism、independently） | 纸质版换行留下的连字符 |
| 第 7 章脚注、参考文献 | al-Ghazälï 和 al-Ghazl 改成 al-Ghazālī | 乱码字母 |
| 第 12 章 | “po” 和 “tuit” 合成 potuit，少 1 个词 | 多余的分音符把词拆开了 |
| 序言 | “Chapters13” 分成两个词，多 1 个词 | 漏掉的空格 |
| 献辞 | 多 1 个词 “Dedication” | 献辞页没有标题，导入工具按目录加了一级标题 |

其他核对：

- 第 7 章的两条脚注各出现一次，正文里各有一个引用；全书没有剩下的星号链接、指向 EPUB 内部文件的链接和 HTML 标签。
- 斜体：每节的斜体数和 EPUB 一致，只有小节标题原来的斜体去掉了（标题统一用普通字体），三个部分的副标题改成了斜体段落。粗体：第 5 章多了 7 处，是上面说的无衬线粗体短语；其余一致。
- 全书重复的段落只有一种：“章节概要”里 14 章的概要和各章开头的斜体内容提要逐字相同，原书就是这样。另外第 1 章和第 5 章各有一个小节叫 “John the High-Yield Trader”，也是原书如此。
- `site.py status` 能解析全部 28 节，共 1294 个块，每节只有一个一级标题。

## 原文疑点

- **缺失的图表**：见上文“来源”。表 P.1、表 3.1、表 6.1、表 6.2 是正文论证要用到的，翻译时只能译出标题和正文，读者看不到表的内容。如果能找到带图表的版本，可以补成 `en/images/` 下的图片或 Markdown 表格。
- **第 6 章的 “Wt”**：同一句里的 W₀、W₁、W₂ 都是下标，“Wt” 应该也是 W 加下标 t，EPUB 里是普通字母，照原样保留。
- **empiri-cism**：第 7 章脚注里的 your “empiri-cism” 也可能是作者有意用连字符拆开这个词，强调“经验”的本义；现在按换行连字符处理，连成 empiricism，翻译时可以再斟酌。
- **漏掉的空格**：这些错误无法判断是出版社的电子书本来就有，还是转换造成的。补上空格不改变意思，所以都补上了。
- **参考文献的格式**：作者、年份、页码之间常缺空格，书名的斜体范围也不完全统一，照原样保留。

- 书末注释“阿拉伯的怀疑论者”一条的 al-Ghazl 是乱码，和参考文献一样改成 al-Ghazālī（翻译完成后补改）。

## 用更好的来源补全（2026-11-05）

上面各节记的是第一次导入时的情况。2026-11-05 用户提供了更好的来源，由 Claude（Opus 5.5 agent）逐块比对，补上缺失的图表，并把 en/ 改成和它一致。这一节记录来源、比对方法和全部改动；改动涉及的各节，审校记录末尾另有“补全后的改动”。

### 来源

- 文件：用户提供的 MOBI（`new.mobi`，1.2 MB，SHA-256 `3fa7c25b97b7909ba2d5ea757e69cb0cf4b4856fcc806006d2666109292d1728`），由它解包成的 EPUB（`new.epub`，953 KB，SHA-256 `1e179298768d9a288c96cb73be35e1b6db6874547419515faf88a283841ce9b3`）。两个文件都不放进仓库，比对只在 `/tmp` 下的副本上进行。`book.json` 的 `source` 记的仍是第一次导入的 EPUB。
- 版本：和原来是同一个 Random House 电子书。版权页同样写 Copyright © 2004，电子书 ISBN 9781588367679，不同的是版本号：这一份是 rh_3.0_140823556_c0_r12，原来导入的是 v3.0_r8，也就是同一个电子书较新的一次修订。元数据里记着出版社 2022 年 8 月更新过这本电子书。
- 结构：34 个 XHTML 文件，顺序和目录都和原来一一对应，没有新的章节，也没有索引；没有中文网站插入的广告页。标记是干净的，没有 Epubor 在行内标签后面加的换行和空格。
- 图片 13 张：封面、书名页的图、出版社标志；两张 7×10 像素左右的小图，分别是带长音符号的 ā 和 ī，用来拼 al-Ghazālī 这个名字；其余 8 张就是原来缺的 5 张表和 3 张图。

### 比对的方法

`tools/compare_better_source.py` 直接读 EPUB，按 `book.json` 的 28 节逐节和 en/ 比较：

```bash
uv run --project framework/tools python -I books/fooled-by-randomness/tools/compare_better_source.py new.epub --places books/fooled-by-randomness/review/note-places.tsv
```

- 逐词比较：规则和 `check_source.py` 一样（转成小写，不计标点，词里的连字符、撇号和点算作词的一部分），整节的词序列放在一起比，所以漏掉、多出和错位的段落都会显示出来，每处差异给出 en/ 的行号。
- 逐段比较字符：英文的一段，如果它的词都来自新版的同一段，而且词数相同，就再比字符（去掉 Markdown 的强调记号；标题不计大小写和章号），找出标点、字母和空格的差别。1312 段里有 1284 段做了字符比较，其余 28 段是标题（章号写法不同，或者原书的标题分成几段）和有词差异的段落，已经在逐词比较里列出。
- 图表：新版每张图片的位置、旁边的图题，以及 en/ 在同一位置有没有图片或表格。从图片改写成的表格不参加逐词比较。
- 注释的位置：新版书末注释的每个主题词都链接到正文里的一个空标记（`nts_001` 等），脚本找出这个标记落在 en/ 的哪一段。
- en/ 有意保留的差异写在脚本的 `KEPT_WORDS` 和 `KEPT_CHARS` 里，打印为 kept；其余一律打印为 CHECK 并计数。改完以后，脚本报告要查的差异为 0，所有图表都找到了对应的图片或表格。
- 纯粹的格式差别（斜体范围、换行、标题级别和大小写）不算差异。

### 补上的图表

新版的 5 张表都是图片，内容是简单的文字表格，所以改写成 Markdown 表格，中英两边各一份，是可以翻译的块；表的图片没有放进仓库。3 张图是曲线图，图片放在 `en/images/`，只出现在英文文件里，图题照原来的中文。负数用减号“−”，金额按体例换算。

| 图表 | 位置（改动后的块号） | 做法 |
| --- | --- | --- |
| 表 P.1 混淆表 | 序章第 12 块，表题和副题后面 | 表格。原表没有列名，表头一行留空；七个组名（General、Market Performance、Finance、Physics and Engineering、Literary Criticism、Philosophy of Science、General Philosophy）用粗斜体单独占一行，共 26 行 |
| 表 3.1 不同尺度上的成功概率 | 第 3 章第 69 块 | 表格，“尺度、概率”两列，7 行 |
| 表 6.1 | 第 6 章第 10 块 | 表格，“事件、概率、结果、期望”四列，3 行 |
| 表 6.2 | 第 6 章第 20 块 | 表格，四列，3 行（原图在“合计”前面空了一行，没有照搬） |
| 图 6.1 时间序列入门 | 第 6 章图题（第 37 块）前面 | 图片 `en/images/figure-6-1.jpg`，图上的标注是英文（OBSERVATION PERIOD、TIME） |
| 表 11.1 交易员的方法与科学的方法 | 第 11 章第 35 块 | 表格，“交易员的叫法、学术名称、说明”三列，6 行 |
| 图 11.1、图 11.2 | 第 11 章两个图题（第 116、117 块）前面 | 图片 `en/images/figure-11-1.jpg`、`figure-11-2.jpg`，图上只有坐标数字 |

表里的中文按术语表和正文已有的译法写，例如 Luck 写“运气”、Skills 写“能力”、Noise 写“噪声”、Survivorship bias 写“幸存者偏差”、Prospect theory 写“前景理论”、Hindsight bias 写“后见之明偏差”；表 11.1 第一列的叫法照第 11 章第 32 块正文的译法写。术语表的“图表”“译者注”和混淆表三处说明已经同步改过。

### 新版的修订

r12 和 r8 之间有作者或出版社的修订。en/ 统一改成新版的文字，中文按下面的原则处理：意思变了的改中文，意思没变的不改。改掉的旧文字都记在这里，以后要对照旧版时可以查。

改变意思的修订，中文跟着改：

| 章节（块） | r8 的文字（原来的 en/） | r12 的文字（现在的 en/） | 中文 |
| --- | --- | --- | --- |
| 序言（15） | adaptation after a severe random event (not coincidentally also dominated by Daniel Kahneman, the pioneer of the ideas on irrational behavior under uncertainty). | adaptation after a severe random event. | 删去“这个领域同样由丹尼尔·卡尼曼……的先驱。”一句 |
| 第 3 章（33） | This point has been examined by behavioral economics pioneers Daniel Kahneman and Amos Tversky with regard to … | This point has been examined in some intellectual traditions with regard to … | 改成“有些思想传统研究过这一点” |
| 第 4 章（6） | what struck me while reading Richard Dawkins’ *Selfish Gene* | what struck me while reading Charles Darwin’s *On the Origin of Species* | 改成“查尔斯·达尔文（Charles Darwin）的《物种起源》（*On the Origin of Species*）”；`recaps/ch04.md` 一条要点跟着改 |
| 第 6 章（15） | people who are judged on their numerical performance | judged solely on | “只凭数字业绩” |
| 第 6 章（17） | interjected, “But, Nassim, you just boasted | interjected, “But you just boasted | 删去“纳西姆，” |
| 第 6 章（21） | they are paid in dollars. | they are paid in dollars, rubles, dinars, Phoenician thekles, or sesterces. | “美元、卢布、第纳尔、腓尼基的谢克尔或者塞斯特斯” |
| 第 6 章（23） | he came by Concorde | he came by the supersonic Concorde | “超音速的协和式飞机” |
| 第 6 章（27） | upgrading their PalmPilot | upgrading their handheld device | “掌上设备” |
| 第 6 章（33） | the global-warming debate | the climate change debate | 两处“全球变暖”改成“气候变化” |
| 第 11 章（18） | compared it to rational models | compared it to so-called rational models | “所谓的理性模型” |
| 第 11 章（24） | 段末有 A motivated reader can get concentrated in four volumes the collection of the major heuristics and biases papers. | 删去这一句 | 删去“有心的读者可以在四卷书里读到……合集。” |
| 第 11 章（26） | 没有 | 新加一段：Clearly there are limitations to what is seen as “irrational”: sometimes people equipped with the wrong framework may detect irrationality where there is none. Many biases seen by the Kahneman and Tversky school are not biases but just complicated behavior missed by the researchers. | 新译一段 |
| 修订第二版致谢（6） | … intellectual drive, after I saw that his work went so much deeper than mere rational choice under uncertainty. … Now understanding happiness is a *real* pursuit. | … intellectual drive. | 删去对应的一大段（163 个词，讲卡尼曼研究的意义） |
| 书末注释（第 4 章） | ***The Selfish Gene:*** Dawkins (1989, 1976). Hegel: In Popper (1994). | 删去这一条 | 删去这一块 |
| 书末注释（第 9 章，83） | 没有 | **The mysterious letter:** John Allen Paulos has a similar story in Innumeracy (Paulos 1988). The story was initially told to the author by the great mathematician (and sometime gambler) Donald Geman. | 新译一条，主题词照第 9 章小标题写“神秘的来信” |

泛指的代词改成两性并列，意思不变，中文按术语表“代词”一条照旧写“他”：第 1 章第 41、43 块（he or she、her or his），第 2 章第 19 块，第 8 章第 28 块，第 9 章第 36 块，第 12 章第 18 块，后记第 5 块（he or she、him or her）和第 14 块（讲央行行长的 he 改成 they），书末注释第 102 块。

新版改正的笔误。这几处原来记在各节的原文疑点里，中文本来就按改正后的意思译，没有改：序言第 6 块 that 改成 than；第 3 章第 80 块删去多余的 that（Note also the implication that…）；第 6 章第 53 块 brand on 改成 brand of；第 11 章第 52 块 spokesmen 改成 spokesman，第 66 块 simulations 改成 stimulations；第 12 章第 8 块 closed superstitions 改成 closet superstitions。

### 比对时发现的 en/ 自己的问题

- 七处斜体和破折号挨着，收尾或开头的星号贴着破折号，按 CommonMark 的规则不起作用，英文页面上会露出星号：序言第 20 块（affirming the consequent）、第 1 章第 23 块（indeterminism）、第 3 章第 49 块（Vanity Fair）、第 5 章第 30 块（interest rate differential）、第 6 章第 38 块（equations of motion）、第 11 章第 53 块（whatever the true reason）和第 90 块（premium sellers）。新版的斜体不包括破折号，en/ 照新版把破折号移到斜体外面。中文这几处的斜体本来就正常。改完以后用 markdown-it 渲染全书，中英文都没有露出的星号。
- 第 13 章第 9 块的 al-Ghazali 改成 al-Ghazālī，和全书其他地方一致，中文括注跟着改。新版这里用两张小图拼长音字母，拼出来是 al-Ghazāalīi，多了两个字母，说明原书这里本来就有排版问题。

### en/ 保留的差异

下面这些地方 en/ 和新版不同，是有意保留的，脚本里都列明了：

- 章号 One 到 Fourteen 写成 1. 到 14.；献辞和作者简介的一级标题是导入时加的；作者简介里作者名字的小型大写字母。
- 纸质版换行留下的连字符，en/ 已经连成一个词：aloof-ness、out-comes（两处）、non-sense，第 7 章脚注的 empiri-cism、in-dependently。新版也是这样，说明连字符来自原书。
- 新版自己的错误：序言的 Chapters13，第 6 章第 8 块的 themagnitude，第 12 章的 po¨tuit，第 7 章脚注的 al-Ghazälï，修订第二版致谢的 pre-and（en/ 写 *pre-* and）。
- 标点后面漏掉空格的 23 处，例如第 1 章 losses,”he says、第 6 章 interjected,“But、第 13 章 colleagues,“Nobels”as well。新版同样没有空格，所以这是原书电子版本来就有的错误，en/ 保留补上的空格。第 10 章 (like myself ) 多出的空格，en/ 照旧去掉。
- 第 7 章正文的两个星号已经换成脚注 `[^1]`、`[^2]`，脚注文件里的使用说明（To return to the corresponding text…）不收。

`tools/check_source.py` 比的是第一次导入的 EPUB，补全以后它会报出这次的改动；以后核对原文用 `tools/compare_better_source.py`。

### 注释能不能放回正文

新版里，107 条书末注释的主题词都链接到正文的一个位置，107 个位置全部找到了，对照表在 `review/note-places.tsv`（标记、章节、en/ 文件和行号、注释的主题词、那一段的开头）。没有找不到位置的注释，每个位置也都有注释链接过来。

书末注释这一节仍保留为单独的一节，没有改成脚注。原因有三个：原书正文里看不到注释的标记，读者是从注释链接回正文的；不少注释有好几段（例如“肯定后件”一条带三行推理式），框架的脚注只能是一行；改成脚注要拆掉这个已经译完、审校过的一节。如果以后想在阅读器里从正文跳到注释，可以用这张对照表来做，需要用户决定。

### 原文疑点（补全时新发现的）

- 第 6 章第 21 块的 Phoenician thekles：查不到 thekles 这种货币。腓尼基的货币是 shekel（谢克尔），阿拉米语写作 tekel，thekles 应该就是它，中文写“腓尼基的谢克尔”。
- 第 6 章的 Wt：图 6.1 上的 W 带下标 t，证实了上面“原文疑点”里的推测。正文照术语表仍写 Wt，没有改。
- 书末注释“神秘的来信”一条的 Innumeracy 在新版里没有斜体，en/ 照新版；中文照体例写《数盲》（*Innumeracy*）。

### 其他同步修改

- `glossary.md`：“图表”一条、“译者注”一条和核心概念表里的混淆表一行，改成图表已经补上。
- `review/terms/people-zh.tsv`：加了查尔斯·达尔文和约翰·艾伦·保罗斯（John Allen Paulos）两行；道金斯一行写明第 4 章和书末注释的改动（他在第 5 章正文里还出现一次）；Don Geman 一行写明书末注释新加的一条写作 Donald Geman，照写英文。`review/terms/README.md` 的人数改成 477。
- `recaps/ch04.md` 一条要点跟着第 4 章的修订改了，记在 `review/recaps.md`。
- 减号“−”是新出现的字符，重新生成了这本书的字体子集（`python3 scripts/site.py fonts fooled-by-randomness`）。

### 改动前后的数字

| 项目 | 改动前 | 改动后 |
| --- | --- | --- |
| en/ 正文的词数（`compare_better_source.py` 的算法，不含表格） | 98,337 | 98,235 |
| 新版对应部分的词数 | | 98,244 |
| 新加的 5 张表里的英文词数 | 0 | 261 |
| 图片 | 0 | 3 |
| `site.py status` 的块数 | 1294 | 1300（5 张表、第 11 章 1 段；书末注释删 1 块、补 1 块） |
| zh-cn/ 的汉字数 | 153,899 | 154,146 |

改完以后运行了 `python3 scripts/site.py status fooled-by-randomness`（28 节，1300/1300 块已译，第 7 章注释 2/2）和 `python3 scripts/site.py check fooled-by-randomness`（通过）。在阅读器的草稿预览里打开了序章、第 3、6、11 章，5 张表都显示成表格，3 张图都能加载。这些改动做了译者自检，还没有经过另一个 agent 的双语审校。
