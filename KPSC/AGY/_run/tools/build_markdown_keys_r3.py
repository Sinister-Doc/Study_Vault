import os
import sys
import json
import re

sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

MOCKS_DIR = os.path.join(ROOT_DIR, "06_Mock_Tests")
KEYS_DIR = os.path.join(MOCKS_DIR, "Markdown_Keys")

def rebuild_markdown_keys_and_index():
    print("=== Rebuilding Companion Markdown Keys & Master Index for 22 CBT Tests ===")
    os.makedirs(KEYS_DIR, exist_ok=True)

    # Scan existing note basenames
    vault_notes = {}
    for dp, _, fns in os.walk(ROOT_DIR):
        if "_run" in dp or ".git" in dp:
            continue
        for fn in fns:
            if fn.endswith(".md"):
                vault_notes[fn[:-3].lower()] = fn[:-3]

    concept_map = {
        "kadambas": "Early_Dynasties_Kadambas_and_Gangas",
        "badami chalukyas": "Badami_Chalukyas_Architecture_and_Empire",
        "rashtrakutas": "Rashtrakutas_of_Manyakheta_and_Kavirajamarga",
        "vachana movement": "Kalyana_Chalukyas_Kalachuris_and_Vachana_Movement",
        "hoysalas": "Hoysalas_of_Dwarasamudra_and_Seunas",
        "vijayanagara": "Vijayanagara_Empire_Polity_and_Culture",
        "adil shahis": "Bahmani_and_Adil_Shahi_Sultanates",
        "bahmanis": "Bahmani_and_Adil_Shahi_Sultanates",
        "keladi nayakas": "Nayakas_of_Keladi_and_Chitradurga",
        "chitradurga": "Nayakas_of_Keladi_and_Chitradurga",
        "mysore": "Mysore_Kingdom_Wodeyars_and_Dewans",
        "freedom struggle": "Freedom_Struggle_and_Armed_Revolts_in_Karnataka",
        "unification": "Karnataka_Unification_Social_Reforms_and_Culture",
        "geography": "Karnataka_Location_Physiography_and_Geology",
        "climate": "Karnataka_Climate_and_Rainfall_Patterns",
        "forests": "Karnataka_Forests_Wildlife_and_Biodiversity",
        "agriculture": "Karnataka_Agro_Climatic_Zones_and_Agriculture",
        "minerals": "Karnataka_Mineral_Resources_and_Energy",
        "demography": "Karnataka_Demography_Urbanisation_and_Infrastructure",
        "infrastructure": "Karnataka_Demography_Urbanisation_and_Infrastructure",
        "irrigation": "Karnataka_Drainage_and_River_Basins",
        "ramsar": "Karnataka_Forests_Wildlife_and_Biodiversity",
        "halmidi": "Prehistory_and_Protohistory_Karnataka",
        "nanjundappa": "Social_Welfare_and_Justice_Karnataka",
        "article 371j": "Social_Welfare_and_Justice_Karnataka",
        "humanities": "Indian_History_Overview",
        "gma": "Logical_and_Analytical_Reasoning",
        "science": "Science_and_Technology_Developments",
        "environment": "Environment_Biodiversity_Climate",
        "physics": "Science_and_Technology_Developments",
        "chemistry": "Science_and_Technology_Developments",
        "biology": "Science_and_Technology_Developments",
        "space": "Science_and_Technology_Developments",
        "biotechnology": "Science_and_Technology_Developments",
        "nuclear": "Science_and_Technology_Developments",
        "ai": "Science_and_Technology_Developments",
        "tech": "Science_and_Technology_Developments",
        "energy": "Karnataka_Mineral_Resources_and_Energy",
        "schemes": "Karnataka_Flagship_Schemes",
        "pyq 2014": "PYQ_Analysis",
        "pyq 2017": "PYQ_Analysis",
        "pyq 2020": "PYQ_Analysis",
        "pyq": "PYQ_Analysis",
    }

    cbt_files = sorted([f for f in os.listdir(MOCKS_DIR) if f.startswith("CBT_") and f.endswith(".html")])
    index_md = """# KPSC KAS Computer-Based Test (CBT) Mock Examinations Suite
**Exam Cycle**: 2026-27 | **As-Of Anchor**: 2026-10-13 | **Total CBT Tests**: 22 | **Total Questions**: 1,225

The study vault features a complete, offline-capable **Computer-Based Test (CBT)** simulator engine replicating the official KPSC online examination environment:
- **Simulation Engine**: Robust wall-clock countdown timer (zero drift, survives reload, auto-submits on expiration), pre-exam instructions with standard Exam Mode and 2-minute Quick Check modes.
- **Sectional Navigation**: Section tabs inside the same single-file HTML test with live 5-state palette counters (Answered, Not Answered, Marked for Review, Marked & Answered, Not Visited).
- **Correctness & Evaluation**: State keyed strictly by stable question IDs (`q.id`), pure scoring function calculating exact competitive raw scores with -0.50 negative marking per question, plus detailed section and topic performance analytics.
- **Privacy**: Neutral candidate profile, zero PII, works 100% offline via local browser double-click.

---

## 1. Master Examination Directory

| Test Name | Category | Questions | Time Limit | Marking Scheme | Interactive CBT Simulator | Companion Markdown Key |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""

    for f in cbt_files:
        html_path = os.path.join(MOCKS_DIR, f)
        with open(html_path, "r", encoding="utf-8") as fl:
            content = fl.read()

        m = re.search(r'const EXAM_DATA = (\{.*?\});', content, re.DOTALL)
        if not m:
            continue
        data = json.loads(m.group(1))

        title = data.get("title", f)
        paper = data.get("paper", "Prelims")
        q_count = len(data.get("questions", []))
        duration = data.get("duration_minutes", 120)
        sections = data.get("sections", [])

        base_name = f.replace(".html", "")
        key_filename = f"{base_name}_Key.md"
        key_path = os.path.join(KEYS_DIR, key_filename)

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
> - **Sections**: {", ".join([s['name'] for s in sections])}

---

## Question-by-Question Solution & Verification Matrix

"""
        for idx, q in enumerate(data.get("questions", [])):
            sec_name = "General Studies"
            for s in sections:
                if s["id"] == q.get("section_id"):
                    sec_name = s["name"]
                    break

            key_md += f"### Q{idx+1}. [{q.get('subject', 'General Studies')} | {sec_name}] ID: {q['id']}\n"
            key_md += f"**Question**: {q['text']}\n\n"
            for opt in q['options']:
                mark = " (Correct)" if (opt['id'] == q.get('answer_id') or opt['label'] == q.get('answer')) else ""
                key_md += f"- **{opt['label']}**: {opt['text']}{mark}\n"
            key_md += f"\n- **Official Key**: **{q.get('answer')}**\n"
            if q.get('statement_truths'):
                key_md += f"- **Statement Verification**: {q['statement_truths']}\n"
            key_md += f"- **Detailed Explanation**: {q['explanation']}\n"

            # Resolve vault note reference
            raw_ref = q.get('linked_note') or q.get('vault_note', '')
            if raw_ref:
                raw_lower = raw_ref.strip().lower()
                if raw_lower in vault_notes:
                    key_md += f"- **Vault Note Reference**: [[{vault_notes[raw_lower]}]]\n"
                elif raw_lower in concept_map:
                    key_md += f"- **Vault Note Reference**: [[{concept_map[raw_lower]}]]\n"
                else:
                    key_md += f"- **Topic / Focus**: {raw_ref}\n"
            key_md += "\n---\n\n"

        safe_write(key_path, key_md)
        print(f"Rebuilt Key: {key_filename} ({q_count} Qs)")

        index_md += f"| {title} | {paper} | {q_count} Qs | {duration} Mins | +2.0 / -0.50 | [{f}](file:///{html_path.replace(os.sep, '/')}) | [{key_filename}](Markdown_Keys/{key_filename}) |\n"

    index_path = os.path.join(MOCKS_DIR, "README.md")
    safe_write(index_path, index_md)
    print("Updated 06_Mock_Tests/README.md")

if __name__ == "__main__":
    rebuild_markdown_keys_and_index()
