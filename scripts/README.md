# GEO-Master Scripts

仓库脚本用于把 GEO-Master 的模板、Schema 和监测方法变成可运行、可校验、可复现的工程流程。

| 脚本 | 用途 | 依赖 |
|---|---|---|
| [`summarize_visibility.py`](summarize_visibility.py) | 汇总监测 CSV，按总体和平台计算提及、官网引用、推荐、事实准确率与负面率 | Python 标准库 |
| [`import_monitor_runs.py`](import_monitor_runs.py) | 将 Elmo 或 GEO/AEO Tracker 导出转换为统一的 `monitor-run` JSONL | Python 标准库 |
| [`validate_examples.py`](validate_examples.py) | 校验仓库 JSON Schema 与示例数据 | `jsonschema` |
| [`test_summarize_visibility.py`](test_summarize_visibility.py) | 测试可见性汇总口径，特别是缺失值分母处理 | Python 标准库 |
| [`test_import_monitor_runs.py`](test_import_monitor_runs.py) | 测试监测数据适配器 | Python 标准库 |

## `summarize_visibility.py`

将 [`templates/weekly-monitoring.csv`](../templates/weekly-monitoring.csv) 或兼容 CSV 转换为 Markdown 或 JSON 汇总。

### 快速运行

```bash
python scripts/summarize_visibility.py templates/weekly-monitoring.csv
```

输出 JSON：

```bash
python scripts/summarize_visibility.py templates/weekly-monitoring.csv \
  --format json \
  --output out/visibility-summary.json
```

输出指标：

- 品牌提及率；
- 官网引用率；
- 明确推荐率；
- 事实准确率；
- 负面情绪率；
- 总体与逐平台结果；
- 每项指标的可判断样本数量。

### 缺失值原则

脚本不会把以下值当作 `false` 或 0：

```text
unknown
not_provided
not_applicable
null
空值
```

这些值从对应指标的分母中排除。只有明确的 `yes/no`、`true/false`、`1/0` 才进入布尔指标计算。

事实准确率只在以下状态中计算：

```text
accurate
partial
incorrect
outdated
conflicting
```

这符合 GEO-Master 的证据原则：缺失数据不等于失败，无法判断不等于没有发生。

### 测试

```bash
python scripts/test_summarize_visibility.py
```

测试覆盖：

- 多平台分组；
- `unknown` 不进入分母；
- 布尔指标计算；
- 事实准确率；
- 负面情绪率；
- Markdown 报告生成。

## `import_monitor_runs.py`

将 Elmo 或 GEO/AEO Tracker 的运行记录转换为 GEO-Master 的 [`monitor-run.schema.json`](../schemas/monitor-run.schema.json) 兼容 JSONL。

输出目录：

```text
monitor-import/
├── monitor-runs.jsonl
├── import-manifest.json
└── raw/
    └── <run-id>.txt
```

原始回答单独保存，并在标准记录中写入相对路径和 SHA-256。

### 导入 GEO/AEO Tracker

输入可以是：

- `ScrapeRun[]` 数组；
- 包含 `runs` 的对象；
- 包含 `state.runs` 的 AppState 导出对象。

```bash
python scripts/import_monitor_runs.py tracker-export.json \
  --source geo-aeo-tracker \
  --project-id PROJECT-MY-BRAND \
  --brand "My Brand" \
  --brand-alias "MyBrand" \
  --official-domain example.com \
  --competitor "Competitor A" \
  --country US \
  --language en-US \
  --output-dir private/imports/tracker-2026-07-28
```

映射的主要字段：

```text
provider             → provider.product
prompt               → prompt.text
answer               → raw answer file
sources[]             → citations[]
createdAt            → collected_at
brandMentions[]       → observation.brand_mentioned
competitorMentions[]  → competitor_observations[]
sentiment             → observation.sentiment
country               → context.country
```

上游 `visibilityScore` 不会被直接复制成 GEO-Master 结论，因为它是上游工具自己的综合口径。

### 导入 Elmo

支持 Elmo `prompt_runs` 常见字段：

```text
id
promptId
model
version
webSearchEnabled
rawOutput.response
textContent
competitorsMentioned
brandMentioned
citations[]
createdAt
```

如果导出对象同时包含 `prompts` 数组，脚本会使用 `id` 和 `value` 还原 Prompt 文本：

```bash
python scripts/import_monitor_runs.py elmo-export.json \
  --source elmo \
  --project-id PROJECT-MY-BRAND \
  --brand "My Brand" \
  --official-domain example.com \
  --country US \
  --language en-US \
  --output-dir private/imports/elmo-2026-07-28
```

如果运行记录只有 `promptId`，可以额外提供 Prompt 映射：

```json
{
  "prompt-id-1": "What are the best products for this use case?",
  "prompt-id-2": "Compare My Brand with Competitor A."
}
```

```bash
python scripts/import_monitor_runs.py elmo-runs.json \
  --source elmo \
  --prompt-map prompt-map.json \
  --project-id PROJECT-MY-BRAND \
  --brand "My Brand" \
  --official-domain example.com
```

### 采集方式必须声明

默认：

```text
collection_method=imported_dataset
interface=vendor_representation
```

如果已确认数据来自其他方式，应显式设置：

```bash
--collection-method official_api
--interface api
```

或：

```bash
--collection-method browser_automation
--interface web_desktop
```

不要把第三方数据供应商、浏览器自动化、官方 API 和消费者 Web/App 的结果视为完全相同的产品界面。

### 导入器不会推断什么

源数据没有直接证据时，脚本不会自动判断：

- 品牌是否被明确推荐；
- 推荐位置；
- 品牌事实是否准确；
- 引用页面是否真正影响了答案；
- 最终订单是否来自 GEO。

这些字段会保持 `false`、`null` 或 `not_evaluable`，等待后续人工或受控实验审核。

## 本地验证

```bash
python -m py_compile \
  scripts/import_monitor_runs.py \
  scripts/test_import_monitor_runs.py \
  scripts/summarize_visibility.py \
  scripts/test_summarize_visibility.py \
  scripts/validate_examples.py

python scripts/test_import_monitor_runs.py
python scripts/test_summarize_visibility.py
python scripts/validate_examples.py
```

## 隐私与安全

建议将完整运行数据写入私有目录，不要把以下内容提交到公开仓库：

- API Key、Cookie 和登录令牌；
- 未公开 Prompt；
- 客户原始回答和截图；
- 个人信息；
- 未脱敏询盘、订单和收入数据；
- 数据供应商的受限响应体。

公开时只提交脱敏样例、聚合报告或可复现脚本。
