# Agent Prompt: SHIMUL Exam Deep-Research & Study Vault Builder

---

## 0. Context & Urgency

I am preparing for the **SHIMUL (Shimoga District Co-operative Milk Producers' Societies Union) recruitment exam**, which is happening **within the next 7-10 days**. This is time-critical — prioritize breadth-with-depth on high-yield topics over exhaustive coverage of low-yield ones. Work fast, cite sources, and don't get stuck perfecting one subject while others remain untouched.

I also want you to **flag, wherever relevant, where SHIMUL's syllabus overlaps with other Milk Union / Karnataka Co-operative Societies exams** (e.g. KMF, other District Milk Unions, Karnataka State Co-operative exams). Don't do full separate research on those exams right now — just annotate overlaps inside the SHIMUL material so the vault is reusable later with minimal rework.

My end goal: a **markdown vault** that (a) fully documents the exam, (b) teaches me the subject matter in a learnable, memorizable way, and (c) can be used by any LLM agent afterward to actively quiz/teach me (spaced repetition style) using only the vault content as ground truth.

---

## 1. Research Objectives

Research and compile the following, using web search and YouTube search (use the `ingest-youtube` skill to extract transcripts/notes from any YouTube video you cite as a source — don't just link videos, extract their teaching content):

1. **Official syllabus** for the SHIMUL exam (post-wise if the syllabus differs by post — e.g. Junior Assistant, Clerk, Technical posts, etc.). If an official notification/PDF exists, find and extract it directly.
2. **Exam pattern**: number of sections, number of questions per section, marks distribution, negative marking (yes/no and ratio), duration, qualifying cutoffs if known, language of paper (Kannada/English/both).
3. **Previous Year Question papers (PYQs)** — as many years as you can find, for SHIMUL specifically, and secondarily for other Karnataka Milk Union / Co-operative exams if SHIMUL-specific PYQs are scarce (label these clearly as "adjacent exam, not confirmed identical pattern").
4. **Subject-wise preparation material**, specifically for these sections (confirm exact section names/weightage from the syllabus first, then research each):
   - **Dairy/Milk Union functioning & KMF (Karnataka Milk Federation) structure** — organizational hierarchy, functions of District Milk Unions vs. KMF vs. village-level Dairy Cooperative Societies (DCS), procurement/processing/marketing chain, relevant schemes (e.g. Ksheera Bhagya, farmer payment systems), history of the Anand Pattern / Amul model / White Revolution / Operation Flood as it applies to Karnataka's cooperative dairy structure.
   - **Co-operative societies (general + Karnataka-specific)** — Co-operative Societies Act (Karnataka Co-operative Societies Act, 1959, and/or the Multi-State Co-operative Societies Act if relevant), principles of cooperation, structure/governance of a cooperative society (board, general body, office bearers), types of cooperative societies, relevant amendments or recent changes.
   - **General Knowledge (GK)** — prioritize: current affairs (last 6-12 months, national + Karnataka-specific), Karnataka state GK (geography, history, government schemes, districts, culture), static GK commonly asked in Karnataka govt/co-op exams (national symbols, awards, sports, books & authors, important days).
   - **Indian Constitution** — Preamble, fundamental rights & duties, DPSP, structure of government (Union & State), Panchayati Raj (73rd Amendment — especially relevant given cooperative/rural context), important articles commonly tested in these exams, amendments frequently asked about.
5. For each subject, identify **what's actually asked** (from PYQs/pattern) vs. what's theoretically in scope — weight your content accordingly.

---

## 2. Research Method

- Use web search broadly first (official SHIMUL/KMF sites, Karnataka govt cooperative dept sites, exam-prep portals like exampur, testbook, adda247, Karnataka-specific coaching sites, Kannada-language sources too since local coaching content may be more accurate).
- Use YouTube search for Kannada/English exam-prep channels covering SHIMUL, KMF, or Karnataka co-op exams — then use `ingest-youtube` to pull actual content (explanations, question walkthroughs) rather than just noting the video exists.
- Cross-verify facts (syllabus, pattern, cutoffs) across at least 2 sources where possible; flag anything you couldn't verify or found conflicting info about, rather than presenting a guess as fact.
- Do not fabricate PYQ questions — only include ones you actually sourced. If PYQs are scarce, say so explicitly and substitute with "PYQ-style practice questions" clearly labeled as agent-generated, not official.

---

## 3. Output: Vault Structure

Create/update the markdown vault at: `VAULT_PATH = D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\Shimul`

Use this file structure:

```
VAULT_PATH/
├── 00-index.md                     # Overview, links to everything below, exam countdown, priority order
├── 01-exam-overview.md             # Syllabus (post-wise if applicable) + exam pattern + sources
├── 02-study-plan.md                # Day-by-day plan for the remaining time before the exam
├── subjects/
│   ├── dairy-union-kmf.md
│   ├── cooperative-societies.md
│   ├── general-knowledge.md
│   └── indian-constitution.md
├── pyq-bank.md                     # All sourced previous year questions, tagged by subject & year
└── quiz-bank.md                    # Flashcard/quiz-ready Q&A pairs generated FROM the subject files
```

### 00-index.md must include
- One-paragraph exam overview
- Days remaining until exam (compute from today's date) and a link to `02-study-plan.md`
- A priority-ranked list of subjects/topics based on (a) marks weightage and (b) how frequently they appear in PYQs
- Links to every other file

### 01-exam-overview.md must include
- Full syllabus, organized by section, with source links/citations
- Full exam pattern table (sections, question count, marks, negative marking, duration)
- Any eligibility/post-specific notes if relevant
- A "Confidence & Gaps" subsection noting anything unverified or conflicting between sources

### 02-study-plan.md must include
- A realistic day-by-day schedule for the time remaining, allocating more time to high-weightage/high-frequency topics
- Built-in revision + mock-test days near the end
- Should reference the quiz-bank and pyq-bank for practice sessions

### subjects/*.md — for EACH subject file, use this internal structure
1. **Section weightage & typical question style** (from the pattern/PYQ research)
2. **Core concepts**, organized hierarchically (headings → sub-bullets), written for genuine understanding, not just fact-dumps — include short explanations of *why*, not just *what*
3. **Key facts/lists to memorize** — call these out distinctly (tables, numbered lists) since these are what get tested directly
4. **Mnemonics or memory aids** where useful (especially for lists like Fundamental Rights, Union vs State list items, DCS→Union→KMF hierarchy, etc.)
5. **Overlap notes** — inline callouts like `> 🔁 Overlap: also tested in [other Milk Union/Co-op exam] — same core concept` wherever you notice this
6. **Sources** — list every source used, so I can go deeper if needed

### pyq-bank.md
- Group by subject, then by year (or "year unknown" if undated)
- Each entry: question, options (if MCQ), correct answer, brief explanation, source
- Clearly separate a "Verified official PYQs" section from an "Adjacent-exam / unconfirmed pattern" section

### quiz-bank.md
- Generate this FROM the subject files (after they're written), not from raw research
- Format as simple Q&A pairs plus a handful of MCQ-style questions with distractors, ready for any agent to use to quiz me interactively later
- Tag each question with subject + difficulty (easy/medium/hard) + whether it's PYQ-derived or newly generated
- Include a short instruction block at the top of this file: *"Agent instructions: use this file to quiz the user one question at a time, track right/wrong, and re-surface missed questions more often (spaced repetition)."* — so any future agent session can pick this up and start teaching/quizzing me directly.

---

## 4. Quality Bar

- Prefer accuracy over completeness — a smaller, verified vault beats a large, unverifiable one, especially with 7-10 days on the clock.
- Every non-obvious factual claim should be traceable to a source (link or citation note).
- Write for genuine comprehension — I want to *understand* the co-op/dairy structure and constitutional concepts, not just memorize disconnected facts, because that retention is what will actually get me through both objective questions and any interview stage.
- Keep language simple and exam-focused; avoid padding.
- At the end, give me a short summary of: what you found solid confidence in, what's shaky/unverified, and what I should prioritize studying first given the 2-week window.

---

## 5. After Building the Vault

Once the vault is built, be ready (in this or a future session) to:
- Actively quiz me from `quiz-bank.md` and `pyq-bank.md`
- Explain any concept from the subject files in more depth on request
- Update the vault as I find additional official notifications or papers
