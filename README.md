# Replication package: An Integrated Diversity Attribute Framework (IDAF) for Software Engineering: A Cross-Domain Analysis of Diversity Attributes

Anonymised for double-anonymous review. The public DOI replaces this note at camera-ready.

## Overview
This package contains everything needed to re-derive the numbers and figures in the paper: the search strategy and selection funnel for both corpora, the lists of the 32 management reviews and the 34 software engineering reviews, the 48-attribute framework with definitions and provenance, the Table I example comments with their identifiers, the two coding matrices, the second-coder check, and the scripts that rebuild every coverage count and Figs. 2, 4 and 5 from the data files. Fig. 1 (the selection flow) and Fig. 3 (the IDAF wheel) are drawings and have no script. The Stack Overflow comment dataset used for the Table I examples belongs to its authors (Cheriyan et al., 2026, doi 10.17706/jsw.21.2.45-77) and is not redistributed; the comment identifiers are listed instead.

## Contents
- 01_search/ search strings, databases and record counts, filters, date ranges, and the selection funnel for both domains; fig1_prisma.jpg (Fig. 1).
- 02_included_studies/ the 32 management reviews (P1 to P32) and the 34 software engineering reviews (P1 to P34).
- 03_framework/ the five category definitions (Table II), the attribute by framework matrix (42 baseline attributes by the four seminal frameworks, with baseline and IDAF category), the 48 IDAF attributes with full definitions, sources, origin and flags (Table I), the example comments with their identifiers and selection notes, fig2_sankey.png (Fig. 2) with its script, fig3_idaf.jpg (Fig. 3), and fig4_growth.png/.pdf (Fig. 4) with its script.
- 04_coding/ the two coding matrices, the one candidate attribute not accepted, the software engineering specific terms noted during coding, the derived coverage counts, and the scripts that rebuild the counts and Fig. 5.
- 05_reliability/ the second-coder check of the software engineering coding (Section III-B of the paper).

## How to reproduce
Python 3.9 or later with matplotlib (`python -m pip install matplotlib`); Fig. 2 additionally needs plotly and kaleido. Then:
```
cd 04_coding
python build_counts.py        # coverage_counts.csv and the headline numbers of Section V
python build_fig5_bars.py     # fig5_coverage_bars.pdf/.png (Fig. 5)
cd ../03_framework
python build_fig4_growth.py   # fig4_growth.pdf/.png (Fig. 4)
python build_fig2_sankey.py   # fig2_sankey.html, and fig2_sankey_rebuilt.png when kaleido can find a Chrome binary
```
All scripts use relative paths only. The headline numbers printed by build_counts.py (35 of 48 attributes covered in software engineering, 45 in management, 13 unmentioned and 12 in one or two reviews, 7.6 attributes per review, range 1 to 14) are the ones reported in Sections V and VI.

## Known limitations
- Extraction and coding were done by one author and independently verified by a second author (05_reliability); no fully independent double coding was performed.
- Coverage is presence based: a review that mentions an attribute in passing counts the same as one that analyzes it.
- Screening exclusion reasons were recorded at the level of the funnel counts, not per record.

## License
Data and documentation: CC BY 4.0. Code: MIT.

## Citation
Anonymous authors. Replication package for "An Integrated Diversity Attribute Framework (IDAF) for Software Engineering: A Cross-Domain Analysis of Diversity Attributes", submitted for review. DOI to be added at camera-ready.
