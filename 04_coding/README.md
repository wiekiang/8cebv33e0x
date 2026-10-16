# Coding

- coding_matrix_management.csv: the management coding matrix, 48 IDAF attributes (rows) by 32 reviews (P1 to P32, columns), 1 = the review mentions the attribute. The columns of P2, P21 and P24 are kept for transparency but excluded from all counts (see ../02_included_studies/management_reviews.csv). The attribute recorded as "Digital Trust" during coding is the IDAF attribute Trust.
- candidate_not_accepted_social_identity.csv: the one candidate attribute recorded during coding (three reviews) but not accepted into IDAF (Section III-A of the paper). It is excluded from all counts and figures.
- coding_matrix_se.csv: the software engineering coding matrix, 48 attributes by 34 records (P1 to P34), 1 = mentioned. The columns of P9, P16 and P18 are kept but excluded from all counts. Same attribute names as the management matrix. Organizational level is coded in the Workplace category.
- coverage_counts.csv: counts derived from the two matrices by build_counts_and_figures.py: management over 29 reviews; SE for stratum (a) (14 reviews, primary analysis), stratum (a) plus the five borderline reviews (19), stratum (b) (8), the full corpus (31), and the broad-scope and single-group subsets of stratum (a).
- fig1_prisma.jpg: Fig. 1 of the paper, the selection flow drawn from the funnel counts in ../01_search/search_strategy.md.
- fig2_idaf.jpg: Fig. 2 of the paper, the IDAF wheel drawn from ../03_framework/idaf_attributes.csv.
- build_counts_and_figures.py: rebuilds coverage_counts.csv and Fig. 3 of the paper (fig3_coverage.pdf, and a .png copy) from the matrices and the stratum tags in ../02_included_studies/se_reviews.csv, and prints the headline numbers (28 of 48 covered in stratum (a), 32 in the 19-review set, 35 in the full corpus, 45 in management, mean attributes per review).
- se_specific_terms.csv: the 20 terms noted during coding of the SE reviews that IDAF does not name (Section V-C), grouped and tested against the acceptance rule. They were noted without a per-review count.
- Reliability: extraction and coding were done by one author (Section III-C of the paper); no second-coder matrix is included.

## Reproduce
```
python -m pip install matplotlib
cd 04_coding
python build_counts_and_figures.py
```
Python 3.9 or later. The script uses relative paths only.
