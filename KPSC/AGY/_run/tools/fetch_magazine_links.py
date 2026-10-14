import urllib.request
import re

url = "https://iasbaba.com/tag/iasbabas-monthly-current-affairs-magazine/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        # Find articles
        articles = re.findall(r'href=[\'"](https?://iasbaba\.com/\d{4}/\d{2}/[^\'" >]+)[\'"]', html)
        print("Found article URLs:")
        for a in set(articles):
            print(a)
except Exception as e:
    print(f"Error: {e}")
