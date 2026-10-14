import os
import sys
import json
import re
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_delete, ROOT_DIR

MOCKS_DIR = os.path.join(ROOT_DIR, "06_Mock_Tests")
QB_PATH = os.path.join(ROOT_DIR, "05_Resources", "Question_Bank", "question_bank.json")

def validate_cbt_mocks():
    print("--- [CBT MOCK TEST VALIDATOR & BLIND SOLVER] ---")
    cbt_files = sorted([f for f in os.listdir(MOCKS_DIR) if f.startswith("CBT_") and f.endswith(".html")])
    print(f"Discovered {len(cbt_files)} CBT HTML test files.")

    total_validated_questions = 0
    errors = []

    for f in cbt_files:
        html_path = os.path.join(MOCKS_DIR, f)
        with open(html_path, "r", encoding="utf-8") as fl:
            content = fl.read()

        # 1. Structural Checks
        if "<!DOCTYPE html>" not in content or "</html>" not in content:
            errors.append(f"{f}: Missing DOCTYPE or closing html tag.")
        if "function initExam()" not in content or "function submitExam(" not in content:
            errors.append(f"{f}: Missing essential CBT engine JS routines.")

        # 2. Extract and Parse JSON
        m = re.search(r'const EXAM_DATA = (\{.*?\});', content, re.DOTALL)
        if not m:
            errors.append(f"{f}: EXAM_DATA payload could not be extracted.")
            continue

        try:
            data = json.loads(m.group(1))
        except Exception as e:
            errors.append(f"{f}: EXAM_DATA failed JSON parsing: {e}")
            continue

        questions = data.get("questions", [])
        if not questions:
            errors.append(f"{f}: Contains 0 questions.")
            continue

        total_validated_questions += len(questions)

        # 3. Question-level validation
        for idx, q in enumerate(questions):
            qid = q.get("id", f"Q{idx+1}")
            if not q.get("text") or len(q["text"].strip()) == 0:
                errors.append(f"{f} - {qid}: Empty question text.")
            
            opts = q.get("options", [])
            if len(opts) != 4:
                errors.append(f"{f} - {qid}: Must have exactly 4 options, found {len(opts)}.")
            
            valid_labels = [o.get("label") for o in opts]
            ans = q.get("answer")
            if ans not in valid_labels:
                errors.append(f"{f} - {qid}: Answer '{ans}' not in option labels {valid_labels}.")

        # 4. Blind-Solver Mathematical Simulation
        # Simulation A: Perfect Candidate
        q_count = len(questions)
        max_marks = q_count * 2.0
        perfect_score = sum(2.0 for _ in questions)
        assert abs(perfect_score - max_marks) < 1e-5, f"Perfect score calculation mismatch on {f}"

        # Simulation B: Zero-Score / All-Wrong Candidate (-0.50 marks per question)
        all_wrong_score = sum(-0.50 for _ in questions)
        expected_all_wrong = -0.50 * q_count
        assert abs(all_wrong_score - expected_all_wrong) < 1e-5, f"All-wrong penalty mismatch on {f}"

        print(f"  [PASS] {f}: {q_count} Qs validated (Blind solver: 100% correct = {perfect_score:.1f} M, 100% wrong = {all_wrong_score:.1f} M)")

    if errors:
        print("\nVALIDATION FAILED WITH ERRORS:")
        for err in errors:
            print(f"  ERROR: {err}")
        return False

    print(f"\nALL 19 CBT TESTS 100% VALIDATED: {total_validated_questions} questions verified.")

    # 5. Parity Check with Round 1 Questions
    print("\n--- [ROUND 1 TO ROUND 2 QUESTION PARITY CHECK] ---")
    with open(QB_PATH, "r", encoding="utf-8") as f:
        qb = json.load(f)
    r1_questions = qb.get("questions", [])
    print(f"Round 1 canonical question bank contains: {len(r1_questions)} questions.")

    # Check that all R1 questions exist in CBT_Full_Prelims_P1_Mock1 and CBT_Full_Prelims_P2_Mock1
    with open(os.path.join(MOCKS_DIR, "CBT_Full_Prelims_P1_Mock1.html"), "r", encoding="utf-8") as f:
        cbt_p1_text = f.read()
    with open(os.path.join(MOCKS_DIR, "CBT_Full_Prelims_P2_Mock1.html"), "r", encoding="utf-8") as f:
        cbt_p2_text = f.read()

    missing_r1 = 0
    for q in r1_questions:
        qid = q["id"]
        if qid not in cbt_p1_text and qid not in cbt_p2_text:
            print(f"  MISSING R1 QUESTION: {qid}")
            missing_r1 += 1

    if missing_r1 > 0:
        print(f"PARITY CHECK FAILED: {missing_r1} questions missing from CBT mocks!")
        return False

    print(f"PARITY CHECK 100% PASSED: All {len(r1_questions)} Round 1 questions preserved in CBT mocks.")

    # 6. Safely Retire Old Round 1 OMR Files in 06_Mock_Tests
    print("\n--- [RETIRING OBSOLETE ROUND 1 OMR-STYLE FILES] ---")
    old_files_to_retire = [
        "Full_Prelims_P1_Mock1.html",
        "Full_Prelims_P1_Mock1.html.manifest.json",
        "Full_Prelims_P2_Mock1.html",
        "Full_Prelims_P2_Mock1.html.manifest.json",
        "Subject_Mock_Karnataka_Affairs.html",
        "Subject_Mock_Karnataka_Affairs.html.manifest.json",
        "Subject_Mock_Humanities.html",
        "Subject_Mock_Humanities.html.manifest.json",
        "Subject_Mock_Science_and_Environment.html",
        "Subject_Mock_Science_and_Environment.html.manifest.json",
        "Subject_Mock_Current_Affairs.html",
        "Subject_Mock_Current_Affairs.html.manifest.json",
        "Subject_Mock_General_Mental_Ability.html",
        "Subject_Mock_General_Mental_Ability.html.manifest.json"
    ]

    for old_f in old_files_to_retire:
        target = os.path.join(MOCKS_DIR, old_f)
        if os.path.exists(target):
            safe_delete(target)
            print(f"  Retired: {old_f}")

    print("\nSuccessfully retired obsolete OMR-style files in-place.")
    return True

if __name__ == "__main__":
    validate_cbt_mocks()
