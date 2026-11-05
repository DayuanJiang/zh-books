# 术语表

翻译前根据 `review/terms/` 里的统计数据裁定（来源和门槛见 [review/terms/README.md](review/terms/README.md)）。“出现次数”和“首次出现”由 `tools/term_stats.py` 按英文词形统计，不含脚注和标题；按正则匹配，同词根的普通用法也会算进去，例如 check、power、case。状态都是“初定”，由 Claude 裁定，等用户确认；改动时要回查已经译完的章节。

## 体例

- **人名**：用 [review/terms/people-zh.tsv](review/terms/people-zh.tsv) 的译名。每节第一次出现时在中文名后括注英文原名，例如“彼得·普罗诺沃斯特（Peter Pronovost）”，之后只写中文。只有名没有姓的人（约翰、杰伊、迪伊、托尔）也照这个办法。表里标 keep 的人（Zhi Xiong 等）照写原名。脚注里的人名照写原文。
- **化名**：引言的约翰、第 8 章的库克、第 9 章的哈格曼先生都是化名或改过身份细节，译文照原文的说法交代即可。
- **机构、产品、地名**：见下面“机构、产品与地名”。没有通行中文名的公司和产品照写原名，和汉字之间加空格。
- **书名、报刊、论文**：正文里用《》，每节第一次出现时括注原题，原题用斜体，例如《太空先锋》（*The Right Stuff*）；文章、论文的原题保留引号，不用斜体，例如作者的《纽约客》文章《清单》（“The Checklist”）。常见报刊不括注，见“全书统一的写法”。脚注里的出处保留原文，不加书名号。
- **数字**：年份、日期、百分比和多位数字用阿拉伯数字，和汉字之间加空格，例如“2008 年 10 月”“36%”“178 项操作”。金额换算成中文的万、亿：$360 million 写“3.6 亿美元”，$1.7 million 写“170 万美元”，$650,000 写“65 万美元”。细则见“全书统一的写法”。
- **单位**：英制单位照原文译出（英尺、英里、磅、码、加仑、英寸），数字要紧时括注公制，例如“8000 英尺（约 2400 米）”；华氏温度一律括注摄氏度，取整数，例如“华氏 66 度（约 19 摄氏度）”“华氏 98.6 度（37 摄氏度）”。cc 写“毫升”；units of blood 写“单位血”，units of packed red cells 写“单位浓缩红细胞”。
- **引语和对话**：外科医生、建筑工人、厨师和投资人的对话都很口语，按原文的语气译，粗话（Crap、damn）保留力度。
- **驾驶舱录音**：第 6 章三段引文是对话记录，角色名译成中文，后面用全角冒号：CAPTAIN 译“机长”，FIRST OFFICER 译“副驾驶”，FLIGHT ENGINEER 译“飞行工程师”，RADIO 译“无线电”，VOICE UNIDENTIFIED 译“身份不明的声音”；[expletive] 写“[脏话]”。航班呼号 Continental One Heavy 照写原文。
- **面板标签、清单条目和标语**：飞机警示灯和面板上的标签照写原文，第一次出现括注中文意思，例如 DOOR FWD CARGO（前货舱门）、LDG ALT（着陆高度）选择钮；原文全用大写的清单条目、标语和厨房笔记译成中文，用引号标出，必要时括注原文，例如“驾驶飞机”（FLY THE AIRPLANE）、“警告：非施工人员禁止入内”。厨房里报单的口令也译成中文，见核心概念表。
- **脚注**：开头引号里的是正文里被注释的词句，译成对应的中文，保留引号，后面用全角冒号，例如 `[^2]: “20 世纪 70 年代”：S. Gorovitz and A. MacIntyre, “Toward a Theory of Medical Fallibility,” *Journal of Medicine and Philosophy* 1 (1976): 51–71.`。后面的出处（作者、标题、刊名、出版地和出版社、卷期、页码、网址）保留英文原样；解释性的句子要翻译。常见格式：
  - See also → 另见
  - Data from X → 数据来自 X
  - Further details of the analysis by X will appear in a forthcoming scientific article. → X 的分析详情将在一篇即将发表的科学论文里公布。
  - Portfolio at www.mcsal.com. → 作品集见 www.mcsal.com。
  - The checklist can be accessed at X. → 清单可在 X 查看。
  - The videos can be viewed at X. → 视频可在 X 观看。
  - See annex, table 2. → 见附录表 2。
  - X events and data from Y → X 的经过和数据来自 Y
  - Testimony of Captain X, … → X 机长的证词，……
  - 引言第 1 条脚注 Identifying details were changed at John’s request. → 应约翰的要求，书中改动了可以辨认身份的细节。
- **脚注标记**：`[^n]` 放在中文里对应词句的后面，编号与英文一致。注释引用的话以引号结束时，标记放在右引号后面。
- **译者注**：写成 `[^t1]:`，在正文里引用。需要译者注的地方：eptitude、Code Blue、operating theater 的字面意思、the right stuff 和书名的关系、世卫组织清单的中文官方名、原文疑点（第 3 章注释 3 的网址）。
- **分隔线**：分隔线 `---` 只写在英文文件里。
- **破折号和句式**：中文译文不用破折号（——），原文的破折号按意思改成逗号、冒号、括号或另起一句；也不用“不是……而是……”这种句式，换成直接的说法。

## 各节标题

| 章节 id | 英文 | 中文标题（`#` 一级标题照这一列写） |
| --- | --- | --- |
| dedication | Dedication | 献辞 |
| introduction | Introduction | 引言 |
| ch01 | 1. The Problem of Extreme Complexity | 第 1 章 极端复杂的难题 |
| ch02 | 2. The Checklist | 第 2 章 清单 |
| ch03 | 3. The End of the Master Builder | 第 3 章 总建造师的终结 |
| ch04 | 4. The Idea | 第 4 章 构想 |
| ch05 | 5. The First Try | 第 5 章 初次尝试 |
| ch06 | 6. The Checklist Factory | 第 6 章 清单工厂 |
| ch07 | 7. The Test | 第 7 章 试验 |
| ch08 | 8. The Hero in the Age of Checklists | 第 8 章 清单时代的英雄 |
| ch09 | 9. The Save | 第 9 章 救回一命 |
| acknowledgments | Acknowledgments | 致谢 |
| about-the-author | About the Author | 关于作者 |

中文版《清单革命》（王佳艺译，浙江人民出版社 2012 年版）把全书重新分成三部分，各章另起了标题（例如第 1 章“人人都会犯错误”，第 4 章“权力下放”），和原书的章名对不上，这里只作参考，标题按原书直译：第 4 章的 The Idea 指作者在这一章里形成的那个“理论”，译“构想”；第 9 章的 The Save 呼应引言里外科医生说的 great saves（救回来的病例），译“救回一命”。

译者读完一章后，如果觉得标题另有更贴切的译法，在汇报里提出，由主会话统一修改。

## 全书统一的写法

翻译开始前先定下的写法，各章都照此执行；译完后编辑提出的新问题，补在这一节。

- **数字**：一到十，以及带“几、十几、数百、上千”的约数，用汉字（三岁的女儿、两天后、几十家医院）；11 以上的确数用阿拉伯数字（178 项操作、24 小时、19 项检查），万和亿前面的数字也用阿拉伯数字（1.3 万多种疾病、9 万人、23 亿）；年份、日期、钟点、金额、百分比一律用阿拉伯数字（凌晨 1:30、下午 3:25、上午 7 点）。原文用英文单词写的大数（thirteen thousand、two hundred feet）同样按这条规则转成阿拉伯数字。倍数写成“是原来的 N 倍”；百分比的增减照原文写“降低了 N%”。
- **书名、报刊括注**：每节第一次出现时括注原题，原题用斜体；文章、论文的原题保留引号，不用斜体。《纽约客》《纽约时报》《新英格兰医学杂志》《柳叶刀》这些常见报刊不括注；其他刊物（《胸外科年鉴》*Annals of Thoracic Surgery*、《美食与美酒》*Food and Wine*、《时尚先生》*Esquire*、《每日镜报》*Daily Mirror*、《纽约邮报》*New York Post*）每节第一次出现时括注。
- **人名**：名人也照常在每节第一次出现时括注英文。脚注里的人名，无论在出处里还是在说明句里，一律照写英文。“勋爵”“爵士”“少校”“机长”这类称呼放在中文名后面：达尔齐勋爵、唐纳森爵士、希尔少校、萨伦伯格机长。
- **泛指的人称**：原文泛指的 he or she、his or her 不必逐字译出，按中文习惯写“病人”“这个人”或省略；原文用 she 泛指病人的地方，中文写“病人”或“她”都可以，同一段里保持一致。
- **作者的身份**：作者是普通外科和内分泌外科医生，叙述里的 we 常指“我们外科医生”或“我们医生”，按上下文补出来，避免读者以为指全人类。
- **医学说法**：中国大陆的通行说法优先，例如“中心静脉导管”“巡回护士”“器械护士”“住院医生”“主治医生”“并发症发生率”。病名和药名第一次出现时不必括注英文，除非原文正在解释这个词（ECMO、asystole）。
- **航空说法**：中国民航的通行说法优先，例如“副驾驶”“机组”“驾驶舱”“滑行”“鸟击”“水上迫降”“慢车”。航空检查单在业内叫“检查单”，本书统一写“清单”，和全书一致。
- **世卫组织**：World Health Organization 每节第一次出现写“世界卫生组织（WHO）”，之后写“世卫组织”；原文写 WHO 的地方也写“世卫组织”。
- **引号里的说法**：原文用引号标出的行话和俗称（“flying fortress”“pause points”“killer items”“cocaine brain”），中文也加引号，第一次出现括注原文。
- **原文疑点**：第 3 章注释 3 的网址 www.darmouthatlas.org 照原文保留，加译者注说明正确的网址是 www.dartmouthatlas.org。原文疑点的完整清单见 [review/source.md](review/source.md)。

## 核心概念

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| checklist | 清单 | 全书的核心概念：把关键步骤写成简短的条目，在规定的时点逐项核对。aviation checklist 也写“清单”，to-do list 写“待办清单” | 检查表、核对表、清单式管理 | introduction | 355 | 初定 |
| check / checks | 检查项 / 核对 | 名词指清单上的一项或停下来核对一次；动词按上下文译“检查”“核对”“确认”；check mark 写“勾”，check box 写“勾选框”，double-check 写“复核” | 支票（check cashing、payroll checks 才是支票） | introduction | 72 | 初定 |
| failure / avoidable failure | 失败 / 可以避免的失败 | 没有做到本可以做到的事；落到器官和机器上按搭配：kidney failure 肾衰竭，engine failure 发动机失效，building failure 建筑失效 | 故障（只在说机器时才用） | introduction | 55 | 初定 |
| ignorance / ineptitude | 无知 / 无能 | 戈罗维茨和麦金太尔区分的两种失败：知识本身还不存在，和知识已经有了却没有用对；ineptitude 第一次出现括注原文；failures of ignorance 写“无知造成的失败” | “无能”在这里指没有正确运用已有的知识，和个人能力高低无关 | introduction | 10 | 初定 |
| necessary fallibility / fallibility | 必然的易错 / 易错 | necessary fallibility 指有些事超出人的能力，失败在所难免；human fallibility 写“人的易错”或“人难免出错” |  | introduction | 5 | 初定 |
| eptitude | “有能”（eptitude） | 作者从 ineptitude 倒推出来的词：始终如一、正确地运用已有的知识；第一次出现括注原文并加译者注 |  | introduction | 1 | 初定 |
| complexity / extreme complexity | 复杂性 / 极端复杂 | 第 1 章标题里的概念：知识和步骤多到个人无法可靠地掌控 |  | introduction | 38 | 初定 |
| complicated | 繁杂 | 齐默尔曼和格卢伯曼的三分法里的第二类：繁杂问题像把火箭送上月球，可以拆成一串简单问题，但没有现成的配方，要多人、多团队协调。第 3 章以外泛泛地用时也可写“复杂”，和 complex 在同一段对照出现时一律写“繁杂” | complex（复杂） | ch01 | 14 | 初定 |
| complex | 复杂 | 三分法里的第三类：复杂问题像养孩子，每一次都不同，经验有用但不够，结果高度不确定；simple problems 写“简单问题”，指照配方就能做成的事 | complicated（繁杂） | ch01 | 40 | 初定 |
| know-how / expertise / experts | 知识和本领 / 专业能力 / 专家 | expertise 指专门的知识和经验，the mantra of modern medicine 那句写“专业能力是现代医学的信条” |  | introduction | 42 | 初定 |
| specialization / superspecialization | 专科化 / 超专科化 | superspecialist 写“超级专科医生”，ultraspecialized 写“分得极细”，subspecialized / subspecialty 写“亚专科” |  | ch01 | 35 | 初定 |
| Master Builder / Master Physician | 总建造师 / “总医师” | 中世纪以来一手包办设计、工程和施工的总负责人；医学里对应的是从诊断到治疗独自包揽一切的医生。第 3 章标题，第一次出现括注原文 | 建筑大师、大师 | ch03 | 8 | 初定 |
| cognitive net | 认知防护网 | 清单像一张网，接住人人都有的记忆、注意力和周全程度上的缺陷；中文版《清单革命》已用这个说法 |  | ch03 | 1 | 初定 |
| forcing function | 强制功能 | 工程术语：迫使人做出必要动作的简单办法，清单就是一种；第一次出现括注原文 | 强制函数 | ch03 | 3 | 初定 |
| all-or-none process | 全有或全无的过程 | 漏掉一个关键步骤就等于白做的过程 |  | ch02 | 1 | 初定 |
| stupid stuff / dumb stuff | 傻瓜都知道的事 | 作者的口语说法，指简单到不值一提、却不能出错的步骤；the stupid but critical stuff 写“傻瓜都知道、却至关重要的事” |  | ch02 | 5 | 初定 |
| construction schedule / submittal schedule | 施工进度表 / 报审进度表 | 前一张列施工任务，后一张列沟通任务：谁要在哪天之前和谁、就哪方面的工程交换（submit）信息 |  | ch03 | 9 | 初定 |
| communication checks | 沟通检查 | 清单里确保相关的人彼此交谈的条目，和列出操作步骤的检查相对；communication tasks 写“沟通任务”，communication checklist 写“沟通清单” |  | ch03 | 5 | 初定 |
| power | 权力 / 决策权 | 第 4 章的核心：复杂局面下要把决策权从中心推到外围（push the power of decision making out to the periphery）；electrical power 写“电力”，engines lost power 写“失去动力” |  | ch01 | 32 | 初定 |
| command-and-control | 命令与控制 | 卡特里娜飓风中政府依赖的集中指挥模式；command-and-control system 写“命令与控制体系” |  | ch04 | 2 | 初定 |
| pause point | 暂停点 | 清单规定团队必须停下来核对的时点；航空用语，第一次出现括注原文；中文版作“检查点” | 检查点（checkpoint） | ch05 | 7 | 初定 |
| checkpoint | 检查点 | 流程中必须核对的一环，例如花旗中心那次被绕过的结构计算复核，帕伯莱清单上的一项 | 暂停点 | ch03 | 2 | 初定 |
| DO-CONFIRM / READ-DO | 先做后确认型 / 边读边做型 | 两类清单：前者凭记忆和经验各自做完，再停下来逐项确认；后者照着清单一边读一边做，像菜谱。第一次出现括注原文；中文版作“操作-确认”和“边读边做” |  | ch06 | 7 | 初定 |
| killer items | “致命项” | 跳过了最危险、又常被漏掉的步骤；non-killer items 写“非致命项”；中文版作“杀手项目” |  | ch06 | 2 | 初定 |
| normal / non-normal checklists | “正常”清单 / “非正常”清单 | 航空用语：日常运行用的清单，和应对各种紧急情况的清单 | 常规、非常规 | ch06 | 2 | 初定 |
| briefing / team briefing | 简报 / 团队简报 | 开始之前团队停下来交代计划、预计的困难和顾虑；taxi and takeoff briefing 写“滑行和起飞简报”，preoperative briefing 写“术前简报”；briefed 写“交代过” |  | ch05 | 7 | 初定 |
| activation phenomenon | 激活现象 | 开头给每个人一个说话的机会，会激发参与感、责任感和开口的意愿 |  | ch05 | 1 | 初定 |
| teamwork | 团队合作 | team 写“团队”，手术团队写“手术团队”；teamwork climate 写“团队合作氛围” |  | ch05 | 16 | 初定 |
| discipline | 纪律 | 第 8 章的核心：遵守审慎的程序、与他人协同的纪律，航空业在职业精神的三项期待之外加上的第四项 | 自律、学科 | ch02 | 16 | 初定 |
| professionalism / selflessness / skill / trustworthiness | 职业精神 / 无私 / 技能 / 可信 | 职业行为准则（code of conduct）共有的三项期待 |  | ch08 | 6 | 初定 |
| autonomy / collegiality | 自主 / 同僚情谊 | 医学界奉为职业指针的两项；作者认为它们离纪律还远 |  | ch03 | 5 | 初定 |
| protocol / judgment / craft | 规程 / 判断 / 手艺 | protocol 指事先规定的做法；craft and protocol 写“手艺与规程”，when to follow one’s judgment and when to follow protocol 写“什么时候听自己的判断，什么时候照规程办” | 协议 | introduction | 19 | 初定 |
| procedure | 手术、操作 / 程序 | 医学里 surgical procedure 写“手术”，office procedures 写“门诊操作”；航空和一般流程写“程序”，standard operating procedures 写“标准操作程序” |  | introduction | 42 | 初定 |
| hero / heroism | 英雄 / 英雄主义 | 第 8 章标题；Hudson River hero 写“哈得孙河英雄” |  | ch08 | 8 | 初定 |
| expert audacity / the right stuff | 专家的胆识 / “过人的素质” | the right stuff 出自沃尔夫的书名，指试飞员的专注、胆量、机智和临场应变；第一次出现括注原文，并加译者注说明和书名的关系 |  | ch08 | 5 | 初定 |
| too much airplane for one man to fly | “飞机太复杂，一个人飞不了” | 1935 年报纸对 299 型的评语，第 2 章借来形容许多行业 |  | ch02 | 2 | 初定 |
| save / great saves | 救回 / 救回来的病例 | 外科医生的说法，把濒死的病人救回来；第 9 章标题 The Save 写“救回一命”；save lives 写“挽救生命”，saved costs 写“节省开支” | 保存 | introduction | 9 | 初定 |
| error / mistake | 差错 / 错误 | 医疗和航空里的 error 多写“差错”；pilot error 写“飞行员失误”；near errors 写“险些发生的差错”；投资里的 mistakes 写“错误” |  | introduction | 57 | 初定 |
| leverage | 杠杆 | 阿基米德的杠杆；Plain soap was leverage 写“普通肥皂就是杠杆”；投资语境的 leveraged 写“举债程度” |  | ch05 | 3 | 初定 |
| behavior-change delivery vehicle | 改变行为的载体 | 卢比对肥皂的说法 |  | ch05 | 1 | 初定 |
| pilot study / pilot sites | 试点研究 / 试点医院 | 第 7 章八家医院的研究；eight-city pilot study 写“八城市试点研究” | 飞行员 | ch05 | 7 | 初定 |
| pilot / test pilot / copilot | 飞行员 / 试飞员 / 副驾驶 | first officer 也写“副驾驶”，captain 写“机长” | 试点 | ch02 | 76 | 初定 |
| pilot flying / pilot not flying | 操纵飞行员 / 非操纵飞行员 | 航空分工：前者开飞机，后者负责发起和朗读清单；第一次出现加引号 |  | ch07 | 3 | 初定 |
| crew | 机组 | cockpit crew 写“驾驶舱机组”，cabin crew 写“客舱机组”；emergency crew、rescue crews 按上下文写“急救人员”“救援人员”，construction crews 写“施工队” |  | ch01 | 23 | 初定 |
| simulator | 模拟器 | flight simulator 写“飞行模拟器”；第 7 章作者把会议室叫作 simulator，写“模拟器”，保留玩笑的意味 |  | ch06 | 7 | 初定 |
| cockpit voice recorder | 驾驶舱话音记录器 |  | 黑匣子（中文口语，不作正式译名） | ch06 | 3 | 初定 |
| ditching | 水上迫降 | ditch the plane in the ocean 写“在海上迫降” |  | ch06 | 4 | 初定 |
| bird strike | 鸟击 | dual bird strikes 写“两台发动机同时遭鸟击” |  | ch08 | 2 | 初定 |
| fly-by-wire | 电传操纵 | fly-by-wire control system 写“电传操纵系统” |  | ch08 | 2 | 初定 |
| uncommanded rollback | 非指令性推力回退 | 发动机没有收到指令就自行降到最低功率；rolled back to minimal power 写“推力回退到最小” |  | ch06 | 2 | 初定 |
| safe surgery checklist | 安全手术清单 | 第 5 到 9 章的主角：三个暂停点、19 项检查的手术清单；WHO safe surgery checklist 写“世卫组织安全手术清单”。中国大陆卫生部门采用的官方中文版叫《手术安全核对表》，第一次出现加译者注说明 | 手术核对表 | ch05 | 20 | 初定 |
| Safe Surgery Saves Lives | “安全手术拯救生命”项目 | 世卫组织的全球项目，中文名采用世卫组织中文资料的说法 |  | acknowledgments | 2 | 初定 |
| before anesthesia / before incision / sign-out / time-out | 麻醉前 / 切皮前 / 离室前核对 / 暂停核对 | 安全手术清单的三个暂停点：麻醉前、切皮前、离开手术室前；Before Incision check 写“切皮前核对”；sign-out 写“离室前核对”；called a time-out 写“叫停，开始核对” |  | ch07 | 10 | 初定 |
| Cleared for Takeoff | “准予起飞” | 哥伦布儿童医院的切皮前清单，以及盖在手术刀上的小金属牌 |  | ch05 | 3 | 初定 |
| Keystone Initiative | “基石计划” | 普罗诺沃斯特在密歇根全州 ICU 推行中心静脉导管清单的项目；第一次出现括注原文 |  | ch02 | 3 | 初定 |
| pay-for-performance | 按绩效付费 |  |  | ch05 | 2 | 初定 |
| Hawthorne effect | 霍桑效应 | 研究对象因为被观察而表现变好 |  | ch07 | 1 | 初定 |
| vital signs | 生命体征 | 体温、脉搏、血压、呼吸频率，后来加上疼痛；vitals chart 写“生命体征记录表” |  | ch02 | 8 | 初定 |
| Code Blue | 蓝色代码（Code Blue） | 医院里召集抢救心搏骤停的紧急呼叫；第一次出现括注原文并加译者注；A nurse called a Code Blue 写“一名护士呼叫了蓝色代码” |  | introduction | 2 | 初定 |
| central line / line infection | 中心静脉导管 / 导管感染 | lines 指插进体内的各种导管，lined him up 写“给他置管”，arterial line 写“动脉导管” | 线路、电线 | ch01 | 24 | 初定 |
| ICU / intensive care / critical care | ICU / 重症监护 / 危重症医学 | 原文写 ICU 的照写 ICU，第一次出现写“重症监护室（ICU）”；intensive care unit 写“重症监护室”；intensivist 写“重症医学科医生”；life support 写“生命支持” |  | ch01 | 67 | 初定 |
| operating room / OR / operating theater | 手术室 | 原文写 OR 的也写“手术室”；第 5 章说明 operating theater 字面意思的地方写“手术剧场”并括注原文、加译者注，第 7 章伦敦的用法直接写“手术室” |  | introduction | 68 | 初定 |
| anesthesiologist / anesthetist | 麻醉科医生 / 麻醉师 | 前者是医生；后者在英国和许多国家不一定是医生（坦桑尼亚的麻醉师都没有医学学位）；anesthesia staff 写“麻醉人员”，nurse anesthetist 写“麻醉护士” |  | introduction | 50 | 初定 |
| circulating nurse / scrub nurse | 巡回护士 / 器械护士 | scrub tech 写“器械技师”；scrubbed-in nurse 写“上台的器械护士” |  | ch05 | 13 | 初定 |
| resident / attending / fellowship | 住院医生 / 主治医生 / 专科培训 | residency 写“住院医生培训”；research fellow 写“研究员”（第 7 章的两位是抽出时间做研究的外科住院医生）；MacArthur Fellow 写“麦克阿瑟学者” |  | introduction | 28 | 初定 |
| general surgery / general surgeon | 普通外科 / 普通外科医生 | general surgery call 写“普通外科值班” |  | introduction | 10 | 初定 |
| complication | 并发症 | major complications 写“严重并发症”；complication rate 写“并发症发生率” |  | ch01 | 32 | 初定 |
| incision | 切口 / 切皮 | make the incision 写“切开皮肤”或“下刀”；before incision 指切开皮肤之前 |  | ch01 | 21 | 初定 |
| surgical fire | 手术室火灾 |  |  | ch07 | 4 | 初定 |
| value investor / margin of safety | 价值投资者 / 安全边际 |  |  | ch08 | 3 | 初定 |
| cocaine brain / greed mode / fear mode | “可卡因大脑” / “贪婪模式” / “恐惧模式” | 帕伯莱和斯皮尔的说法：看到诱人的机会时被大脑奖赏回路支配的状态，和熊市里过度恐惧的状态 |  | ch08 | 6 | 初定 |
| mental checklist / Day Three Checklist | “思维清单” / “第三天清单” | 前者是巴菲特在头脑里过的清单，后者是库克团队在考察第三天结束时核对的清单；three-day list 写“三天清单” |  | ch08 | 5 | 初定 |
| venture capitalists and their styles | 风险投资人；“艺术评论家型”“海绵型”“检察官型”“求爱者型”“终结者型”“机长型” | 斯玛特归纳的评估创业者的六种风格，原文首字母大写并加引号，中文加引号，第一次出现括注原文 |  | ch08 | 17 | 初定 |
| trades / tradesmen | 工种 / 各工种的工人 | 建筑涉及的 16 个专业工种 | 贸易 | ch03 | 7 | 初定 |
| general contractor / subcontractor | 总承包商 / 分包商 |  |  | ch03 | 9 | 初定 |
| structural engineer / structural engineering | 结构工程师 / 结构工程 |  |  | ch03 | 12 | 初定 |
| project executive / field office | 项目执行经理 / 现场办公室 | 原文说他们不再叫 field boss（工头）了 |  | ch03 | 5 | 初定 |
| building failure | 建筑失效 | 原文定义为正在使用的建筑部分或全部倒塌，加引号 |  | ch03 | 2 | 初定 |
| tuned mass damper | 调谐质量阻尼器 |  |  | ch03 | 1 | 初定 |
| recipe | 配方 / 菜谱 | 简单问题的“配方”（照配方烤蛋糕、没有现成的配方可循）；厨房里写下来的做法写“菜谱”，“菜谱是最基本的清单” |  | ch03 | 15 | 初定 |
| sous chef / line cooks / pow wow / read-back | 副主厨 / 灶台厨师 / 碰头会 / 复述确认 | Rialto 厨房里的说法；报单口令 Fire 写“开做”，On hold 写“先等着”，Lobo 写“龙虾” |  | ch04 | 8 | 初定 |
| system | 系统 / 体系 | 伯威克说的 system 指人和技术组合成的整体；health system 写“卫生系统”或“医疗体系”，organ systems 写“器官系统” |  | ch01 | 44 | 初定 |
| patient safety | 患者安全 | WHO Patient Safety 写“世卫组织患者安全项目” |  | ch05 | 4 | 初定 |
| case | 病例 / 手术 | 外科医生说的 case 常指一台手术（five cases 写“五台手术”）；case report 写“病例报告”，case study 写“案例研究” | 案件 | introduction | 62 | 初定 |

## 机构、产品与地名

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| World Health Organization (WHO) | 世界卫生组织（WHO）/ 世卫组织 | 见“全书统一的写法”；WHO headquarters 写“世卫组织总部” |
| Boeing / Airbus | 波音公司 / 空客 | 机型写“波音 747”“波音 777-200ER”“787 梦想飞机”“空客 A320” |
| Model 299 / B-17 / Flying Fortress | 299 型 / B-17 / “空中堡垒” | 第 2 章 |
| U.S. Army Air Corps / Wright Air Field | 美国陆军航空兵 / 赖特机场 | 第 2 章，俄亥俄州代顿 |
| Martin / Douglas | 马丁公司 / 道格拉斯公司 | 和波音竞标的两家飞机制造商 |
| Johns Hopkins Hospital / Johns Hopkins | 约翰斯·霍普金斯医院 / 约翰斯·霍普金斯 |  |
| Michigan Health and Hospital Association | 密歇根州卫生与医院协会 |  |
| Sinai-Grace Hospital / Detroit Receiving Hospital | 西奈-格雷斯医院 / 底特律接收医院 | Eight Mile Road 写“八英里路” |
| Blue Cross Blue Shield of Michigan | 密歇根蓝十字蓝盾 |  |
| Arrow International | 照写原名 | 中心静脉导管制造商 |
| Klagenfurt / Vienna | 克拉根福 / 维也纳 | 奥地利 |
| Harvard Vanguard (Medical Associates) / Kenmore Square | 哈佛先锋医疗协会 / 肯莫尔广场 | 波士顿 |
| Brigham and Women’s Hospital | 布莱根妇女医院 | 作者工作的医院 |
| Harvard School of Public Health / Harvard Medical School / Kennedy School of Government | 哈佛公共卫生学院 / 哈佛医学院 / 肯尼迪政府学院 |  |
| McNamara/Salvia | 麦克纳马拉/萨尔维亚公司 | 结构工程公司 |
| John Moriarty and Associates | 约翰·莫里亚蒂联合公司 | 俄罗斯码头项目的总承包商 |
| Sumner Shane | 照写原名 | 萨尔维亚毕业后加入的建筑工程公司 |
| Russia Wharf | 俄罗斯码头大楼 | 波士顿，波士顿倾茶事件（Boston Tea Party）的发生地旁边 |
| Fenway Park / Green Monster / Boston Red Sox | 芬威球场 / 绿色怪物 / 波士顿红袜队 |  |
| International Place | 国际广场 | 波士顿，菲利普·约翰逊设计 |
| Meadowlands Xanadu / SnowPark | 梅多兰兹仙乐都 / 照写原名 | 新泽西州东卢瑟福 |
| Citicorp building (Citigroup) | 花旗中心 | 原文 Citicorp (now Citigroup) building 写“花旗公司（现在叫花旗集团）大楼”，之后写“花旗中心” |
| Bethlehem Steel | 伯利恒钢铁公司 |  |
| Clash Detective / Project Center | 照写原名 | 建筑软件，第一次出现括注中文意思（碰撞侦探、项目中心） |
| C&E Hardware / Richland Avenue / Athens, Ohio | C&E 五金店 / 里奇兰大道 / 俄亥俄州阿森斯 | 作者童年 |
| Hurricane Katrina / New Orleans / Plaquemines Parish / Jefferson Parish | 卡特里娜飓风 / 新奥尔良 / 普拉克明堂区 / 杰斐逊堂区 |  |
| Federal Emergency Management Agency (FEMA) | 联邦紧急事务管理署（FEMA） | 之后写 FEMA |
| Department of Homeland Security / Department of Transportation | 国土安全部 / 交通部 |  |
| New Orleans Superdome / Ernest N. Morial Convention Center | 新奥尔良超级穹顶体育馆 / 欧内斯特·N.莫里亚尔会议中心 |  |
| Wal-Mart | 沃尔玛 |  |
| Coast Guard / National Guard / Red Cross | 海岸警卫队 / 国民警卫队 / 红十字会 |  |
| Van Halen / M&M’s / Crazy from the Heat | 范·海伦乐队 / M&M’s 巧克力豆 / 《热昏了头》（*Crazy from the Heat*） | 罗斯的回忆录书名没有通行中译名，这里自译 |
| Rialto / James Beard Foundation | Rialto 餐厅 / 詹姆斯·比尔德基金会 | Best Chef award 写“最佳主厨奖” |
| Burger King / Taco Bell | 汉堡王 / 塔可钟 |  |
| Brown University | 布朗大学 |  |
| International Committee of the Red Cross | 红十字国际委员会 |  |
| Columbus Children’s Hospital | 哥伦布儿童医院 |  |
| University of Toronto / Toronto General Hospital | 多伦多大学 / 多伦多综合医院 |  |
| Kaiser | 凯撒医疗集团 | 南加州的几家医院 |
| Centers for Disease Control (CDC) | 美国疾病控制中心 | 原文 U.S. Centers for Disease Control 写“美国疾病控制中心” |
| HOPE | 照写原名 | 巴基斯坦的慈善组织 |
| Procter & Gamble / Safeguard | 宝洁公司 / 舒肤佳 | Safeguard 是舒肤佳在中国的品牌名 |
| Karachi / Soho / Broad Street | 卡拉奇 / 苏豪区 / 布罗德街 |  |
| Creighton University / University of Texas Southwestern | 克赖顿大学 / 得克萨斯大学西南医学中心 |  |
| United Airlines / Continental / Delta Air Lines / US Airways / British Airways | 美国联合航空（美联航）/ 大陆航空 / 达美航空 / 全美航空 / 英国航空 | 航班写“美联航 811 航班”“英航 38 号航班”“全美航空 1549 航班” |
| KLM / Pan American | 荷兰皇家航空 / 泛美航空 | 特内里费空难 |
| Air Accidents Investigation Branch (AAIB) | 英国航空事故调查局（AAIB） |  |
| Federal Aviation Administration / National Transportation Safety Board (NTSB) | 美国联邦航空管理局 / 美国国家运输安全委员会（NTSB） |  |
| Heathrow / La Guardia / Teterboro / Seattle-Tacoma | 希思罗机场 / 拉瓜迪亚机场 / 泰特伯勒机场 / 西雅图-塔科马机场 |  |
| Hudson River / George Washington Bridge | 哈得孙河 / 乔治·华盛顿大桥 | miracle on the Hudson 写“哈得孙河奇迹” |
| Tenerife / Canary Islands | 特内里费 / 加那利群岛 | 1977 年的特内里费空难 |
| Cessna | 塞斯纳 |  |
| Jet A-1 | Jet A-1 航空煤油 |  |
| Pabrai Investment Funds / Aquamarine Capital Management | 帕伯莱投资基金 / Aquamarine 资本管理公司 |  |
| Berkshire Hathaway / Cort Furniture / Enron | 伯克希尔·哈撒韦公司 / Cort 家具公司 / 安然公司 |  |
| Claremont Graduate University / Clemson University | 克莱蒙特研究生大学 / 克莱姆森大学 |  |
| Institute for Healthcare Improvement | 美国医疗保健改进研究所 |  |
| National Institutes of Health | 美国国立卫生研究院 | 作者设想的 National Institute of Health Systems Innovation 写“国家卫生系统创新研究院” |
| University of Washington Medical Center | 华盛顿大学医学中心 | 西雅图，试点医院 |
| St. Mary’s Hospital | 圣玛丽医院 | 伦敦帕丁顿，试点医院 |
| Auckland City Hospital | 奥克兰市立医院 | 新西兰，试点医院 |
| Philippines General Hospital | 菲律宾总医院 | 马尼拉，试点医院 |
| Prince Hamza Hospital | 哈姆扎亲王医院 | 约旦安曼，试点医院 |
| St. Stephen’s Hospital | 圣斯蒂芬医院 | 新德里，试点医院 |
| St. Francis Designated District Hospital | 圣弗朗西斯指定区医院 | 坦桑尼亚伊法卡拉，试点医院 |
| National Health Service | 国家医疗服务体系（NHS） | 英国 |
| National Patient Safety Agency | 英国国家患者安全局 |  |
| Metropolitan Books / Profile Books | 照写原名 | 出版社 |
| MacArthur Foundation | 麦克阿瑟基金会 |  |
| New Yorker / New England Journal of Medicine / Lancet | 《纽约客》/《新英格兰医学杂志》/《柳叶刀》 | 不括注 |
| ABC News / New York Post / Daily Mirror | 美国广播公司新闻 / 《纽约邮报》/《每日镜报》 |  |
| Super Bowl / Air Force Academy | 超级碗 / 美国空军学院 |  |
| Ferrari / Porsche / BMW / Volvo | 法拉利 / 保时捷 / 宝马 / 沃尔沃 | 第 8 章伯威克的比喻 |
| Google / Apple / Coca-Cola | 谷歌 / 苹果 / 可口可乐 |  |
