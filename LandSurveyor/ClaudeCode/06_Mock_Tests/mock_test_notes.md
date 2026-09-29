# Mock Test Notes — KEA Karnataka Land Surveyor 2026

## How These Were Built

**Compilation date:** 2026-09-29
**Compiler:** Claude Code agent (Mock Test Engineer role)
**Working directory:** `D:\...\LandSurveyor\ClaudeCode\06_Mock_Tests\`

> **Verified pattern:** Exam 04.10.2026. Paper 1 (GK) 10:30–12:30; Paper 2 (specific) 14:30–16:30. Each paper: 100 Q / 100 marks / 120 min, 4 options + a 5th "not answered" circle on the OMR, 0.25 deducted per wrong answer **and** 0.25 if no circle is shaded, 10 extra minutes after the bell to shade the 5th circle, minimum 35% per paper to remain eligible. Read from the official KEA notification (`../07_Agent_Log/_pdf_pages/LS_p05.png`).

### 1. Source Material

All three mock tests (mock1.html, mock2.html, mock3.html) were built from:

| Source File | Path | Used For |
|---|---|---|
| Syllabus & Pattern | `02_Syllabus_and_Pattern.md` | Weightage split: Surveying 45, GK 25, Mental Ability 25 |
| PYQ Analysis | `05_Resources/pyq_analysis.md` | 60 expected questions (Q1-Q60) — all labeled "expected" |
| Surveying Basics | `03_Notes/01_Surveying_Basics.md` | Units, chains, RF, errors, field book (~8 Qs) |
| Chain & Compass | `03_Notes/02_Chain_Compass_Survey.md` | Bearings, traverse, corrections, local attraction (~14 Qs) |
| Levelling | `03_Notes/03_Levelling_Contouring.md` | HI/Rise-Fall, curvature, contours (~8 Qs) |
| Theodolite/TS/GPS | `03_Notes/04_Theodolite_Total_Station.md` | Adjustments, GPS, traverse (~7 Qs) |
| Karnataka Revenue | `03_Notes/05_Karnataka_Land_Revenue.md` | RTC, forms, hierarchy, Act year (~7 Qs) |
| History | `03_Notes/06_History.md` | Dynasties, freedom movement, land systems (~8 Qs) |
| Geography | `03_Notes/07_Geography.md` | Rivers, districts, soil, climate, dams (~8 Qs) |
| Polity | `03_Notes/08_Polity.md` | Constitution, FR/DPSP, Panchayati Raj (~8 Qs) |
| Economy/Science | `03_Notes/09_Economy_Science.md` | GDP, inflation, science basics (~8 Qs) |
| Mental Ability | `03_Notes/10_Mental_Ability.md` | Series, coding, blood relations, directions (~12 Qs) |
| Current Affairs 2026 | `04_Current_Affairs_GK/Current_Affairs_2026.md` | Appointments, schemes, ISRO, sports (~8 Qs) |

### 2. Question Distribution Strategy

The **verified official** exam pattern (see `../02_Syllabus_and_Pattern.md`) is 100 MCQs, 100 marks, 120 minutes, 0.25 negative per wrong answer, per paper. Each mock models **one paper**:

- Paper 1 (GK) → 100 questions across the 8 official GK sub-areas
- Paper 2 (specific) → 100 questions on the subject paper

- Surveying & Land Measurement: 45 questions
- General Knowledge: 25 questions  
  - (Of which: History 8, Geography 8, Polity 8, Economy/Science 11)
- Mental Ability: 25 questions
- Current Affairs: 5 questions (included within GK bucket for test balance)

> **Design decision:** The notification's official sub-area list does NOT name Mental Ability. The 25-question Mental Ability block is a **derived/optional** inclusion covering aptitude commonly seen in KEA GK papers; treat it as bonus practice. The 45-question Surveying block models the Paper-2 specific paper.

### 3. Question Labels

- **"expected"** — derived from standard surveying textbooks and static GK; appears throughout mock1.html and mock2.html
- **"PYQ-style"** — 3-5 per test from topics that are standard surveying/KEA knowledge (chain corrections, FB/BB, GPS, Karnataka facts), labeled at source
- **"[verify]"** — volatile facts (appointments, dates, current events) that should be re-checked closer to exam date

### 4. HTML Technical Features

Each HTML file is a **single self-contained file** (no external dependencies):

- **Inline CSS** — all styling embedded in `<style>` tags
- **Inline JavaScript** — all logic embedded in `<script>` tags
- **Pure vanilla JS** — no frameworks, no external libraries
- **Offline capable** — all assets inline (SVG icons, data URLs)
- **Auto-save** — answers stored in `localStorage` so progress survives page reloads
- **No server required** — open directly via `file://` in any browser

### 5. Features Implemented

| Feature | Status | Notes |
|---|---|---|
| Welcome screen with exam specs | ✅ | Count, marks, duration, negative marking |
| Countdown timer (120:00 → 00:00) | ✅ | Auto-submit at 00:00:00 |
| Question palette (color-coded) | ✅ | 4 colors: not-visited, unanswered, attempted, marked |
| Mark-for-review checkbox | ✅ | Per question |
| Section navigation | ✅ | Surveying / GK / Mental Ability tabs |
| Progress bar | ✅ | Per-section + overall |
| Submit button | ✅ | Manual + auto on timeout |
| Scored result screen | ✅ | Per-subject breakdown |
| Answer review screen | ✅ | With explanations |
| Negative marking | ✅ | 0.25 per wrong answer |
| localStorage persistence | ✅ | Saves answers, marks, current question |

> [!warning] Engine vs official OMR — one deliberate difference
> The official notification deducts **0.25 for a wrong answer AND 0.25 if no circle is shaded at all** (the 5th "not answered" circle exists precisely so a deliberate blank is not penalised as a wrong answer). This offline mock scores unattempted questions as **0** to avoid training blind guessing — but on the real OMR you **must shade the 5th circle for any question you skip**, or you lose 0.25 anyway.

### 6. Mock Test Composition

**mock1.html** — 100 questions
- 45 Surveying & Land Measurement
- 25 General Knowledge (History 8, Geography 7, Polity 7, Economy/Science 8, Current Affairs 5)
- 25 Mental Ability

**mock2.html** — 100 questions
- 45 Surveying & Land Measurement
- 25 General Knowledge (History 7, Geography 8, Polity 7, Economy/Science 8, Current Affairs 5)
- 25 Mental Ability

**mock3.html** — 100 questions
- 45 Surveying & Land Measurement
- 25 General Knowledge (History 8, Geography 6, Polity 7, Economy/Science 9, Current Affairs 5)
- 25 Mental Ability

### 7. Source Attribution Summary

> All 180 unique questions are derived from the syllabus notes listed above. No questions were fabricated from unverified external sources. Where web search for 2026 facts failed, the pyq_analysis.md file honestly recorded "[verify]" flags, which are carried into these mocks with the same flagging convention.

### 8. How to Use

1. Open `mock1.html` (or mock2/mock3) in any modern browser (Chrome, Edge, Firefox, Safari)
2. No internet connection needed
3. Click "Start Test" — timer begins counting down from 120:00
4. Use section tabs to navigate between Surveying, GK, and Mental Ability
5. Mark questions for review using the checkbox
6. Submit manually or let the timer auto-submit
7. Review your score and per-subject breakdown
8. Click "Review Answers" to see each question with explanation

### 9. Key Fact Verification Needed

These facts are flagged `[verify]` in the source and may change before the actual exam:

- RBI Governor (Q56): Sanjay Malhotra (Oct 2024) — need to verify incumbency
- G20 presidency 2026 (Q71): US — need to verify
- Karnataka Governor: Thawar Chand Gehlot — verify incumbency close to exam
- ISRO Chairman: V. Narayanan — need to verify
- Nobel Prize 2025 recipients
- Champions Trophy 2025 winner (India — confirmed)
- Karnataka district count (currently 31 — verify for any changes)

### 10. No PYQs Reproduce

The `pyq_analysis.md` file (Section 1) explicitly states no official PYQs were found or retrieved during web searches on 2026-09-29. All questions are **expected-practice material** built from the standard syllabus and textbook knowledge. No question should be cited as "asked in year X".

---

*Generated by: Claude Code agent*
*Model: Claude Sonnet 4.6*
*Date: 2026-09-29*
