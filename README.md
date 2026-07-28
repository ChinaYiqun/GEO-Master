# GEO-Master

> 中国品牌出海与国内 AI 搜索场景的 GEO 实战项目：真实案例、可复现实验、Playbook、模板、数据规范与资料索引。

[![GitHub stars](https://img.shields.io/github/stars/ChinaYiqun/GEO-Master?style=social)](https://github.com/ChinaYiqun/GEO-Master/stargazers)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.0-informational.svg)](CHANGELOG.md)

> **需要把 GEO 方法用于实际业务？**
>
> 查看项目维护者提供的 **[GEO 商业产品介绍](https://tst.ahupo.cn/intro?utm_source=github&utm_medium=repository&utm_campaign=geo-master&utm_content=readme-top)**。
>
> 商业产品与本开源仓库相互独立：仓库继续公开案例、证据标准、模板和实验方法，不因商业合作降低核验要求。

## 在线访问

- **GEO-Master 开源网站：** https://chinayiqun.github.io/geo-master/
- **GEO 商业产品介绍：** [查看产品与服务](https://tst.ahupo.cn/intro?utm_source=github&utm_medium=repository&utm_campaign=geo-master&utm_content=online-access)

仓库研究品牌如何被 ChatGPT、Perplexity、Gemini、Claude、Google AI Search、豆包、DeepSeek、腾讯元宝等生成式平台：

```text
发现 → 理解 → 提及 → 引用 → 推荐 → 访问 → 询盘 → 成交
```

项目不把一次 AI 回答当成稳定排名，也不把服务商截图、外链数量或无法核验的订单数字直接写成成功事实。

---

## 30 分钟开始一次 GEO 基线测试

第一次使用，只需要下面三个文件：

1. [AI 可见性基线测试 Playbook](playbooks/ai-visibility-baseline.md)
2. [30 条中英文基线问题集](templates/baseline-query-set.csv)
3. [每周 GEO 监测表](templates/weekly-monitoring.csv)

最小实验：

```text
选择 10 个真实用户问题
× 2 个 AI 平台
× 每题运行 1–3 次
→ 分别记录品牌提及、官网引用、推荐位置和事实准确性
```

没有基线、原始回答和重复运行记录时，不应宣布“GEO 提升了多少”或“带来了多少订单”。

---

## 现在可以直接使用什么

| 模块 | 内容 | 入口 |
|---|---|---|
| Cases | 国内外 GEO 案例、失败模式和证据核验 | [案例库](cases/README.md) |
| Playbooks | 基线测试、国内 GEO 执行和具体工作流 | [执行手册](playbooks/README.md) |
| Explainers | 提及、引用、推荐、准确性等技术口径 | [技术解释](explainers/README.md) |
| Templates | 问题集、监测表、品牌事实库和归因表 | [模板资产](templates/README.md) |
| References | 学术论文、行业文章、媒体调查和国内信源 | [资料阅读索引](references/GEO-READING-LIST.md) |
| Data | 机器可读运行记录、Schema 和示例数据 | [数据规范](data/README.md) |

推荐入口：

- [新读者从这里开始](START-HERE.md)
- [GEO 学术、行业与媒体资料阅读索引](references/GEO-READING-LIST.md)
- [跨来源综合解读：共识、分歧与证据边界](explainers/geo-literature-synthesis.md)
- [证据与案例评级标准](EVIDENCE-STANDARD.md)
- [90 天路线图](ROADMAP.md)
- [更新记录](CHANGELOG.md)

---

## 仓库结构

```text
GEO-Master/
├── cases/          # 真实案例、第三方案例拆解与失败模式
├── playbooks/      # 可执行步骤和团队工作流
├── explainers/     # 技术机制、指标和概念边界
├── templates/      # CSV、YAML、Markdown 等可复制资产
├── references/     # 原始来源、作者、日期、链接与阅读笔记
├── data/           # 实验数据示例与目录规范
├── schemas/        # 机器可读数据结构
└── docs/           # 项目网站或网站相关资源（如后续迁入）
```

公开文章进入仓库时，按三层处理：

```text
references/  保存来源和结构化阅读笔记
cases/       对高价值案例进行证据化拆解
playbooks/   从多个来源提炼可执行系统
```

---

# AI Coding 强制规则：一次只完成一项内容

> 本节适用于 Codex、Claude Code、GitHub Copilot、Gemini CLI、Cursor Agent、OpenHands 以及其他自动编码或自动维护工具。

## 核心约束

```text
一个任务 = 一个明确交付物
一个提交 = 一个原子变更
达到当前任务验收条件 = 立即停止
```

任何 AI Agent 在修改仓库前，必须遵守以下规则：

1. **只完成当前消息或当前 Issue 明确要求的一项内容。**
2. **不得顺手完成路线图中的下一项。**
3. **不得因为发现相邻问题，就自动扩大任务范围。**
4. **不得在一次提交中同时增加案例、模板、网站功能和文档更新。**
5. **不得进行“顺便重构”“顺便统一格式”“顺便清理全部链接”。**
6. **没有被任务明确点名的文件，默认不得修改。**
7. **完成验收条件后立即停止，不继续寻找可以改进的地方。**
8. **如果一个需求包含多个独立结果，先拆成多个任务；本次只执行第一个任务。**

## 什么算“一项内容”

允许作为一次任务的例子：

- 新增 **一个** GEO 案例；
- 核验 **一篇** 文章；
- 修复 **一个** 失效链接；
- 新增 **一个** CSV 模板；
- 增加网站的 **一个** 筛选功能；
- 修正 **一个** Schema 字段；
- 重写 **一个** 指定文件；
- 为 **一个** 已存在功能补充测试。

不允许放在同一次任务或同一个提交中的组合：

```text
新增文章索引
+ 拆成完整案例
+ 提炼 Playbook
+ 更新网站
+ 更新路线图
+ 创建 Release
```

上面的六项必须拆成六个独立任务，根据优先级逐项完成。

## AI Agent 开始工作前

Agent 必须先在内部明确以下五项：

```text
当前唯一目标：
允许修改的文件：
明确不做的内容：
验收条件：
提交信息：
```

如果任务没有提供“允许修改的文件”，Agent 应选择完成目标所需的**最少文件集合**，而不是扩大到相关目录。

如果存在两种实现方式，应优先选择：

```text
修改文件更少
改动范围更小
更容易验证
更容易回滚
不改变现有接口
```

## AI Agent 完成工作后

提交前必须检查：

- [ ] 本次是否只有一个主要结果；
- [ ] 是否修改了任务没有要求的文件；
- [ ] 是否夹带格式整理、目录重构或其他优化；
- [ ] 是否满足当前任务的验收条件；
- [ ] 是否可以用一句话准确描述这次提交；
- [ ] 是否应该立即停止，而不是继续做下一项。

只要无法用一句话描述提交结果，就说明改动范围可能过大，需要继续拆分。

## Commit 规则

推荐格式：

```text
<type>(<scope>): <一个明确结果>
```

示例：

```text
docs(readme): define atomic AI coding workflow
feat(templates): add citation audit CSV
fix(references): replace one expired source URL
data(schema): add locale field to engine run schema
case(reddit): add one portable power station teardown
```

禁止使用过于宽泛的提交信息：

```text
update project
improve GEO Master
add multiple features
finish roadmap
misc fixes
```

## 推荐的任务描述模板

后续给 AI Coding 工具下任务时，建议复制下面的格式：

```markdown
## 当前唯一任务
新增一份 AI 引用审计 CSV 模板。

## 允许修改
- templates/citation-audit.csv

## 不在本次范围
- 不修改 README
- 不更新网站
- 不新增 Playbook
- 不修改其他模板

## 验收条件
- 包含一行示例数据
- 包含字段说明
- CSV 可以正常打开

## 提交信息
feat(templates): add citation audit CSV
```

如果 Agent 认为还有其他值得完成的事项，只能将其写入“后续建议”，**不能在当前提交中执行**。

---

## 证据原则

四个 AI 可见性指标必须分开：

```text
AI 是否提到品牌
AI 是否引用品牌或官网
AI 是否明确推荐品牌
AI 是否准确描述品牌事实
```

商业结果再单独追踪：

```text
点击或品牌搜索
→ 官网访问
→ 询盘
→ 报价
→ 订单
```

仓库中的结果数字应标记为：

- `verified`：可靠来源已确认；
- `reproduced`：通过多次运行复现；
- `observed`：少量观察；
- `claimed`：案例方宣称；
- `unknown`：尚无数据；
- `not_provided`：来源未提供。

---

## 不做什么

- 不把一次 ChatGPT、豆包或 DeepSeek 回答当成稳定结论；
- 不把 Ahrefs 外链数量等同于 AI 推荐；
- 不伪装普通用户发布品牌营销内容；
- 不建议批量生成低价值社区回复；
- 不保证修改几个标签就一定被模型收录；
- 不替无法独立验证的订单数字背书；
- 不把从业者经验包装成平台官方规则；
- 不用一个总分掩盖负面提及和事实错误。

---

## 开源项目与商业产品

GEO-Master 是开放的学习、研究和复现实验仓库。项目维护者同时提供商业 GEO 产品，面向希望进一步了解产品化方案的读者。

- 开源仓库中的模板、案例和证据标准继续按公开规则维护；
- 商业产品不会被包装成独立第三方结论；
- 涉及产品自身的案例或数据，会明确标记来源和证据等级；
- 是否使用商业产品，不影响参与仓库、提交 Issue 或贡献 PR。

**[查看 GEO 商业产品介绍 →](https://tst.ahupo.cn/intro?utm_source=github&utm_medium=repository&utm_campaign=geo-master&utm_content=readme-commercial-section)**

---

## 贡献

开始贡献前，请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

欢迎提交：

- 可核验的 GEO 案例；
- 失败案例和踩坑记录；
- 平台变化与复现实验；
- 数据集、Prompt、工具和模板；
- 官方文档、行业文章和案例线索；
- 对已有证据链的补充或质疑。

对于多个独立贡献，请分别创建 Issue 或 PR，不要合并成一个大型改动。

## Citation

研究、报告、培训或客户项目使用本仓库时，可以引用 [`CITATION.cff`](CITATION.cff)，并保留各案例对应的原始文章与官方来源。

## License

MIT License。案例引用、截图、第三方文章和外部数据仍遵循其原始版权与使用规则。
