"""
fix_source_urls.py
Standardizes frontmatter URLs across notes to canonical, active government domains
avoiding discontinued department subdomains.
"""

import os
import glob
import re

ROOT_DIR = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\KPSC\AGY"

# Canonical URL replacements
replacements = {
    "https://sw.karnataka.gov.in": "https://karnataka.gov.in",
    "https://hfw.karnataka.gov.in": "https://karnataka.gov.in",
    "https://itskarnataka.gov.in": "https://karnataka.gov.in",
    "https://kits.karnataka.gov.in": "https://karnataka.gov.in",
    "https://lokayukta.kar.nic.in": "https://dpar.karnataka.gov.in",
    "https://isro.gov.in": "https://www.isro.gov.in",
    "https://ktbs.kar.nic.in": "https://kseeb.karnataka.gov.in",
}

count = 0
for f in glob.glob(os.path.join(ROOT_DIR, "03_Notes", "**", "*.md"), recursive=True):
    content = open(f, encoding="utf-8").read()
    orig = content
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
    if content != orig:
        open(f, "w", encoding="utf-8").write(content)
        count += 1
        print(f"Updated URLs in: {os.path.basename(f)}")

print(f"Total files updated: {count}")
