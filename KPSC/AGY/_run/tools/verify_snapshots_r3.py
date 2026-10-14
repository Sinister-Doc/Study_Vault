import os
import sys
import json
sys.path.insert(0, os.path.dirname(__file__))
import safe_ops

ROOT_DIR = safe_ops.ROOT_DIR
PARENT_DIR = os.path.abspath(os.path.join(ROOT_DIR, ".."))
BEFORE_FILE = os.path.join(ROOT_DIR, "_run", "before_snapshot_r3.json")
AFTER_FILE = os.path.join(ROOT_DIR, "_run", "after_snapshot_r3.json")

def capture_snapshot(target_file):
    entries = []
    for entry in sorted(os.scandir(PARENT_DIR), key=lambda e: e.name):
        st = entry.stat()
        entries.append({
            "name": entry.name,
            "is_dir": entry.is_dir(),
            "size": st.st_size if not entry.is_dir() else 0,
            "mtime": st.st_mtime
        })
    safe_ops.safe_write(target_file, json.dumps(entries, indent=2))
    return entries

def init_before_snapshot():
    entries = capture_snapshot(BEFORE_FILE)
    print(f"Captured Round 3 before-snapshot with {len(entries)} entries at: {BEFORE_FILE}")

def verify_parent_snapshots():
    after_entries = capture_snapshot(AFTER_FILE)
    print(f"Captured Round 3 after-snapshot with {len(after_entries)} entries.")

    with open(BEFORE_FILE, "r", encoding="utf-8") as f:
        before_entries = json.load(f)

    before_map = {e["name"]: e for e in before_entries}
    after_map = {e["name"]: e for e in after_entries}

    violations = []
    for name, b in before_map.items():
        if name == "AGY":
            continue
        if name not in after_map:
            violations.append(f"MISSING: {name} deleted outside ROOT!")
        else:
            a = after_map[name]
            if b["size"] != a["size"]:
                violations.append(f"SIZE CHANGED: {name} size {b['size']} -> {a['size']}")
            if b["mtime"] != a["mtime"]:
                violations.append(f"MTIME CHANGED: {name} mtime {b['mtime']} -> {a['mtime']}")

    for name in after_map:
        if name not in before_map:
            violations.append(f"NEW FILE OUTSIDE ROOT: {name}")

    if violations:
        print("PARENT SNAPSHOT COMPARISON FAILED:")
        for v in violations:
            print(f"  VIOLATION: {v}")
        return False
    else:
        print("PARENT SNAPSHOT COMPARISON 100% CLEAN: Zero external modifications detected.")
        return True

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--after":
        verify_parent_snapshots()
    else:
        init_before_snapshot()
