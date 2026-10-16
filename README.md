# Replication package: An Integrated Diversity Attribute Framework (IDAF) for Software Engineering: A Cross-Domain Analysis of Diversity Attributes

Anonymised for double-anonymous review. The public DOI replaces this note at camera-ready.

## Overview
This package contains everything needed to re-derive the numbers in the paper: the search strategy and selection funnel for both corpora, the lists of included reviews with their strata, the 48-attribute framework with definitions and provenance, the two coding matrices, and one script that rebuilds every coverage count and Fig. 3 from the matrices. Fig. 1 (the selection flow) is a drawing of the funnel counts in 01_search and has no script. The Stack Overflow comment dataset used for the Table I examples belongs to its authors (Cheriyan et al., 2026, doi 10.17706/jsw.21.2.45-77) and is not redistributed; the comment identifiers are listed instead.

## Contents
- 01_search/ search strings, databases and record counts, filters, date ranges, and the selection funnel for both domains.
- 02_included_studies/ the 29 management reviews and the 31 software engineering reviews (plus the six papers excluded at full text), with the stratum classification and scope tags of the SE reviews.
- 03_framework/ the five category definitions, the attribute by framework matrix (42 baseline attributes by the four seminal frameworks, with baseline and IDAF category), the 48 IDAF attributes with full definitions, sources, origin and flags, and the Table I example comments with their identifiers, sources and selection notes.
- 04_coding/ the two coding matrices, the coverage counts for every stratum, and the script that rebuilds the counts and Fig. 3.

## How to reproduce
Python 3.9 or later with matplotlib (`python -m pip install matplotlib`). Then:
```
cd 04_coding
python build_counts_and_figures.py   # coverage_counts.csv, fig3_coverage.pdf/.png, headline numbers
```

## Known limitations
- The stratum classification and scope tags were made from titles and abstracts and confirmed from the full texts for the eight papers whose review status was in doubt; the other classifications rest on titles and abstracts.
- Coding was done by one author; no second-coder matrix is included.

## License
Data and documentation: CC BY 4.0. Code: MIT.

## Citation
Anonymous authors. Replication package for "An Integrated Diversity Attribute Framework (IDAF) for Software Engineering: A Cross-Domain Analysis of Diversity Attributes", submitted for review. DOI to be added at camera-ready.
