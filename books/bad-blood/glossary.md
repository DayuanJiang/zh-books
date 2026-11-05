# 术语表

翻译前根据 `review/terms/` 里的统计数据裁定（来源和门槛见 [review/terms/README.md](review/terms/README.md)）。“出现次数”和“首次出现”由 `tools/term_stats.py` 按英文词形统计，不含脚注；按正则匹配，可能把同词根的普通用法也算进去，例如 reader 也会算上报纸的读者，tip 也会算上移液吸头（pipette tip）。状态都是“初定”，由 Claude 裁定，等用户确认；改动时要回查已经译完的章节。

## 体例

- **人名**：用 [review/terms/people-zh.tsv](review/terms/people-zh.tsv) 的译名。每节第一次出现时在中文名后括注英文原名，例如“亨利·莫斯利（Henry Mosley）”，之后只写中文。脚注里的人名照写原文。
- **名和姓**：原文只写名的照写名，只写姓的照写姓。第 1 到 18 章作者多用名称呼霍姆斯和巴尔瓦尼（Elizabeth 写“伊丽莎白”，Sunny 写“桑尼”）；第 19 章作者本人出场以后改用姓（Holmes 写“霍姆斯”，Balwani 写“巴尔瓦尼”）。中文跟着原文变，不统一成一种。同姓的人（霍姆斯一家、富兹一家、两位唐纳德·卢卡斯）按原文的写法区分，原文分不清时按上下文补全名。
- **化名**：作者说明里说一部分人用了化名。化名和真名一样音译，正文不加注。
- **第一人称**：第 19 章起作者以“我”出场，后面各章的“我”都指作者；致谢和尾声同样。
- **称谓和军衔**：Dr. 按身份写“医生”或“博士”，例如 Dr. Sundene 写“森迪恩医生”，Dr. J 写“J 博士”。LTC 和 Lieutenant Colonel 写“中校”，Colonel 写“上校”，General 写“将军”，admiral 写“海军上将”。
- **机构、产品、代号**：见下面“机构、产品与地名”。没有通行中文名的公司、产品和设备照写原名，和汉字之间加空格，例如“Theranos 的 Edison”。
- **书名、报刊、电影、歌曲、电视节目**：用《》，每节第一次出现时括注原题，原题用斜体，例如《回到未来》（*Back to the Future*）；文章和报道的标题保留引号，不用斜体。常见报刊不括注，见“全书统一的写法”。
- **数字**：年份、日期、百分比和多位数字用阿拉伯数字，和汉字之间加空格，例如“2006 年 11 月 17 日”“60 名员工”。金额换算成中文的万、亿：$9 billion 写“90 亿美元”，$165 million 写“1.65 亿美元”，$150,000 写“15 万美元”。英制单位照原文，必要时括注公制，例如“6 英尺 5 英寸（约 1.96 米）”。
- **引语、邮件和便笺**：邮件、短信、便笺、Glassdoor 评论和对话按原文的语气译，口语就译成口语，粗话保留力度。原文的 [sic] 写“[原文如此]”；原文的拼写错误不在中文里模仿，有 [sic] 的地方照样标出。第 18 章富兹便笺上的速记保留简短的笔记口吻。
- **信封和车牌**：第 21 章信封上的地址照写英文，只把 Via Hand Delivery 译成“专人递送”。巴尔瓦尼的车牌 DAZKPTL、VDIVICI 照写，原文已经解释了含义。
- **念错和拆开念的名字**：第 20 章泰勒把 Boies 念成 Boy-zee，第 23 章员工喊 Carrey-rou，中文保留原文的拼法，必要时加译者注说明。
- **斜体强调**：原文用斜体表示强调的词，中文保留斜体。序章里特意拼写出来并用斜体强调的 one hundred and sixty-five million dollars 写“*1.65 亿美元*”。
- **脚注**：开头粗体的是正文里被注释的词句，译成对应的中文，保留粗体和冒号，例如 `[^1]: **“伊丽莎白今天早上给我打了电话”：** Email with...`。后面的出处（作者、标题、刊名、日期、网址、页码、案号、Ibid.）保留英文原样；解释性的句子和描述出处的说法要翻译。常见格式：
  - Email with the subject line “RE: Observations” sent by Sunny Balwani to Diana Dupuy at 11:21 a.m. PST on March 4, 2010. → Sunny Balwani 于 2010 年 3 月 4 日太平洋时间上午 11:21 发给 Diana Dupuy 的邮件，主题为“RE: Observations”。
  - Email without a subject line sent by Richard Fuisz to me → Richard Fuisz 发给我的邮件，没有主题
  - Deposition of Lorraine Fuisz, 32. → Lorraine Fuisz 的取证证词，第 32 页。
  - deposition of Erika Cheung taken on March 7, 2017 → Erika Cheung 的取证证词，2017 年 3 月 7 日
  - Minutes of August 24, 2010, meeting between Walgreens and Theranos. → 沃尔格林和 Theranos 2010 年 8 月 24 日会议的纪要。
  - LinkedIn profile of Jay Rosan → Jay Rosan 的 LinkedIn 个人资料
  - Ibid. 和 Ibid., 49. 照写。
  - [inactive] → [已失效]
- **脚注标记**：`[^n]` 放在中文里对应词句的后面，编号与英文一致。
- **译者注**：作者说明第二段说出处写在书末的注释里，这里的注释已经改成各章的脚注，可以照原文译再加一条译者注说明。尾声写于 2018 年初，霍姆斯和巴尔瓦尼当时还没有被起诉，是否加译者注在翻译尾声时决定。
- **分隔线**：分隔线 `---` 只写在英文文件里。
- **破折号和句式**：中文译文不用破折号（——），原文的破折号按意思改成逗号、冒号、括号或另起一句；也不用“不是……而是……”这种句式，换成直接的说法。

## 各节标题

| 章节 id | 英文 | 中文标题（`#` 一级标题照这一列写） |
| --- | --- | --- |
| dedication | Dedication | 献辞 |
| authors-note | Author’s Note | 作者说明 |
| prologue | Prologue | 序章 |
| ch01 | 1. A Purposeful Life | 第 1 章 有意义的人生 |
| ch02 | 2. The Gluebot | 第 2 章 点胶机器人 |
| ch03 | 3. Apple Envy | 第 3 章 艳羡苹果 |
| ch04 | 4. Goodbye East Paly | 第 4 章 告别东帕洛 |
| ch05 | 5. The Childhood Neighbor | 第 5 章 儿时的邻居 |
| ch06 | 6. Sunny | 第 6 章 桑尼 |
| ch07 | 7. Dr. J | 第 7 章 J 博士 |
| ch08 | 8. The miniLab | 第 8 章 miniLab |
| ch09 | 9. The Wellness Play | 第 9 章 健康牌 |
| ch10 | 10. “Who Is LTC Shoemaker?” | 第 10 章 “舒梅克中校是谁？” |
| ch11 | 11. Lighting a Fuisz | 第 11 章 引爆富兹 |
| ch12 | 12. Ian Gibbons | 第 12 章 伊恩·吉本斯 |
| ch13 | 13. Chiat\Day | 第 13 章 Chiat\Day |
| ch14 | 14. Going Live | 第 14 章 上线 |
| ch15 | 15. Unicorn | 第 15 章 独角兽 |
| ch16 | 16. The Grandson | 第 16 章 孙子 |
| ch17 | 17. Fame | 第 17 章 成名 |
| ch18 | 18. The Hippocratic Oath | 第 18 章 希波克拉底誓言 |
| ch19 | 19. The Tip | 第 19 章 线报 |
| ch20 | 20. The Ambush | 第 20 章 伏击 |
| ch21 | 21. Trade Secrets | 第 21 章 商业秘密 |
| ch22 | 22. La Mattanza | 第 22 章 屠鱼仪式 |
| ch23 | 23. Damage Control | 第 23 章 危机公关 |
| ch24 | 24. The Empress Has No Clothes | 第 24 章 女皇的新衣 |
| epilogue | Epilogue | 尾声 |
| acknowledgments | Acknowledgments | 致谢 |
| about-the-author | About the Author | 关于作者 |

几个标题的考虑：

- 第 1 章的 purposeful 出自霍姆斯接受《纽约客》采访时的话（spend their lives on something purposeful），正文那句话里的译法要和标题呼应。
- 第 4 章的 East Paly 是唐·卢卡斯对东帕洛阿尔托的轻蔑叫法，正文写“东帕洛”，第一次出现时说明是东帕洛阿尔托。
- 第 9 章的 play 指西夫韦押在健康业务上的一步棋，所以写“健康牌”。
- 第 11 章是 lighting a fuse（点燃导火索）的谐音双关，中文用“引爆”保留点火的意思和富兹的名字。
- 第 22 章的 la mattanza 是西西里渔民静候多时、再突然围杀鱼群的古老仪式，西科诺尔菲用它比喻耐心准备、一击发稿；正文照写意大利语 la mattanza，第一次出现时说明。
- 第 24 章套用《皇帝的新衣》，皇帝换成了女皇。

成起宏的中译本（北京联合出版公司 2019 年版，上海译文出版社 2025 年新版）的章名只作参考，上面的标题是按正文自己译的。译者读完一章后，如果觉得标题另有更贴切的译法，在汇报里提出，由主会话统一修改。

## 全书统一的写法

从《AI 帝国》（`books/empire-of-ai`）译完后定下的写法里，挑出适用于这本书的几条，翻译前先定下来：

- **数字**：一到十，以及带“几、十几、数百、上千”的约数，用汉字（两天后、十天后、几十名员工）；11 以上的确数用阿拉伯数字（150 多人、24 小时）；万和亿前面的数字也用阿拉伯数字（1.5 万名员工、90 亿美元）；年份、日期、钟点、金额、百分比一律用阿拉伯数字（下午 5 点、凌晨 3 点）。倍数写“增长到原来的 N 倍”，不写“增长了 N 倍”。
- **书名、报刊括注**：每节第一次出现时括注原题，原题用斜体，例如《史蒂夫·乔布斯传》（*Steve Jobs*）；文章、论文、博客文章的原题保留引号，不用斜体。《华尔街日报》《纽约时报》《华盛顿邮报》《纽约客》《财富》《福布斯》《连线》《时代》《金融时报》《今日美国》这些常见报刊不括注。
- **人名**：名人也照常在每节第一次出现时括注英文。脚注里的人名，无论在出处里还是在说明句里，一律照写英文。“卡特政府”“克林顿政府”“里根政府”这类说法不括注。
- **平台名**：Facebook、LinkedIn、Yelp、Glassdoor、Gmail、Craigslist、TechCrunch 照写原名。
- **头衔**：CEO 和 chief executive 写“首席执行官”，president 写“总裁”，chief operating officer 写“首席运营官”，chief financial officer 写“首席财务官”，chief scientific officer 写“首席科学官”，chief medical officer 写“首席医疗官”，general counsel 写“总法律顾问”，chairman 写“董事长”（政府委员会的 chairman 写“主席”），vice president 写“副总裁”，senior vice president 写“高级副总裁”，executive vice president 写“执行副总裁”。secretary of state 写“国务卿”，secretary of defense 写“国防部长”，Senate majority leader 写“参议院多数党领袖”。
- **公司的写法**：Theranos 照写，不写“希拉洛斯”；“Theranos 的”“Theranos 公司”按语感选用。Walgreens 写“沃尔格林”，Safeway 写“西夫韦”。

## 核心概念

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| Edison / Edisons | Edison | Theranos 第一代自有检测设备，由点胶机器人改造而来，只能做免疫测定；名字取自“美国最伟大的发明家”；复数也写 Edison（“几台 Edison”） | 发明家爱迪生（正文没有点他的名） | ch02 | 97 | 初定 |
| miniLab | miniLab | 第二代设备，想把几大类检测装进一台机器，从未在实验室里用于患者样本；第一次出现时括注“迷你实验室” | 普通的“小型实验室” | ch08 | 55 | 初定 |
| 4S | 4S | miniLab 的内部代号，取自 iPhone 4S |  | ch08 | 11 | 初定 |
| Theranos 1.0 | Theranos 1.0 | 最早的原型：卡盒加读取器，靠微流控 |  | prologue | 10 | 初定 |
| gluebot / glue robot | 点胶机器人 | 纽金特买来改造成 Edison 的点胶机器人；gluebot 是员工的戏称，第 2 章章名 |  | ch02 | 5 | 初定 |
| nanotainer | nanotainer（微型采血管） | Theranos 装指尖血的微型采血管，霍姆斯起的名字；每节第一次出现时括注 | 普通采血管 | ch13 | 21 | 初定 |
| cartridge | 卡盒 | 插进读取器的一次性检测卡盒，里面有试剂和微流控通道 | 试剂盒（kit）、墨盒 | prologue | 45 | 初定 |
| reader | 读取器 | 烤面包机大小的盒子，读取卡盒里的信号，再无线传给服务器 | 报纸的读者 | prologue | 40 | 初定 |
| TheraPatch / patch | 贴片 | 霍姆斯最初的构想：贴在皮肤上测血并自动给药的贴片；TheraPatch 照写 |  | ch01 | 11 | 初定 |
| six-blade | “六刀片”机 | 六台 miniLab 上下叠放、共用一台细胞仪的拼凑机器，用来提高通量；blade 借自刀片服务器 |  | ch14 | 2 | 初定 |
| wellness center | 健康中心 | Theranos 在西夫韦、沃尔格林店内开的采血点，Theranos 规定要叫这个名字 | 诊所（clinic） | ch09 | 14 | 初定 |
| Project T-Rex / Project Beta / Project Stanford | “霸王龙计划” / “贝塔计划” / “斯坦福计划” | 西夫韦、沃尔格林、Chiat\Day 内部对 Theranos 合作项目的代号 |  | ch07 | 6 | 初定 |
| Frat Pack / Therabros | “兄弟会帮” / “Thera 兄弟” | 克里斯蒂安·霍姆斯和他在杜克大学的兄弟会兄弟；Therabros 是 Chiat\Day 员工对其中三人的叫法 |  | ch08 | 9 | 初定 |
| Jurassic Park / Normandy | “侏罗纪公园” / “诺曼底” | 实验室两个房间的绰号：楼上的“侏罗纪公园”放商用分析仪，是取得 CLIA 资质的部分；楼下的“诺曼底”放 Theranos 自己的设备，后来 Edison 就摆在这里 |  | ch14 | 16 | 初定 |
| Eagle One / Eagle Two | “一号鹰” / “二号鹰” | 保镖给霍姆斯和巴尔瓦尼起的代号 |  | ch17 | 2 | 初定 |
| extra-ordinary | *非*凡 | 霍姆斯在邮件里把 extra 写成斜体再加连字符来强调；中文写“*非*凡”，只把“非”字设成斜体。序章原文紧接着说明 extra 的斜体和连字符，所以这里在后面括注英文原词，写成“*非*凡”（*extra*-ordinary） |  | prologue | 1 | 初定 |
| blood test / blood testing | 血液检测 | 全书最常用的说法；lab test 写“化验”或“实验室检测” | 验血（只在口语对话里用） | prologue | 125 | 初定 |
| test result | 检测结果 |  |  | prologue | 38 | 初定 |
| finger-stick / fingerstick | 指尖采血 | finger-stick sample 写“指尖血样本”，finger-stick test 写“指尖血检测”，prick a finger 写“扎手指” | 静脉采血 | ch04 | 45 | 初定 |
| venous draw / venipuncture | 静脉采血 | 用针从手臂静脉抽血 |  | ch07 | 14 | 初定 |
| lab / laboratory | 实验室 | 研发实验室和临床实验室都写“实验室”，需要区分时加限定 | 化验室 | prologue | 296 | 初定 |
| clinical lab / CLIA lab | 临床实验室 / CLIA 实验室 | Theranos 依照 CLIA 取得资质、检测患者样本的实验室 | 研发实验室 | ch07 | 21 | 初定 |
| lab director / laboratory director | 实验室主任 | CLIA 证书上署名、对检测结果负责的人 |  | ch09 | 11 | 初定 |
| assay | 检测 / 检测方法 | 书中解释 assay 和 blood test 同义；按上下文写“检测”或“检测方法”；assay validation 写“检测方法验证” | 化验单 | ch02 | 26 | 初定 |
| immunoassay | 免疫测定 | chemiluminescent immunoassay 写“化学发光免疫测定”；immunoassay group 写“免疫测定组” | 免疫疗法 | ch02 | 21 | 初定 |
| general chemistry | 常规生化检测 | 钾、钠、葡萄糖、胆固醇等电解质和代谢指标；chem 18 panel 写“18 项生化组合” |  | ch12 | 7 | 初定 |
| analyzer | 分析仪 | commercial analyzer 写“商用分析仪” |  | ch08 | 38 | 初定 |
| Siemens ADVIA | 西门子 ADVIA 分析仪 | Theranos 改装后用来测稀释过的指尖血样本的商用分析仪；ADVIA 1800 照写型号 |  | ch14 | 12 | 初定 |
| spectrophotometer / cytometer | 分光光度计 / 细胞仪 | miniLab 里装的检测部件；photomultiplier tube 写“光电倍增管” |  | ch08 | 9 | 初定 |
| pipette | 移液器 | pipette tip 写“移液吸头”；liquid handler 写“液体处理工作站” |  | ch02 | 18 | 初定 |
| microfluidics | 微流控 | 在芯片上的微小通道里移动微量液体的技术 |  | ch01 | 13 | 初定 |
| dilute / dilution | 稀释 | Theranos 把指尖血稀释后再上商用分析仪，是全书的关键做法之一 |  | ch02 | 39 | 初定 |
| reagent / antibody | 试剂 / 抗体 |  |  | ch01 | 15 | 初定 |
| proficiency testing | 能力验证 | 临床实验室一年三次的外部考核，第 16 章开始反复出现；第一次出现时可说明 | 能力测试、水平测验 | ch16 | 34 | 初定 |
| quality control | 质控 | quality-control check 写“质控检查”，quality-control failure 写“质控失败” |  | ch09 | 20 | 初定 |
| validation | 验证 | validation phase 写“验证期”，validation study 写“验证研究”，validation report 写“验证报告” |  | ch04 | 22 | 初定 |
| coefficient of variation (CV) | 变异系数（CV） | 衡量检测结果离散程度的指标；第一次出现写全称再括注 CV | 简历（Tyler’s CV 里的 CV） | ch16 | 11 | 初定 |
| sensitivity / equivocal zone | 灵敏度 / 灰区 | 第 16 章梅毒检测的数据；equivocal zone 是结果既不算阳性也不算阴性的区间 |  | ch16 | 9 | 初定 |
| reference range / normal range | 参考范围 / 正常范围 |  |  | ch19 | 3 | 初定 |
| hemolysis | 溶血 | 红细胞破裂释放出钾，让钾的检测值偏高 |  | ch14 | 3 | 初定 |
| dead volume / throughput | 死体积 / 通量 | high throughput 写“高通量” |  | ch14 | 3 | 初定 |
| pathologist | 病理医生 | 美国临床实验室的主任通常由病理医生担任 | 病理学研究者 | ch07 | 7 | 初定 |
| clinical laboratory scientist (CLS) | 临床检验技师（CLS） | 经州政府认证、可以处理人体样本的检验人员；第一次出现写全称再括注 CLS | 科学家 | ch09 | 9 | 初定 |
| phlebotomist | 采血员 |  |  | ch09 | 7 | 初定 |
| lab associate | 实验室助理 | 埃丽卡·张这样在临床实验室工作的初级员工 |  | ch16 | 5 | 初定 |
| CLIA | CLIA | 《临床实验室改进修正案》（Clinical Laboratory Improvement Amendments），联邦法律；每节第一次出现写“《临床实验室改进修正案》（CLIA）”；CLIA certificate 和 CLIA license 写“CLIA 证书” |  | ch07 | 23 | 初定 |
| CMS | CMS | 美国联邦医疗保险和医疗补助服务中心（Centers for Medicare and Medicaid Services），监管临床实验室；每节第一次出现写全称再括注 CMS |  | ch07 | 33 | 初定 |
| FDA | FDA | 美国食品药品监督管理局；每节第一次出现写全称再括注 FDA |  | ch02 | 59 | 初定 |
| laboratory-developed test (LDT) | 实验室自建检测（LDT） | 实验室自己开发、只在本实验室使用的检测，处在 FDA 和 CMS 监管之间的灰色地带 |  | ch07 | 12 | 初定 |
| inspection / survey | 检查 | CMS 和州卫生部门对实验室的现场检查；inspector 写“检查员”，inspection report 写“检查报告” | 调查（investigation） | ch09 | 58 | 初定 |
| deficiencies / sanctions | 缺陷 / 处罚 | CMS 检查报告列出的问题和随后的处罚 |  | ch06 | 7 | 初定 |
| institutional review board (IRB) | 机构审查委员会（IRB） | 监督医学研究是否安全、合乎伦理的委员会 |  | ch10 | 6 | 初定 |
| Medicare / Medicaid | 联邦医疗保险 / 医疗补助 | 每节第一次出现括注英文 |  | ch07 | 15 | 初定 |
| startup | 创业公司 |  | 初创企业（不混用） | prologue | 53 | 初定 |
| founder / cofounder | 创始人 / 联合创始人 |  |  | prologue | 30 | 初定 |
| venture capitalist / venture capital | 风险投资人 / 风险投资 | venture capital firm 写“风投公司”，VC 照写或写“风投” |  | prologue | 27 | 初定 |
| funding round / Series B | 融资 / B 轮 | Series B round 写“B 轮融资” |  | prologue | 12 | 初定 |
| valuation | 估值 |  |  | prologue | 12 | 初定 |
| unicorn | 独角兽 | 风险投资人艾琳·李 2013 年造的词，指估值 10 亿美元以上的创业公司；第 15 章章名 |  | ch15 | 8 | 初定 |
| hockey-stick forecast | 曲棍球棒式预测 | 收入先停滞几年、再直线上升的预测 |  | prologue | 1 | 初定 |
| vaporware | 雾件 | 大张旗鼓地宣布、多年后才拿得出来甚至一直拿不出来的软件或硬件；尾声里有定义 |  | epilogue | 1 | 初定 |
| stealth mode | 隐身模式 | 创业公司对外不公开产品的阶段 |  | ch12 | 2 | 初定 |
| board / director | 董事会 / 董事 | board of counselors 写“顾问委员会”，board of fellows（哈佛医学院）写“理事会” |  | prologue | 92 | 初定 |
| general counsel | 总法律顾问 |  |  | ch02 | 7 | 初定 |
| pharmaceutical company / drugmaker | 制药公司 |  |  | prologue | 24 | 初定 |
| secrecy / silo | 保密 / 各自封闭的部门 | 霍姆斯管理 Theranos 的方式：部门之间互不通气，information split into silos 写“信息被隔断在各个部门里” |  | ch02 | 16 | 初定 |
| black turtleneck | 黑色高领毛衣 | 霍姆斯模仿乔布斯的打扮 |  | ch03 | 7 | 初定 |
| patent / patent interference | 专利 / 专利抵触程序 | interference 指两个申请人争夺同一发明优先权的程序 |  | ch01 | 80 | 初定 |
| trade secrets | 商业秘密 | 第 21 章章名；Theranos 用来威胁员工和消息来源的理由 | 商业机密（不混用） | ch02 | 19 | 初定 |
| confidentiality agreement / NDA | 保密协议 | nondisclosure agreement 也写“保密协议” |  | ch02 | 15 | 初定 |
| lawsuit / litigation | 诉讼 |  |  | ch02 | 41 | 初定 |
| deposition | 取证证词 | 庭审前在律师面前宣誓作证的记录；动词 depose 写“取证” | 罢免 | authors-note | 14 | 初定 |
| affidavit | 宣誓书 | 第 18、20 章 Theranos 要艾伦·比姆和泰勒签的文件 |  | ch18 | 13 | 初定 |
| anti-SLAPP | 反 SLAPP 动议 | SLAPP 指为压制公众参与而提起的诉讼；第一次出现时说明 |  | ch11 | 1 | 初定 |
| whistleblower | 吹哨人 |  | 告密者 | ch18 | 3 | 初定 |
| source (journalism) | 消息来源 | confidential source 写“匿名消息来源” | 出处（脚注的 source） | prologue | 44 | 初定 |
| on the record / deep background | 公开具名 / 深度背景 | on deep background 指只提供背景、不能引用也不能透露来源；off the record 写“不公开” |  | ch19 | 11 | 初定 |
| tip | 线报 | 第 19 章章名，指给记者的爆料 | 小费、移液吸头 | ch02 | 17 | 初定 |
| No surprises | “不搞突然袭击” | 《华尔街日报》的规矩：发稿前把要写的每一点告诉报道对象 |  | ch19 | 1 | 初定 |
| la mattanza | la mattanza（屠鱼仪式） | 西西里渔民静候多时再围杀鱼群的古老仪式；正文照写意大利语，第一次出现时说明 |  | ch22 | 5 | 初定 |
| Hippocratic Oath | 希波克拉底誓言 | 第 18 章章名 |  | ch18 | 2 | 初定 |
| the Journal | 《华尔街日报》 | 原文简称 the Journal 时也写全名 |  | ch05 | 76 | 初定 |
| Silicon Valley / the Valley | 硅谷 |  |  | prologue | 56 | 初定 |
| fraud | 欺诈 | 法律意义上的欺诈 | 骗局（只在口语里用） | ch05 | 9 | 初定 |
| H-1B visa | H-1B 签证 | 许多印度裔员工靠它留在美国，所以怕被解雇 |  | ch14 | 1 | 初定 |

## 检测项目和医学名词

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| potassium / sodium / calcium / glucose | 钾 / 钠 / 钙 / 葡萄糖（血糖） | 常规生化检测项目 |
| cholesterol / LDL cholesterol | 胆固醇 / 低密度脂蛋白胆固醇 | 原文解释 LDL 是“坏胆固醇” |
| vitamin D / vitamin B₁₂ | 维生素 D / 维生素 B₁₂ |  |
| PSA (prostate-specific antigen) | 前列腺特异性抗原（PSA） | 原文有定义 |
| TSH (thyroid-stimulating hormone) | 促甲状腺激素（TSH） |  |
| IgE | 免疫球蛋白 E（IgE） | allergen-specific IgE 写“过敏原特异性 IgE” |
| creatinine | 肌酐 |  |
| prothrombin time | 凝血酶原时间 |  |
| hemoglobin | 血红蛋白 |  |
| syphilis / herpes / hepatitis C / HIV | 梅毒 / 疱疹 / 丙型肝炎 / 艾滋病病毒（HIV） |  |
| swine flu / H1N1 | 猪流感 / H1N1 |  |
| SARS / Ebola / Zika | 非典（SARS） / 埃博拉 / 寨卡 |  |
| SEIR | SEIR 模型 | 易感、暴露、感染、康复四个阶段的传染病模型，原文有解释 |
| lancet / transfer pen | 采血针 / 转移笔 | 转移笔是把指尖血吸进卡盒的小注射器 |
| saline solution | 生理盐水 |  |
| qualitative / quantitative test | 定性检测 / 定量检测 |  |

## 机构、产品与地名

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| Theranos | 照写 Theranos | 成起宏译本作“希拉洛斯”，中文报道多保留英文 |
| Walgreens / Safeway | 沃尔格林 / 西夫韦 | 美国连锁药店和连锁超市 |
| Apple / Google / Facebook / Microsoft / Oracle / Intel / IBM / Panasonic / Logitech | 苹果 / 谷歌 / Facebook / 微软 / 甲骨文 / 英特尔 / IBM / 松下 / 罗技 |  |
| Uber / Spotify / Yahoo / Netscape / SpaceX / NASA | 优步 / Spotify / 雅虎 / 网景 / SpaceX / NASA |  |
| Novartis / Pfizer / Celgene / AstraZeneca / Johnson & Johnson / Centocor | 诺华 / 辉瑞 / 新基 / 阿斯利康 / 强生 / 森托科 | Centocor 是强生旗下公司 |
| Siemens / Abbott Laboratories / Roche / Beckman Coulter / Bio-Rad / Tecan | 西门子 / 雅培 / 罗氏 / 贝克曼库尔特 / 伯乐 / 帝肯 | 检测设备厂商 |
| DiaSorin / Cholestech / Abaxis / Piccolo Xpress / Fisnar / Ocean Optics / Biosite / Becton Dickinson | 照写原名 | 第 2 到 9 章提到的设备和厂商；Becton Dickinson 也作 BD |
| Quest Diagnostics / LabCorp / ARUP / Sonora Quest | 奎斯特诊断 / LabCorp / ARUP / Sonora Quest | 大型商业检验实验室；reference laboratory 写“第三方检验实验室” |
| Colaborate / Take Care Health Systems | 照写原名 | 亨特的咨询公司 / 沃尔格林旗下的诊所公司 |
| TBWA\Chiat\Day / Chiat\Day | 照写 Chiat\Day | 广告公司，第一次出现写“广告公司 TBWA\Chiat\Day” |
| DKC | 照写 DKC | 公关公司 |
| Partner Fund Management | 照写 Partner Fund Management | 对冲基金，简称 Partner Fund |
| Lucas Venture Group / RWI Ventures / ATA Ventures / MedVenture | 卢卡斯风投集团 / 照写原名 |  |
| Boies, Schiller & Flexner / Boies Schiller | 博伊斯·席勒律师事务所 | 每节第一次出现括注英文全名 |
| McDermott Will & Emery | 麦德莫特律师事务所 | 每节第一次出现括注英文全名 |
| Wilson Sonsini Goodrich & Rosati | 威尔逊·桑西尼律师事务所 |  |
| Skadden, Arps, Slate, Meagher & Flom | 世达律师事务所 |  |
| Gibson, Dunn & Crutcher | 吉布森·邓恩律师事务所 |  |
| Keker & Van Nest / Kendall Brill & Klieger / Banie & Ishimoto / Zuckerman Spaeder / Davis & Gilbert / Farella Braun + Martel / Antonelli, Terry, Stout & Kraus / Fletcher & Company | 照写原名 | 律师事务所和出版经纪公司 |
| Baxter International | 百特国际 |  |
| Fuisz Pharma / Fuisz Technologies | 照写原名 |  |
| CommerceBid.com / Commerce One / Lotus / Genomic Health | 照写原名 |  |
| Wells Fargo / Credit Suisse / Cox Enterprises / Walmart / Fiat Chrysler Automobiles / New England Patriots | 富国银行 / 瑞信 / 考克斯企业 / 沃尔玛 / 菲亚特克莱斯勒汽车公司 / 新英格兰爱国者队 |  |
| Dow Jones / News Corporation / Knopf | 道琼斯 / 新闻集团 / 克诺夫出版社 |  |
| The Wall Street Journal / The New York Times / The Washington Post / The New Yorker | 《华尔街日报》/《纽约时报》/《华盛顿邮报》/《纽约客》 |  |
| Fortune / Forbes / Wired / Time / Glamour / Inc. / Fast Company / USA Today / Financial Times / Bloomberg Businessweek / Chicago Tribune | 《财富》/《福布斯》/《连线》/《时代》/《魅力》/《Inc.》/《快公司》/《今日美国》/《金融时报》/《彭博商业周刊》/《芝加哥论坛报》 |  |
| CNBC / CNN / CBS / NBC / Fox News / Fox Business | 照写原名 | 电视台 |
| Mad Money / Today / Charlie Rose | 《疯狂金钱》/《今日秀》/《查理·罗斯秀》 | 电视节目 |
| Litigation Daily / American Lawyer Media / TechCrunch / Pathology Blawg | 照写原名 | 新闻简报、媒体和博客 |
| Hematology Reports | 《血液学报告》（*Hematology Reports*） | 医学期刊 |
| Stanford University / Stanford Hospital / Hoover Institution | 斯坦福大学 / 斯坦福医院 / 胡佛研究所 |  |
| Johns Hopkins / Cleveland Clinic / Mayo Clinic / MD Anderson Cancer Center / Weill Cornell Medical Center | 约翰斯·霍普金斯 / 克利夫兰医学中心 / 梅奥诊所 / MD 安德森癌症中心 / 威尔康奈尔医学中心 |  |
| UCSF / Harvard Medical School / Chinese University of Hong Kong / University of Washington | 加州大学旧金山分校 / 哈佛医学院 / 香港中文大学 / 华盛顿大学 |  |
| Duke / Georgia Tech / MIT / Yale / Cambridge / Princeton / Santa Clara University | 杜克大学 / 佐治亚理工学院 / 麻省理工学院 / 耶鲁大学 / 剑桥大学 / 普林斯顿大学 / 圣克拉拉大学 |  |
| U.S. Central Command (CENTCOM) / Pentagon / Fort Detrick | 美国中央司令部 / 五角大楼 / 德特里克堡 | CENTCOM 第一次出现写“美国中央司令部（CENTCOM）” |
| U.S. Army Medical Research Institute of Infectious Diseases | 美国陆军传染病医学研究所 |  |
| Justice Department / SEC / State Department | 司法部 / 证券交易委员会 / 国务院 | SEC 第一次出现写“美国证券交易委员会（SEC）” |
| New York State Department of Health / California Department of Public Health / Laboratory Field Services | 纽约州卫生厅 / 加州公共卫生厅 / 实验室现场服务处 |  |
| AACC / College of American Pathologists | 美国临床化学协会（AACC） / 美国病理学家协会 |  |
| Palo Alto / East Palo Alto / Menlo Park / Mountain View / Newark / Pleasanton | 帕洛阿尔托 / 东帕洛阿尔托 / 门洛帕克 / 山景城 / 纽瓦克 / 普莱森顿 | 纽瓦克指加州的纽瓦克 |
| Sand Hill Road / Hillview Avenue / Page Mill Road / East Meadow Circle | 沙丘路 / 希尔维尤大道 / 佩奇米尔路 / 东梅多环路 |  |
| Arizona / Phoenix / Scottsdale / Fountain Hills | 亚利桑那州 / 菲尼克斯 / 斯科茨代尔 / 芳廷希尔斯 |  |
| Old Facebook building | 原 Facebook 大楼 | Theranos 2012 年搬进的总部 |
