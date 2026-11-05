# 致谢（acknowledgments）审校记录

全节 15 个块（标题和 14 个段落），原文没有注释，中英逐块对应（`site.py status` 显示 15/15）。英文是 2026 年 11 月 5 日从 HarperCollins 的完整电子书补进来的，见 [source.md](source.md) 的“用更好的来源补全（2026-11-05）”。

## 1. 译者自检

- 执行者：Claude（Opus 5.5），译者本人。
- 范围：标题和 14 个段落，从第 1 块到第 15 块逐段对照英文，查漏译、增译、否定、数字、人名、机构名、头衔和体例。块号按 `site.py status` 的算法，标题是第 1 块。
- 处理：
  - 人名：除了作者本人，本节一共出现 26 个人。[review/terms/people-zh.tsv](terms/people-zh.tsv) 里已有的照表写：布兰登（Brandon）、希拉·汉（Sheila Heen）、加里·诺斯纳（Gary Noesner）、查克·雷吉尼（Chuck Regini）、温妮·米勒（Winnie Miller）、查理·博杜安（Charlie Beaudoin）。表里没有的 19 人按通行的音译习惯译，补进了表里，例如霍利斯·海姆鲍奇（Hollis Heimbouch）、文斯·达尔丰佐（Vince Dalfonzo）、约翰·利古奥里（John Liguori）、汤姆·斯特伦茨（Tom Strentz）。塔尔·拉兹照中文版《掌控谈话》的写法。每人第一次出现括注英文，之后原文只写名的写名：霍利斯、希拉、约翰、加里、查克、丹尼斯、文斯、德里克、塔尔。第 3 块原文又写全名 Tahl Raz，中文照写全名“塔尔·拉兹”，括注只在第 2 块第一次出现时加。凯西·埃林斯沃思已故的丈夫只有名，写“比尔（Bill）”。
  - 布兰登照第 5、9 章的写法，只写名、括注 Brandon，加“我儿子”。第 2 块 another Chris in the room 写“屋里多了一个克里斯”。
  - 机构：第 8 块第一次出现 Crisis Negotiation Unit 和缩写 CNU，照术语表写“危机谈判小组（CNU）”，之后写“危机谈判小组”。Critical Incident Negotiation Team 写“FBI 重大事件谈判组”，和术语表的“重大事件应对小组”用同一个说法。第 10 块的 Joint Terrorist Task Force 写“联合反恐特遣队”（正式名称是 Joint Terrorism Task Force，记在 source.md 的原文疑点里），Crisis Negotiation Team 写“危机谈判组”。第 11 块 NYPD’s Hostage Negotiation Team 写“纽约市警察局人质谈判组”。HarperCollins 写“哈珀柯林斯”，USC 写“南加州大学”，Georgetown 写“乔治城大学”。这些写法都补进了术语表。
  - 头衔：lead international kidnapping negotiator 照术语表写“首席国际绑架案谈判专家”；publisher 指出版社里负责这本书的人，写“出版人”；agent 写“经纪人”；an adjunct at Georgetown 写“到乔治城大学当兼职教授”；wingmen 写“搭档”。
  - 数字：five a.m. 写“早上 5 点”，in three hours 写“三个小时后”，since he was two years old 写“从两岁起”，two years later、a year after that 写“两年后”“又过了一年”。
  - 第 14 块 “I need a car in sixty seconds or she dies.” 是第 3 章那个入门练习“60 秒，否则她就死”里的话，写“60 秒之内给我弄辆车来，否则她就死”，数字写法和第 3 章一致。stopped breathing 写“吓得屏住了呼吸”。
  - 破折号：第 8 块原文的括号里用破折号连着 Crisis Negotiation Unit 和缩写 CNU，中文改成一个分句“帮他做到这一点的，是他在危机谈判小组（CNU）的团队”，免得括号里再套括号。全节中文没有破折号，也没有体例禁用的对比句式。
  - 第 15 块 blessed、grace 写“蒙福”“恩典”，保留原文的宗教色彩；最后一句 (I need all the help I can get.) 是作者的自嘲，写“（我需要的帮助，越多越好。）”。
- 发现并修改：
  - 第 2 块 “Brandon was there to keep the information flow going as Tahl soaked it up”：初稿“他负责让信息源源不断地说出来”，“信息”和“说出来”搭配不上，改为“负责让信息源源不断地流动，塔尔就把这些全都吸收进去”。
- 术语一致性：`tools/term_consistency.py` 在本节标出 1 处，第 2 块的 To be fair 写成“说句公道话”。这是日常说法，和第 6 章讲的“公平”这个概念无关，保留。
- 还没有做：双语审校、中文通读和阅读器校样。

## 2. 双语审校（补全部分）

- 审校者：agent（Opus 5.5），独立的双语审校，没有参与这次补全和翻译。
- 范围：全节 15 个块，逐句对照英文，查意思、漏译、数字、人名、机构名、术语、中文是否通顺、破折号和体例禁用的对比句式。英文先用 `tools/compare_source.py` 和完整电子书比过，15 个块文字一致。人名逐个和 [terms/people-zh.tsv](terms/people-zh.tsv) 以及各章的写法核对。
- 发现并修改（3 处）：
  - 第 2 块 helping me shape and create these ideas：译文“帮我梳理、打磨这些想法”缺了 create（构思、提出）的意思，改为“帮我构思、打磨这些想法”。
  - 第 4 块 Steve Ross, my agent, is a man of integrity and was perfect for this book：译文“为人正直，和这本书再合适不过”，主语是人，后半句搭配不顺，改为“为人正直，由他来经手这本书再合适不过”。
  - 第 14 块 Georgetown and USC have both been phenomenal places to teach：译文“都是非常好的教书的地方”连用两个“的”，语气也比 phenomenal 弱，改为“都是绝佳的教书之地”。
- 核对后保留的写法：
  - 人名：26 人的译名和人名表一致，每人第一次出现时括注英文，之后只写名的地方写名；新增的 19 个音译名读音合理。
  - 第 8 块 five a.m.、in three hours 写“早上 5 点”“三个小时后”，合乎数字体例；括号里 Crisis Negotiation Unit 和 CNU 之间的破折号改写成分句，意思完整。
  - 第 10 块 Joint Terrorist Task Force 写“联合反恐特遣队”，和术语表一致；原文的笔误已经记在 [source.md](source.md)，同意不加译者注。
  - 第 14 块练习里的那句话，和第 3 章的“60 秒，否则她就死”写法一致。
  - 第 2 块 To be fair 写“说句公道话”，是日常说法，和第 6 章的“公平”概念无关，同意保留。
- 全节中文没有破折号，也没有体例禁用的对比句式。
- 运行 `python3 scripts/site.py status never-split-the-difference`：全书 13 节都是 review，1958/1958 个块已译，注释 23/23；`python3 scripts/site.py check never-split-the-difference` 的草稿构建通过。改动用到的字都已经在字体子集里，没有重新生成字体。
