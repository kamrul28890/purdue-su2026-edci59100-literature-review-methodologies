# PRISMA-ScR chain reconciliation (terminates at 58)

## Verified from workbooks
- `Merged List.xlsx` Sheet1 = **90 rows** → confirms "90 unique records screened."
- Curated background/transition = **39** (all `source_database = Curated Workbook` → snowball/manual) → the Phase-2 set.
- Curated core = **19** (database-origin) → the Phase-1 included set.
- Raw identification (WoS 769 + Scopus 674 = 1443; → 123 after filters) lives only in original exports → **reported as recorded** (cannot be recomputed from available files).

## Recommended reconciled chain
**Identification**
- Database search (WoS 769 + Scopus 674 = 1443) → database subject/language/type filters → 123 → duplicates removed (−33) → **90 unique records** (database track).
- Backward snowballing of included papers' reference lists → **separate identification source** (Phase 2).

**Screening — database track (Phase 1)**
- 90 records → title/abstract screening (−32) → 58 sought for retrieval → full-text assessed → excluded at full text (−39) → **19 core VLM studies included**.

**Snowballing track (Phase 2)**
- Reference-chain identification → **39 background/transition studies included**.

**Included**
- Final corpus = 19 (database) + 39 (snowball) = **58 studies**.

## The one number needing author confirmation
The draft reported "**58 full-text assessed → 33 excluded → 25 included**" for the database track.
Under the reconciled corpus the database track yields **19** (not 25), because (a) Bui is removed and (b) the 5 transition papers came via snowball, not the database search.
So the database full-text exclusion becomes **−39** (58 − 19), and snowball becomes **39** (not 31).

Two awkward coincidences to avoid confusing readers:
- "58 sought for retrieval" (database track) vs "58 final corpus" are different sets that share the number 58.

## AUTHOR DECISION (confirmed 2026-06-27): Recommended reconciliation (R)
Final PRISMA numbers for the diagram:
- Identification (database): WoS 769 + Scopus 674 = 1443 → filters → 123 → duplicates removed (−33) → **90 unique** records.
- Identification (snowball): separate track, backward reference-chain.
- Screening (database): 90 → title/abstract (−32) → **58 sought/assessed** → full-text excluded (−39) → **19 included**.
- Snowball: **39 included**.
- **Final corpus = 19 + 39 = 58.**
- Note in caption: the "58 assessed (database track)" and the "58 final corpus" are distinct sets that coincidentally share the value 58.
