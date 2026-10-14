import os
import sys
import json
import re

sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

mocks_dir = os.path.join(ROOT_DIR, "06_Mock_Tests")
files = sorted(os.listdir(mocks_dir))
inventory = []
for f in files:
    if f.endswith(".html") and f.startswith("CBT_"):
        p = os.path.join(mocks_dir, f)
        with open(p, "r", encoding="utf-8") as fp:
            content = fp.read()
        m = re.search(r'const EXAM_DATA = (\{.*?\});', content, re.DOTALL)
        if m:
            data = json.loads(m.group(1))
            inventory.append({
                "file": f,
                "title": data.get("title", ""),
                "paper": data.get("paper", ""),
                "questions_count": len(data.get("questions", [])),
                "duration_mins": data.get("duration_minutes", data.get("duration_mins", 120)),
                "sections": [s.get("name") for s in data.get("sections", [])]
            })

print(f"Total CBT HTML Files: {len(inventory)}")
total_qs = sum(item["questions_count"] for item in inventory)
print(f"Total Questions Across All HTML Files: {total_qs}")
for item in inventory:
    print(f"- {item['file']}: {item['questions_count']} Qs | Paper: {item['paper']} | Duration: {item['duration_mins']}m | Sections: {item['sections']}")
