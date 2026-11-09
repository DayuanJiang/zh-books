# 术语表

第一版，由 `en-zh-translation-polish` 的 `terms.py` 抽取的候选词（spaCy，频次不少于 8）和预先列出的核心概念整理而来。“出现次数”和“首次出现”由脚本统计，不含书末注释。状态都是“初定”：译法在样章审阅后确认；改动时要回查已经译完的章节。每条的原文例句和裁定者记在 `review/terms/glossary-evidence.tsv`；目前都由 Claude 初定，等用户确认。

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| System 1 / System 2 | 系统 1 / 系统 2 | 书中两个虚构的“角色”：快速、自动的思考和缓慢、费力的思考；作主语时可以说“系统 1 认为” | 大脑的具体部位；不写成“系统一” | introduction | 463 | 初定 |
| judgment and choice | 判断与选择 | 全书的主题 |  | introduction | 16 | 初定 |
| decision making | 决策 |  |  | introduction | 39 | 初定 |
| informed gossip / intelligent gossip | 有见地的闲谈 | 引言里作者希望读者在办公室饮水机旁谈论别人决策的那种闲谈 | 八卦、流言 | introduction | 2 | 初定 |
| gossip（单独出现） | 闲谈 | 饮水机旁谈论别人的判断和选择；“gossip is exchanged”这类搭配可以写成“说长道短” | 八卦（贬义、娱乐化） | introduction | 8 | 初定 |
| label | 名称 / 诊断名称；动词作“贴上标签” | 疾病和偏差的名称，作者用它比喻判断错误的“诊断术语” | 标签（名词时不用） | introduction | 33 | 初定 |
| intuition / intuitive judgment | 直觉 / 直觉判断 |  | 灵感 | introduction | 23 | 初定 |
| expert intuition | 专家直觉 |  |  | introduction | 8 | 初定 |
| heuristic | 启发式 | 简化判断的经验法则，例如代表性启发式 | 启发法（算法意义） | introduction | 116 | 初定 |
| bias | 偏差 | 可以预测的系统性错误 | 偏见（对群体的成见） | introduction | 160 | 初定 |
| systematic error | 系统性错误 |  | 测量学的系统误差 | introduction | 11 | 初定 |
| cognitive illusion | 认知错觉 |  | 幻觉（感官上不存在的东西） | ch01 | 12 | 初定 |
| WYSIATI (what you see is all there is) | 所见即全部 | 只根据眼前的信息下结论；首次出现时写“所见即全部（WYSIATI）” |  | ch07 | 22 | 初定 |
| cognitive ease / cognitive strain | 认知放松 / 认知紧张 | 处理信息时感到轻松或吃力的程度 | 认知负荷 | ch05 | 53 | 初定 |
| priming / prime | 启动效应 / 启动 | 先接触的刺激影响后来的反应 | 准备、底漆 | ch04 | 48 | 初定 |
| ego depletion | 自我损耗 |  |  | ch03 | 6 | 初定 |
| associative memory | 联想记忆 |  |  | introduction | 16 | 初定 |
| associative coherence | 联想一致性 |  |  | ch05 | 8 | 初定 |
| the associative machine | 联想机器 | 第 4 章标题 |  | ch04 | 16 | 初定 |
| the lazy controller | 懒惰的控制者 | 第 3 章标题，指系统 2 |  | ch03 | 1 | 初定 |
| law of least effort | 最省力法则 |  |  | ch02 | 5 | 初定 |
| mere exposure effect | 单纯曝光效应 |  |  | ch05 | 6 | 初定 |
| halo effect | 光环效应 |  | 晕轮效应（同义，统一用光环效应） | introduction | 19 | 初定 |
| mental shotgun | 心理霰弹枪 | 系统 1 计算的东西比需要的多 |  | ch08 | 10 | 初定 |
| substitution | 替代 | 用简单问题代替困难问题回答 | 替换（物件） | introduction | 56 | 初定 |
| intensity matching | 强度匹配 |  |  | ch08 | 13 | 初定 |
| law of small numbers | 小数定律 |  | 大数定律 | ch10 | 14 | 初定 |
| anchor / anchoring effect | 锚 / 锚定效应 |  |  | ch11 | 146 | 初定 |
| anchoring index | 锚定指数 |  |  | ch11 | 4 | 初定 |
| availability / availability heuristic | 可得性 / 可得性启发式 | 例子越容易想起，越被判断为常见 | 易得性（统一用可得性） | introduction | 74 | 初定 |
| availability cascade | 可得性级联 |  |  | ch13 | 14 | 初定 |
| affect heuristic | 情感启发式 |  |  | introduction | 11 | 初定 |
| representativeness | 代表性 |  |  | ch08 | 47 | 初定 |
| base rate | 基础比率 |  | 基数 | ch07 | 85 | 初定 |
| conjunction fallacy | 合取谬误 |  |  | ch15 | 9 | 初定 |
| regression to the mean | 均值回归 |  | 回归分析 | ch17 | 17 | 初定 |
| illusion of understanding | 理解的错觉 |  |  | ch19 | 2 | 初定 |
| illusion of validity | 有效性错觉 |  |  | ch20 | 9 | 初定 |
| hindsight bias | 后见之明偏差 |  |  | ch19 | 4 | 初定 |
| outcome bias | 结果偏差 |  |  | ch19 | 6 | 初定 |
| narrative fallacy | 叙事谬误 |  |  | ch19 | 3 | 初定 |
| planning fallacy | 规划谬误 |  |  | ch23 | 19 | 初定 |
| outside view / inside view | 外部视角 / 内部视角 |  |  | ch23 | 29 | 初定 |
| reference class | 参照类别 |  | 参照点 | ch23 | 7 | 初定 |
| overconfidence / optimistic bias | 过度自信 / 乐观偏差 |  |  | introduction | 42 | 初定 |
| premortem | 事前验尸 |  |  | ch24 | 6 | 初定 |
| Econs / Humans | 经济人 / 普通人 | 理性主体模型里的人和真实的人；大写的 Humans 才译“普通人” | 人类（泛指） | ch25 | 21 | 初定 |
| rational agent model | 理性主体模型 |  |  | ch25 | 19 | 初定 |
| utility / expected utility theory | 效用 / 期望效用理论 |  | 实用、功用 | ch23 | 117 | 初定 |
| Bernoulli | 伯努利 | 丹尼尔·伯努利 |  | ch25 | 46 | 初定 |
| theory-induced blindness | 理论导致的盲目 |  |  | ch25 | 10 | 初定 |
| prospect theory | 前景理论 |  | 展望理论（统一用前景理论） | introduction | 56 | 初定 |
| reference point | 参照点 |  | 参照类别 | ch25 | 54 | 初定 |
| loss aversion | 损失厌恶 |  | 损失规避（统一用损失厌恶） | ch09 | 64 | 初定 |
| diminishing sensitivity | 敏感度递减 |  |  | ch09 | 9 | 初定 |
| endowment effect | 禀赋效应 |  |  | ch27 | 26 | 初定 |
| risk aversion / risk seeking | 风险规避 / 风险寻求 |  |  | ch19 | 49 | 初定 |
| sure thing / sure gain / sure loss | 确定的事 / 确定的收益 / 确定的损失 |  |  | introduction | 67 | 初定 |
| fourfold pattern | 四重模式 |  |  | ch29 | 12 | 初定 |
| decision weight | 决策权重 |  |  | ch29 | 43 | 初定 |
| certainty effect / possibility effect | 确定性效应 / 可能性效应 |  |  | ch29 | 30 | 初定 |
| denominator neglect | 忽视分母 |  |  | ch30 | 6 | 初定 |
| narrow framing / broad framing | 窄框架 / 宽框架 | 把决策一个个单独看，或放在一起看 |  | ch31 | 24 | 初定 |
| framing effect / frame | 框架效应 / 框架 |  |  | introduction | 14 | 初定 |
| risk policy | 风险策略；监管语境作“风险政策” | 第 31 章：个人或机构作风险决策时遵循的规则；第 13 章说的是政府对风险的监管政策，译“风险政策” | 两个义项不要混用 | ch13 | 14 | 初定 |
| mental account / mental accounting | 心理账户 |  |  | ch32 | 28 | 初定 |
| sunk cost | 沉没成本 |  |  | ch32 | 4 | 初定 |
| disposition effect | 处置效应 |  |  | ch32 | 3 | 初定 |
| preference reversal | 偏好逆转 |  |  | ch33 | 10 | 初定 |
| joint evaluation / single evaluation | 联合评估 / 单独评估 |  |  | ch15 | 50 | 初定 |
| experiencing self / remembering self | 体验自我 / 记忆自我 |  |  | introduction | 59 | 初定 |
| peak-end rule / duration neglect | 峰终定律 / 忽视时长 |  |  | ch35 | 26 | 初定 |
| experienced well-being / life satisfaction | 体验幸福感 / 生活满意度 |  |  | introduction | 73 | 初定 |
| focusing illusion | 聚焦错觉 |  |  | ch38 | 14 | 初定 |
| U-index | U 指数 |  |  | ch37 | 9 | 初定 |
| nudge / libertarian paternalism | 助推 / 自由意志家长制 |  |  | ch17 | 12 | 初定 |
| default option / status quo | 默认选项 / 现状 |  |  | ch20 | 25 | 初定 |
| Amos Tversky | 阿莫斯·特沃斯基 |  |  | dedication | 27 | 初定 |
| Speaking of … | 说起…… | 每章结尾的小结，列出可以在闲谈中说的话 |  | ch01 | 40 | 初定 |
| fast thinking / slow thinking | 快思考 / 慢思考 |  |  | introduction | 12 | 初定 |
| agent（把两个系统比作行动者） | 主体 | 引言里“两个主体的比喻” | 代理人 | introduction | 46 | 初定 |
| character（虚构的角色） | 角色 | 系统 1 和系统 2 是故事里的两个角色 | 性格 | introduction | 25 | 初定 |
| effortful / effortless | 费力的 / 不费力的 |  |  | introduction | 39 | 初定 |
| voluntary / involuntary | 自主的 / 不由自主的 | voluntary attention 译作“主动注意” |  | ch01 | 14 | 初定 |
| working memory | 工作记忆 |  |  | ch01 | 6 | 初定 |
| Müller-Lyer illusion | 缪勒-莱尔错觉 | 中间是复姓的连字符 |  | ch01 | 8 | 初定 |
| psychopath / psychopathy | 精神病态者 / 精神病态 |  | 精神病人 | ch01 | 3 | 初定 |
| self-control | 自我控制 |  |  | ch01 | 26 | 初定 |
| impression | 印象 | 系统 1 产生的印象，与 belief（信念）对照 |  | introduction | 84 | 初定 |
| stereotype | 刻板印象 |  |  | introduction | 39 | 初定 |
| The Invisible Gorilla | 《看不见的大猩猩》 | 沿用大陆中译本书名 |  | ch01 | 2 | 初定 |

## 第二批（2026-11-04 补充）

来源：纸质版索引的 600 个概念词条、spaCy 候选词（干净原文，频次不少于 3）和 51 个定义句，统计数据在 `review/terms/`。出现次数和首次出现按干净原文统计，不含书末注释。

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| experienced utility / decision utility | 体验效用 / 决策效用 | 边沁意义上的快乐与痛苦 / 决策时的“想要程度” |  | ch35 | 21 | 初定 |
| causal / statistical base rate | 因果性基础比率 / 统计性基础比率 |  |  | ch16 | 13 | 初定 |
| Linda problem | 琳达问题 |  |  | ch15 | 16 | 初定 |
| Tom W problem | 汤姆·W 问题 |  |  | ch14 | 38 | 初定 |
| bat-and-ball problem | 球拍和球问题 |  |  | ch03 | 12 | 初定 |
| Asian disease problem | 亚洲疾病问题 |  |  | ch34 | 5 | 初定 |
| helping experiment | 助人实验 |  |  | ch16 | 8 | 初定 |
| cold-hand experiment | 冷手实验 |  |  | ch35 | 12 | 初定 |
| jumping to conclusions | 急于下结论 | 与第 7 章标题一致 |  | ch07 | 10 | 初定 |
| basic assessments | 基本评估 | 系统 1 自动进行的评估 |  | ch08 | 9 | 初定 |
| expectation principle | 期望原则 |  |  | ch29 | 7 | 初定 |
| expected value | 期望值 |  |  | ch25 | 30 | 初定 |
| value function | 价值函数 | 前景理论里的价值函数 |  | ch26 | 13 | 初定 |
| subjective probability / prior probability | 主观概率 / 先验概率 |  |  | ch15 | 31 | 初定 |
| probability distribution | 概率分布 |  |  | appendix-a-judgment-under | 9 | 初定 |
| confidence interval | 置信区间 |  |  | ch24 | 9 | 初定 |
| correlation coefficient | 相关系数 |  |  | ch17 | 4 | 初定 |
| multiple regression | 多元回归 |  |  | ch21 | 2 | 初定 |
| experience sampling | 经验取样 |  |  | ch37 | 6 | 初定 |
| sunk-cost fallacy | 沉没成本谬误 |  |  | ch23 | 6 | 初定 |
| affective forecasting | 情感预测 | 预测自己将来的感受 |  | ch38 | 4 | 初定 |
| competition neglect | 忽视竞争 |  |  | ch24 | 4 | 初定 |
| precautionary principle | 预防原则 |  |  | ch32 | 4 | 初定 |
| conjunctive / disjunctive events | 合取事件 / 析取事件 |  |  | appendix-a-judgment-under | 11 | 初定 |
| executive control | 执行控制 |  |  | ch02 | 3 | 初定 |
| formulation effects | 表述效应 |  |  | appendix-b-choices-values-and | 5 | 初定 |
| negativity dominance | 负面主导 |  |  | ch28 | 3 | 初定 |
| indifference map | 无差异曲线图 |  |  | ch27 | 9 | 初定 |
| adaptation level | 适应水平 |  |  | ch26 | 2 | 初定 |
| confirmation bias | 证实偏差 | 只找支持自己看法的证据 |  | ch07 | 2 | 初定 |
| positive test strategy | 正向检验策略 |  |  | ch07 | 1 | 初定 |
| ideomotor effect | 观念运动效应 |  |  | ch04 | 2 | 初定 |
| reference group | 参照群体 |  |  | ch18 | 2 | 初定 |
| irrational perseverance | 非理性坚持 |  |  | ch23 | 1 | 初定 |
| agency problem | 代理问题 |  |  | ch32 | 1 | 初定 |
| illusory correlation | 错觉相关 |  |  | appendix-a-judgment-under | 4 | 初定 |
| pseudo-certainty effect | 伪确定性效应 |  |  | appendix-b-choices-values-and | 1 | 初定 |
| dead-loss effect | 纯损失效应 |  |  | appendix-b-choices-values-and | 1 | 初定 |
| cash discount / credit card surcharge | 现金折扣 / 信用卡附加费 |  |  | ch34 | 8 | 初定 |
| duration-weighted | 按时长加权 |  |  | ch35 | 4 | 初定 |
| intuitive prediction / baseline prediction | 直觉预测 / 基线预测 |  |  | ch12 | 31 | 初定 |
| associative machinery | 联想机制 |  |  | ch05 | 8 | 初定 |
| 3-D heuristic | 三维启发式 |  |  | ch09 | 2 | 初定 |
| probability neglect | 忽视概率 |  |  | ch13 | 2 | 初定 |
| loss aversion ratio | 损失厌恶比率 |  |  | ch26 | 2 | 初定 |
| Moses illusion | 摩西错觉 |  |  | ch06 | 2 | 初定 |
| norm theory | 常态理论 |  |  | ch06 | 2 | 初定 |
| flow / optimal experience | 心流 / 最佳体验 | 契克森米哈赖的概念 |  | ch03 | 16 | 初定 |
| reference class forecasting | 参照类别预测 |  |  | ch23 | 1 | 初定 |
| retrievability of instances | 实例的可提取性 |  |  | appendix-a-judgment-under | 2 | 初定 |
| Save More Tomorrow | “明天多储蓄”计划 |  |  | conclusions | 2 | 初定 |
| task set | 任务定势 |  |  | ch02 | 3 | 初定 |
| hedonimeter | 快乐计 |  |  | ch35 | 8 | 初定 |
| rare event | 罕见事件 |  |  | ch14 | 20 | 初定 |
| behavioral economics | 行为经济学 |  |  | introduction | 18 | 初定 |
| illusion of skill | 技能错觉 |  |  | ch20 | 5 | 初定 |
| Add-1 task | 加 1 任务 |  |  | ch02 | 10 | 初定 |
| wheel of fortune | 幸运轮盘 | 第 11 章的锚定实验 |  | ch11 | 5 | 初定 |
| Stumbling to Happiness（原文如此） | 《撞上幸福》 | 丹尼尔·吉尔伯特的书，实际书名是 Stumbling on Happiness；原文的笔误保留，译文用中译本书名，可加译者注说明 |  | ch07 | 1 | 初定 |
| cash equivalent | 现金等值 | 和一个赌局同样有吸引力的确定金额 |  | ch30 | 5 | 初定 |
| salience / salient | 显著性 / 显著 | 作心理学概念时用：某个念头或事件在脑中有多突出，影响注意、记忆提取和决策权重（第 12、30、38 章和附录 A）；只是日常的“引人注目”时，可以写突出、醒目、显眼 |  | introduction | 21 | 初定 |
