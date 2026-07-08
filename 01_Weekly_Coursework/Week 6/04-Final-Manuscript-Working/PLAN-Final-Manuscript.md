# Plan — Final Literature Review Manuscript (EDCI 59100-016, Assignment 11)

**Author:** Md Kamruzzaman Kamrul · **Date:** 2026-06-27 · **Course final due:** 2026-06-28 11:59 PM
**Target title:** *Vision-Language Models for Construction Site Safety and Progress Monitoring: A Scoping Review*
**Eventual venue:** *Automation in Construction* (Elsevier) — numbered citation style.

---

## 0. Strategy

This is a **targeted hardening pass** on an already-strong draft (Week 5: 49/50), not a rewrite. Two decoupled waves:

- **Wave 1 (submittable June 28):** everything achievable from the existing 58-paper corpus + the `D:\Research\03. VLM\analysis` pipeline. Standalone and complete.
- **Wave 2 (AutoCon polish, later):** only items needing the new **IEEE Xplore** (± ACM DL, ASCE) database search that the author will run.

**Output format:** LaTeX (`.tex`) → PDF, per established workflow. Build on the Week 5 `.tex`.

**Source of truth for ALL numbers:** `D:\Research\03. VLM\analysis\outputs\data\curated_58_analysis_dataset.csv` (+ the pre-computed descriptive/scientometric output tables). No estimated figures.

---

## 1. Corpus reconciliation (APPROVED)

| Decision | Resolution |
|---|---|
| Final corpus | **58 peer-reviewed studies** = 39 background/transition + 19 core VLM. Single source of truth. |
| Bui et al. (2026) arXiv | **Removed from counted corpus**; retained as explicitly-flagged *contextual preprint* in Discussion only. Resolves reviewer C5/m1. |
| Core paradigm split | Recompute for 19 core (Bui was 7th Paradigm A ⇒ expected A=6, B=6, C=7 — verify). |
| Year / geography / journal / modality | **Rebuild from `curated_58`** (draft's Fig 1 & Table 3 were estimated and are wrong). |
| DOIs | Apply **23 corrections** from `curated_58_doi_corrections.csv`. |
| PRISMA flow | Reconcile terminal numbers so the chain ends at **58**; derive Phase-1/Phase-2 split from screening workbooks + `source_database` provenance. |
| Exclusion reasons | Present the three reason **categories** qualitatively (no per-reason counts exist). |

---

## 2. Target manuscript structure & section-level changes

### NEW front matter
- **Abstract** (≤250 words, structured): corpus size (58), PRISMA-ScR method, 3 architectural paradigms, headline gaps (evaluation fragmentation, private datasets, temporal-reasoning gap), contribution. → resolves P5/P6.
- **Keywords** (5–6).
- **Corresponding-author / affiliation line.** → resolves P7.

### 1. Introduction
- Rebalance safety-heavy framing toward **equal safety + progress** billing (M10).
- Add **Prior-Reviews Gap Table** (Table NEW-1) and **narrow the novelty claim** to: *"the first PRISMA-ScR scoping review to map VLM architectural-paradigm evolution across construction safety **and** progress monitoring."* (C1, m7).
- Fix **"semantic gap"** attribution → credit Wu et al. (2021) as the *construction application*, not the origin (m3).
- Resolve **VLM / MLLM / LMM** terminology in one explicit sentence (m2).
- Trim over-reliance on Alaloul 2022 (cited 4×) (m1).

### 2. Methodology
- Add explicit **mixed-method statement**: PRISMA-ScR for selection/descriptive mapping + thematic synthesis framework for analysis (M3).
- Strengthen **two-database justification** + insert a Wave-2 hook paragraph for IEEE Xplore (M9).
- Strengthen **data-charting reliability** statement (single reviewer, acknowledged) (M4).
- **Restructure PRISMA diagram** (Fig 2): two parallel identification tracks (database + backward snowball) merging before inclusion; full-text **exclusion reasons** shown (C4).

### 3. Descriptive Analysis — TRIM + synthesis takeaways (Katie + Lowell)
- **Consolidate** Geography + Journal into one compact "bibliometric snapshot" (one table, short prose).
- **Keep:** corpus composition; publication-trend chart (Fig 1, **x-axis fixed**, M8); paradigm distribution; metrics landscape.
- **Add** NEW scientometric subsection (Table/Fig NEW-5): keyword co-occurrence / thematic map + citation bursts (from pipeline).
- **End every retained subsection with a bold one-sentence synthesis takeaway** ("Taken together, …") (Lowell).
- All counts recomputed from `curated_58`.

### 4. Thematic Analysis (architectures)
- **Reframe the Three-Layered Framework as an organizing/synthesis tool**, not a novel theory (C2). Keep framework figure (Fig 3).
- **Recast A→B→C as typological, not chronological**, backed by **Paradigm×Year chart** (Fig NEW-2) showing coexistence (C6). Replace anthropomorphic "the community shifted" phrasing (m5).
- **Add quantitative cross-study synthesis** per paradigm (Table NEW-4): mAP / BLEU ranges where comparable; explicit "not comparable" where heterogeneous (M1 — also Lowell's #1 ask).
- Convert each paradigm subsection's closing from description → interpretation.

### 5. Applications (Layer 3)
- Expand **progress-tracking** treatment toward parity with safety (M10).
- Keep safety/progress application flow; ensure each ends with interpretive takeaway.

### 6. Discussion
- **Add Cross-Paradigm × Application synthesis** (Table/Fig NEW-3): which paradigm serves safety vs progress; which combinations are absent (M5).
- Foreground **evaluation fragmentation** and **near-universal private datasets** as explicitly-named contributions (Lowell).
- Keep the four-RQ structure; ensure RQ answers reference the rebuilt numbers.

### 6.x Limitations — expand (M6)
- Convert 7 one-liners into substantive paragraphs: each = limitation + implication for interpretation + how future work addresses it.
- Keep the **quality-appraisal** limitation explicit.
- Fix the **geography math** to match rebuilt numbers (m4).

### 7. Next Steps (NEW — required Week 6 element)
- Dedicated section: what remains incomplete; what to do next; how to extend/strengthen.
- Concrete items: construction-specific VLM benchmark dataset; temporal-reasoning focus; IEEE Xplore expansion (Wave 2); dual-reviewer charting + quality appraisal; preprint→peer-review tracking.

### 8. Conclusion
- Restate **three contributions with precision**; drop undefended "first/no prior review" phrasing (m7).

### References
- Rebuild from `curated_58` + apply 23 DOI corrections; verify volume/year flags (m8). Sync with working reference document.

---

## 3. Figures & tables register

| ID | Status | Source | Resolves |
|---|---|---|---|
| Fig 1 Publication trend | **Rebuild** (fix x-axis, real counts) | `yearly_publication_citation_trends.csv` / `curated_58` | M8 |
| Fig 2 PRISMA flow | **Restructure** (parallel tracks + exclusion reasons) | screening workbooks + PRISMA script | C4 |
| Fig 3 Three-Layer Framework | Keep; recaption as organizing tool | existing | C2/C7 |
| Table 1 Inclusion/Exclusion | Keep; add preprint accommodation note | existing | C5 |
| Table 2 Charting framework | Keep | existing | — |
| Bibliometric snapshot (was Tables 3+4) | **Consolidate** | `top_countries_metrics.csv`, `top_journals_metrics.csv` | Katie trim |
| Table 5 App domain/automation | **Rebuild** | `curated_58` | — |
| Table 6 Paradigm distribution | **Rebuild** (19 core, A/B/C) | `curated_58` | C6 |
| Table 7 Metrics landscape | **Rebuild** | `curated_58` validation_metric | — |
| Master charting table | **Rebuild** from `curated_58`; fix labels (Wang Y. vs Wang X.; VQA-as-task; hardware→validation-setting) | `curated_58` | m6 |
| **NEW-1 Prior-reviews gap table** | Build | review papers in corpus | C1 |
| **NEW-2 Paradigm×Year** | Build | `curated_58` | C6 |
| **NEW-3 Paradigm×Application cross-tab** | Build | `curated_58` | M5 |
| **NEW-4 Quantitative performance synthesis** | Build | `curated_58` + extracts | M1 |
| **NEW-5 Scientometric (keyword/thematic + bursts)** | Build | scientometric output tables | rigor/Lowell |

---

## 4. Data-integrity & verification protocol

- Every paper-level claim (model, dataset, metric, limitation) verified against `curated_58` fields and/or `paper_text_extracts/*.txt`. No invented numbers.
- Quantitative ranges (BLEU/mAP) pulled only where reported; gaps reported as gaps.
- DOIs taken from `doi_resolved`; the 23 flagged corrections applied.
- After drafting, run a claim-by-claim citation check pass on Intro + Discussion.

## 5. Writing-quality (OWL) pass
Run OWL skills on heaviest sections after content edits: `owl-paramedic`/`owl-conciseness` (Intro, Discussion), `owl-transitions` (section seams — Lowell coherence), `owl-active-voice`, `owl-logic` (novelty + typology arguments). Address P2–P4 word-overuse ("profound", "critical", "paradigm-shifting").

---

## 6. Execution sequence (Wave 1)

1. **Data build** — scripts over `curated_58` to emit all rebuilt table/figure values + the 5 NEW artifacts; reconcile PRISMA terminal numbers. Verify paradigm split.
2. **Methodology + PRISMA restructure**; descriptive-section trim + synthesis takeaways.
3. **Thematic synthesis hardening** (M1 quantitative synthesis, C2 reframe, C6 typology) — largest block.
4. **Discussion cross-synthesis (M5) + Limitations (M6) + Next Steps + Abstract/keywords.**
5. **References rebuild + DOI fixes + figure/label cleanup.**
6. **OWL polish pass.**
7. **Compile `.tex` → PDF; checkpoint with author before "final."**

## 7. Reviewer-issue traceability (Wave 1 unless noted)

Resolved-in-Wave-1: C1, C2, C3(+), C4, C5, C6, C7✓, M1, M2✓, M3, M4✓+, M5, M6, M7✓, M8, M10, m1–m8, P1–P7, **Next Steps**, abstract.
Wave-2: **M9** (IEEE Xplore search → revised PRISMA/distributions), optional external CS-survey citation anchor for the VLM definition (C3 enhancement).

## 8. Wave-2 data request (author to run)
IEEE Xplore (± ACM DL, ASCE Library) with the **same Boolean strings**; return: raw record count, post-filter count, and any unique new papers (title/DOI/year). I integrate into PRISMA numbers, distributions, and the database-justification paragraph.

## 9. Open confirmations
- PRISMA screening-chain reconstruction: I'll derive the most defensible Phase-1/Phase-2 split from the screening workbooks; will flag if any raw number can't be reconstructed and must be stated as reported.
