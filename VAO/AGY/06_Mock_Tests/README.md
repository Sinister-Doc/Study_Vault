# KEA VAO (Village Administrative Officer) 2026 — Offline Timed HTML Mock Tests

## Architecture & How They Were Built
These 3 mock tests are self-contained, standalone single-file HTML applications engineered to run 100% offline in any modern web browser without requiring an internet connection, external CSS frameworks, or JavaScript CDNs.

### Core Features Implemented:
1. **Interactive Countdown Timer:** Calibrated to the official KEA examination duration (120 minutes) with real-time display and automated auto-submit when the countdown expires. Visual alert triggers in the final 5 minutes.
2. **Dynamic Question Navigation Palette:**
   - Real-time color-coded state tracking (Not Attempted, Answered in Emerald Green, Marked for Review in Amber, and Answered & Marked for Review in Violet).
   - Instant jump navigation to any question.
3. **Official Marking Engine:**
   - **+1.0 Mark** for correct answers.
   - **-0.25 Mark (1/4th penalty)** for incorrect answers.
   - 0.00 for unattempted questions.
4. **Instant Scorecard & Deep Analytical Review:**
   - Net Marks, Accuracy Percentage, Total Correct vs Wrong breakdown.
   - Subject-wise performance diagnostic table.
   - Comprehensive question-by-question review with official explanations and derivation steps.

---

## Test Directory & Sourcing

| Test File | Exam Paper Simulation | Question Bank Composition & Sourcing |
| :--- | :--- | :--- |
| **`Mock_Test_1_Paper_1_General_Knowledge_and_Rural_Admin.html`** | Paper-I: GK, Heritage & Rural Governance | Curated from KEA/KPSC Village Accountant PYQs + Karnataka History, Geography, Constitution, and 5 Guarantee schemes. |
| **`Mock_Test_2_Paper_2_Language_and_Computer_Knowledge.html`** | Paper-II: Kannada, English & Computer | High-yield Kannada grammar (Sandhi, Samasa, Tatsama), English rules (Voice, Conditionals), and MS Office/Networking. |
| **`Mock_Test_3_Full_Length_High_Yield_Simulation.html`** | Comprehensive Full-Length Simulation | Balanced marathon drill combining General Knowledge, Languages, Rural Administration, and Computer Knowledge. |

---

## How to Launch
Double-click on any `.html` file inside this folder, or right-click and select **"Open with Google Chrome / Microsoft Edge"**. No local web server or installation required.
