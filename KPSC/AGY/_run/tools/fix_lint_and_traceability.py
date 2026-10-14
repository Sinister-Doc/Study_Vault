import os
import sys
import json
import re

sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

def fix_frontmatter():
    print("--- Fixing Frontmatter in 32 Round 2 Notes ---")
    files_to_fix = [
        # Karnataka History
        ("03_Notes/01_Karnataka_History_and_Culture/Badami_Chalukyas_Architecture_and_Empire.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.2"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Bahmani_and_Adil_Shahi_Sultanates.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.3"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Early_Dynasties_Kadambas_and_Gangas.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.2"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Early_Karnataka_Dynasties.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.2"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Freedom_Struggle_and_Armed_Revolts_in_Karnataka.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.4"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Freedom_Struggle_in_Karnataka.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.4"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Hoysalas_of_Dwarasamudra_and_Seunas.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.2"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Kalyana_Chalukyas_Kalachuris_and_Vachana_Movement.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.2"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Karnataka_Unification_and_Social_Movements.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.5"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Karnataka_Unification_Social_Reforms_and_Culture.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.5"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Mysore_Kingdom_Wodeyars_and_Dewans.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.3"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Nayakas_of_Keladi_and_Chitradurga.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.3"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Prehistory_and_Protohistory_Karnataka.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.2"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Rashtrakutas_of_Manyakheta_and_Kavirajamarga.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.2"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Vijayanagara_Empire_Polity_and_Culture.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.3"]),
        ("03_Notes/01_Karnataka_History_and_Culture/Vijayanagara_and_Mysore_Kingdom.md", ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.3"]),

        # Karnataka Geography
        ("03_Notes/03_Geography_Karnataka_and_World/Karnataka_Agro_Climatic_Zones_and_Agriculture.md", ["P1-S2.4", "M-GS2-S1.2", "M-GS3-S3.1"]),
        ("03_Notes/03_Geography_Karnataka_and_World/Karnataka_Climate_and_Rainfall_Patterns.md", ["P1-S2.4", "M-GS2-S1.2"]),
        ("03_Notes/03_Geography_Karnataka_and_World/Karnataka_Demography_Urbanisation_and_Infrastructure.md", ["P1-S2.4", "P1-S2.8", "M-GS2-S1.2", "M-GS3-S3.3"]),
        ("03_Notes/03_Geography_Karnataka_and_World/Karnataka_Drainage_and_River_Basins.md", ["P1-S2.4", "M-GS2-S1.2"]),
        ("03_Notes/03_Geography_Karnataka_and_World/Karnataka_Forests_Wildlife_and_Biodiversity.md", ["P1-S2.4", "P2-S2.2", "M-GS2-S1.2", "M-GS3-S2.1"]),
        ("03_Notes/03_Geography_Karnataka_and_World/Karnataka_Location_Physiography_and_Geology.md", ["P1-S2.4", "M-GS2-S1.2"]),
        ("03_Notes/03_Geography_Karnataka_and_World/Karnataka_Mineral_Resources_and_Energy.md", ["P1-S2.4", "M-GS2-S1.2", "M-GS3-S1.1"]),
        ("03_Notes/03_Geography_Karnataka_and_World/Karnataka_Physiography_and_Rivers.md", ["P1-S2.4", "M-GS2-S1.2"]),
        ("03_Notes/03_Geography_Karnataka_and_World/Karnataka_Soils_and_Land_Degradation.md", ["P1-S2.4", "M-GS2-S1.2"]),

        # Monthly Current Affairs
        ("04_Current_Affairs_GK/Monthly_Digests_2026/2026-02_February.md", ["P1-S1.1", "P1-S1.2", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]),
        ("04_Current_Affairs_GK/Monthly_Digests_2026/2026-03_March.md", ["P1-S1.1", "P1-S1.2", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]),
        ("04_Current_Affairs_GK/Monthly_Digests_2026/2026-04_April.md", ["P1-S1.1", "P1-S1.2", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]),
        ("04_Current_Affairs_GK/Monthly_Digests_2026/2026-05_May.md", ["P1-S1.1", "P1-S1.2", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]),
        ("04_Current_Affairs_GK/Monthly_Digests_2026/2026-06_June.md", ["P1-S1.1", "P1-S1.2", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]),
        ("04_Current_Affairs_GK/Monthly_Digests_2026/2026-07_July.md", ["P1-S1.1", "P1-S1.2", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]),
        ("04_Current_Affairs_GK/Monthly_Digests_2026/2026-08_August.md", ["P1-S1.1", "P1-S1.2", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]),
        ("04_Current_Affairs_GK/Monthly_Digests_2026/2026-09_September.md", ["P1-S1.1", "P1-S1.2", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]),
        ("04_Current_Affairs_GK/Monthly_Digests_2026/2026-10_October.md", ["P1-S1.1", "P1-S1.2", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"])
    ]

    for rel_path, refs in files_to_fix:
        full_path = os.path.join(ROOT_DIR, rel_path.replace("/", os.sep))
        if not os.path.exists(full_path):
            print(f"Skipping missing file: {rel_path}")
            continue
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if syllabus_lines exists
        refs_str = "[" + ", ".join(refs) + "]"
        if "syllabus_lines:" in content:
            content = re.sub(r'syllabus_lines:\s*\[.*?\]', f'syllabus_refs: {refs_str}\nsyllabus_refs_partial: []', content)
        elif "syllabus_refs:" in content:
            content = re.sub(r'syllabus_refs:\s*\[.*?\]', f'syllabus_refs: {refs_str}', content)
        else:
            # Insert before the second ---
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = parts[1]
                fm = fm.rstrip() + f"\nsyllabus_refs: {refs_str}\nsyllabus_refs_partial: []\n"
                content = "---" + fm + "---" + parts[2]

        safe_write(full_path, content)
        print(f"Updated frontmatter: {rel_path}")

def fix_notes_links():
    print("--- Fixing Broken Internal Links in Notes ---")
    ir_note = os.path.join(ROOT_DIR, "03_Notes", "04_Polity_Governance_and_Public_Administration", "India_Foreign_Policy_and_IR.md")
    if os.path.exists(ir_note):
        with open(ir_note, "r", encoding="utf-8") as f:
            txt = f.read()
        txt = txt.replace("[[National_Current_Affairs]]", "[[2026-10_October]]")
        safe_write(ir_note, txt)
        print("Updated India_Foreign_Policy_and_IR.md link")

def fix_start_here():
    print("--- Updating 00_START_HERE.md ---")
    start_here = os.path.join(ROOT_DIR, "00_START_HERE.md")
    with open(start_here, "r", encoding="utf-8") as f:
        txt = f.read()

    # Fix json wikilinks
    txt = txt.replace("[[02_Syllabus_and_Pattern/exam_config.json]]", "[exam_config.json](02_Syllabus_and_Pattern/exam_config.json)")
    txt = txt.replace("[[02_Syllabus_and_Pattern/syllabus_lines.json]]", "[syllabus_lines.json](02_Syllabus_and_Pattern/syllabus_lines.json)")
    txt = txt.replace("[[05_Resources/Question_Bank/question_bank.json]]", "[question_bank.json](05_Resources/Question_Bank/question_bank.json)")

    # Fix Current affairs section in 00_START_HERE.md
    old_ca_sec = """### 2.3 Current Affairs & Flagship Schemes (`04_Current_Affairs_GK/`)
- [[04_Current_Affairs_GK/01_Monthly_Digests_2025_2026/National_Current_Affairs.md]]: 12-month national digest (BNS criminal laws, 106th amendment, Mission Divyastra, Bharat Ratna 2024).
- [[04_Current_Affairs_GK/01_Monthly_Digests_2025_2026/International_Current_Affairs.md]]: 12-month global digest (BRICS expansion, AU in G20, India-EFTA TEPA, IMEC corridor, COP28/29).
- [[04_Current_Affairs_GK/01_Monthly_Digests_2025_2026/Karnataka_Current_Affairs.md]]: State digest (Gig Workers Bill, Greater Bengaluru Bill, Yettinahole Phase-1, Hoysala UNESCO sites, Sahitya Sammelana).
- [[04_Current_Affairs_GK/02_Karnataka_State_Schemes_and_Policies/Karnataka_Flagship_Schemes.md]]: Consolidated guide to the Five Guarantees (Gruha Lakshmi, Gruha Jyothi, Yuva Nidhi, Shakti, Anna Bhagya)."""

    new_ca_sec = """### 2.3 Current Affairs & Flagship Schemes (`04_Current_Affairs_GK/`)
- [[04_Current_Affairs_GK/Monthly_Digests_2026/2026-10_October.md]]: October 2026 Master Digest (Nobel Prizes 2024, Ratan Tata legacy, RBI monetary stance, Mysuru Dasara, 16 categories).
- [[04_Current_Affairs_GK/Monthly_Digests_2026/2026-09_September.md]]: September 2026 Master Digest (Yettinahole Phase-1, Quad Summit Wilmington, Sub-classification verdict, Paris Paralympics).
- [[04_Current_Affairs_GK/Monthly_Digests_2026/2026-08_August.md]]: August 2026 Master Digest (Wayanad landslides geology, Greater Bengaluru Governance Bill, Unified Pension Scheme UPS).
- [[04_Current_Affairs_GK/Monthly_Digests_2026/2026-07_July.md]]: July 2026 Master Digest (Union Budget 2024-25, Economic Survey, Karnataka Gig Workers Bill, UNESCO World Heritage).
- [[04_Current_Affairs_GK/Monthly_Digests_2026/2026-06_June.md]]: June 2026 Master Digest (18th Lok Sabha formation, Cabinet committees, UGC-NET reforms, environmental summits).
- [[04_Current_Affairs_GK/Monthly_Digests_2026/2026-05_May.md]]: May 2026 Master Digest (General Elections 2024, Chabahar port agreement, RBI record dividend, heatwaves).
- [[04_Current_Affairs_GK/Monthly_Digests_2026/2026-04_April.md]]: April 2026 Master Digest (Supreme Court climate ruling Art 21/14, AFSPA updates, WTO dispute settlements).
- [[04_Current_Affairs_GK/Monthly_Digests_2026/2026-02_February.md]]: February 2026 Master Digest (Karnataka Budget 2024-25, Interim Union Budget, Bharat Ratna announcements, Five Guarantees).
- [[04_Current_Affairs_GK/02_Karnataka_State_Schemes_and_Policies/Karnataka_Flagship_Schemes.md]]: Consolidated guide to the Five Guarantees (Gruha Lakshmi, Gruha Jyothi, Yuva Nidhi, Shakti, Anna Bhagya)."""

    if old_ca_sec in txt:
        txt = txt.replace(old_ca_sec, new_ca_sec)
    else:
        # Fallback regex replacement
        txt = re.sub(r'### 2\.3 Current Affairs.*?(?=### 2\.4)', new_ca_sec + "\n\n", txt, flags=re.DOTALL)

    # Fix Mocks section in 00_START_HERE.md
    old_mock_sec = """### 2.5 Offline Interactive Mock Tests (`06_Mock_Tests/`)
- `Full_Prelims_P1_Mock1.html`: Full 100-question Paper 1 Mock (Current Events + Humanities).
- `Full_Prelims_P2_Mock1.html`: Full 100-question Paper 2 Mock (State Programmes + Science + Mental Ability).
- 5 Subject-wise drill mocks: Current Affairs, Humanities, Karnataka Affairs, Science & Environment, and General Mental Ability.
- [[06_Mock_Tests/README.md]]: Guide to taking the mocks offline in your browser."""

    new_mock_sec = """### 2.5 Computer-Based Test (CBT) Offline Mocks Suite (`06_Mock_Tests/`)
- 19 Standalone, zero-dependency CBT HTML examination simulators replicating KPSC/NTA online interfaces.
- **Full-Length Prelims Mocks**: 3 Full Paper 1 Mocks (300 Qs) + 3 Full Paper 2 Mocks (300 Qs).
- **Sectional Drills**: 6 Subject Mocks (300 Qs) covering History, Geography, Polity, Economy, Science/Environment, and GMA.
- **Monthly Current Affairs Mocks**: 9 Monthly CBT Mocks (Feb 2026 – Oct 2026, 225 Qs).
- **Authentic PYQ Master Mock**: 100-question KPSC KAS 2014–2020 verified question set.
- Detailed companion answer keys and rationale in `06_Mock_Tests/Markdown_Keys/`.
- [[06_Mock_Tests/README.md]]: Master Examination Directory and offline simulator instructions."""

    if old_mock_sec in txt:
        txt = txt.replace(old_mock_sec, new_mock_sec)
    else:
        txt = re.sub(r'### 2\.5 Offline Interactive Mock Tests.*?(?=\n\n---|\Z)', new_mock_sec, txt, flags=re.DOTALL)

    safe_write(start_here, txt)
    print("Updated 00_START_HERE.md")

def rebuild_markdown_keys():
    print("--- Rebuilding Companion Markdown Keys with 100% Valid Note Mappings ---")
    mocks_dir = os.path.join(ROOT_DIR, "06_Mock_Tests")
    keys_dir = os.path.join(mocks_dir, "Markdown_Keys")
    os.makedirs(keys_dir, exist_ok=True)

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

    cbt_files = sorted([f for f in os.listdir(mocks_dir) if f.startswith("CBT_") and f.endswith(".html")])
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
        html_path = os.path.join(mocks_dir, f)
        with open(html_path, "r", encoding="utf-8") as fl:
            content = fl.read()

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
        key_path = os.path.join(keys_dir, key_filename)

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

            # Resolve vault note reference
            raw_ref = q.get('vault_note', '')
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

    index_path = os.path.join(mocks_dir, "README.md")
    safe_write(index_path, index_md)
    print("Updated 06_Mock_Tests/README.md")

if __name__ == "__main__":
    fix_frontmatter()
    fix_notes_links()
    fix_start_here()
    rebuild_markdown_keys()
    print("=== All Lint & Frontmatter Fixes Applied Successfully ===")
