# Changelog

GEO-Master 的重要更新记录在这里。

版本格式遵循语义化版本思路：

- `MAJOR`：内容结构、数据结构或使用方式发生不兼容变化；
- `MINOR`：新增案例、模板、Playbook、数据集或工具；
- `PATCH`：纠错、补充证据、更新链接和小幅改进。

## Unreleased

### Planned

- 品牌事实库 YAML 模板；
- 官网内容改造 Playbook；
- Reddit 合规参与清单；
- GEO 询盘与订单归因表；
- 首次真实品牌 30 天基线实验；
- 机器可读案例索引。

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

- 新增完整案例、模板或 Playbook：记录在 `Added`；
- 修正案例证据等级或关键结论：记录在 `Changed`；
- 删除失效或不合规内容：记录在 `Removed`；
- 修正错误数据、链接和作者信息：记录在 `Fixed`；
- 平台变化导致方法不再适用：记录在 `Deprecated`。