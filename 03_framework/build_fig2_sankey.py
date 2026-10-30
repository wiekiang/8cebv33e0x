"""Fig. 2 of the paper: Sankey flow from the four seminal frameworks, through the five categories,
to the 42 baseline attributes. Reads attribute_by_framework.csv (baseline categories).
Python 3.9+, plotly and kaleido (python -m pip install plotly kaleido). Run: python build_fig2_sankey.py
Writes fig2_sankey.html (interactive) and fig2_sankey.png.
"""
import csv, os
import plotly.graph_objects as go

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, "attribute_by_framework.csv"), encoding="utf-8-sig")))
FW = [("LR_loden_rosener_1991", "Loden & Rosener (1991)"), ("GR_gardenswartz_rowe_1998", "Gardenswartz & Rowe (1998)"),
      ("RC_rijamampianina_carmichael_2005", "Rijamampianina & Carmichael (2005)"), ("M_maier_2005", "Maier (2005)")]
CATS = ["Core", "Fixed", "Variable", "Value foundations", "Workplace"]
CAT_COL = {"Core": "#7C3AED", "Fixed": "#2B6CB0", "Variable": "#2A9D8F", "Value foundations": "#ED8936", "Workplace": "#B91C1C"}
FW_COL = ["#1B4332", "#2D6A4F", "#52B788", "#74C69D"]
DEG_COL = {1: "#B7E4C7", 2: "#52B788", 3: "#2D6A4F", 4: "#1B4332"}

def rgba(hexcol, a): return "rgba(%d,%d,%d,%.2f)" % (int(hexcol[1:3], 16), int(hexcol[3:5], 16), int(hexcol[5:7], 16), a)
cat_of = {r["attribute"]: r["category_baseline"] for r in rows}
sets = {k: {r["attribute"] for r in rows if r[k] == "1"} for k, _ in FW}
deg = {r["attribute"]: int(r["n_frameworks"]) for r in rows}

labels, colors, xs, ys = [], [], [], []
for i, (k, name) in enumerate(FW):
    labels.append("%s  (%d)" % (name, len(sets[k]))); colors.append(FW_COL[i]); xs.append(0.01); ys.append((i + 0.5) / len(FW))
cat_node = {}
for i, c in enumerate(CATS):
    n = sum(1 for a in cat_of if cat_of[a] == c)
    cat_node[c] = len(labels); labels.append("%s  (%d)" % (c, n)); colors.append(CAT_COL[c]); xs.append(0.42); ys.append((i + 0.5) / len(CATS))
ordered = [a for c in CATS for a in sorted(a2 for a2 in cat_of if cat_of[a2] == c)]
attr_node = {}
for i, a in enumerate(ordered):
    attr_node[a] = len(labels); labels.append("%s  %s" % (a, "●" * deg[a])); colors.append(DEG_COL[deg[a]]); xs.append(0.99); ys.append((i + 0.5) / len(ordered))

src, tgt, val, lcol = [], [], [], []
for i, (k, _) in enumerate(FW):
    for c in CATS:
        n = sum(1 for a in sets[k] if cat_of[a] == c)
        if n: src.append(i); tgt.append(cat_node[c]); val.append(n); lcol.append(rgba(FW_COL[i], 0.30))
for a in ordered:
    src.append(cat_node[cat_of[a]]); tgt.append(attr_node[a]); val.append(1); lcol.append(rgba(CAT_COL[cat_of[a]], 0.30))

fig = go.Figure(go.Sankey(arrangement="snap",
    node=dict(pad=4, thickness=18, line=dict(color="#555", width=0.5), label=labels, color=colors, x=xs, y=ys),
    link=dict(source=src, target=tgt, value=val, color=lcol)))
fig.update_layout(font=dict(size=18, family="Arial"), width=2400, height=1400, margin=dict(l=10, r=10, t=60, b=60),
    paper_bgcolor="white", plot_bgcolor="white",
    annotations=[dict(x=0.005, y=1.03, xref="paper", yref="paper", text="<b>Seminal frameworks</b>", showarrow=False, xanchor="left", font=dict(size=15)),
                 dict(x=0.42, y=1.03, xref="paper", yref="paper", text="<b>Category</b>", showarrow=False, xanchor="center", font=dict(size=15)),
                 dict(x=0.995, y=1.03, xref="paper", yref="paper", text="<b>Baseline attributes (dots = number of frameworks naming it)</b>", showarrow=False, xanchor="right", font=dict(size=15))])
fig.write_html(os.path.join(HERE, "fig2_sankey.html"))
try:
    fig.write_image(os.path.join(HERE, "fig2_sankey_rebuilt.png"), scale=2)
except Exception as e:  # kaleido needs a Chrome binary (plotly_get_chrome); the HTML is still written
    print("PNG export skipped:", str(e).strip().splitlines()[0] if str(e).strip() else type(e).__name__)
print("wrote fig2_sankey.html; %d attributes, %d links" % (len(ordered), len(src)))
