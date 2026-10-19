"""On beast: make 1280px JPEGs of finished benchmark renders. usage: to_jpg.py <results.jsonl> <outdir>"""
import json, os, sys
from PIL import Image
res, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
n = 0
for line in open(res):
    r = json.loads(line)
    dst = os.path.join(out, r["id"] + ".jpg")
    if r.get("status") != "success" or os.path.exists(dst):
        continue
    im = Image.open(os.path.join("/mnt/data/ComfyUI/output", r["file"])).convert("RGB")
    im.thumbnail((1280, 1280), Image.LANCZOS)
    im.save(dst, quality=88)
    n += 1
print("converted", n)
