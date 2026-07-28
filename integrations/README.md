# GEO-Master 工具生态与集成架构

GEO-Master 不再只是一套文章、案例和模板。项目正在形成一条完整的 GEO 工作链：

```text
网站审计
→ 品牌事实治理
→ 真实问题基线
→ 内容生产与审核
→ 多站点发布
→ 多模型持续监测
→ 引用选择与吸收研究
→ 业务归因与复盘
```

## 能力地图

| 能力层 | GEO-Master 中的入口 | 参考或可对接项目 | 解决的问题 |
|---|---|---|---|
| 网站审计 | [geo-master Skill](../.agents/skills/geo-master/SKILL.md) | `zubair-trabzada/geo-seo-claude` | 爬虫、内容、Schema、事实冲突和技术基础 |
| 事实与证据 | 模板、案例标准、基线 Playbook | GEO-Master 原生能力 | 品牌和产品信息是否一致、可靠、可追溯 |
| 内容运营 | `geo-master` 的 `workflow` 模式 | `yaojingang/GEOFlow` | 知识库、RAG、生成、审核、发布和多站分发 |
| 实证研究 | [geo-master-citation-lab Skill](../.agents/skills/geo-master-citation-lab/SKILL.md) | `yaojingang/geo-citation-lab` | 引用选择、内容吸收、实体曝光和界面差异 |
| 持续监测 | [geo-master-monitor Skill](../.agents/skills/geo-master-monitor/SKILL.md) | `elmohq/elmo`、`danishashko/geo-aeo-tracker` | 多模型运行、竞品、引用、趋势、地域和告警 |
| 商业实施 | [GEO 产品介绍](https://tst.ahupo.cn/intro?utm_source=github&utm_medium=repository&utm_campaign=geo-master&utm_content=integrations) | 项目维护者产品 | 面向真实企业的部署、运营、监测和支持 |

## 三个可调用 Skill

### 1. `geo-master`

统一完成网站诊断、品牌事实治理、基线设计、内容规划、GEOFlow 式运营链路和优化前后验证。

重点原则：

- 不用“玄学总分”代替证据；
- 不把爬虫可访问等同于平台一定收录；
- 不把一次回答等同于稳定排名；
- 不把订单直接归因给 GEO。

### 2. `geo-master-citation-lab`

把 AI 搜索拆成可测量环节：

```text
搜索是否触发
→ 哪些来源被选择
→ 引用页面内容是否进入答案
→ 哪些品牌和实体被呈现
→ Web、App、地区和平台之间有何差异
```

它可以接入外部公开研究，但默认只保存数据清单、字段映射、查询和复现方法，不把大型数据集或论文 PDF 直接搬进仓库。

### 3. `geo-master-monitor`

负责真实的长期监测：

- 多平台、多模型和多地区 Prompt 运行；
- 品牌与竞品提及、引用、推荐和准确率；
- 引用域名与页面机会；
- 历史趋势和漂移告警；
- 周报、月报和商业归因衔接；
- 对接 Elmo 或 GEO/AEO Tracker 等自托管系统。

## 推荐组合

### 轻量诊断

```text
geo-master quick
→ 修正关键事实和页面问题
→ 使用 baseline-query-set.csv 建立基线
```

### 企业持续运营

```text
geo-master audit
→ GEOFlow 式内容生产与审核
→ geo-master-monitor 定时运行
→ geo-master-citation-lab 分析引用变化
→ lead-attribution.csv 记录后续业务结果
```

### 服务商或咨询团队

```text
客户网站审计
→ 证据化问题清单
→ 可执行内容 Brief
→ 持续监测看板
→ 优化前后对照报告
→ 明确归因边界的客户复盘
```

需要面向真实企业落地时，可查看维护者提供的 **[GEO 产品化方案](https://tst.ahupo.cn/intro?utm_source=github&utm_medium=repository&utm_campaign=geo-master&utm_content=integrations-bottom)**。

## 数据兼容原则

所有工具最终应尽量映射到 GEO-Master 的稳定数据结构：

```text
prompt_id
run_id
provider
model_label
market
language
interface
answer_reference
citation_url
brand_mentioned
official_site_cited
explicitly_recommended
fact_accuracy
evidence_state
```

外部工具的综合分可以保留，但必须同时导出底层观测项，避免一个分数掩盖：

- 负面提及；
- 参数错误；
- 引用消失；
- 样本不平衡；
- 平台缺失；
- 抓取失败；
- 地区和界面差异。

## 为什么不整仓复制

GEOFlow、Elmo 和 GEO/AEO Tracker 都是可独立部署的应用。直接复制进 GEO-Master 会带来：

- 大量重复代码和依赖；
- 上游更新难以同步；
- 不同许可证和 NOTICE 管理复杂；
- 项目定位混乱；
- 安全、密钥和部署责任扩大。

因此采用：

```text
吸收架构和能力
+ 定义统一数据契约
+ 提供 Skill 和适配边界
+ 保留上游项目独立部署
```

后续若引入实质代码，将单独建立适配器目录，并完整保留原作者版权、许可证、修改说明和必要的 NOTICE 文件。

## 上游项目与许可证

| 项目 | 许可证 | 当前吸收方式 |
|---|---|---|
| `zubair-trabzada/geo-seo-claude` | MIT | 审计路由、爬虫检查、结构化数据与报告思路 |
| `yaojingang/GEOFlow` | Apache-2.0 | 内容工程、审核发布、队列和多站点分发思路 |
| `yaojingang/geo-citation-lab` | 代码 MIT；原创内容 CC BY 4.0；第三方材料各自许可 | 实验设计、引用选择/吸收、数据导入边界 |
| `elmohq/elmo` | MIT | 自托管长期监测、Prompt、竞品和报告架构 |
| `danishashko/geo-aeo-tracker` | MIT | 多模型并行、地域监测、引用机会和漂移告警 |

当前 GEO-Master 新增内容为原创整合工作流，没有复制上述项目的大段代码、数据集或研究正文。
