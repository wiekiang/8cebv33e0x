# Coding

- coding_matrix_management.csv: the management coding matrix, 48 IDAF attributes (rows) by 32 reviews (P1 to P32, columns), 1 = the review mentions the attribute. The attribute recorded as "Digital Trust" during coding is the IDAF attribute Trust.
- coding_matrix_se.csv: the software engineering coding matrix, 48 attributes by 34 reviews (P1 to P34), 1 = mentioned. Same attribute names as the management matrix. Organizational level, work experience and work style are coded in the Workplace category (Section IV-C of the paper).
- candidate_not_accepted_social_identity.csv: the one candidate attribute recorded during coding of the management reviews (three reviews) but not accepted into IDAF under the acceptance rule of Section III-A. It is excluded from all counts and figures.
- se_specific_terms.csv: the 20 software engineering specific terms noted during coding of the SE reviews that IDAF does not name, grouped and tested against the acceptance rule. They were noted without a per-review count and are the basis of recommendation 5 in Section VI-A (technical role, contribution type, community reputation).
- coverage_counts.csv: for each attribute, the number of the 32 management reviews and of the 34 software engineering reviews that mention it, written by build_counts.py. Dividing by 32 and 34 gives the percentages in Section V and Fig. 5.
- build_counts.py: rebuilds coverage_counts.csv from the two matrices and prints the headline numbers of Sections V and VI.
- build_fig5_bars.py: draws Fig. 5 (fig5_coverage_bars.pdf/.png) from coverage_counts.csv.
- Reliability: see ../05_reliability.

## Reproduce
```
python -m pip install matplotlib
cd 04_coding
python build_counts.py
python build_fig5_bars.py
```
Python 3.9 or later. The scripts use relative paths only.
