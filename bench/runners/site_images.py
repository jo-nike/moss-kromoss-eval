"""On beast: full-res JPEG q95 + 800 px thumbnails for the showcase site.
usage: site_images.py <results.jsonl> <outdir>   (writes <outdir>/full/<id>.jpg and <outdir>/thumb/<id>.jpg)"""
import json, os, sys
from PIL import Image
res, out = sys.argv[1], sys.argv[2]
for sub in ("full", "thumb"):
    os.makedirs(os.path.join(out, sub), exist_ok=True)
n = 0
for line in open(res):
    r = json.loads(line)
    full, thumb = (os.path.join(out, s, r["id"] + ".jpg") for s in ("full", "thumb"))
    if r.get("status") != "success" or (os.path.exists(full) and os.path.exists(thumb)):
        continue
    im = Image.open(os.path.join("/mnt/data/ComfyUI/output", r["file"])).convert("RGB")
    im.save(full, quality=95, subsampling=0)
    im.thumbnail((800, 800), Image.LANCZOS)
    im.save(thumb, quality=82)
    n += 1
print("converted", n)
