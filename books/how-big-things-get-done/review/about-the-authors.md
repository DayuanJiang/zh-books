# 关于作者（about-the-authors）审校记录

全节 3 个块，没有注释，中英逐块对应（`site.py status` 显示 3/3）。

## 1. 译者自检

- 执行者：translation agent（Opus 5.5），译者本人。
- 范围：标题和两位作者的简介共 3 个块，对照英文检查漏译、增译、数字、金额换算、人名、书名和头衔。
- 处理：
  - 标题照术语表写“关于作者”。
  - 第 2 块：Bent Flyvbjerg 照 people-zh.tsv 写“傅以斌（Bent Flyvbjerg）”。原文一句话里并列了三个身份，最后一个是毕马威的评价，中文拆成两句：“傅以斌（Bent Flyvbjerg）是牛津大学和哥本哈根信息技术大学的教授，经济地理学家。全球会计师事务所网络毕马威（KPMG）称他是‘世界首屈一指的超大型项目专家’。”原文引语用单引号，中文用双引号。KPMG 写通行的中文名“毕马威”，括注原名。
  - 数字照“全书统一的写法”：over one hundred projects 写“100 多个项目”，$1 billion or more 写“10 亿美元及以上”。knighted by the Queen of Denmark 照术语表写“获丹麦女王授予爵士勋位”。
  - 第 3 块：三本书照术语表写《风险》（*Risk*）、《未来的胡话》（*Future Babble*）、《超预测》（*Superforecasting*），第一次出现括注原题；《纽约时报》照体例不括注。“(with Philip E. Tetlock)” 只修饰《超预测》，书名后面已经有括注的原题，中文就把合著者移到前面，写成“并与菲利普·E.泰洛克（Philip E. Tetlock）合著《超预测》”。“*New York Times* bestselling author” 写“《纽约时报》畅销书作家”，和原文一样不说明是哪本书上了畅销书榜。
- 发现并修改：对照英文重读，没有发现需要修改的意义问题。
- 检查：`python3 scripts/site.py status how-big-things-get-done` 显示 about-the-authors 为 3/3；在 `/tmp` 下的副本里把本节设成草稿，用 `framework/tools/build.py --drafts` 构建通过。中文没有破折号，也没有体例禁用的对比句式。
- 未决：
  - the world’s leading megaproject expert 译“世界首屈一指的超大型项目专家”，也可以译“全球顶尖的超大型项目专家”。

## 2. 双语审校

- 执行者：另一个独立上下文的 agent（Opus 5.5），没有参与翻译。
- 范围：标题和两位作者的简介共 3 个块，对照英文核对意义、数字和金额换算、人名、书名和头衔。审校者没有改文件，意见由编辑核实后处理。
- 发现：1 条；编辑对照英文核实后采纳 1 条，不采纳 0 条。
  - 第 2 块 “Bent Flyvbjerg is a professor at the University of Oxford and the IT University of Copenhagen, an economic geographer, and ‘the world’s leading megaproject expert’, according to global accounting network KPMG.”：原译“全球会计师事务所网络毕马威”定语太长，读者容易断成“网络毕马威”；“教授，经济地理学家”两个身份直接并排，缺一个连接词。照审校者的写法改为“……的教授，也是经济地理学家。全球性会计师事务所毕马威（KPMG）称他是……”。改法省掉了 network：毕马威由各地的成员所组成，中文一般直接称它为会计师事务所，这个细节对读者理解这句话没有影响，意思没有变。
- 不采纳：没有。这一条核实后成立。
- 审校者的总体判断：没有发现意义错误、漏译、增译或否定用反的地方，原文疑点没有需要补记的；`site.py status` 显示 3/3。意思没有错，只是第 2 块前两句读起来不顺。

## 3. 中文通读

- 执行者：编辑 agent（Opus 5.5）。
- 范围：采纳审校意见后，只看中文读完全节，再回查英文。
- 发现并修改：没有修改。改动后第 2 块“是……教授，也是经济地理学家”和第 3 块“是记者，也是《纽约时报》畅销书作家”句式相同，两位作者的简介读起来是一组。“100 多个”“10 亿美元及以上”“获丹麦女王授予爵士勋位”照体例写。第 3 块的“菲利普·E.泰洛克”带中间名缩写，和英文一致；致谢里英文写 Philip Tetlock，中文也不带缩写，两节各自照原文。
- 检查：`python3 scripts/site.py status how-big-things-get-done` 显示 about-the-authors 为 3/3；中文没有破折号，也没有体例禁用的对比句式。

## 状态

- 没有未解决的意义问题。
- 译者自检的未决项（the world’s leading megaproject expert 译“世界首屈一指”还是“全球顶尖”）仍留给主会话，审校者没有提出改动。
- 还没做的：第 4 项阅读器校样。
