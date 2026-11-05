# 结语与速查表（conclusion）审校记录

全节 49 个块，原文没有注释，译文加了 1 条译者注（[^t1]）；中英逐块对应（`site.py status` 显示 49/49）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5）。
- 范围：全节 49 块，从章首到章末对照英文逐块检查漏译、增译、否定、条件、数字、谁做了什么、比较对象、术语义项、人名和格式。另外做了这几项：
  - 速查表里和正文重复的句子（`review/terms/repeats.tsv` 里标着 conclusion 的 62 条），逐条拿英文找到第 1、2、4、5、8 章译文里的对应块，比较中文，62 条全部一字不差。其中第 4 章的两句（“So, first off, thanks for agreeing to this interview…”“On a scale of 1 to 5…”）初稿是我自己译的，写完后第 4 章的译文出来了，改为照第 4 章的写法。
  - Key skills 一项列出的各章主题，和章标题、小节标题的译法对照：“避开坏数据”“轻松随意地聊”“给会面定调”（第 6 章小节“约见面并定调”）“客户细分”“会前准备和复盘”（第 8 章小节“会前准备”“复盘”）都一致。
  - 用阅读器的渲染库 markdown-it 渲染中英两个文件：斜体 1 处、加粗 11 处、有序列表 2 个、无序列表 17 个、列表项 85 个、引用块 1 个，两边相同，译文里没有露出的星号。“会面前、会面中和会面后的流程”下面三个连着的列表，中间那个照英文用 `*`，三个列表保持分开。
  - 运行 `tools/term_consistency.py`：本节没有缺少约定译法的块。
  - 全节没有破折号，也没有体例禁用的对比句式。原文的破折号都改成了冒号或逗号，例如速查表 Results of a good meeting 的三条，标签后面的破折号写成冒号（“事实：……”）；引文 “Hey, don’t even worry about it…” 写成“嘿，压根别放在心上，这种事我懂。”
- 发现并修改：
  - “After all, you’re putting it on the line to try and make their lives better.”：初稿“你把自己押了上去”读着别扭，putting it on the line 说的是冒着失去一切的风险，改为“毕竟，你豁出一切，努力让他们的生活变得更好”。
  - “Did anyone have family in the police?”：初稿“有没有谁的家人在警察局工作”，in the police 指在警队当差，范围比“在警察局工作”宽，改为“有没有谁家里有人当警察？”
  - “You aren’t sure why you’re having the meeting”：初稿“你说不清自己为什么要开这次会面”，“开会面”搭配不当，改为“你说不清这次会面是为了什么”。
  - 速查表 Vision 一条的 “half-sentence version of how you’re making the world better”：初稿“你要怎样让世界变得更好”，把现在进行时译成了将来，改为“用半句话说清你正在怎样让世界变得更好”。
  - 速查表 Pedestal 一条的 “show that they, in particular, can provide that help”：初稿“他们本人尤其能提供这种帮助”，“尤其能”读着不通，in particular 强调的是“偏偏是他们”，改为“让对方看到，这种帮助恰恰是他们能给的”。
  - “I work with a few other founders building educational curriculum”：初稿“创业教育课程”多出了原文没有的“创业”，改为“教学课程”。
- 几处译法的考虑：
  - Hack it 一节：小标题照术语表写“快刀斩乱麻”；“Cutting through it was a hack (ba-dum tish!)” 译“一刀砍断它，是一记巧招（咚咚锵！）”。中文“巧招”没有“砍”的意思，读者看不出作者为什么接一句“咚咚锵”，所以加了译者注 [^t1]，说明 hack 既指砍、劈，也指取巧的捷径。结尾 “hack through the knot” 照术语表译“一刀斩断这个结”。
  - “It’s not like he didn’t know their number.”：their 指警察，作者的笑话是谁都知道报警电话。译“他又不是不知道警察的电话号码”，把 their 说明白，笑点保留在正文里，没有加注。
  - “a trial session scheduled”：健身教练的语境，译“约好了一节试课”。术语表的“试用”指产品试用，这里不合用。
  - “geeking out” 出现两次，译“着了魔似的……琢磨”“全都来了劲，琢磨起……”，两处都用“琢磨”呼应。
  - “Eternity will forgive our earthly blunders.”：译“永恒会原谅我们在尘世犯下的错”，和第 8 章末尾的“永恒会原谅你的”呼应。
  - “If relevant” 在本节出现四次（正文一次，流程列表三次），都照第 8 章写“需要的话”。
  - “Collecting compliments instead of facts and commitments”：译“收集恭维，拿它们代替事实和承诺”，避开体例禁用的对比句式。
  - “Exposing your ego (aka The Pathos Problem)”：照术语表写“把自尊心亮出来（也叫悲情问题）”。
  - 速查表 Commitment 一条的 “such as meaningful amounts of time, reputational risk, or money”：这一条和第 5 章不完全相同（第 5 章是 time, reputation, or money），句式照第 5 章写，用词照本节原文：“比如相当多的时间、声誉风险或金钱”。
  - 符号一组的小标题 “Writing it down” 加 “signal symbols” 译“**记下来（信号符号）：**”；“The big prep question:” 译“**会前准备的那个大问题：**”。
  - “subscribe to the rss” 写“RSS”；Twitter 照术语表不写“推特”；网址、推特账号和邮箱的链接文字和链接地址都照原样。
- 人名：本节只有 Alexander 一人，第一次出现写“亚历山大（Alexander）”，后文 “the Great” 写“大帝”，和 `review/terms/people-zh.tsv` 一致。戈尔迪之结、哥斯达黎加、基辅、牛津大学、联合国照术语表。
- 数字：Twenty minutes later 写“20 分钟后”，1 to 5 写“1 到 5 分”，big 3 写“三个”，Chapters 1 & 3 写“（第 1 章和第 3 章）”，都照“全书统一的写法”。
- 未决：
  - 速查表 “Being too formal” 下的两句照第 4 章现在的译文写，五条“你没在争取承诺与推进的迹象”和“推进”一条照第 5 章现在的译文写，第 1、2、8 章的重复句也一样。这几章在审校中如果改了这些句子，这里要跟着改。“Being too formal” 下的第三句 “Let’s set up a meeting.” 只出现在速查表，译“我们约个时间见面吧。”
  - 请主会话确认几处译法：“谢谢！”（小标题 Thanks!）、“这一路很愉快”（It’s been fun.）、“去把事情做成吧”（Make it happen.）、“带课指南”（facilitation guides）、“万一你喜欢看列表呢”（Just in case you like lists.），以及 hack 双关是否保留译者注。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 速查表 Mistakes and symptoms 第 5 项的第三条 | …I need to be coding! | 这一条结尾缺右引号；中文照第 8 章补上右引号 |
| 速查表 Signs you aren’t pushing for commitment and advancement | Meetings which "went well"；They haven't given up anything of value | 这一组用直引号和直撇号，其他各组用弯引号；中文一律用“” |
| 速查表 | Being too formal 下多出 “Let’s set up a meeting.”，going through the motions 下多出 “You aren’t sure why you’re having the meeting”，Commitment 一条写 meaningful amounts of time, reputational risk | 和正文的对应列表不完全相同，原文如此，照本节原文译 |
| Thanks! 末段 | 链接文字是 aloha@foundercentric.com，链接地址是 mailto:mom@foundercentric.com | 两者不一致，照原样保留；这些网址和邮箱是 2013 年的，现在未必有效 |

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：全节 49 块和 1 条译者注，逐块对照英文读完，核对意义、漏译、增译、否定、数字、人名、术语和格式；速查表里和正文重复的 60 多条句子，用脚本找到第 1、2、4、5、8 章的对应中文逐条比较，全部一字不差；Key skills 一项和各章标题、小节标题对照，说法一致。
- 发现：7 条；编辑逐条找到英文和中文核实后，采纳 7 条，不采纳 0 条。其中 3 条照审校者的建议改，4 条采纳了问题、换了改法：
  - “Don’t beat yourself up over it.” 和 “don’t beat yourself up (or your cofounders) over mistakes”：审校者认为“苛责”偏书面，和作者聊天式的口吻不合，这一点成立。审校者建议两处分别写“太自责”和“怪自己（或者怪你的联合创始人）”，编辑改成两处都用“跟自己过不去”：“别为这个跟自己过不去。”“别因为犯了错就跟自己（或者跟你的联合创始人）过不去。”英文两处用的是同一个说法，中文也用同一个说法；“跟某人过不去”也能用在联合创始人身上，意思是为难对方。
  - “Alexander jumped straight to the end result without any of the work.”：“直接跳到了最终结果”照搬英文，改为“亚历山大一点功夫都没花，一步就得到了最终结果”。
  - “We all stood around a bit dumbfounded”：We all 指工作坊里在场的所有人，“我们几个”听着人数太少，而且前一段 We all started geeking out 译的是“我们全都”。审校者建议“我们全都愣在那儿，有点傻眼”，“愣”和“傻眼”意思重复，编辑改为“我们全都站在那儿，有点傻眼”，stood around 也照顾到了。
  - 速查表 Commitment 一条，“giving up something they value such as meaningful amounts of time, reputational risk, or money”：原译“拿出……声誉风险”搭配不通。审校者建议“拿自己的声誉冒险”，编辑保留术语表里的“声誉风险”，改为“承诺：对方付出自己看重的东西，表明自己是认真的，比如花上相当多的时间、承担声誉风险，或者掏钱。”“付出”也更贴近 giving up。译者自检一节说这一条“句式照第 5 章写”，现在这一句和第 5 章的写法不同了；英文两处本来就不一样（第 5 章是 time, reputation, or money），各照各的原文译，不影响速查表的一致性。
  - 速查表 Facts 一条，“concrete, specific facts about what they do and why they do it”：原译前置定语太长，连用两个“的”，照审校者的建议改为“事实：对方在做什么、为什么这么做，这些实实在在的具体事实（与之相对的是恭维、空话和看法这些坏数据）”。
  - “you’ve got to get your hands dirty… It’s something you learn by doing.”：相邻两句都用“动手”，第二句改为“要边做边学”。审校者建议“得边做边学”，前后已经有两个“你得”，编辑保留原来的“要”。
  - “with folks ranging from Oxford to the UN”：“合作的人从牛津大学到联合国都有”主语是人，后面接机构名，照审校者的建议改为“合作对象从牛津大学到联合国都有”。
- 不采纳的发现：没有。7 条都是表达上的问题，核对后都成立。
- 审校者的总体判断：没有发现意义错误、漏译、增译、否定或数字方面的问题；人名、机构名、地名、数字和章节引用都照术语表和全书统一的写法；全文没有破折号，也没有体例禁用的句式；译者注 [^t1] 解释 hack 的双关，位置和内容都合适。七条都是表达层面的小问题，改不改都不影响读者理解原意。这一节译文忠实，语气贴近样章，可以进入中文通读。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳双语审校的修改以后，从章首到章末顺着中文读完全节，看语句是否连贯、用词是否重复、指代是否清楚、人名和术语前后是否一致。
- 发现并修改：1 处。开篇第 4 段 “Startups do cool stuff and make their lives better.” 原译“让人们的生活变得更好”，这一段短短五句里“人们”“人人”出现了四次，改为“让大家的生活变得更好”。回查英文，their 指前一句的 People，意思不变。
- 检查过、没有改的地方：
  - 指代：开篇末段“努力让他们的生活变得更好”里的“他们”接前一句的“人人”；健身教练一段“给他们打个电话”的“他们”，后一句写明了是警察，都清楚。
  - 一致：亚历山大第一次出现括注英文，后文写“大帝”；“戈尔迪之结”“一记巧招”“一刀斩断这个结”照术语表；“琢磨”两次呼应 geeking out 的两次出现；“需要的话”四处一致；“声誉风险”照术语表。
  - 速查表里和其他章重复的句子没有改动，和各章仍然一字不差。
- 改动都回查过英文，意思、数字和语气没有变化。改完后运行 `site.py status`，本节仍是 49/49 块，中英逐块对应；全文仍然没有破折号，也没有体例禁用的句式。

## 状态

没有未解决的意义问题。还需要主会话定下来的，是译者自检里列出的几处措辞（“谢谢！”“这一路很愉快”“去把事情做成吧”“带课指南”“万一你喜欢看列表呢”，以及 hack 双关是否保留译者注），这些都不涉及意义。速查表里照抄第 1、2、4、5、8 章的句子，如果那几章在审校中改了，这里要跟着改。
