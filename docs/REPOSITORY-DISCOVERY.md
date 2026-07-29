# Repository discovery checklist

This file records the repository metadata and publishing actions that cannot be expressed reliably through README content alone.

## Recommended GitHub About description

Use this exact description or a close variant:

```text
Open-source GEO toolkit for Chinese brands: website audits, AI visibility baselines, reproducible experiments, Agent Skills, multi-model monitoring, schemas and data templates.
```

A bilingual alternative:

```text
面向中国品牌出海与国内 AI 搜索的开源 GEO 工程工具箱：网站审计、AI 可见性基线、可复现实验、Agent Skills、多模型监测与数据模板。
```

The description should spell out the function of the project. `GEO-Master` alone is ambiguous because GitHub and web search frequently interpret `geo` as geospatial or geography.

## Recommended GitHub topics

GitHub allows up to 20 topics. Recommended set:

```text
geo
generative-engine-optimization
ai-search
ai-visibility
answer-engine-optimization
ai-seo
brand-monitoring
agent-skills
website-audit
reproducible-research
chatgpt
perplexity
gemini
claude
deepseek
doubao
qwen
chinese
china
global-marketing
```

Do not rely on the generic `geo` topic by itself. Always pair it with `generative-engine-optimization`, `ai-search`, and `ai-visibility` to disambiguate the project from geographic information systems.

## Recommended website field

Use a stable documentation, demo, or project landing page. Avoid temporary URLs. The URL should contain a concise project description, canonical repository link, and links back to the README, releases, cases, and reproducible experiments.

## Search-facing release checklist

For every meaningful release:

1. Create a GitHub Release with a descriptive title such as `GEO-Master v0.4 — China AI visibility baseline and reproducible monitoring demo`.
2. Include the full phrase `Generative Engine Optimization` in the release title or first paragraph.
3. Name concrete platforms where applicable: ChatGPT, Perplexity, Gemini, Claude, DeepSeek, Doubao, Tencent Yuanbao, Kimi, Qwen.
4. Link to one executable script, one dataset or fixture, one report, and one case.
5. Publish a short English release summary even when the main release notes are Chinese.
6. Announce the release from a stable page that links to the canonical GitHub repository.

## Discovery tests

After metadata changes and a release, repeat these searches:

```text
GitHub repository search:
- generative engine optimization Chinese
- GEO AI visibility China brand
- 中文 GEO AI 搜索
- AI visibility DeepSeek Doubao open source
- GEO website audit Agent Skills

External search:
- site:github.com/ChinaYiqun/GEO-Master
- "GEO-Master" "Generative Engine Optimization"
- "ChinaYiqun/GEO-Master"
```

Record the date, search engine, rank or absence, and query. Indexing can take time; do not treat one immediate search as definitive.

## README signals that should remain near the top

The first screen should contain:

- the expansion `Generative Engine Optimization`;
- the Chinese use case: 中国品牌出海与国内 AI 搜索;
- concrete capabilities: website audit, AI visibility baseline, reproducible experiments, Agent Skills, multi-model monitoring, schemas and data templates;
- named domestic and international platforms;
- a runnable command and links to tests or data;
- English navigation.

## Evidence standard

Search discoverability is not a substitute for product evidence. Keep the repository's distinction between:

- website crawl/readiness signals;
- observed AI platform answers;
- repeated and reproducible results;
- commercial attribution.

Do not claim that metadata, topics, `llms.txt`, Schema, stars, or a single answer prove GEO success.
