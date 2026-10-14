import urllib.request
import re

url = "https://iasbaba.com/2024/03/current-affairs-ias-upsc-revamped-current-affairs-magazine-february-2024/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        matches = re.findall(r'href=[\'"](https?://[^\'" >]+\.pdf)[\'"]', html, re.IGNORECASE)
        print("Found PDF links:", matches)
except Exception as e:
    print("Error:", e)
