# GEO-Master 数据目录

> 保存可复现实验的结构化结果。公开数据必须脱敏，并遵守平台条款、版权和隐私要求。

## 推荐目录

```text
data/
├── README.md
├── examples/
│   └── engine-run.example.json
├── raw-responses/
│   └── README.md
├── normalized-runs/
│   └── runs.jsonl
├── query-sets/
│   └── baseline-query-set.csv
└── reports/
    └── YYYY-MM-summary.md
```

## 数据层级

### 1. Query Set

保存问题定义：

- `query_id`；
- 问题文本；
- 意图类型；
- 漏斗阶段；
- 国家和语言；
- 目标品牌、产品和竞品；
- 期望核验的事实；
- 优先级。

初始模板位于：[`templates/baseline-query-set.csv`](../templates/baseline-query-set.csv)。

### 2. Raw Response

保存平台原始回答或授权截图。

建议每次运行一个文件：

```text
raw-responses/RUN-20260720-001.md
```

文件头部记录：

```yaml
run_id: RUN-20260720-001
timestamp: 2026-07-20T10:00:00+08:00
platform: Perplexity
query_id: B001
language: en
country: US
account_state: logged_out
conversation_state: new_chat
```

正文保存完整回答和引用列表。公开时注意：

- 不发布私人对话或账号信息；
- 不大段重新分发受版权保护的页面正文；
- 截图中移除用户姓名、头像、邮箱和设备信息；
- 平台不允许公开或自动采集时，只保存必要的结构化观察值。

### 3. Normalized Run

将每次回答转成统一结构，用于统计。

Schema：[`schemas/engine-run.schema.json`](../schemas/engine-run.schema.json)

示例：[`data/examples/engine-run.example.json`](examples/engine-run.example.json)

推荐使用 JSONL：每行一条完整 JSON 记录。

```text
normalized-runs/runs.jsonl
```

### 4. Aggregated Report

月报或实验报告只包含聚合数据和必要示例：

- 品牌提及率；
- 官网引用率；
- 推荐率；
- 事实准确率；
- 负面提及率；
- 回答稳定性；
- 引用域名分布；
- 修改前后差异；
- 失败结果和限制。

## 缺失值规则

不要把缺失值写成 0。

| 值 | 含义 |
|---|---|
| `null` | 当前没有值或不适用 |
| `unknown` | 需要判断，但无法获得信息 |
| `not_provided` | 案例方没有提供 |
| `not_applicable` | 该字段不适用于本次运行 |
| `false` | 已明确确认没有发生 |
| `0` | 已测量，结果确实为零 |

## 文件命名

### Run ID

```text
RUN-YYYYMMDD-NNN
```

例如：

```text
RUN-20260720-001
```

### 实验 ID

```text
EXP-YYYYMM-brand-topic
```

例如：

```text
EXP-202607-wegear-power-bank
```

### 报告

```text
YYYY-MM-platform-brand-summary.md
```

## 最低公开要求

公开一个实验至少包含：

- 问题集或问题选择规则；
- 平台和模式；
- 国家、语言和账号状态；
- 时间范围；
- 运行次数；
- 结构化结果；
- 修改内容；
- 成功标准；
- 失败结果；
- 其他可能解释。

## 不应公开的数据

- 登录 Cookie、Token、API Key；
- 用户私人对话；
- 未经授权的客户名称和订单；
- 可识别个人身份的信息；
- 商业合同、报价和 CRM 明细；
- 违反平台条款采集的数据；
- 无法确认版权状态的大量原文和图片。

数据目录的目标是支持验证，不是囤积网页或私人内容。