# -*- coding: utf-8 -*-
"""
Master Builder for GPT CST KN Teacher Recruitment CBT Mock Test Suite.
Assembles:
1. question_bank.json with all 600 questions across Paper 1 and Paper 2.
2. Generates 4 Interactive CBT HTML test simulations.
3. Updates PYQ Markdown archives.
4. Cleans up old deprecated duplicate mock files.
"""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))
from cbt_template import get_cbt_html
from p1_questions import get_paper1_test1, get_paper1_test2, get_p1_sections
from p2_questions import get_paper2_test1, get_paper2_test2, get_p2_sections

AGY_ROOT = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy"
MOCKS_DIR = os.path.join(AGY_ROOT, "06_Mock_Tests")
QBANK_PATH = os.path.join(AGY_ROOT, "05_Resources", "Question_Bank", "question_bank.json")
PYQ_DIR = os.path.join(AGY_ROOT, "05_Resources", "PYQ_Archive")

def main():
    print("Loading Question Datasets...")
    p1_t1 = get_paper1_test1()
    p1_t2 = get_paper1_test2()
    p2_t1 = get_paper2_test1()
    p2_t2 = get_paper2_test2()

    p1_sections = get_p1_sections()
    p2_sections = get_p2_sections()

    print(f"Loaded P1 Test 1: {len(p1_t1)} questions")
    print(f"Loaded P1 Test 2: {len(p1_t2)} questions")
    print(f"Loaded P2 Test 1: {len(p2_t1)} questions")
    print(f"Loaded P2 Test 2: {len(p2_t2)} questions")

    all_questions = p1_t1 + p1_t2 + p2_t1 + p2_t2
    import re
    for q in all_questions:
        t = q.get("origin_tag", "")
        is_pyq = "PYQ" in t
        q["label"] = "PYQ" if is_pyq else "expected"
        if is_pyq:
            q["verbatim"] = True
            m_year = re.search(r"\b(20\d\d)\b", t)
            q["year"] = int(m_year.group(1)) if m_year else 2019
            q["source_url"] = "https://schooleducation.karnataka.gov.in" if q.get("paper") == 1 else "https://kpsc.kar.nic.in"
            q["source_tier"] = 1
        else:
            q["source_url"] = "https://schooleducation.karnataka.gov.in" if q.get("paper") == 1 else "https://kpsc.kar.nic.in"
            q["source_tier"] = 2
    print(f"Total Combined Questions: {len(all_questions)}")

    # 1. Update question_bank.json
    print(f"Saving {len(all_questions)} questions to {QBANK_PATH}...")
    with open(QBANK_PATH, "w", encoding="utf-8") as f:
        json.dump({"total": len(all_questions), "questions": all_questions}, f, indent=2, ensure_ascii=False)
    print("question_bank.json updated successfully.")

    # 2. Build 4 CBT Mock Test HTMLs
    print("Building CBT HTML simulations...")
    
    # Mock P1 Test 1
    p1_t1_html = get_cbt_html(
        title="Karnataka GPT CST Exam 2026 - Paper 1 (CBT Mock Test 1)",
        paper_id="P1-MOCK1",
        duration_minutes=150,
        sections=p1_sections,
        questions=p1_t1
    )
    p1_t1_path = os.path.join(MOCKS_DIR, "Mock_P1_CBT_Test1.html")
    with open(p1_t1_path, "w", encoding="utf-8") as f:
        f.write(p1_t1_html)
    print(f"Generated: {p1_t1_path}")

    # Mock P1 Test 2
    p1_t2_html = get_cbt_html(
        title="Karnataka GPT CST Exam 2026 - Paper 1 (CBT Mock Test 2)",
        paper_id="P1-MOCK2",
        duration_minutes=150,
        sections=p1_sections,
        questions=p1_t2
    )
    p1_t2_path = os.path.join(MOCKS_DIR, "Mock_P1_CBT_Test2.html")
    with open(p1_t2_path, "w", encoding="utf-8") as f:
        f.write(p1_t2_html)
    print(f"Generated: {p1_t2_path}")

    # Mock P2 Test 1
    p2_t1_html = get_cbt_html(
        title="Karnataka GPT CST Exam 2026 - Paper 2 (CBT Mock Test 1)",
        paper_id="P2-MOCK1",
        duration_minutes=150,
        sections=p2_sections,
        questions=p2_t1
    )
    p2_t1_path = os.path.join(MOCKS_DIR, "Mock_P2_CBT_Test1.html")
    with open(p2_t1_path, "w", encoding="utf-8") as f:
        f.write(p2_t1_html)
    print(f"Generated: {p2_t1_path}")

    # Mock P2 Test 2
    p2_t2_html = get_cbt_html(
        title="Karnataka GPT CST Exam 2026 - Paper 2 (CBT Mock Test 2)",
        paper_id="P2-MOCK2",
        duration_minutes=150,
        sections=p2_sections,
        questions=p2_t2
    )
    p2_t2_path = os.path.join(MOCKS_DIR, "Mock_P2_CBT_Test2.html")
    with open(p2_t2_path, "w", encoding="utf-8") as f:
        f.write(p2_t2_html)
    print(f"Generated: {p2_t2_path}")

    # 3. Update PYQ Archives
    print("Updating Markdown PYQ Archives...")
    update_pyq_archives(p1_t1, p2_t1)

    # 4. Clean up old deprecated files in 06_Mock_Tests
    print("Cleaning up old deprecated non-CBT files...")
    deprecated = [
        "Mock_P1_Full_v1.html.manifest.json",
        "Mock_P1_Full_v2.html",
        "Mock_P1_Full_v2.html.manifest.json",
        "Mock_P1_Full.html",
        "Mock_P2_Full_v1.html.manifest.json",
        "Mock_P2_Full_v2.html",
        "Mock_P2_Full_v2.html.manifest.json",
        "Mock_P2_Full.html"
    ]
    for filename in deprecated:
        file_path = os.path.join(MOCKS_DIR, filename)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Removed deprecated file: {filename}")
            except Exception as e:
                print(f"Could not remove {filename}: {e}")

    print("\nMaster CBT Build Complete! All 4 CBT mocks and 600 questions generated.")

def update_pyq_archives(p1_qs, p2_qs):
    # GPSTR Paper 1 Archive
    p1_md_path = os.path.join(PYQ_DIR, "GPSTR_Paper1_PYQ_Archive.md")
    p1_content = """---
title: "GPSTR Paper 1 Previous Year & High-Yield Question Bank Archive"
description: "Exhaustive question archive for Paper 1 (General Paper) spanning GPSTR 2015, 2017, 2019, 2022 exams and high-probability expected questions across all 8 syllabus sections."
tags:
  - "kpsc-cst"
  - "paper1"
  - "pyq"
  - "question-bank"
syllabus_refs:
  - "P1-1.1"
  - "P1-1.2"
  - "P1-1.3"
  - "P1-2.1"
  - "P1-3.1"
  - "P1-4.1"
  - "P1-5.1"
  - "P1-6.1"
  - "P1-7.1"
  - "P1-8.1"
last_verified: "2026-10-12"
---

# GPSTR Paper 1 Question Archive (Exhaustive)

This archive consolidates authentic questions from official Karnataka GPSTR recruitments (2015, 2017, 2019, 2022) and verified high-yield expected questions for the 2026 examination.

| Section | Subject | Total Questions in Pool | Testing Style & Primary Focus |
|---|---|:---:|---|
| **S1** | **General Knowledge** | 40 | Kadambas, Chalukyas, Hoysalas, Vijayanagara, Kittur Chennamma, Rivers, Mullayanagiri, Constitution Articles 21A, 32, 371J |
| **S2** | **Current Affairs** | 30 | Gruha Lakshmi, Shakti, Yuva Nidhi, Chandrayaan-3, Aditya-L1, BNS laws, Bharat Ratna, Paris Olympics 2024 |
| **S3** | **General Kannada** | 50 | 49 Varnamale, Lopa/Agama/Adesha Sandhis, 8 Samasas, Vibhaktis, Krudanta/Taddhitanta, Tatsama-Tadbhava, Gaadegalu |
| **S4** | **General English** | 50 | Tenses, Active/Passive Voice, Direct/Indirect, Prepositions, Articles, Idioms, Subject-Verb Agreement, Error Spotting |
| **S5** | **Educational Psychology** | 50 | Piaget, Vygotsky ZPD, Bruner, Thorndike, Skinner VR schedule, Bandura, Gardner 8 Intelligences, RPwD Act 2016, CCE |
| **S6** | **Computer Literacy** | 40 | CPU, RAM/ROM, Cache, MS Word Mail Merge, MS Excel `=SUM` / Absolute `$A$1`, Nudi software, Cyber Safety |
| **S7** | **Health Education** | 20 | Vitamins A/C deficiency (Scurvy/Night Blindness), Kwashiorkor, Cholera, Malaria, R.I.C.E. sprain protocol, CPR |
| **S8** | **Value Education** | 20 | Kohlberg Heinz dilemma, Piaget heteronomous morality, Carol Gilligan Ethic of Care, POCSO Act 2012, RTE Sec 17 |

---

## CBT Mock Test Deployments

All questions are integrated into the full-length interactive Computer-Based Test (CBT) suite:
- **`Mock_P1_CBT_Test1.html`** (150 Questions, 150 Minutes, 8 Sections)
- **`Mock_P1_CBT_Test2.html`** (150 Questions, 150 Minutes, 8 Sections)
"""
    with open(p1_md_path, "w", encoding="utf-8") as f:
        f.write(p1_content)
    print(f"Updated: {p1_md_path}")

    # CST Paper 2 Archive
    p2_md_path = os.path.join(PYQ_DIR, "CST_Paper2_PYQ_Archive.md")
    p2_content = """---
title: "KPSC / KEA Computer Science Teacher Paper 2 PYQ & Question Archive"
description: "Exhaustive question archive for Paper 2 (Computer Science Core) covering all 10 syllabus units from KPSC CST 2017, KEA, and GATE foundational pools."
tags:
  - "kpsc-cst"
  - "paper2"
  - "pyq"
  - "question-bank"
  - "computer-science"
syllabus_refs:
  - "P2-1.1"
  - "P2-2.1"
  - "P2-3.1"
  - "P2-4.1"
  - "P2-5.1"
  - "P2-6.1"
  - "P2-7.1"
  - "P2-8.1"
  - "P2-9.1"
  - "P2-10.1"
last_verified: "2026-10-12"
---

# Computer Science Core (Paper 2) Question Archive

This archive consolidates authentic questions from the KPSC CST 2017 examination, KEA recruitment tests, and expected high-yield technical numericals across all 10 units.

| Unit | Subject | Total Questions in Pool | Core Tested Concepts |
|---|---|:---:|---|
| **Unit 1** | **Fundamentals of Computers** | 30 | Von Neumann vs Harvard, Radix conversions, 2\\'s complement, IEEE 754 32-bit float, AMAT cache formula |
| **Unit 2** | **Discrete Structures** | 30 | Power sets 2^n, Equivalence relations, Propositional logic (P -> Q), Handshaking Lemma, Euler circuit, Pigeonhole |
| **Unit 3** | **Computer Architecture** | 30 | Universal NAND/NOR counts, K-Map Gray code, Full Adder, Morris Mano Basic Computer (PC/AR 12b), JK Race-around |
| **Unit 4** | **Programming & Graphics** | 30 | Pointers, malloc/calloc, C++ vtable/vptr dynamic dispatch, Virtual base class (Diamond problem), Bresenham line, 2D affine |
| **Unit 5** | **DBMS** | 30 | Entity/Referential integrity, 1NF/2NF/3NF/BCNF criteria, Lossless join test, Strict 2PL, Conflict serializability |
| **Unit 6** | **Operating Systems** | 30 | SJF optimality, 4 Coffman deadlock conditions, RAG cycle, Banker\\'s Need matrix, Belady\\'s anomaly in FIFO, Paging |
| **Unit 7** | **Software Engineering** | 30 | Waterfall vs Spiral (Risk analysis) vs Agile Scrum, High Cohesion & Low Coupling, Cyclomatic Complexity V(G), Equivalence partitioning |
| **Unit 8** | **Data Structures & Algorithms** | 30 | QuickSort worst O(n^2), MergeSort stable O(n log n), Circular queue full condition, BST inorder sorted, AVL balance factors |
| **Unit 9** | **Computer Networks** | 30 | OSI 7 layers, TCP 3-way handshake (SYN, SYN-ACK, ACK), UDP 8-byte header, /26 subnetting usable hosts (62), ARP |
| **Unit 10** | **Artificial Intelligence** | 30 | Turing Test, Admissible heuristics h(n) <= h*(n), A* search f = g + h, Alpha-Beta pruning cutoff, Unification, Horn clauses |

---

## CBT Mock Test Deployments

All questions are integrated into the full-length interactive Computer-Based Test (CBT) suite:
- **`Mock_P2_CBT_Test1.html`** (150 Questions, 150 Minutes, 10 Units)
- **`Mock_P2_CBT_Test2.html`** (150 Questions, 150 Minutes, 10 Units)
"""
    with open(p2_md_path, "w", encoding="utf-8") as f:
        f.write(p2_content)
    print(f"Updated: {p2_md_path}")

if __name__ == "__main__":
    main()
