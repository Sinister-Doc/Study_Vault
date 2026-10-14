"""
Master Unattended Pipeline Runner for CST Exam Prep Vault
Enforces canonical OUTPUT_ROOT boundary guard:
OUTPUT_ROOT = D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy
"""

import os
import sys
import json
import time
import datetime
import subprocess
from pathlib import Path

# Paths
OUTPUT_ROOT = Path(r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy").resolve()
WORKSPACE_ROOT = Path(r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep").resolve()
CST_DIR = WORKSPACE_ROOT / "CST"
SCRIPTS_DIR = CST_DIR / "_cst_scripts"
RUN_DIR = OUTPUT_ROOT / "_run"
ACTIONS_LOG = RUN_DIR / "actions.log"
STATE_FILE = RUN_DIR / ".pipeline_state.json"
PYTHON_EXE = Path(r"D:\Softwares\pyenv\Scripts\python.exe")

PIPELINE_STEPS = [
    {
        "id": "step_1",
        "name": "01_framework_and_syllabus_lock",
        "script": SCRIPTS_DIR / "01_framework_and_syllabus_lock.py",
        "desc": "Initialize scaffold, lock raw notification, syllabus lines, and configs in OUTPUT_ROOT"
    },
    {
        "id": "step_2",
        "name": "02_curate_sources_and_youtube",
        "script": SCRIPTS_DIR / "02_curate_sources_and_youtube.py",
        "desc": "Curate verified source registry and 26+ coursework YouTube videos into OUTPUT_ROOT"
    },
    {
        "id": "step_3",
        "name": "03_pyq_and_question_bank_gatherer",
        "script": SCRIPTS_DIR / "03_pyq_and_question_bank_gatherer.py",
        "desc": "Compile verbatim PYQs from GPSTR 2015-2022, validate question bank schema in OUTPUT_ROOT"
    },
    {
        "id": "step_4",
        "name": "04_generate_study_vault_notes",
        "script": SCRIPTS_DIR / "04_generate_study_vault_notes.py",
        "desc": "Generate structured Obsidian notes with Mermaid diagrams and wikilinks in OUTPUT_ROOT"
    },
    {
        "id": "step_5",
        "name": "05_build_mocks_and_study_plan",
        "script": SCRIPTS_DIR / "05_build_mocks_and_study_plan.py",
        "desc": "Build interactive offline HTML mock tests, 00_START_HERE, and 14-day study plan in OUTPUT_ROOT"
    },
    {
        "id": "step_6",
        "name": "06_qa_and_lint_audit",
        "script": SCRIPTS_DIR / "06_qa_and_lint_audit.py",
        "desc": "Run traceability, link-check, mmdc linting, and compile RUN_REPORT.md in OUTPUT_ROOT"
    }
]

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

def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def save_state(state):
    try:
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")
        log_action(f"[FILE WRITE] {STATE_FILE}")
    except Exception as e:
        log_action(f"[STATE ERROR] {e}")

def main():
    force_run = "--force" in sys.argv
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    RUN_DIR.mkdir(parents=True, exist_ok=True)

    log_action("========================================================")
    log_action("STARTING GPT CST KN TEACHER RESEARCH PIPELINE EXECUTION")
    log_action(f"Working Directory: {WORKSPACE_ROOT}")
    log_action(f"ENFORCED OUTPUT ROOT: {OUTPUT_ROOT}")
    log_action(f"Python Executable: {PYTHON_EXE}")
    log_action("========================================================")

    state = load_state() if not force_run else {}

    guard_violations = 0
    total_start = time.time()
    for step in PIPELINE_STEPS:
        step_id = step["id"]
        step_name = step["name"]
        script_path = step["script"]

        if not force_run and state.get(step_id) == "COMPLETED":
            log_action(f"[SKIP] {step_name} already completed in previous run.")
            continue

        log_action(f"--> [STARTING STEP] {step_name}: {step['desc']}")
        step_start = time.time()

        try:
            cmd = [str(PYTHON_EXE), str(script_path)]
            log_action(f"[COMMAND RUN] {' '.join(cmd)}")
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd=str(WORKSPACE_ROOT)
            )

            for line in proc.stdout:
                line_clean = line.strip()
                if line_clean:
                    if "[GUARD REJECTED]" in line_clean:
                        guard_violations += 1
                    log_action(f"   [{step_name}] {line_clean}")

            proc.wait()
            duration = round(time.time() - step_start, 2)

            if guard_violations >= 5:
                log_action("[FATAL GUARD STOP] 5 or more guard violations detected! Halting pipeline.")
                break

            if proc.returncode == 0:
                state[step_id] = "COMPLETED"
                save_state(state)
                log_action(f"<-- [SUCCESS] {step_name} completed in {duration}s.")
            else:
                log_action(f"<-- [WARNING] {step_name} exited with code {proc.returncode}. Continuing pipeline...")
                state[step_id] = f"WARNING_CODE_{proc.returncode}"
                save_state(state)

        except Exception as e:
            log_action(f"<-- [ERROR] Unexpected exception in {step_name}: {str(e)}. Continuing pipeline...")
            state[step_id] = f"ERROR_{str(e)[:50]}"
            save_state(state)

    total_duration = round(time.time() - total_start, 2)
    log_action("========================================================")
    log_action(f"PIPELINE RUN FINISHED in {total_duration}s.")
    log_action(f"Actions Log: {ACTIONS_LOG}")
    log_action(f"Run Report: {RUN_DIR / 'RUN_REPORT.md'}")
    log_action(f"Open Items: {RUN_DIR / 'OPEN_ITEMS.md'}")
    log_action("========================================================")

if __name__ == "__main__":
    main()
