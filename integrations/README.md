# GEO-Master 工具生态与集成架构

GEO-Master 正在从资料、模板和独立 Skill 工具箱升级为一套可插拔的 GEO Operating System：

```text
研究与基准
→ 品牌事实治理
→ 真实问题地图
→ 网站与内容审计
→ 内容生产和审核
→ 多站点发布
→ 多模型持续监测
→ 引用选择与吸收实验
→ SEO 与流量联动
→ 询盘和订单归因
```

## 平台架构

完整设计见：

- [GEO-Master 平台架构蓝图](../docs/GEO-MASTER-PLATFORM-ARCHITECTURE.md)
- [机器可读上游能力注册表](upstream-capabilities.json)
- [能力注册表 JSON Schema](../schemas/integration-registry.schema.json)
- [注册表校验脚本](../scripts/validate_integration_registry.py)

GEO-Master 不是把外部仓库整仓复制进来，而是采用：

```text
吸收能力与架构
+ 统一事实、问题、实验和证据契约
+ 提供 CLI / HTTP / Library / Data Import Adapter
+ 保留上游独立部署和许可证责任
```

## 三层职责

### GEO-Master Core

负责跨工具必须稳定的部分：

- 品牌、产品、声明和来源；
- 问题、意图、市场、语言和人群；
- 实验、对照、版本和证据；
- 提及、官网引用、推荐和事实准确性；
- 竞品、引用页面和 Share of Voice；
- 访问、询盘、报价和订单的独立归因；
- 许可证、隐私、安全和人工审核边界。

### GEO-Master Adapters

负责把外部工具接入统一契约：

- 技术审计器；
- 内容分析和改写器；
- RAG 与内容任务系统；
- 多站发布系统；
- Prompt 与引用监测平台；
- GSC、SERP、外链和流量数据；
- 人工测试表、浏览器自动化和第三方导出。

### External Runtimes

负责上游项目自己的：

- UI 和管理后台；
- 模型调用；
- 调度、队列和数据库；
- 抓取供应商；
- 部署、升级和安全；
- 原始许可证义务。

## 能力地图

| 能力层 | GEO-Master 入口 | 已吸收或计划对接的上游能力 |
|---|---|---|
| 研究与基准 | Citation Lab、案例与实验 Schema | `GEO-optim/GEO`、`cxcscmu/AutoGEO`、`geo-citation-lab` |
| 品牌事实 | `brand-facts.yaml`、`claims-and-sources.csv` | GEO-Master 原生能力 |
| 网站审计 | `geo-master` Skill | GeoReady、`geo-seo-claude`、GEORank、aeo.js |
| AI 可读层 | 审计和内容产物 | Dualmark、aeo.js、LLMS Generator Toolkit、llms.txt |
| 内容分析 | Content Brief、Citation Lab | GEO Analyzer、AutoGEO、Agent Skills |
| 内容运营 | `geo-master workflow` | GEOFlow、GEORank |
| 多站发布 | 外部 Adapter | GEOFlow Agent、WordPress REST、HTTP、静态站 |
| 持续监测 | `geo-master-monitor` | Getcito、Gego、Searchstack、Elmo、GEO/AEO Tracker |
| 引用研究 | `geo-master-citation-lab` | GEO Citation Lab、GEO-Bench、真实平台复测 |
| SEO 联动 | Adapter 与报告 | Searchstack、GSC、SERP、外链和 AI Referral |
| Agent 编排 | 三个 GEO-Master Skills | Aaron Marketing Skills、Digital Marketing Pro 的工作流思想 |
| 业务归因 | `lead-attribution.csv` | GEO-Master 原生证据边界 |

完整项目清单、许可证、吸收状态、差异化和禁止项以 [`upstream-capabilities.json`](upstream-capabilities.json) 为准。

## 当前覆盖的上游项目

机器注册表当前纳入：

1. `GEO-optim/GEO`
2. `cxcscmu/AutoGEO`
3. `yaojingang/GEOFlow`
4. `yaojingang/GEORank`
5. `ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool`
6. `AI2HU/gego`
7. `alexpospekhov/searchstack-aeo`
8. `Auriti-Labs/geo-optimizer-skill`
9. `houtini-ai/geo-analyzer`
10. `dodopayments/dualmark`
11. `multivmlabs/aeo.js`
12. `aaron-he-zhu/aaron-marketing-skills`
13. `indranilbanerjee/digital-marketing-pro`
14. `jeredhiggins/llms-generator-toolkit`
15. `AnswerDotAI/llms-txt`
16. `zubair-trabzada/geo-seo-claude`
17. `yaojingang/geo-citation-lab`
18. `elmohq/elmo`
19. `danishashko/geo-aeo-tracker`

“纳入”不等于复制。每个项目有独立的集成模式：

- `reference-standard`：作为标准或研究基线；
- `concept-only`：吸收方法、架构或工作流；
- `clean-room-reimplementation`：根据公开能力重新设计实现；
- `cli-adapter`：调用上游 CLI 并标准化输出；
- `library-adapter`：作为可选库集成；
- `external-service-adapter`：通过 HTTP 或进程边界连接；
- `data-importer`：导入上游导出数据。

## 三个 Agent Skills

### `geo-master`

统一完成：

- 网站快速诊断和完整审计；
- 品牌事实与来源治理；
- 基线问题设计；
- 内容规划、审核和发布链路设计；
- 优化前后验证。

### `geo-master-citation-lab`

研究：

```text
搜索是否触发
→ 哪些来源被选择
→ 引用内容是否进入答案
→ 品牌与产品实体是否曝光
→ Web、App、地区、语言和平台是否不同
```

### `geo-master-monitor`

负责：

- 多平台、多模型、多地区运行；
- 品牌和竞品提及、引用、推荐与准确性；
- 引用域名和页面机会；
- 历史趋势和漂移告警；
- 周报、月报与商业归因衔接；
- 外部监测工具数据导入。

## 推荐组合

### 轻量诊断

```text
geo-master quick
→ 修正关键事实和页面问题
→ 用 baseline-query-set.csv 建立基线
→ 优化后重跑同一问题
```

### 技术型独立站

```text
GeoReady / aeo.js 审计
→ Dualmark 或 aeo.js 提供 AI 可读页面
→ GEO-Master 保存底层 Finding
→ 多模型基线复测
```

### 企业内容运营

```text
品牌事实与问题地图
→ GEOFlow 知识库和内容任务
→ 人工事实审核
→ 多站点发布
→ Getcito / Gego / Elmo 持续监测
→ Citation Lab 解释引用变化
```

### SEO 与 GEO 联动

```text
Searchstack / GSC / SERP / 外链
→ GEO-Master 问题和页面机会
→ 内容或技术改造
→ AI 引用与传统搜索同时复测
```

### 国内 AI 搜索

```text
中文品牌事实
→ DeepSeek / 豆包 / 元宝 / Kimi / 通义问题集
→ 分平台、地区、登录和界面记录
→ 引用与事实准确性人工复核
→ 与国际平台结果分开报告
```

## 数据兼容原则

外部工具最终应映射到稳定数据结构：

```text
project_id
prompt_id
run_id
provider
model_label
collection_method
country
language
interface
account_state
conversation_state
answer_reference
citation_url
brand_mentioned
official_site_cited
explicitly_recommended
fact_accuracy
evidence_state
```

外部综合分可以保留，但必须同时导出底层观测项，避免一个数字掩盖：

- 负面提及；
- 参数错误；
- 引用消失；
- 样本不平衡；
- 平台缺失；
- 抓取失败；
- 地区和界面差异；
- 供应商表示与消费者界面差异。

## 许可证边界

| 类型 | GEO-Master 集成原则 |
|---|---|
| MIT / Apache-2.0 | 可适配或独立重实现；复制实质代码时保留版权、许可证、修改说明和 NOTICE |
| GPL | 仅通过 HTTP、CLI 或独立进程边界集成，不复制进 MIT Core |
| CC BY / 混合许可 | 代码和内容分别处理，按材料署名和核验第三方权利 |
| 未确认或受限材料 | 只记录链接、字段、方法和复现步骤，不复制资产或正文 |

CI 会运行：

```bash
python scripts/validate_integration_registry.py
```

它校验：

- JSON Schema；
- 能力和上游 ID 唯一性；
- 上游引用的能力是否存在；
- GPL 是否保持进程边界；
- 每个上游是否记录保留能力、差异化和禁止项。

## 下一步实施顺序

```text
1. 审计 Adapter：GeoReady / aeo.js / Dualmark
2. 监测 Adapter：Getcito / Gego / Searchstack
3. 完成 Elmo / GEO-AEO Tracker 导入测试
4. GEOFlow 项目、事实、问题和任务 ID 映射
5. Adapter Result Schema 与 SDK
6. 轻量 Dashboard 和报告
```

需要面向真实企业部署、实施与长期运营时，可查看维护者提供的 **[GEO 产品化方案](https://tst.ahupo.cn/intro?utm_source=github&utm_medium=repository&utm_campaign=geo-master&utm_content=integrations-bottom)**。
