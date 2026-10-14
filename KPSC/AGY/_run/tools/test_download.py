import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_download, ROOT_DIR

target_file = os.path.join(ROOT_DIR, "_sources", "magazines", "IASbaba", "2026-02", "IASbaba_Monthly_Digest_Feb.pdf")
url = "https://iasbaba.com/wp-content/uploads/2024/03/IASBABAS-Current-Affairs-Monthly-Magazine-February-2024.pdf"

print("Initiating safe_download...")
meta = safe_download(url, target_file)
print("Download success! Meta:", meta)
