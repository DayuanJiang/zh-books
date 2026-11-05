# 术语统计

翻译之前做的统计。英文用整理过的 `en/`（和 EPUB 逐节核对过词数，见 [../source.md](../source.md)），统计时去掉脚注，只算正文。这本书没有脚注，去掉脚注的副本和 `en/` 完全相同。

```bash
# 1. 正文语料和 spaCy 候选词（en-zh-translation-polish 的脚本，门槛：频次不少于 3）
corpus.py extract --root <去掉脚注的 en/ 副本> --include '*.md' --language en --out en.json
terms.py candidates --corpus en.json --english-backend spacy --spacy-model en_core_web_sm --min-frequency 3 --out candidates.json
# 2. 其余几份表，并把出现次数和首次出现的章节填进 glossary.md 的核心概念表
$PY -I books/the-mom-test/tools/term_stats.py candidates.json
```

`$PY` 是装了 `en-zh-translation-polish/scripts/requirements-spacy.txt`（spaCy 3.8.7）和 `en_core_web_sm` 3.8.0 的 Python 3.12 环境，第 1 步的两个脚本也在这个环境里运行。`term_stats.py` 只读本书的 `book.json`、`en/`、`people-zh.tsv` 和 `glossary.md`，不读 EPUB。

| 文件 | 内容 | 数量 |
| --- | --- | --- |
| `candidates.tsv` | spaCy 名词短语候选：频次、分布的章数、首次出现的章节、词数、常见词形 | 614（多词 111） |
| `entities.tsv` | spaCy 识别出的专名（人名、机构、产品、地名、作品等）：标签、次数、章数、首次出现的章节。错标很多，只用来发现名字 | 146 |
| `people-zh.tsv` | 书里出现的每个人：中文译名、依据（established 是通行译名，transliterated 是按新华社译名规则音译）、身份和说明 | 44 |
| `people.tsv` | `people-zh.tsv` 里每个人在正文中出现的次数、章数和首次出现的章节，以及计数用的正则 | 44 |
| `definitions.tsv` | 原文里的定义句（I call、is called、refer to、calls them、types of、the mnemonic、e.g. 等），以及列表里用破折号接着解释的术语（例如 Commitment、Product risk 两项） | 50 |
| `headings.tsv` | 各节的全部标题，含级别（`#` 11 个，`##` 和 `###` 86 个） | 97 |
| `repeats.tsv` | 在书里出现不止一次的段落、引文和列表项，主要是速查表照抄正文的部分，各处要译得一字不差 | 63 |
| `glossary-evidence.tsv` | 术语表核心概念每一条的首次出现和原文例句，以及裁定者 | 97 |

- **没有纸质版索引**：这本书是作者自己出版的小册子，没有索引，所以没有 `index-terms.tsv`。人名的来源是 `entities.tsv` 里的 PERSON 一类，加上通读全书时记下的名字。spaCy 认出的人名全部收进了 `people-zh.tsv`；它没有认成人名的 Scott 和 Lafley/Martin 是通读时补的；它把 App Store、Groupon、McKinsey、Twitter 这些错标成人名，放进了术语表的“机构、产品与地名”。
- **人名的译法**：名人和有中译本的作者先在网上核对通行译名，例如史蒂夫·布兰克（《四步创业法》中译本）、埃里克·莱斯（《精益创业》中译本）、雷富礼和罗杰·马丁（《宝洁制胜战略》中译本）、理查德·鲁梅尔特、尼尔·雷克汉姆、戈登·拉姆齐、凯文·贝肯；查不到通行译名的按新华社译名规则音译，非英语的名字按原语言读音（西班牙语的 Verónica Torras、匈牙利语的 Tóth Orsolya）。书里没有华裔人物。
- **筛选**：从这几份数据里挑出书中特有、反复出现或作者专门定义过的概念。作者自己命名的做法（妈妈测试、悲情问题、会面反模式、客户切分）、第 2 章的三种坏数据和三种应对（挡开恭维、锚定空话、深挖想法）、第 5 章的承诺与推进、第 6 章约见面的五个要素，都来自定义句和小标题。僵尸线索、被发好人卡、房间里的大象、止痛药和维生素这类比喻频次低，是通读时补上的。速查表重复正文的列表，所以记笔记的十二个符号的说明也统一写进了术语表。常见的创业和销售用语（推销、线索、引荐、预算、采购流程）也收进来，保证各章译法一致。
- **结果**：术语表核心概念 97 条（全书译完后按编辑的建议又补了 rewarding、best guess、beliefs、exact quote 4 条），另有一张机构、产品与地名的表（19 行），状态都是“初定”。章节标题是自己定的：在网上、豆瓣和中文书店都没有查到这本书的中译本。
- **注意**：
  - 出现次数按英文词形的正则匹配统计，含标题，可能把同词根的普通用法也算进去，例如 learning 含动词用法，meeting、commit、business 含各种搭配。正则写在 `term_stats.py` 的 `COUNTS` 里。
  - `people.tsv` 按全名、姓或书里只有一个人用的名来数，只有名的人（Pete、Tim）在后面不跟姓时才算。所以第 4 章只写 Steve 的那一次没有算到布兰克名下；第 6 章示范邮件的 Pete 和致谢里的 Pete 合在一行。
  - `definitions.tsv` 按关键词抓句子，含不少普通用法（例如 called the police），zombie leads 这类用冒号下定义的句子抓不到，要结合通读。

## 一致性检查（全书译完后）

```bash
uv run --project framework/tools python -I books/the-mom-test/tools/term_consistency.py report.json
```

对 `term_consistency.py` 里 `TERMS` 列出的术语和 `people-zh.tsv` 里的每个人，找出英文含这个词或名字的块，检查对应的中文块里有没有约定的译法，没有的写进 `report.json`。同一术语有不止一种译法的，回到上下文判断是否需要统一。
