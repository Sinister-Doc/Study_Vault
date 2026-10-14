import os
import sys
import urllib.request
import re

url = "https://karnatakavarthe.org/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        matches = re.findall(r'href=[\'"](https?://[^\'" >]+)[\'"]', html)
        mag_links = [m for m in matches if any(k in m.lower() for k in ["march", "janapada", "magazine", "pdf"])]
        print(f"Total matching links found: {len(mag_links)}")
        for l in sorted(list(set(mag_links)))[:15]:
            print(l)
except Exception as e:
    print(f"Error connecting: {e}")
