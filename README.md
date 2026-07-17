# GEO-Master

> 中国品牌出海 GEO 实战案例库、SOP 与复现实验。

[![GitHub stars](https://img.shields.io/github/stars/ChinaYiqun/GEO-Master?style=social)](https://github.com/ChinaYiqun/GEO-Master/stargazers)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Cases](https://img.shields.io/badge/cases-building-orange.svg)](cases/)

GEO-Master 研究中国品牌如何被 ChatGPT、Perplexity、Gemini、Claude 和 Google AI Search **发现、理解、引用与推荐**。

这里不堆砌空泛概念，也不把服务商截图直接当成成功证据。每个主题尽量按照以下结构展开：

**真实业务问题 → 案例拆解 → 具体实施 → 技术解释 → 数据验证 → 可复用模板 → 失败复盘**

## 为什么做这个项目

现有 GEO 项目大多偏向通用教程、学术论文或自动化工具。GEO-Master 的重点是：

- 面向中国品牌出海、B2B 外贸、消费电子、机器人、SaaS 与跨境电商；
- 用 CASE 驱动，而不是先讲一整本技术教科书；
- 同时记录成功案例、失败案例和无法验证的营销宣称；
- 提供可以直接复制的 SOP、Prompt、监测表和内容模板；
- 逐步公开自有复现实验和长期数据。

## 从这里开始

- [新读者入口：我应该先看什么？](START-HERE.md)
- [第三方 GEO 运营案例与公众号观察](cases/third-party-operations/README.md)
- [第三方运营案例索引](cases/third-party-operations/CASE-INDEX.md)
- [案例模板](CASE-TEMPLATE.md)
- [证据与案例评级标准](EVIDENCE-STANDARD.md)
- [90 天迭代路线](ROADMAP.md)
- [参与贡献](CONTRIBUTING.md)

## 当前重点案例

| Case | 场景 | 核心链路 | 状态 |
|---|---|---|---|
| [Case 001：实验室仪器 Reddit GEO](cases/b2b-industrial/case-001-lab-instrument-reddit/README.md) | B2B 外贸 | Reddit + Perplexity + Ahrefs + 官网内容 | 已发布初版 |
| Case 002：户外电源采购问题挖掘 | 消费电子 | 社区问题 + 对比内容 + AI 引用 | 待核验 |
| Case 003：庭院机器人负面讨论治理 | 机器人 | 负面语料 + 内容修正 + 提及率监测 | 待核验 |
| Case 004：智能安防品牌 AI 可见性 | 智能家居 | 官网 + 社区 + Perplexity 监测 | 待核验 |
| Case 005：产品参数更新后 AI 仍引用旧数据 | 通用 | 实体一致性 + Freshness + 引用纠错 | 计划中 |

> 所有结果数字都会标记为“已验证”“可复现”“案例方宣称”或“无法验证”。

## 第三方运营案例与公众号观察

单独整理持续产出 GEO 内容的公众号、服务商、行业媒体和项目主理人，并将其中有价值的运营案例拆成标准 CASE。

- 账号名单只作为**观察池**，不等于推荐或背书；
- 文章中的订单、提及率、转化率默认按“案例方宣称”处理；
- 每个正式案例都要记录来源、动作、数据口径、证据等级、合规风险和复现实验；
- 公众号原文只做必要摘要，不大段复制。

当前观察池包括老钱聊GEO、招财兔 GEO、硅星人Pro、壹通GEO、GEO标准、柏导叨叨、盒创GEO流量前沿、极亿欧、AI研究实验室等内容产出方。

查看：[第三方 GEO 运营案例与公众号观察](cases/third-party-operations/README.md)

## 每个 CASE 包含什么

一个完整 CASE 不只是一篇文章，而是一组可以直接执行的材料：

```text
case-xxx-name/
├── README.md              # 30 秒摘要与完整故事
├── implementation.md      # 实施步骤、人员、周期和工具
├── mechanism.md           # 为什么可能有效
├── verification.md        # 数据、证据和归因核查
├── replication-plan.md    # 如何复现实验
└── assets/                # Prompt、问题库、监测表和内容模板
```

## 核心内容地图

### 1. CASE：先看别人到底做了什么

- B2B 工业品如何从采购问题切入；
- 消费电子如何进入 AI 对比与推荐答案；
- Reddit、YouTube、Quora、LinkedIn 与官网如何协同；
- AI 提及率提高但没有询盘时，问题出在哪里；
- 服务商“成功案例”中的数据是否经得起验证；
- 国内公众号和服务商运营案例中，哪些动作真正可以复现。

### 2. Playbook：拿去就能执行

- GEO 基线测试；
- Reddit 社区参与；
- 产品页与对比页改造；
- AI 引用监测；
- 品牌实体一致性检查；
- GEO 询盘与订单归因。

### 3. Explainers：只讲案例需要的技术

- 为什么被 Google 收录不等于会被 AI 引用；
- Query Fan-out 如何改变关键词研究；
- Passage Retrieval 为什么更关注段落而非整页；
- 品牌提及、官网引用和推荐进入榜单有什么区别；
- 抓取、索引、召回、重排、生成与引用选择的完整链路。

### 4. Templates：减少重复劳动

- CASE 收集表；
- 采购问题库；
- AI 可见性基线问题集；
- 每周监测表；
- Reddit 回复检查清单；
- 内容 Brief；
- 询盘和订单归因表；
- [第三方运营案例简版模板](cases/third-party-operations/CASE-SUMMARY-TEMPLATE.md)。

## 我们不会做什么

- 不把一次 ChatGPT 回答当成稳定结论；
- 不把 Ahrefs 外链数据等同于 AI 推荐；
- 不伪装普通用户发布品牌营销内容；
- 不建议批量生成低价值社区回复；
- 不保证“修改几个标签就能被大模型收录”；
- 不替无法独立验证的订单数字背书。

## 贡献方式

欢迎提交：

- 可核验的 GEO 案例；
- 失败案例与踩坑记录；
- 平台变化和复现实验；
- 工具、数据集、Prompt 与模板；
- 公众号、演讲、访谈和服务商案例线索；
- 对已有案例证据链的补充或质疑。

开始前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## Star 与关注

这个仓库会持续更新真实案例、复现实验和可下载模板。觉得方向有价值，可以 Star 以便跟踪后续更新。

## License

MIT License。案例引用、截图和第三方材料仍遵循其原始版权与使用规则。