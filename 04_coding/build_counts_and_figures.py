"""Rebuild every coverage count in the paper and Fig. 3 from the two coding matrices.

Inputs (relative to this folder): coding_matrix_management.csv, coding_matrix_se.csv,
../02_included_studies/management_reviews.csv (status), ../02_included_studies/se_reviews.csv (stratum and scope tags),
../03_framework/idaf_attributes.csv (categories). Reviews excluded at full text keep their matrix columns but are
filtered out here by the status and stratum columns, so every count can be reproduced with or without them.
Outputs: coverage_counts.csv, fig3_coverage.pdf/.png (the paper's Fig. 3), and a printed summary.
Python 3.9+, matplotlib. Run: python build_counts_and_figures.py
"""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))
def rd(p): return list(csv.DictReader(open(os.path.join(HERE, p), encoding="utf-8-sig")))

mg = {r["attribute"]: r for r in rd("coding_matrix_management.csv")}
se = {r["attribute"]: r for r in rd("coding_matrix_se.csv")}
mreviews = rd("../02_included_studies/management_reviews.csv")
reviews = [r for r in rd("../02_included_studies/se_reviews.csv") if r["stratum"] != "excluded"]
cats = {r["attribute"]: r["category"] for r in rd("../03_framework/idaf_attributes.csv")}
cats = {k.lower(): v for k, v in cats.items()}
MP = [r["code"] for r in mreviews if r["status"] == "included"]
A = [r["code"] for r in reviews if r["stratum"] == "a"]
B = [r["code"] for r in reviews if r["stratum"] == "b"]
BORDER = [r["code"] for r in reviews if r["stratum"] == "borderline"]
ALL = [r["code"] for r in reviews]
BROAD = [r["code"] for r in reviews if r["scope_tag"] == "broad"]
SINGLE = [r["code"] for r in reviews if r["scope_tag"] == "single_group"]

def count(mat, attr, cols): return sum(int(mat[attr][c]) for c in cols)
attrs = sorted(mg)
rows = []
for a in attrs:
    rows.append({"attribute": a, "category": cats[a.lower()],
                 "mgmt_count_of_%d" % len(MP): count(mg, a, MP), "se_stratum_a_count_of_%d" % len(A): count(se, a, A),
                 "se_a_plus_borderline_count_of_%d" % len(A + BORDER): count(se, a, A + BORDER), "se_stratum_b_count_of_%d" % len(B): count(se, a, B),
                 "se_all_count_of_%d" % len(ALL): count(se, a, ALL), "se_broad_scope_count_of_%d" % len(BROAD): count(se, a, BROAD),
                 "se_single_group_count_of_%d" % len(SINGLE): count(se, a, SINGLE)})
KM, KA = "mgmt_count_of_%d" % len(MP), "se_stratum_a_count_of_%d" % len(A)
with open(os.path.join(HERE, "coverage_counts.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

def covered(cols): return sum(1 for a in attrs if count(se, a, cols) > 0)
print("stratum (a) n=%d: %d of 48 attributes covered" % (len(A), covered(A)))
print("a + borderline n=%d: %d covered; all n=%d: %d covered" % (len(A + BORDER), covered(A + BORDER), len(ALL), covered(ALL)))
print("management n=%d: %d of 48 covered" % (len(MP), sum(1 for a in attrs if count(mg, a, MP) > 0)))
for a in sorted(attrs, key=lambda a: -count(mg, a, MP))[:10]:
    print("  management %-20s %2d (%.0f%%)   SE(a) %2d (%.0f%%)" % (a, count(mg, a, MP), 100 * count(mg, a, MP) / len(MP), count(se, a, A), 100 * count(se, a, A) / len(A)))
print("mean attributes per stratum (a) review: %.1f (broad %.1f, single-group %.1f)" % (
    sum(count(se, a, A) for a in attrs) / len(A), sum(count(se, a, BROAD) for a in attrs) / len(BROAD),
    sum(count(se, a, SINGLE) for a in attrs) / len(SINGLE)))

# ---- Fig. 3: shared percentage axis, grouped by category ----
COLORS = {"m": "#7a7a7a", "s": "#1f5fbf"}
CATS = ["Core", "Fixed", "Variable", "Value foundations", "Workplace"]
f = 6.5
plt.rcParams.update({"font.size": f, "font.family": "DejaVu Sans", "pdf.fonttype": 42})
order = []
for c in CATS:
    block = [r for r in rows if r["category"] == c]
    block.sort(key=lambda r: (-r[KA], -r[KM], r["attribute"]))
    order.append(("cat", c)); order += [("attr", r) for r in block]
fig, ax = plt.subplots(figsize=(7.16, 4.9)); y = len(order) - 1
for kind, item in order:
    if kind == "cat":
        ax.text(-1.5, y, item.upper(), ha="right", va="center", fontsize=f * 0.95, fontweight="bold")
        ax.axhspan(y - 0.5, y + 0.5, color="#f0f0f0", lw=0)
    else:
        m, s = item[KM], item[KA]
        pm, ps = 100 * m / len(MP), 100 * s / len(A)
        lc = COLORS["s"] if ps > pm else (COLORS["m"] if pm > ps else "#c9c9c9")  # connector takes the colour of the higher domain
        ax.plot([pm, ps], [y, y], color=lc, lw=1.4, alpha=0.45, zorder=1)
        ax.scatter([pm], [y], s=22, color=COLORS["m"], zorder=3, edgecolor="white", lw=0.5)
        ax.scatter([ps], [y], s=22, color=COLORS["s"], zorder=4, marker="D", edgecolor="white", lw=0.5)
        ax.text(-1.5, y, item["attribute"], ha="right", va="center", fontsize=f * 0.95)
        lo, hi = min(pm, ps), max(pm, ps)
        if hi - lo < 4: ax.text(hi + 1.6, y, "%d | %d" % (m, s), va="center", fontsize=f * 0.8, color="#333")
        else:
            lab_lo, col_lo = (str(m), COLORS["m"]) if pm <= ps else (str(s), COLORS["s"])
            lab_hi, col_hi = (str(s), COLORS["s"]) if pm <= ps else (str(m), COLORS["m"])
            ax.text(lo + 1.6 if lo < 3 else lo - 1.6, y, lab_lo, va="center", ha="left" if lo < 3 else "right", fontsize=f * 0.8, color=col_lo)
            ax.text(hi + 1.6, y, lab_hi, va="center", ha="left", fontsize=f * 0.8, color=col_hi)
    y -= 1
ax.set_xlim(0, 100); ax.set_ylim(-0.7, len(order) - 0.3); ax.set_yticks([])
ax.set_xticks(range(0, 101, 20)); ax.set_xticklabels(["%d%%" % v for v in range(0, 101, 20)], fontsize=f * 0.9)
ax.set_xlabel("Share of reviews mentioning the attribute", fontsize=f, labelpad=2)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
ax.grid(axis="x", color="#e3e3e3", lw=0.5); ax.set_axisbelow(True); ax.tick_params(axis="x", length=2, pad=1)
ax.legend(handles=[Line2D([], [], marker="o", color=COLORS["m"], ls="", ms=5, label="Management reviews (n = %d)" % len(MP)),
                   Line2D([], [], marker="D", color=COLORS["s"], ls="", ms=4.5, label="SE reviews about people in SE (n = %d)" % len(A)),
                   Line2D([], [], color=COLORS["m"], lw=1.4, alpha=0.45, label="Gap, management higher"),
                   Line2D([], [], color=COLORS["s"], lw=1.4, alpha=0.45, label="Gap, SE higher")],
          loc="lower right", frameon=False, fontsize=f * 0.95, handletextpad=0.4)
fig.subplots_adjust(left=0.24, right=0.99, top=0.995, bottom=0.07)
for ext, kw in (("pdf", {}), ("png", {"dpi": 300})): fig.savefig(os.path.join(HERE, "fig3_coverage." + ext), **kw)
print("wrote coverage_counts.csv and fig3_coverage.pdf/.png")
