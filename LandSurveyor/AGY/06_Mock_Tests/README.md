# KEA Land Surveyor 2026 — Offline Timed HTML Mock Tests

## Architecture & How They Were Built
These 3 mock tests are self-contained, standalone single-file HTML applications engineered to run 100% offline in any modern web browser (Edge, Chrome, Firefox, Safari) without requiring an internet connection or external libraries.

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
| **`Mock_Test_1_Paper_1_General_Knowledge.html`** | Paper-I: General Knowledge | 100% curated from KEA 2023/2024 Land Surveyor & KPSC PYQs + 2026 Karnataka Budget & State Schemes. |
| **`Mock_Test_2_Paper_2_Specific_Surveying.html`** | Paper-II: Specific Technical Surveying | Authentic surveying numericals, chain/compass/levelling checks, theodolite formulas, GPS/GIS, and Bhoomi/Mojini land records. |
| **`Mock_Test_3_Full_Technical_Marathon.html`** | High-Yield Paper I & II Marathon Drill | Balanced simulation covering highest-weightage topics across both papers for rapid pre-exam confidence. |

---

## How to Launch
Double-click on any `.html` file inside this folder, or right-click and select **"Open with Google Chrome / Microsoft Edge"**. No local web server or installation required.
