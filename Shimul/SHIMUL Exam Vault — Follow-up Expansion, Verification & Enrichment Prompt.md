# Agent Prompt: SHIMUL Exam Study Vault — Expansion, Verification & Quality Upgrade

## 0. CONTEXT

The SHIMUL/Karnataka cooperative-dairy exam research vault has **already been created and populated using the previous master research prompt**.

This is **NOT a request to rebuild the vault from scratch**.

Your task is to perform a structured **audit → verify → fix → expand → enrich → re-index** pass over the existing workspace.

The existing material, structure, diagrams, tables, notes, PYQs and quiz content are valuable and must be treated as the current baseline.

### Core rule

**Preserve before expanding.**

Do not casually delete, replace, rewrite away, or collapse existing material merely because you are adding newer/better material.

Where existing content is valid:
- retain it;
- improve it only where useful;
- add missing depth around it.

Where existing content is outdated, incorrect, ambiguous, poorly sourced, duplicated, or misleading:
- correct it;
- clearly indicate what was changed where appropriate;
- preserve historical information when it is historically relevant rather than overwriting it with current information.

The goal is to make the vault **broader, deeper, more current and more exam-useful without losing the simplicity and readability of the existing material**.

---

# 1. PRIMARY OBJECTIVE

Upgrade the existing SHIMUL study vault into a **comprehensive, current, competitive-exam-ready knowledge base covering SHIMUL, KMF, Karnataka cooperative dairying and Karnataka cooperative-society topics**.

The upgraded vault should function simultaneously as:

1. A rapid revision resource.
2. A conceptual learning resource.
3. A factual/GK reference.
4. A current-affairs reference.
5. A quick-lookup handbook.
6. A source-backed database of important facts and statistics.
7. A foundation from which a future LLM can quiz and teach me.

Maintain the same overall **simple, structured, exam-focused flavour** of the existing vault.

Do NOT turn it into an academic textbook.

The ideal style is:

**Simple explanation → structured facts → visual/flowchart → quick table → important exam points → deeper supporting detail → sources.**

---

# 2. SOURCE & FACT-CHECKING GUARDRAILS

This is one of the highest-priority requirements.

## 2.1 Source hierarchy

Use the following source priority whenever possible:

### Tier 1 — Primary / Official
Prefer these for factual authority:

- SHIMUL official sources
- KMF official website/publications
- Karnataka Government departments
- Karnataka Department of Cooperation
- Registrar of Co-operative Societies, Karnataka
- Karnataka Government Gazettes / official notifications
- Karnataka Milk Federation annual reports / official reports
- District Milk Unions and their official publications
- Government of India ministries/departments
- Ministry of Cooperation
- Department of Animal Husbandry & Dairying
- NDDB
- India Code
- Official Acts, Rules, notifications, circulars and amendments
- Official statistical publications and annual reports
- Official parliamentary/government documents wherever relevant

For legal material, use the **official/current statutory source wherever available**, rather than relying on coaching material or secondary summaries.

### Tier 2 — Institutional / High-quality secondary
Use where appropriate:

- Established newspapers/publications
- Reputed research institutions
- Officially affiliated/institutional publications
- Established industry bodies

### Tier 3 — Coaching / Exam-preparation sources
Sources such as Testbook, Adda247, Exampur, coaching websites, blogs, etc. may be used for:

- discovering topics;
- locating potentially useful PYQs;
- identifying recurring exam themes;
- finding explanations where primary material is difficult to interpret.

However:

**Do NOT use coaching material as the final authority for a legal provision, current organizational structure, current office-holder, current numerical statistic, amendment, notification, or other important factual claim when an official source is available.**

### Tier 4 — YouTube

YouTube is primarily an **explanatory/teaching source**, not the final authority for current factual claims where official documentation exists.

When using YouTube:

- Search Kannada and English content.
- Prefer knowledgeable/relevant educational channels.
- Use `ingest-youtube` to extract the transcript/teaching content.
- Do not merely paste a video link.
- Capture the useful explanation/facts from the video.
- Cross-check important factual claims against primary sources wherever possible.

### Hard rule

**A YouTube video or coaching website must not override a current official source.**

If sources conflict:
1. investigate the conflict;
2. prefer the current authoritative primary source;
3. explicitly flag the conflict where it matters.

---

# 3. CURRENT-DATE & CURRENT-AFFAIRS RULE

Treat the **actual date on which this task is executed** as the research cutoff.

Do not assume that information already present in the vault is still current.

For all "current", "latest", "recent", "present", "currently serving", "current structure", "current production", "current membership", etc.:

- verify the latest available information;
- record the relevant date/year/quarter;
- identify whether a change is announced, proposed, approved, or actually implemented;
- do not confuse historical information with current information.

For numerical data, always try to capture:

**Value + unit + geography/entity + period + source + publication/report date.**

For example, distinguish carefully between:

- annual milk procurement;
- daily average procurement;
- peak procurement;
- milk sales;
- milk processing capacity;
- installed capacity;
- actual utilization;
- number of DCS;
- number of members;
- number of producers;
- number of consumers/customers;
- turnover;
- product sales;
- union-wise figures.

Never silently convert one into another.

---

# 4. TASK 1 — AUDIT THE EXISTING VAULT

Before adding material, inspect the entire existing vault.

Create an internal audit of:

### A. Content coverage
What is already well covered?

### B. Missing topics
What important areas are absent?

### C. Weak topics
Where is the material too brief for a competitive exam?

### D. Outdated information
Which facts, structures, office-holders, statistics, schemes or organizational details need current verification?

### E. Rendering issues
Identify:

- broken Mermaid diagrams;
- invalid Mermaid syntax;
- malformed Markdown tables;
- excessively wide tables;
- malformed callouts;
- inconsistent headings;
- links that do not work;
- formatting that could cause poor rendering in Obsidian.

### F. Source-quality issues
Identify important claims based only on weak/secondary sources that can now be upgraded to official sources.

### G. Duplication
Identify redundant content, but **do not remove valid information merely for tidiness**.

Where appropriate, consolidate references while preserving useful content.

---

# 5. TASK 2 — MERMAID & VISUAL STRUCTURE UPGRADE

## 5.1 Fix all existing Mermaid diagrams

Any existing Mermaid diagram that fails to render must be fixed.

Use conservative, Obsidian-compatible Mermaid syntax.

Avoid unnecessarily complicated syntax.

Before considering a diagram complete, check for:

- invalid node syntax;
- malformed arrows;
- unsupported punctuation;
- problematic brackets/quotes;
- excessively long labels;
- unsupported Mermaid features;
- incorrect nesting;
- unclear direction.

Prefer simple diagrams that render reliably.

## 5.2 Add substantially more flowcharts

Do not remove useful existing flowcharts.

Add new flowcharts wherever they materially improve understanding.

Potential areas include, but are not limited to:

### Dairy / KMF / SHIMUL
- Farmer → DCS → Milk Collection → Testing → Chilling → District Union → Processing → Packaging → Distribution → Consumer
- DCS → District Milk Union → KMF relationship
- SHIMUL organizational structure
- KMF organizational ecosystem
- Milk procurement and payment flow
- Milk quality/testing flow
- Cold-chain flow
- Dairy product production flow
- Product distribution/marketing flow
- Cooperative member → society → union → federation relationship
- Government scheme implementation flow where relevant
- Organizational/administrative changes where a flowchart makes them clearer

### Cooperative societies
- Registration process
- Cooperative governance structure
- General Body → Board → Office Bearers relationship
- Election/governance lifecycle
- Audit/accountability structure
- Member admission/rights/responsibilities
- Statutory oversight structure
- Important legal procedures where useful
- Amendment/change pathway where relevant

### Constitution / GK
Add flowcharts only where they genuinely improve comprehension.

Do not create decorative diagrams simply to increase the number.

---

# 6. TASK 3 — FLOWCHART + EXPLANATION RULE

A flowchart must **NOT be the only explanation**.

Whenever a flowchart is added:

### First:
Show the concise visual flow.

### Immediately after:
Explain the same process in simple language.

For example:

> **Flow:** Farmer → DCS → Union → KMF → Market → Consumer

Then explain:

- What each level does.
- What information/material/money moves between the levels.
- Who owns/controls what.
- Where decisions are taken.
- What is unique about each stage.
- What an exam candidate is likely to be asked.

Use consistent tags such as:

`[CONCEPT]`
`[EXAM FACT]`
`[CURRENT]`
`[DATA]`
`[LAW]`
`[PYQ]`
`[OVERLAP]`
`[IMPORTANT]`

Do not overload every sentence with tags. Tag information meaningfully.

---

# 7. TASK 4 — EXPAND QUICK-LOOKUP TABLES

Add more useful tables while retaining all valuable existing tables.

Use tables for information that benefits from comparison or memorization.

Examples include:

### Dairy / KMF / SHIMUL
- KMF vs District Milk Union vs DCS
- KMF vs SHIMUL
- Karnataka Milk Unions and areas covered
- Union headquarters where officially available
- Major dairy plants/facilities
- Milk products and product categories
- Milk-derived products and their uses
- KMF brands/products
- Procurement metrics
- Processing capacity
- Milk sales
- Membership / DCS numbers
- Important institutions and their roles
- Important historical milestones
- Schemes related to dairy/cooperatives
- Current organizational structure
- Recent administrative/structural changes

### Dairy GK
Where reliable data is available, add:

- major milk-producing states;
- Karnataka's position;
- Karnataka milk production;
- union-wise procurement where available;
- annual/quarterly procurement figures;
- major dairy product categories;
- breeds/types of cattle relevant to Karnataka dairy;
- indigenous vs crossbred/exotic breeds;
- buffalo breeds where relevant;
- milk quality/testing terminology;
- important dairy terminology;
- important units and metrics.

Do not manufacture state-wise consumer or enterprise data.

If "consumer base" statistics are not officially published in a sufficiently reliable form, explicitly say so and use the closest valid official metric instead.

---

# 8. TASK 5 — SHIMUL & KMF DEEP-DIVE

Expand the existing dairy-union section significantly.

The vault should make me capable of answering questions such as:

- What is SHIMUL?
- What is KMF?
- How are SHIMUL and KMF connected?
- What is the role of a District Milk Union?
- What is the role of a DCS?
- How does milk move through the cooperative structure?
- How are farmers paid?
- How is milk procured and tested?
- What products are manufactured?
- How is milk marketed?
- What are the major facilities/plants?
- What is the geographic/operational scope?
- What are the major statistics?
- What are major schemes connected to the sector?
- What are the recent organizational changes?
- What administrative or structural changes occurred recently?
- What major current-affairs developments involving SHIMUL/KMF matter for exams?

## Current-affairs subsection

Create a dedicated/currently maintained section for:

**SHIMUL/KMF Current Affairs**

Include, where verified:

- leadership/office-holder changes;
- appointments;
- administrative changes;
- restructuring;
- new plants/projects;
- expansion;
- mergers/reorganization;
- major policy decisions;
- important agreements/MoUs;
- new products;
- technology initiatives;
- procurement changes;
- payment-system changes;
- farmer-oriented initiatives;
- government interventions;
- major financial/operational developments;
- important court/legal developments;
- awards/recognition;
- significant controversies only where reliably documented and exam-relevant.

For each current-affairs item, include:

**Date | Event | What changed | Why it matters | Source**

Do not include trivial news simply because it mentions KMF or SHIMUL.

---

# 9. TASK 6 — GENERAL KNOWLEDGE EXPANSION

Expand the dairy/KMF-related GK substantially.

The GK should go beyond generic "KMF facts".

Include useful factual clusters such as:

### Dairy GK
- milk composition/basic terminology;
- types/forms of milk;
- dairy products;
- milk processing terminology;
- milk preservation;
- pasteurization;
- homogenization;
- fermentation;
- major dairy product categories;
- relevant breeds;
- Karnataka-specific cattle/dairy facts;
- major dairy institutions;
- major dairy schemes;
- White Revolution;
- Operation Flood;
- Anand Pattern;
- NDDB;
- cooperative dairy architecture.

### Karnataka-specific
- major milk unions;
- important dairy locations/plants;
- major dairy-related institutions;
- state-specific dairy initiatives;
- relevant geography/agriculture connections.

### Data & metrics
Where officially available:

- production;
- procurement;
- sales;
- processing;
- capacity;
- members;
- societies;
- consumer/customer reach;
- turnover;
- product volumes;
- year-over-year trends;
- quarter-wise trends.

Always preserve the exact period attached to each number.

---

# 10. TASK 7 — COOPERATIVE SOCIETIES & KARNATAKA CO-OPERATIVE LAW

Expand the existing cooperative-societies material beyond principles and generic governance.

Focus particularly on:

**Karnataka Co-operative Societies Act, 1959 and applicable Rules/amendments.**

Research from official legal/government sources.

## Cover, as relevant to the exam:

- important definitions;
- registration;
- incorporation;
- membership;
- member rights;
- member responsibilities;
- share capital;
- general body;
- board of directors;
- office bearers;
- meetings;
- elections;
- tenure;
- disqualification;
- supersession/administrative intervention where applicable;
- audit;
- inspection;
- inquiry;
- dispute resolution;
- surcharge/recovery;
- accounts;
- returns;
- reserves;
- distribution of profits;
- penalties/offences where relevant;
- winding up;
- liquidation;
- appeals/revisions;
- powers of Registrar;
- government supervision;
- important committees/authorities;
- provisions relevant to cooperative dairy societies/unions.

Do NOT attempt to summarize every section indiscriminately.

Use **exam-weightage + relevance + official-source availability** to prioritize.

## Legal citation rule

For every important provision, identify where possible:

**Act / Rule | Section/Rule number | Topic | Plain-language meaning | Exam relevance | Current status | Official source**

Where an amendment has changed the provision, explain the change briefly.

---

# 11. TASK 8 — AMENDMENT & CURRENT-LAW TRACKING

Create/update a section specifically for:

**Recent amendments / notifications / rule changes**

For each significant change:

| Date | Law/Rule | Provision | What changed | Effective status | Exam relevance | Source |

Distinguish clearly between:

- proposed;
- introduced;
- passed;
- notified;
- brought into force;
- currently operative.

Never present a bill/proposal as if it were already law.

Where the consolidated Act/Rules and an amendment notification appear inconsistent, investigate and flag the discrepancy rather than guessing.

---

# 12. TASK 9 — SOURCE TAGGING SYSTEM

Introduce a consistent source-tagging system throughout the vault.

Recommended tags:

- `[OFFICIAL]`
- `[OFFICIAL-LAW]`
- `[KMF]`
- `[SHIMUL]`
- `[GOVT-KA]`
- `[GOI]`
- `[NDDB]`
- `[STATISTICS]`
- `[CURRENT]`
- `[YOUTUBE]`
- `[SECONDARY]`
- `[PYQ]`
- `[PYQ-ADJACENT]`
- `[EXAM-FACT]`
- `[CONCEPT]`
- `[IMPORTANT]`
- `[UNVERIFIED]`
- `[CONFLICT]`

Use only tags that actually add value.

Every important factual addition should have a traceable source.

---

# 13. TASK 10 — CONFIDENCE & EVIDENCE CONTROL

Do not use "100% fact checked" as a substitute for evidence.

Instead, apply this rule:

### Core Study Material
A fact should enter the core material only when there is reasonable source support.

### High-confidence
Supported directly by an authoritative/current official source.

### Medium-confidence
Supported by a credible source but primary confirmation is unavailable or incomplete.

### Unverified
Potentially useful but cannot currently be established reliably.

### Conflicting
Two credible sources disagree.

For medium-confidence, unverified or conflicting material:

**label it explicitly.**

Never silently convert uncertainty into fact.

---

# 14. TASK 11 — UPDATE EXISTING PYQ & QUIZ MATERIAL

After updating the subject files:

### PYQ Bank
Review the existing PYQ material for:

- outdated answers;
- incorrect explanations;
- incorrect attribution;
- duplicated questions;
- weak sourcing.

Preserve verified PYQs.

Do not fabricate official PYQs.

If the new research reveals additional genuinely sourced questions, add them with the existing provenance rules.

### Quiz Bank
Regenerate/expand the quiz bank from the **updated subject files**, not directly from raw web research.

Add questions on:

- new facts;
- new legal provisions;
- new current affairs;
- new statistics;
- KMF/SHIMUL structure;
- dairy terminology;
- comparative tables;
- recent changes.

Maintain clear labels distinguishing:

- PYQ-derived;
- PYQ-adjacent;
- newly generated.

---

# 15. TASK 12 — FILE STRUCTURE EXPANSION

Preserve the existing vault structure.

You may add files where they genuinely improve organization.

For example, consider adding:

```text
references/
    dairy-data-and-statistics.md
    kmf-shimul-current-affairs.md
    karnataka-cooperative-law-reference.md
    dairy-gk-quick-reference.md
    diagrams-and-processes.md
```

Only create separate files when the additional material is substantial enough to justify separation.

Do not fragment the vault unnecessarily.

Update `00-index.md` so all new files remain discoverable.

---

# 16. TASK 13 — READABILITY & SIMPLICITY GUARDRAILS

Despite the increased scope:

**Do not make the vault harder to study.**

Maintain:

- short paragraphs;
- clear headings;
- logical hierarchy;
- simple language;
- useful tables;
- visual summaries;
- concise exam facts;
- explanations immediately after technical concepts.

Avoid:

- huge walls of prose;
- unnecessary academic detail;
- repetitive explanations;
- decorative diagrams;
- overly wide tables;
- unexplained jargon;
- facts with no apparent exam/useful context.

When a topic becomes detailed:

**Layer it.**

Example:

### 30-second version
5–8 essential facts.

### 2-minute version
Concept + structure + flowchart.

### 10-minute version
Detailed explanation + statistics + law + current context.

This layered approach should be used particularly for KMF/SHIMUL and cooperative-law topics.

---

# 17. TASK 14 — EXAM-ORIENTED PRIORITIZATION

Do not treat every discovered fact equally.

Mark especially important material with `[IMPORTANT]`.

Prioritize according to:

1. Confirmed SHIMUL syllabus relevance.
2. Evidence from SHIMUL PYQs.
3. Evidence from adjacent Karnataka Milk Union/cooperative exams.
4. Importance of the concept within the organization/law.
5. Recent current-affairs significance.
6. Likelihood of direct factual questioning.

Where possible distinguish:

**Must Know → Should Know → Useful Enrichment**

Do not remove enrichment merely because it is lower priority; simply make its priority visible.

---

# 18. TASK 15 — OVERLAP MAPPING

Continue the existing overlap philosophy.

Where a topic is useful beyond SHIMUL, annotate:

> 🔁 **Overlap:** Relevant to other Karnataka Milk Union / KMF / Cooperative Society examinations.

Also identify particularly reusable topics for:

- other District Milk Unions;
- KMF-related recruitment;
- Karnataka cooperative examinations;
- general Karnataka government competitive examinations.

Do not conduct unnecessary full separate research on every adjacent exam.

---

# 19. TASK 16 — CHANGE LOG

Create or update:

`change-log.md`

Record substantial updates such as:

- new source discovered;
- outdated fact corrected;
- major diagram fixed;
- new topic added;
- legal provision updated;
- current-affairs update added;
- statistic updated;
- conflicting sources identified/resolved.

Keep this concise.

This allows a future agent to understand what changed during subsequent maintenance passes.

---

# 20. FINAL QUALITY-CONTROL PASS

Before finishing, perform a final audit.

Check:

### Content
- Are major dairy/KMF/SHIMUL knowledge gaps addressed?
- Is cooperative-law coverage meaningfully deeper?
- Is current-affairs coverage current?
- Are useful statistics included where reliable?
- Are important Karnataka-specific facts covered?

### Visuals
- Does every Mermaid diagram use valid syntax?
- Are tables valid Markdown and reasonably readable?
- Are there enough flowcharts for genuinely complex processes?

### Sources
- Are important facts traceable?
- Are official sources preferred where available?
- Are YouTube sources being used mainly for explanation?
- Are weak/conflicting sources clearly labelled?

### Consistency
- Are tags used consistently?
- Are terms such as KMF, SHIMUL, DCS, Union, Federation etc. used consistently?
- Are historical and current facts clearly separated?

### Exam utility
- Can I revise a topic quickly?
- Can I understand it conceptually?
- Can a future LLM generate quizzes from it?
- Can I distinguish high-priority exam facts from enrichment?

---

# 21. FINAL REPORT TO ME

After completing the vault upgrade, provide a concise completion report containing:

### A. What was added
Major new subject areas, data, current affairs, legal content, tables and diagrams.

### B. What was fixed
Mermaid, tables, incorrect/outdated facts, weak sourcing, etc.

### C. What was verified
Important facts that now have strong official/current source support.

### D. What remains uncertain
Any unresolved conflicts, unavailable official data, or claims that could not be fully verified.

### E. Highest-priority new material
The most important additions I should study first.

### F. Files changed/created
A concise list of modified and newly created vault files.

Do not claim that everything is "100% verified" merely because a search was performed.

The objective is:

**maximum useful coverage + strong evidence + current information + simple presentation + exam relevance.**

---

# 22. WORKING PRINCIPLE

Throughout this task, think of the existing vault as a **living exam knowledge base**, not a static document.

The correct workflow is:

**AUDIT → IDENTIFY GAPS → VERIFY EXISTING FACTS → PRIORITIZE → ADD → EXPLAIN → VISUALIZE → SOURCE → QUALITY CHECK → UPDATE INDEX → UPDATE QUIZ BANK**

Preserve valuable existing work.

Expand intelligently.

Correct only when evidence supports the correction.

Prefer official/current sources.

Use YouTube to improve understanding, not to bypass primary-source verification.

Keep everything simple enough that I can actually study it under exam pressure.