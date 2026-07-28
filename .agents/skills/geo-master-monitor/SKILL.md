---
name: geo-master-monitor
description: Operate a provider-neutral, evidence-based AI visibility monitoring workflow for GEO-Master. Use for scheduled multi-model prompt runs, brand and competitor tracking, citation analysis, geographic comparisons, drift alerts, citation opportunities, historical reporting, and bridges to self-hosted tools such as Elmo or GEO/AEO Tracker. Never present scraper output, demo data, heuristic scores, or provider-normalized answers as equivalent without recording collection method and limitations.
---

# GEO-Master Monitor

## Purpose

This skill provides the long-running monitoring layer missing from a documentation-only GEO repository.

```text
brand and competitor setup
→ prompt portfolio
→ provider adapters
→ scheduled runs
→ normalized evidence
→ mentions/citations/recommendations/accuracy metrics
→ drift and opportunity analysis
→ content or fact correction
→ business attribution
```

It is provider-neutral. GEO-Master owns the measurement contract; external platforms may execute and visualize the runs.

## Modes

| Mode | Purpose | Output |
|---|---|---|
| `setup` | Configure a brand, competitors, markets, and providers | monitoring manifest |
| `prompts` | Build and govern a prompt portfolio | prompt set |
| `run` | Execute or import a batch of platform observations | normalized run records |
| `visibility` | Measure brand visibility and accuracy | visibility report |
| `citations` | Analyze cited domains and pages | citation report |
| `competitors` | Compare brands and recommendation positions | competitor report |
| `opportunities` | Find missing sources and content gaps | prioritized opportunity list |
| `drift` | Detect material changes over time | alert report |
| `geo` | Compare countries, languages, or interfaces | geographic comparison |
| `report` | Produce periodic stakeholder reporting | weekly/monthly report |
| `bridge` | Map Elmo, GEO/AEO Tracker, or another system into GEO-Master | adapter specification |

Use one mode per execution.

## Monitoring manifest

Define:

```yaml
project_id:
brand:
  canonical_name:
  aliases: []
  official_domains: []
competitors: []
markets:
  - country:
    language:
    interface:
providers: []
schedule:
query_set_version:
brand_fact_version:
retention_policy:
```

Never infer aliases or competitors silently. Record when each was added or retired.

## Prompt portfolio

Prompts should reflect real user decisions, not only branded searches.

Required categories:

- category discovery;
- problem/solution;
- recommendation;
- comparison;
- product selection;
- alternatives;
- pricing or commercial intent;
- local or regional availability;
- support, risk, or limitation;
- brand and product fact checks.

Each prompt records:

```text
prompt_id
exact_text
language
market
intent
funnel_stage
expected_entities
business_value
owner
active_from
active_to
version
```

Persona variants may be useful, but do not multiply prompts merely to inflate run volume. Preserve the parent prompt ID.

## Provider and collection adapters

For every provider run record:

- provider/product name;
- visible model label where available;
- API, browser automation, scraper, data vendor, manual, or imported method;
- country, language, interface, login state, and plan tier where observable;
- collection timestamp;
- request/response identifiers where permitted;
- raw answer reference;
- visible citations;
- failure state and retry count;
- cost and latency when available.

Collection methods are not interchangeable. A third-party scraper may expose a different interface, model, locale, or citation representation from the consumer product.

## Parallel execution

Parallel prompt × provider runs are allowed when the provider and account terms permit them.

Control:

- concurrency;
- per-provider rate limits;
- retries with backoff;
- timeout;
- idempotency key;
- run batch ID;
- cost ceiling;
- cancellation and partial completion;
- duplicate response detection.

Do not hide missing providers. A partial batch remains partial.

## Normalized measurements

Keep these metrics separate.

### Visibility

- mention present;
- first mention position;
- number of mentions;
- candidate-list inclusion;
- explicit recommendation;
- recommendation position;
- positive, neutral, negative, or mixed framing;
- share of voice across a controlled prompt set.

### Citations

- official domain cited;
- any brand-controlled page cited;
- independent source cited;
- citation order;
- cited-domain frequency;
- cited-page frequency;
- citation diversity;
- competitor-only citation pages;
- inaccessible or redirected citations.

### Accuracy

Compare answer claims against the active brand fact version:

- accurate;
- partially accurate;
- outdated;
- conflicting;
- unsupported;
- not evaluable.

### Commercial outcomes

Track separately:

- AI referral;
- branded search;
- direct visit;
- lead;
- qualified lead;
- quote;
- order;
- revenue;
- attribution confidence.

Do not create a single score that hides negative mentions, factual errors, missing providers, or sample imbalance.

## Competitor intelligence

Compare competitors using identical prompts and controlled collection conditions.

Report:

- mention share;
- recommendation share;
- average recommendation position;
- official-site citation share;
- independent-source citation share;
- cited domains unique to each competitor;
- claims or proof points repeatedly used as recommendation reasons;
- markets and interfaces where outcomes diverge.

A competitor battlecard must preserve evidence links and distinguish platform observations from analyst interpretation.

## Citation opportunities

An opportunity exists when a relevant source or page repeatedly supports competitors but not the target brand.

Classify opportunities:

```text
missing_official_answer
missing_product_fact
missing_comparison_content
missing_independent_evidence
outdated_brand_information
weak_entity_consistency
technical_access_problem
source_relationship_opportunity
not_actionable
```

Do not recommend buying links, manipulating communities, fabricating reviews, or creating ineligible Wikipedia pages.

## Geographic and interface analysis

Compare by:

- country;
- language;
- Web/App;
- desktop/mobile when material;
- logged-in/logged-out;
- provider account tier;
- collection method.

Use comparable prompt translations and preserve the original meaning. Do not treat raw prompt translation as equivalent without review.

## Drift alerts

Alerts should rely on minimum sample and persistence rules.

Possible triggers:

- official citation disappears across repeated runs;
- recommendation share falls materially;
- a competitor enters high-value prompts;
- inaccurate or outdated fact appears repeatedly;
- negative framing persists;
- citation domain mix changes sharply;
- provider failures exceed a threshold;
- a market diverges from the global baseline.

Record:

```text
alert_id
metric
baseline_window
comparison_window
absolute_change
relative_change
sample_size
persistence_rule
severity
supporting_runs
status
owner
```

Avoid alerts based on one volatile answer unless the event is a severe factual or safety issue.

## Historical reporting

Weekly and monthly reports should include:

1. coverage and failed runs;
2. prompt and provider changes;
3. mention, citation, recommendation, and accuracy trends;
4. competitor movement;
5. citation opportunities;
6. important raw examples;
7. completed actions;
8. before/after evidence;
9. business outcomes with attribution confidence;
10. next prioritized actions.

Every chart must disclose denominator, period, providers, and missing data.

## Elmo bridge

`elmohq/elmo` is a self-hosted AI visibility platform useful for:

- recurring prompt execution;
- tracking brand mentions, descriptions, and citations;
- competitor benchmarking;
- automated reporting;
- multi-organization or white-label deployment;
- retaining monitoring data on infrastructure controlled by the operator.

Bridge requirements:

- map Elmo brand, prompt, provider, response, citation, and competitor records to GEO-Master stable IDs;
- retain raw response references and provider metadata;
- export normalized results into `engine-run` compatible records;
- document Elmo version and adapter version;
- avoid assuming Elmo metrics use GEO-Master definitions until mapped and tested.

## GEO/AEO Tracker bridge

`danishashko/geo-aeo-tracker` provides useful patterns for:

- local-first project storage;
- multi-model parallel batches;
- country-scoped tracking;
- prompt and persona management;
- citation-domain aggregation;
- competitor-only citation opportunities;
- drift alerts and historical deltas;
- scheduled runs;
- optional cloud persistence;
- provider-specific scraping and grounded-search stages.

Bridge requirements:

- disclose Bright Data, OpenRouter, Gemini, browser, or other collection routes;
- treat demo data as demo data;
- record provider dataset IDs or adapter identifiers without exposing secrets;
- map local IndexedDB/Supabase records to exportable GEO-Master schemas;
- keep SRO or visibility scores decomposable into underlying observations;
- do not equate scraper representation with the exact public consumer interface.

## Data storage

Recommended separation:

```text
private/raw/                 answers, screenshots, credentials-free request metadata
private/normalized/          normalized run and citation records
public/examples/             sanitized examples
public/reports/              aggregated reports with evidence limits
```

Never commit API keys, cookies, service-role credentials, private prompts, customer data, or raw commercial records.

## Guardrails

- Respect provider terms, robots rules, rate limits, and applicable law.
- Do not bypass authentication, CAPTCHAs, access restrictions, or paywalls.
- Do not claim all providers were measured when adapters were missing.
- Do not compare different countries, interfaces, or models as if controlled.
- Do not use a composite score as the only evidence.
- Do not fabricate citations, sentiment, recommendation positions, or conversions.
- Do not let an LLM-generated analysis overwrite raw observations.
- Require human review before customer-facing claims or publication.

## Attribution

This original GEO-Master monitoring workflow is informed by:

- `elmohq/elmo`, MIT licensed, copyright Blue Whale Software, LLC;
- `danishashko/geo-aeo-tracker`, MIT licensed, copyright Daniel Shashko.

No substantial third-party source code is vendored by this skill. Future code reuse must preserve copyright and license notices.

## Completion report

End each run with:

```text
mode
project and prompt-set version
providers requested and completed
collection methods
runs completed and failed
metrics calculated
alerts or opportunities found
limitations
next single action
```
