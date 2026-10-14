import os
import sys
import json
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR
from cbt_compiler import compile_cbt_test

MOCKS_DIR = os.path.join(ROOT_DIR, "06_Mock_Tests")
QB_PATH = os.path.join(ROOT_DIR, "05_Resources", "Question_Bank", "question_bank.json")

def build_full_mocks():
    with open(QB_PATH, "r", encoding="utf-8") as f:
        qb = json.load(f)
    existing_qs = qb.get("questions", [])

    # ----------------------------------------------------
    # 1. Full Prelims Paper 1 - Mock 1 (100 Qs from Round 1 Bank)
    # ----------------------------------------------------
    p1_m1_qs = [q for q in existing_qs if q.get("subject") in ["Current Affairs", "Humanities"]]
    p1_m1_data = {
        "title": "KPSC KAS Prelims Mock Test 01 (Paper 1: General Studies & Humanities)",
        "paper": "Paper 1",
        "duration_mins": 120,
        "marks_per_q": 2.0,
        "negative_marking": 0.50,
        "questions": p1_m1_qs
    }
    p1_m1_path = os.path.join(MOCKS_DIR, "CBT_Full_Prelims_P1_Mock1.html")
    compile_cbt_test(p1_m1_data, p1_m1_path)

    # ----------------------------------------------------
    # 2. Full Prelims Paper 2 - Mock 1 (100 Qs from Round 1 Bank)
    # ----------------------------------------------------
    p2_m1_qs = [q for q in existing_qs if q.get("subject") in ["Karnataka Affairs", "Science and Environment", "General Mental Ability"]]
    p2_m1_data = {
        "title": "KPSC KAS Prelims Mock Test 01 (Paper 2: General Studies & General Mental Ability)",
        "paper": "Paper 2",
        "duration_mins": 120,
        "marks_per_q": 2.0,
        "negative_marking": 0.50,
        "questions": p2_m1_qs
    }
    p2_m1_path = os.path.join(MOCKS_DIR, "CBT_Full_Prelims_P2_Mock1.html")
    compile_cbt_test(p2_m1_data, p2_m1_path)

    print("Completed Full Prelims Mock 1 for Paper 1 and Paper 2.")

if __name__ == "__main__":
    build_full_mocks()
