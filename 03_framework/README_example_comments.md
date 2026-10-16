# Example comments (Table I of the paper, column "Example")

## Sources and licensing
- Stack Overflow comments come from the dataset compiled by Cheriyan, Savarimuthu and Cranefield for "Taming the Online Software Engineering Tongue" (Journal of Software 21(2), 2026, doi 10.17706/jsw.21.2.45-77): 311,073 Stack Overflow comments posted 2010 to 2020 with the community flag type of each comment (Rude Or Offensive 108,473; Unwelcoming or Unfriendly 28,030; declined flags 38,067; no flag 136,503). The dataset belongs to its authors and is not redistributed here; `comment_id` is the dataset's own identifier. Stack Overflow content is licensed CC BY-SA 4.0; attribution is given to the dataset and the identifiers allow each comment to be traced. No user names are reproduced.
- For nine attributes the dataset had no comment that matched the attribute definition. For these a public Hacker News comment in which a developer describes the attribute in their own words is used, marked "(HN)" in Table I. `comment_id` is "HN-" followed by the Hacker News item id, and the URL is given in `edit`. Hacker News comments are public; no user names are reproduced.
- The comments are public and the study involved no interaction with people.

## Selection procedure (one coder, 15 and 16 October 2026)
1. For each of the 48 attributes a small keyword set was defined (column `keywords_searched`, `*` marks a word stem) and every comment whose text matched a keyword was retrieved.
2. Candidates were restricted to 3 to 22 words, without URLs or code, and without slurs or profanity (a fixed word list). Matches were sorted by length, flagged comments first.
3. Among the shortest matches the coder chose one comment that illustrates the attribute as defined in `idaf_attributes.csv`. False matches (for example SQL UNION for union affiliation, "migrate to hooks" for immigration status, "disabled" buttons for physical abilities) were skipped.
4. Where only part of a comment is printed, `edit` says "excerpt" and the omission is marked with an ellipsis in Table I when it falls inside the printed text. User handles (@name) were removed. For comment 17738 a run of question marks was reduced to one.
5. Hacker News comments were retrieved through the HN Algolia search API on 16 October 2026 with the keywords listed in `keywords_searched`.

## File
`example_comments.csv`: attribute, comment_id, flag_type, creation_date, example_as_printed, original_comment_text, edit, keywords_searched.
