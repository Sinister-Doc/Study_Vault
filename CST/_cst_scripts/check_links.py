import sys, urllib.request, re, json
sys.stdout.reconfigure(encoding='utf-8')

with open(r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy\05_Resources\YouTube_Resources.md", "r", encoding="utf-8") as f:
    text = f.read()

urls = re.findall(r"https://www\.youtube\.com/watch\?v=([a-zA-Z0-9_-]+)", text)

for vid in sorted(set(urls)):
    oembed = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    try:
        req = urllib.request.Request(oembed, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as res:
            data = json.loads(res.read().decode("utf-8"))
            print(f"[OK 200] {vid}: {data.get('title')} ({data.get('author_name')})")
    except urllib.error.HTTPError as e:
        print(f"[HTTP {e.code}] {vid}")
    except Exception as e:
        print(f"[ERR] {vid}: {e}")
