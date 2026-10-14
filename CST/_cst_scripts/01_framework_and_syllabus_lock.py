"""
Phase 1 & 2 Setup: Framework Extraction, Directory Scaffolding & Syllabus Lock
Enforces canonical OUTPUT_ROOT boundary guard:
OUTPUT_ROOT = D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy
"""

import os
import sys
import json
import datetime
import subprocess
from pathlib import Path

# Paths
OUTPUT_ROOT = Path(r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy").resolve()
WORKSPACE_ROOT = Path(r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep").resolve()
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
    log_action("=== STARTING STEP 1: Framework & Syllabus Lock ===")
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    RUN_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Initialize scaffold inside OUTPUT_ROOT using examkit.py
    run_cmd([
        PYTHON_EXE, EXAMKIT_PY, "init",
        "--workspace", str(OUTPUT_ROOT),
        "--kind", "prep",
        "--exam", "Karnataka GPT CST Recruitment 2026",
        "--overwrite"
    ], desc="examkit init scaffold in OUTPUT_ROOT")

    # Ensure Paper1 and Paper2 folders exist under OUTPUT_ROOT
    p1_subdirs = [
        "01_General_Knowledge", "02_Current_Affairs", "03_General_Kannada",
        "04_General_English", "05_Educational_Psychology", "06_Computer_Literacy",
        "07_Health_Education", "08_Value_Education", "Resources"
    ]
    for d in p1_subdirs:
        (OUTPUT_ROOT / "Paper1" / d).mkdir(parents=True, exist_ok=True)
        
    p2_subdirs = [
        "Unit01_Fundamentals_of_Computers", "Unit02_Discrete_Structures",
        "Unit03_Computer_Architecture", "Unit04_Programming_and_Graphics",
        "Unit05_DBMS", "Unit06_Operating_Systems", "Unit07_Software_Engineering",
        "Unit08_Data_Structures_and_Algorithms", "Unit09_Networks_and_Communication",
        "Unit10_Artificial_Intelligence", "Resources"
    ]
    for d in p2_subdirs:
        (OUTPUT_ROOT / "Paper2" / d).mkdir(parents=True, exist_ok=True)

    syllabus_dir = OUTPUT_ROOT / "02_Syllabus_and_Pattern"
    raw_syl_dir = syllabus_dir / "Raw_Syllabus"

    # 2. Extract Raw Notification Facts (strictly omitting PII)
    raw_notification_extract = """# Official Notification Excerpts - Karnataka Teachers' Recruitment 2026

**Conducting Authority:** Centralised Admission Cell (CAC / ಕೇಂದ್ರೀಕೃತ ದಾಖಲಾತಿ ಘಟಕ), Department of School Education, Bengaluru.
**Notification Order No:** EP 80 DPI 2026 (ಇಪಿ 80 ಡಿಪಿಐ 2026), dated 10.08.2026.
**Official Website:** https://schooleducation.karnataka.gov.in

## Key Dates:
- Notification Published: 10.08.2026
- Application Start: 18.08.2026
- Application End: 07.09.2026

## Post Details:
- Cadre: Graduate Primary School Teacher - Computer Science Teacher (GPT - CST 1 to 8 / ಗಣಕ ವಿಜ್ಞಾನ ಶಿಕ್ಷಕರು 1 ರಿಂದ 8ನೇ ತರಗತಿ).
- Cadre Split: 80% Local Cadre (Kalyana Karnataka / KK), 20% Residual Parent Cadre (RPC / Non-KK), 8% Bengaluru Urban/Rural state cadre.
- Mode of Examination: Competitive Written Examination (OMR-based objective multiple choice).

## Candidate Eligibility Context (De-identified):
- Post: Computer Science Teacher (RPC / Non-KK)
- Applied District: KODAGU District
- Qualification: B.E. in Electronics & Communication Engineering (ECE), VTU Belagavi, 2023.
"""
    safe_write_text(raw_syl_dir / "official_notification_extract.md", raw_notification_extract)

    # 3. Create exam_config.json
    exam_config = {
        "exam": "Karnataka GPT CST Teacher Recruitment 2026",
        "body": "Centralised Admission Cell (CAC), Department of School Education, Government of Karnataka",
        "notification": {
            "name": "Karnataka Education Department Services (Public Instruction Department) (Special Recruitment) Rules, 2026 - EP 80 DPI 2026",
            "date": "2026-08-10",
            "url": "https://schooleducation.karnataka.gov.in"
        },
        "format": "omr-style",
        "languages": ["English", "Kannada"],
        "alt_language": "kn",
        "dropped_policy": "award_all",
        "multiple": "wrong",
        "papers": [
            {
                "id": "P1",
                "name": "Paper 1 - General Paper",
                "duration_min": 150,
                "qualifying": "Minimum 50% aggregate (45% for SC/ST/Cat-I/PH)",
                "sections": [
                    {"id": "S1", "name": "General Knowledge", "subject": "General Knowledge", "questions": 20, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S2", "name": "Current Affairs", "subject": "Current Affairs", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S3", "name": "General Kannada", "subject": "General Kannada", "questions": 25, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S4", "name": "General English", "subject": "General English", "questions": 25, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S5", "name": "Educational Psychology", "subject": "Educational Psychology", "questions": 25, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S6", "name": "Computer Literacy", "subject": "Computer Literacy", "questions": 20, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S7", "name": "Health Education", "subject": "Health Education", "questions": 10, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S8", "name": "Value Education", "subject": "Value Education", "questions": 10, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"}
                ]
            },
            {
                "id": "P2",
                "name": "Paper 2 - Computer Science Core",
                "duration_min": 150,
                "qualifying": "Minimum 50% aggregate (45% for SC/ST/Cat-I/PH)",
                "sections": [
                    {"id": "S1", "name": "Unit 1: Fundamentals of Computers", "subject": "Fundamentals of Computers", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S2", "name": "Unit 2: Discrete Structures and Optimization", "subject": "Discrete Structures", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S3", "name": "Unit 3: Computer System Architecture", "subject": "Computer Architecture", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S4", "name": "Unit 4: Programming Languages and Computer Graphics", "subject": "Programming and Graphics", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S5", "name": "Unit 5: Database Management Systems", "subject": "DBMS", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S6", "name": "Unit 6: System Software and Operating Systems", "subject": "Operating Systems", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S7", "name": "Unit 7: Software Engineering", "subject": "Software Engineering", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S8", "name": "Unit 8: Data Structures and Algorithms", "subject": "Data Structures and Algorithms", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S9", "name": "Unit 9: Data Communication and Computer Networks", "subject": "Computer Networks", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"},
                    {"id": "S10", "name": "Unit 10: Artificial Intelligence", "subject": "Artificial Intelligence", "questions": 15, "marks_correct": 1, "negative": "0.25", "blank": 0, "multiple": "wrong"}
                ]
            }
        ]
    }
    config_path = syllabus_dir / "exam_config.json"
    safe_write_text(config_path, json.dumps(exam_config, indent=2))

    # 4. Create syllabus_lines.json
    lines = []
    
    # Paper 1 Lines
    p1_items = [
        ("P1-1.1", "P1", "General Knowledge", "Indian and Karnataka History", "Ancient, medieval, modern history and Karnataka culture/art", "high"),
        ("P1-1.2", "P1", "General Knowledge", "Geography", "Physical geography, rivers, natural resources, crops, population", "high"),
        ("P1-1.3", "P1", "General Knowledge", "Indian Constitution", "Preamble, Fundamental Rights, Directive Principles, Executive, Judiciary", "high"),
        ("P1-1.4", "P1", "General Knowledge", "Indian Economy", "Key economic indicators, public undertakings, planning, 5-year plans", "medium"),
        ("P1-1.5", "P1", "General Knowledge", "General Science", "Everyday physics, chemistry, biology, scientific inventions and discoveries", "medium"),
        ("P1-2.1", "P1", "Current Affairs", "National and International Affairs", "Key national events, international summits, treaties, Bilateral relations", "high"),
        ("P1-2.2", "P1", "Current Affairs", "State Government Schemes", "Karnataka state developmental schemes, welfare initiatives, budget highlights", "high"),
        ("P1-2.3", "P1", "Current Affairs", "Awards, Honours and Sports", "Nobel prizes, Jnanpith, Bharat Ratna, Olympic/national sports records", "medium"),
        ("P1-3.1", "P1", "General Kannada", "Vyakarna - Varnamale, Sandhi, Samasa", "ಕನ್ನಡ ವರ್ಣಮಾಲೆ, ಸಂಧಿಗಳು, ಸಮಾಸಗಳು, ವಿಭಕ್ತಿ ಪ್ರತ್ಯಯಗಳು", "high"),
        ("P1-3.2", "P1", "General Kannada", "Vocabulary & Idioms", "ಸಮಾನಾರ್ಥಕ, ವಿರುದ್ಧಾರ್ಥಕ, ನಾಣ್ಣುಡಿಗಳು, ಗಾದೆ ಮಾತುಗಳು", "high"),
        ("P1-3.3", "P1", "General Kannada", "Sahitya Charitre", "ಹಳಗನ್ನಡ ಮತ್ತು ಹೊಸಗನ್ನಡ ಸಾಹಿತ್ಯ ಚರಿತ್ರೆ, ಪ್ರಮುಖ ಕವಿಗಳು ಮತ್ತು ಕೃತಿಗಳು", "medium"),
        ("P1-4.1", "P1", "General English", "Grammar & Parts of Speech", "Nouns, pronouns, verbs, tenses, active/passive voice, reported speech", "high"),
        ("P1-4.2", "P1", "General English", "Vocabulary & Comprehension", "Synonyms, antonyms, idioms, phrasal verbs, unseen reading comprehension", "high"),
        ("P1-5.1", "P1", "Educational Psychology", "Growth & Development", "Stages of development, physical, cognitive, emotional, social changes", "high"),
        ("P1-5.2", "P1", "Educational Psychology", "Learning Theories", "Pavlov, Skinner, Thorndike, Piaget, Vygotsky, Bruner, Kohler", "high"),
        ("P1-5.3", "P1", "Educational Psychology", "Intelligence & Motivation", "Theories of intelligence (Spearman, Gardner), Maslow's hierarchy, motivation", "high"),
        ("P1-5.4", "P1", "Educational Psychology", "Personality & Mental Health", "Freud's psychoanalysis, adjustment mechanisms, stress, defense mechanisms", "medium"),
        ("P1-6.1", "P1", "Computer Literacy", "Basics of Computer Systems", "Hardware, software, operating systems (Windows, Linux), memory hierarchy", "high"),
        ("P1-6.2", "P1", "Computer Literacy", "Office & Kannada Typing Tools", "MS Word, Excel formulas, PowerPoint, Google Workspace, Nudi & Baraha fonts", "high"),
        ("P1-6.3", "P1", "Computer Literacy", "Internet & Cyber Security", "Browsers, search engines, cybersecurity threats, malware, IT Act overview", "medium"),
        ("P1-7.1", "P1", "Health Education", "Health & Hygiene", "Communicable/non-communicable diseases, nutrition, yoga, first aid", "medium"),
        ("P1-8.1", "P1", "Value Education", "Moral & Social Values", "Universal, national, moral values, human rights, value integration in teaching", "medium"),
    ]
    for pid, pap, subj, unit, text, prio in p1_items:
        lines.append({
            "id": pid, "paper": pap, "subject": subj, "unit": unit, "topic": unit, "text": text, "priority": prio
        })

    # Paper 2 Lines
    p2_items = [
        ("P2-1.1", "P2", "Fundamentals of Computers", "Architecture & Evolution", "Functional components, Von Neumann architecture, computer generations, classification", "high"),
        ("P2-1.2", "P2", "Fundamentals of Computers", "Hardware & Assembly", "Motherboard components, BIOS, CMOS, memory hierarchy, system bus, PC assembly", "high"),
        ("P2-2.1", "P2", "Discrete Structures", "Mathematical Logic & Sets", "Propositional & predicate logic, truth tables, normal forms, set relations, functions", "high"),
        ("P2-2.2", "P2", "Discrete Structures", "Graph Theory & Combinatorics", "Euler/Hamiltonian paths, planar graphs, trees, pigeonhole principle, recurrence relations", "high"),
        ("P2-2.3", "P2", "Discrete Structures", "Boolean Algebra", "Boolean functions, canonical forms, Karnaugh maps, minimization", "high"),
        ("P2-3.1", "P2", "Computer Architecture", "Digital Logic", "Logic gates, combinational circuits, multiplexers, decoders, sequential circuits, flip-flops, counters", "high"),
        ("P2-3.2", "P2", "Computer Architecture", "CPU & Instruction Formats", "Register transfer, instruction cycle, addressing modes, RISC vs CISC", "high"),
        ("P2-3.3", "P2", "Computer Architecture", "Memory & I/O", "Cache mapping techniques, virtual memory, paging, DMA, interrupts, bus arbitration", "high"),
        ("P2-4.1", "P2", "Programming and Graphics", "C & C++ Programming", "Control flow, arrays, pointers, dynamic memory, structs, OOP concepts, polymorphism, templates", "high"),
        ("P2-4.2", "P2", "Programming and Graphics", "Web Technologies", "HTML5, CSS3, JavaScript DOM, XML, client-side scripting basics", "medium"),
        ("P2-5.1", "P2", "DBMS", "Data Models & ER", "3-tier architecture, ER modeling, relational algebra, tuple calculus", "high"),
        ("P2-5.2", "P2", "DBMS", "SQL & Normalization", "DDL, DML, joins, subqueries, ACID properties, functional dependencies, 1NF to BCNF", "high"),
        ("P2-5.3", "P2", "DBMS", "Transactions & Recovery", "Concurrency control, locks, two-phase locking, serializability, recovery techniques", "medium"),
        ("P2-6.1", "P2", "Operating Systems", "Process Management", "Process states, PCB, CPU scheduling algorithms, threads, multithreading", "high"),
        ("P2-6.2", "P2", "Operating Systems", "Synchronization & Deadlocks", "Critical section, semaphores, mutex, deadlock prevention, detection, Banker's algorithm", "high"),
        ("P2-6.3", "P2", "Operating Systems", "Memory & Storage", "Paging, segmentation, page replacement algorithms (FIFO, LRU), disk scheduling (SSTF, SCAN)", "high"),
        ("P2-7.1", "P2", "Software Engineering", "SDLC & Agile", "Waterfall, Spiral, Agile Scrum, Sprint ceremonies, user stories", "high"),
        ("P2-7.2", "P2", "Software Engineering", "Testing & Design", "Coupling & cohesion, Black-box & White-box testing, unit/integration/regression testing", "high"),
        ("P2-8.1", "P2", "Data Structures and Algorithms", "Linear & Non-linear Data Structures", "Arrays, linked lists, stacks, queues, binary search trees, AVL trees, heaps", "high"),
        ("P2-8.2", "P2", "Data Structures and Algorithms", "Algorithm Design & Complexity", "Asymptotic analysis (Big-O, Omega, Theta), Divide & Conquer, Greedy, Dynamic Programming, Graph algorithms", "high"),
        ("P2-9.1", "P2", "Computer Networks", "OSI & TCP/IP Reference Models", "Layer responsibilities, packet encapsulation, physical media, multiplexing", "high"),
        ("P2-9.2", "P2", "Computer Networks", "Network Layer & Routing", "IPv4/IPv6 addressing, subnetting, CIDR, ARP, routing protocols (distance vector, link state)", "high"),
        ("P2-9.3", "P2", "Computer Networks", "Transport & Application Protocols", "TCP three-way handshake, UDP, flow control, DNS, HTTP, SMTP, network security & firewalls", "high"),
        ("P2-10.1", "P2", "Artificial Intelligence", "Search & Problem Solving", "State space search, BFS, DFS, Heuristic search (A*, Best-first), game playing (Minimax, Alpha-beta)", "high"),
        ("P2-10.2", "P2", "Artificial Intelligence", "Knowledge Representation & Machine Learning", "Propositional/predicate logic, expert systems, neural networks, supervised vs unsupervised learning", "high")
    ]
    for pid, pap, subj, unit, text, prio in p2_items:
        lines.append({
            "id": pid, "paper": pap, "subject": subj, "unit": unit, "topic": unit, "text": text, "priority": prio
        })

    syllabus_obj = {
        "exam": "Karnataka GPT CST Teacher Recruitment 2026",
        "source_url": "https://schooleducation.karnataka.gov.in",
        "retrieved": "2026-10-12",
        "notification": {
            "name": "EP 80 DPI 2026",
            "date": "2026-08-10"
        },
        "lines": lines
    }
    syllabus_lines_path = syllabus_dir / "syllabus_lines.json"
    safe_write_text(syllabus_lines_path, json.dumps(syllabus_obj, indent=2))

    # 5. Validate with examkit.py
    run_cmd([PYTHON_EXE, EXAMKIT_PY, "validate", "config", str(config_path)], desc="Validate exam_config.json")
    run_cmd([PYTHON_EXE, EXAMKIT_PY, "validate", "syllabus", str(syllabus_lines_path)], desc="Validate syllabus_lines.json")

    # 6. Initialize ledger tasks
    ledger_tasks = [
        "Phase 0: Environment smoke test & directory initialization",
        "Phase 1: Official framework & exam brief lock",
        "Phase 2: Syllabus line-by-line lock and validation",
        "Phase 3: Source registry and YouTube resource curation",
        "Phase 4: Comprehensive study notes generation for Paper 1 and Paper 2",
        "Phase 5: Current affairs and GK capsule generation",
        "Phase 6: Verbatim PYQ archive and question bank compilation",
        "Phase 7: Offline HTML interactive mock test generation",
        "Phase 8: 14-day study plan and START_HERE navigation index",
        "Phase 9: Quality audit, link-check, and traceability verification"
    ]
    for task in ledger_tasks:
        run_cmd([PYTHON_EXE, EXAMKIT_PY, "ledger", "--workspace", str(OUTPUT_ROOT), "add", "--text", task], desc=f"Ledger add: {task[:30]}...")

    log_action("=== STEP 1 FINISHED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
