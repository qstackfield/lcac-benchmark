#!/usr/bin/env python3
"""
LCAC Leaderboard Generator
Aggregates participant results into results/leaderboard.md
"""

import json, pathlib, statistics

participants_dir = pathlib.Path("results/participants")
leaderboard_path = pathlib.Path("results/leaderboard.md")

rows = []
for f in sorted(participants_dir.glob("*.json")):
    try:
        data = json.load(open(f))
        trust = data["metrics"].get("trust_index", 0)
        model = data.get("model", "unknown")
        org = data.get("participant", "anonymous")
        verdict = data.get("verdict", "-")
        rows.append((trust, model, org, verdict))
    except Exception:
        continue

rows.sort(reverse=True)

with open(leaderboard_path, "w") as out:
    out.write("# LCAC Public Leaderboard\n\n")
    out.write("| Rank | Model | Organization | Trust Index | Verdict |\n")
    out.write("|------|--------|--------------|--------------|----------|\n")
    for i, (trust, model, org, verdict) in enumerate(rows, 1):
        out.write(f"| {i} | {model} | {org} | {trust:.3f} | {verdict} |\n")

print(f"[✓] Leaderboard updated → {leaderboard_path}")
