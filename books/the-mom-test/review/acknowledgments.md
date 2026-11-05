# 致谢（acknowledgments）审校记录

全节 8 个块，原文没有注释，译文加了 1 条译者注（`[^t1]`）；中英逐块对应（`site.py status` 显示 8/8）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：全节 8 块，从标题到最后一段对照原文逐块检查漏译、增译、否定、条件、数字、谁感谢谁做了什么、术语义项、人名和格式。另外做了这几项：
  - 人名逐个对照 `review/terms/people-zh.tsv`：本节提到 32 个人、共 35 处（含只有名的 Devin、Laurence、Ryan、Ian、Pete，只写姓的 Lafley、Martin；Devin 和封面设计者 Devin Hunt 按人名表分两条），都用了约定的译名；每人第一次出现时括注英文，第二次出现的戴夫·查普曼、萨利姆·维拉尼、史蒂夫·布兰克只写中文。第一段十位审读者的顺序和英文相同。
  - 用 markdown-it 渲染译文：书名 *4 Steps to the E.piphany* 和译者注里的 *Playing to Win* 两处斜体都生效，页面上没有露出的星号。
  - 运行 `tools/term_consistency.py`：本节没有不符合约定译法的块。
  - 查了全节有没有破折号和体例禁用的对比句式，都没有。
- 发现并修改：
  - “big thanks to some other writers”和“big thanks for Mom & Dad”：初稿两段都写“还要非常感谢”，前后两段读着重复。后一段改为“当然，也要好好谢谢爸爸妈妈”。
  - “especially Salim Virani for calling me on my BS”：人名表的说明写的是“当面戳穿我的胡扯”，英文 calling me on 没有“当面”的意思。初稿没有照搬“当面”，译“我一胡扯，他就戳穿我”，保留作者随口说笑的语气。
- 几处译法的考虑：
  - “Nobody gets through the startup life alone.”：照术语表 startup life 的译法，写“创业生活，谁也没法一个人熬过来”。
  - “taking a punt on us”：英式说法，指冒险下注，译“在我们身上赌一把”。
  - “getting on that crazy train”：保留列车的比喻，译“跟我一起登上了那趟疯狂的列车”。上一句的 us 包括这三位伙伴，“跟我一起”是从上下文补出来的主语关系。
  - “lovingly yelling at me about sales every Friday”：保留作者“满怀爱意地吼”这种反差的说法，every Friday 译“每个星期五”。
  - “forcing me to actually read *4 Steps to the E.piphany*”：actually 说的是之前一直没真读，译“逼着我真把……读了一遍”。书名照术语表写《四步创业法》（*4 Steps to the E.piphany*），本节第一次出现，括注原题。
  - “my peers in the Braintrust who were the perfect sounding board”：Braintrust 照术语表照写；sounding board 指可以拿想法去试、听对方反应的人，译“有了想法找他们商量，再合适不过”。
  - “the good bits of the startup education world”：译“创业教育圈好的一面”，保留 good bits 暗含的“这一行也有不好的地方”。
  - “Richard Rumelt and Lafley/Martin on strategy”：鲁梅尔特和 Lafley/Martin 是两份不同的著作，用“理查德·鲁梅尔特（Richard Rumelt）以及雷富礼（Lafley）和马丁（Martin）”把两组分开。原文只写了两人的姓，没写书名，照第 8 章的做法括注 Lafley、Martin，并加了和第 8 章一字不差的译者注，说明指的是两人合著的《宝洁制胜战略》（*Playing to Win*）。
  - “Amy Hoy on worldviews, Brant Cooper on segmentation”：worldviews 译“世界观”，和第 7 章 worldview 的译法一致；segmentation 照术语表译“客户细分”。
  - “Derek Sivers on remembering that businesses are meant to make you happy”：前四项都写“谈某某”，这一项原文本身换了说法，译“则提醒你记住，做生意本来就是为了让自己快乐”。
  - “insane startup and/or shipwreck stories”：and/or 是作者的玩笑，这些故事有的讲创业，有的讲沉船，有的两样都是（创业失败也像沉船）。译“一大堆疯狂故事（有创业的，有翻船的，也有两样都占的）”，“翻船”在中文里同样既有字面意思，也能比喻失败。
  - “Veronica Torras”：人名表注明她的原名带重音（Verónica），这不算原文拼错，括注照英文原文写 Veronica Torras。
  - 两处 “Thanks!”：第一段是对审读者说的，译“谢谢大家！”；最后一段是对提供照片的网站说的，译“谢谢！”。
  - 网址 heisenbergmedia.com 和链接地址照写。这个 EPUB 里没有作者照片（见 `review/source.md`），照原文译，不另加说明。
- 未决：
  - 人名表里的审读者译名（丹尼尔·滕纳、安德烈亚斯·克林格、贝罗妮卡·托拉斯等）都是按读音音译的，没有通行译名，请用户确认。
  - 本节的 Pete、Tom Stone、Tim Barnes 和第 6 章示范邮件、开场白里的 Pete、Tom、Tim 是不是同一人，原文没说，译名照人名表写，没有加说明。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 6 块 | big thanks for Mom & Dad | for 应为 to，按“感谢爸爸妈妈”译 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 8 块（标题和 7 段正文）和末尾的 1 条译者注，逐块对照英文，查漏译、增译、否定、谁感谢谁做了什么和读着拗口的句子；另外逐个对照 `review/terms/people-zh.tsv` 核对 32 个人共 35 处提及的译名和括注，核对“创业生活”“客户细分”、Braintrust、《四步创业法》等术语和书名，以及破折号和“不是……而是……”句式。本节原文没有脚注。
- 发现：3 条，都是措辞问题；核实后采纳 3 条，不采纳 0 条。编辑逐条找出英文和中文核对过，问题都属实，三条都照审校者的建议改：
  - “A huge thanks to all the people who helped with feedback, and especially those who took the time to write up their ridiculously useful line-by-line comments: Daniel Tenner, ...”：原译“尤其是那些花时间把逐行意见写下来的人，这些意见有用得不得了：丹尼尔·滕纳……”，冒号紧跟在“这些意见有用得不得了”后面，名单读起来像在列举意见；“给过反馈、帮过忙的人”也像是两类人，原文说的是用反馈帮了忙的一类人。改为“万分感谢所有给过我反馈的人，尤其要感谢下面这几位，他们花时间写下了逐行的意见，有用得不得了：丹尼尔·滕纳（Daniel Tenner）、……”，“下面这几位”先点明冒号后面列的是人。
  - “Thanks to Saul Klein for lovingly yelling at me about sales every Friday”：原译“冲我吼销售的事”，“吼”后面直接带“……的事”作宾语，搭配别扭。改为“每个星期五都满怀爱意地为销售的事冲我吼”。
  - “and Derek Sivers on remembering that businesses are meant to make you happy.”：这一段列的是哪些作者的作品帮到了这本书，原文的 you 是泛指。原译“则提醒你记住”读着像作者突然转向读者说话，“提醒”和“记住”也有些重复。改为“德里克·西弗斯（Derek Sivers）则提醒我们，做生意本来就是为了让自己快乐”。
  - 不采纳的：没有。三处改后的中文都回查过英文，意思和英文一致。
- 审校者的总体判断：这一节译得忠实，读起来也顺。8 个块和 1 条译者注都对照过，没有发现意义错误、漏译、增译或否定弄反的地方，每一句谁感谢谁做了什么都对得上。人名全部和人名表一致，每人在本节第一次出现时括注英文，戴夫·查普曼、萨利姆·维拉尼、史蒂夫·布兰克第二次出现时只写中文，德文（Devin）和德文·亨特（Devin Hunt）按人名表分开写。术语和书名符合术语表，译者注 `[^t1]` 位置合适，和第 8 章的同一条译者注一字不差。全文没有破折号，也没有“不是……而是……”句式。“for Mom & Dad”的笔误按“感谢爸爸妈妈”译出并记入原文疑点，处理得当；shipwreck 译成“翻船”，字面意思和“失败”的比喻都保住了。需要改的只有上面三处小措辞，改完可以进入中文通读。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳审校意见以后，从标题到译者注顺着中文读完全节，看行文是否连贯，有没有重复、指代不清的地方，人名和术语前后是否一致。
- 发现并修改（回查了英文，意思没有变）：
  - “Thanks to Steve Blank for writing it.”：原译“感谢史蒂夫·布兰克（Steve Blank）写了这本书”。在致谢里，“这本书”最容易被读成《妈妈测试》本身，而且本节第 5 块的“对这本书的影响”“直接帮到了这本书”指的确实是《妈妈测试》，同一节里“这本书”就指了两本不同的书。英文的 it 指的是前一句的《四步创业法》，改为“写了那本书”，和后文的“这本书”分开。
- 读过、确认不用改的地方：审校时改过的三处放回上下文里读，衔接通顺；第一段改动以后，“下面这几位”和冒号后的十人名单对得上。32 个人名在本节第一次出现时都括注英文，后面只写中文。第 5 块相邻两句都写了“这本书”，指的都是《妈妈测试》，读着清楚，保留。第 6 块“疯狂故事（有创业的，有翻船的，也有两样都占的）”和“创业的种子”两处“创业”分别对应原文的 startup 和 entrepreneurial，保留。
- 检查：`site.py status` 显示 acknowledgments 8/8；`tools/term_consistency.py` 在本节没有报告不符合约定译法的块；全节没有破折号，也没有“不是……而是……”句式。

## 状态

- 没有未解决的意义问题。原文疑点照上面的表处理，双语审校和中文通读没有发现新的原文疑点。
- 译者自检里留下的两项待用户确认的事（审读者译名是音译；本节的 Pete、Tom Stone、Tim Barnes 和第 6 章的同名人物是不是同一人）不影响意思，照人名表写。
- 阅读器校样还没做；`book.json` 里本节的状态按分工由主会话修改。
