import urllib.request
import re

url = "https://www.insightsonindia.com/downloads/monthly-current-affairs-compilations/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        pdfs = re.findall(r'href=[\'"](https?://[^\'" >]+\.pdf)[\'"]', html, re.IGNORECASE)
        print("Found Insights PDF links:", len(pdfs))
        for p in set(pdfs)[:10]:
            print(p)
except Exception as e:
    print(f"Error: {e}")
