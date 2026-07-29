# Changelog

GEO-Master 的重要更新记录在这里。

版本格式遵循语义化版本思路：

- `MAJOR`：内容结构、数据结构或使用方式发生不兼容变化；
- `MINOR`：新增案例、模板、Playbook、数据集或工具；
- `PATCH`：纠错、补充证据、更新链接和小幅改进。

## Unreleased — 0.4.0-dev

### Added

- `docs/GEO-MASTER-PLATFORM-ARCHITECTURE.md`：GEO-Master Control Plane、Execution Plane、Evidence Plane、适配器契约和分阶段实施蓝图；
- `integrations/upstream-capabilities.json`：19 个 GEO、AEO、AI 可见性、内容运营和营销 Agent 上游项目的机器可读能力注册表；
- `schemas/integration-registry.schema.json`：上游能力、许可证、集成模式、状态、差异化和禁止项 Schema；
- `scripts/validate_integration_registry.py`：校验注册表结构、能力引用、ID 唯一性与 GPL 进程边界；
- CI 增加集成能力注册表编译和验证步骤。

### Changed

- README 将项目定位从 GEO 工程工具箱升级为可插拔 GEO Operating System；
- `integrations/README.md` 重构为统一能力地图、三层职责、集成模式、数据原则和实施顺序；
- 版本标识更新为 `0.4.0-dev`。

### Integrated ecosystem

当前注册表纳入：

- `GEO-optim/GEO`、`cxcscmu/AutoGEO`；
- `yaojingang/GEOFlow`、`yaojingang/GEORank`；
- Getcito、Gego、Searchstack、Elmo、GEO/AEO Tracker；
- GeoReady、GEO Analyzer、Dualmark、aeo.js、LLMS Generator Toolkit、llms.txt；
- Aaron Marketing Skills、Digital Marketing Pro；
- `geo-seo-claude`、`geo-citation-lab`。

这些项目成为 GEO-Master 能力体系的子集，但默认不整仓复制。MIT、Apache、GPL、CC 和混合许可分别使用适配器、独立重实现、进程边界或引用边界。

## 0.3.0-dev

### Added

- `.agents/skills/geo-master/SKILL.md`：统一的网站审计、事实治理、基线、内容工作流和优化验证 Skill；
- `.agents/skills/geo-master-citation-lab/SKILL.md`：引用选择、内容吸收、实体曝光、界面差异和外部研究导入 Skill；
- `.agents/skills/geo-master-monitor/SKILL.md`：多模型 Prompt 运行、品牌/竞品监测、引用机会、地域比较和漂移告警 Skill；
- `integrations/README.md`：GEO-Master 工具生态、上游项目、许可证和适配边界；
- `schemas/monitor-run.schema.json`：兼容人工测试、外部数据和自托管工具的监测运行 Schema；
- `data/examples/monitor-run.example.json`：标准多模型监测记录示例；
- `templates/citation-audit.csv`：AI 引用页面、位置、来源类型、内容吸收和实体曝光审计表；
- `scripts/import_monitor_runs.py`：Elmo 与 GEO/AEO Tracker 监测运行导入器；
- `scripts/summarize_visibility.py`：零依赖的监测 CSV 汇总 CLI，输出总体和逐平台可见性指标；
- `scripts/test_summarize_visibility.py`：验证缺失值分母、多平台分组和指标计算的标准库测试；
- `README.en.md`：面向全球开发者、出海品牌和英文搜索的项目入口；
- `docs/REPOSITORY-DISCOVERY.md`：GitHub About、Topics、Release 与搜索发现性检查表；
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

- 重构主 README，将 `Generative Engine Optimization`、中国品牌出海、国内 AI 搜索、具体平台和可运行证据前置，降低与地理信息 `GEO` 的搜索歧义；
- README 增加 5 分钟可复现实验、工程校验命令和能力—资产核验矩阵；
- CI 增加可见性汇总脚本的编译、测试与 Markdown/JSON 冒烟校验；
- `scripts/README.md` 增加可见性汇总 CLI 的指标口径、缺失值规则和本地验证流程；
- 将 README 中的大段 AI Coding 规则迁移到 `AGENTS.md`；
- README 保留企业产品入口，但将其置于开源能力、代码和证据说明之后；
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

- 首次真实品牌 30 天基线实验；
- 国内多平台回答差异实验；
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
