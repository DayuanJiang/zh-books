# 附录 准备一份谈判一页纸（appendix）审校记录

全节 80 个块：一级标题 1 个、二级标题 5 个、三级标题 3 个、段落 70 个、列表 1 个（四项）。原文没有注释，中英逐块对应（`site.py status` 显示 80/80）。英文是 2026 年 11 月 5 日从 HarperCollins 的完整电子书补进来的，见 [source.md](source.md) 的“用更好的来源补全（2026-11-05）”。

## 1. 译者自检

- 执行者：Claude（Opus 5.5），译者本人。
- 范围：从标题到最后一段，80 个块逐块对照英文，查漏译、增译、否定、条件、数字、术语义项、人名、斜体和体例。块号按 `site.py status` 的算法，标题是第 1 块。
- 处理：
  - 标题：照章标题“第 1 章 新规则”的格式写“附录 准备一份谈判一页纸”。Negotiation One Sheet 照术语表和第 1 章第 169 块写“谈判一页纸”。第 6 块娱乐业的 one sheet 第一次出现，写“一页纸”（one sheet），之后写“一页纸”。
  - 五个部分 Section I 到 Section V 写“第一部分”到“第五部分”。Labels/Accusation Audit 写“标注与指责清单”；Noncash Offers 写“非现金的提议”，和第 6 章的“非金钱条件”（nonmonetary terms）分开。
  - 三个三级标题都写成“用来……的问题”。deal killers 照术语表写“搅黄交易的人”；deal-killing issues 写“搅黄交易的因素”，标题里已经有“问题”（questions），issues 再写“问题”会分不清；diffuse 照术语表写“化解”。这几个写法补进了术语表。
  - 术语：labels 写“标注”，calibrated questions 写“校准式问题”，accusation audit 写“指责清单”（perform an accusation audit 写“列一份指责清单”），tactical empathy 写“战术共情”，behind the table 写“桌子后面”，“What” and “How” questions 写“‘什么’式和‘怎么’式的问题”，It seems like 和 It seems as though 都写“似乎”，“That’s right.” 写“没错”。第 30 块 “you haven’t done it right” 里的 right 写“到位”，“没错”只留给 That’s right。
  - BATNA：第 12 块第一次出现，写“一个叫 BATNA 的东西”；第 13 块原文给出全称，写“Best Alternative To a Negotiated Agreement 的缩写，意思是谈判协议的最佳替代方案”，和术语表的译法一致。罗杰·费希尔（Roger Fisher）、威廉·尤里（William Ury）、《谈判力》（*Getting to Yes*）在本节第一次出现，照体例括注。这里原文没有拿书名玩文字游戏，所以没有加译者注。
  - wimp-win：第 16 块照术语表写“认怂的‘双赢’（wimp-win）”，第一次出现括注原文；第 24 块列表里的 wimp out 写“临阵认怂”，和它呼应。
  - 数字和金额：$10,000 写“1 万美元”，$100、$140、$150 写“100 美元”“140 美元”“150 美元”，7:1 写“7 比 1”，ninety days 写“90 天”，four months 写“四个月”，three to five 写“三到五”，Decades of 写“几十年的”。
  - 填空式的标注（第 35 到 39 块、第 74 到 76 块）：空格照英文写成下划线，前后留空格。用仓库的 markdown-it 渲染过，下划线照原样显示，不会被当成强调符号。
  - 斜体：电子书里一句一段的斜体（每部分开头的说明、问题和标注）照写斜体；第 18 块的 *and*、第 43 块的两个 *what*、第 44 块的 *really* 保留在对应的词上。
  - 和正文相同的问题用正文的译法：第 54 块第一句和第 8 章第 76 块的第一句相同，中文也相同；第 55 到 57 块的三个问题照第 8 章第 76 块；第 51、65 块 “What’s/What is the biggest challenge you face?” 照第 7 章第 101 块写“你面临的最大挑战是什么？”；第 64 块照第 8 章第 137 块写“我们这次要对付的是什么？”；第 47 块照第 7 章第 103 块的“我们这是想达成什么？”去掉“这是”（原文没有 here）。第 48 块 “How is that worthwhile?” 中文写“这件事的价值在哪里？”，用“在哪里”提问，仍是没有固定答案的开放式问题，意思不变。
  - 第 45 块：J. K. 罗琳（J. K. Rowling）照体例括注；Harry Potter 在原文里是定语，没有斜体，书名广为人知，就写“《哈利·波特》的作者”，和《纽约时报》一样省去括注。引文没有查到通行的中译，自译。
  - 第 79 块讲的是第 6 章给孟菲斯律师协会做培训的事，“在协会杂志上为我做一篇封面报道”照第 6 章的说法；his board 写“理事会”。
  - 第 7 块原文 “It will have five short sections” 句末没有标点，中文照常写句号，记在 source.md 的原文疑点里。
  - 破折号：第 3、12、33、71 块原文的破折号改成逗号或分句；第 3 块原文用破折号连起来的两句话 you don’t rise to the occasion 和 you fall to your highest level of preparation，写成“人不会临场超常发挥，只会退回到……”，没有用体例禁用的对比句式。全节中文没有破折号。
- 发现并修改：
  - 第 16 块：初稿“很多自以为抱着‘双赢’目标的人，其实是一种认怂的‘双赢’心态”，主语“人”和“心态”搭配不上，改为“其实抱着的是一种认怂的‘双赢’（wimp-win）心态”。
  - 第 52 块 “How does this fit into what the objective is?”：初稿“这和我们的目标怎么对得上？”多了原文没有的“我们的”，删掉。
  - 第 59 块 “Internal negotiating influence”：初稿“在对方内部”，原文没有说是哪一方，改为“在组织内部”；comfortable with things as they are 从“满足于现状”改为更贴切的“安于现状”。
- 术语一致性：`tools/term_consistency.py` 在本节标出 1 处，第 6 块的 summarizes a product 写成“概括一件作品”。这是日常用法，和作者讲的总结技巧无关，保留。
- 阅读器里要留意的地方：构建器把一句一段的短斜体段落标为小标题样式（`reader-subheading`），第 3 章的 *It seems like …* 三行也是这样。附录里的问题和标注因此会显示得比较醒目，留给阅读器校样时决定是否需要处理。
- 还没有做：双语审校、中文通读和阅读器校样。

## 2. 双语审校（补全部分）

- 审校者：agent（Opus 5.5），独立的双语审校，没有参与这次补全和翻译。
- 范围：全节 80 个块，逐块对照英文，查意思、漏译、数字和金额、术语、斜体、填空式标注的下划线、中文是否通顺、破折号和体例禁用的对比句式。英文先用 `tools/compare_source.py` 和完整电子书比过，83 个单元（列表的四项各算一个）文字一致。和正文重复的句子、问题，逐个和第 6 到 9 章的译法核对。
- 发现并修改（6 处）：
  - 第 3 块 When the pressure is on, you don’t rise to the occasion …：同一句话在第 9 章“本章要点”最后一条（第 212 块）已经译成“压力来了，你没法临场超常发挥，准备到哪一步，就只能发挥到哪一步。”附录的译文“人不会临场超常发挥，只会退回到……”和它说法不一，“不会……只会……”也接近体例禁用的对比句式。改成和第 9 章相同的写法。
  - 第 18 块：一句话里连用两个“所以”（“所以，要知道自己不能接受什么……所以最好的结果很可能……”），删掉第二个。
  - 第 32 块 Prepare three to five labels to perform an accusation audit：译文“准备三到五句标注，列一份指责清单”把两件事写成了并列，原文的意思是用这几句标注来做指责清单，改为“准备三到五句标注，用来列一份指责清单”。
  - 第 42 块 identify and overcome potential deal killers：deal killers 照术语表写“搅黄交易的人”，“克服……的人”搭配不上，改为“找出、搞定可能搅黄交易的人”。
  - 第 44 块 our basic human expectations about negotiation：译文“我们作为人对谈判的一些基本预期”是硬译，改为“我们每个人对谈判都抱有的一些基本预期，常常会碍事”。
  - 第 60 块 A surprisingly high percentage of negotiations hinge on something outside dollars and cents. Often they have more to do with …：译文“比例高得惊人的谈判，关键都在钱以外的东西上。它们往往……”，前一句主语不通，后一句的“它们”指代不清。改为“成败取决于钱以外因素的谈判，比例高得惊人。这些谈判往往更多地关乎……”。
- 核对后保留的写法：
  - 数字和金额：1 万美元、100 美元、140 美元、150 美元、7 比 1、90 天、四个月、三到五、几十年，合乎体例。
  - 术语：标注、校准式问题、指责清单、战术共情、桌子后面、认怂的“双赢”（wimp-win）、搅黄交易的人、搅黄交易的因素、非现金的提议，都和术语表一致；“没错”只用在第 30 块的 That’s right，同一块的 done it right 写“总结到位”。
  - BATNA 第 12 块先写“一个叫 BATNA 的东西”，第 13 块原文给出全称时再解释，顺着原文的讲法，可以接受。
  - 填空式标注（第 35 到 39 块、第 74 到 76 块）的下划线数和英文相同；斜体保留在 *and*、两个 *what*、*really* 对应的词上。
  - 和正文重复的问题：第 54 到 57 块和第 8 章第 76 块一致，第 51、65 块和第 7 章一致，第 64 块和第 8 章第 137 块一致。
  - 第 45 块 J. K. 罗琳的引文意思完整；“名言”比 a great quote 稍重，可以接受。
  - 第 79 块“给律师协会做培训”和第 6 章孟菲斯律师协会那一段的说法一致。
  - 第 7 块原文句末没有标点、第 58 块把 defuse 写成 diffuse，同意译者照常写句号、写“化解”。
- 改完以后，全节中文没有破折号，也没有体例禁用的对比句式。
- 运行 `python3 scripts/site.py status never-split-the-difference`：全书 13 节都是 review，1958/1958 个块已译，注释 23/23；`python3 scripts/site.py check never-split-the-difference` 的草稿构建通过。改动用到的字都已经在字体子集里，没有重新生成字体。
- 仍待处理：阅读器把一句一段的短斜体显示成小标题样式，附录里的问题和标注因此很醒目，留给阅读器校样时决定。
