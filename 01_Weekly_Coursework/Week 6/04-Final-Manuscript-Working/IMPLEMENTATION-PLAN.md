# Final Manuscript — Implementation Plan

> **For agentic workers:** Implement task-by-task. Steps use checkbox (`- [ ]`) syntax. This is an academic-manuscript build, not a code project: "verification" = LaTeX compiles cleanly **and** every number/figure matches `curated_58` **and** every `\cite{}` resolves. There is no git repo; checkpoints are *compile-and-verify*, not commits. Do not run `git init` without asking the author.

**Goal:** Transform the Week 5 draft (49/50) into the AutoCon-grade final manuscript by rebuilding all numbers from `curated_58`, executing Dr. Lowell's synthesis feedback, resolving all corpus-achievable reviewer issues, and adding the required Abstract + Next Steps.

**Architecture:** Single LaTeX manuscript built from the Week 5 `.tex`. A one-time Python data-build step regenerates every number and the 5 new tables/figures from the authoritative dataset, written to a `data_build/` artifacts folder that the prose tasks consume. Content edits proceed section-by-section, each ending in a compile-and-verify checkpoint.

**Tech Stack:** LaTeX (pdflatex + tikz/pgfplots/pgf-pie), Python 3 (pandas, openpyxl), the existing pipeline at `D:\Research\03. VLM\analysis`.

## Global Constraints

- **Corpus = 58 peer-reviewed studies** (39 background/transition + 19 core VLM). Single source of truth: `D:\Research\03. VLM\analysis\outputs\data\curated_58_analysis_dataset.csv`.
- **Bui et al. (2026) arXiv** is NOT counted in the 58; cited only as a flagged contextual preprint.
- **No estimated numbers.** Every count/percentage/range traces to `curated_58` or a `paper_text_extracts/*.txt`.
- **DOIs:** use `doi_resolved`; apply all 23 corrections from `curated_58_doi_corrections.csv`.
- **Format:** LaTeX → PDF. Numbered citations, *Automation in Construction* style.
- **Working dir:** `D:\Purdue\Courses\02. Summer 2026\01. EDCI 59100-016 DIS\Week 6\04-Final-Manuscript-Working\` (hereafter `WORK/`).
- **Base draft:** `Week 5\03-Submissions\Assignment10_Draft_Manuscript\Draft_Literature_Review_Plan_Summer26_Kamrul_MdKamruzzaman.tex`.
- **Narrow novelty claim wording (verbatim, reuse everywhere):** "the first PRISMA-ScR scoping review to map vision-language-model architectural-paradigm evolution across construction safety and progress monitoring."

---

## Phase 0 — Data build (foundation; do first)

### Task 0.1: Refresh pipeline outputs & snapshot the authoritative numbers

**Files:**
- Create: `WORK/data_build/build_manuscript_numbers.py`
- Create (output): `WORK/data_build/manuscript_numbers.json`
- Read: `D:\Research\03. VLM\analysis\outputs\data\curated_58_analysis_dataset.csv`

**Interfaces:**
- Produces: `manuscript_numbers.json` with keys `total`, `group_counts`, `core_paradigm_counts`, `year_hist`, `country_counts`, `journal_counts`, `modality_counts`, `app_domain_counts`, `automation_counts`, `metric_family_counts`, `private_vs_public_dataset`, `paradigm_by_year`, `paradigm_by_application`. Consumed by every table/figure task below.

- [ ] **Step 1: Write `build_manuscript_numbers.py`**

```python
import pandas as pd, json, pathlib
SRC = pathlib.Path(r"D:\Research\03. VLM\analysis\outputs\data\curated_58_analysis_dataset.csv")
OUT = pathlib.Path(__file__).parent / "manuscript_numbers.json"
c = pd.read_csv(SRC)
core = c[c.dataset_group == "Core"].copy()

def norm_focus(s):
    s = str(s).lower()
    if "safety" in s and "progress" in s: return "Both"
    if "safety" in s: return "Safety"
    if "progress" in s: return "Progress"
    if "review" in s: return "Review"
    return "Other"

out = {
  "total": int(len(c)),
  "group_counts": c.dataset_group.value_counts().to_dict(),
  "year_hist": {int(k): int(v) for k, v in c.year.value_counts().sort_index().items()},
  "doi_mismatch_count": int((c.doi_mismatch_flag == True).sum()),
  "core_total": int(len(core)),
  "app_domain_counts": c.focus.map(norm_focus).value_counts().to_dict(),
}
# country: split multi-country cells, count primary (first listed) for the geography table
prim = c.countries_analysis.dropna().map(lambda s: str(s).split(";")[0].strip())
out["country_primary_counts"] = prim.value_counts().to_dict()
OUT.write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
```

- [ ] **Step 2: Run it**

Run: `python "WORK/data_build/build_manuscript_numbers.py"`
Expected: prints JSON; `total` = 58; `group_counts` shows Core=19, Background/Transition=39; `doi_mismatch_count` = 23.

- [ ] **Step 3: Manually reconcile paradigm split for the 19 core**

Cross-reference the 19 core refs against the Week 5 master-table paradigm assignments (A/B/C). Record in `manuscript_numbers.json` under `core_paradigm_counts`. Expected A=6, B=6, C=7 (Bui removed from A). **Verify by listing the 19 core titles and their paradigm** — do not assume.

- [ ] **Step 4: Verify against draft**

Compare `year_hist` and `country_primary_counts` to the Week 5 Fig 1 and Table 3. Confirm they differ (they should). Note every changed number in `WORK/data_build/CHANGES.md`.

### Task 0.2: Reconcile the PRISMA screening chain to terminate at 58

**Files:**
- Read: screening workbooks under `D:\Research\03. VLM\` (`Merged List*.xlsx`, `Papers_2nd Phase.xls`, `Scopus and WoS list\*`), and `revise_methodology_prisma_from_existing.py`.
- Create: `WORK/data_build/prisma_chain.md`

- [ ] **Step 1:** Extract the identification/screening counts (raw WoS, raw Scopus, post-filter, duplicates, title/abstract excluded, full-text assessed, full-text excluded) from the workbooks and the PRISMA script.
- [ ] **Step 2:** Derive the Phase-1 (database) vs Phase-2 (snowball) split using `source_database` provenance (`WoS`/`Scopus`/`Curated Workbook`). Document the cleanest defensible chain ending at **58**.
- [ ] **Step 3:** Write `prisma_chain.md` with the final numbers + a note on any value that must be reported "as recorded" because it can't be reconstructed.
- [ ] **Step 4: Author checkpoint** — surface the reconciled chain to the author before it goes into the diagram (the only number the author may need to confirm).

### Task 0.3: Generate LaTeX for the 5 NEW artifacts + rebuilt tables

**Files:**
- Create: `WORK/data_build/tables/*.tex` (one file per table/figure)
- Read: `manuscript_numbers.json`, scientometric output tables under `…\outputs\scientometric\tables\`, descriptive tables under `…\outputs\descriptive\tables\`

- [ ] **Step 1:** Emit `tbl_prior_reviews.tex` (NEW-1) — columns: Review (year) · Tech focus · Application scope · VLMs covered? — populated from the review papers in the corpus (refs 30, 506, 507, and the Gap-Analysis reviews) + the cited reviews (Rabbi 2024, Jiang 2023, Paneru 2021, Zhong 2019, Li 2025).
- [ ] **Step 2:** Emit `fig_paradigm_year.tex` (NEW-2) — pgfplots stacked bar, paradigm×year, from `paradigm_by_year`.
- [ ] **Step 3:** Emit `tbl_paradigm_application.tex` (NEW-3) — cross-tab paradigm×{Safety,Progress,Both} from `paradigm_by_application`.
- [ ] **Step 4:** Emit `tbl_perf_synthesis.tex` (NEW-4) — per-paradigm metric ranges (mAP/BLEU/etc.) pulled from `validation_metric` + extracts; explicit "not comparable" cells.
- [ ] **Step 5:** Emit `tbl_scientometric.tex` / `fig_thematic_map.tex` (NEW-5) — top keyword co-occurrence clusters + citation bursts from scientometric tables.
- [ ] **Step 6:** Emit rebuilt `fig_pubyear.tex` (fixed continuous x-axis), `tbl_bibliometric.tex` (merged geography+journal), `tbl_appdomain.tex`, `tbl_paradigm_dist.tex`, `tbl_metrics.tex`, `tbl_master.tex` (58→Phase-1 charting; corrected labels).
- [ ] **Step 7: Verify** every emitted `.tex` snippet compiles in a minimal standalone wrapper without error.

---

## Phase 1 — Working manuscript scaffold

### Task 1.1: Create the working `.tex` from the Week 5 base

**Files:**
- Create: `WORK/Final_Literature_Review_Manuscript_Summer26_Kamrul_MdKamruzzaman.tex` (copy of base)

- [ ] **Step 1:** Copy the Week 5 `.tex` to `WORK/` under the final filename.
- [ ] **Step 2: Compile baseline** — Run: `pdflatex -interaction=nonstopmode <file>.tex` twice (for refs). Expected: PDF builds, no undefined references. This is the regression baseline.
- [ ] **Step 3:** If the toolchain is missing, STOP and tell the author which LaTeX distribution to install before continuing.

---

## Phase 2 — Front matter (Abstract, keywords, author line)

### Task 2.1: Add structured Abstract + keywords + corresponding-author line

**Files:** Modify `WORK/<final>.tex` (title block).

- [ ] **Step 1:** Insert a ≤250-word structured abstract after the title block: *Background → Objective → Methods (PRISMA-ScR, 58 peer-reviewed studies, WoS+Scopus + backward snowball) → Results (3 paradigms A/B/C; key distributions) → Key gaps (evaluation fragmentation, ~85% private datasets, temporal-reasoning gap) → Contribution (narrow novelty wording verbatim).*
- [ ] **Step 2:** Add 5–6 keywords; add corresponding-author/affiliation line (resolves P7).
- [ ] **Step 3: Verify** word count ≤250 (`detex`/manual). Compile.

---

## Phase 3 — Introduction

### Task 3.1: Rebalance, add prior-reviews table, narrow novelty, fix attributions

**Files:** Modify `WORK/<final>.tex` Section 1; input `tables/tbl_prior_reviews.tex`.

- [ ] **Step 1:** Add equal safety+progress framing (≥1 progress-focused paragraph in the motivation) (M10).
- [ ] **Step 2:** Insert the Prior-Reviews Gap Table (NEW-1) and a sentence using the **verbatim narrow novelty claim** (C1, m7).
- [ ] **Step 3:** Reword the "semantic gap" sentence to credit Wu et al. (2021) as the construction *application*, not origin (m3).
- [ ] **Step 4:** Add one sentence fixing VLM/MLLM/LMM hierarchy (m2). Reduce Alaloul 2022 to ≤2 cites in the section (m1).
- [ ] **Step 5: Verify** compile; all new `\cite{}` resolve; prior-reviews table renders.

---

## Phase 4 — Methodology + PRISMA

### Task 4.1: Mixed-method statement, database justification, charting reliability

**Files:** Modify Section 2.

- [ ] **Step 1:** Add explicit mixed-method paragraph (PRISMA-ScR selection/mapping + thematic synthesis framework) (M3).
- [ ] **Step 2:** Strengthen WoS+Scopus justification + add Wave-2 hook sentence for IEEE Xplore (M9).
- [ ] **Step 3:** Strengthen single-reviewer charting-reliability statement (M4). Update corpus count to 58 + add preprint-accommodation note to Table 1 (C5).
- [ ] **Step 4: Verify** compile.

### Task 4.2: Restructure the PRISMA diagram (parallel tracks + exclusion reasons)

**Files:** Replace the `fig:prisma` TikZ block; use numbers from `prisma_chain.md`.

- [ ] **Step 1:** Redraw as two parallel identification tracks (database + backward snowball) merging before the inclusion box; add full-text exclusion-reason categories (C4).
- [ ] **Step 2:** Set all counts from `prisma_chain.md`; final box = 58.
- [ ] **Step 3: Verify** compile; the diagram's terminal count equals 58 and matches `group_counts`.

---

## Phase 5 — Descriptive Analysis (trim + rebuild + scientometric)

### Task 5.1: Rebuild distributions, trim, add synthesis takeaways

**Files:** Modify Section 3; input rebuilt table snippets.

- [ ] **Step 1:** Replace Fig 1 with rebuilt `fig_pubyear.tex` (continuous x-axis, real counts) (M8).
- [ ] **Step 2:** Replace geography + journal tables with merged `tbl_bibliometric.tex` (Katie trim).
- [ ] **Step 3:** Replace app-domain, paradigm-distribution, metrics tables with rebuilt snippets; update all prose counts to `manuscript_numbers.json`.
- [ ] **Step 4:** Append a **bold one-sentence synthesis takeaway** to each retained subsection (Lowell). Add the private-vs-public dataset finding (~85% private) explicitly.
- [ ] **Step 5: Verify** every count in Section 3 prose matches `manuscript_numbers.json` (grep each number).

### Task 5.2: Add scientometric subsection (NEW-5)

**Files:** New subsection in Section 3; input `tbl_scientometric.tex`/`fig_thematic_map.tex`.

- [ ] **Step 1:** Write a focused subsection: keyword co-occurrence/thematic clusters + citation bursts, each with an interpretive takeaway (not raw dumps).
- [ ] **Step 2: Verify** compile; figures render.

---

## Phase 6 — Thematic Analysis (architectures)

### Task 6.1: Reframe framework as organizing tool; typological recast

**Files:** Modify Section 4.1–4.4.

- [ ] **Step 1:** Recast framework prose + Fig 3 caption as a synthesis/organizing tool, not novel theory (C2).
- [ ] **Step 2:** Insert Paradigm×Year figure (NEW-2) and rewrite A→B→C as **typological coexistence**; replace "the community shifted" phrasing (C6, m5).
- [ ] **Step 3: Verify** compile; figure renders; no chronological-claim language remains (grep "shifted toward", "transitioned").

### Task 6.2: Quantitative cross-study synthesis

**Files:** New subsection 4.x; input `tbl_perf_synthesis.tex`.

- [ ] **Step 1:** Add per-paradigm performance synthesis (mAP/BLEU ranges where comparable; "not comparable" stated as a finding) (M1).
- [ ] **Step 2:** Convert each paradigm subsection's closing sentence from description → interpretation.
- [ ] **Step 3: Verify** every performance figure cited traces to an extract; compile.

---

## Phase 7 — Applications (Layer 3)

### Task 7.1: Rebalance progress vs safety

**Files:** Modify Section 5 (applications).

- [ ] **Step 1:** Expand progress-tracking treatment toward parity (M10); add interpretive takeaway to each application subsection.
- [ ] **Step 2: Verify** compile.

---

## Phase 8 — Discussion

### Task 8.1: Cross-paradigm × application synthesis + named contributions

**Files:** Modify Section 6.1; input `tbl_paradigm_application.tex` (NEW-3).

- [ ] **Step 1:** Add the cross-synthesis (which paradigm serves safety vs progress; absent combinations as gaps) (M5).
- [ ] **Step 2:** Name **evaluation fragmentation** and **private-dataset reliance** as explicit contributions (Lowell). Ensure RQ answers reference rebuilt numbers.
- [ ] **Step 3: Verify** compile; cross-tab table matches `paradigm_by_application`.

---

## Phase 9 — Limitations

### Task 9.1: Expand to substantive paragraphs

**Files:** Modify Section 6.2.

- [ ] **Step 1:** Convert each limitation into a paragraph (limitation + implication + future remedy); keep quality-appraisal limitation; fix geography math to rebuilt numbers (m4, M6).
- [ ] **Step 2: Verify** compile; geography percentages match `country_primary_counts`.

---

## Phase 10 — Next Steps (NEW, required)

### Task 10.1: Add dedicated Next Steps section

**Files:** New Section before Conclusion.

- [ ] **Step 1:** Write Next Steps: incomplete items; what to do next; extension path. Concrete: construction-specific VLM benchmark; temporal-reasoning focus; IEEE Xplore expansion (Wave 2); dual-reviewer charting + quality appraisal; preprint→peer-review tracking.
- [ ] **Step 2: Verify** compile; section present in ToC.

---

## Phase 11 — Conclusion

### Task 11.1: Precise contributions

**Files:** Modify Section 7.

- [ ] **Step 1:** Restate three contributions precisely; remove undefended "first/no prior review" phrasing; use narrow novelty wording (m7).
- [ ] **Step 2: Verify** compile.

---

## Phase 12 — References

### Task 12.1: Rebuild reference list + apply DOI corrections

**Files:** Modify `thebibliography`; cross-check `curated_58_doi_corrections.csv`.

- [ ] **Step 1:** Apply all 23 DOI corrections; correct any volume/year flags (m8). Add Bui (2026) as a clearly-marked preprint entry (contextual).
- [ ] **Step 2:** Ensure every `\bibitem` is cited and every `\cite` resolves (no orphan/undefined).
- [ ] **Step 3:** Update the working reference document (`WorkingDocument_FullReferenceList…`) to match.
- [ ] **Step 4: Verify** compile twice; zero `LaTeX Warning: Citation undefined` and zero `Reference ... undefined`.

---

## Phase 13 — Writing-quality (OWL) pass

### Task 13.1: OWL polish on heaviest sections

- [ ] **Step 1:** Run `owl-paramedic` / `owl-conciseness` on Introduction and Discussion.
- [ ] **Step 2:** Run `owl-transitions` on all section seams (Lowell coherence).
- [ ] **Step 3:** Run `owl-active-voice` and `owl-logic` on the novelty + typology arguments.
- [ ] **Step 4:** Reduce over-used intensifiers — "profound", "critical" (>10×), "paradigm-shifting" (P2–P4).
- [ ] **Step 5: Verify** compile; re-read for meaning preservation.

---

## Phase 14 — Final verification & author checkpoint

### Task 14.1: Whole-manuscript verification

- [ ] **Step 1: Number audit** — grep every numeric claim; confirm each matches `manuscript_numbers.json` / `prisma_chain.md`.
- [ ] **Step 2: Citation audit** — confirm zero undefined citations/refs; every charted claim traces to corpus.
- [ ] **Step 3: Rubric audit** — check all 8 rubric rows (core requirements, intro, synthesis, organization, methodology alignment, interpretation, limitations+Next Steps, evidence, writing) are satisfied; confirm 20+ sources (we have ~40+), 10+ pages, title page, Next Steps present.
- [ ] **Step 4: Reviewer-issue audit** — tick each Wave-1 item in the traceability matrix (C1,C2,C3,C4,C5,C6,M1,M3,M5,M6,M8,M10,m1–m8,P1–P7).
- [ ] **Step 5: Final compile** → `WORK/<final>.pdf`.
- [ ] **Step 6: Author checkpoint** — present the PDF + a change-summary (what changed vs Week 5, mapped to Lowell + reviewer items) before declaring final.

---

## Self-Review (spec coverage)

- Abstract/keywords → T2.1 ✓ · Prior-reviews table/novelty → T3.1 ✓ · PRISMA restructure → T4.2 ✓ · Trim+takeaways → T5.1 ✓ · Scientometric → T5.2 ✓ · Framework reframe/typology → T6.1 ✓ · Quant synthesis → T6.2 ✓ · Progress rebalance → T3.1/T7.1 ✓ · Cross-synthesis → T8.1 ✓ · Limitations → T9.1 ✓ · Next Steps → T10.1 ✓ · Conclusion → T11.1 ✓ · DOI/refs → T12.1 ✓ · OWL → T13.1 ✓ · 58-reconcile+rebuilds → Phase 0 ✓.
- Wave-2 (M9 IEEE Xplore, optional CS-survey anchor) intentionally deferred; hook left in T4.1.
- No placeholders; all numbers sourced from Phase 0 artifacts.
