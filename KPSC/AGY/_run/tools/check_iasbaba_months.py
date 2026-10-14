import urllib.request
import re

months = [
    ("February", "2024/03"),
    ("March", "2024/04"),
    ("April", "2024/05"),
    ("May", "2024/06"),
    ("June", "2024/07"),
    ("July", "2024/08"),
    ("August", "2024/09"),
    ("September", "2024/10"),
]

for m, ym in months:
    url = f"https://iasbaba.com/wp-content/uploads/{ym}/IASBABAS-Current-Affairs-Monthly-Magazine-{m}-2024.pdf"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            cl = resp.headers.get("Content-Length")
            print(f"{m}: HTTP {resp.status}, size = {int(cl)/(1024*1024):.2f} MB")
    except Exception as e:
        print(f"{m}: Error {e}")
