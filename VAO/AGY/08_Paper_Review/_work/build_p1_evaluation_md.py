# -*- coding: utf-8 -*-
"""
Script to generate VAO/AGY/08_Paper_Review/Paper1_Evaluation.md
"""
import json, re

with open('VAO/AGY/08_Paper_Review/_work/p1_items_with_exps.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Calculate statistics
total_q = len(items)
attempted = sum(1 for it in items if it['marked'] != 5)
correct = sum(1 for it in items if it['status'] == 'CORRECT')
wrong = sum(1 for it in items if it['status'] == 'WRONG')
unatt = sum(1 for it in items if it['status'] == 'UNANSWERED')
marks_pos = correct * 1.0
marks_neg = wrong * 0.25
net_score = marks_pos - marks_neg
accuracy = (correct / attempted * 100) if attempted > 0 else 0

md = []
md.append("# KEA Village Administrative Officer (VAO) 2026 — Paper 1 (General Knowledge) Evaluation Report\n")

md.append("| Examination Parameter | Candidate / Paper Record |")
md.append("| :--- | :--- |")
md.append("| **Examination** | KEA Village Administrative Officer (VAO / ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ) Competitive Examination 2026 |")
md.append("| **Department** | Department of Revenue (ಕಂದಾಯ ಇಲಾಖೆ), Government of Karnataka |")
md.append("| **Paper Name** | Paper 1: General Knowledge (ಸಾಮಾನ್ಯ ಜ್ಞಾನ) (Morning Session) |")
md.append("| **Subject Code** | `NHKGA41026M` |")
md.append("| **Booklet Series** | **B1** |")
md.append("| **Total Questions** | 100 Multiple-Choice Questions |")
md.append("| **Maximum Marks** | 100.00 Marks |")
md.append("| **Marking Scheme** | +1.0 for Correct, -0.25 for Wrong / Multiple, 0.0 for Option (5) (Unattempted) |")
md.append("| **Evaluation Basis** | Official notifications, authoritative keys, domain analysis & verified calculations |\n")

md.append("## 1. Executive Performance Scorecard\n")
md.append("| Metric | Count | Marks Contributed |")
md.append("| :--- | :--- | :--- |")
md.append(f"| **Total Questions in Paper** | **{total_q}** | — |")
md.append(f"| **Attempted (Options 1–4)** | **{attempted}** | — |")
md.append(f"| **Correct Answers** | **{correct}** | **+{marks_pos:.2f}** |")
md.append(f"| **Incorrect Answers** | **{wrong}** | **-{marks_neg:.2f}** |")
md.append(f"| **Unanswered (Option 5 Marked)** | **{unatt}** | **0.00** (Safe, no penalty) |")
md.append(f"| **Blank / Unmarked Questions** | **0** | **0.00** (100% OMR compliance) |")
md.append(f"| **NET TOTAL SCORE** | **—** | **`{net_score:.2f} / 100.00`** |")
md.append(f"| **Accuracy on Attempted** | **{accuracy:.2f}%** | — |\n")

md.append("> [!NOTE] Scoring Compliance & Option (5) Regulation")
md.append("> Under official KEA regulations, Option (5) serves as the mandatory non-attempt declaration bubble to prevent post-examination tampering. Marking Option (5) carries **zero penalty (0.00 marks)**. Leaving any question entirely blank incurs a **-0.25 penalty**; the candidate had 0 blank questions, maintaining complete procedural compliance.\n")

md.append("> [!WARNING] Paper 1 Sensitivity Note: Question P1-Q024")
md.append("> In question `P1-Q024`, the candidate darkened bubble `(5)`, but bubble `(2)` bears a partial erasure/scratch mark. Per primary visual inspection, candidate intent is clearly Option (5) (Unattempted, **0.00 marks**, yielding **38.75**). If an aggressive high-sensitivity optical OMR scanner interprets bubble (2) as a simultaneous mark, it may be scored as a multiple-marked question (-0.25), adjusting the net score to **38.50**.\n")

md.append("## 2. Question-by-Question Detailed Evaluation\n")
md.append("| Q# | Question ID | Question Summary | Marked | Key | Status | Marks | One-Line Reasoning / Solution |")
md.append("| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |")

# Status badges
for it in items:
    qn = it['q_num']
    qid = it['q_id']
    q_txt = it['question']
    marked_str = str(it['marked'])
    key_str = str(it['key'])
    status = it['status']
    marks = it['marks']
    marks_str = f"+{marks:.2f}" if marks > 0 else (f"{marks:.2f}" if marks < 0 else "0.00")
    
    if status == 'CORRECT':
        badge = "✅ `CORRECT`"
    elif status == 'WRONG':
        badge = "❌ `WRONG`"
    else:
        badge = "⚪ `UNANSWERED`"
        
    # Build a clean summary
    # Truncate summary if too long, keep salient part
    summary = q_txt
    if len(summary) > 75:
        summary = summary[:72].rstrip() + "..."
    # Escape pipe characters in summary
    summary = summary.replace('|', '/')
    
    # One-line reasoning
    exp = it.get('coaching_exp', '')
    if not exp or len(exp) < 10:
        # Fallback reasoning from option text
        correct_opt = it['options'].get(it['key'], '')
        exp = f"Correct answer is option ({it['key']}): {correct_opt}."
    else:
        # Clean explanation to one line
        exp = ' '.join(exp.split())
        if len(exp) > 160:
            exp = exp[:157].rstrip() + "..."
    exp = exp.replace('|', '/')
    
    md.append(f"| {qn} | `{qid}` | {summary} | `{marked_str}` | `{key_str}` | {badge} | {marks_str} | {exp} |")

md.append("\n---\n")
md.append("## 3. Module-Wise Performance Analysis & Insights\n")

md.append("""### A. Domain Performance Breakdown

| Subject Domain | Estimated Questions | Candidate Attempted | Correct | Accuracy | Performance Appraisal |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **General Science & Technology** | ~20 | 18 | 12 | 66.7% | **Strong**: Good grasp of basic biology, human physiology (asthma, heart chambers), physics, and scientific terminology. |
| **Karnataka History & Heritage** | ~18 | 15 | 9 | 60.0% | **Moderate to Strong**: Good recall of Kadamba chronology, Vijayanagara administrative terms, and Mysore civil services. |
| **Indian Constitution & Polity** | ~16 | 13 | 8 | 61.5% | **Solid**: Accurate on basic constitutional articles, emergency provisions, and parliamentary terms. |
| **Karnataka & Indian Geography** | ~16 | 12 | 7 | 58.3% | **Average**: Sound knowledge on river basins and dams; slight confusion on dynamic regional infrastructure notifications. |
| **Rural Development & Land Administration** | ~14 | 11 | 6 | 54.5% | **Needs Polish**: Key revenue administration concepts, KLR Act provisions, and survey terminology showed vulnerabilities. |
| **Mental Ability & Arithmetic** | ~10 | 7 | 4 | 57.1% | **Moderate**: Basic percentage and ratio questions solved; multi-step logical deduction incurred time pressure errors. |
| **Current Affairs (2025–2026)** | ~6 | 4 | 1 | 25.0% | **Vulnerable**: High penalty rate on recent sports championships, localized project names (KWIN City), and awards. |

---

### B. Strategic Recommendations & Cross-Vault Study Links

1. **Revenue Administration & Land Laws (Primary VAO Functional Need):**
   - High-yield focus required on Karnataka Land Revenue Act, 1964 and Karnataka Land Reforms Act, 1961.
   - Revisit: `[[07_Panchayat_Raj_Act_and_Rural_Administration]]` and land administration chapters for Tahsildar powers, record of rights (RTC/Pahani), mutation registers, and dispute procedures.

2. **Karnataka History & Dynasty Timelines:**
   - Review chronological sequences of Chalukyas, Rashtrakutas, Hoysalas, and Vijayanagara nayakas.
   - Comprehensive study note available: `[[08_Karnataka_History_Dynasty_Wise_Deep_Dive]]` and foundational note `[[04_Karnataka_History_and_Heritage]]`.

3. **Karnataka Geography & Resource Projects:**
   - Sharpen knowledge on river tributaries, irrigation projects, mineral belts, and railway division reorganizations.
   - Deep-dive reference note: `[[09_Karnataka_Geography_Deep_Dive]]` and `[[05_Karnataka_and_Indian_Geography]]`.

4. **Negative Marking Mitigation:**
   - 33 incorrect answers contributed -8.25 marks of penalties. Converting 10 borderline guesses into safe Option (5) unattempted selections would have lifted the net score above **41.00**.
""")

with open('VAO/AGY/08_Paper_Review/Paper1_Evaluation.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

print("Successfully generated VAO/AGY/08_Paper_Review/Paper1_Evaluation.md")
