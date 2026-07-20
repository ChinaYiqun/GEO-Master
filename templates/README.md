# GEO 模板与可下载资产

> 用于减少重复劳动。复制文件后替换示例数据，即可建立自己的 GEO 项目。

## 已发布模板

### [AI 可见性基线问题集](baseline-query-set.csv)

用于测试不同 AI 平台中的：

- 品牌提及；
- 官网引用；
- 推荐位置；
- 参数准确性；
- 竞争对手覆盖；
- 地域和语言差异。

### [每周 GEO 监测表](weekly-monitoring.csv)

用于保存每次运行的环境和结果，避免只保留截图。字段包括平台、问题、时间、地区、登录状态、品牌提及、引用 URL、推荐位置、准确性和备注。

### [完整 CASE 模板](../CASE-TEMPLATE.md)

适合自主实验、完整企业案例和长期追踪项目。

### [第三方运营案例简版模板](../cases/third-party-operations/CASE-SUMMARY-TEMPLATE.md)

适合公众号文章、服务商案例、访谈、演讲和公开复盘的快速拆解。

## 计划中的模板

| 文件 | 用途 |
|---|---|
| `brand-facts.yaml` | 品牌名称、定位、产品、参数、来源和状态 |
| `claims-and-sources.csv` | 每项品牌声明对应的证据和更新时间 |
| `question-map.csv` | 用户问题、意图、漏斗阶段和现有内容覆盖 |
| `content-brief.md` | 一篇 GEO 内容的事实、结构、来源和验证要求 |
| `reddit-reply-checklist.md` | 社区参与前的相关性、披露和合规检查 |
| `citation-audit.csv` | AI 引用域名、页面、位置和支持的声明 |
| `lead-attribution.csv` | 访问、品牌搜索、询盘和订单归因 |
| `case-intake-form.md` | 收集第三方案例所需的原始信息 |

## 使用建议

1. 不要删除时间、地区、语言和登录状态字段；
2. 同一个问题至少运行多次；
3. 新对话和多轮对话分开记录；
4. 原始回答和截图保留在私有或授权目录；
5. 商业数据脱敏后再提交到公开仓库；
6. 不要用空白值伪装成 0；缺失数据写 `unknown` 或 `not_provided`。

## 数据状态建议

```text
verified      已通过可靠来源确认
claimed       案例方宣称
observed      单次或少量观察
reproduced    已多次重复出现
unknown       尚未获得数据
not_applicable 不适用
```

## 贡献新模板

模板应该：

- 有明确使用场景；
- 提供一行示例数据；
- 解释每个关键字段；
- 避免收集不必要的个人信息；
- 能够被其他品牌直接 Fork 使用；
- 配套一个 Playbook 或案例说明。

建议先阅读 [AI 可见性基线测试](../playbooks/ai-visibility-baseline.md)。