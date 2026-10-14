import os
import sys
import json
import re
import hashlib

sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

mocks_dir = os.path.join(ROOT_DIR, "06_Mock_Tests")
src_dir = os.path.join(mocks_dir, "_src")
bank_file = os.path.join(src_dir, "bank.json")

def normalize_text(text):
    if not text:
        return ""
    # Remove extra whitespace and lower-case
    return re.sub(r'\s+', ' ', text.strip().lower())

def extract_bank():
    html_files = sorted([f for f in os.listdir(mocks_dir) if f.startswith("CBT_") and f.endswith(".html")])
    
    total_in = 0
    file_counts = {}
    seen_hashes = {}
    master_bank = []
    exact_duplicates = []

    for f in html_files:
        f_path = os.path.join(mocks_dir, f)
        with open(f_path, "r", encoding="utf-8") as fp:
            content = fp.read()
        m = re.search(r'const EXAM_DATA = (\{.*?\});', content, re.DOTALL)
        if not m:
            continue
        data = json.loads(m.group(1))
        paper_name = data.get("paper", "")
        test_title = data.get("title", "")
        questions = data.get("questions", [])
        
        file_counts[f] = len(questions)
        total_in += len(questions)

        for q in questions:
            norm_q = normalize_text(q.get("text", ""))
            q_hash = hashlib.sha256(norm_q.encode("utf-8")).hexdigest()[:16]

            # Ensure every option has stable option id
            options = []
            for opt in q.get("options", []):
                opt_label = opt.get("label", "")
                opt_id = opt.get("id", f"opt_{opt_label.lower()}")
                options.append({
                    "id": opt_id,
                    "label": opt_label,
                    "text": opt.get("text", "")
                })

            # Map correct answer to option id if not already
            ans_raw = q.get("answer", "")
            ans_id = q.get("answer_id")
            if not ans_id:
                for opt in options:
                    if opt["label"] == ans_raw or opt["id"] == ans_raw:
                        ans_id = opt["id"]
                        break
            if not ans_id and options:
                ans_id = options[0]["id"]

            question_entry = {
                "id": q.get("id"),
                "text_hash": q_hash,
                "text": q.get("text", ""),
                "options": options,
                "answer": ans_raw,
                "answer_id": ans_id,
                "explanation": q.get("explanation", ""),
                "statement_truths": q.get("statement_truths", ""),
                "subject": q.get("subject", "General Studies"),
                "paper": paper_name,
                "syllabus_id": q.get("syllabus_id", ""),
                "type": q.get("type", "multiple-choice"),
                "difficulty": q.get("difficulty", "standard"),
                "sources": q.get("source_url") or q.get("sources") or "KPSC Notification / Standard Textbooks",
                "linked_note": q.get("vault_note", ""),
                "origin_file": f
            }

            if q_hash in seen_hashes:
                exact_duplicates.append({
                    "duplicate_id": q.get("id"),
                    "text_hash": q_hash,
                    "origin_file": f,
                    "original_id": seen_hashes[q_hash]["id"],
                    "original_file": seen_hashes[q_hash]["origin_file"],
                    "text_snippet": q.get("text", "")[:80]
                })
            else:
                seen_hashes[q_hash] = question_entry
                master_bank.append(question_entry)

    print(f"Extraction Summary:")
    print(f"Total Questions In: {total_in}")
    print(f"Total Unique Questions in Master Bank: {len(master_bank)}")
    print(f"Total Exact Duplicates Logged: {len(exact_duplicates)}")
    print(f"Integrity Check: {total_in} == {len(master_bank)} + {len(exact_duplicates)} -> {total_in == len(master_bank) + len(exact_duplicates)}")

    safe_write(bank_file, json.dumps({
        "metadata": {
            "version": "1.0",
            "as_of_date": "2026-10-13",
            "total_in": total_in,
            "unique_count": len(master_bank),
            "duplicates_count": len(exact_duplicates)
        },
        "questions": master_bank,
        "duplicates_log": exact_duplicates,
        "source_file_counts": file_counts
    }, indent=2))
    print(f"Saved Master Question Bank to: {bank_file}")

if __name__ == "__main__":
    extract_bank()
