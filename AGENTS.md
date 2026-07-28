# GEO-Master AI Agent 工作规则

本文件适用于 Codex、Claude Code、GitHub Copilot、Gemini CLI、Cursor Agent、OpenHands 以及其他自动编码或自动维护工具。

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
8. **如果一个需求包含多个独立结果，先拆成多个任务，逐项完成。**

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

上面的独立结果应拆成独立提交，根据优先级逐项完成。

## 开始工作前

Agent 必须先在内部明确：

```text
当前唯一目标：
允许修改的文件：
明确不做的内容：
验收条件：
提交信息：
```

如果任务没有提供“允许修改的文件”，Agent 应选择完成目标所需的最少文件集合。

存在多种实现方式时，优先选择：

```text
修改文件更少
改动范围更小
更容易验证
更容易回滚
不改变现有接口
```

## 完成工作后

提交前检查：

- [ ] 本次是否只有一个主要结果；
- [ ] 是否修改了任务没有要求的文件；
- [ ] 是否夹带格式整理、目录重构或其他优化；
- [ ] 是否满足当前任务的验收条件；
- [ ] 是否可以用一句话准确描述这次提交；
- [ ] 是否应该立即停止，而不是继续做下一项。

无法用一句话描述提交结果，通常说明范围过大，应继续拆分。

## Commit 规则

推荐格式：

```text
<type>(<scope>): <一个明确结果>
```

示例：

```text
docs(readme): expose GEO tool ecosystem
feat(skill): add citation experiment workflow
feat(templates): add citation audit CSV
fix(references): replace one expired source URL
data(schema): add locale field to engine run schema
case(reddit): add one portable power station teardown
```

避免过于宽泛的提交信息：

```text
update project
improve GEO Master
add multiple features
finish roadmap
misc fixes
```

## 推荐任务模板

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

如果 Agent 发现其他值得完成的事项，只能写入后续建议，不能夹带执行。

## 外部项目吸收规则

GEO-Master 可以吸收其他开源项目的架构、能力和工作流，但必须：

1. 先确认许可证；
2. 优先采用兼容层、数据契约和独立适配器，而不是整仓复制；
3. 复制实质代码时保留版权、许可证、修改说明和 NOTICE；
4. 不复制受限论文、数据、图片、字体或品牌资产；
5. 不把上游项目的统计口径直接包装成 GEO-Master 官方标准；
6. 不把启发式评分宣传成平台排名机制；
7. 记录上游版本、提交和适配器版本；
8. 保持原始数据、标准化数据和派生结论分层。

当前集成架构见 [`integrations/README.md`](integrations/README.md)。
