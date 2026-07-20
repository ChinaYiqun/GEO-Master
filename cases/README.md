# GEO 案例库

> 从真实业务问题进入，查看别人做了什么、结果是否可信，以及你可以复制什么。

## 案例阅读原则

每个案例尽量区分四类信息：

1. **公开事实**：可以通过原文、官方页面或原始数据核验；
2. **案例方宣称**：由作者或服务商提供，但缺少独立验证；
3. **GEO-Master 分析**：根据公开材料作出的机制解释；
4. **复现实验**：用于验证方法是否具有增量效果。

不要只看标题中的订单量、提及率或增长百分比。优先检查测试问题、样本量、时间范围、平台、对照组和归因口径。

## 按地区与渠道阅读

### 海外 GEO

- [Case 001：实验室仪器 Reddit GEO——“136 单”案例拆解](b2b-industrial/case-001-lab-instrument-reddit/README.md)
- [TP-002：Ahrefs 如何用 Reddit 反向挖掘真实需求](third-party-operations/cases/TP-002-ahrefs-reddit-demand-research/README.md)
- [TP-003：Ahrefs Brand Radar 的 AI 可见性监测工作流](third-party-operations/cases/TP-003-ahrefs-brand-radar-monitoring/README.md)
- [TP-004：Tenten“Reddit GEO 三步法”拆解](third-party-operations/cases/TP-004-tenten-reddit-geo-teardown/README.md)

### 国内 GEO

- [TP-005：一个被 AI 频繁推荐的官网，长什么样？](third-party-operations/cases/TP-005-laoqian-ai-friendly-website/README.md)
- [TP-006：品牌事实库怎么搭建？](third-party-operations/cases/TP-006-lijinlong-brand-fact-base/README.md)
- [国内 GEO 原文与信源索引](../references/DOMESTIC-GEO-SOURCES.md)
- [国内 GEO 执行手册](../playbooks/DOMESTIC-GEO-PLAYBOOK.md)

## 按问题阅读

| 你遇到的问题 | 推荐案例 / 材料 |
|---|---|
| 品牌完全不被 AI 提及 | TP-006 品牌事实库、GEO 基线测试 |
| 官网有内容但不被引用 | TP-005 官网结构、Case 001 内容沉淀 |
| 不知道用户真正问什么 | TP-002 Reddit 需求挖掘 |
| 不知道怎么持续监测 | TP-003 Brand Radar、基线测试 Playbook |
| 想做 Reddit，但担心方法不合规 | TP-004 Reddit 方法拆解 |
| 看到“136 单”“提升 67%”不知道真假 | Case 001、证据评级标准 |

## 案例状态

| 状态 | 含义 |
|---|---|
| 已验证 | 关键动作和数据存在公开原始证据 |
| 可复现 | 方法可通过公开步骤重复测试 |
| 案例方宣称 | 结果来自作者或服务商，尚无独立验证 |
| 拆解中 | 已建立案例，但证据或复现实验尚未补全 |
| 有争议 | 关键结论存在冲突或无法重复出现 |
| 已失效 | 平台机制、链接或实施条件已发生重大变化 |

## 建议的案例结构

```text
case-name/
├── README.md              # 故事、动作、结果与结论
├── implementation.md      # 人员、周期、工具和执行步骤
├── mechanism.md           # 为什么可能有效
├── verification.md        # 证据、数据和归因核查
├── replication-plan.md    # 如何设计对照实验
└── assets/                # Prompt、问题库、监测表和截图
```

新案例请从根目录的 [CASE-TEMPLATE.md](../CASE-TEMPLATE.md) 开始。第三方文章的快速拆解可以使用 [第三方案例简版模板](third-party-operations/CASE-SUMMARY-TEMPLATE.md)。

## 计划中的案例

- 户外电源高购买意图问题挖掘；
- 庭院机器人负面语料治理；
- 智能安防品牌 AI 提及率变化；
- 产品参数更新后 AI 仍引用旧版本；
- GEO 提及增加但没有询盘的失败案例；
- 国内多平台同一问题回答差异实验。

提交案例线索时，请同时提供原始标题、来源、发布日期、链接和关键结果宣称。