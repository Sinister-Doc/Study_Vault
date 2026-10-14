# -*- coding: utf-8 -*-
"""
Assembles and writes finalized, 100% distinct datasets for p1_questions.py and p2_questions.py.
"""
import os
import sys

BASE_DIR = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\_cst_scripts"
sys.path.append(BASE_DIR)

import build_p1_test2
import build_p2_test2

# 1. Update p1_questions.py
with open(os.path.join(BASE_DIR, "p1_t1_base.py"), "r", encoding="utf-8") as f:
    p1_base = f.read()

p1_t2_qs = build_p1_test2.get_paper1_test2_questions()
import json
p1_t2_json = json.dumps(p1_t2_qs, ensure_ascii=False, indent=4)

p1_full_code = f"""{p1_base}

def get_paper1_test2():
    \"\"\"
    Exhaustive, completely distinct 150 questions for Paper 1 Test 2.
    \"\"\"
    import build_p1_test2
    return build_p1_test2.get_paper1_test2_questions()

def get_p1_sections():
    return [
        {{"id": "S1", "name": "General Knowledge", "count": 20}},
        {{"id": "S2", "name": "Current Affairs", "count": 15}},
        {{"id": "S3", "name": "General Kannada", "count": 25}},
        {{"id": "S4", "name": "General English", "count": 25}},
        {{"id": "S5", "name": "Educational Psychology", "count": 25}},
        {{"id": "S6", "name": "Computer Literacy", "count": 20}},
        {{"id": "S7", "name": "Health Education", "count": 10}},
        {{"id": "S8", "name": "Value Education", "count": 10}}
    ]
"""

with open(os.path.join(BASE_DIR, "p1_questions.py"), "w", encoding="utf-8") as f:
    f.write(p1_full_code)

print("Updated p1_questions.py successfully.")

# 2. Update p2_questions.py
with open(os.path.join(BASE_DIR, "p2_questions.py"), "r", encoding="utf-8") as f:
    p2_orig = f.read()

end_idx = p2_orig.find("def get_paper2_test2")
p2_base = p2_orig[:end_idx]

# Fix AMAT in p2_base
p2_base = p2_base.replace(
    '"answer": "B",\n            "explanation": "AMAT = Hit_Time + (Miss_Rate * Miss_Penalty) = 2 + (0.05 * 50) = 2 + 2.5 = 4.5 ns (or 0.95*2 + 0.05*50 = 1.9 + 2.5 = 4.4 ns)."',
    '"answer": "A",\n            "explanation": "In hierarchical memory where cache is checked first (hit time = 2 ns) and on miss main memory is accessed (miss penalty = 50 ns): AMAT = Hit Time + (Miss Rate * Miss Penalty) = 2 + (0.05 * 50) = 2 + 2.5 = 4.5 ns."'
)

p2_full_code = f"""{p2_base}

def get_paper2_test2():
    \"\"\"
    Exhaustive, completely distinct 150 questions for Paper 2 Test 2.
    \"\"\"
    import build_p2_test2
    return build_p2_test2.get_paper2_test2_questions()

def get_p2_sections():
    return [
        {{"id": "U1", "name": "Fundamentals of Computers", "count": 15}},
        {{"id": "U2", "name": "Digital Logic & Organization", "count": 15}},
        {{"id": "U3", "name": "Programming with C & C++", "count": 15}},
        {{"id": "U4", "name": "Data Structures & Algorithms", "count": 15}},
        {{"id": "U5", "name": "Database Management Systems", "count": 15}},
        {{"id": "U6", "name": "Operating Systems", "count": 15}},
        {{"id": "U7", "name": "Computer Networks", "count": 15}},
        {{"id": "U8", "name": "Software Engineering & OOAD", "count": 15}},
        {{"id": "U9", "name": "Web Technologies", "count": 15}},
        {{"id": "U10", "name": "Information Security & Emerging Trends", "count": 15}}
    ]
"""

with open(os.path.join(BASE_DIR, "p2_questions.py"), "w", encoding="utf-8") as f:
    f.write(p2_full_code)

print("Updated p2_questions.py successfully.")
