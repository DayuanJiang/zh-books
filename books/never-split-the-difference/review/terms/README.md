# 术语统计

翻译之前做的统计。英文用整理过的 `en/`（和 EPUB 逐章核对过词数，见 [../source.md](../source.md)），统计时去掉脚注，只算正文。这本书没有脚注，去掉脚注的副本和 `en/` 完全相同。

```bash
# 1. 正文语料和 spaCy 候选词（en-zh-translation-polish 的脚本，门槛：频次不少于 3）
corpus.py extract --root <去掉脚注的 en/ 副本> --include '*.md' --language en --out en.json
terms.py candidates --corpus en.json --english-backend spacy --spacy-model en_core_web_sm --min-frequency 3 --out candidates.json
# 2. 其余几份表，并把出现次数和首次出现的章节填进 glossary.md 的核心概念表
$PY -I books/never-split-the-difference/tools/term_stats.py candidates.json
```

`$PY` 是装了 `en-zh-translation-polish/scripts/requirements-spacy.txt`（spaCy 3.8.7）和 `en_core_web_sm` 3.8.0 的 Python 3.12 环境，第 1 步的两个脚本也在这个环境里运行。`term_stats.py` 只读本书的 `book.json`、`en/`、`people-zh.tsv` 和 `glossary.md`，不读 EPUB。

| 文件 | 内容 | 数量 |
| --- | --- | --- |
| `candidates.tsv` | spaCy 名词短语候选：频次、分布的章数、首次出现的章节、词数、常见词形 | 1500（多词 274） |
| `entities.tsv` | spaCy 识别出的专名（人名、机构、地名、作品等）：标签、次数、章数、首次出现的章节。错标很多，只用来发现名字 | 655（其中 PERSON 212） |
| `people-zh.tsv` | 书里出现的每个有名字的人：中文译名、依据（established 是通行译名，transliterated 是按新华社译名规则音译，keep 是照写原文）、身份和说明 | 125 |
| `people.tsv` | `people-zh.tsv` 里每个人在正文中出现的次数、章数和首次出现的章节，以及计数用的正则和限定的章节 | 125 |
| `definitions.tsv` | 原文里的定义句（I call、what I call、is called、known as、refer to、the term、that is、technique、rule、model、effect、theory、three kinds of 等） | 163 |
| `headings.tsv` | 各章的全部标题，含级别：`#` 10 个，章副标题 10 个，`##` 76 个，`###` 21 个 | 117 |
| `italics.tsv` | 两个词以上的斜体短语和大写开头的斜体单词：书名、影片、作者点名的概念、引用的邮件和脚本 | 79 |
| `repeats.tsv` | 在书里出现不止一次的段落和列表项，各处要译得一字不差 | 6 |
| `glossary-evidence.tsv` | 术语表核心概念每一条的首次出现和原文例句，以及裁定者 | 146 |

- **没有纸质版索引**：用户提供的 EPUB 只有第 1 到 10 章，印刷版的索引、注释和附录都不在里面，所以没有 `index-terms.tsv`。人名的来源是 `entities.tsv` 里的 PERSON 一类，加上通读全书时记下的名字：spaCy 漏掉的 Mishary、Samantha、Eddie，只以绰号出现的 the Blind Sheikh，只在书名里出现的笛卡尔，都是通读时补的；它把 Key Lessons、Dos Palmas、Jedi 这些错标成人名，没有收进人名表。
- **人名的译法**：名人和有中译本的作者先在网上和中文维基百科核对通行译名，例如罗杰·费希尔和威廉·尤里（《谈判力》中译本）、希拉·汉（《高难度谈话》中译本）、迪帕克·马尔霍特拉和马克斯·H. 巴泽曼（《哈佛经典谈判术》中译本）、埃伦·兰格、罗伯特·米勒、泰德·莱昂西斯；查不到通行译名的按新华社译名规则音译，非英语的名字按原语言读音（西班牙语的何塞、华金、赫苏斯·布埃诺、吉列尔莫·索韦罗，荷兰语的威廉·德·弗拉明）。共 50 个通行译名、74 个音译、1 个照写原文（TJ）。书里没有能确认身份的华裔人物；Ediborah Yap 和 Alastair Onglingswan 的姓可能来自菲律宾华人的姓氏，没有查到中文名，按音译，记在说明里。
- **章名**：中文版《掌控谈话》（赵坤译，北京联合出版公司、磨铁图书，2018）的章名只作参考，豆瓣只列出前六章。术语表里的章名是按这份译文的术语自己定的。
- **筛选**：从这几份数据里挑出书中特有、反复出现或作者专门定义过的概念。作者的方法（战术共情、镜像模仿、标注、指责清单、校准式问题、“没错”、三次法则、阿克曼模型、黑天鹅）来自定义句、斜体和小节标题；第 5 章积极倾听的六种手段、第 9 章的三种谈判风格、第 10 章的三种筹码和三种误会来自小节标题和列表。“吐信息”“收尾谈判专家”“路过式派活”“关怀式对质”这类只出现一两次的说法，是通读时补上的。书里引用的行为经济学概念（前景理论、损失厌恶、系统 1 和系统 2）和常见的谈判用语（对方、筹码、讨价还价）也收进来，保证各章译法一致。
- **结果**：术语表核心概念 146 条，分成九组；另有一张书名与影片的表和一张机构、产品与地名的表，状态都是“初定”。
- **注意**：
  - 出现次数按英文词形的正则匹配统计，含标题，可能把同词根的普通用法也算进去，例如 deal、frame、range、punch、constrained。正则写在 `term_stats.py` 的 `COUNTS` 里。
  - `people.tsv` 按全名、姓或书里只有一个人用的名来数。同名同姓的人在 `term_stats.py` 的 `PATTERNS` 里按章节分开：第 2 章的 Joe 是纽约警察局的谈判专家，第 4 章的 Joe 是虚构的“商人乔”；第 4 章的 Martin 是纽约警察局的副队长，第 7、8 章的 Martin 是马丁·伯纳姆；第 6 章的 Moore 是唐·A. 穆尔，第 10 章的是玛格丽特·穆尔。第 2 章博比说的 Where’s Chris? 指克里斯·沃茨，却算在了作者名下。
  - `definitions.tsv` 按关键词抓句子，含不少普通用法（例如 rule、that is），“镜像就是重复对方最后三个词”这种用冒号或 is when 下定义的句子不一定抓得到，要结合通读。

## 一致性检查（全书译完后）

```bash
uv run --project framework/tools python -I books/never-split-the-difference/tools/term_consistency.py report.json
```

对 `term_consistency.py` 里 `TERMS` 列出的术语和 `people-zh.tsv` 里的每个人，找出英文含这个词或名字的块，检查对应的中文块里有没有约定的译法，没有的写进 `report.json`。人名用和 `people.tsv` 一样的正则，按名或姓的中文都算对。同一术语有不止一种译法的，回到上下文判断是否需要统一。
