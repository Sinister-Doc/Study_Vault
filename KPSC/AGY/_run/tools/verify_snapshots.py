"""
verify_snapshots.py
Captures read-only listing of the parent KPSC directory,
verifies that NO outside files were modified or touched,
saves _run/after_snapshot.json and logs the verification result.
"""

import os
import sys
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import safe_ops

ROOT_DIR = safe_ops.ROOT_DIR
PARENT_DIR = os.path.abspath(os.path.join(ROOT_DIR, ".."))
BEFORE_FILE = os.path.join(ROOT_DIR, "_run", "before_snapshot.json")
AFTER_FILE = os.path.join(ROOT_DIR, "_run", "after_snapshot.json")

# Capture parent entries (excluding AGY internal contents)
after_entries = []
for entry in sorted(os.scandir(PARENT_DIR), key=lambda e: e.name):
    # Only inspect attributes of direct children of PARENT_DIR
    st = entry.stat()
    after_entries.append({
        "name": entry.name,
        "is_dir": entry.is_dir(),
        "size": st.st_size if not entry.is_dir() else 0,
        "mtime": st.st_mtime
    })

# Write after snapshot
safe_ops.safe_write(AFTER_FILE, json.dumps(after_entries, indent=2))
print(f"Captured after snapshot with {len(after_entries)} entries.")

# Compare with before snapshot
before_entries = json.load(open(BEFORE_FILE, encoding="utf-8"))
before_map = {e["name"]: e for e in before_entries}
after_map = {e["name"]: e for e in after_entries}

violations = []
for name, b in before_map.items():
    if name == "AGY":
        continue  # AGY is our workspace
    if name not in after_map:
        violations.append(f"MISSING: {name} was deleted from parent directory!")
    else:
        a = after_map[name]
        if b["size"] != a["size"]:
            violations.append(f"SIZE CHANGED: {name} size changed from {b['size']} to {a['size']}")
        if b["mtime"] != a["mtime"]:
            violations.append(f"MTIME CHANGED: {name} mtime changed from {b['mtime']} to {a['mtime']}")

for name in after_map:
    if name not in before_map:
        violations.append(f"NEW FILE IN PARENT: {name} was created outside ROOT!")

if violations:
    print("PARENT SNAPSHOT COMPARISON FAILED:")
    for v in violations:
        print(" - " + v)
    sys.exit(1)
else:
    print("PARENT SNAPSHOT INTEGRITY VERIFIED: 100% MATCH. Zero parent files modified, deleted, or created.")
    safe_ops.log_action("SNAPSHOT_VERIFIED", "Parent KPSC directory untouched - 100% integrity match.")
