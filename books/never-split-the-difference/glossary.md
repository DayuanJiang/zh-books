# 术语表

翻译前根据 `review/terms/` 里的统计数据裁定（来源和门槛见 [review/terms/README.md](review/terms/README.md)）。“出现次数”和“首次出现”由 `tools/term_stats.py` 按英文词形统计，含标题；按正则匹配，可能把同词根的普通用法也算进去，例如 deal、frame、range、punch。状态都是“初定”，由 Claude 裁定，等用户确认；改动时要回查已经译完的章节。

中文版《掌控谈话》（赵坤译，北京联合出版公司、磨铁图书，2018）的书名和章名只作参考，下面的译法是按这份译文自己定的；和中文版不同的地方在“不要混同”一栏注明。

## 体例

- **人名**：用 [review/terms/people-zh.tsv](review/terms/people-zh.tsv) 的译名。每章第一次出现时在中文名后括注英文原名，例如“罗伯特·姆努金（Robert Mnookin）”，之后只写中文。只有名的人（Anna、Benjie、Julie）也照此括注。名人也照常括注；孙子这样的中国古人和耶稣基督这样的宗教人物不括注（见“全书统一的写法（译完后定）”）。作者自己写“克里斯·沃斯”，不括注。
- **机构、产品、地名**：见下面“机构、产品与地名”。没有通行中文名的公司和产品照写原名，和汉字之间加空格。
- **书名、报刊、电影、报告**：正文里用《》，每章第一次出现时括注原题，原题用斜体，例如《谈判力》（*Getting to Yes*）；报告、文章的原题保留引号，不用斜体。《纽约时报》《华盛顿邮报》、CNN 这些常见媒体不括注。书名和影片的译法见“书名与影片”。
- **数字**：一到十，以及带“几、十几、数百、上千”的约数，用汉字（三个小时、十几年）；11 以上的确数用阿拉伯数字（144 名学生、27 楼）；年份、日期、钟点、金额、百分比一律用阿拉伯数字（1993 年 9 月 30 日、上午 8 点半、65%），表示“完全”的口语说法“百分之百”除外。数字和汉字之间加空格。补充规定见“全书统一的写法（译完后定）”。
- **金额**：整数的大额换算成万、亿：$150,000 写“15 万美元”，$10 million 写“1000 万美元”，$100 billion 写“1000 亿美元”。带零头的精确数（1 万以上、个位或十位不是 0 的数）照写阿拉伯数字，不换算，千位不加逗号，以免丢掉作者强调的“零头”效果：$4,751 写“4751 美元”，$37,263 写“37263 美元”，€15,321.37 写“15321.37 欧元”。$1.99 和 $2.00 照写“1.99 美元”“2.00 美元”。
- **单位**：英制单位照原文，必要时括注公制，例如“6 英尺 2 英寸、250 磅（约 1.88 米、113 公斤）”“华氏 70 度（约 21 摄氏度）”。
- **对话、脚本和粗话**：人质谈判的对话、电话和邮件按原文的语气译，口语就译成口语；Holy shit、asshole、bullshit 这类粗话保留力度。第 4 章的筹款电话脚本保留“筹款人：”“史密斯先生：”这样的说话人标记。
- **回译**：原文用英语转述的中文典故，回到中文原文：Sun Tzu 的 the supreme art of war: to subdue the enemy without fighting 写“不战而屈人之兵，善之善者也”；第 5 章的 Sleeping in the same bed and dreaming different dreams 写“同床异梦”。
- **斜体强调**：原文用斜体强调的词（*why*、*how*、*not*），中文在对应的词上保留斜体；书名的斜体改成书名号。整段斜体的邮件保留斜体。
- **注释**：这个 EPUB 没有脚注，也没有书末注释。需要说明的地方写译者注 `[^t1]:`，在正文里引用。
- **破折号和句式**：中文译文不用破折号（——），原文的破折号按意思改成逗号、冒号、括号或另起一句；也不用“不是……而是……”这种句式，换成直接的说法。全书已经译完的部分都遵守这一条。

## 各节标题

| 章节 id | 英文 | 中文标题（`#` 一级标题照这一列写） | 副标题（标题下的斜体段落） |
| --- | --- | --- | --- |
| ch01 | 1. The New Rules | 第 1 章 新规则 | 怎样成为最聪明的人……不管在哪个房间里 |
| ch02 | 2. Be a Mirror | 第 2 章 做一面镜子 | 怎样迅速建立融洽关系 |
| ch03 | 3. Don’t Feel Their Pain, Label It | 第 3 章 别去感受对方的痛苦，把它标注出来 | 怎样用战术共情建立信任 |
| ch04 | 4. Beware “Yes”—Master “No” | 第 4 章 当心“是”，掌握“不” | 怎样推动谈判，让对方放心说出真正的利害 |
| ch05 | 5. Trigger the Two Words That Immediately Transform Any Negotiation | 第 5 章 让对方说出那两个立刻扭转谈判的字 | 怎样获得说服对方的许可 |
| ch06 | 6. Bend Their Reality | 第 6 章 扭转对方眼中的现实 | 怎样塑造“公平” |
| ch07 | 7. Create the Illusion of Control | 第 7 章 营造掌控的错觉 | 怎样校准问题，化冲突为合作 |
| ch08 | 8. Guarantee Execution | 第 8 章 确保执行 | 怎样识破说谎者，让其他人都说到做到 |
| ch09 | 9. Bargain Hard | 第 9 章 强硬议价 | 怎样拿到你要的价格 |
| ch10 | 10. Find the Black Swan | 第 10 章 找到黑天鹅 | 怎样揭开未知的未知，取得突破 |

中文版的章名（豆瓣只列出前六章）：第一章 新规则；第二章 重复对方的话；第三章 体会他人痛苦，不如把他们的痛苦“标注”出来；第四章 小心“是”，掌控“不”；第五章 得到一句话，瞬间改变谈判；第六章 扭转现实。第 5 章的 the two words 指 “That’s right”，这里译作“没错”，正好两个字，所以标题写“那两个字”。

各章的小节标题在 [review/terms/headings.tsv](review/terms/headings.tsv)，译者按下面的术语自己译；第 2 到 10 章末的 Key Lessons 一律写“本章要点”。译者读完一章后，如果觉得标题另有更贴切的译法，在汇报里提出，由主会话统一修改。

## 全书统一的写法

下面几条是译前定的。各章译完后补充的写法，见下一节“全书统一的写法（译完后定）”。

- **人名的简称**：一个人在章内第二次出现时，原文只写名的写名，只写姓的写姓，例如 Amy 写“埃米”，Mnookin 写“姆努金”。和作者同名的克里斯·沃茨，第二次出现以后写“沃茨”；只写 Chris 的地方（第 2 章博比说的 Where’s Chris?）写“克里斯”，读者能从上下文分清。第 8 章的 Jesus（赫苏斯·布埃诺）不要写成“耶稣”。
- **头衔**：lead international kidnapping negotiator 写“首席国际绑架案谈判专家”；Supervisory Special Agent 写“监督特工”；FBI director 写“联邦调查局局长”；FBI agent 写“FBI 特工”，agents 写“特工”；deputy attorney general 写“司法部副部长”；secretary of state 写“国务卿”；lieutenant（纽约警察局）写“副队长”。
- **代词**：作者泛指谈判者时 he、she、they 交替使用，中文写“对方”“谈判者”或“他”，不刻意跟着原文换性别。
- **章号**：原文的 Chapter 9 写“第 9 章”。第 1 章 The Book 一节说第 4 章讲“没错”和总结、第 5 章讲“不”，实际正好相反；第 3 章说身体语言“在第 9 章细讲”，实际在第 8 章；第 8 章 As we discussed in Chapter 5，三种“是”其实在第 4 章；第 9 章 the FM DJ Voice I talked about in Chapter 3：这种语调的特点在第 2 章讲解，第 3 章开头哈莱姆那起案子里作者用过这种语调，但没有讲它的特点（第 9 章 `[^t1]` 照这个意思写）。这些地方正文照原文译，在后面加译者注说明实际的章号。
- **原文前后不一的清单**：第 2 章说 It’s just four simple steps，列了五步；第 9 章说阿克曼模型 has only four steps，列了六步。照原文译，加译者注说明。
- **其他原文疑点**（记在 [review/source.md](review/source.md)）：第 9 章的 complementary PDF 按 complimentary 的意思写“免费的 PDF”；第 4 章脚本少了句号、少了 to 的地方，中文照通顺的句子写，不加注。
- **“是”“不”“没错”**：作者把 “Yes”“No”“That’s right” 当作概念讨论的地方，中文加引号写“是”“不”“没错”；“没错”只用来译 That’s right，别处的 right、exactly、sure 写“对”“确实”“当然”，以免读者把普通的附和当成作者说的那两个字。
- **网址**：http://info.blackswanltd.com/3-types 照写。

## 全书统一的写法（译完后定）

各章译完后，编辑提出了一些各章写法不一、或者体例没有说清的地方，统一如下。块号按 `tools/term_consistency.py` 的编号；写着“已改”的地方，zh-cn 里已经改好。

- **小节标题**：各章 zh-cn 里现在的小节标题全部确认，照现在的写法定稿，例如第 2 章“让精神分裂的人平静下来”“慢。下。来。”“声音”，第 3 章“在订满的航班上拿到座位，再顺便升个舱”，第 7 章“怎样*拿不到*钱”。The 7-38-55 Percent Rule 照术语表写“7-38-55 法则”，Percent 不译。
- **数字**：
  - 原文的 decades 不带约数词时写阿拉伯数字（two decades 写“20 年”）；带 more than 的写“二十多年”“三十多年”；泛指的 decades 写“几十年”；a decade of 写“十年来”。
  - 第 5 章萨巴亚说的 five hundred years（第 28、31、48 块）按确数写“500 年”，三处一致，不改成“五百年”。
  - 100 percent 表示“完全”的口语说法，写“百分之百”（with us 100 percent 写“百分之百站在我们这边”）；概率、比例和出价里的百分比照写“100%”（第 1 章第 103 块，第 6 章第 111 块，第 9 章的 65%、85%、95%、100%，第 10 章第 219、220 块的入住率）。要改的三处：第 6 章第 54 块“100% 不理性”，第 8 章第 27 块“100% 站在我们这边”，第 8 章第 82 块“100% 支持”。
  - 折扣照写百分比：ten percent 写“便宜 10%”，不换成“打九折”（第 8 章第 162 块）。
- **金额**：1 万以上的数，只要个位和十位都是 0，就照“整数的大额”换算成万：$134.5k 写“13.45 万美元”，$143k 写“14.3 万美元”，$127,000 写“12.7 万美元”，$32,500 写“3.25 万美元”。照写全部阿拉伯数字的，是作者当作“不整的数”来用的精确数，个位或十位不是 0：37263 美元、37893 美元、30812 欧元、28346 欧元、23567 欧元、15321.37 欧元。1 万以下的数照写阿拉伯数字（4751 美元、9499 美元、1829 美元）。要改的一处：第 8 章第 36 块“16500 美元”写成“1.65 万美元”。
- **句式**：“与其说……不如说……”“并不在于……而在于……”和“不是……而是……”同属体例禁用的对比句式，改成直接的说法。第 3 章第 128 块、第 6 章第 95 块已经改过。还要改的四处：第 2 章第 35 块（这与其说是投降计划，不如说是逃跑计划）、第 8 章第 69 块（与其说是靠我们高明的策略，不如说是碰上了好运气）、第 10 章第 59 块（谈判与其说是跟对手比赛，不如说更像走钢丝）、第 10 章第 181 块（他最主要的利益，并不在于谈一笔用人质换钱的交易）。
- **译者注和原文的史实错误**：保留现有四条纠正史实的译者注：第 1 章 `[^t1]`（阿蒂卡的死者）和 `[^t3]`（特沃斯基和卡尼曼的任职学校），第 7 章 `[^t2]`（萨巴亚死的时间），第 10 章 `[^t2]`（复活和升天相隔 40 天）。标准是：书中叙述的具体史实（人数、日期、任职的机构、宗教常识）明显写错，读者会信以为真的，加译者注。研究出处有出入（第 2 章怀斯曼的服务员实验）、前后说法小有出入（第 2 章的 car 和 van，第 5 章本吉是军官还是警官）、排印错误，照原文译，不加注，记在 [review/source.md](review/source.md)。俗语和典故的意思下文已经讲清的（第 8 章 W. C. 菲尔兹那句话，第 9 章的 Golden Rule），也不加注。
- **人名**：
  - 中国古人回到汉字，不括注英文拼法：Sun Tzu 写“孙子”。耶稣基督、上帝这类宗教人物也不括注。已改：第 3 章第 45 块，第 10 章第 116 块。
  - 一个人在章内先只出现名、后面才出现全名时，名第一次出现时括注名，全名第一次出现时再括注全名，例如第 2 章第 117 块“多米尼克（Dominick）”、第 118 块“多米尼克·米西诺（Dominick Misino）”。同一个全名在章内再次出现时不再括注（第 10 章第 180 块的威廉·格里芬）。
  - 第 4 章电话脚本里第一次出现的人名照常括注：“奥巴马（Obama）总统”“史密斯先生（Mr. Smith）”。
  - Ben Ottenhoff 只写名时照人名表写“本”，句子要安排得不会读成“本来”的“本”，照第 4 章第 142、145 块现在的写法（“在我的课上，本读了……”“好在本这个人很聪明”“本的故事”）。
- **头衔和称呼**：
  - CEO 一律写“首席执行官”。已改：第 5 章第 116、117、120 块。
  - politician、political figure 写“政界人物”；原文带贬义或语境明显负面时写“政客”（第 3 章第 42 块围攻希拉里的 pundits and politicians，第 7 章第 45、61、63 块的 crooked、sleazy politician）。
  - 绑匪或对方指定的 negotiator 也写“谈判者”，政府任命的写“谈判代表”（第 7 章第 23 块的马来西亚参议员，第 6 章第 75 块的伊朗前核谈判代表）。已改：第 8 章第 29 块。
- **aggressive 和 assertive**：assertive 写“强势”（强势型、直接强势的语调）；aggressive 按上下文写“咄咄逼人”“气势汹汹”“凶”“强硬”，不写“强势”，读者才分得清这两种特质。已改：第 7 章第 104 块。
- **aloud**：label it aloud、speaking them aloud 写“说出来”“说出口”“开口”，不写“大声”。已改：第 1 章第 160 块。
- **diffuse / defuse**：diffuse 写“化解”；两个词对照出现时（第 3 章第 75 块），diffuse 写“冲淡”，defuse 写“拆掉……的引信”。defuse 单独出现时写“化解”（第 1 章第 160 块）或“拆掉……的引信”（第 3 章第 136 块）都可以。
- **强调**：原文用全大写强调的词，中文用粗体（第 3 章第 109 块“**您的**华盛顿红皮队”）。原文已经用文字说明是大字的（第 9 章 “YOU WIN” in big letters），照常写“你赢了”。
- **其他说法**：
  - moving beyond / go outside the negotiating table 写“走到谈判桌之外”“到谈判桌之外”，不用“走出谈判桌”；compare notes 写“交流一下各自听到了什么”（第 10 章）。
  - country clearance 写“国别许可”，第一次出现时括注英文（第 3 章）。
  - 成对出现的 presenting / underlying dynamic 写“外显的动因 / 潜在的动因”（第 3 章第 127 块）；单独出现的 underlying dynamic 按上下文写，例如第 7 章第 122 块“藏在背后的症结”。
  - anticipatory labels 写“抢先一步的标注”（第 3 章）。
  - well-being 和 safety、trust 并列时写“舒适感”，和“安全感”分开（第 3 章第 113、200 块）；人质的 well-being 写“安全”“平安无恙”。
  - work-for-hire 写“雇佣作品”，第 2 章第 60 块括注原文并加译者注；作者的原话 We don’t do work-for-hire 写“我们不做雇佣作品”。
  - 第 5 章：sting operation 写“诱捕行动”；Tagalog 写“他加禄语”；quarterback、lineman、linebacker 写“四分卫”“锋线球员”“线卫”；subtle epiphany 写“不易察觉的顿悟”；the world according to … 写“……眼中的世界”。
  - 作者叫好时说的 Bang! 写“漂亮！”，别写成拟声词“砰”（第 4 章第 128 块）；Bingo! 按上下文写“成了！”“就是它！”“中了！”。
  - 各章自己的写法选择（第 4 章“屁用没有”的力度、“听不到‘不’，就别往下谈”不押韵、“两个字母”的括注、“停顿”加引号，第 7 章第 15、107 块两个问句措辞略有不同，第 8 章第 70 块“人质生还情况询问”和第 107 块 When/What 的括注，第 10 章第 146 块 follow-ability 写“让人愿意追随你”），照各章现在的写法。

## 核心概念

### 谈判的基本说法

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| negotiation / negotiate / negotiator | 谈判 / 谈判 / 谈判者 | 书里的谈判泛指一方想从另一方得到东西的任何互动，日常对话也算；FBI 和警方的 negotiator 写“谈判专家”；绑匪或对方指定的 negotiator 也写“谈判者”，政府任命的写“谈判代表” | 协商、交涉 | ch01 | 537 | 初定 |
| counterpart | 对方 | 作者对谈判另一方的中性叫法；需要强调身份时写“谈判对方”；复数也写“对方” | 对手（adversary、opponent）、同行 | ch01 | 228 | 初定 |
| the other side / the other party | 对方 / 另一方 | 和 counterpart 同指 |  | ch01 | 87 | 初定 |
| adversary / opponent | 对手 | 带敌对意味；第 4 章吉姆·坎普用 adversary 指 counterpart（his word for counterpart），那里括注原文 | 对方（counterpart）、敌人（enemy） | ch01 | 22 | 初定 |
| hostage negotiation / hostage negotiator | 人质谈判 / 人质谈判专家 |  |  | ch01 | 32 | 初定 |
| lead international kidnapping negotiator | 首席国际绑架案谈判专家 | 作者在 FBI 的职务；第 8 章写作 lead international hostage negotiator，同样译 |  | ch01 | 4 | 初定 |
| hostage-taker / kidnapper | 劫持者 / 绑匪 | hostage-taker 是扣押人质的人；绑架案里的写“绑匪” |  | ch01 | 90 | 初定 |
| bad guys | 歹徒 | FBI 的口语说法，语气偏口语，也可写“坏人” |  | ch01 | 16 | 初定 |
| crisis negotiation / crisis intervention | 危机谈判 / 危机干预 |  |  | ch01 | 10 | 初定 |
| deal / deal making | 交易 / 达成交易 | 按上下文写“交易”“协议”“生意”；make a deal 写“谈成” |  | ch01 | 113 | 初定 |
| No deal is better than a bad deal | 没有交易也比坏交易好 | 作者反复说的口诀，全书一字不改 |  | ch06 | 3 | 初定 |
| win-win / win-lose / wimp-win deal | 双赢 / 一赢一输 / 认怂的“双赢” | wimp-win 拿 win-win 谐音，指没敢争取、把价值留在桌上的交易；第一次出现时括注原文 |  | ch01 | 9 | 初定 |
| compromise / split the difference | 妥协 / 折中 | split the difference 指各让一半、取中间数，例如 15 万美元的赎金出 7.5 万美元 | 让步（concession） | ch01 | 32 | 初定 |
| never split the difference | 绝不折中 | 原书书名，也是第 6 章的规则 |  | ch06 | 1 | 初定 |
| bargaining / haggling | 讨价还价 / 议价 | haggle 偏口语，写“讨价还价”；第 1 章 quid pro quo bargaining 写“你来我往的讨价还价” | 谈判（negotiation） | ch01 | 56 | 初定 |
| bare-knuckle bargaining | 硬碰硬的讨价还价 |  |  | ch09 | 6 | 初定 |
| brass tacks | 实打实的细节 | get down to the brass tacks 写“谈到实打实的价钱”；作者常加引号 |  | ch01 | 3 | 初定 |
| problem solving / problem solver | 解决问题 / 解决问题的人 | 《谈判力》一派以理性解决问题为核心；joint problem-solving 写“共同解决问题” |  | ch01 | 16 | 初定 |
| BATNA | 谈判协议的最佳替代方案（BATNA） | 第一次出现写全称再括注，之后写 BATNA；第 1 章 authoritative acronyms like BATNA and ZOPA 说的是缩写本身，那里先写缩写、再括注中文全称：“BATNA（谈判协议的最佳替代方案）和 ZOPA（可能达成协议的区间）这类听上去很权威的缩写” |  | ch01 | 2 | 初定 |
| ZOPA | 可能达成协议的区间（ZOPA） | 第 9 章的 Zone of Possible Agreement；第 1 章只出现缩写，写法见上一行 BATNA |  | ch01 | 4 | 初定 |
| implementation / execution | 执行 / 落实 | 第 8 章标题 Guarantee Execution 写“确保执行” |  | ch01 | 28 | 初定 |

### 倾听与共情

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| Tactical Empathy | 战术共情 | 全书的核心概念：理解对方此刻的感受和想法，听出感受背后的东西，并把这种理解说出来，借此扩大之后的影响力 | 战术同理心（中文版的译法）；同情（sympathy） | ch01 | 12 | 初定 |
| empathy / empathize / empathic | 共情 / 共情 / 共情的 | 作者的定义：认识到对方的视角，并把这种认识说出来；共情不等于同意对方 | 同理心、移情、同情 | ch01 | 60 | 初定 |
| sympathy | 同情 | 认同对方的价值观、给对方拥抱，作者用来和共情对照 | 共情 | ch03 | 3 | 初定 |
| forced empathy | 强制共情 | 第 8 章：用“我该怎么做到呢？”或报出自己的名字，让对方不得不从你的角度看问题 |  | ch08 | 2 | 初定 |
| emotional intelligence | 情商 | emotional intelligence on steroids 写“加强版的情商” | 情绪智力（学术译法，书里不用） | ch01 | 6 | 初定 |
| active listening | 积极倾听 | 心理咨询的通用译法；行为改变阶梯模型的第一阶段 | 主动聆听 | ch01 | 6 | 初定 |
| Behavioral Change Stairway Model (BCSM) | 行为改变阶梯模型（BCSM） | FBI 危机谈判小组的模型，五个阶段：积极倾听、共情、融洽关系、影响、行为改变；原文只写 the Behavioral Change Stairway、没有 Model 时，写“行为改变阶梯”（第 5 章第 12 块） |  | ch05 | 4 | 初定 |
| rapport | 融洽关系 | establish rapport 写“建立融洽关系”；口语处可写“关系拉近了” | 信任（trust） | ch01 | 20 | 初定 |
| unconditional positive regard | 无条件积极关注 | 卡尔·罗杰斯的概念，心理咨询的通用译法 |  | ch01 | 4 | 初定 |
| Late-Night FM DJ Voice | 深夜电台 DJ 的语调 | 低沉、柔和、缓慢、语调下沉的说话方式；DJ voice 简写“DJ 语调” | 深夜电台主持人的声音（中文版的译法） | ch01 | 14 | 初定 |
| positive/playful voice / direct or assertive voice | 积极轻快的语调 / 直接强势的语调 | 作者说的另外两种语调；积极轻快的是默认语调 |  | ch02 | 6 | 初定 |
| downward / upward inflection | 语调下沉 / 语调上扬 | downward-inflecting statement 写“语调下沉的陈述句” |  | ch02 | 10 | 初定 |
| mirroring / mirror | 镜像模仿 / 镜像 | 重复对方刚说的最后三个词（或最关键的一到三个词）；名词 a mirror 写“镜像”，动词 mirror 写“用镜像回应” | 照镜子；重复对方的话（中文版的译法） | ch01 | 53 | 初定 |
| isopraxism | 同步行为（isopraxism） | 镜像模仿的学名，第一次出现时括注 |  | ch02 | 1 | 初定 |
| labeling / label | 标注 | 给对方的情绪起个名字并说出来；名词 a label 写“一句标注”；mislabel 写“故意标错”；第 3 章标题的 Label It 写“把它标注出来”；anticipatory labels 写“抢先一步的标注”。第 10 章第 153 块 we label it in ways that allow us to dismiss it 是日常的贬义用法，写“贴个标签”“这个标签” | 贴标签（中文含贬义）、标签化；这一栏只针对作者讲的标注技巧 | ch01 | 97 | 初定 |
| It seems like … / It sounds like … / It looks like … | 似乎…… / 听起来…… / 看起来…… | 标注的三种固定开头，全书统一；人物在普通对话里用 It seems like 标注时也写“似乎”，位置可以挪到句中，更像口语（第 1 章第 63 块、第 3 章第 175 块）；It seems 用作普通说法、不起标注作用时（第 3 章第 35 块 It seems like wizardry），按意思写“看起来”“好像” | 我听到……（I’m hearing that，作者说不要用） | ch01 | 40 | 初定 |
| accusation audit | 指责清单 | 把对方可能说你的最坏的话列出来，抢在对方之前说出口；做这件事写“列一份指责清单” | 指控审查、控告审计 | ch01 | 10 | 初定 |
| taking the sting out | 先拔刺 | 辩护律师在开场陈述里先把当事人的弱点都说出来 |  | ch03 | 1 | 初定 |
| presenting / underlying (behavior, emotion) | 外显的 / 潜在的 | 第 3 章：看得见的行为和驱动它的情绪；presenting behavior 写“外显行为”，underlying emotion 写“潜在情绪”；成对的 presenting / underlying dynamic 写“外显的动因 / 潜在的动因” |  | ch03 | 10 | 初定 |
| dynamic | 局面 / 互动 / 心理作用（按上下文） | 书里很常见，指双方之间正在形成的局面，或互惠这类心理作用，没有固定译法；negative dynamics 写“负面的局面”；第 8 章三次法则那句 whatever dynamic you’re trying to drill into，drill into 取 drill something into someone（反复灌输，让人记牢）的意思，写“反复强化的……心理作用” | 动力、动力学；drill into 不理解成“深入挖掘” | ch01 | 39 | 初定 |
| neural resonance | 神经共振 |  |  | ch03 | 3 | 初定 |
| words, music, and dance | 言辞、音乐和舞蹈 | 指话语、语调和肢体语言 |  | ch03 | 1 | 初定 |
| Effective Pauses / Minimal Encouragers | 有效停顿 / 简短鼓励语 | 第 5 章列出的积极倾听手段；鼓励语指“是”“好”“嗯”“我明白”这类短句 |  | ch05 | 2 | 初定 |
| paraphrase / paraphrasing | 转述 | 用自己的话把对方的意思说一遍 | 镜像（照原话重复） | ch01 | 5 | 初定 |
| summary / summarize | 总结 | 第 5 章：转述加标注就是总结 |  | ch01 | 21 | 初定 |
| “That’s right” | “没错” | 对方认可你对他的总结时说的话，作者说这是谈判里最动听的两个字；Assertive 型说的 that’s it exactly、you hit it on the head 写“完全正确”“说到点子上了” | “你说得对”（You’re right） | ch01 | 43 | 初定 |
| “You’re right” | “你说得对” | 敷衍、想让对方闭嘴时说的话 | “没错”（That’s right） | ch05 | 9 | 初定 |
| assumptions / hypotheses | 预设 / 假设 | 第 2 章 Assumptions Blind, Hypotheses Guide 写“预设让人盲目，假设为人引路” |  | ch01 | 23 | 初定 |
| state of schizophrenia / the voice in their head | 精神分裂状态 / 脑子里的声音 | 作者的比喻：谈判双方都只听自己脑子里的声音 |  | ch02 | 10 | 初定 |
| people mover | 能打动人的人 | 第 2 章和 problem solver（解决问题的人）对照 |  | ch02 | 1 | 初定 |
| vomiting information | 吐信息 | 作者咨询公司的说法：对方一股脑儿说出大量信息；第一次出现时加引号 |  | ch02 | 2 | 初定 |
| proof of life | 生存证明 | 证明人质还活着的证据；proof-of-life question 写“生存证明问题” |  | ch02 | 7 | 初定 |
| closer | 收尾谈判专家 | 第 2 章：被叫来敲定最后细节的人 |  | ch02 | 8 | 初定 |
| Making Shit Up (MSU) | 瞎编（MSU） | 第 2 章警方当时的谈判路子，括注缩写 |  | ch02 | 1 | 初定 |
| drive-bys | 路过式派活 | 第 2 章：上司顺路进门丢下一件急活 |  | ch02 | 2 | 初定 |
| “sixty seconds or she dies” | “60 秒，否则她就死” | 作者课上的破冰练习 |  | ch03 | 1 | 初定 |
| “Big Bad Prime” / prime contractor | “大坏总包” / 总承包商 | 第 3 章安娜的案例 |  | ch03 | 4 | 初定 |
| frequent callers / energy vampires | 常客来电者 / 能量吸血鬼 | 危机热线上天天打来的老来电者 |  | ch04 | 6 | 初定 |
| CareFronting / CareFrontation | 关怀式对质（CareFronting） | HelpLine 的叫法，把 care 和 confront 拼在一起；第一次出现时括注原文 |  | ch04 | 2 | 初定 |

### “是”与“不”

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| “Yes” / “No” (as words) | “是” / “不” | 作者把这两个词当作概念讨论时，加引号写“是”“不”；对话里的回答按语气写“是”“对”“好”“不”“不行”，但要看得出是肯定还是否定 |  | ch01 | 245 | 初定 |
| Counterfeit / Confirmation / Commitment “Yes” | 假意的“是” / 确认的“是” / 承诺的“是” | 第 4 章和第 8 章的三种“是” |  | ch04 | 11 | 初定 |
| “No”-oriented question / “Yes pattern” | 引出“不”的问题 / “是”模式 | 第 4 章：故意让对方回答“不”的问题，和一路逼对方说“是”的推销话术 |  | ch04 | 10 | 初定 |
| the right to veto | 否决权 | 吉姆·坎普的说法 |  | ch04 | 1 | 初定 |
| autonomy | 自主 / 自主权 | the need for autonomy 写“对自主的需要” |  | ch04 | 5 | 初定 |
| niceness | 友善 | 第 4 章：把友善当润滑剂和伪装；niceness ruse 写“友善的伪装” |  | ch04 | 5 | 初定 |
| “Is now a bad time to talk?” | “现在说话不方便吗？” | 引出“不”的范例句；对照的 Do you have a few minutes to talk? 写“你有几分钟时间吗？” |  | ch04 | 2 | 初定 |
| “Have you given up on this project?” | “你们已经放弃这个项目了吗？” | 第 4 章的一句话邮件；第 7、10 章的变体照这个句式写 |  | ch04 | 4 | 初定 |
| “Yes” is nothing without “How” | 没有“怎么做”，“是”就毫无意义 | 第 5 章和第 8 章的口诀 |  | ch01 | 6 | 初定 |
| “I’ll try” | “我试试” | 作者说这等于“我打算失败” |  | ch08 | 1 | 初定 |

### 校准式问题与执行

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| calibrated questions / calibrate | 校准式问题 / 校准 | 以“怎么”“什么”开头、没有固定答案的开放式问题，像校准枪的瞄具一样对准特定的问题 | 校准问题（可以理解，但全书统一写“校准式问题”） | ch01 | 70 | 初定 |
| open-ended / closed-ended questions | 开放式问题 / 封闭式问题 |  |  | ch01 | 14 | 初定 |
| “How am I supposed to do that?” | “我该怎么做到呢？” | 全书最常用的校准式问题，也是委婉说“不”的第一步；变体照“我该怎么……呢？”写，例如“我该怎么接受呢？”“我该怎么多付 200 美元呢？” | 你让我怎么办？ | ch01 | 22 | 初定 |
| “How” questions / How/No | “怎么”式问题 / 用“怎么”说“不” |  |  | ch01 | 15 | 初定 |
| “Why” questions | “为什么”式问题 | 作者说“为什么”在任何语言里都像指责 |  | ch07 | 7 | 初定 |
| illusion of control | 掌控的错觉 | 让对方以为自己掌控着局面；第 7 章标题写“营造掌控的错觉” | 控制错觉（心理学术语） | ch01 | 14 | 初定 |
| unbelief / suspend unbelief | 不信 / 放下不信 | 凯文·达顿的说法：对对方的话主动抵触、完全拒绝；暗用 suspend disbelief（姑且信之） | 怀疑（doubt） | ch07 | 8 | 初定 |
| showdown | 对峙 |  |  | ch07 | 7 | 初定 |
| hostage mentality | 人质心态 | 觉得局面不在自己掌控之中时的防御或反击（第 7 章第 133 块的写法），“失去控制”容易被读成情绪失控 |  | ch07 | 2 | 初定 |
| fight-or-flight / reptilian brain / limbic system / neocortex | 战斗或逃跑 / 爬行动物脑 / 边缘系统 / 新皮层 |  |  | ch07 | 7 | 初定 |
| reciprocity | 互惠 | norm of reciprocity 写“互惠规范” |  | ch02 | 13 | 初定 |
| behind the table / Level II players | 桌子后面的人 / 第二层级的参与者 | 不在谈判桌上，却能促成或阻挠执行的人 |  | ch07 | 7 | 初定 |
| deal makers / deal killers | 促成交易的人 / 搅黄交易的人 | deal breaker 也写“搅黄交易的人” |  | ch01 | 8 | 初定 |
| decision architects / decision makers | 决策架构师 / 决策者 |  |  | ch08 | 5 | 初定 |
| 7-38-55 Percent Rule | 7-38-55 法则 | 梅拉比安的研究：言辞占 7%，语调占 38%，肢体语言和表情占 55% |  | ch08 | 4 | 初定 |
| verbal / paraverbal / nonverbal / body language | 言语 / 副语言 / 非言语 / 肢体语言 | paraverbal 原文括注 how it’s said，写“副语言（怎么说）” |  | ch01 | 26 | 初定 |
| Rule of Three | 三次法则 | 让对方在同一次谈话里三次认同同一件事 |  | ch08 | 5 | 初定 |
| Pinocchio Effect | 匹诺曹效应 | 说谎的人用词更多，像匹诺曹的鼻子一样越说越长 |  | ch08 | 4 | 初定 |
| pronouns | 代词 | 第 8 章：爱说“我”的人往往做不了主，多说“我们”“他们”的人更可能是决策者 |  | ch02 | 7 | 初定 |
| the Chris discount | 克里斯折扣 |  |  | ch08 | 3 | 初定 |
| bid against themselves | 自己跟自己压价 | 对方没等你还价就一再降低自己的要价 |  | ch01 | 10 | 初定 |
| “the art of letting someone else have your way” | “让别人照你的意思行事的艺术” |  |  | ch08 | 1 | 初定 |
| listener’s judo / psychological judo | 倾听者的柔道 / 心理柔道 | 借对方的力达到自己的目的 |  | ch06 | 4 | 初定 |

### 心理学与行为经济学

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| behavioral economics / rational actors | 行为经济学 / 理性行为者 |  |  | ch01 | 3 | 初定 |
| System 1 / System 2 | 系统 1 / 系统 2 | 卡尼曼的概念，照《思考，快与慢》中译本 |  | ch01 | 14 | 初定 |
| Cognitive Bias | 认知偏差 |  |  | ch01 | 2 | 初定 |
| Framing Effect / framing | 框架效应 / 框定 | frame a negotiation 写“为谈判设定框架” |  | ch01 | 13 | 初定 |
| Prospect Theory | 前景理论 |  |  | ch01 | 4 | 初定 |
| Certainty Effect | 确定性效应 |  |  | ch06 | 1 | 初定 |
| Loss Aversion | 损失厌恶 | aversion to loss 也写“损失厌恶” | 损失规避（也通行，全书统一写“损失厌恶”） | ch01 | 8 | 初定 |
| amygdala | 杏仁核 | 大脑里产生恐惧的部位 |  | ch03 | 8 | 初定 |
| Ultimatum Game / proposer / accepter | 最后通牒博弈 / 提议者 / 接受者 |  |  | ch06 | 19 | 初定 |
| winner’s curse / buyer’s remorse | 赢家诅咒 / 买家懊悔 |  |  | ch06 | 2 | 初定 |
| similarity principle / in-group | 相似性原则 / 内群体 |  |  | ch10 | 4 | 初定 |
| paradox of power | 权力悖论 | 越用力逼，对方越抗拒 |  | ch10 | 1 | 初定 |

### 期限、公平与锚定

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| deadline | 最后期限 / 期限 |  |  | ch01 | 42 | 初定 |
| fair / fairness / unfair | 公平 / 公平 / 不公平 |  |  | ch01 | 50 | 初定 |
| the F-word / F-bomb | “F 字” / 扔出 F 炸弹 | 英语里 F-word 通常指脏话 fuck，作者借来指 Fair；第一次出现写“那个 F 字：‘公平’（Fair）”，并加译者注说明双关 |  | ch06 | 8 | 初定 |
| anchor / anchoring / extreme anchor | 锚点 / 锚定 / 极端的锚点 | 名词写“锚点”，动词写“锚定”；set an extreme anchor 写“抛出一个极端的锚点” |  | ch01 | 44 | 初定 |
| “anchor and adjustment” effect | “锚定与调整”效应 |  |  | ch06 | 1 | 初定 |
| range / bolstering range | 区间 / 支撑区间 | bolstering range 指区间的下限就是你真正想要的数 |  | ch06 | 13 | 初定 |
| nonmonetary terms / pivot to terms | 非金钱条件 / 转向非金钱条件 | nonsalary terms 写“薪水以外的条件” | 非货币条件 | ch06 | 13 | 初定 |
| odd numbers / nonround numbers | 不整的数 / 带零头的数 | 指 37263 美元这种听起来经过计算的数 | 奇数 | ch06 | 8 | 初定 |
| pleasant persistence | 愉快地坚持 |  |  | ch06 | 3 | 初定 |
| unofficial mentor | 非正式的导师 |  |  | ch06 | 2 | 初定 |
| rainmaker | 呼风唤雨的人 | 能带来大客户、大生意的人；make it rain 写“去呼风唤雨吧” |  | ch06 | 3 | 初定 |

### 讨价还价

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| negotiation style / Analyst / Accommodator / Assertive | 谈判风格 / 分析型 / 迁就型 / 强势型 | 第 9 章的三种类型；指人时写“分析型的人”“迁就型的人”“强势型的人”；小写的 assertive 写“强势”；aggressive 按上下文写“咄咄逼人”“气势汹汹”“凶”“强硬”，不写“强势” | 包容型、果断型 | ch04 | 43 | 初定 |
| “I am normal” paradox | “我很正常”悖论 |  |  | ch09 | 1 | 初定 |
| Golden Rule / Black Swan rule | 黄金法则 / 黑天鹅法则 |  |  | ch09 | 2 | 初定 |
| taking a punch / punching back | 挨一拳 / 回击 |  |  | ch09 | 14 | 初定 |
| strategic umbrage | 策略性动怒 |  |  | ch09 | 4 | 初定 |
| “I” messages | “我”信息 | “我觉得……，因为……”这种以“我”开头、设定界限的说法 |  | ch09 | 2 | 初定 |
| no neediness / ready-to-walk mindset | 别显得非要不可 / 随时可以走人的心态 |  |  | ch09 | 3 | 初定 |
| tough love | 严厉的爱 |  |  | ch09 | 1 | 初定 |
| Ackerman model / Ackerman bargaining | 阿克曼模型 / 阿克曼议价法 | 第 1 章的 the Ackerman system 也写“阿克曼模型”；以目标价的 65%、85%、95%、100% 依次出价，最后报带零头的数，再加一件非金钱的东西 |  | ch01 | 11 | 初定 |
| target price / first offer / counteroffer | 目标价 / 首次出价 / 还价 |  |  | ch01 | 18 | 初定 |

### 黑天鹅与筹码

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| Black Swan | 黑天鹅 | 书中指谈判里那些一旦挖出来就会改变全局的未知信息，作者说每场谈判至少有三只；作者的公司也以此命名 |  | ch01 | 49 | 初定 |
| Black Swan theory | 黑天鹅理论 | 塔勒布的概念 |  | ch10 | 1 | 初定 |
| known knowns / known unknowns / unknown unknowns | 已知的已知 / 已知的未知 / 未知的未知 |  |  | ch10 | 15 | 初定 |
| leverage | 筹码 | 书中的定义：让对方蒙受损失或得不到好处的能力；动词 leverage 写“利用”；Black Swans are leverage multipliers 写“黑天鹅能让筹码成倍增加” | 杠杆、权力（power） | ch01 | 55 | 初定 |
| positive / negative / normative leverage | 正面筹码 / 负面筹码 / 规范筹码 | 能给对方想要的东西 / 能伤害对方 / 能用对方自己的规范说服他 |  | ch10 | 21 | 初定 |
| religion | 信仰 | 作者借来指对方的世界观和存在的理由，有时就是字面上的宗教；原文加引号的地方保留引号 | 宗教（只在字面意义上用） | ch10 | 17 | 初定 |
| worldview | 世界观 |  |  | ch01 | 9 | 初定 |
| reason for being | 存在的理由 |  |  | ch10 | 2 | 初定 |
| “They’re crazy!” | “他们疯了！” |  |  | ch10 | 4 | 初定 |
| ill-informed / constrained / other interests | 信息有误 / 有难处 / 另有利益 | 第 10 章：误以为对方疯了的三种情况；constraints 写“难处”或“限制” |  | ch01 | 15 | 初定 |
| face time | 面对面接触 | Get Face Time 写“争取面谈” |  | ch10 | 6 | 初定 |
| unguarded moments | 不设防的时刻 |  |  | ch08 | 4 | 初定 |
| backup listeners | 后备倾听者 |  |  | ch10 | 2 | 初定 |
| suicide by cop | 借警自杀 | 故意制造危机，逼警察开枪打死自己 |  | ch10 | 1 | 初定 |
| stewardship | 管家职分 | 基督教用语，指替上帝管理资源的责任 |  | ch10 | 2 | 初定 |
| Dawn of the Third Day | 第三天的黎明 |  |  | ch10 | 3 | 初定 |
| GIGO (Garbage In, Garbage Out) | 垃圾进，垃圾出（GIGO） |  |  | ch10 | 1 | 初定 |
| cap rate / cash cow / due diligence | 资本化率 / 摇钱树 / 尽职调查 |  |  | ch10 | 5 | 初定 |

### 全书结构

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| Key Lessons | 本章要点 | 第 2 到 10 章最后一节的标题 |  | ch02 | 9 | 初定 |
| Negotiation One Sheet | 谈判一页纸 | 第 1 章提到的附录，这个 EPUB 里没有 |  | ch01 | 1 | 初定 |

## 书名与影片

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| *Getting to Yes* | 《谈判力》 | 罗杰·费希尔、威廉·尤里著，中译本书名。作者拿书名的字面意思（达成“是”）玩文字游戏的地方（the getting to “Yes” in the title、the flip side of *Getting to Yes*），括注原题并加译者注 |
| *Bargaining with the Devil: When to Negotiate, When to Fight* | 《与魔鬼谈判：何时谈判，何时战斗》 | 罗伯特·姆努金著；没有查到中译本，自译 |
| *Thinking, Fast and Slow* | 《思考，快与慢》 | 中译本书名 |
| *Start with NO* | 《从“不”开始》 | 吉姆·坎普著；没有查到中译本，自译 |
| *You Can Negotiate Anything* | 《万事皆可谈判》 | 赫布·科恩著；没有查到中译本，自译 |
| *Descartes’ Error: Emotion, Reason, and the Human Brain* | 《笛卡尔的错误：情绪、理性与人脑》 | 安东尼奥·达马西奥著；主书名沿用中译本《笛卡尔的错误》，副题自译 |
| *How to Become a Rainmaker* | 《如何成为呼风唤雨的人》 | 杰弗里·福克斯著；有 2003 年的中译本，书名没有核实，自译 |
| *Split-Second Persuasion* | 《瞬间说服》 | 凯文·达顿著；自译 |
| *Negotiation Genius* | 《哈佛经典谈判术》 | 迪帕克·马尔霍特拉、马克斯·H. 巴泽曼著，中译本书名 |
| *Fooled by Randomness* / *The Black Swan* | 《随机漫步的傻瓜》/《黑天鹅》 | 塔勒布著，中译本书名 |
| *Gladiator* / *Aladdin* / *Double Indemnity* | 《角斗士》/《阿拉丁》/《双重赔偿》 | 电影 |
| *Downs v. United States* | 唐斯诉美国案 | 判例名，不加书名号 |
| “Lessons of Waco: Proposed Changes in Federal Law Enforcement” | 《韦科的教训：联邦执法的改革建议》 | 1993 年司法部的报告 |
| *New York Times* / *Washington Post* / CNN | 《纽约时报》/《华盛顿邮报》/ CNN | 不括注 |

## 机构、产品与地名

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| FBI / the Bureau | FBI / 联邦调查局 | 原文写 FBI 的照写 FBI；the Bureau 写“联邦调查局” |
| FBI Academy / Quantico | FBI 学院 / 匡蒂科 | 学院在弗吉尼亚州匡蒂科，书里常用 Quantico 代称 |
| Crisis Negotiation Unit (CNU) | 危机谈判小组（CNU） | 设在 FBI 学院 |
| Hostage Rescue Team (HRT) | 人质营救队（HRT） |  |
| Critical Incident Response Group (CIRG) | 重大事件应对小组（CIRG） | 1994 年成立；其中的 Crises Negotiation、Crises Management、Behavioral Sciences、Hostage Rescue 写“危机谈判、危机管理、行为科学和人质营救” |
| Crisis Negotiation Team / Crisis Negotiation Coordinator | 危机谈判组 / 危机谈判协调员 | FBI 纽约、匹兹堡分局的 |
| Joint Terrorism Task Force (JTTF) | 联合反恐特遣队（JTTF） |  |
| Negotiation Operation Center (NOC) | 谈判行动中心（NOC） |  |
| Supervisory Special Agent (SSA) | 监督特工（SSA） |  |
| SWAT / NYPD / TARU | 特警队（SWAT）/ 纽约市警察局（NYPD）/ 技术支援响应组（TARU） |  |
| CIA / State Department / U.S. Court of Appeals | 中央情报局 / 国务院 / 美国联邦上诉法院 |  |
| OGA (Other Government Agency) | 其他政府机构（OGA） | 美国政府和军方内部对中央情报局的代称；第 7 章第 35 块的正文和译者注 `[^t1]` |
| U.S. Park Police / 82nd Airborne | 美国公园警察 / 第 82 空降师 |  |
| The Black Swan Group | 黑天鹅集团 | 作者的咨询公司 |
| Harvard Law School / Harvard Business School | 哈佛法学院 / 哈佛商学院 |  |
| Harvard Negotiation Project / Harvard Negotiation Research Project / Winter Negotiation Course | 哈佛谈判项目 / 哈佛谈判研究项目 / 冬季谈判课程 |  |
| MIT / Tufts / Georgetown University / Princeton / University of Chicago | 麻省理工学院 / 塔夫茨大学 / 乔治城大学 / 普林斯顿大学 / 芝加哥大学 |  |
| UCLA / Haas School of Business / Columbia Business School / INSEAD | 加州大学洛杉矶分校 / 哈斯商学院 / 哥伦比亚商学院 / 欧洲工商管理学院 |  |
| HelpLine | HelpLine 危机热线 | 照写原名 |
| Abu Sayyaf / Al Qaeda / Muslim Brotherhood / Taliban / ISIS | 阿布沙耶夫 / 基地组织 / 穆斯林兄弟会 / 塔利班 / “伊斯兰国” | 阿布沙耶夫是菲律宾南部的伊斯兰武装组织 |
| Philippine National Police Special Action Force / Scout Rangers | 菲律宾国家警察特别行动部队 / 侦察游骑兵 |  |
| Chase Manhattan Bank / Security Trust Company | 大通曼哈顿银行 / 安全信托公司 |  |
| Girl Scouts | 女童子军 | Girl Scout cookies 写“女童子军饼干” |
| St. Thomas More prep school | 圣托马斯·莫尔预科学校 | 第 5 章，在康涅狄格州；St. Thomas More School 写“圣托马斯·莫尔学校” |
| 1993 World Trade Center bombing | 1993 年世贸中心爆炸案 | 第 5 章 |
| Washington Redskins / New York Giants / FedEx Field | 华盛顿红皮队 / 纽约巨人队 / 联邦快递球场 |  |
| Dallas Mavericks / Washington Wizards / Washington Capitals | 达拉斯独行侠队 / 华盛顿奇才队 / 华盛顿首都人队 | 独行侠队 2017 年以前中文多作“小牛队” |
| NFL / NFL Players Association (NFLPA) / NBA | NFL / NFL 球员工会 / NBA |  |
| UT / Ole Miss | 得克萨斯大学 / 密西西比大学 | 第 3 章的橄榄球比赛 |
| American Airlines / Economy Plus | 美国航空 / Economy Plus（加宽经济舱） |  |
| Toyota 4Runner / Coca-Cola / Disney / John Deere / eBay / iPhone / iPad | 丰田 4Runner / 可口可乐 / 迪士尼 / 约翰迪尔 / eBay / iPhone / iPad | Salsa Red Pearl 写“萨尔萨珍珠红” |
| Memphis Bar Association | 孟菲斯律师协会 |  |
| Israeli National Security Council / Israel Defense Forces (IDF) / Knesset | 以色列国家安全委员会 / 以色列国防军 / 以色列议会 |  |
| XYZ Committee / ABC Corp. / X Corp. | XYZ 委员会 / ABC 公司 / X 公司 | 化名，照写字母 |
| New York / Brooklyn / Harlem / Kansas City / Pittsburgh / Quantico, Virginia | 纽约 / 布鲁克林 / 哈莱姆 / 堪萨斯城 / 匹兹堡 / 弗吉尼亚州匡蒂科 |  |
| Waco / Ruby Ridge / Attica / Munich / Jacksonville / Nashville | 韦科 / 红宝石岭 / 阿蒂卡 / 慕尼黑 / 杰克逊维尔 / 纳什维尔 |  |
| Haiti / Port-au-Prince / Manila / Mindanao / Jolo Island / Dos Palmas | 海地 / 太子港 / 马尼拉 / 棉兰老岛 / 霍洛岛 / 多斯帕尔马斯 | 多斯帕尔马斯是私人潜水度假村 |
| Ecuador / Mira River / St. Martin Parish, Louisiana / Rochester / Charleston, King Street | 厄瓜多尔 / 米拉河 / 路易斯安那州圣马丁堂区 / 罗切斯特 / 查尔斯顿国王街 |  |
| National Mall / Washington Monument / Lincoln Memorial / Vietnam Veterans Memorial | 国家广场 / 华盛顿纪念碑 / 林肯纪念堂 / 越战老兵纪念碑 |  |
| Seoul / Istanbul / Dubai / Greenhills | 首尔 / 伊斯坦布尔 / 迪拜 / 绿山 | 绿山是马尼拉的购物中心 |
