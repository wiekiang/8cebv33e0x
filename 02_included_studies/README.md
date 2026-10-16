# Included studies

- management_reviews.csv: the 32 management reviews (P1 to P32) that passed title and abstract screening, with a status column. Full-text reading excluded P2, P21 and P24 (status "excluded at full text", reason in the note column) because inclusion or equity in them did not refer to human diversity; the 29 with status "included" are the RQ1 corpus. These P-codes are the ones cited in Table I of the paper for the six added attributes.
- se_reviews.csv: the 34 software engineering records (P1 to P34) that passed title and abstract screening. Full-text reading excluded P9 and P18 (primary studies) and P16 (preprint, not peer reviewed), marked stratum "excluded"; the remaining 31 are the RQ2 corpus. Columns:
  - stratum: a = about people in software engineering, b = about software for diverse users, c = neither, borderline = people adjacent to software development (students, entrepreneurs) or a mixed design whose main contribution is an instrument (P30). Sizes: a = 14, b = 8, c = 4, borderline = 5, excluded = 3.
  - stratum_basis: "title and abstract" or "full text" (the eight papers whose review status was checked from the full text in October 2026).
  - review_status: "review" for the 31 included papers, "primary study" or "preprint, not peer reviewed" for the three excluded. P7, P12, P24 and P34 were confirmed as reviews from the full text; P34 and P30 are mixed designs with a systematic review component.
  - scope_tag: for the 14 stratum (a) reviews only. single_group = the review is about one group (P7, P10, P12, P14, P15, P23, P24, P34); broad = diversity in software engineering in general (P4, P13, P26, P27, P31, P33).
  - in_primary_analysis: yes for the 14 stratum (a) reviews used for the primary RQ2 analysis.
  - note: reason for the stratum or the status.
- Stratum (a) plus the five borderline reviews (P3, P17, P21, P28, P30) is the 19-review sensitivity set.
- P23 carries a 2014 publication year although the search window starts in 2015; it was retained because it was returned by the search and met the inclusion criteria.
