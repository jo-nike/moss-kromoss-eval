"""MOSS-Image benchmark runner. Runs ON beast against localhost ComfyUI, one job at a time.

usage: python3 bench_run.py <prompts_dir> <results.jsonl>
Reads prompts_*.jsonl, renders each at ~2 MP with the SFT bf16 model (25 steps, er_sde/simple,
cfg 2.5, SLG 22 for 0-0.5), appends one result line per id. Re-running skips ids already done.
"""
import glob, json, math, os, sys, time, urllib.request, uuid, zlib

URL = "http://127.0.0.1:8188"
NEG = "nsfw, worst quality, bad anatomy, watermark, jpeg artifact"
SIZES = {"1:1": (1456, 1456), "4:5": (1296, 1616), "3:4": (1248, 1680), "2:3": (1184, 1776), "9:16": (1088, 1936),
         "5:4": (1616, 1296), "4:3": (1680, 1248), "3:2": (1776, 1184), "16:9": (1936, 1088), "21:9": (2208, 944)}


def layout_prompt(p):
    lay = p["layout"]
    W, H = lay["canvas"]
    items = []
    for it in lay["items"]:
        x0, y0, x1, y1 = it["bbox"]
        out = {k: v for k, v in it.items() if k != "bbox"}
        # top-left xyxy pixels -> centred yxyx, enclosing fractional edges (as compile_prompt.py does)
        out["bbox"] = [math.floor(y0) - H // 2, math.floor(x0) - W // 2, math.ceil(y1) - H // 2, math.ceil(x1) - W // 2]
        items.append(out)
    summary = {"caption": p["prompt"]}
    if lay.get("meta"):
        summary = {"meta": lay["meta"], "canvas": "single", "caption": p["prompt"]}
    return json.dumps({"summary": summary, "items": items, "bbox_coord_space": "abs_centralized", "bbox_format": "yxyx"},
                      ensure_ascii=False, separators=(",", ":")), (W, H)


def graph(text, w, h, seed, prefix):
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "moss_image_sft_bf16.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen3.5_9b_int8_convrot.safetensors", "type": "moss_image", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "flux2-vae.safetensors"}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": text}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": NEG}},
        "6": {"class_type": "EmptyFlux2LatentImage", "inputs": {"width": w, "height": h, "batch_size": 1}},
        "15": {"class_type": "SkipLayerGuidanceDiTSimple", "inputs": {"model": ["1", 0], "double_layers": "", "single_layers": "22", "start_percent": 0.0, "end_percent": 0.5}},
        "7": {"class_type": "KSampler", "inputs": {"model": ["15", 0], "positive": ["4", 0], "negative": ["5", 0], "latent_image": ["6", 0],
                                                  "seed": seed, "steps": 25, "cfg": 2.5, "sampler_name": "er_sde", "scheduler": "simple", "denoise": 1.0}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["7", 0], "vae": ["3", 0]}},
        "9": {"class_type": "SaveImage", "inputs": {"images": ["8", 0], "filename_prefix": prefix}},
    }


def call(path, body=None):
    for attempt in range(60):  # ride out a ComfyUI restart (~5 min)
        try:
            req = urllib.request.Request(URL + path, data=json.dumps(body).encode() if body is not None else None,
                                         headers={"Content-Type": "application/json"})
            return json.load(urllib.request.urlopen(req, timeout=30))
        except urllib.error.HTTPError:
            raise
        except Exception:
            time.sleep(5)
    raise RuntimeError(f"ComfyUI unreachable for {path}")


def main():
    pdir, out = sys.argv[1], sys.argv[2]
    # prompt files arrive while the run is going: keep re-scanning until all six are in and rendered
    while True:
        attempted = set()
        if os.path.exists(out):
            attempted = {json.loads(l)["id"] for l in open(out)}
        files = sorted(glob.glob(os.path.join(pdir, "prompts_*.jsonl")))
        pending = [p for f in files for p in map(json.loads, filter(str.strip, open(f))) if p["id"] not in attempted]
        if not pending:
            if len(files) >= 6:
                break
            time.sleep(30)
            continue
        run(pending, out)
    print("ALLDONE")


def run(prompts, out):
    for p in prompts:
        if p.get("format") == "layout":
            text, (w, h) = layout_prompt(p)
        else:
            text, (w, h) = p["prompt"], SIZES[p["aspect"]]
        seed = zlib.crc32(p["id"].encode())
        rec = {"id": p["id"], "seed": seed, "w": w, "h": h}
        try:
            r = call("/api/prompt", {"prompt": graph(text, w, h, seed, f"claude/moss/bench/{p['id']}"), "client_id": str(uuid.uuid4())})
            pid = r["prompt_id"]
            while True:
                hist = call(f"/api/history/{pid}")
                if pid in hist and hist[pid]["status"].get("completed") is not None:
                    break
                time.sleep(3)
            st = hist[pid]["status"]
            msgs = {m[0]: m[1] for m in st["messages"]}
            rec["status"] = st["status_str"]
            if st["status_str"] == "success":
                img = hist[pid]["outputs"]["9"]["images"][0]
                rec["file"] = f"{img['subfolder']}/{img['filename']}"
                rec["secs"] = round((msgs["execution_success"]["timestamp"] - msgs["execution_start"]["timestamp"]) / 1000, 1)
            else:
                rec["error"] = str(msgs.get("execution_error", {}).get("exception_message", st))[:500]
        except Exception as e:
            rec["status"], rec["error"] = "error", repr(e)[:500]
        with open(out, "a") as f:
            f.write(json.dumps(rec) + "\n")


main()
