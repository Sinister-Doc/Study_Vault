"""
Phase 7 & 8: Interactive Offline Mock Test Generation and 14-Day Study Plan
Enforces canonical OUTPUT_ROOT boundary guard:
OUTPUT_ROOT = D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy
"""

import os
import sys
import datetime
import subprocess
from pathlib import Path

# Paths
OUTPUT_ROOT = Path(r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy").resolve()
WORKSPACE_ROOT = Path(r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep").resolve()
MOCK_DIR = OUTPUT_ROOT / "06_Mock_Tests"
RUN_DIR = OUTPUT_ROOT / "_run"
ACTIONS_LOG = RUN_DIR / "actions.log"

EXAMKIT_PY = Path(r"C:\Users\supre\.gemini\config\skills\exam-primer\scripts\examkit.py")
PYTHON_EXE = Path(r"D:\Softwares\pyenv\Scripts\python.exe")

def log_action(msg: str):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    try:
        RUN_DIR.mkdir(parents=True, exist_ok=True)
        with open(ACTIONS_LOG, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
    except Exception as e:
        print(f"[LOG ERROR] {e}")

def is_canonical_subpath(target: Path, root: Path) -> bool:
    try:
        resolved_target = target.resolve()
        resolved_root = root.resolve()
        common = os.path.commonpath([str(resolved_target), str(resolved_root)])
        return os.path.normcase(common) == os.path.normcase(str(resolved_root))
    except Exception:
        return False

def safe_write_text(target_path: Path, content: str, encoding="utf-8") -> bool:
    target_resolved = target_path.resolve()
    if not is_canonical_subpath(target_resolved, OUTPUT_ROOT):
        log_action(f"[GUARD REJECTED] Write attempt outside OUTPUT_ROOT: {target_resolved}")
        return False
    
    final_path = target_resolved
    if final_path.exists():
        base = final_path.stem
        ext = final_path.suffix
        v2_path = final_path.with_name(f"{base}-v2{ext}")
        if v2_path.exists():
            log_action(f"[SKIP] Target already exists: {final_path}")
            return True
        final_path = v2_path

    final_path.parent.mkdir(parents=True, exist_ok=True)
    final_path.write_text(content, encoding=encoding)
    log_action(f"[FILE WRITE] {final_path}")
    return True

def run_cmd(cmd, desc=""):
    cmd_str = ' '.join(str(c) for c in cmd)
    log_action(f"[COMMAND RUN] {desc}: {cmd_str}")
    res = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, cwd=str(WORKSPACE_ROOT))
    if res.returncode != 0:
        log_action(f"[COMMAND WARN] {desc} returned {res.returncode}: {res.stderr.strip()}")
    else:
        log_action(f"[COMMAND SUCCESS] {desc}")
    return res

def main():
    log_action("=== STARTING STEP 5: Interactive Mocks and Study Plan Generation ===")
    MOCK_DIR.mkdir(parents=True, exist_ok=True)
    
    config_file = OUTPUT_ROOT / "02_Syllabus_and_Pattern" / "exam_config.json"
    bank_file = OUTPUT_ROOT / "05_Resources" / "Question_Bank" / "question_bank.json"

    mock_p1_out = MOCK_DIR / "Mock_P1_Full_v1.html"
    if mock_p1_out.exists():
        mock_p1_out = MOCK_DIR / "Mock_P1_Full_v2.html"

    mock_p2_out = MOCK_DIR / "Mock_P2_Full_v1.html"
    if mock_p2_out.exists():
        mock_p2_out = MOCK_DIR / "Mock_P2_Full_v2.html"

    # Build Full Paper 1 Mock
    run_cmd([
        PYTHON_EXE, EXAMKIT_PY, "build-mock",
        "--workspace", str(OUTPUT_ROOT),
        "--config", str(config_file),
        "--bank", str(bank_file),
        "--out", str(mock_p1_out),
        "--kind", "full",
        "--paper", "P1",
        "--mode", "omr-style",
        "--title", "Karnataka GPT CST 2026 - Paper 1 Full Mock Test",
        "--overwrite"
    ], desc="Build Full Paper 1 Mock")

    # Build Full Paper 2 Mock
    run_cmd([
        PYTHON_EXE, EXAMKIT_PY, "build-mock",
        "--workspace", str(OUTPUT_ROOT),
        "--config", str(config_file),
        "--bank", str(bank_file),
        "--out", str(mock_p2_out),
        "--kind", "full",
        "--paper", "P2",
        "--mode", "omr-style",
        "--title", "Karnataka GPT CST 2026 - Paper 2 (Computer Science Core) Full Mock Test",
        "--overwrite"
    ], desc="Build Full Paper 2 Mock")

    # Generate 00_START_HERE.md
    start_here = """# Karnataka GPT CST (Computer Science Teacher) Exam Study Vault

Welcome to your structured, source-verified Obsidian study vault for the **Karnataka Graduate Primary School Teachers Recruitment 2026 (GPT - CST 1 to 8)**, conducted by the Centralised Admission Cell (CAC), Department of School Education.

---

## 📌 Exam Facts at a Glance

| Item | Official Specification |
|---|---|
| **Conducting Authority** | Centralised Admission Cell (CAC), Department of School Education, Govt. of Karnataka |
| **Notification Reference** | Order No. EP 80 DPI 2026, dated 10.08.2026 |
| **Post Applied** | Computer Science Teacher (CST 1 to 8) - Residual Parent Cadre (Non-KK) |
| **Applied District** | Kodagu District |
| **Exam Pattern** | Paper 1 (General: 150 Marks, 150 mins) + Paper 2 (CST Core: 150 Marks, 150 mins) |
| **Mode of Exam** | OMR-based Objective Multiple Choice Examination |
| **Language** | Bilingual (English & Kannada) |

---

## 🗂️ Vault Navigation & Structure (Agy Isolated Root)

- [[01_Study_Plan]] : Day-by-day 14-day preparation, revision, and mock testing timetable.
- `Paper1/` : Complete notes for Paper 1 (General Knowledge, Kannada Grammar, General English, Educational Psychology, Computer Literacy, Health & Value Education).
- `Paper2/` : Complete notes for Paper 2 (10 Core Computer Science Units).
- `02_Syllabus_and_Pattern/` : Official notification extract, `exam_config.json`, and `syllabus_lines.json`.
- `05_Resources/` :
  - `Source_Registry.md` : Authoritative textbooks and official government sites.
  - `YouTube_Resources.md` : Curated video coursework mapped to syllabus line IDs.
  - `Question_Bank/` : Verbatim past exam questions and model MCQs.
  - `PYQ_Analysis.md` : Weightage and topic frequency trends.
- `06_Mock_Tests/` : Single-file offline interactive HTML mocks (opens in any browser with instant OMR scoring).
- `_run/` : Append-only actions log, run report, and open items.

---

## 🚀 Quick Launch
1. Open [[01_Study_Plan]] and check off completed daily targets.
2. Review [[Von_Neumann_and_Hardware_Architecture]] and [[Piaget_and_Cognitive_Development]].
3. Practice interactive mocks in `06_Mock_Tests/Mock_P1_Full_v1.html` and `06_Mock_Tests/Mock_P2_Full_v1.html`.
"""
    safe_write_text(OUTPUT_ROOT / "00_START_HERE.md", start_here)

    # Generate 01_Study_Plan.md
    study_plan = """# 14-Day Structured Study Plan: Karnataka GPT CST Recruitment

> **Candidate Background:** B.E. in Electronics & Communication Engineering (ECE, VTU 2023).
> **Strategic Focus:** Front-load Paper 2 CS core units (engineering strength), dedicate deep focus to Paper 1 non-engineering sections (Educational Psychology, Kannada Grammar, Value Education), and finish with mock testing and revision.

---

## Week 1: Paper 2 (Computer Science Core Focus)

- [ ] **Day 1: Fundamentals of Computers & Hardware**
  - Read: [[Von_Neumann_and_Hardware_Architecture]]
  - Watch: Statecraft IAS Academy [Unit 01 Fundamentals (41m)](https://youtu.be/OvboDQ1Fi44)
  - Tasks: System bus, Motherboard North/Southbridge, Register transfer (PC, IR, MAR, MBR).
- [ ] **Day 2: Discrete Structures Part 1 (Logic & Sets)**
  - Read: [[Propositional_Logic_and_Truth_Tables]]
  - Watch: Gate Smashers [Propositional Logic & Truth Tables (18m)](https://youtu.be/yl_V_C0g2jM)
  - Tasks: Conditional equivalences, Contrapositive, De Morgan's laws, Tautologies.
- [ ] **Day 3: Computer System Architecture & Digital Logic**
  - Read: [[Digital_Logic_and_Combinational_Circuits]]
  - Watch: Dr. Gururaj Bulbule, Sadhana Academy [Logic Gates (25m)](https://youtu.be/kodEefWzx5s)
  - Tasks: Universal gates (NAND/NOR counts), 4:16 decoder expansions, Multiplexers.
- [ ] **Day 4: Programming Languages (C, C++, OOP) & Web Basics**
  - Tasks: Pointers, Dynamic Memory, Virtual functions, Polymorphism, HTML/CSS DOM.
- [ ] **Day 5: Database Management Systems (DBMS)**
  - Read: [[Relational_Model_and_Normalization]]
  - Watch: Gate Smashers [DBMS Normalization 1NF to BCNF (24m)](https://youtu.be/5fs1PR851bc)
  - Tasks: Candidate keys, Functional dependency closure, 3NF vs BCNF.
- [ ] **Day 6: Operating Systems**
  - Read: [[Process_Scheduling_and_Deadlocks]]
  - Watch: Knowledge Gate [CPU Scheduling Algorithms (32m)](https://youtu.be/ewCw_G_zX_w)
  - Tasks: FCFS vs SJF, Round Robin time quantum, 4 Coffman deadlock conditions.
- [ ] **Day 7: Software Engineering & Data Structures Review**
  - Tasks: Agile Scrum sprints, Cyclomatic complexity ($V(G) = E - N + 2$), QuickSort $O(n^2)$ worst case.
  - Review: Flashcard self-test on Paper 2 Units 1-7.

---

## Week 2: Paper 1 & Integrated Mock Practice

- [ ] **Day 8: Computer Networks & Communication**
  - Tasks: OSI 7-layer architecture, IPv4 CIDR subnetting calculations, TCP 3-way handshake.
- [ ] **Day 9: Artificial Intelligence & Paper 1 Computer Literacy**
  - Read: [[Office_Tools_and_Nudi_Typing]]
  - Watch: Teacher's Academy [Computer Literacy Scoring Guide (42m)](https://youtu.be/RAAi5WtSJDo)
  - Tasks: A* search admissibility ($h(n) \le h^*(n)$), Nudi typing Scroll Lock toggle.
- [ ] **Day 10: Educational Psychology (Heaviest Non-CS Area)**
  - Read: [[Piaget_and_Cognitive_Development]]
  - Watch: Shrishail Sir, Payana Academy [Educational Psychology Marathon (2h 45m)](https://youtu.be/VxWM_ZAkkHc)
  - Tasks: Piaget's 4 stages, Vygotsky's ZPD, Skinner's operant conditioning, Maslow's hierarchy.
- [ ] **Day 11: General Kannada Grammar & General English**
  - Read: [[Kannada_Grammar_Sandhi_and_Samasa]]
  - Watch: Chethana Academy [Complete Kannada Grammar (4h 12m)](https://youtu.be/lHAV0r6sHVY)
  - Tasks: ಆದೇಶ ಸಂಧಿ, ಗಮಕ ಸಮಾಸ, Active/Passive voice, Reported speech.
- [ ] **Day 12: General Knowledge (History, Geography, Constitution)**
  - Watch: Classic Education [Indian Constitution Revision (3h 50m)](https://youtu.be/CyQmNKsjisw)
  - Tasks: Article 21A, Halmidi inscription (Kadambas), Cauvery and Krishna river basins.
- [ ] **Day 13: Current Affairs, Health & Value Education**
  - Tasks: Communicable vs non-communicable diseases, Vitamin C (Scurvy), Utilitarian ethics.
- [ ] **Day 14: Full-Length Mock Exams & Mistake Sweep**
  - [ ] Take Full Paper 1 Mock: `06_Mock_Tests/Mock_P1_Full_v1.html`
  - [ ] Take Full Paper 2 Mock: `06_Mock_Tests/Mock_P2_Full_v1.html`
  - [ ] Analyze mistakes using instant OMR score reports; revise weak spots.
"""
    safe_write_text(OUTPUT_ROOT / "01_Study_Plan.md", study_plan)
    log_action("=== STEP 5 FINISHED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
