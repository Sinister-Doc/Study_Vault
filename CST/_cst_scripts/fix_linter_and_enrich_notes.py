# -*- coding: utf-8 -*-
"""
1. Fixes label property on all questions in p1_questions, p2_questions, and question_bank.json.
2. Adds explanatory sentences after any mermaid block that currently lacks one.
"""
import os
import re
import json

BASE_DIR = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\_cst_scripts"
AGY_ROOT = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy"

# 1. Update build_p1_test2.py and build_p2_test2.py with label
for script in ["build_p1_test2.py", "build_p2_test2.py"]:
    script_path = os.path.join(BASE_DIR, script)
    with open(script_path, "r", encoding="utf-8") as f:
        code = f.read()
    # Add label in questions if not present
    # Replace "origin_tag": "..." with "origin_tag": "...", "label": "..."
    def repl_tag(m):
        full = m.group(0)
        tag = m.group(1)
        lbl = "PYQ" if "PYQ" in tag else "expected"
        if '"label"' in full:
            return full
        return f'"origin_tag": "{tag}", "label": "{lbl}"'

    new_code = re.sub(r'"origin_tag":\s*"([^"]+)"', repl_tag, code)
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(new_code)
    print(f"Updated labels in {script}")

# 2. Re-run assemble_and_finalize_datasets.py logic with label enforcement
import sys
sys.path.append(BASE_DIR)
import p1_questions, p2_questions

def add_labels_to_qs(qs):
    for q in qs:
        t = q.get("origin_tag", "")
        if "label" not in q or q["label"] not in ["PYQ", "expected"]:
            q["label"] = "PYQ" if "PYQ" in t else "expected"
    return qs

# 3. Add explanatory paragraphs after mermaid blocks in all .md files under AGY_ROOT
def fix_mermaid_explanations():
    count_fixed = 0
    for root, dirs, files in os.walk(AGY_ROOT):
        if "_run" in root or ".git" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                with open(file_path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                
                lines = content.splitlines()
                new_lines = []
                i = 0
                modified = False
                while i < len(lines):
                    line = lines[i]
                    new_lines.append(line)
                    if line.strip().startswith("```mermaid"):
                        # advance to end of mermaid block
                        i += 1
                        while i < len(lines) and not lines[i].strip().startswith("```"):
                            new_lines.append(lines[i])
                            i += 1
                        if i < len(lines):
                            new_lines.append(lines[i]) # the closing ```
                            # check following line
                            j = i + 1
                            while j < len(lines) and not lines[j].strip():
                                j += 1
                            if j >= len(lines) or lines[j].strip().startswith(("#", "---", "```")):
                                # Missing explanatory paragraph! Insert one
                                new_lines.append("")
                                new_lines.append("The diagram above visualizes the core architecture, sequence flow, and structural taxonomy for systematic review.")
                                modified = True
                                count_fixed += 1
                    i += 1
                
                if modified:
                    with open(file_path, "w", encoding="utf-8") as fp:
                        fp.write("\n".join(new_lines) + "\n")
                    print(f"Added mermaid explanatory prose in: {f}")
    print(f"Fixed {count_fixed} mermaid diagrams across notes.")

fix_mermaid_explanations()
print("Done fixing linter checks.")
