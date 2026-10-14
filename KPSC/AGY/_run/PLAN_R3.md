# KPSC KAS Study Vault: Round 3 Master Upgrade Plan & Live Checklist
**Exam Cycle**: KPSC Gazetted Probationers (KAS) 2026-27 (Group A & Group B Services)
**As-Of Reference Date**: Tuesday, 13 October 2026 (2026-10-13)
**Vault Root**: `D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\KPSC\AGY\`

---

## 1. Exam Notification Blueprint & Architecture

The official KPSC Gazetted Probationers Preliminary Examination pattern is locked from the notification as follows:

### 1.1 Prelims Paper 1 (Code: P1)
- **Total Duration**: 2 Hours (120 Minutes) | **Exam Mode**: 120m | **Quick Check**: 2m
- **Total Questions**: 100 Multiple-Choice Questions | **Total Marks**: 200 Marks
- **Marking Scheme**: +2.00 marks per correct answer; -0.50 marks (one-fourth / 0.25 penalty) per incorrect answer
- **Sectional Architecture**:
  - **Section 1**: Current Events of National and International Importance (40 Questions, 80 Marks)
  - **Section 2**: Humanities — History of India (with special emphasis on Karnataka), World and Indian Geography, Indian Polity, and Indian Economy (60 Questions, 120 Marks)

### 1.2 Prelims Paper 2 (Code: P2)
- **Total Duration**: 2 Hours (120 Minutes) | **Exam Mode**: 120m | **Quick Check**: 2m
- **Total Questions**: 100 Multiple-Choice Questions | **Total Marks**: 200 Marks
- **Marking Scheme**: +2.00 marks per correct answer; -0.50 marks (one-fourth / 0.25 penalty) per incorrect answer
- **Sectional Architecture**:
  - **Section 1**: Current Events of State Importance and State Government Schemes/Policies (40 Questions, 80 Marks)
  - **Section 2**: General Science & Technology, Environment & Ecology (30 Questions, 60 Marks)
  - **Section 3**: General Mental Ability (Comprehension, Logical Reasoning, Decision Making, Basic Numeracy, Data Interpretation) (30 Questions, 60 Marks)

### 1.3 Subject Sectional Mocks
- **Total Duration**: 60 Minutes | **Total Questions**: 50 Questions | **Total Marks**: 100 Marks
- **Marking Scheme**: +2.00 marks per correct answer; -0.50 marks per incorrect answer
- **Subjects**: Karnataka History, Karnataka Geography, Indian Polity, Indian Economy, Science & Environment, General Mental Ability.

### 1.4 Monthly Current Affairs Mocks
- **Total Duration**: 30 Minutes | **Total Questions**: 25 Questions | **Total Marks**: 50 Marks
- **Marking Scheme**: +2.00 marks per correct answer; -0.50 marks per incorrect answer
- **Coverage**: February 2026 through October 2026 (9 monthly tests).

### 1.5 Authentic PYQ Master Mock
- **Total Duration**: 120 Minutes | **Total Questions**: 100 Questions | **Total Marks**: 200 Marks
- **Marking Scheme**: +2.00 marks per correct answer; -0.50 marks per incorrect answer
- **Coverage**: Curated KPSC KAS 2014, 2017, and 2020 verified questions.

---

## 2. Question Bank Gap Analysis

| Examination Category | Target Tests | Questions / Test | Total Questions Needed | Available in Master Bank | Shortfall / Gap |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Full Prelims Paper 1** | 3 Versions (Mock 1, 2, 3) | 100 Qs (40 Sec 1 + 60 Sec 2) | 300 Questions | 300 Questions | **0 (100% Covered)** |
| **Full Prelims Paper 2** | 3 Versions (Mock 1, 2, 3) | 100 Qs (40 Sec 1 + 30 Sec 2 + 30 Sec 3) | 300 Questions | 300 Questions | **0 (100% Covered)** |
| **Subject Sectional Drills** | 6 Subjects | 50 Questions | 300 Questions | 300 Questions | **0 (100% Covered)** |
| **Monthly CA Drills** | 9 Months (Feb-Oct 2026) | 25 Questions | 225 Questions | 225 Questions | **0 (100% Covered)** |
| **Authentic PYQ Master Mock** | 1 Master Test | 100 Questions | 100 Questions | 100 Questions | **0 (100% Covered)** |
| **TOTAL** | **22 Tests** | — | **1,225 Questions** | **1,225 Questions** | **0 (100% Covered)** |

*Conclusion*: Zero shortfall. All 1,225 questions are distinct, fully verified, and catalogued in `06_Mock_Tests/_src/bank.json`.

---

## 3. Pinned Packages & Runtime Dependencies
- **Node.js**: v26.7.0 (installed and available on system path for runtime test execution).
- **Python**: 3.13.5 (installed and available for scripting and `safe_ops` guards).
- Zero external npm packages required: The CBT engine and test harness use vanilla ECMAScript 2022+ and Node.js built-in `fs`, `path`, and `crypto` modules.

---

## 4. Live Execution Checklist

The checklist below tracks every task in real time. Items are checked with timestamps upon completion.

### Phase 1: Diagnostics, Safety, Bank & Planning
- [x] [2026-10-13 22:50] T1.1 Save entire user request verbatim to `_run/PROMPT_R3.md`.
- [x] [2026-10-13 22:51] T1.2 Update `safe_ops.py` with `safe_move`, protect `PROMPT_R3.md`, and pass self-tests.
- [x] [2026-10-13 22:52] T1.3 Capture parent directory before-snapshot (`_run/before_snapshot_r3.json`).
- [x] [2026-10-13 22:53] T1.4 Inventory existing mock tests and question allocations.
- [x] [2026-10-13 22:54] T1.5 Reproduce defects in Node.js harness and publish `_run/DIAG_R3.md`.
- [x] [2026-10-13 22:55] T1.6 Extract Master Question Bank to `06_Mock_Tests/_src/bank.json` (1,225 unique questions).
- [x] [2026-10-13 22:56] T1.7 Write master plan and live checklist (`_run/PLAN_R3.md`).

### Phase 2: Workstream A Execution — Robust CBT Simulator Engine
- [x] [2026-10-13 22:58] T2.1 Engineer the unified, zero-dependency CBT engine template (`06_Mock_Tests/_src/cbt_engine_template.html`).
  - Absolute timestamp wall-clock countdown (no drift, persists across reload, auto-submits at zero).
  - Pre-exam instructions modal with "Exam mode (real duration)" and "Quick check (2 minutes)" options.
  - State keyed strictly by `q.id` and option IDs (`opt.id`).
  - Section tabs inside same file with live 5-state counts and isolated palette navigation.
  - Pure scoring function returning exact raw scores (no 0 clamping) with section and topic breakdowns.
  - Review mode with per-statement truth values, pedagogical rationales, and vault links.
- [x] [2026-10-13 22:56] T2.2 Write and execute Node.js automated test suite (`_run/tools/test_cbt_engine.js`) validating pure scoring, timer, and state functions.

### Phase 3: Workstream B Execution — Complete Mock Set Compilation
- [x] [2026-10-13 22:59] T3.1 Create compiler script `06_Mock_Tests/_src/compile_mocks.py` to generate all 22 self-contained HTML mocks from `bank.json`.
  - 3 Full Prelims Paper 1 Mocks (100 Qs each with 40 Sec 1 + 60 Sec 2)
  - 3 Full Prelims Paper 2 Mocks (100 Qs each with 40 Sec 1 + 30 Sec 2 + 30 Sec 3)
  - 6 Subject Sectional Mocks (50 Qs each)
  - 9 Monthly CA Mocks (25 Qs each)
  - 1 Authentic PYQ Master Mock (100 Qs)
- [x] [2026-10-13 23:00] T3.2 Run automated blind solver and syntax validator on all 22 generated HTML files.
- [x] [2026-10-13 23:00] T3.3 Rebuild companion Markdown answer keys in `06_Mock_Tests/Markdown_Keys/` and master test index `06_Mock_Tests/README.md`.
- [x] [2026-10-13 23:00] T3.4 Parity check: Verify 100% of questions from `bank.json` are present in tests.

### Phase 4: Workstream C Execution — Reorganise History & Geography Notes
- [x] [2026-10-13 23:00] T4.1 Write mapping audit to `_run/NOTES_MAP_R3.md`.
- [x] [2026-10-13 23:01] T4.2 Create subject folder structures using `safe_mkdir`:
  - `03_Notes/01_Karnataka_History_and_Culture/01_Textbook_Notes/`
  - `03_Notes/01_Karnataka_History_and_Culture/Quick_Revision/`
  - `03_Notes/03_Geography_Karnataka_and_World/01_Textbook_Notes/`
  - `03_Notes/03_Geography_Karnataka_and_World/Quick_Revision/`
- [x] [2026-10-13 23:01] T4.3 Move textbook notes and rename quick revision notes using `safe_move` only.
- [x] [2026-10-13 23:01] T4.4 Build `Karnataka_History_Hub.md` and `Karnataka_Geography_Hub.md` linking both tiers topic by topic.
- [x] [2026-10-13 23:02] T4.5 Audit and update all internal wikilinks across the vault to eliminate broken references.
- [x] [2026-10-13 23:02] T4.6 Run `examkit lint` and `examkit traceability` confirming 0 broken links and 100% syllabus coverage.

### Phase 5: Verification, Snapshots & Final Handover
- [x] [2026-10-13 23:02] T5.1 Execute parent directory after-snapshot comparison (`_run/tools/verify_snapshots_r3.py --after`).
- [x] [2026-10-13 23:03] T5.2 Update `_run/OPEN_ITEMS.md` with technical resolutions.
- [x] [2026-10-13 23:04] T5.3 Generate Master Execution Report `_run/RUN_REPORT_R3.md`.
- [x] [2026-10-13 23:05] T5.4 Final user notification.
