# 术语表

翻译前根据 `review/terms/` 里的统计数据裁定（来源和门槛见 [review/terms/README.md](review/terms/README.md)）。“出现次数”和“首次出现”由脚本按英文词形统计，不含脚注；按正则匹配，可能把同词根的普通用法也算进去。状态都是“初定”，由 Claude 裁定，等用户确认；改动时要回查已经译完的章节。

## 体例

- **人名**：用 [review/terms/people-zh.tsv](review/terms/people-zh.tsv) 的译名。每章第一次出现时在中文名后括注英文原名，例如“山姆·奥特曼（Sam Altman）”，之后只写中文。脚注里的人名照写原文。
- **机构、产品、代号**：见下面“机构、产品与地名”。没有通行中文名的公司和产品照写原名，和汉字之间加空格。
- **书名、报刊、电影、论文**：正文里用《》，第一次出现时括注原题；脚注里的出处保留原文，不加书名号。
- **数字**：年份、日期、百分比和多位数字用阿拉伯数字，和汉字之间加空格，例如“2023 年 11 月 17 日”“5 名董事”。金额换算成中文的万、亿：$10 billion 写“100 亿美元”，$1.5 million 写“150 万美元”。英制单位照原文，必要时括注公制。第 13 章的 10²⁶ 照写。
- **引语**：推文、Slack 消息、邮件和对话按原文的语气译，口语就译成口语，粗话保留力度。奥特曼推文里全用小写字母的风格，中文不必模仿。
- **脚注**：开头粗体的是正文里被注释的词句，译成对应的中文，保留粗体和冒号，例如 `[^1]: **“我能帮什么忙”：** Tripp Mickle, Cade Metz, ...`。后面的出处（作者、标题、刊名、日期、网址、页码、案号）保留英文原样；解释性的句子要翻译。常见格式：
  - Author interview with Daniel Pena, May 2024. → 作者对 Daniel Pena 的采访，2024 年 5 月。
  - Author correspondence with X → 作者与 X 的通信
  - Documents viewed by the author → 作者看过的文件
  - [inactive] → [已失效]
- **脚注标记**：`[^n]` 放在中文里对应词句的后面，编号与英文一致。
- **分隔线和表情**：分隔线 `---` 只写在英文文件里；表情符号照写。
- **破折号和句式**：中文译文不用破折号（——），原文的破折号按意思改成逗号、冒号、括号或另起一句；也不用“不是……而是……”这种句式，换成直接的说法。全书已经译完的部分都遵守这一条。

## 各节标题

| 章节 id | 英文 | 中文标题（`#` 一级标题照这一列写） |
| --- | --- | --- |
| dedication | Dedication | 献辞 |
| epigraph | Epigraph | 题词 |
| authors-note | Author’s Note | 作者说明 |
| prologue | Prologue: A Run for the Throne | 序章 问鼎王座 |
| ch01 | 1. Divine Right | 第 1 章 君权神授 |
| ch02 | 2. A Civilizing Mission | 第 2 章 教化使命 |
| ch03 | 3. Nerve Center | 第 3 章 神经中枢 |
| ch04 | 4. Dreams of Modernity | 第 4 章 现代化之梦 |
| ch05 | 5. Scale of Ambition | 第 5 章 野心的规模 |
| ch06 | 6. Ascension | 第 6 章 登顶 |
| ch07 | 7. Science in Captivity | 第 7 章 被俘获的科学 |
| ch08 | 8. Dawn of Commerce | 第 8 章 商业的黎明 |
| ch09 | 9. Disaster Capitalism | 第 9 章 灾难资本主义 |
| ch10 | 10. Gods and Demons | 第 10 章 神与魔 |
| ch11 | 11. Apex | 第 11 章 巅峰 |
| ch12 | 12. Plundered Earth | 第 12 章 被掠夺的大地 |
| ch13 | 13. The Two Prophets | 第 13 章 两位先知 |
| ch14 | 14. Deliverance | 第 14 章 救赎 |
| ch15 | 15. The Gambit | 第 15 章 险招 |
| ch16 | 16. Cloak-and-Dagger | 第 16 章 密谋 |
| ch17 | 17. Reckoning | 第 17 章 清算 |
| ch18 | 18. A Formula for Empire | 第 18 章 帝国的公式 |
| epilogue | Epilogue: How the Empire Falls | 尾声 帝国如何崩塌 |
| acknowledgments | Acknowledgments | 致谢 |
| about-the-author | About the Author | 关于作者 |

译者读完一章后，如果觉得标题另有更贴切的译法，在汇报里提出，由主会话统一修改。

## 核心概念

| 英文 | 首选译法 | 适用的意思 | 不要混同 | 首次出现 | 出现次数 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| empire / empires of AI | 帝国 / AI 帝国 | 全书的核心比喻：像殖民帝国一样攫取资源、剥削劳动、垄断知识的 AI 巨头 | 王国、企业集团 | prologue | 47 | 初定 |
| colonialism / colonial | 殖民主义 / 殖民的 |  |  | prologue | 16 | 初定 |
| AI colonialism | AI 殖民主义 | 作者早年报道系列的名字 |  | acknowledgments | 1 | 初定 |
| data colonialism | 数据殖民主义 | Couldry 和 Mejias 提出的概念 |  | ch04 | 2 | 初定 |
| extractivism | 攫取主义 | 拉美学者的概念：为少数人掠夺土地、资源和劳动的经济秩序；首次出现括注原文 | 采掘业（只指行业时才用） | ch04 | 7 | 初定 |
| extraction / extract | 攫取 / 开采（看对象） | 资源用“开采”，财富、价值、劳动用“攫取” |  | prologue | 18 | 初定 |
| dispossession | 剥夺 | 夺走土地、水和其他资源；献辞里的 refuse dispossession 译“拒绝被剥夺” |  | dedication | 6 | 初定 |
| civilizing mission | 教化使命 | 第 2 章标题，殖民帝国用来为扩张辩护的说法 | 文明的使命 | ch02 | 1 | 初定 |
| disaster capitalism | 灾难资本主义 | 第 9 章标题，娜奥米·克莱恩的概念 |  | ch09 | 1 | 初定 |
| surveillance capitalism | 监控资本主义 |  |  | ch04 | 4 | 初定 |
| Global South / Global North | 全球南方 / 全球北方 |  | 第三世界 | prologue | 17 | 初定 |
| AGI / artificial general intelligence | AGI / 通用人工智能 | 正文里写 AGI 的照写 AGI；写全称的译“通用人工智能”，第一次出现时括注 AGI | 强人工智能 | prologue | 157 | 初定 |
| AI / artificial intelligence | AI / 人工智能 | 原文写 AI 的照写 AI，写全称的译“人工智能” |  | epigraph | 25 | 初定 |
| beneficial AGI / benefits all of humanity | 有益的 AGI / 造福全人类 | OpenAI 使命里的说法 |  | prologue | 17 | 初定 |
| mission (OpenAI's) | 使命 | OpenAI 的使命 | 任务 | epigraph | 78 | 初定 |
| scale / scaling | 规模 / 扩大规模、规模化 | 作者批评的核心逻辑：不断加大数据、算力和模型；动词 scale 译“扩大规模” | 缩放、伸缩 | authors-note | 207 | 初定 |
| scaling laws | 规模定律 | OpenAI 研究人员命名的经验规律 | 缩放定律、扩展定律 | ch04 | 14 | 初定 |
| OpenAI’s Law | OpenAI 定律 | 仿照摩尔定律的说法 |  | ch02 | 7 | 初定 |
| compute | 算力 | 名词：训练和运行模型用的计算资源；动词用法按上下文译“计算” | 计算机 | ch02 | 91 | 初定 |
| data center / campus / megacampus | 数据中心 / 园区 / 超大型园区 |  |  | prologue | 102 | 初定 |
| hyperscaler | 超大规模云服务商 | 亚马逊、微软、谷歌、Meta 这样的大型云计算公司 |  | ch12 | 7 | 初定 |
| chip / GPU / TPU | 芯片 / GPU / TPU | 第一次出现时 GPU 写“图形处理器（GPU）” |  | authors-note | 74 | 初定 |
| large language model (LLM) | 大语言模型 |  | 大型语言模型 | prologue | 35 | 初定 |
| language model | 语言模型 |  |  | prologue | 61 | 初定 |
| generative AI | 生成式 AI |  | 生成 AI | prologue | 68 | 初定 |
| model / AI model | 模型 |  |  | authors-note | 564 | 初定 |
| training / training data | 训练 / 训练数据 |  |  | authors-note | 198 | 初定 |
| parameters | 参数 |  |  | ch02 | 19 | 初定 |
| model weights | 模型权重 / 权重 |  |  | ch06 | 12 | 初定 |
| inference / inferencing | 推理 | 运行训练好的模型；reasoning 也译“推理”，两者同时出现时 inference 写“推理（运行模型）” |  | ch04 | 7 | 初定 |
| capabilities | 能力 | 模型的能力；capabilities research 译“能力研究” |  | ch02 | 92 | 初定 |
| frontier model | 前沿模型 |  |  | ch13 | 11 | 初定 |
| multimodal | 多模态 |  |  | ch04 | 11 | 初定 |
| deep learning / neural network | 深度学习 / 神经网络 |  |  | ch02 | 142 | 初定 |
| connectionism / connectionists | 联结主义 / 联结主义者 |  | 连接主义 | ch04 | 18 | 初定 |
| symbolism / symbolists | 符号主义 / 符号主义者 |  |  | ch04 | 8 | 初定 |
| expert systems | 专家系统 |  |  | ch04 | 5 | 初定 |
| AI winter | AI 寒冬 |  |  | ch04 | 1 | 初定 |
| machine learning | 机器学习 |  |  | ch02 | 16 | 初定 |
| reinforcement learning / RLHF | 强化学习 / 基于人类反馈的强化学习（RLHF） | 第一次出现写全称再括注 RLHF，之后写 RLHF |  | ch05 | 39 | 初定 |
| pure language hypothesis / grounding hypothesis | 纯语言假说 / 具身假说 | 前者认为只靠语言数据就能达到 AGI，后者认为还要接触视觉等其他感知 |  | ch05 | 13 | 初定 |
| hallucinations | 幻觉 | 作者认为这个词本身有误导性，注意保留引号 |  | ch04 | 9 | 初定 |
| chatbot | 聊天机器人 |  |  | epigraph | 36 | 初定 |
| prompt | 提示词 / 输入提示 | 名词作“提示词”，动词作“输入……提示”或按上下文 |  | ch04 | 38 | 初定 |
| open source / open-source | 开源 |  |  | ch02 | 17 | 初定 |
| API | API |  |  | ch03 | 49 | 初定 |
| red teaming | 红队测试 |  |  | ch08 | 3 | 初定 |
| distillation | 蒸馏 |  |  | ch08 | 2 | 初定 |
| diffusion model | 扩散模型 |  |  | ch04 | 16 | 初定 |
| superintelligence | 超级智能 |  |  | prologue | 15 | 初定 |
| AI safety / safety | AI 安全 / 安全 | 研究和应对 AI 可能造成的灾难性后果 | 安保（security） | prologue | 209 | 初定 |
| security | 安保 / 安全（按搭配） | 公司安保、信息安全；cybersecurity 译“网络安全”；national security 译“国家安全” |  | prologue | 38 | 初定 |
| Trust and Safety | 信任与安全团队 | 负责产品滥用和内容政策的团队 | AI 安全 | ch08 | 18 | 初定 |
| alignment / superalignment | 对齐 / 超级对齐 |  |  | ch01 | 29 | 初定 |
| existential risk / x-risk | 生存风险 | 可能毁灭人类的风险；existential threat 译“生存威胁” | 存在主义 | ch01 | 37 | 初定 |
| rogue AI | 失控的 AI |  |  | ch02 | 7 | 初定 |
| p(doom) | p(doom)（末日概率） |  |  | ch10 | 5 | 初定 |
| effective altruism (EA) / effective altruists | 有效利他主义 / 有效利他主义者 |  |  | ch02 | 40 | 初定 |
| effective accelerationism (e/acc) | 有效加速主义（e/acc） |  |  | ch10 | 3 | 初定 |
| Doomers / Boomers | 末日派 / 繁荣派 | 公司内部对两派人的俗称：担心 AI 灾难的一派和主张加快商业化的一派；Boomer 是对 Doomer 的谐音，第一次出现时括注原文并加译者注 | 婴儿潮一代 | ch10 | 43 | 初定 |
| Exploratory Research / Safety / Startup clan | 探索研究派 / 安全派 / 创业派 | 奥特曼划分的三个“派系”（clan） | 部落、氏族 | ch06 | 34 | 初定 |
| Applied division / Research division | 应用部门 / 研究部门 |  |  | ch06 | 34 | 初定 |
| The Blip | “插曲” | 员工对奥特曼被解雇又复职那几天的叫法，第一次出现时括注 The Blip，并加译者注说明 blip 既指短暂的波动，也指漫威电影里一半人类消失又回来的事件 |  | ch16 | 7 | 初定 |
| Omnicrisis | 全面危机 | 员工造的词，指 2024 年接连爆发的丑闻和离职潮；第一次出现时括注原文 |  | ch17 | 10 | 初定 |
| The Divorce | “分家” | 达里奥·阿莫迪等人离开 OpenAI、创办 Anthropic |  | ch06 | 6 | 初定 |
| not consistently candid | 没有始终坦诚 | 董事会解雇奥特曼时的措辞，全书引用时保持一致 |  | prologue | 4 | 初定 |
| board / independent directors | 董事会 / 独立董事 |  |  | prologue | 242 | 初定 |
| nonprofit / for-profit / capped-profit | 非营利 / 营利 / 利润封顶 | capped-profit structure 译“利润封顶结构” |  | prologue | 88 | 初定 |
| clawback clause / nondisparagement | 追回条款 / 不得贬损协议 |  |  | ch17 | 14 | 初定 |
| vested equity / tender offer | 已归属股权 / 要约收购（员工股份出售） | tender offer 在书里是让员工出售股份的定向要约，译“股份收购要约” |  | prologue | 14 | 初定 |
| data annotation / labeling / annotators | 数据标注 / 标注员 |  |  | prologue | 33 | 初定 |
| data workers | 数据工作者 |  |  | ch05 | 10 | 初定 |
| content moderation / moderators | 内容审核 / 审核员 |  |  | ch05 | 14 | 初定 |
| crowd work / crowdworkers | 众包工作 / 众包工人 |  |  | ch09 | 1 | 初定 |
| contractors | 外包人员 / 承包商（按上下文） |  |  | authors-note | 12 | 初定 |
| hype | 炒作 |  |  | prologue | 8 | 初定 |
| abundance | 富足 | 献辞里的 in the name of abundance 译“以富足之名” |  | dedication | 6 | 初定 |
| accountability | 问责 | AI accountability 译“AI 问责” |  | ch02 | 26 | 初定 |
| governance / regulation | 治理 / 监管 |  |  | prologue | 46 | 初定 |
| startup accelerator / batch | 创业加速器 / 一期（batchmates 译“同期创业者”） |  |  | ch01 | 12 | 初定 |
| stochastic parrots | 随机鹦鹉 | 论文标题《论随机鹦鹉的危险》 |  | ch07 | 8 | 初定 |
| iterative deployment | 迭代部署 | OpenAI 的产品发布思路：边发布边改进 |  | ch13 | 5 | 初定 |
| Superassistant | 超级助手 | OpenAI 内部团队名，ChatGPT 界面出自这个团队 |  | ch10 | 13 | 初定 |
| Estallido Social | “社会大爆发” | 智利 2019 年开始的大规模抗议，第一次出现时括注西班牙语原文 |  | ch12 | 2 | 初定 |
| kaitiakitanga | kaitiakitanga（守护） | 毛利语概念，照写原文并括注意思 |  | epilogue | 1 | 初定 |
| Feel the AGI | 感受 AGI | 苏茨克维的口头禅 |  | ch05 | 3 | 初定 |
| Intelligence Age | 智能时代 |  |  | prologue | 2 | 初定 |

## 机构、产品与地名

| 英文 | 译法 | 说明 |
| --- | --- | --- |
| OpenAI / Anthropic / DeepMind / Meta / xAI | 照写原名 |  |
| Microsoft / Google / Nvidia / Amazon / Apple | 微软 / 谷歌 / 英伟达 / 亚马逊 / 苹果 |  |
| Facebook / Tesla / SpaceX / Y Combinator (YC) | Facebook / 特斯拉 / SpaceX / Y Combinator（YC） |  |
| Baidu / Alibaba / Uber / Airbnb | 百度 / 阿里巴巴 / 优步 / 爱彼迎 |  |
| Sama / Scale AI / Remotasks / Appen / CloudFactory | 照写原名 | 数据标注外包公司 |
| ChatGPT / GPT-4 / DALL-E / Codex / Whisper | 照写原名 | 产品和模型名 |
| code names: Arrakis, Scallion, Strawberry, Orion, Gobi, Omni, Sky, Nest | 照写原名，第一次出现时括注中文意思 | 例如 Strawberry（草莓） |
| The New York Times / The Wall Street Journal / The Washington Post | 《纽约时报》/《华尔街日报》/《华盛顿邮报》 |  |
| The Atlantic / Wired / Time / MIT Technology Review / The Information | 《大西洋月刊》/《连线》/《时代》/《麻省理工科技评论》/《The Information》 |  |
| MIT / Stanford / UC Berkeley | 麻省理工学院 / 斯坦福大学 / 加州大学伯克利分校 |  |
| Kenya / Chile / Uruguay / Colombia / Venezuela | 肯尼亚 / 智利 / 乌拉圭 / 哥伦比亚 / 委内瑞拉 |  |
| Atacama Desert / Santiago / Nairobi | 阿塔卡马沙漠 / 圣地亚哥 / 内罗毕 |  |
| Māori / te reo Māori | 毛利人 / 毛利语 |  |
