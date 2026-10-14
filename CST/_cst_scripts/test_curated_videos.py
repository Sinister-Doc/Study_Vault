import sys, urllib.request, json
sys.stdout.reconfigure(encoding='utf-8')

video_ids = [
    # Already verified working:
    "OvboDQ1Fi44", "vWE2Kjb1R-Y", "rmNaX7g3agQ", "WaKFTxqx1I0", "kodEefWzx5s",
    "9TlHvipP5yA", "IPvYjXCsTg8", "lHAV0r6sHVY", "ea4PUB-DGeU", "VxWM_ZAkkHc",
    "RAAi5WtSJDo", "0XvQOtmDT9M", "ascjrEwGESo", "hMqU4gE_yxM", "0oPY66rWSGo",
    "CyQmNKsjisw",
    # 10 Newly curated working replacements:
    "5GDTIUVlHB8", "hjGD08xfg9c", "VCIVXPoiLpU", "6kYngPvoGxU", "09_LlHjoEiY",
    "zuegQmMdy8M", "SzRs2y1TcSY", "_bn0CF5zqvo", "FrgpjsrQsF4", "tkbsh1ephO0"
]

all_ok = True
for vid in video_ids:
    oembed = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    try:
        req = urllib.request.Request(oembed, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as res:
            data = json.loads(res.read().decode("utf-8"))
            print(f"[OK 200] {vid}: {data.get('title')} ({data.get('author_name')})")
    except Exception as e:
        print(f"[FAIL] {vid}: {e}")
        all_ok = False

print(f"\nTotal tested: {len(video_ids)} | All valid 200: {all_ok}")
