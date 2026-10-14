import json
import os

qb_path = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy\05_Resources\Question_Bank\question_bank.json"
archive_dir = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy\05_Resources\PYQ_Archive"

with open(qb_path, "r", encoding="utf-8") as f:
    qb = json.load(f)

questions = qb.get("questions", [])

def build_archive_md(title, paper_code, q_list):
    md = [f"# {title}\n", f"> Curated and categorized repository of examination questions, expected high-yield items, and referenced questions for Karnataka Teachers Recruitment.\n"]
    for idx, q in enumerate(q_list, 1):
        md.append(f"## {q['id']} — Q{idx} ({q['subject']})")
        md.append(f"**Syllabus Line:** `{q['syllabus_id']}` | **Category Tag:** `{q['label'].upper()}` | **Origin:** {q.get('origin_tag', 'Official')}\n")
        md.append(f"**Question (English):** {q['text']}")
        if q.get('text_alt'):
            md.append(f"**ಕನ್ನಡ ಆವೃತ್ತಿ:** {q['text_alt']}\n")
        md.append("**Options:**")
        for opt in q['options']:
            md.append(f"- **{opt['label']}**: {opt['text']}")
        md.append(f"\n**Correct Answer:** `{q['answer']}`")
        md.append(f"**Detailed Explanation:** {q['explanation']}\n")
        md.append("---\n")
    return "\n".join(md)

p1_qs = [q for q in questions if q.get("paper") == "P1"]
p2_qs = [q for q in questions if q.get("paper") == "P2"]

p1_md = build_archive_md("GPSTR Paper 1 - Question Bank & Previous Year Archive", "P1", p1_qs)
with open(os.path.join(archive_dir, "GPSTR_Paper1_PYQ_Archive.md"), "w", encoding="utf-8") as f:
    f.write(p1_md)

p2_md = build_archive_md("CST Paper 2 - Computer Science Question Bank & PYQ Archive", "P2", p2_qs)
with open(os.path.join(archive_dir, "CST_Paper2_PYQ_Archive.md"), "w", encoding="utf-8") as f:
    f.write(p2_md)

print("Synchronized PYQ archives successfully.")
