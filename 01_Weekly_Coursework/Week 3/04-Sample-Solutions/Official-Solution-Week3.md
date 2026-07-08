Official solution — Week 3: Initial search results & annotated bibliography

Context and continuity

- Builds on Week 1 topic exploration and Week 2 scoping-plan. Students should use the Week 2 search plan to retrieve candidate papers and produce an annotated bibliography and extraction table.

1. Goal for Week 3

- Produce a reproducible set of candidate papers (20–40) and an annotated bibliography for the top 10–15 most relevant items. Complete data extraction for each annotated item.

2. Example search-log entry (model)

- Database: IEEE Xplore
- Date: 2026-05-30
- Search string: ("vision-language" OR "vision language" OR "VLM" OR "multimodal model") AND ("spatiotemporal" OR "temporal reasoning" OR "activity recognition") AND (construction OR "construction site")
- Results returned: 312 — after title/abstract screen: 38 candidates — after full-text screen: 22 included

3. Annotated bibliography template (for each item)

- Citation: authors, year, venue
- One-sentence summary: core contribution
- Methods / model: datasets, model type, tasks
- Key findings: metrics, evaluation context
- Relevance to research question: 1–2 sentences
- Limitations and notes: dataset size, setting, generalizability

4. Two sample annotated entries (model)

- Smith et al. (2023). "Multimodal temporal reasoning for activity detection" — CVPR Workshop.
  - Summary: Proposes a transformer-based VLM adapted for short video reasoning.
  - Methods: Uses a custom construction-site-like dataset with annotated actions; combines image frames and natural-language prompts.
  - Findings: 78% top-1 accuracy on action classification; temporal consistency improved with spatiotemporal attention.
  - Relevance: Demonstrates feasibility of VLMs for action recognition in construction-like footage.
  - Limitations: Small dataset and synthetic scenarios; no field deployment.

- Lee & Gomez (2022). "Field deployment of multimodal safety monitoring" — Journal of Construction Engineering.
  - Summary: Case study deploying a multimodal monitoring pipeline (vision + sensor metadata) on an active site.
  - Methods: Pipeline integrates object detection and simple rule-based temporal logic to flag unsafe behaviours; limited natural-language grounding.
  - Findings: Improved hazard detection rates vs baseline but high false positives in cluttered scenes.
  - Relevance: Practical deployment issues and integration challenges for real-world sites.
  - Limitations: Not using modern VLMs; limited generalizability beyond a single site.

5. Data extraction table (columns — model)

- ID | Citation | Year | Venue | Dataset(s) | Model type | Task | Metrics | Deployment context | Key findings | Limitations

6. Week 3 marking rubric (50 points)

- Search reproducibility & coverage — 15 pts: Clear search logs, appropriate databases, and evidence of iterative refinement (15).
- Relevance & selection — 10 pts: Candidate corpus size appropriate; justification for included items (10).
- Annotated bibliography quality — 15 pts: Concise summaries, correct methods, clear relevance statements (15).
- Data extraction completeness — 10 pts: All required fields filled for annotated items (10).

7. Instructor notes

- Expect variation in corpus size; judge whether students reasonably limited the scope given time and resources.
- For students with small candidate pools, check that search strings and databases were reasonable before marking down.

File saved as: Week 3/Official-Solution-Week3.md
