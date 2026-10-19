"""Build data.json for index.html from bench/ (prompts, render logs, per-image grades)."""
import json, os, statistics

ROOT = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(ROOT, "bench")
MODELS = [
    {"key": "moss", "name": "MOSS-Image SFT", "short": "MOSS SFT", "settings": "25 steps · er_sde · CFG 2.5 · SLG 22"},
    {"key": "kromoss", "name": "Kromoss", "short": "Kromoss", "settings": "25 steps · er_sde · CFG 2.5 · SLG 22"},
    {"key": "dmd8", "name": "Kromoss + 8-step DMD LoRA", "short": "Kromoss 8-step", "settings": "8 steps · euler · CFG 1 · no SLG"},
]
SETS = [("A", "people, anatomy"), ("B", "groups, counting"), ("C", "sci-fi, fantasy, architecture"),
        ("D", "art styles"), ("E", "text, design, layout"), ("F", "lighting, technique, materials")]


def jsonl(path):
    return [json.loads(l) for l in open(path) if l.strip()] if os.path.exists(path) else []


prompts = [p for s, _ in SETS for p in jsonl(f"{B}/prompts_{s}.jsonl")]
results = {m["key"]: {r["id"]: r for r in jsonl(f"{B}/results_{m['key']}.jsonl")} for m in MODELS}
grades = {m["key"]: {g["id"]: g for s, _ in SETS for g in jsonl(f"{B}/reviews/{m['key']}/review_{s}.jsonl")} for m in MODELS}

out = []
for p in prompts:
    base = results["moss"][p["id"]]
    renders = {k: {"secs": r[p["id"]].get("secs"), "w": r[p["id"]]["w"], "h": r[p["id"]]["h"]}
               for k, r in results.items() if r.get(p["id"], {}).get("status") == "success"}
    out.append({"id": p["id"], "category": p.get("category"), "sub": p.get("sub"), "format": p.get("format"),
                "prompt": p["prompt"], "layout": p.get("layout"), "w": base["w"], "h": base["h"], "seed": base["seed"],
                "renders": renders,
                "grades": {k: g[p["id"]] for k, g in grades.items() if p["id"] in g}})


def stats(ids, key):
    gs = [grades[key][i] for i in ids if i in grades[key]]
    if not gs:
        return None
    checks = [c["result"] for g in gs for c in g["checks"]]
    return {"mean": round(statistics.mean(g["score"] for g in gs), 3), "pass": round(checks.count("pass") / len(checks), 3), "n": len(gs)}


summary = {}
for m in MODELS:
    k = m["key"]
    summary[k] = {s: stats([p["id"] for p in prompts if p["id"][0] == s], k) for s, _ in SETS}
    all_ = stats([p["id"] for p in prompts], k)
    summary[k]["all"] = all_ if all_ and all_["n"] == len(prompts) else None  # no "All 300" figure from a partial set
    secs = [r["secs"] for r in results[k].values() if r.get("secs")]
    summary[k]["secs"] = statistics.median(secs) if secs else None

note = ("Mean is the 1-5 grade; the percentage is the share of checklist items graded a full pass. Each model's images were "
        "graded by six reviewers (one per set) working from the same instructions, without seeing the other models' images. "
        "Grader-to-grader variation was not measured, so read small gaps with caution.")
footer = ("Rendered on Beast (RTX 5080 16 GB) with ComfyUI v0.41.0-18 (6607f36b), torch 2.12.1+cu130. Seeds are CRC32 of the "
          "prompt id, identical across the three models. Full-size images are JPEG q95 of the original PNG renders; the PNGs "
          "are in the repo's <a href=\"https://github.com/jo-nike/moss-kromoss-eval/releases\">releases</a>. Prompts, render "
          "logs, grades and runners: <a href=\"https://github.com/jo-nike/moss-kromoss-eval\">github.com/jo-nike/moss-kromoss-eval</a>.")
json.dump({"models": MODELS, "sets": [{"key": s, "name": n} for s, n in SETS], "summary": summary, "note": note,
           "footer": footer, "prompts": out}, open(f"{ROOT}/data.json", "w"), ensure_ascii=False, separators=(",", ":"))
print({k: (v["all"], v["secs"]) for k, v in summary.items()})
