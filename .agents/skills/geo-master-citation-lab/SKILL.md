---
name: geo-master-citation-lab
description: Design, run, import, and analyze reproducible AI-search citation experiments for GEO-Master. Use for citation selection, citation absorption, entity exposure, source-domain ecology, cross-platform comparisons, Web versus App differences, and compatible external research datasets. Never turn correlations from a static dataset into platform ranking rules.
---

# GEO-Master Citation Lab

## Purpose

This skill adds an empirical research layer to GEO-Master. It measures observed AI-search behavior rather than assigning a speculative website score.

```text
prompt
→ search triggered
→ sources selected
→ cited content absorbed
→ brand/entity surfaced
→ recommendation formed
→ visit/lead/order evidence
```

Each stage must be measured separately.

## Modes

| Mode | Purpose | Output |
|---|---|---|
| `design` | Create a controlled experiment | protocol and sampling plan |
| `collect` | Record answers, citations, and context | structured run records |
| `selection` | Study which sources are cited | citation-selection report |
| `absorption` | Study how cited pages affect answers | absorption report |
| `entity` | Measure brand/product exposure | entity-exposure report |
| `interface` | Compare Web/App/region/login states | interface comparison |
| `import` | Map external datasets into GEO-Master | field map and import manifest |
| `compare` | Compare platforms, periods, or interventions | controlled delta report |

Use one mode per execution.

## Experiment design

Record at minimum:

- experiment ID and protocol version;
- prompt ID and exact prompt text;
- prompt category and user intent;
- platform, interface, model label, region, language, login state;
- collection time and collector method;
- new conversation or follow-up context;
- answer text or authorized reference to raw answer;
- visible citations and their order;
- errors, refusals, timeouts, or missing citations;
- brand, competitor, and entity targets;
- disclosure of automation, APIs, scraping services, or manual collection.

Prefer controlled prompt sets and repeated runs. Do not mix Web and App records without an explicit interface field.

## Search triggering

Classify each run as:

```text
search_visible
search_inferred
answer_without_visible_search
citations_without_clear_search_state
no_usable_answer
collection_failed
unknown
```

Visible citations do not prove that every sentence came from those pages.

## Citation selection

For every citation record capture:

- URL and canonical URL where available;
- registrable domain;
- citation order and interface position;
- source type;
- official brand source or independent source;
- page availability at collection time;
- duplicate, syndicated, redirected, or mirrored relationship;
- page title, language, publication date, and last-modified date when observable.

Suggested source types:

```text
official_site
news_media
industry_media
community
video
marketplace
review_platform
academic
public_institution
documentation
aggregator
unknown
```

Citation breadth is not the same as answer influence.

## Citation absorption

When both the answer and cited page are available, evaluate observable overlap:

- named entities;
- numbers, dates, units, and product parameters;
- definitions;
- comparisons;
- procedural steps;
- unique phrases;
- supported paraphrases;
- conflicts across cited sources;
- claims present in the answer but unsupported by accessible citations.

Use conservative labels:

```text
strong_supported_overlap
partial_supported_overlap
possible_semantic_overlap
citation_without_detected_overlap
page_unavailable
answer_unavailable
not_evaluable
```

This is text-and-source analysis, not access to model-internal attribution.

## Entity exposure

Measure separately:

- brand mentioned;
- product/model mentioned;
- official site cited;
- candidate-list inclusion;
- explicit recommendation;
- recommendation reason;
- sentiment or risk framing;
- factual accuracy;
- obsolete, conflicting, or hallucinated facts;
- competitor share of mentions and recommendation positions.

A domain citation does not automatically mean positive brand exposure.

## Interface and platform comparisons

Control or record:

- Web versus App;
- desktop versus mobile where relevant;
- country and language;
- signed-in versus signed-out;
- free versus paid tier when observable and permitted;
- conversation state;
- model/version label displayed by the product;
- collection method and provider.

Do not publish a platform ranking without comparable samples and uncertainty reporting.

## Importing external research

Before importing:

1. Read the source dataset documentation and license.
2. Record source repository, release/tag/commit, retrieval date, and checksum.
3. Preserve original IDs and raw fields.
4. Create a transformation map rather than overwriting raw data.
5. Keep source-specific limitations beside derived metrics.
6. Do not republish restricted PDFs or third-party assets.
7. Separate raw, normalized, analytical, and published layers.

Recommended layout:

```text
data/external/<source>/<version>/manifest.json
 data/external/<source>/<version>/raw/          # only when redistribution is allowed
 data/external/<source>/<version>/normalized/
 data/external/<source>/<version>/reports/
```

For large datasets, store only manifests, schemas, queries, and reproducible download instructions in GEO-Master unless redistribution is necessary and permitted.

## GEO Citation Lab bridge

`yaojingang/geo-citation-lab` can serve as an external research source for:

- controlled cross-platform prompt experiments;
- citation selection versus citation absorption;
- Chinese generative-search citation ecology;
- Web/App interface differences;
- source-domain and page-feature analysis;
- reproducible scripts, reports, and research navigation.

Important limitations must travel with any derived conclusion:

- static datasets describe a collection snapshot, not permanent platform behavior;
- some source datasets lack complete answer text, timestamps, model versions, or collection batches;
- correlation between page features and citation outcomes is not a ranking rule;
- citation frequency, brand recommendation, sentiment, and business conversion require different data.

## GEO-Master compatibility

Use or extend:

- `schemas/engine-run.schema.json` for run-level records;
- `templates/baseline-query-set.csv` for prompts;
- `templates/weekly-monitoring.csv` for repeated observations;
- `templates/claims-and-sources.csv` for factual verification;
- `templates/lead-attribution.csv` for downstream outcomes.

Stable keys should connect:

```text
experiment_id
run_id
prompt_id
answer_id
citation_id
canonical_page_id
domain_id
entity_id
claim_id
```

## Reporting

Every report must state:

- sample scope;
- collection period;
- platform/interface coverage;
- missing fields and failed runs;
- repeated-run policy;
- normalization and deduplication rules;
- descriptive findings;
- uncertainty and alternative explanations;
- claims that the evidence does not support.

## Guardrails

- Do not fabricate platform runs or citations.
- Do not infer current behavior from an old static snapshot without qualification.
- Do not call a citation a recommendation unless the answer explicitly recommends the entity.
- Do not treat page-length, Q&A format, Schema, or evidence density as guaranteed ranking factors.
- Do not bypass access controls or platform terms.
- Do not expose private prompts, customer data, credentials, or unpublished business results.
- Do not republish third-party datasets or papers beyond their licenses.

## Attribution

This original GEO-Master workflow is informed by `yaojingang/geo-citation-lab`, whose software components use MIT licensing and whose original reports/documentation/visualizations use CC BY 4.0, with third-party materials retaining their own terms. No large dataset, paper collection, or substantial source code is vendored by this skill.

## Completion report

End each run with:

```text
mode
protocol and version
data source and license
sample collected or imported
normalization performed
findings supported
findings not supported
remaining limitations
next single action
```
