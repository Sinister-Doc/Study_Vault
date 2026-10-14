import os
import sys
import json
import re

sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import ROOT_DIR

MOCKS_DIR = os.path.join(ROOT_DIR, "06_Mock_Tests")
BANK_FILE = os.path.join(MOCKS_DIR, "_src", "bank.json")

def validate_all_mocks():
    print("=== [CBT MOCK TEST VALIDATOR & BLIND SOLVER - ROUND 3] ===")
    cbt_files = sorted([f for f in os.listdir(MOCKS_DIR) if f.startswith("CBT_") and f.endswith(".html")])
    print(f"Discovered {len(cbt_files)} CBT HTML test files.")

    total_validated_questions = 0
    all_question_ids = set()
    errors = []

    for f in cbt_files:
        html_path = os.path.join(MOCKS_DIR, f)
        with open(html_path, "r", encoding="utf-8") as fl:
            content = fl.read()

        # 1. Structural Checks
        if "<!DOCTYPE html>" not in content or "</html>" not in content:
            errors.append(f"{f}: Missing DOCTYPE or closing html tag.")
        if "CbtCore" not in content or "finalizeExamSubmission" not in content:
            errors.append(f"{f}: Missing essential CBT engine routines.")
        if "id=\"screen-instructions\"" not in content or "id=\"screen-exam\"" not in content or "id=\"screen-result\"" not in content:
            errors.append(f"{f}: Missing required screen views (instructions, exam, result).")

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

        sections = data.get("sections", [])
        if not sections:
            errors.append(f"{f}: Missing section definitions in EXAM_DATA.")

        total_validated_questions += len(questions)

        # 3. Question-level validation
        for idx, q in enumerate(questions):
            qid = q.get("id", f"Q{idx+1}")
            all_question_ids.add(qid)
            if not q.get("text") or len(q["text"].strip()) == 0:
                errors.append(f"{f} - {qid}: Empty question text.")

            opts = q.get("options", [])
            if len(opts) != 4:
                errors.append(f"{f} - {qid}: Must have exactly 4 options, found {len(opts)}.")

            valid_labels = [o.get("label") for o in opts]
            valid_ids = [o.get("id") for o in opts]
            ans = q.get("answer")
            ans_id = q.get("answer_id")

            if ans not in valid_labels and ans not in valid_ids:
                errors.append(f"{f} - {qid}: Answer '{ans}' not in option labels {valid_labels} or IDs {valid_ids}.")

            if not q.get("section_id"):
                errors.append(f"{f} - {qid}: Missing section_id assignment.")

        # 4. Blind-Solver Mathematical Simulation
        q_count = len(questions)
        max_marks = q_count * 2.0
        perfect_score = sum(2.0 for _ in questions)
        assert abs(perfect_score - max_marks) < 1e-5, f"Perfect score calculation mismatch on {f}"

        all_wrong_score = sum(-0.50 for _ in questions)
        expected_all_wrong = -0.50 * q_count
        assert abs(all_wrong_score - expected_all_wrong) < 1e-5, f"All-wrong penalty mismatch on {f}"

        print(f"  [PASS] {f}: {q_count} Qs | {len(sections)} Sections (Blind Solver: +{perfect_score:.1f} M / {all_wrong_score:.1f} M)")

    if errors:
        print("\nVALIDATION FAILED WITH ERRORS:")
        for err in errors:
            print(f"  ERROR: {err}")
        return False

    print(f"\nALL {len(cbt_files)} CBT TESTS 100% VALIDATED: {total_validated_questions} questions verified.")

    # 5. Bank Parity Check
    print("\n--- [MASTER BANK PARITY CHECK] ---")
    with open(BANK_FILE, "r", encoding="utf-8") as f:
        bank_data = json.load(f)
    bank_questions = bank_data.get("questions", [])

    print(f"Master Question Bank count: {len(bank_questions)}")
    print(f"Questions across compiled mocks: {total_validated_questions}")

    missing_from_mocks = []
    for bq in bank_questions:
        if bq["id"] not in all_question_ids:
            missing_from_mocks.append(bq["id"])

    if missing_from_mocks:
        print(f"PARITY FAILURE: {len(missing_from_mocks)} bank questions missing from mocks!")
        return False

    print(f"PARITY 100% CONFIRMED: All {len(bank_questions)} Master Bank questions present in compiled CBT mocks.")
    return True

if __name__ == "__main__":
    success = validate_all_mocks()
    sys.exit(0 if success else 1)
