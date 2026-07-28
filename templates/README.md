# GEO 模板与可下载资产

> 从品牌事实、问题基线、内容生产、官网审计，到持续监测、服务商验收和商业归因。

## 推荐使用顺序

```mermaid
flowchart LR
    A[品牌事实库] --> B[声明与来源]
    B --> C[问题地图]
    C --> D[基线问题集]
    D --> E[官网审计]
    E --> F[内容 Brief 与内容任务]
    F --> G[审核与发布]
    G --> H[引用和多模型监测]
    H --> I[月度报告]
    I --> J[询盘和订单归因]
```

第一次使用建议先完成：

1. [`brand-facts.yaml`](brand-facts.yaml)
2. [`question-map.csv`](question-map.csv)
3. [`baseline-query-set.csv`](baseline-query-set.csv)
4. [`weekly-monitoring.csv`](weekly-monitoring.csv)

---

## 1. 品牌事实与来源

### [品牌事实库 YAML](brand-facts.yaml)

统一管理品牌、别名、公司主体、产品型号、参数、认证、服务范围、状态和变更记录。

它是企业内部事实源，不是 AI 平台保证读取的特殊文件。

### [声明与来源表](claims-and-sources.csv)

为每条公开声明记录：

- Claim ID；
- 官方和第三方来源；
- 生效、失效和审核状态；
- 负责人和审核人；
- 是否允许公开。

事实、页面、问题、运行记录和引用审计应尽量使用稳定 ID 连接。

---

## 2. 用户问题与基线

### [用户问题地图](question-map.csv)

将问题连接到用户意图、漏斗阶段、业务价值、事实缺口、证据缺口、目标平台和负责人。

### [AI 可见性基线问题集](baseline-query-set.csv)

提供中英文示例问题，用于测试：

- 品牌提及；
- 官网引用；
- 明确推荐；
- 参数准确性；
- 竞品覆盖；
- 地域和语言差异。

### [每周 GEO 监测表](weekly-monitoring.csv)

适合人工或小规模运行，记录平台、问题、时间、地区、登录状态、品牌提及、引用、推荐、准确性和原始回答位置。

更复杂的工具导入和长期监测使用：

- [`monitor-run.schema.json`](../schemas/monitor-run.schema.json)
- [`monitor-run.example.json`](../data/examples/monitor-run.example.json)
- [`import_monitor_runs.py`](../scripts/import_monitor_runs.py)

---

## 3. 网站与内容执行

### [官网 GEO 审计表](website-audit.csv)

逐页检查：

- HTTP、索引和 robots 状态；
- Canonical、Title、H1 和正文可提取性；
- 品牌实体是否清楚；
- 产品事实是否一致；
- 日期、来源和 Schema；
- 旧内容、重复页面和修复责任人。

### [GEO 内容 Brief](content-brief.md)

适用于产品页、对比页、选型指南、FAQ、案例、文章和白皮书。定义问题、直接答案、事实、证据、限制条件、CTA、发布前基线和复测。

### [内容运营任务 Schema](../schemas/content-task.schema.json)

把内容生产变成可追踪工作流：

```text
Brand Facts / Claim IDs / Question IDs
→ 生成配置
→ 事实与合规审核
→ 本地或多站发布
→ AI 平台复测
```

标准示例：[`content-task.example.json`](../data/examples/content-task.example.json)

### [Reddit 社区参与检查清单](reddit-reply-checklist.md)

用于判断是否应回复、是否需要披露关系、链接是否必要，以及如何避免伪装用户、刷帖和虚假口碑。

---

## 4. 引用实验与持续监测

### [AI 引用审计表](citation-audit.csv)

逐条记录：

- 平台、模型、采集方式和界面；
- 引用 URL、域名、位置和来源类型；
- 是否为品牌官方来源；
- 页面是否可访问；
- 答案中的声明；
- 引用页面与答案的可观察内容重合；
- 品牌和竞品实体曝光；
- 事实和证据状态。

不要把“出现在引用列表”直接等同于“真正影响了答案”。

### Agent Skills

- [`geo-master-citation-lab`](../.agents/skills/geo-master-citation-lab/SKILL.md)：引用选择、内容吸收、实体曝光和界面差异；
- [`geo-master-monitor`](../.agents/skills/geo-master-monitor/SKILL.md)：多模型、竞品、地域、引用机会和漂移告警。

---

## 5. 服务商验收与月度报告

### [GEO 服务商验收表](service-provider-scorecard.csv)

用于核查服务商是否：

- 定义了真实 Query Set 和优化前基线；
- 进行重复运行；
- 记录地区、语言、账号和界面；
- 交付原始回答和引用 URL；
- 分开衡量提及、引用、推荐和准确性；
- 跟踪负面信息和竞品；
- 说明归因方法和禁用做法；
- 支持数据导出并明确数据所有权；
- 约定可验收结果，而不是只保证“排名”。

### [GEO 月度报告](monthly-report.md)

覆盖：

- 数据完整性和运行失败；
- Prompt、模型和环境变化；
- 提及、引用、推荐、准确率；
- 引用域名、竞品和机会；
- 页面和事实修正；
- 优化前后对照；
- 访问、询盘、订单和归因置信度；
- 下月可验收行动。

---

## 6. 商业归因

### [线索与订单归因表](lead-attribution.csv)

区分：

- AI referral；
- 品牌搜索；
- 直接访问；
- 用户自报；
- First touch 和 Last touch；
- 辅助渠道；
- 询盘、报价、订单和收入；
- 归因置信度。

订单发生在 GEO 工作之后，不代表订单一定由 GEO 带来。

商业数据必须脱敏后才能进入公开仓库。

---

## 7. 案例与贡献

- [完整 CASE 模板](../CASE-TEMPLATE.md)
- [第三方运营案例简版模板](../cases/third-party-operations/CASE-SUMMARY-TEMPLATE.md)
- [证据评级标准](../EVIDENCE-STANDARD.md)
- [贡献指南](../CONTRIBUTING.md)

---

## 数据规范

| 数据 | Schema / 示例 |
|---|---|
| 单次人工或标准平台运行 | [`engine-run.schema.json`](../schemas/engine-run.schema.json) / [`engine-run.example.json`](../data/examples/engine-run.example.json) |
| 多模型或外部工具监测运行 | [`monitor-run.schema.json`](../schemas/monitor-run.schema.json) / [`monitor-run.example.json`](../data/examples/monitor-run.example.json) |
| 内容生成、审核和多站发布任务 | [`content-task.schema.json`](../schemas/content-task.schema.json) / [`content-task.example.json`](../data/examples/content-task.example.json) |

自动校验：

```bash
python3 scripts/validate_examples.py
python3 scripts/test_import_monitor_runs.py
```

GitHub Actions 会在 Push 和 Pull Request 时执行相同检查。

---

## 使用原则

1. 不要删除时间、地区、语言、界面和账号状态；
2. 同一个高价值问题应重复运行；
3. 新对话和多轮对话分开记录；
4. 原始回答和截图保留在私有或授权目录；
5. 不要用空白值伪装成 `0`；
6. 不要把 Demo 数据混入真实监测；
7. 第三方采集和消费者产品界面必须区分；
8. 综合分必须能拆回底层观测项；
9. 模板和 Schema 修改需要记录版本；
10. 外部项目和数据必须保留许可证和来源。

## 缺失值和证据状态

```text
verified       已通过可靠来源确认
reproduced     已多次重复出现
observed       单次或少量观察
claimed        来源方宣称
pending        正在核验
expired        已过期
unknown        尚未获得数据
not_provided   来源未提供
not_applicable 不适用
```

不要把 `unknown`、空白、`false` 和 `0` 混为一谈。

## 仍在计划中的模板

| 文件 | 用途 |
|---|---|
| `case-intake-form.md` | 收集第三方案例所需的原始信息 |
| `experiment-protocol.md` | 受控跨平台实验方案 |
| `adapter-mapping.csv` | 外部工具字段到 GEO-Master Schema 的映射 |
