import os
import json
import re

ROOT = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\KPSC\AGY"

def audit():
    print("=== AUDIT HELPER ===")
    mock_dir = os.path.join(ROOT, "06_Mock_Tests")
    html_files = [f for f in os.listdir(mock_dir) if f.endswith(".html")]
    for hf in html_files:
        hp = os.path.join(mock_dir, hf)
        with open(hp, "r", encoding="utf-8") as f:
            txt = f.read()
        ids = re.findall(r'"id":\s*"(KAS-[^"]+)"', txt)
        unique_ids = list(dict.fromkeys(ids))
        print(f"{hf}: {len(ids)} occurrences, {len(unique_ids)} unique question IDs")

    # Check manifest files
    manifests = [f for f in os.listdir(mock_dir) if f.endswith(".manifest.json")]
    for mf in manifests:
        mp = os.path.join(mock_dir, mf)
        with open(mp, "r", encoding="utf-8") as f:
            mdata = json.load(f)
        qs = mdata.get("questions", [])
        print(f"{mf}: {len(qs)} questions listed")

if __name__ == "__main__":
    audit()
