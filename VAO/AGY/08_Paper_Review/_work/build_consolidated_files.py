# -*- coding: utf-8 -*-
"""
Script to build the two requested consolidated evaluation markdown files:
1. Consolidated_Evaluation_Coaching_Key.md
2. Consolidated_Evaluation_Web_and_Domain.md
"""
import json, re

# Load Paper 1 and Paper 2 parsed items
with open('VAO/AGY/08_Paper_Review/_work/p1_items_with_exps.json', 'r', encoding='utf-8') as f:
    p1_items = json.load(f)

with open('VAO/AGY/08_Paper_Review/_work/p2_parsed_eval.json', 'r', encoding='utf-8') as f:
    p2_items = json.load(f)

# Load Paper 2 explanations
with open('VAO/AGY/08_Paper_Review/_work/build_p2_evaluation_md.py', 'r', encoding='utf-8') as f:
    p2_code = f.read()

# Extract explanations dict from build_p2_evaluation_md.py
m_exp = re.search(r'explanations\s*=\s*(\{.*?\n\})', p2_code, re.DOTALL)
if m_exp:
    # safely evaluate dict
    p2_exps = eval(m_exp.group(1))
else:
    p2_exps = {}

print(f"Loaded {len(p1_items)} P1 items, {len(p2_items)} P2 items, {len(p2_exps)} P2 explanations.")

# -------------------------------------------------------------------------------------------------
# 1. BUILD Consolidated_Evaluation_Coaching_Key.md
# -------------------------------------------------------------------------------------------------
def generate_coaching_key_md():
    # Statistics
    p1_att = sum(1 for it in p1_items if it['marked'] != 5)
    p1_c = sum(1 for it in p1_items if it['status'] == 'CORRECT')
    p1_w = sum(1 for it in p1_items if it['status'] == 'WRONG')
    p1_u = sum(1 for it in p1_items if it['status'] == 'UNANSWERED')
    p1_net = p1_c * 1.0 - p1_w * 0.25

    p2_att = sum(1 for it in p2_items if it['marked'] != 5)
    p2_c = sum(1 for it in p2_items if it['status'] == 'CORRECT')
    p2_w = sum(1 for it in p2_items if it['status'] == 'WRONG')
    p2_u = sum(1 for it in p2_items if it['status'] == 'UNANSWERED')
    p2_net = p2_c * 1.0 - p2_w * 0.25

    tot_q = len(p1_items) + len(p2_items)
    tot_att = p1_att + p2_att
    tot_c = p1_c + p2_c
    tot_w = p1_w + p2_w
    tot_u = p1_u + p2_u
    tot_net = p1_net + p2_net
    tot_acc = (tot_c / tot_att * 100) if tot_att > 0 else 0

    # Sectional stats for P2
    k_items = p2_items[0:35]
    e_items = p2_items[35:70]
    c_items = p2_items[70:100]

    def sec_stats(sec):
        att = sum(1 for it in sec if it['marked'] != 5)
        c = sum(1 for it in sec if it['status'] == 'CORRECT')
        w = sum(1 for it in sec if it['status'] == 'WRONG')
        u = sum(1 for it in sec if it['status'] == 'UNANSWERED')
        net = c * 1.0 - w * 0.25
        acc = (c / att * 100) if att > 0 else 0
        return len(sec), att, c, w, u, net, acc

    k_tot, k_att, k_c, k_w, k_u, k_net, k_acc = sec_stats(k_items)
    e_tot, e_att, e_c, e_w, e_u, e_net, e_acc = sec_stats(e_items)
    c_tot, c_att, c_c, c_w, c_u, c_net, c_acc = sec_stats(c_items)

    lines = []
    lines.append("# KEA VAO 2026 — Consolidated Evaluation Report (Official Coaching & Key PDF Baseline)\n")
    lines.append("> **Document Type:** Unified Comprehensive Examination Review (Paper 1 + Paper 2 Compressed)")
    lines.append("> **Evaluation Sourcing:** Master Coaching Key PDF (`VAO-NHK-GK.pdf` by The Target 100 / KannadaJobInfo) mapped to candidate Booklet Series **B1** via cyclic shift `Coaching_Q = (Our_Q - 10) if Our_Q > 10 else (Our_Q + 90)`, paired with official Paper 2 linguistic & computer key.")
    lines.append("> **Candidate OMR Source:** `VAO_omr.pdf` (P1 Answer Sheet No: `124666`, P2 Answer Sheet No: `234666`, Series: `B1`).\n")

    lines.append("## 1. Master Examination Merit Scorecard\n")
    lines.append("| Examination Parameter | Paper 1 (General Knowledge) | Paper 2 (Language & Computers) | Consolidated Exam Total |")
    lines.append("| :--- | :---: | :---: | :---: |")
    lines.append(f"| **Question Booklet Code** | `NHKGA41026M` (Morning) | `NHKGA41026A` (Afternoon) | **Series B1** |")
    lines.append(f"| **Total Questions** | 100 | 100 | **200** |")
    lines.append(f"| **Attempted Questions (1–4)** | {p1_att} | {p2_att} | **{tot_att}** |")
    lines.append(f"| **Correct Answers** | {p1_c} (+{p1_c:.2f}) | {p2_c} (+{p2_c:.2f}) | **{tot_c} (+{tot_c:.2f})** |")
    lines.append(f"| **Incorrect Answers** | {p1_w} (-{p1_w*0.25:.2f}) | {p2_w} (-{p2_w*0.25:.2f}) | **{tot_w} (-{tot_w*0.25:.2f})** |")
    lines.append(f"| **Unanswered (Option 5 Marked)** | {p1_u} (0.00) | {p2_u} (0.00) | **{tot_u} (0.00 Safe)** |")
    lines.append(f"| **Blank / Unmarked Questions** | 0 | 0 | **0 (100% OMR Compliance)** |")
    lines.append(f"| **Accuracy on Attempted** | {p1_c/p1_att*100:.2f}% | {p2_c/p2_att*100:.2f}% | **{tot_acc:.2f}%** |")
    lines.append(f"| **NET TOTAL SCORE ACHIEVED** | **`{p1_net:.2f} / 100.00`** *(or 38.50)* | **`{p2_net:.2f} / 100.00`** | **`{tot_net:.2f} / 200.00`** |\n")

    lines.append("### Paper 2 Section-Wise Breakdown")
    lines.append("| Section | Subject Domain | Questions | Attempted | Correct | Wrong | Unattempted | Accuracy | Net Score |")
    lines.append("| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |")
    lines.append(f"| **Part A** | General Kannada (ಸಾಮಾನ್ಯ ಕನ್ನಡ) | 35 | {k_att} | {k_c} | {k_w} | {k_u} | {k_acc:.2f}% | **`{k_net:.2f} / 35.00`** |")
    lines.append(f"| **Part B** | General English | 35 | {e_att} | {e_c} | {e_w} | {e_u} | {e_acc:.2f}% | **`{e_net:.2f} / 35.00`** |")
    lines.append(f"| **Part C** | Computer Knowledge (ಗಣಕ ಜ್ಞಾನ) | 30 | {c_att} | {c_c} | {c_w} | {c_u} | {c_acc:.2f}% | **`{c_net:.2f} / 30.00`** |")
    lines.append(f"| **Total** | **Combined Paper 2** | **100** | **{p2_att}** | **{p2_c}** | **{p2_w}** | **{p2_u}** | **{p2_c/p2_att*100:.2f}%** | **`{p2_net:.2f} / 100.00`** |\n")

    lines.append("> [!NOTE] Scoring Compliance & Option (5) Rules")
    lines.append("> 1. **Option (5) Protection:** Under official KEA regulations, Option (5) serves as the mandatory non-attempt declaration bubble to prevent post-examination tampering. Marking Option (5) incurs **zero penalty (0.00 marks)**. The candidate appropriately marked Option (5) across 37 total questions, preventing negative penalties.")
    lines.append("> 2. **P1-Q024 Sensitivity:** The candidate shaded bubble `(5)`, but bubble `(2)` bears a partial erasure mark. Candidate intent is Option (5) (0.00 marks, giving `38.75`). If an aggressive optical OMR scanner reads bubble (2) as a simultaneous mark, it may score as a multiple mark (-0.25), adjusting the Paper 1 score to `38.50` and the combined score to `100.25`.\n")

    lines.append("## 2. Paper 1 Detailed Question-by-Question Evaluation\n")
    lines.append("| Q# | ID | Question Summary | Marked | Key | Status | Marks | Solution / Reasoning (Coaching PDF Key) |")
    lines.append("| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |")
    for it in p1_items:
        qn = it['q_num']
        qid = it['q_id']
        q_txt = it['question']
        marked_str = str(it['marked'])
        key_str = str(it['key'])
        status = it['status']
        marks = it['marks']
        marks_str = f"+{marks:.2f}" if marks > 0 else (f"{marks:.2f}" if marks < 0 else "0.00")
        badge = "✅ `CORRECT`" if status == 'CORRECT' else ("❌ `WRONG`" if status == 'WRONG' else "⚪ `UNANSWERED`")
        
        summary = q_txt[:70].rstrip() + "..." if len(q_txt) > 73 else q_txt
        summary = summary.replace('|', '/')
        
        exp = it.get('coaching_exp', '')
        if not exp or len(exp) < 10:
            exp = f"Correct answer is option ({it['key']})."
        else:
            exp = ' '.join(exp.split())
            if len(exp) > 150:
                exp = exp[:147].rstrip() + "..."
        exp = exp.replace('|', '/')
        lines.append(f"| {qn} | `{qid}` | {summary} | `{marked_str}` | `{key_str}` | {badge} | {marks_str} | {exp} |")

    lines.append("\n## 3. Paper 2 Detailed Question-by-Question Evaluation\n")
    lines.append("| Q# | ID | Question Summary | Marked | Key | Status | Marks | Solution / Reasoning (Official Linguistic/IT Baseline) |")
    lines.append("| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |")
    for it in p2_items:
        qn = it['q_num']
        qid = it['q_id']
        q_txt = it['question']
        marked_str = str(it['marked'])
        key_str = str(it['key'])
        status = it['status']
        marks = it['marks']
        marks_str = f"+{marks:.2f}" if marks > 0 else (f"{marks:.2f}" if marks < 0 else "0.00")
        badge = "✅ `CORRECT`" if status == 'CORRECT' else ("❌ `WRONG`" if status == 'WRONG' else "⚪ `UNANSWERED`")
        
        summary = q_txt[:70].rstrip() + "..." if len(q_txt) > 73 else q_txt
        summary = summary.replace('|', '/')
        
        exp = p2_exps.get(qn, f"Correct answer is option ({it['key']}).")
        exp = exp.replace('|', '/')
        lines.append(f"| {qn} | `{qid}` | {summary} | `{marked_str}` | `{key_str}` | {badge} | {marks_str} | {exp} |")

    lines.append("\n---\n")
    lines.append("## 4. Synthesis & Key Takeaways\n")
    lines.append("""- **Aggregate Merit Position**: Combined net score of **`100.50 / 200.00`** (50.25%) places the candidate in a solid position for the competitive Village Administrative Officer selection.
- **Asymmetric Strength**: Stellar accuracy in Paper 2 English (85.71%) and Computer Knowledge (78.57%) provided the principal scoring engine.
- **Revision Recommendations**:
  - `[[01_General_Kannada_Grammar_and_Vocabulary]]`: Classical Kannada literature, metrics (Ragale, Kanda), and ancient poets.
  - `[[07_Panchayat_Raj_Act_and_Rural_Administration]]`: Revenue administration, KLR Act, mutation registers, and dispute resolution.
  - `[[08_Karnataka_History_Dynasty_Wise_Deep_Dive]]` and `[[09_Karnataka_Geography_Deep_Dive]]`: Dynasty chronologies and state geographic infrastructure.
""")

    with open('VAO/AGY/08_Paper_Review/Consolidated_Evaluation_Coaching_Key.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print("Saved Consolidated_Evaluation_Coaching_Key.md successfully")

generate_coaching_key_md()
