"""Rebuild every coverage count in the paper from the two coding matrices.

Inputs (relative to this folder): coding_matrix_management.csv, coding_matrix_se.csv,
../02_included_studies/management_reviews.csv, ../02_included_studies/se_reviews.csv (the review lists),
../03_framework/idaf_attributes.csv (categories). All 32 management reviews and all 34 software engineering reviews are included.
Outputs: coverage_counts.csv (read by build_fig5_bars.py) and a printed summary of the headline numbers.
Python 3.9+, standard library only. Run: python build_counts.py
"""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
def rd(p): return list(csv.DictReader(open(os.path.join(HERE, p), encoding="utf-8-sig")))

mg = {r["attribute"]: r for r in rd("coding_matrix_management.csv")}
se = {r["attribute"]: r for r in rd("coding_matrix_se.csv")}
mreviews = rd("../02_included_studies/management_reviews.csv")
reviews = rd("../02_included_studies/se_reviews.csv")
cats = {r["attribute"]: r["category"] for r in rd("../03_framework/idaf_attributes.csv")}
cats = {k.lower(): v for k, v in cats.items()}
MP = [r["code"] for r in mreviews]
ALL = [r["code"] for r in reviews]

def count(mat, attr, cols): return sum(int(mat[attr][c]) for c in cols)
attrs = sorted(mg)
rows = []
for a in attrs:
    rows.append({"attribute": a, "category": cats[a.lower()],
                 "mgmt_count_of_%d" % len(MP): count(mg, a, MP), "se_count_of_%d" % len(ALL): count(se, a, ALL)})
KM, KA = "mgmt_count_of_%d" % len(MP), "se_count_of_%d" % len(ALL)
with open(os.path.join(HERE, "coverage_counts.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

def covered(cols): return sum(1 for a in attrs if count(se, a, cols) > 0)
print("software engineering n=%d: %d of 48 attributes covered" % (len(ALL), covered(ALL)))
print("management n=%d: %d of 48 covered" % (len(MP), sum(1 for a in attrs if count(mg, a, MP) > 0)))
for a in sorted(attrs, key=lambda a: -count(mg, a, MP))[:10]:
    print("  management %-20s %2d (%.0f%%)   SE %2d (%.0f%%)" % (a, count(mg, a, MP), 100 * count(mg, a, MP) / len(MP), count(se, a, ALL), 100 * count(se, a, ALL) / len(ALL)))
for a in sorted(attrs, key=lambda a: -count(se, a, ALL))[:10]:
    print("  SE         %-20s %2d (%.0f%%)   mgmt %2d (%.0f%%)" % (a, count(se, a, ALL), 100 * count(se, a, ALL) / len(ALL), count(mg, a, MP), 100 * count(mg, a, MP) / len(MP)))
print("mean attributes per SE review: %.1f" % (sum(count(se, a, ALL) for a in attrs) / len(ALL)))


def n_mentioned(mat, cols, lo, hi): return sum(1 for a in attrs if lo <= count(mat, a, cols) <= hi)
print("SE attributes mentioned by no review: %d; by one or two reviews: %d" % (n_mentioned(se, ALL, 0, 0), n_mentioned(se, ALL, 1, 2)))
for c in sorted(set(cats.values())):
    inc = [a for a in attrs if cats[a.lower()] == c]
    print("  %-18s %2d attributes, %2d mentioned in SE, %2d in management" % (c, len(inc), sum(1 for a in inc if count(se, a, ALL)), sum(1 for a in inc if count(mg, a, MP))))
per = [sum(int(se[a][c]) for a in attrs) for c in ALL]
print("attributes per SE review: mean %.1f, range %d to %d" % (sum(per) / len(per), min(per), max(per)))
print("wrote coverage_counts.csv")
