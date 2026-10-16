# Search strategy (both searches run in April 2026)

## Management domain (RQ1 extension)
- Search string: (diversity OR equity OR inclusion) AND (management OR managing)
- Databases and records: Web of Science (22), PsycINFO (21), Business Source Complete (13), ScienceDirect (6), Scopus (29), ABI/INFORM Global (23). Total 114.
- Filters: management subject category where available; English; title and abstract; review-type documents where the database offers the filter (review status confirmed at screening).
- Date range: 2015 to April 2026.
- Funnel: 114 identified -> 80 after deduplication -> 40 excluded (not a review paper), 8 excluded (not human diversity) -> 32 read in full -> 3 excluded at full text (not human diversity: financial inclusion, brand equity, social equity as a policy goal) -> 29 included.

## Software engineering domain (RQ2 application)
- Search string: (diversity OR equity OR inclusion) AND ("software engineering" OR "software development") AND ("systematic review" OR "literature review" OR "systematic mapping")
- Databases and records: ACM Digital Library (150), IEEE Xplore (65), Scopus (254), Web of Science (155), ScienceDirect (46), Wiley (48), Springer (200). Google Scholar (30) was a validation search, run to check whether relevant reviews had been missed by the seven databases; its records were pooled before deduplication. Total 948.
- Filters: English; title and abstract.
- Date range: 2015 to April 2026, the same window as the management search. P23 (Khan and Azeem) carries a 2014 publication year; it was returned by the search, met the inclusion criteria, and was retained.
- Funnel: 948 identified -> 614 after deduplication -> 580 excluded (not an SE review, or not focused on EDI from a human perspective) -> 34 read in full -> 3 excluded at full text (2 primary studies, 1 preprint not peer reviewed) -> 31 included.
- Stratification: each included review was classified from title and abstract as (a) about people in SE, (b) about software for diverse users, (c) neither, or borderline, and the classification and review status were confirmed from the full texts. See 02_included_studies/se_reviews.csv.

## Selection flow diagram
- Fig. 1 of the paper shows the funnel counts above; it was drawn by hand from them and has no script.
- Screening was done on titles and abstracts; exclusion reasons were recorded at the level of the funnel counts above, not per record. Full-text exclusions are recorded per paper in 02_included_studies.
