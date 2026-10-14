import os
import sys
import json
import re
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

MOCKS_DIR = os.path.join(ROOT_DIR, "06_Mock_Tests")
KEYS_DIR = os.path.join(MOCKS_DIR, "Markdown_Keys")

def build_keys_and_index():
    os.makedirs(KEYS_DIR, exist_ok=True)
    cbt_files = sorted([f for f in os.listdir(MOCKS_DIR) if f.startswith("CBT_") and f.endswith(".html")])
    
    index_md = """# KPSC KAS Computer-Based Test (CBT) Mock Examinations Suite
**Exam Cycle**: 2026-27 | **As-Of Anchor**: 2026-10-13 | **Total CBT Tests**: 19

The study vault features a complete, offline-capable **Computer-Based Test (CBT)** simulator engine replicating the official KPSC online examination environment:
- **Navigation & Palette**: 5-state NTA/KPSC question palette (Answered, Not Answered, Marked for Review, Marked & Answered, Not Visited).
- **Controls**: Save & Next, Clear Response, Mark for Review & Next, Question Paper Modal, Instructions.
- **Scoring**: Instant automated score calculation with -0.25 (-0.50 marks per 2-mark question) negative marking, detailed question-by-question review mode, and localStorage state autosave.
- **Privacy**: Neutral candidate profile, zero PII, works 100% offline via local browser.

---

## 1. Master Examination Directory

| Test Name | Category | Questions | Time Limit | Marking Scheme | Interactive CBT Simulator | Companion Markdown Key |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""

    for f in cbt_files:
        html_path = os.path.join(MOCKS_DIR, f)
        with open(html_path, "r", encoding="utf-8") as fl:
            content = fl.read()
        
        # Extract json payload
        m = re.search(r'const EXAM_DATA = (\{.*?\});', content, re.DOTALL)
        if not m:
            continue
        data = json.loads(m.group(1))
        
        title = data.get("title", f)
        paper = data.get("paper", "Prelims")
        q_count = len(data.get("questions", []))
        duration = data.get("duration_mins", 120)
        
        base_name = f.replace(".html", "")
        key_filename = f"{base_name}_Key.md"
        key_path = os.path.join(KEYS_DIR, key_filename)
        
        # Build Companion Markdown Key
        key_md = f"""---
title: {title} - Answer Key & Detailed Rationale
test_file: {f}
questions_count: {q_count}
last_verified: 2026-10-13
---

# {title}
**Official Answer Key and Detailed Solutions (ಅಧಿಕೃತ ಕೀ ಉತ್ತರಗಳು ಮತ್ತು ವಿವರಣೆಗಳು)**

> [!exam-info]
> - **Total Questions**: {q_count}
> - **Maximum Marks**: {q_count * 2}
> - **Negative Marking**: -0.50 marks per incorrect response
> - **Simulator File**: [{f}](../{f})

---

## Question-by-Question Solution & Verification Matrix

"""
        for idx, q in enumerate(data.get("questions", [])):
            key_md += f"### Q{idx+1}. [{q.get('subject', 'General Studies')}] ID: {q['id']}\n"
            key_md += f"**Question**: {q['text']}\n\n"
            for opt in q['options']:
                mark = " (Correct)" if opt['label'] == q['answer'] else ""
                key_md += f"- **{opt['label']}**: {opt['text']}{mark}\n"
            key_md += f"\n- **Official Key**: **{q['answer']}**\n"
            if q.get('statement_truths'):
                key_md += f"- **Statement Verification**: {q['statement_truths']}\n"
            key_md += f"- **Detailed Explanation**: {q['explanation']}\n"
            if q.get('vault_note'):
                key_md += f"- **Vault Note Reference**: [[{q['vault_note']}]]\n"
            key_md += "\n---\n\n"
            
        safe_write(key_path, key_md)
        print(f"Generated Key: {key_filename} ({q_count} Qs)")
        
        index_md += f"| {title} | {paper} | {q_count} Qs | {duration} Mins | +2.0 / -0.50 | [{f}](file:///{html_path.replace(os.sep, '/')}) | [{key_filename}](Markdown_Keys/{key_filename}) |\n"

    index_path = os.path.join(MOCKS_DIR, "README.md")
    safe_write(index_path, index_md)
    print(f"Updated Master Test Index at: {index_path}")

if __name__ == "__main__":
    build_keys_and_index()
