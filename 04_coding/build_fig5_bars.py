"""Fig. 5 of the paper: grouped vertical bars (management vs software engineering) per attribute,
grouped by IDAF category. Reads coverage_counts.csv written by build_counts.py (run that first).
Python 3.9+, matplotlib. Run: python build_fig5_bars.py
"""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, "coverage_counts.csv"), encoding="utf-8-sig")))
KM = next(k for k in rows[0] if k.startswith("mgmt_count_of_")); NM = int(KM.rsplit("_", 1)[1])
KS = next(k for k in rows[0] if k.startswith("se_count_of_")); NS = int(KS.rsplit("_", 1)[1])
for r in rows: r[KM], r[KS] = int(r[KM]), int(r[KS])

CATS = ["Core", "Fixed", "Variable", "Value foundations", "Workplace"]
C_M, C_S = "#2B6CB0", "#ED8936"          # management blue, software engineering orange
BAND = ["#f4f6fa", "#ffffff"]
f = 7.0
plt.rcParams.update({"font.size": f, "font.family": "DejaVu Sans", "pdf.fonttype": 42})

order, bounds = [], []
for c in CATS:
    block = sorted([r for r in rows if r["category"] == c], key=lambda r: (-r[KS], -r[KM], r["attribute"]))
    bounds.append((c, len(order), len(order) + len(block)))
    order += block

PER_ROW = 24
nrows = -(-len(order) // PER_ROW)
fig, axes = plt.subplots(nrows, 1, figsize=(7.16, 2.9 * nrows))
w = 0.38
for row, ax in enumerate(axes):
    seg = order[row * PER_ROW:(row + 1) * PER_ROW]; off = row * PER_ROW
    for i, r in enumerate(seg):
        pm, ps = 100 * r[KM] / NM, 100 * r[KS] / NS
        ax.bar(i - w / 2, pm, w, color=C_M, zorder=3)
        ax.bar(i + w / 2, ps, w, color=C_S, zorder=3)
        for xx, n, p, col in ((i - w / 2, r[KM], pm, C_M), (i + w / 2, r[KS], ps, C_S)):
            ax.text(xx, p + 1.5, "%d (%.0f%%)" % (n, p) if n else "0", rotation=90, ha="center", va="bottom", fontsize=f * 0.72, color=col)
    k0 = 0
    for k, (c, a, b) in enumerate(bounds):
        lo, hi = max(a, off), min(b, off + len(seg))
        if lo >= hi: continue
        ax.axvspan(lo - off - 0.5, hi - off - 0.5, color=BAND[k % 2], lw=0, zorder=0)
        label = c.upper() + (" (CONT.)" if a < off else "")
        ax.text((lo + hi - 1) / 2 - off, 110, label, ha="center", va="bottom", fontsize=f * 0.95, fontweight="bold", color="#333")
        if lo > off: ax.axvline(lo - off - 0.5, color="#c8c8c8", lw=0.6, zorder=2)
    ax.set_xticks(range(len(seg))); ax.set_xticklabels([r["attribute"] for r in seg], rotation=55, ha="right", rotation_mode="anchor", fontsize=f * 0.92)
    ax.set_xlim(-0.6, PER_ROW - 0.4); ax.set_ylim(0, 120)
    ax.set_yticks(range(0, 101, 20)); ax.set_yticklabels(["%d%%" % v for v in range(0, 101, 20)], fontsize=f * 0.9)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    ax.spines["left"].set_color("#999"); ax.spines["bottom"].set_color("#999")
    ax.grid(axis="y", color="#e3e3e3", lw=0.5, zorder=1); ax.set_axisbelow(True); ax.tick_params(length=2, pad=1)
axes[1].legend(handles=[Patch(color=C_M, label="Management reviews (n = %d)" % NM), Patch(color=C_S, label="Software engineering reviews (n = %d)" % NS)],
               loc="upper left", bbox_to_anchor=(0.52, 0.92), frameon=False, fontsize=f * 0.95, handlelength=1.2)
fig.supylabel("Share of reviews mentioning the attribute", fontsize=f, x=0.012)
fig.tight_layout(rect=(0.02, 0, 1, 1), h_pad=1.0)
for ext, kw in (("pdf", {}), ("png", {"dpi": 300})): fig.savefig(os.path.join(HERE, "fig5_coverage_bars." + ext), **kw)
print("wrote fig5_coverage_bars.pdf/.png")
