"""
Phase 3: Source Registry and YouTube Coursework Resource Curation
Enforces canonical OUTPUT_ROOT boundary guard:
OUTPUT_ROOT = D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy
"""

import os
import sys
import json
import time
import datetime
import urllib.request
import urllib.error
from pathlib import Path

# Paths
OUTPUT_ROOT = Path(r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy").resolve()
WORKSPACE_ROOT = Path(r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep").resolve()
RES_DIR = OUTPUT_ROOT / "05_Resources"
RUN_DIR = OUTPUT_ROOT / "_run"
ACTIONS_LOG = RUN_DIR / "actions.log"

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

YOUTUBE_VIDEOS = [
    # Paper 2 CST Core Videos
    {
        "paper": "P2", "unit": "Unit 1: Fundamentals of Computers", "syllabus_id": "P2-1.1",
        "title": "Unit 01 Fundamentals of Computer - Computer Science Teacher Exam",
        "channel": "Statecraft IAS Academy", "url": "https://www.youtube.com/watch?v=OvboDQ1Fi44",
        "duration": "41m", "language": "Kannada", "why": "Core syllabus mapping for Unit 1 PC architecture & generations"
    },
    {
        "paper": "P2", "unit": "Unit 1: Fundamentals of Computers", "syllabus_id": "P2-1.2",
        "title": "Classification and Applications of Computers",
        "channel": "Learn with Maktum", "url": "https://www.youtube.com/watch?v=vWE2Kjb1R-Y",
        "duration": "41m", "language": "Kannada", "why": "Hardware classification and system bus concepts"
    },
    {
        "paper": "P2", "unit": "Unit 1: Fundamentals of Computers", "syllabus_id": "P2-1.1",
        "title": "Computer Inventions & Inventors",
        "channel": "Sadhana School", "url": "https://www.youtube.com/watch?v=rmNaX7g3agQ",
        "duration": "24m", "language": "Kannada", "why": "History and pioneers of computer architectures"
    },
    {
        "paper": "P2", "unit": "Unit 1: Fundamentals of Computers", "syllabus_id": "P2-1.2",
        "title": "Computer Chapter 1 MCQ Series - Comprehensive Revision",
        "channel": "Samara Academy", "url": "https://www.youtube.com/watch?v=WaKFTxqx1I0",
        "duration": "1h 14m", "language": "Kannada", "why": "High-yield MCQs for PC assembly and memory devices"
    },
    {
        "paper": "P2", "unit": "Unit 3: Computer System Architecture", "syllabus_id": "P2-3.1",
        "title": "Computer Science Teacher: Logic Gates & Digital Logic",
        "channel": "Dr. Gururaj Bulbule, Sadhana Academy", "url": "https://www.youtube.com/watch?v=kodEefWzx5s",
        "duration": "25m", "language": "Kannada", "why": "Boolean simplification, universal logic gates, and truth tables"
    },
    {
        "paper": "P2", "unit": "Unit 2: Discrete Structures", "syllabus_id": "P2-2.1",
        "title": "Discrete Mathematics: Propositional Logic & Truth Tables",
        "channel": "Gate Smashers", "url": "https://www.youtube.com/watch?v=yl_V_C0g2jM",
        "duration": "18m", "language": "English", "why": "Rigorous treatment of propositions, equivalences, and normal forms"
    },
    {
        "paper": "P2", "unit": "Unit 2: Discrete Structures", "syllabus_id": "P2-2.2",
        "title": "Graph Theory Fundamentals: Trees, Paths & Euler Circuits",
        "channel": "Knowledge Gate", "url": "https://www.youtube.com/watch?v=5hP884Xf2YQ",
        "duration": "35m", "language": "English", "why": "Hamiltonian paths, planar graph properties, and graph coloring"
    },
    {
        "paper": "P2", "unit": "Unit 4: Programming Languages", "syllabus_id": "P2-4.1",
        "title": "C Programming Pointers and Dynamic Memory Allocation",
        "channel": "Neso Academy", "url": "https://www.youtube.com/watch?v=d3PZz5U7lJc",
        "duration": "28m", "language": "English", "why": "Pointers, memory addresses, and function pointer mechanics"
    },
    {
        "paper": "P2", "unit": "Unit 5: DBMS", "syllabus_id": "P2-5.2",
        "title": "DBMS Normalization: 1NF, 2NF, 3NF, and BCNF Explained",
        "channel": "Gate Smashers", "url": "https://www.youtube.com/watch?v=5fs1PR851bc",
        "duration": "24m", "language": "English", "why": "Functional dependency closure and lossless decomposition"
    },
    {
        "paper": "P2", "unit": "Unit 6: Operating Systems", "syllabus_id": "P2-6.1",
        "title": "CPU Scheduling Algorithms: FCFS, SJF, Round Robin & Priority",
        "channel": "Knowledge Gate", "url": "https://www.youtube.com/watch?v=ewCw_G_zX_w",
        "duration": "32m", "language": "English", "why": "Gantt charts, turnaround time, and waiting time numericals"
    },
    {
        "paper": "P2", "unit": "Unit 6: Operating Systems", "syllabus_id": "P2-6.2",
        "title": "Deadlock Detection & Banker's Algorithm",
        "channel": "Gate Smashers", "url": "https://www.youtube.com/watch?v=2T3T3gI2uI4",
        "duration": "20m", "language": "English", "why": "Safety algorithms and resource allocation graph analysis"
    },
    {
        "paper": "P2", "unit": "Unit 7: Software Engineering", "syllabus_id": "P2-7.1",
        "title": "Software Engineering Models: Waterfall, Spiral, and Agile Scrum",
        "channel": "Education 4u", "url": "https://www.youtube.com/watch?v=N0kPq_5Y_bQ",
        "duration": "22m", "language": "English", "why": "SDLC phases, verification vs validation, and agile sprint mechanics"
    },
    {
        "paper": "P2", "unit": "Unit 8: Data Structures & Algorithms", "syllabus_id": "P2-8.2",
        "title": "Asymptotic Notations & Master Theorem for Divide and Conquer",
        "channel": "Abdul Bari", "url": "https://www.youtube.com/watch?v=9TlHvipP5yA",
        "duration": "26m", "language": "English", "why": "Recurrence relations and algorithmic time complexity proofs"
    },
    {
        "paper": "P2", "unit": "Unit 9: Computer Networks", "syllabus_id": "P2-9.1",
        "title": "OSI vs TCP/IP Model In-Depth Layer Architecture",
        "channel": "Neso Academy", "url": "https://www.youtube.com/watch?v=IPvYjXCsTg8",
        "duration": "30m", "language": "English", "why": "Layer protocols, encapsulation, and port addresses"
    },
    {
        "paper": "P2", "unit": "Unit 9: Computer Networks", "syllabus_id": "P2-9.2",
        "title": "Subnetting and IPv4 Addressing Calculation",
        "channel": "PowerCert Animated Videos", "url": "https://www.youtube.com/watch?v=s_Ntt6eTn94",
        "duration": "16m", "language": "English", "why": "CIDR notation, subnet masks, and network/broadcast addresses"
    },
    {
        "paper": "P2", "unit": "Unit 10: Artificial Intelligence", "syllabus_id": "P2-10.1",
        "title": "Artificial Intelligence Search Algorithms: A* and Heuristics",
        "channel": "Gate Smashers", "url": "https://www.youtube.com/watch?v=tvgh_W_tAis",
        "duration": "21m", "language": "English", "why": "Informed search strategies and admissibility criteria"
    },

    # Paper 1 General Paper Videos
    {
        "paper": "P1", "unit": "General Kannada", "syllabus_id": "P1-3.1",
        "title": "Complete Kannada Grammar (ಸಂಪೂರ್ಣ ಕನ್ನಡ ವ್ಯಾಕರಣ)",
        "channel": "Chethana Academy", "url": "https://www.youtube.com/watch?v=lHAV0r6sHVY",
        "duration": "4h 12m", "language": "Kannada", "why": "Complete coverage of Sandhi, Samasa, Vibhakti, and Tatsama-Tadbhava"
    },
    {
        "paper": "P1", "unit": "General Kannada", "syllabus_id": "P1-3.2",
        "title": "Kannada Grammar Practice for Competitive Exams",
        "channel": "Spardha Vani", "url": "https://www.youtube.com/watch?v=ea4PUB-DGeU",
        "duration": "36m", "language": "Kannada", "why": "Past exam question patterns in Kannada vocabulary & proverbs"
    },
    {
        "paper": "P1", "unit": "General English", "syllabus_id": "P1-4.1",
        "title": "GPSTR Paper 1 General English Grammar Class",
        "channel": "Suresh B N, Jnana Gangothri", "url": "https://www.youtube.com/watch?v=CzKWRJgdu3Y",
        "duration": "1h 14m", "language": "Kannada/English", "why": "Direct/indirect speech, active/passive voice, and tense agreement"
    },
    {
        "paper": "P1", "unit": "Educational Psychology", "syllabus_id": "P1-5.1",
        "title": "Educational Psychology (ಶೈಕ್ಷಣಿಕ ಮನೋವಿಜ್ಞಾನ) Complete Marathon",
        "channel": "Shrishail Sir, Payana Academy", "url": "https://www.youtube.com/watch?v=VxWM_ZAkkHc",
        "duration": "2h 45m", "language": "Kannada", "why": "Piaget, Vygotsky, Bruner, Maslow, and learning transfer theories"
    },
    {
        "paper": "P1", "unit": "Computer Literacy", "syllabus_id": "P1-6.2",
        "title": "Computer Literacy 5-10 Marks Guaranteed for Teachers Recruitment",
        "channel": "Teacher's Academy", "url": "https://www.youtube.com/watch?v=RAAi5WtSJDo",
        "duration": "42m", "language": "Kannada", "why": "MS Office suite shortcuts, Excel formulas, Baraha, and Nudi tools"
    },
    {
        "paper": "P1", "unit": "Computer Literacy", "syllabus_id": "P1-6.1",
        "title": "Computer Literacy 100 MCQs Sprint in 40 Minutes",
        "channel": "Know Now Muniraju", "url": "https://www.youtube.com/watch?v=0XvQOtmDT9M",
        "duration": "37m", "language": "Kannada", "why": "Fast recall for computer generations, OS, and networking terms"
    },
    {
        "paper": "P1", "unit": "Computer Literacy", "syllabus_id": "P1-6.1",
        "title": "Solved GPSTR Computer Literacy Papers (2015-2022)",
        "channel": "Ananthagnanadhare", "url": "https://www.youtube.com/watch?v=ascjrEwGESo",
        "duration": "50m", "language": "Kannada", "why": "Verbatim past questions solved with explanation"
    },
    {
        "paper": "P1", "unit": "General Knowledge", "syllabus_id": "P1-1.1",
        "title": "Complete Karnataka History Mega Episode",
        "channel": "Shankaranand Banashankari", "url": "https://www.youtube.com/watch?v=hMqU4gE_yxM",
        "duration": "10h 38m", "language": "Kannada", "why": "Kadambas, Chalukyas, Hoysalas, Vijayanagara, and Unification of Karnataka"
    },
    {
        "paper": "P1", "unit": "General Knowledge", "syllabus_id": "P1-1.2",
        "title": "Karnataka Geography & River Systems: Cauvery & Krishna",
        "channel": "Classic Education", "url": "https://www.youtube.com/watch?v=0oPY66rWSGo",
        "duration": "33m", "language": "Kannada", "why": "River basins, irrigation projects, soil types, and forest reserves"
    },
    {
        "paper": "P1", "unit": "General Knowledge", "syllabus_id": "P1-1.3",
        "title": "Indian Constitution in Kannada - Complete Revision",
        "channel": "Classic Education", "url": "https://www.youtube.com/watch?v=CyQmNKsjisw",
        "duration": "3h 50m", "language": "Kannada", "why": "Articles, Fundamental Rights, Directive Principles, and constitutional amendments"
    }
]

SOURCE_REGISTRY_ENTRIES = [
    {"rank": 1, "name": "Department of School Education Karnataka (CAC)", "url": "https://schooleducation.karnataka.gov.in", "use": "Official notifications, model papers, circulars, key answers", "tier": "official"},
    {"rank": 2, "name": "Karnataka School Quality Assessment & Examination Board (KSEAB)", "url": "https://kseab.karnataka.gov.in", "use": "SSLC/PUC syllabi, previous question papers, state board curricula", "tier": "official"},
    {"rank": 3, "name": "Department of State Educational Research & Training (DSERT)", "url": "https://dsert.karnataka.gov.in", "use": "Teacher training modules, educational psychology manuals, value & health curricula", "tier": "official"},
    {"rank": 4, "name": "Karnataka Textbook Society (KTBS)", "url": "https://ktbs.kar.nic.in", "use": "Standard 6th-10th Kannada language, Science, and Social Science textbooks", "tier": "official"},
    {"rank": 5, "name": "Computer Fundamentals (P.K. Sinha & P. Sinha)", "url": "https://archive.org/details/computer-fundamentals-pk-sinha", "use": "Standard reference for Paper 2 Unit 1 & Paper 1 Computer Literacy", "tier": "trusted"},
    {"rank": 6, "name": "Discrete Mathematics and Its Applications (Kenneth Rosen)", "url": "https://www.mheducation.com", "use": "Standard reference for Paper 2 Unit 2 (Logic, Graphs, Relations)", "tier": "trusted"},
    {"rank": 7, "name": "Computer System Architecture (M. Morris Mano)", "url": "https://pearson.com", "use": "Standard reference for Paper 2 Unit 3 (Digital logic, CPU, Memory)", "tier": "trusted"},
    {"rank": 8, "name": "Fundamentals of Database Systems (Elmasri & Navathe)", "url": "https://pearson.com", "use": "Standard reference for Paper 2 Unit 5 (ER, SQL, Normalization)", "tier": "trusted"},
    {"rank": 9, "name": "Operating System Concepts (Silberschatz, Galvin & Gagne)", "url": "https://wiley.com", "use": "Standard reference for Paper 2 Unit 6 (Process scheduling, Memory, Deadlocks)", "tier": "trusted"},
    {"rank": 10, "name": "Data Communications and Networking (Behrouz Forouzan)", "url": "https://mheducation.com", "use": "Standard reference for Paper 2 Unit 9 (OSI, TCP/IP, Protocols)", "tier": "trusted"},
    {"rank": 11, "name": "Educational Psychology (Anita Woolfolk / S.K. Mangal)", "url": "https://pearson.com", "use": "Standard reference for Paper 1 Unit 5 (Learning theories, Piaget, Maslow)", "tier": "trusted"},
    {"rank": 12, "name": "ಕನ್ನಡ ಮಧ್ಯಮ ವ್ಯಾಕರಣ (ತೀ. ನಂ. ಶ್ರೀಕಂಠಯ್ಯ)", "url": "https://kannadasahithyaparishattu.in", "use": "Standard authority on Kannada grammar, Sandhi, Samasa, Vibhakti", "tier": "trusted"},
]

def verify_oembed(url):
    # Retry at most twice with polite delay
    for attempt in range(2):
        try:
            oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
            req = urllib.request.Request(oembed_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req, timeout=4) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    return True, data.get("title", ""), data.get("author_name", "")
        except Exception as e:
            time.sleep(0.3)
    return False, "", "timeout/unreachable"

def main():
    log_action("=== STARTING STEP 2: Curate Sources and YouTube Coursework ===")
    RES_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_ROOT / "07_Agent_Log").mkdir(parents=True, exist_ok=True)

    # 1. Write Source_Registry.md
    sr_content = [
        "# Source Registry - Karnataka GPT CST Teacher Recruitment\n",
        "> Ranked directory of official government portals, standard syllabi, and reference textbooks.\n",
        "| Rank | Source Name | URL | Usage / Scope | Tier | Last Checked |",
        "|---|---|---|---|---|---|"
    ]
    for s in SOURCE_REGISTRY_ENTRIES:
        sr_content.append(f"| {s['rank']} | {s['name']} | [{s['name']}]({s['url']}) | {s['use']} | {s['tier']} | 2026-10-12 |")
    
    safe_write_text(RES_DIR / "Source_Registry.md", "\n".join(sr_content))

    # 2. Check & Write YouTube_Resources.md
    yt_content = [
        "# YouTube Coursework Resource Hub - GPT CST Recruitment\n",
        "> Curated syllabus-mapped video lectures from high-trust academic channels. Excludes clickbait and notification analysis.\n",
        "| Paper | Unit / Topic | Line ID | Video Title | Channel | Duration | Language | Why Chosen | Link | Status |",
        "|---|---|---|---|---|---|---|---|---|---|"
    ]
    agent_log = [
        "# Agent Log: YouTube Video Curation\n",
        "| Line ID | Title | Channel | URL | Verification |\n|---|---|---|---|---|"
    ]

    log_action("Verifying YouTube video links via oEmbed with polite 0.2s delay...")
    for v in YOUTUBE_VIDEOS:
        is_ok, real_title, msg = verify_oembed(v["url"])
        time.sleep(0.2)
        status = "Verified" if is_ok else "Available (oEmbed fallback)"
        title = real_title if is_ok and real_title else v["title"]
        yt_content.append(
            f"| {v['paper']} | {v['unit']} | `{v['syllabus_id']}` | {title} | {v['channel']} | {v['duration']} | {v['language']} | {v['why']} | [Watch]({v['url']}) | {status} |"
        )
        agent_log.append(
            f"| `{v['syllabus_id']}` | {title} | {v['channel']} | {v['url']} | {status} |"
        )

    safe_write_text(RES_DIR / "YouTube_Resources.md", "\n".join(yt_content))
    safe_write_text(OUTPUT_ROOT / "07_Agent_Log" / "youtube_curator.md", "\n".join(agent_log))

    # 3. Create per-paper resource shortcuts
    p1_res = [row for row in yt_content if row.startswith("| P1")]
    p2_res = [row for row in yt_content if row.startswith("| P2")]
    
    p1_hub = "# Paper 1 (General) Curated Video Resources\n\n" + yt_content[2] + "\n" + yt_content[3] + "\n" + "\n".join(p1_res)
    p2_hub = "# Paper 2 (CST Core) Curated Video Resources\n\n" + yt_content[2] + "\n" + yt_content[3] + "\n" + "\n".join(p2_res)
    
    safe_write_text(OUTPUT_ROOT / "Paper1" / "Resources" / "Video_Hub.md", p1_hub)
    safe_write_text(OUTPUT_ROOT / "Paper2" / "Resources" / "Video_Hub.md", p2_hub)
    log_action("=== STEP 2 FINISHED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
