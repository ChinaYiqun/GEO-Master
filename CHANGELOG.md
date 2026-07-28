# Changelog

GEO-Master 的重要更新记录在这里。

版本格式遵循语义化版本思路：

- `MAJOR`：内容结构、数据结构或使用方式发生不兼容变化；
- `MINOR`：新增案例、模板、Playbook、数据集或工具；
- `PATCH`：纠错、补充证据、更新链接和小幅改进。

## Unreleased — 0.3.0-dev

### Added

- `.agents/skills/geo-master/SKILL.md`：统一的网站审计、事实治理、基线、内容工作流和优化验证 Skill；
- `.agents/skills/geo-master-citation-lab/SKILL.md`：引用选择、内容吸收、实体曝光、界面差异和外部研究导入 Skill；
- `.agents/skills/geo-master-monitor/SKILL.md`：多模型 Prompt 运行、品牌/竞品监测、引用机会、地域比较和漂移告警 Skill；
- `integrations/README.md`：GEO-Master 工具生态、上游项目、许可证和适配边界；
- `schemas/monitor-run.schema.json`：兼容人工测试、外部数据和自托管工具的监测运行 Schema；
- `data/examples/monitor-run.example.json`：标准多模型监测记录示例；
- `templates/citation-audit.csv`：AI 引用页面、位置、来源类型、内容吸收和实体曝光审计表；
- `AGENTS.md`：标准 AI Coding 工作规则和外部开源项目吸收规范；
- `references/GEO-READING-LIST.md`：GEO 学术、行业、中文研报与媒体调查来源的结构化阅读索引；
- `explainers/geo-literature-synthesis.md`：跨来源共识、分歧、证据地图、企业执行路径与合规边界；
- `templates/brand-facts.yaml`：品牌事实库 YAML 模板；
- `templates/claims-and-sources.csv`：声明与来源管理表；
- `templates/question-map.csv`：用户问题地图模板；
- `templates/content-brief.md`：GEO 内容 Brief 模板；
- `templates/reddit-reply-checklist.md`：Reddit 合规社区参与检查清单；
- `templates/lead-attribution.csv`：GEO 询盘与订单归因表；
- 完整版国内 GEO 执行手册与国内信源索引更新；
- 机器可读 AI 单次运行 Schema 与标准示例数据。

### Changed

- 重构主 README，将项目从资料导航升级为“审计—内容运营—多模型监测—引用实验—商业归因”的工具体系入口；
- 将 README 中的大段 AI Coding 规则迁移到 `AGENTS.md`；
- README 增加商业产品入口，并通过 UTM 区分 GitHub 导流位置；
- `START-HERE.md` 增加产品化方案入口；
- 主 README 增加学术、行业和媒体阅读入口；
- `explainers/README.md` 增加 GEO 文献综合解读入口；
- 对资料中的失效链接、作者信息、学术起源和强确定性表述增加核验状态与风险说明。

### Integrated concepts

当前以原创 Skill、数据契约和适配边界吸收以下项目能力，未整仓复制：

- `zubair-trabzada/geo-seo-claude`：网站审计、爬虫、Schema 和报告工作流；
- `yaojingang/GEOFlow`：知识库、RAG、审核、发布和多站分发；
- `yaojingang/geo-citation-lab`：引用选择、内容吸收、实体曝光和实证研究；
- `elmohq/elmo`：自托管多模型监测、竞品和周期报告；
- `danishashko/geo-aeo-tracker`：并行运行、地域比较、引用机会和漂移告警。

### Planned

- GEO 服务商验收表；
- 官网审计表；
- 月度报告模板；
- 首次真实品牌 30 天基线实验；
- Elmo 与 GEO/AEO Tracker 的机器可读导入/导出适配器；
- GEOFlow 内容任务与 GEO-Master 事实/问题 ID 的映射规范；
- 机器可读案例索引与自动校验流程；
- 第一个正式 `v0.3.0` Release。

## 0.2.0 — 2026-07-20

### Added

- `playbooks/ai-visibility-baseline.md`：AI 可见性基线测试流程；
- `templates/baseline-query-set.csv`：30 条中英文基线问题；
- `templates/weekly-monitoring.csv`：逐次运行监测表；
- `explainers/mentions-vs-citations.md`：提及、引用、推荐与准确性口径；
- `cases/README.md`、`playbooks/README.md`、`explainers/README.md`、`templates/README.md` 导航；
- GitHub 案例提交和信源纠错 Issue Forms；
- Pull Request 模板；
- MIT License。

### Changed

- 更新 `START-HERE.md`，将规划中的入口替换为实际可用文件；
- 更新 `ROADMAP.md`，同步真实完成进度和 Release 计划；
- 明确最小实验要求和商业归因边界。

## 0.1.0 — 2026-07-17

### Added

- 项目定位和主 README；
- 案例证据评级标准；
- 完整 CASE 模板；
- 第三方运营案例简版模板；
- 实验室仪器 Reddit GEO 案例拆解；
- Ahrefs Reddit 需求研究案例；
- Ahrefs Brand Radar 监测案例；
- Tenten Reddit GEO 方法拆解；
- 国内 GEO 原文与信源索引；
- 国内 GEO 执行手册；
- 老钱聊GEO 官网结构拆解；
- 招财兔 GEO 品牌事实库拆解；
- 贡献指南和首批公开 Issues。

## 维护规则

- 新增完整案例、模板、Playbook、数据集或工具：记录在 `Added`；
- 修正案例证据等级、关键结论或项目结构：记录在 `Changed`；
- 删除失效或不合规内容：记录在 `Removed`；
- 修正错误数据、链接和作者信息：记录在 `Fixed`；
- 平台变化导致方法不再适用：记录在 `Deprecated`。
