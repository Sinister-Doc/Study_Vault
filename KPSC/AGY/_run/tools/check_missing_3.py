import urllib.request
import re

urls = [
    ("2026-03", "https://iasbaba.com/2024/06/current-affairs-ias-upsc-revamped-current-affairs-magazine-march-2024/"),
    ("2026-07", "https://iasbaba.com/2024/08/current-affairs-ias-upsc-revamped-current-affairs-magazine-july-2024/"),
    ("2026-08", "https://iasbaba.com/2024/09/current-affairs-ias-upsc-revamped-current-affairs-magazine-august-2024/")
]

for tag, url in urls:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            pdfs = re.findall(r'href=[\'"](https?://iasbaba\.com/wp-content/uploads/[^\'" >]+\.pdf)[\'"]', html, re.IGNORECASE)
            print(f"{tag}: status {resp.status}, PDFs found: {pdfs}")
    except Exception as e:
        print(f"{tag}: URL {url} error: {e}")
