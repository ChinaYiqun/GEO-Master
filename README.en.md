# GEO-Master — Open-source GEO Engineering Toolkit for Chinese Brands

> **Generative Engine Optimization (GEO), AI Search Optimization, and AI Visibility** for Chinese brands operating in global markets and domestic AI search ecosystems.

[简体中文](README.md) | **English**

[![GitHub stars](https://img.shields.io/github/stars/ChinaYiqun/GEO-Master?style=social)](https://github.com/ChinaYiqun/GEO-Master/stargazers)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Validation](https://github.com/ChinaYiqun/GEO-Master/actions/workflows/validate.yml/badge.svg)](https://github.com/ChinaYiqun/GEO-Master/actions/workflows/validate.yml)
[![Version](https://img.shields.io/badge/version-0.3.0--dev-informational.svg)](CHANGELOG.md)

GEO-Master is an evidence-first, reproducible open-source toolkit for studying and improving how brands are discovered, understood, mentioned, cited, and recommended by:

- global AI search products: ChatGPT, Perplexity, Gemini, Claude, Google AI Search;
- Chinese AI search products: DeepSeek, Doubao, Tencent Yuanbao, Kimi, and Qwen.

It combines website GEO audits, real-query visibility baselines, reproducible experiments, Agent Skills, provider-neutral monitoring schemas, import adapters, cases, and reusable CSV/YAML/JSON templates.

```text
discovered → understood → mentioned → cited → recommended → visited → contacted
```

GEO-Master does **not** treat crawler access, Schema, `llms.txt`, backlinks, a heuristic score, or one AI answer as proof of stable visibility or commercial success.

## Why this is not just another GEO guide

| Claim | Verifiable repository asset |
|---|---|
| Website GEO audit workflow | [geo-master Agent Skill](.agents/skills/geo-master/SKILL.md) |
| Real AI visibility baseline | [Baseline playbook](playbooks/ai-visibility-baseline.md) and [30-query bilingual set](templates/baseline-query-set.csv) |
| Multi-model monitoring contract | [Monitor Skill](.agents/skills/geo-master-monitor/SKILL.md) and [monitor-run schema](schemas/monitor-run.schema.json) |
| Provider data integration | [Elmo and GEO/AEO Tracker importer](scripts/import_monitor_runs.py) |
| Reproducible analysis | [Visibility summary CLI](scripts/summarize_visibility.py) and its [standard-library test](scripts/test_summarize_visibility.py) |
| Citation and absorption experiments | [Citation Lab Skill](.agents/skills/geo-master-citation-lab/SKILL.md) |
| Cases with evidence labels | [Case library](cases/README.md) and [evidence standard](EVIDENCE-STANDARD.md) |
| Machine-readable records | [Schemas](schemas/) and [example data](data/README.md) |
| Reusable operating assets | [Templates](templates/README.md) and [playbooks](playbooks/README.md) |

## Five-minute reproducible demo

Clone the repository and generate a platform-level visibility summary from the bundled monitoring template:

```bash
git clone https://github.com/ChinaYiqun/GEO-Master.git
cd GEO-Master

python scripts/summarize_visibility.py templates/weekly-monitoring.csv
python scripts/summarize_visibility.py templates/weekly-monitoring.csv \
  --format json \
  --output out/visibility-summary.json
```

Run the executable checks:

```bash
python scripts/test_summarize_visibility.py
python scripts/test_import_monitor_runs.py
python scripts/validate_examples.py
```

The summary CLI uses only the Python standard library. Unknown and blank observations are excluded from denominators instead of being silently counted as failures.

## Core capabilities

| Capability | What it provides | Entry point |
|---|---|---|
| Website GEO audit | Crawler access, extractability, brand facts, Schema, obsolete content, citability and evidence gaps | [geo-master Skill](.agents/skills/geo-master/SKILL.md) |
| AI visibility baseline | Repeatable queries, environment controls, raw-answer retention and separate mention/citation/recommendation/accuracy metrics | [Baseline playbook](playbooks/ai-visibility-baseline.md) |
| Citation experiments | Controlled prompt experiments, citation selection, content absorption, entity exposure and Web/App differences | [Citation Lab Skill](.agents/skills/geo-master-citation-lab/SKILL.md) |
| Multi-model monitoring | Brand and competitor share of voice, citation domains, regional differences, history and drift alerts | [Monitor Skill](.agents/skills/geo-master-monitor/SKILL.md) |
| Monitoring data normalization | Import Elmo or GEO/AEO Tracker exports into a provider-neutral schema | [Importer documentation](scripts/README.md) |
| Content engineering | Brand facts, question maps, briefs, review, publishing, multi-site distribution and retesting | [Integrations](integrations/README.md) |
| Cases and evidence | Domestic and international cases with claimed, observed, reproduced and verified states kept separate | [Cases](cases/README.md) |
| Templates and schemas | CSV, YAML, Markdown and JSON assets for baselines, monitoring, audits, facts, content and attribution | [Templates](templates/README.md) |

## Thirty-minute baseline

Start with three files:

1. [AI visibility baseline playbook](playbooks/ai-visibility-baseline.md)
2. [30 bilingual baseline queries](templates/baseline-query-set.csv)
3. [Weekly monitoring CSV](templates/weekly-monitoring.csv)

Minimum design:

```text
10 real user questions
× 2 AI platforms
× 1–3 runs per question
→ record mentions, citations, recommendations and fact accuracy
```

For a stronger baseline, use at least 20 questions, two platforms, and three runs for high-priority questions while recording date, region, language, account state, conversation state, model or mode, raw answer, and cited URLs.

## Three Agent Skills

### `geo-master`

Use for website diagnosis, full audits, brand fact governance, query baselines, content plans, GEOFlow-style operations, and before/after verification.

### `geo-master-citation-lab`

Use for controlled citation-selection and content-absorption experiments, entity exposure, platform/language/region comparisons, and licensed external research imports.

### `geo-master-monitor`

Use for provider-neutral multi-model monitoring, brand and competitor observations, citation opportunities, regional differences, historical comparisons, weekly/monthly reporting, and drift alerts.

## Measurement model

Keep these four outcomes separate:

```text
brand mentioned
brand or official site cited
brand explicitly recommended
brand facts described accurately
```

Record commercial outcomes separately:

```text
AI mention or citation
→ click or branded search
→ website visit
→ lead
→ quote
→ order
```

Evidence states used by the repository include:

```text
verified       confirmed by reliable evidence
reproduced     repeated under recorded conditions
observed       limited observation
claimed        asserted by a source
pending        verification incomplete
expired        no longer current
unknown        evidence unavailable
not_provided   source did not provide the information
```

## Repository structure

```text
GEO-Master/
├── .agents/skills/  # executable GEO Agent Skills
├── cases/           # cases, evidence checks and failure modes
├── playbooks/       # repeatable execution procedures
├── explainers/      # metrics, mechanisms and boundaries
├── integrations/    # ecosystem and adapter architecture
├── templates/       # CSV, YAML and Markdown assets
├── references/      # source and reading indexes
├── data/            # examples and reproducible data conventions
├── schemas/         # machine-readable contracts
├── scripts/         # import, validation and analysis tools
├── docs/            # project and repository operations
├── AGENTS.md        # AI coding rules
└── ROADMAP.md       # 90-day roadmap
```

## What the project will not do

- fabricate reviews, citations, community posts, or customer evidence;
- mass-produce low-value pages or undisclosed promotional replies;
- present heuristic scores as official platform ranking mechanisms;
- claim that `llms.txt`, Schema, crawler access, or backlinks guarantee inclusion;
- turn vendor claims or unverifiable order numbers into facts;
- hide negative mentions, incorrect facts, missing platforms, or failed experiments inside one aggregate score;
- copy code, datasets, papers, screenshots, or content beyond license and copyright permissions.

## Start here

- [Start here](START-HERE.md)
- [Case library](cases/README.md)
- [Playbooks](playbooks/README.md)
- [Templates](templates/README.md)
- [Evidence standard](EVIDENCE-STANDARD.md)
- [Tool ecosystem](integrations/README.md)
- [Roadmap](ROADMAP.md)
- [Repository discovery checklist](docs/REPOSITORY-DISCOVERY.md)

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md), and [CASE-TEMPLATE.md](CASE-TEMPLATE.md). Contributions are welcome for real cases, failed experiments, platform changes, datasets, prompts, adapters, monitoring integrations, and evidence corrections.

## Citation and license

Use [CITATION.cff](CITATION.cff) when citing the repository in research, reports, training, or client work. Original GEO-Master code and content are licensed under the [MIT License](LICENSE); third-party assets remain under their respective licenses and copyright terms.
