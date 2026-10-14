import os
import sys
import json
import re

# Add _run/tools to path for safe_ops
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_run", "tools"))
from safe_ops import safe_write, ROOT_DIR

MOCKS_DIR = os.path.join(ROOT_DIR, "06_Mock_Tests")
SRC_DIR = os.path.join(MOCKS_DIR, "_src")
BANK_FILE = os.path.join(SRC_DIR, "bank.json")
TEMPLATE_FILE = os.path.join(SRC_DIR, "cbt_engine_template.html")

def compile_all_mocks():
    print("=== Compiling 22 Self-Contained CBT HTML Mocks from Master Question Bank ===")

    with open(BANK_FILE, "r", encoding="utf-8") as f:
        bank_data = json.load(f)

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_html = f.read()

    questions_by_file = {}
    for q in bank_data["questions"]:
        orig = q.get("origin_file")
        if orig:
            questions_by_file.setdefault(orig, []).append(q)

    print(f"Loaded {len(bank_data['questions'])} questions across {len(questions_by_file)} target files.")

    compiled_count = 0
    total_compiled_questions = 0

    for filename, q_list in sorted(questions_by_file.items()):
        test_id = filename.replace(".html", "")

        # Determine metadata, duration, and sections based on file type
        if "Full_Prelims_P1" in filename:
            title = f"KPSC KAS Prelims Paper 1 — {test_id.split('_')[-1]} (Full Mock)"
            paper_type = "Paper 1 (Current Events + Humanities)"
            duration_minutes = 120
            # Sections: 40 Qs Current Events, 60 Qs Humanities
            sections = [
                {"id": "SEC-P1-1", "name": "Section 1: Current Events (National & Int.)", "q_count": 40},
                {"id": "SEC-P1-2", "name": "Section 2: Humanities (History, Geo, Polity, Econ)", "q_count": 60}
            ]
            for idx, q in enumerate(q_list):
                q["section_id"] = "SEC-P1-1" if idx < 40 else "SEC-P1-2"

        elif "Full_Prelims_P2" in filename:
            title = f"KPSC KAS Prelims Paper 2 — {test_id.split('_')[-1]} (Full Mock)"
            paper_type = "Paper 2 (State Affairs + Science + Mental Ability)"
            duration_minutes = 120
            # Sections: 40 Qs State Affairs, 30 Qs Science, 30 Qs Mental Ability
            sections = [
                {"id": "SEC-P2-1", "name": "Section 1: State Importance & Schemes", "q_count": 40},
                {"id": "SEC-P2-2", "name": "Section 2: General Science & Technology", "q_count": 30},
                {"id": "SEC-P2-3", "name": "Section 3: General Mental Ability", "q_count": 30}
            ]
            for idx, q in enumerate(q_list):
                if idx < 40:
                    q["section_id"] = "SEC-P2-1"
                elif idx < 70:
                    q["section_id"] = "SEC-P2-2"
                else:
                    q["section_id"] = "SEC-P2-3"

        elif "Sectional" in filename:
            subject_clean = filename.replace("CBT_Sectional_", "").replace(".html", "").replace("_", " ")
            title = f"KPSC KAS Sectional Mock — {subject_clean} (50 Questions)"
            paper_type = f"Sectional: {subject_clean}"
            duration_minutes = 60
            sections = [
                {"id": "SEC-DRILL-1", "name": "Part A: Fundamental & Conceptual Questions", "q_count": 25},
                {"id": "SEC-DRILL-2", "name": "Part B: Advanced Analytical & Applied Focus", "q_count": 25}
            ]
            for idx, q in enumerate(q_list):
                q["section_id"] = "SEC-DRILL-1" if idx < 25 else "SEC-DRILL-2"

        elif "CA_Mock" in filename:
            month_clean = filename.replace("CBT_CA_Mock_", "").replace(".html", "").replace("_", " ")
            title = f"KPSC KAS Monthly Current Affairs Mock — {month_clean}"
            paper_type = f"Current Affairs: {month_clean}"
            duration_minutes = 30
            sections = [
                {"id": "SEC-CA-1", "name": "National & Global Affairs", "q_count": 13},
                {"id": "SEC-CA-2", "name": "Karnataka State Developments", "q_count": 12}
            ]
            for idx, q in enumerate(q_list):
                q["section_id"] = "SEC-CA-1" if idx < 13 else "SEC-CA-2"

        elif "PYQ" in filename:
            title = "KPSC KAS Authentic Previous Year Questions (PYQ) Master Mock"
            paper_type = "Verified Previous Year Questions (2014-2020)"
            duration_minutes = 120
            sections = [
                {"id": "SEC-PYQ-1", "name": "Paper 1 Selected PYQs (Humanities & CA)", "q_count": 50},
                {"id": "SEC-PYQ-2", "name": "Paper 2 Selected PYQs (State, S&T, GMA)", "q_count": 50}
            ]
            for idx, q in enumerate(q_list):
                q["section_id"] = "SEC-PYQ-1" if idx < 50 else "SEC-PYQ-2"
        else:
            title = f"KPSC KAS Examination — {test_id}"
            paper_type = "General Studies"
            duration_minutes = 120
            sections = [{"id": "SEC-GEN", "name": "General Studies", "q_count": len(q_list)}]
            for q in q_list:
                q["section_id"] = "SEC-GEN"

        exam_payload = {
            "test_id": test_id,
            "title": title,
            "paper": paper_type,
            "duration_minutes": duration_minutes,
            "positive_marks": 2.0,
            "negative_penalty": 0.5,
            "sections": sections,
            "questions": q_list
        }

        # Embed into template
        json_str = json.dumps(exam_payload, ensure_ascii=False)
        compiled_html = template_html.replace("__EXAM_TITLE__", title)
        compiled_html = compiled_html.replace("__EXAM_JSON__", json_str)

        target_path = os.path.join(MOCKS_DIR, filename)
        safe_write(target_path, compiled_html)
        print(f"Compiled: {filename} ({len(q_list)} Qs | {len(sections)} sections | {duration_minutes}m)")

        compiled_count += 1
        total_compiled_questions += len(q_list)

    print(f"\nCompilation Complete: {compiled_count} tests compiled with {total_compiled_questions} total questions.")
    assert total_compiled_questions == len(bank_data["questions"]), "Parity failure: question counts mismatch!"
    print("100% Question Parity Confirmed with Master Bank!")

if __name__ == "__main__":
    compile_all_mocks()
