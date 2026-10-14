# Diagnostic Audit of Round 2 CBT Exam Simulator Engine
**Audit Date**: 2026-10-13 (Tuesday, 13 October 2026)
**Artifact Evaluated**: `06_Mock_Tests/_src/cbt_engine_template.html` & 22 compiled CBT HTML files in `06_Mock_Tests/`
**Runtime Diagnostic Harness**: Node.js v26.7.0 (`_run/tools/test_diagnostics.js`)
**Diagnostic Status**: **REPRODUCED WITH CONCRETE RUNTIME EVIDENCE**

---

## 1. Summary of Identified Defects

The Round 2 CBT engine provided a responsive visual interface, but contained foundational logical and architectural defects in time management, state indexing, score calculations, and sectional isolation:

| Category | Defect Description | Severity | Impact on Candidate |
| :--- | :--- | :--- | :--- |
| **Timer** | Decrementing `timeRemaining` counter drifts over long sessions and resets on browser reload during dwell times. | **Critical** | Time distortion; candidate can reset timer by refreshing page. |
| **Evaluation** | State keyed by array index (`currentQuestionIndex`) instead of stable question IDs (`q.id`). | **Critical** | Corrupts evaluation if questions are reordered, filtered, or viewed section-wise. |
| **Scoring** | Clamped `Math.max(0, netScore)` truncates negative competitive marks to zero; lacks section/topic breakdowns. | **High** | Inaccurate KPSC KAS performance analytics; negative penalty hidden. |
| **Navigation** | All 22 tests lack `sections` metadata, forcing a single unsegmented 100-question palette with no section tabs. | **High** | Non-compliant with official KPSC Prelims Paper 1 & Paper 2 sectional architecture. |
| **Workflow** | Missing pre-exam instructions modal and test-mode selector (Exam Mode vs 2-minute Quick Check). | **Medium** | Test starts immediately upon page load without candidate confirmation. |

---

## 2. Detailed Technical Defects & Runtime Evidence

### 2.1 Timer Drift, Lack of Persistence & Reset Vulnerability
- **Location**: `06_Mock_Tests/_src/cbt_engine_template.html`, Lines 626, 855-870, 873-881.
- **Root Cause**:
  1. **Clock Drift**: Line 856 uses `setInterval(() => { timeRemaining--; ... }, 1000)`. In modern browsers, `setInterval` ticks drift significantly over 120 minutes due to CPU power-saving, task throttling, and background tab de-prioritization.
  2. **Reload Reset Vulnerability**: `saveState()` is invoked strictly inside `loadQuestion(idx)` (Line 760). If a candidate dwells on a question for 15 minutes without clicking another question or button, and then reloads the browser, `localStorage` still holds the time saved when the question was initially loaded. The candidate gains back all elapsed dwell time.
  3. **No Absolute Timestamp**: The engine does not compute `targetEndTime = Date.now() + durationMs`.
- **Node.js Harness Reproduction**:
  ```javascript
  // Simulated candidate on Q0 with 7200s (120m)
  // Dwells for 900s (15m), then reloads page
  reloaded_time = localStorage.getItem('timeRemaining'); // 7200s
  // Result: Candidate regains 15 minutes!
  ```
- **Remediation for Round 3**:
  - Compute `examEndTime = Date.now() + (durationMinutes * 60 * 1000)` upon candidate confirmation.
  - On every interval tick, compute `remainingSeconds = Math.max(0, Math.round((examEndTime - Date.now()) / 1000))`.
  - Persist `examEndTime` in `localStorage`. On page reload, the remaining time is mathematically derived from the real wall clock, preventing drift and reload cheating.
  - Implement instant auto-submit when `remainingSeconds === 0`.
  - Provide instructions screen with dual mode options: **Exam Mode (Official Duration)** and **Quick Check (2 Minutes)**.

---

### 2.2 Answer Keying by Array Position vs Question ID
- **Location**: `06_Mock_Tests/_src/cbt_engine_template.html`, Lines 623, 786, 801, 816, 924.
- **Root Cause**:
  1. User responses are stored as `userAnswers[currentQuestionIndex] = { selectedOption: sel }`.
  2. In `submitExam()` (Line 924), evaluation iterates:
     `EXAM_DATA.questions.forEach((q, idx) => { const userSel = userAnswers[idx]?.selectedOption; ... })`.
  3. This couples answers strictly to array index `idx` (`0..N-1`). If a candidate filters questions by section, or if questions are sorted/shuffled, the index points to the wrong question, causing complete answer key corruption.
- **Node.js Harness Reproduction**:
  ```javascript
  // Q0 has ID P1-Q001 (Ans: A), Q1 has ID P1-Q002 (Ans: B)
  userAnswers[0] = { selectedOption: 'A' }; // User answered P1-Q001
  // If Section 2 shows Q1 as first item (index 0):
  userAnswers[0] evaluated against P1-Q002 -> Answer evaluated as WRONG!
  ```
- **Remediation for Round 3**:
  - Store answers keyed strictly by question ID: `userAnswers[q.id] = { selectedOptionId: optId, timestamp: Date.now() }`.
  - In scoring functions, lookup `userAnswers[q.id]`, making evaluation 100% immune to index shifts, section filtering, or reordering.

---

### 2.3 Evaluation & Negative Scoring Clamping Defect
- **Location**: `06_Mock_Tests/_src/cbt_engine_template.html`, Lines 936-939.
- **Root Cause**:
  - Line 938: `const netScore = Math.max(0, positiveMarks - negativeMarks);`.
  - `Math.max(0, ...)` artificially clamps the score to zero. In competitive exams under KPSC KAS rules, if a candidate has 10 correct (+20.0) and 60 incorrect (-30.0), the true net score is `-10.0`. Truncating it to `0.0` hides actual penalty performance.
  - Missing Sectional & Thematic Performance Breakdown: The submit screen only displays global net marks. It does not calculate per-section accuracy (Current Events vs Humanities vs Science vs Mental Ability).
- **Node.js Harness Reproduction**:
  ```javascript
  let positiveMarks = 10 * 2.0; // 20.0
  let negativeMarks = 60 * 0.50; // 30.0
  let netScore = Math.max(0, positiveMarks - negativeMarks); // 0.0 (Suppresses -10.0 penalty)
  ```
- **Remediation for Round 3**:
  - Report exact raw score without arbitrary truncation at zero.
  - Build a pure scoring function `scoreExam(answers, questions, markingScheme)` returning:
    - `totalMarks`, `positiveMarks`, `negativePenalty`, `netScore`, `accuracyPercentage`
    - `sectionBreakdown`: per section `{ name, total, attempted, correct, incorrect, netMarks }`
    - `topicBreakdown`: per subject `{ subject, total, attempted, correct, incorrect, netMarks }`.

---

### 2.4 Lack of Sectional Architecture in Compiled Tests
- **Location**: All 22 files in `06_Mock_Tests/*.html`.
- **Root Cause**:
  - Inspection of `EXAM_DATA` in all 22 HTML tests revealed `sections: []`.
  - Because `sections` was empty, `renderSectionTabs()` fell back to a single generic "General Studies" tab spanning all 100 questions.
  - Official KPSC Prelims structure dictates:
    - **Paper 1**: Section 1 (Current Events, 40 Qs), Section 2 (Humanities, 60 Qs).
    - **Paper 2**: Section 1 (State Importance, 40 Qs), Section 2 (Science & Tech, 30 Qs), Section 3 (General Mental Ability, 30 Qs).
  - The palette had no section tabs, no section-specific question counts, and no ability to view section progress separately.
- **Remediation for Round 3**:
  - Include rich `sections` schema in `EXAM_DATA`:
    ```json
    "sections": [
      { "id": "SEC-1", "name": "Section 1: Current Events", "start_idx": 0, "end_idx": 39, "q_count": 40 },
      { "id": "SEC-2", "name": "Section 2: Humanities", "start_idx": 40, "end_idx": 99, "q_count": 60 }
    ]
    ```
  - Section tabs allow switching palette views to the current section or viewing all questions.
  - Section header displays live counts: Answered, Not Answered, Marked for Review, Not Visited for that specific section.

---

### 2.5 Option ID and Statement Truth Integrity
- **Location**: `06_Mock_Tests/_src/cbt_engine_template.html`, Lines 727-757.
- **Root Cause**:
  - Options lacked explicit unique IDs (`opt.id`), relying solely on display label (`opt.label = 'A'`).
  - If options were reordered, matching against `'A'` would fail.
- **Remediation for Round 3**:
  - Ensure every option has a stable `id` (e.g. `opt_a`, `opt_b`, `opt_c`, `opt_d`).
  - Correct answer stores the option ID.
  - Script validates that statement truth values mathematically produce the correct option.

---

## 3. Conclusion & Mandate for Engine Redesign

All 5 defects have been formally identified and verified with runtime code traces. Workstream A will replace `cbt_engine_template.html` and compile the self-contained, standalone CBT suite according to the rigorous correctness rules outlined above.
