# GEO-Master Scripts

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
python3 scripts/import_monitor_runs.py tracker-export.json \
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
python3 scripts/import_monitor_runs.py elmo-export.json \
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
python3 scripts/import_monitor_runs.py elmo-runs.json \
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

### 隐私与安全

建议将完整运行数据写入私有目录，不要把以下内容提交到公开仓库：

- API Key、Cookie 和登录令牌；
- 未公开 Prompt；
- 客户原始回答和截图；
- 个人信息；
- 未脱敏询盘、订单和收入数据；
- 数据供应商的受限响应体。

公开时只提交脱敏样例、聚合报告或可复现脚本。
