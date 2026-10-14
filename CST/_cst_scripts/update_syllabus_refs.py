import re
import os

notes_base = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy\03_Notes"

updates = {
    os.path.join(notes_base, "Paper1", "01_General_Knowledge", "Indian_Constitution_and_Polity.md"): ["P1-1.3", "P1-1.4", "P1-1.5"],
    os.path.join(notes_base, "Paper1", "02_Current_Affairs", "Karnataka_and_National_Current_Affairs_2026.md"): ["P1-2.1", "P1-2.2", "P1-2.3"],
    os.path.join(notes_base, "Paper1", "03_General_Kannada", "Kannada_Grammar_Sandhi_and_Samasa.md"): ["P1-3.1", "P1-3.2", "P1-3.3"],
    os.path.join(notes_base, "Paper1", "04_General_English", "General_English_Grammar_and_Vocabulary.md"): ["P1-4.1", "P1-4.2"],
    os.path.join(notes_base, "Paper1", "05_Educational_Psychology", "Child_Development_and_Learning_Theories.md"): ["P1-5.1", "P1-5.2", "P1-5.3", "P1-5.4"],
    os.path.join(notes_base, "Paper1", "06_Computer_Literacy", "Office_Automation_and_Kannada_Software.md"): ["P1-6.1", "P1-6.2", "P1-6.3"],
    os.path.join(notes_base, "Paper2", "Unit02_Discrete_Structures", "Graph_Theory_and_Trees.md"): ["P2-2.2", "P2-2.3"],
    os.path.join(notes_base, "Paper2", "Unit03_Computer_Architecture", "Digital_Logic_and_Combinational_Circuits.md"): ["P2-3.1", "P2-3.2", "P2-3.3"],
    os.path.join(notes_base, "Paper2", "Unit04_Programming_and_Graphics", "C_and_CPP_Core_Concepts.md"): ["P2-4.1", "P2-4.2"],
    os.path.join(notes_base, "Paper2", "Unit05_DBMS", "Relational_Model_and_Normalization.md"): ["P2-5.1", "P2-5.2", "P2-5.3"],
    os.path.join(notes_base, "Paper2", "Unit06_Operating_Systems", "Process_Scheduling_and_Deadlocks.md"): ["P2-6.1", "P2-6.2", "P2-6.3"],
    os.path.join(notes_base, "Paper2", "Unit07_Software_Engineering", "SDLC_Models_and_Testing_Strategies.md"): ["P2-7.1", "P2-7.2"],
    os.path.join(notes_base, "Paper2", "Unit09_Networks_and_Communication", "OSI_Model_and_IP_Subnetting.md"): ["P2-9.1", "P2-9.2", "P2-9.3"],
    os.path.join(notes_base, "Paper2", "Unit10_Artificial_Intelligence", "Search_Algorithms_and_Admissible_Heuristics.md"): ["P2-10.1", "P2-10.2"]
}

for filepath, refs in updates.items():
    if not os.path.exists(filepath):
        print(f"Not found: {filepath}")
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_refs_block = "syllabus_refs:\n" + "\n".join(f'  - "{r}"' for r in refs)
    content = re.sub(r'syllabus_refs:[\s\S]*?(?=syllabus_refs_partial:)', new_refs_block + "\n", content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {os.path.basename(filepath)} with {refs}")

print("All frontmatter syllabus_refs updated.")
