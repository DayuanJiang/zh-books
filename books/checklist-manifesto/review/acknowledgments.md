# 致谢（acknowledgments）审校记录

全节 11 个块（1 个标题、10 个段落），没有注释，也没有译者注，中英逐块对应（`site.py status` 显示 11/11）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全节 11 块，对照原文逐段检查漏译、增译、否定、人数和名单、谁做了什么、职务和机构名、术语义项；人名逐个对照 `review/terms/people-zh.tsv`。第 8 块的几份名单逐个数过：八个研究点的主要研究者 11 人，科学顾问组负责人 4 人，英国国家患者安全局 2 人，外科与公共卫生中心的同事 10 人，和原文相同。`site.py status` 显示 11/11；正文没有破折号，也没有体例禁用的对比句式。
- 检查：`tools/term_consistency.py` 在本节只标出第 4 块的 “name: Geoff Smart”，原因是 “Smart, tough, and tireless” 里形容词 smart 碰上了斯玛特的姓，属于误报；第 9 块的“杰夫·斯玛特（Geoff Smart）”写法正确。
- 发现并修改：
  - 第 4 块 “checked my facts, provided suggestions, and kept me honest”：初稿“提出了不少建议”多了原文没有的“不少”，改为“给我提建议”。
  - 第 5 块 “proved extraordinary in both her dedication and her effectiveness in carrying out work that has now extended across dozens of countries”：初稿“这项工作”在一句里出现两次，读着拖沓，改为“她推进的这项工作如今已经扩展到几十个国家，她的投入和成效都非同一般”。
  - 第 8 块 “the leaders of our scientific advisory group, as well as the many participants in the WHO Safe Surgery Saves Lives study group”：初稿写成“他们是我们科学顾问组的负责人，还有……研究组的众多参与者”，容易读成研究组的参与者也属于顾问组负责人。改为用分号隔开，让研究组的参与者成为“离不开以下各方”里单独的一项，和原文 as well as 并列的关系一致。
  - 第 9 块 “who let me invade their kitchen”：初稿“他们任由我闯进他们的厨房”两个“他们”相连，改为“闯进自己的厨房”。同一块 “who sent me the work of Geoff Smart”：初稿“寄给了我”带出了邮寄的意思，原文没有说怎么送来的，改为“发给了我”。
  - 第 10 块 “my life in writing and research and surgery”：初稿“一边当外科医生”把 surgery 说成了身份，改为“一边做手术”，和前面的“写作”“做研究”一样都是说做的事。
- 照体例处理的地方：
  - 人名：全节 86 个人名都按 `people-zh.tsv` 写，在本节第一次出现时括注英文，之后只写中文（伯威克在第 5 块第二次出现时只写中文）。称号放在中文名后面：Sir Liam Donaldson 写“利亚姆·唐纳森爵士（Sir Liam Donaldson）”，Lord Naren Patel 写“纳伦·帕特尔勋爵（Lord Naren Patel）”，Lord Ara Darzi 按表里的说明写“达尔齐勋爵（Lord Ara Darzi）”。Margaret Chan 用本人的中文姓名“陈冯富珍”。表里标 keep 的照写原名：Sooyeon Hwang，Yen Liow 和 Eeling Liow 照原文合写成“Yen 和 Eeling Liow”。原文合写的 “Jamie and Christopher Cooper-Hohn” 也合写成“杰米和克里斯托弗·库珀-霍恩（Jamie and Christopher Cooper-Hohn）”。原文没有说成对出现的几位是夫妻，译文没有加“夫妇”。
  - 机构和项目：World Health Organization 在本节第一次出现写“世界卫生组织（WHO）”，之后写“世卫组织”；WHO Patient Safety 按术语表写“世卫组织患者安全项目”，chair 写“主席”，executive director 写“执行主任”；director general、deputy director general、assistant director general 写“总干事”“副总干事”“助理总干事”；WHO Safe Surgery program 写“世卫组织安全手术项目”，WHO Safe Surgery Saves Lives study group 写“世卫组织‘安全手术拯救生命’研究组”；National Patient Safety Agency in the U.K. 写“英国国家患者安全局”；Brigham and Women’s Center for Surgery and Public Health 写“布莱根妇女医院外科与公共卫生中心”；Harvard Vanguard Medical Associates 写“哈佛先锋医疗协会”；Metropolitan Books 照写原名，第一次出现加“出版社”，第二次的 Metropolitan 照原文简写。
  - 术语：ICUs 在本节第一次出现写“重症监护室（ICU）”；research fellow 写“研究员”；principal investigators 写“主要研究者”；作者的文章写“《纽约客》文章《清单》（“The Checklist”）”，和术语表的例子相同；《纽约客》不括注。
  - 医学说法：H1N1 influenza 写“甲型 H1N1 流感”（中国大陆的通行说法）；diarrheal infections 写“感染性腹泻”；operating room crises 写“手术室危机”。
  - 比喻照原文保留：“the steel columns of the surgery checklist work” 写“手术清单工作的钢铁支柱”，和第 3 章摩天大楼的钢结构呼应。
  - 第 9 块 “Unnamed here are …”：here 指本书正文。核对了英文全书：伦纳德、豪伊特和塞梅尔只出现在注释的出处里（第 4 章注释 1、第 1 章注释 2），卡茨、希尔、阿尔维斯、赫伯特在正文里没有出现，所以译作“还有一些人的名字没有出现在书中”。
- 未决：
  - 第 8 块 “Sidhir Joseph”：原文的拼写和《新英格兰医学杂志》2009 年八城市试点研究论文的作者名单（Sudhir Joseph）对不上，见下面“原文疑点”。译文暂按 `people-zh.tsv` 写“西迪尔·约瑟夫（Sidhir Joseph）”；如果主会话改用正确的拼写，建议改成“苏迪尔·约瑟夫（Sudhir Joseph）”，并同步修改 `people-zh.tsv`。
  - 第 8 块 “Lord Ara Darzi”：按表的说明只写“达尔齐勋爵”；同一份名单里的 Lord Naren Patel 写了全名“纳伦·帕特尔勋爵”，如果要两处一致，可以改成“阿拉·达尔齐勋爵”。
  - 第 7 块 “were early and vital backers”：backers 写“支持者”。`people-zh.tsv` 把这几位记作“早期资助人”，原文没有明说是出钱，按字面写得宽一些。
  - 第 8 块 “our eight study sites around the world”：写“八个研究点”，照原文的 study sites；第 7 章同样这八家医院写作“八家试点医院”，如果希望全书一致，可以改成“我们在世界各地的八家试点医院”。
  - 第 3 块 “My agent”：写“经纪人”，指作者的文学经纪人，中文读者大多能从上下文看懂，没有补“文学”。
  - 第 4 块 “kept me honest” 译作“让我始终实事求是”，“with inspired intelligence” 译作“审读文稿时才思敏锐”，“with almost alarming efficiency” 译作“以高得几乎吓人的效率”，都按意思处理。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 8 块，八个研究点的主要研究者名单 | Sidhir Joseph | 《新英格兰医学杂志》2009 年论文 “A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population” 的作者名单写作 Sudhir Joseph（新德里圣斯蒂芬医院），原文疑似拼错。`en/` 照原文保留；译文暂按 `people-zh.tsv` 写“西迪尔·约瑟夫（Sidhir Joseph）”，是否改成“苏迪尔·约瑟夫（Sudhir Joseph）”由主会话决定 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 11 块逐块对照原文，逐个核对人名表；几份名单逐个数过（世卫组织工作人员 13 人，八家试点医院的主要研究者 11 人，科学顾问组负责人 4 人，外科与公共卫生中心的同事 10 人），“将近十年”“过去三年”“几十个国家”“十多年”这些数量也核对过；检查了破折号和体例禁用的句式。
- 发现：9 条；编辑逐条回查英文和中文后，采纳 9 条，不采纳 0 条。其中 6 条照审校者的建议改，3 条（第 2 块开头、施洛斯、雷姆尼克）换了写法：
  - 意思问题，照建议改：
    - 第 9 块 “who let me invade their kitchen”：“他们任由我闯进自己的厨房”里的“自己”可以理解成“我自己”，和 their kitchen 相反。改为“他们任由我闯进他们的厨房”。第 4 章写的也是“厨房”，两处保持一致。
    - 第 9 块 “Unnamed here are Jonathan Katz, …”：原译“名字没有出现在书中”和事实不符，这些名字就印在致谢里，伦纳德、豪伊特和塞梅尔还出现在注释的出处里（第 4 章、第 1 章）。编辑在英文全书里核对过，这几位在正文里都没有出现。改为“还有一些人，正文里没有提到他们的名字：”。
  - 统一说法，照建议改：
    - 第 8 块 “the principal investigators at our eight study sites around the world”：“八个研究点”改为“八家试点医院”，和第 7 章以及术语表 pilot sites 的写法一致，指的是同一批医院。
  - 翻译腔和用词分寸：
    - 第 2 块 “the ones behind the writing, the ones behind the ideas, and the ones who made both possible”：照搬了 made both possible 的说法。审校者建议把最后一类写成“让写作和研究得以进行”，这样会把 ideas 换成“研究”，编辑改为“一类帮我把书写出来，一类给了我书中的想法，还有一类人，没有他们，这两样都无从谈起”。同一块 “As the book involved background research …” 主语搭配不当，照建议改为“写这本书需要……做背景研究”。
    - 第 5 块 “was kind enough to bring me aboard to lead it and then showed me what leadership in public health really meant”：“好心请我”口气像施舍，“领导力真正意味着什么”是直译腔。照建议改为“承蒙他邀请我加入并领导这项行动，后来他又让我见识了公共卫生领域真正的领导力是什么样子”。
    - 第 7 块 “were early and vital backers”：“早期至关重要的支持者”修饰语堆在一起。审校者建议写“很早就给了我们至关重要的支持”，编辑先照此改，通读时一度写成“给了这项工作”，因为同一块已经有两个“这项工作”，最后仍用“我们”。backers 照原文写“支持”。
    - 第 4 块 “Roslyn Schloss provided meticulous copyediting and a vital final review”：“做了一丝不苟的文字编辑”容易读成“当了一个文字编辑”。审校者建议“加工了文字”，编辑改为“一丝不苟地做了文字编辑工作，还完成了至关重要的最后一轮审读”，保留出版业通用的“文字编辑”。
    - 第 10 块 “has been nothing but kind and loyal”：“不离不弃”感情色彩过重。审校者建议“一直信任我、支持我”，其中“信任”是原文没有的意思，而且这一块已经有好几个“支持”。编辑改为“待我一向宽厚，也一直站在我这边”，用“站在我这边”对应 loyal。
    - 第 9 块 “whose generosity and forbearance helped me explore their fields”：“帮我探索了他们的领域”是直译，照建议改为“让我得以深入了解他们的领域”。
  - 不采纳的：没有。9 条都核实成立。
- 审校者的总体判断：全节没有漏译、增译或数字错误，名单人数和人名都和原文、人名表一致，`site.py status` 显示 11/11，可以定稿，只需要小改。需要改的意思问题有两处（厨房的“自己”和“没有出现在书中”），其余是翻译腔、用词分寸和全书统一的说法。审校者还核对了 “Sidhir Joseph”：2009 年《新英格兰医学杂志》论文的作者名单写的是 Sudhir Joseph，译者在“原文疑点”里的记录是对的；达尔齐勋爵只写姓是照人名表的规定，算不上错误，同一份名单里纳伦·帕特尔勋爵写了全名，是否统一由主会话决定。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：顺着中文读完全节 11 块，看连贯、重复、指代和人名术语前后是否一致。每一处改动都回查了英文。
- 发现并修改：
  - 第 2 块 “But this book could never have been completed without all of them.”：采纳审校意见后，前一句出现了“没有他们，这两样都无从谈起”，后面的“要是没有他们每一个人”就容易读成只指第三类人。改为“但要是没有所有这些人”，指前面说的所有要感谢的人，和 all of them 一致。
  - 第 4 块 “went through the text with inspired intelligence”：上一句改成“最后一轮审读”后，紧接着的“审读文稿时才思敏锐”重复了“审读”。改为“看稿时才思敏锐”。
  - 第 7 块 “were early and vital backers”：同上，“这项工作”在一块里出现三次，改回审校者建议的“给了我们至关重要的支持”。“我们”指作者和他的团队，和后文“我们的八家试点医院”“我们科学顾问组”的说法相同。
  - 第 10 块 “I could not be more fortunate to have such extraordinary people behind me.”：这一块里“支持”出现了四次，最后一句改为“我能有这样一群了不起的人做后盾，真是再幸运不过了”，“做后盾”对应 behind me。
  - 没有改的地方：“至关重要”在第 2、4、5、7 块各出现一次，原文这几处也接连用了 pivotal、vital、crucial、vital；换成别的词会改变分量，保留。第 5 块“世卫组织患者安全项目主席……发起了世卫组织减少手术死亡的全球行动”两次写“世卫组织”，第二次对应原文 the organization’s，写全称更清楚，保留。
  - 一致性：人名都和人名表一致，本节第一次出现时括注英文，伯威克第二次出现只写中文；凯瑟琳、亨特、哈蒂、沃克在本节第一次出现也括注了英文。“世界卫生组织（WHO）”只在第一次出现时写全称，之后写“世卫组织”。`tools/term_consistency.py` 在本节标出的 “name: Geoff Smart” 仍是 “Smart, tough, and tireless” 造成的误报。
  - 修改后运行 `site.py status`，仍是 11/11；中文里没有破折号，也没有体例禁用的句式。

## 状态

没有未解决的意义问题。译者自检“未决”里的两项已经处理：“八个研究点”已改为“八家试点医院”；backers 照原文写“支持”。剩下两项留给主会话：Sidhir Joseph 是否改用正确拼写 Sudhir Joseph（见“原文疑点”），以及达尔齐勋爵是否写全名“阿拉·达尔齐勋爵”，和纳伦·帕特尔勋爵一致。这两项都不影响意思。
