"""Cumulative growth of the attribute space by category, from the four seminal frameworks to IDAF.
Reads attribute_by_framework.csv (baseline, 42 attributes) and idaf_attributes.csv (48 attributes).
Python 3.9+, matplotlib. Run: python build_fig4_growth.py
"""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, "attribute_by_framework.csv"), encoding="utf-8-sig")))
idaf = list(csv.DictReader(open(os.path.join(HERE, "idaf_attributes.csv"), encoding="utf-8-sig")))
CATS = ["Core", "Fixed", "Variable", "Value foundations", "Workplace"]
COL = {"Core": "#7C3AED", "Fixed": "#2B6CB0", "Variable": "#2A9D8F", "Value foundations": "#ED8936", "Workplace": "#B91C1C"}
steps = [("LR_loden_rosener_1991", "Loden &\nRosener\n(1991)"), ("GR_gardenswartz_rowe_1998", "Gardenswartz\n& Rowe\n(1998)"),
         ("RC_rijamampianina_carmichael_2005", "Rijamampianina\n& Carmichael\n(2005)"), ("M_maier_2005", "Maier\n(2005)")]
seen, series, labels = set(), {c: [] for c in CATS}, []
for key, lab in steps:
    seen |= {r["attribute"] for r in rows if r[key] == "1"}
    for c in CATS: series[c].append(sum(1 for r in rows if r["attribute"] in seen and r["category_baseline"] == c))
    labels.append(lab)
for c in CATS: series[c].append(sum(1 for r in idaf if r["category"] == c))   # IDAF: additions and reassignments applied
labels.append("Contemporary\nreviews\n(2015 to 2026)")
totals = [sum(series[c][i] for c in CATS) for i in range(len(labels))]

f = 7.0
plt.rcParams.update({"font.size": f, "font.family": "DejaVu Sans", "pdf.fonttype": 42})
fig, ax = plt.subplots(figsize=(3.5, 2.4))
x = range(len(labels)); bottom = [0] * len(labels)
for c in CATS:
    ax.bar(x, series[c], 0.62, bottom=bottom, color=COL[c], label=c, zorder=3, edgecolor="white", linewidth=0.6)
    for i, v in enumerate(series[c]):
        if v >= 3: ax.text(i, bottom[i] + v / 2, str(v), ha="center", va="center", fontsize=f * 0.8, color="white")
    bottom = [b + v for b, v in zip(bottom, series[c])]
for i, t in enumerate(totals): ax.text(i, t + 0.8, str(t), ha="center", va="bottom", fontsize=f * 0.95, fontweight="bold")
ax.set_xticks(list(x)); ax.set_xticklabels(labels, fontsize=f * 0.78)
ax.set_ylim(0, 54); ax.set_yticks(range(0, 55, 12)); ax.set_ylabel("Cumulative number of attributes", fontsize=f)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
ax.grid(axis="y", color="#e3e3e3", lw=0.5, zorder=0); ax.set_axisbelow(True); ax.tick_params(length=2, pad=1)
ax.legend(loc="upper left", frameon=False, fontsize=f * 0.85, handlelength=1.0, ncol=1)
fig.subplots_adjust(left=0.13, right=0.99, top=0.98, bottom=0.2)
for ext, kw in (("pdf", {}), ("png", {"dpi": 300})): fig.savefig(os.path.join(HERE, "fig4_growth." + ext), **kw)
print(labels, totals, {c: series[c] for c in CATS})
