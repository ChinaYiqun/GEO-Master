---
name: geo-master
description: Audit websites for AI-search readiness, build evidence-based GEO baselines, plan content improvements, and connect GEO-Master assets with GEOFlow-style content operations. Use for GEO audits, AI crawler checks, citability reviews, brand fact governance, query baselines, content plans, multi-site workflow design, and before/after verification. Never claim that a heuristic score proves ChatGPT, Doubao, DeepSeek, Claude, Gemini, or Perplexity visibility.
---

# GEO-Master Skill

## Purpose

This skill turns GEO-Master from a reference repository into an executable workflow:

```text
website discovery and audit
→ brand facts and source verification
→ real user query baseline
→ content and technical remediation
→ optional GEOFlow production/distribution plan
→ repeated AI-platform testing
→ evidence-labelled report
```

The skill combines three complementary layers:

1. **GEO-Master evidence layer** — real queries, repeat runs, source tracking, evidence grades, and commercial attribution boundaries.
2. **Website audit layer** — crawler access, content extractability, structured data, technical SEO, and report generation.
3. **Content operations layer** — knowledge bases, prompts, review, publishing, and multi-site distribution workflows compatible with GEOFlow-style operations.

## Route

Select exactly one mode for the current task.

| Mode | Use when | Primary output |
|---|---|---|
| `quick` | A fast website diagnosis is needed | concise findings and next actions |
| `audit` | A full GEO and SEO review is needed | `GEO-AUDIT-REPORT.md` |
| `baseline` | The user needs real AI-platform visibility measurements | query set and run plan |
| `content` | The user needs pages, FAQs, comparisons, or briefs | prioritized content plan |
| `facts` | Brand names, models, parameters, dates, or claims conflict | brand fact and source plan |
| `workflow` | The user wants a repeatable production and distribution system | GEOFlow-compatible operating design |
| `verify` | Changes have already been made | before/after evidence comparison |

Do not mix unrelated modes in one change. A full program may run the modes sequentially, but each execution should state its current mode.

## Required discovery

Before recommendations:

1. Confirm the target URL, brand, market, language, and business type.
2. Fetch the homepage and relevant public pages.
3. Inspect `robots.txt`, sitemap availability, canonical URLs, page titles, rendered text, and structured data.
4. Identify whether core facts are present as text rather than only images, scripts, PDFs, or authenticated content.
5. Search the repository for existing brand facts, query sets, cases, or templates before creating new ones.
6. Separate what was directly observed from what still requires a real platform test.

Never treat a single fetched page as proof of the whole site.

## Mode: quick

Use a limited, evidence-based snapshot. Check:

- Can public crawlers access the site?
- Is the brand and product identity explicit?
- Are important claims supported by sources, dates, or test conditions?
- Does the site directly answer real customer questions?
- Are there obvious conflicts between pages, languages, PDFs, and product versions?
- Are important pages discoverable through navigation or sitemap?
- Is there a clear next action for interested visitors?

Return no invented overall score. Use priorities:

```text
critical  blocks discovery or makes key facts unreliable
high      materially reduces understanding or citation readiness
medium    limits coverage or usefulness
low       polish or optional enhancement
```

## Mode: audit

### A. Discovery and access

Check:

- HTTP availability and redirects;
- robots rules affecting major search and AI crawlers;
- sitemap presence and useful coverage;
- canonical consistency;
- public accessibility without login;
- server-rendered or otherwise extractable main content;
- stable URLs and internal linking;
- duplicate and obsolete pages.

Crawler access is a prerequisite, not proof of inclusion or recommendation.

### B. Brand facts and entity clarity

Extract and compare:

- official brand and company names;
- aliases and language variants;
- product families, models, versions, and lifecycle status;
- service regions and contact information;
- prices, availability, delivery, and after-sales terms;
- certifications, awards, tests, and case studies;
- effective dates and last-updated dates.

Classify each material claim as:

```text
verified       confirmed by a reliable source
reproduced     observed repeatedly under recorded conditions
observed       seen in a limited test
claimed        asserted by a company, customer, author, or service provider
pending        verification incomplete
expired        no longer current
unknown        evidence unavailable
not_provided   source did not provide the information
```

### C. Content usefulness and extractability

Evaluate whether pages:

- answer the main question early;
- use descriptive headings;
- contain self-contained factual passages;
- explain who the product is for and not for;
- include limitations and trade-offs;
- distinguish facts from marketing claims;
- provide dates, units, test conditions, and sources;
- include comparison, selection, FAQ, case, and support content where appropriate;
- remain understandable when a paragraph is extracted from the page.

Do not enforce a universal passage length. Word-count patterns can be diagnostic hints, not ranking rules.

### D. Structured and technical signals

Review:

- Organization, Product, Article, FAQ, LocalBusiness, SoftwareApplication, Breadcrumb, and other relevant JSON-LD;
- consistency between structured data and visible text;
- author, publisher, date published, and date modified fields;
- Open Graph and social metadata;
- mobile usability and basic performance risks;
- security and mixed-content problems;
- broken links and redirect chains.

Schema can reduce ambiguity but does not guarantee AI citation.

### E. Off-site evidence

Identify relevant independent sources:

- industry publications;
- customer reviews;
- documentation and standards bodies;
- YouTube demonstrations;
- Reddit and specialist communities;
- GitHub, Product Hunt, G2, Trustpilot, or sector-specific platforms;
- Wikipedia or Wikidata only where notability and policy requirements are genuinely satisfied.

Do not recommend fabricated reviews, undisclosed promotion, mass posting, or manipulating community discussions.

### F. Report

The report must include:

1. scope and observation date;
2. pages and sources inspected;
3. verified facts;
4. critical conflicts and risks;
5. technical findings;
6. content gaps mapped to user questions;
7. prioritized fixes;
8. a real platform baseline plan;
9. evidence limitations;
10. measurement and attribution plan.

## Mode: baseline

A GEO baseline measures actual answers, not website appearance alone.

Use or adapt:

- `templates/baseline-query-set.csv`;
- `templates/weekly-monitoring.csv`;
- `schemas/engine-run.schema.json`;
- `playbooks/ai-visibility-baseline.md`.

Minimum recommended design:

```text
20 or more real user questions
2 or more AI platforms
3 runs per important question where practical
new conversations separated from follow-up conversations
region, language, date, login state, and model recorded
raw answer and cited URLs retained
```

Measure separately:

- brand mentioned;
- official site cited;
- brand explicitly recommended;
- brand facts described accurately;
- competitor coverage;
- negative or obsolete information;
- referral, brand search, visit, lead, quote, and order evidence.

If direct access to an AI platform is unavailable, produce the test plan and mark results as `pending`. Never simulate a platform result and present it as observed.

## Mode: facts

Create or update a brand fact system using:

- `templates/brand-facts.yaml`;
- `templates/claims-and-sources.csv`;
- stable IDs connecting facts, pages, queries, and observations.

For every important fact record:

- exact claim;
- product or entity scope;
- effective and expiry dates;
- official source;
- independent source where available;
- evidence state;
- owner and reviewer;
- affected pages and languages;
- correction or retirement action.

Fix fact conflicts before producing more content.

## Mode: content

Start from real customer questions, not keyword volume alone.

Prioritize content that fills an evidence gap:

- direct-answer product pages;
- comparison and selection guides;
- use-case and limitation pages;
- FAQs;
- testing methodology and results;
- implementation cases;
- support, warranty, delivery, and regional availability pages;
- version and product-lifecycle notices.

Each content brief should define:

- target question and user intent;
- direct answer;
- facts required;
- evidence required;
- claims that must not be made;
- comparison dimensions;
- page owner and review date;
- baseline query and retest schedule;
- commercial next action.

## Mode: workflow

Use this mode when the user wants GEOFlow-style content engineering or multi-site distribution.

### Inputs

GEO-Master provides the governance inputs:

```text
brand-facts.yaml
claims-and-sources.csv
question-map.csv
content-brief.md
baseline-query-set.csv
weekly-monitoring.csv
```

### Operating flow

```text
approved facts and source documents
→ knowledge-base ingestion and chunking
→ question and content-brief selection
→ model and prompt configuration
→ draft generation
→ factual and compliance review
→ local or channel publication
→ sitemap, structured data, and machine-readable maps
→ AI-platform retest
→ lead and business attribution
→ correction and content refresh
```

### GEOFlow compatibility principles

When integrating with GEOFlow or a similar system:

1. Use supported APIs, CLI commands, queues, and authenticated interfaces.
2. Discover real routes and capabilities before proposing commands.
3. Separate draft generation, review, approval, publication, synchronization, and deletion.
4. Keep secrets, credentials, customer data, and unpublished business facts out of public repositories.
5. Preserve source IDs and fact versions through the content pipeline.
6. Require human approval for factual claims, regulated content, publication, and destructive actions.
7. Treat `llms.txt`, sitemap, Schema, and static distribution as discoverability aids, not guarantees.
8. Prevent mass low-value page generation, location swapping, and duplicate multi-site content.
9. Feed published URLs and change dates back into the GEO-Master monitoring records.
10. Compare observed AI answers before and after publication using the same query set.

### Build versus integrate

Do not copy the full GEOFlow application into GEO-Master. Keep responsibilities separated:

- GEO-Master: standards, cases, templates, audits, tests, evidence, and benchmark data;
- GEOFlow: deployable content operations, review, publishing, and distribution;
- commercial product: managed implementation, monitoring, reporting, and support where offered.

## Mode: verify

Use identical or controlled query sets before and after changes. Report:

- what changed;
- when it changed;
- which URLs were affected;
- what remained constant;
- platform, model, region, language, and login state;
- run counts;
- changes in mentions, citations, recommendations, and accuracy;
- other plausible explanations;
- business results with attribution confidence.

Do not attribute an order to GEO solely because it happened after an optimization.

## Guardrails

- Do not invent platform-specific ranking factors.
- Do not claim that `llms.txt`, Schema, crawler access, or a high heuristic score guarantees inclusion.
- Do not hide commercial relationships.
- Do not manufacture reviews, citations, community posts, or customer evidence.
- Do not expose credentials or private customer data.
- Do not publish generated content without required review.
- Do not convert third-party marketing numbers into verified facts.
- Do not copy substantial third-party code without preserving the applicable license and attribution.

## Third-party inspiration and attribution

This original GEO-Master workflow was informed by, but does not vendor or reproduce substantial code from:

- `zubair-trabzada/geo-seo-claude` — MIT-licensed Claude Code GEO/SEO audit skill by Zubair Trabzada. Useful concepts include routed audit modes, crawler checks, structured-data review, reporting, and client workflow support.
- `yaojingang/GEOFlow` — Apache-2.0-licensed GEO content engineering and multi-site distribution system. Useful concepts include knowledge-base/RAG inputs, review and publishing stages, queues, channel distribution, analytics, and an operational Agent Skill.

When code or substantial content is later incorporated from either project, preserve its copyright notice, license requirements, modification notices, and any NOTICE obligations.

## Completion report

At the end of every run, state:

```text
mode selected
scope inspected
facts directly observed
facts still pending
files or pages changed
verification performed
remaining risks
next single action
```
