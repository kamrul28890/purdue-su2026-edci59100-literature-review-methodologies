# Reviewer Report — *Automation in Construction* (Draft)
**Manuscript:** Vision-Language Models for Construction Site Safety and Progress Monitoring: A Scoping Review  
**Author:** Md Kamruzzaman Kamrul  
**Reviewer Stance:** Senior academic (30 years, construction management); AiC editorial board member  
**Verdict if submitted today:** Major Revision — not acceptable in current form

---

## Preamble

This manuscript addresses a timely and genuinely important problem: the emergence of Vision-Language Models in construction site AI represents a real paradigm shift that the field needs mapped. The methodological choice of a scoping review is appropriate, and the author has assembled a respectable corpus. However, the paper has structural, methodological, argumentative, and scholarly precision issues at every level that would prevent publication in *Automation in Construction* in its current form. The comments below are organized by severity and location.

---

## CRITICAL ISSUES (Must resolve before any acceptance decision)

### C1. The core novelty claim is undefended and partially false

**Location:** Abstract (implied), Section 1 Introduction, and Section 7 Conclusion paragraph 2.

The paper claims to provide "the first systematic scoping map of VLM architectures applied to active construction management." This is a strong falsifiability claim. To make it, the author must conduct — and present — a brief but explicit secondary search of prior reviews to demonstrate none covers this ground. The current introduction cites Rabbi & Jeelani (2024), Jiang & Messner (2023), Paneru & Jeelani (2021), and Zhong et al. (2019) as existing reviews but never systematically analyzes what each one covers and what it omits. A table mapping prior reviews by (a) year, (b) technology focus, (c) application scope, and (d) whether VLMs were addressed would make this claim defensible. Without it, a peer reviewer can simply assert "Li et al. (2025) — already in your own references — covers construction scene understanding including VLMs," and the claim collapses.

**Required fix:** Add a prior reviews table in Section 1. Either defend the "first" claim rigorously or restate it as "the first scoping review using PRISMA-ScR to specifically map VLM paradigm evolution in construction safety and progress monitoring," which is more precisely defensible.

---

### C2. Framework novelty is overstated and its theoretical grounding is circular

**Location:** Section 4.1 (Three-Layered Spatiotemporal VLM Framework).

The Three-Layered Framework — Layer 1 (Inputs), Layer 2 (Cognitive Engine / Paradigms), Layer 3 (Outputs) — is structurally identical to a standard input-process-output (IPO) model or a basic control systems architecture. The paper attempts to ground this in Czarnowski et al. (2020) and Parasuraman et al. (2000), but:

1. Parasuraman et al. (2000) is a human factors paper about levels of automation in human-machine systems. It does not propose a VLM classification framework.
2. Czarnowski et al. (2020) is a computer science conference paper (ICCS 2020 Lecture Notes). Critically, **conference proceedings are listed in the paper's own exclusion criteria** (Table 1). Citing a source you would have excluded from your own review to justify your analytical framework is a logical inconsistency.
3. The "sensory → cognitive → actuator" tripartite structure is engineering systems 101; it cannot be the primary theoretical novelty.

**Required fix:** Either (a) demonstrate the framework's novelty more specifically — what classifications does it enable that existing frameworks (e.g., the CV review taxonomies in Zhong 2019, Paneru 2021) do not? — or (b) reposition the framework as a synthesis and organizational tool rather than an original theoretical contribution. Reframe the contribution accordingly throughout. Also remove or replace the Czarnowski (2020) conference proceedings citation with a peer-reviewed source.

---

### C3. The paper never formally defines "Vision-Language Model"

**Location:** Throughout, but critically Section 1 paragraph 5 and Section 4.

The paper's entire analytical framework depends on the term "VLM," yet it is never formally defined. This matters enormously because the corpus includes:

- **CNN-LSTM captioning** (Liu et al. 2020, Bang & Kim 2020): traditional encoder-decoder models with no shared embedding space and no language model in the modern sense
- **CLIP**: a contrastive alignment model, not a generative VLM
- **ChatGPT + YOLO pipeline** (Xiao et al. 2024): two separate models pipelined together, not an integrated VLM
- **Claude 3.7 Sonnet** (Tuomisto et al. 2026): a proprietary frontier multimodal model

Are all of these "VLMs"? Under what definition? The Paradigm B section includes image captioning systems from 2020-2022 that predate modern VLMs. A rigorous definition early in the paper — distinguishing contrastive alignment models, generative VLMs, and hybrid agentic stacks — would significantly strengthen the analytical claim and clarify whether the paradigm taxonomy is tracking technical architecture evolution or simply the application of any text-producing visual AI.

**Required fix:** Add a definitional subsection or paragraph in Section 1 (or at the start of Section 4) that establishes the VLM taxonomy boundary. Engage with at least one published VLM survey from computer science to anchor the definition (e.g., Li et al. 2024 "BLIP" family survey, or a review in IEEE TPAMI).

---

### C4. PRISMA diagram is structurally non-compliant with PRISMA-ScR standards

**Location:** Figure 2 (PRISMA flow diagram).

The official PRISMA-ScR flow diagram (Tricco et al. 2018) requires:

1. A box at the **Identification** stage for "Additional records identified through other sources" (the backward snowballing). In the current diagram, backward snowballing appears as a linear step *after* inclusion — this misrepresents the methodology. Snowballing is a separate identification source, not a downstream filter.
2. The exclusion box at full-text review should list **specific reasons** for exclusion with counts (e.g., "outside construction domain: n=14; insufficient multimodal detail: n=12; unimodal only: n=7").
3. The current diagram shows 58 articles going to full-text review after 90-32=58, with 33 excluded, yielding 25. But the text says the 31 snowballed papers were identified "concurrently" with Phase 1 — the PRISMA diagram should show two parallel tracks (database + snowball) merging before the final inclusion box.

A TikZ-generated diagram is technically acceptable to AiC; the visual format is not the issue. The logical structure of the PRISMA flow is the issue.

**Required fix:** Restructure the PRISMA diagram to show: (1) Phase 1 (database) and Phase 2 (snowball) as parallel identification tracks, (2) exclusion reasons at full-text stage, per PRISMA-ScR specification.

---

### C5. Key inclusion criterion is violated by two cited papers

**Location:** Table 1 (Inclusion/Exclusion Criteria) vs. reference list.

The paper's stated inclusion criteria specify "High-impact peer-reviewed journal" as the only accepted source type, with "Conference proceedings and industry white papers" explicitly excluded. Yet:

1. **Czarnowski et al. (2020)**: Published in *Computational Science – ICCS 2020*, Lecture Notes in Computer Science — a conference proceedings volume. This citation appears in the theoretical framework (Section 4.1) and is cited as a peer-reviewed source.
2. **Bui et al. (2026)**: Published as an arXiv preprint — not peer-reviewed at the time of this review. The paper is cited 4 times (Sections 1, 4.2, 5.1, Discussion RQ2) for substantive claims. The original reference incorrectly listed it as *IEEE Access* and was corrected to arXiv — but this means the inclusion is an arXiv preprint, which fails the eligibility criterion.

If Bui (2026) is retained, the eligibility criteria must be explicitly revised to allow preprints, and the limitations section must discuss what this means for evidentiary quality. If it is excluded per the stated criteria, multiple claims in the text that lean on Bui (2026) need alternative citations.

**Required fix:** Either (a) revise the eligibility criteria to explicitly accommodate preprints and conference proceedings and add them to the corpus count with appropriate qualification, or (b) remove these citations from the analytical corpus (though they may remain as contextual references with a footnote explaining their status).

---

### C6. The temporal "paradigm evolution" argument is factually undermined by publication dates

**Location:** Sections 4.1, 4.2, 4.3 — the narrative of A → B → C as chronological progression.

The paper argues that Paradigm A (zero-shot) evolved into Paradigm B (fine-tuned), which evolved into Paradigm C (hybrid agentic). However, the publication dates in the master table contradict this:

- **Paradigm A**: Papers include Bui 2026, Wang & El-Gohary 2024, Sun 2024 — these are *more recent* than many Paradigm C papers
- **Paradigm B**: Includes Bang & Kim 2020 and Liu 2020 — these *predate* Paradigm A papers like Zhang 2025 and Liang 2024
- **Paradigm C**: Xiao 2024, Jeoung 2025 — contemporaneous with Paradigm A papers

This is not a chronological progression. It is a typological classification of architectures that happen to have a loose historical tendency, but the three paradigms coexist in the 2023–2026 literature simultaneously. If the framework claims chronological "paradigm shifts" (as the language in each section implies), this claim is falsified by the data.

**Required fix:** Either (a) reframe the paradigm taxonomy as a typological (architectural) rather than chronological classification, explicitly acknowledging all three paradigms are active simultaneously in the current literature, or (b) construct a timeline analysis (e.g., Figure showing paper counts by paradigm per year) demonstrating the claimed temporal dominance shift. The narrative in Sections 4.1–4.3 using phrases like "the construction research community transitioned toward" must be qualified.

---

### C7. No figure presenting the Three-Layered Framework

**Location:** Section 4.1.

The Three-Layered Spatiotemporal VLM Framework is the paper's central intellectual contribution, yet there is no figure illustrating it. For a paper in *Automation in Construction* — a journal that regularly publishes system architecture diagrams — the absence of a visual representation of the framework is a major omission. A reviewer reading this paper has no visual anchor for understanding how the three layers map to the 25 papers, how the three paradigms sit within Layer 2, or what the relationships between layers are. Section 4.1 describes the framework in prose for two paragraphs without a single visual.

**Required fix:** Create a framework figure (similar in intent to Figure 2 in Chan et al. 2025 or Figure 1 in Li et al. 2025) showing the three-layer architecture, the three paradigms within Layer 2, the input types in Layer 1, and the output domains in Layer 3. This figure should be present before Section 4.1.

---

## MAJOR ISSUES (Require substantive revision)

### M1. Chapters 4 and 5 lack quantitative cross-study synthesis

**Location:** Sections 4 and 5 throughout.

*Automation in Construction* expects more from a findings synthesis than narrative description of individual papers. Currently, Sections 4 and 5 are largely organized as: "Paper X did Y. Paper Z also did Y. However, paper W showed limitation L." This is annotation, not synthesis. An AiC reviewer will ask: across the papers in each paradigm, what performance levels have been achieved? What are the best and worst results? What architectural choices are associated with higher performance?

Specific gaps:
- Paradigm A (7 papers): What mAP ranges are achieved by zero-shot approaches on construction datasets? How does CLIP-based zero-shot compare to DINOv2-based approaches in the studies included?
- Paradigm B (6 papers): BLEU scores reported by Liu 2020, Zhai 2023, Jung 2024 — can these be compared? Even a note that "BLEU-4 scores ranged from X to Y across captioning studies" would add analytical value.
- Paradigm C (7 papers): What types of failures are most common? The paper notes hallucination in Xiao 2024 and prompt sensitivity in Jeoung 2025 — are there patterns?

**Required fix:** Add a synthesis subsection at the end of each paradigm section (or as Section 4.4 "Cross-Paradigm Synthesis") that (a) tabulates key performance figures across studies where comparable, (b) identifies architectural choices associated with better outcomes, and (c) explicitly states where performance data is not comparable due to heterogeneous metrics (which is itself a finding).

---

### M2. Research questions are internally inconsistent with the paper's scope

**Location:** Section 1, Research Questions; Section 6, Discussion.

**RQ2** asks: "How is multimodal data (visual and textual) fused and processed to **evaluate safety hazards on active sites**?" This is safety-only, yet the paper covers both safety and progress monitoring. The Discussion answer to RQ2 (Section 6.1) discusses all 20 core VLM papers, including progress tracking papers — which are outside the RQ2 question as stated.

**RQ4** specifies "spatiotemporal tasks in construction," but several included papers address non-spatiotemporal tasks (PPE detection from single frames, static image classification) that are not spatiotemporal in any meaningful sense.

**Required fix:** Revise RQ2 to cover multimodal fusion for *both* safety and progress monitoring (e.g., "How is multimodal data fused and processed across construction safety and progress applications?"). Revise RQ4 or clarify the scope of "spatiotemporal" — if the paper intends it broadly, define it early. If it means specifically temporal-sequential analysis, exclude single-frame studies from RQ4's scope.

---

### M3. The paper conflates two distinct things under "scoping review"

**Location:** Sections 2–3 (methodology) vs. Sections 4–5 (thematic analysis).

PRISMA-ScR scoping reviews traditionally stop at descriptive characterization. When the author introduces an original theoretical framework (the Three-Layered VLM taxonomy) and uses it as an analytical lens for the findings, this crosses into a *systematic review with narrative synthesis* or a *structured literature review*. A pure scoping review would map existing classifications; it would not impose a new taxonomy and use it to reorganize 25 papers.

This is not necessarily a disqualifying problem — many AiC papers combine scoping methods with novel synthesis frameworks. But the paper cannot simultaneously claim (a) "this is a scoping review that maps without evaluating" and (b) "this is a novel framework that classifies VLM paradigms." These claims have different standards of evidence and different peer review expectations.

**Required fix:** Clarify in Section 2 (Data Synthesis subsection) that the study employs a *mixed-method approach*: PRISMA-ScR for the selection and descriptive mapping, and a novel thematic synthesis framework for the analytical chapters. Review papers in AiC that use similar mixed designs (e.g., Sherafat et al. 2020 uses a framework to organize a review) and align the methodological language.

---

### M4. Data charting reliability is unaddressed

**Location:** Section 2.4 (Data Charting and Extraction Process).

The paper describes a standardized data charting form but does not state:
- Whether screening and charting was performed by a single researcher or multiple reviewers
- Whether any inter-rater reliability (e.g., Cohen's kappa) was calculated
- Whether the protocol was pre-registered (OSF, PROSPERO, or equivalent)
- How disagreements were resolved

For a scoping review in a top construction engineering journal in 2026, this is expected baseline transparency. Even a student thesis would be expected to report these. A single-reviewer study without reliability testing is methodologically exposed to bias claims.

**Required fix:** Add to Section 2.4 a statement about who conducted screening and charting, whether any verification was performed, and acknowledge single-reviewer limitation explicitly in Section 6.2 (Limitations). If dual-review was conducted but not reported, add it. If truly single-reviewer, this should be prominently flagged as a limitation with an acknowledgment of how bias may have affected paradigm classification.

---

### M5. The Discussion fails to integrate Chapters 4 and 5

**Location:** Section 6.1 (Discussion).

The paper has two thematic analysis chapters — Chapter 4 (architectures) and Chapter 5 (applications). Both cover the same 25 papers from different angles. The Discussion section (Section 6.1) answers the four RQs but does not synthesize the cross-chapter findings. Specifically:

- **What is the relationship between architectural paradigm and application domain?** For example: Is Paradigm A predominantly used for safety or progress? Is Paradigm C always combined with both? This is the most interesting cross-cutting finding and the Discussion never addresses it.
- **Which paradigm-application combinations are absent?** Are there zero Paradigm B papers on robotic inspection? Why? That's a research gap.
- **How do the limitations in Chapter 4 manifest in the application outcomes of Chapter 5?** The prompt sensitivity of Paradigm C (Chapter 4) — how does it specifically impact safety compliance checking (Chapter 5)?

**Required fix:** Add a cross-cutting synthesis paragraph (or subsection 6.1.5: "Cross-Chapter Synthesis") that bridges the architecture and application analyses and identifies the most important paradigm-application interactions and gaps.

---

### M6. The Limitations section is insufficient for AiC

**Location:** Section 6.2.

Five single-sentence limitations with no substantive elaboration do not meet AiC standards for a scoping review paper. Each stated limitation should be explained with (a) what the specific implication is for the findings, and (b) how future work should address it. For example, "the English-language restriction may have excluded relevant work published in Chinese, Korean, or other languages" — since 35.7% of the corpus is from East Asian institutions, this limitation is particularly significant. How much Chinese-language construction AI research might have been missed? What does this mean for the completeness of the safety application mapping?

Additionally, a critical limitation is entirely absent: **the lack of quality appraisal**. Scoping reviews explicitly do not assess quality, but AiC reviewers will note that the master table assigns equal weight to a 16-paper probing study (Bui 2026, arXiv) and a fully peer-reviewed, extensively validated system paper (Chan et al. 2025, AutoCon 177). The paper must explicitly acknowledge that equal treatment in a scoping review does not imply equal evidential weight, and that future systematic reviews would need quality appraisal before claiming which approaches "work."

**Required fix:** Expand Section 6.2 to at least 4–5 substantive paragraphs, each developing one limitation and its specific implication for interpretation. Add the quality appraisal limitation explicitly.

---

### M7. "Chapters" — incorrect document structure terminology for a journal article

**Location:** Throughout — Sections 3, 4, 5 repeatedly referred to as "Chapter 3," "Chapter 4," "Chapter 5."

Journal articles have *sections*, not *chapters*. "Chapters" appear in books and theses. Using "Chapter" throughout signals to an AiC reviewer that this draft originated as course work or thesis rather than having been prepared for journal submission. This is a non-trivial signal — it invites reviewers to question the level of journal preparation.

**Required fix:** Replace all occurrences of "Chapter X" with "Section X" throughout the manuscript. Also update cross-references such as "as discussed in Chapter 5 (Layer 3: The Output Layer)" to "Section 5."

---

### M8. Bar chart (Figure 1) has misleading x-axis with unexplained gaps

**Location:** Figure 1 (Annual distribution of publications).

The x-axis shows years 2010, 2015, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026 — with 5-year gaps between 2010-2015 and 4-year gaps between 2015-2019, then annual thereafter. The visual impression given by a bar chart with equally spaced bars is a continuous annual timeline. Readers will incorrectly infer that no papers appeared in 2011-2014 or 2016-2018, when in fact those years were excluded by the search criteria (no baseline papers from that period). The chart makes the temporal acceleration argument visually misleading.

**Required fix:** Either (a) use a continuous timeline x-axis with equal spacing proportional to actual years (the 5-year gap should appear visually as 5× the width of a 1-year gap), or (b) annotate clearly that years with no bars reflect papers from those years that did not meet inclusion criteria, or (c) separate the two baseline papers (2010, 2015) as a separate pre-VLM baseline category and start the main chart at 2019.

---

### M9. The search strategy excludes important databases

**Location:** Section 2.1.

The search is limited to Web of Science and Scopus. For construction management AI research, standard practice includes at minimum:
- **IEEE Xplore**: Critical for computer vision and AI papers, many of which appear in IEEE Transactions on Industrial Informatics, IEEE Access, and IEEE Robotics and Automation Letters before being indexed in WoS/Scopus
- **ACM Digital Library**: Relevant for human-computer interaction aspects (AR safety systems, Chen 2024 type papers)
- **ASCE Library**: Direct access to ASCE journal papers (JCEM, Journal of Computing in Civil Engineering)

The paper's justification for WoS + Scopus alone (using rabbi2024 and zhong2019 as precedent) is circular — those are also literature reviews that may have had the same gap. The absence of IEEE Xplore is particularly significant given that 3 papers in the corpus came from IEEE venues.

**Required fix:** Either (a) add a search of IEEE Xplore with the same query and report what additional unique records were retrieved, or (b) explicitly defend why IEEE Xplore was excluded (e.g., "preliminary testing showed negligible overlap with non-construction-phase IEEE papers") with documented evidence.

---

### M10. Progress monitoring is treated as secondary despite being in the title

**Location:** Section 1 (Introduction), Section 5.2.

The title states "safety and progress monitoring" with equal billing, but:
- The Introduction devotes approximately 80% of its space to safety (semantic gap, PPE, NLP-CV disconnect, OSHA regulations)
- Progress monitoring is introduced only in one paragraph and largely as an afterthought ("these multimodal systems can create human-readable captions for daily progress")
- Section 5.2 (Progress Tracking) is roughly half the length of Section 5.1 (Safety)
- Of the four RQs, none explicitly names progress monitoring (RQ2 specifically names "safety hazards")

This asymmetry either reflects the actual corpus distribution (if true, it should be reported in Section 3.5 with analysis) or reflects an editorial imbalance in the paper's framing (if so, it should be corrected).

**Required fix:** Either retitle the paper to accurately reflect its safety focus ("with applications to safety management and progress monitoring") or substantially expand the progress monitoring treatment in Section 1 and Section 5.2. Report in Section 3.3 the exact safety vs. progress vs. both breakdown more explicitly and use this to frame the relative coverage.

---

## MINOR ISSUES (Correctional — must be fixed but do not require structural rework)

### m1. Over-reliance on single sources for key claims

- *Alaloul et al. (2022)* is cited 4 times in the first three paragraphs. No single source should anchor more than one or two claims in the same section.
- *Bui et al. (2026)* (an arXiv preprint) is cited 4 times across the paper for substantive claims about the field. A preprint should not bear this evidential weight.
- *Zhang et al. (2025)* is cited 3 times within 3 sentences in Section 4.2 (Paradigm A). Vary sources.

---

### m2. Terminology inconsistency — VLMs vs. MLLMs vs. LMMs

The paper uses "Vision-Language Model (VLM)," "multi-modal large language model (MLLM)," and "Large Multimodal Model (LMM)" — three different terms for what appear to be overlapping categories — without defining the distinctions. Section 1 paragraph 5 introduces MLLMs "upon which VLMs combine image processing and NLP" — this definition is confused. Define the hierarchy (or explain there is none) in Section 1.

---

### m3. The "semantic gap" attribution

**Location:** Section 1, paragraph 4, citing Wu et al. (2021).

The term "semantic gap" in computer vision has a well-documented history dating to Smeulders et al. (2000) in IEEE TPAMI and the broader CBIR literature. Attributing its invention or definition to Wu et al. (2021) is inaccurate. Wu et al. (2021) applied the concept to construction safety — that's the right attribution scope. The attribution should read: "this fundamental limitation — the semantic gap between visual detection and regulatory meaning [Wu et al. 2021] — ..." to credit the construction-specific application without implying Wu invented the concept.

---

### m4. The geographic distribution math in the Limitations is incorrect

**Location:** Section 6.2.

The Limitations state "69% of papers originate from East Asia or North America." From Table 3: China (20) + US (13) + South Korea (6) = 39 papers. If "East Asia" includes Hong Kong (5) and Taiwan (3), then East Asia + North America = 20+6+5+3+13 = 47 papers = 83.9% of 56. Even using the narrow definition (China + Korea + US only = 39), that is 69.6% — but the text says exactly "69%," suggesting a specific calculation was done. State the actual calculation basis explicitly (which countries are included in "East Asia or North America") to make this verifiable.

---

### m5. Anthropomorphic framing of paradigm transitions

**Location:** Sections 4.1, 4.2, 4.3 — recurring phrase pattern.

Each paradigm section ends with "the construction research community transitioned toward..." and begins with "To overcome the [limitation], the construction research community shifted toward...". This rhetorical device implies purposive, coordinated action by a community that actually consists of independent researchers. More importantly, it makes untestable claims about causation (did the community shift because of limitation X, or for other reasons?). AiC expects more precise causal language.

**Suggested alternative:** "Subsequent studies addressed this limitation by deploying..." or "The literature shows a shift toward... with [n] papers from [years] employing..."

---

### m6. The master table (Table 7) inconsistencies

Several entries in Table 7 need verification or standardization:

- **Chen et al. (2024)** — Domain listed as "Safety (VQA)." VQA is a method, not a domain. Use "Safety" and note the VQA approach in the Task column.
- **Wang et al. (2024)** in the Paradigm B section — this row references the wangxiao2024 paper (proactive safety via visual-text similarity) but the label "Wang et al. (2024)" is ambiguous given Wang & El-Gohary (2024) also appears in the table as a separate entry. Distinguish with author initials: "Wang Y. et al. (2024)" vs "Wang X. & El-Gohary (2024)."
- **Bui et al. (2026)** — Domain listed as "Safety & Progress." The paper's actual focus per the title ("Can VLMs understand construction workers?") is primarily worker behavior recognition. The domain classification should be "Safety & Progress (Evaluation)" to signal its exploratory/benchmark character.
- **Hardware column** consistently says "Cloud" for most papers — this column adds little value for papers that don't report deployment environment. If the hardware information is unavailable for most papers, consider replacing this column with one that adds more analytical value (e.g., "Validation Setting" — Lab / Controlled Field / Real Site).

---

### m7. The paper's conclusion overstates contributions

**Location:** Section 7, paragraph 2.

"The review makes three primary contributions to the field. First, it provides the first systematic scoping map..." — as noted in C1, this "first" claim is undefended. Second contribution: "explicitly answers four foundational research questions... synthesizing evidence across a heterogeneous corpus that no prior review has systematically addressed" — the second clause ("no prior review has systematically addressed") is itself the same undefended claim as C1. Third contribution: "identifies the field's most critical gaps" — gap identification is standard output of any review; it is only a contribution if the gaps identified are novel or specifically actionable. Restate contributions with precision.

---

### m8. Publication venue inconsistencies suggest incomplete verification

- **Chen et al. (2024)**: DOI listed as `10.1016/j.autcon.2023.105158` — the `2023` in the DOI path means it was registered in 2023, but the paper is listed as Volume 157, 2024. Verify the volume/year are correct.
- **Chan et al. (2025)**: DOI path `10.1016/j.autcon.2025.106305` suggests 2025 registration. Verify.
- **Tuomisto et al. (2026)**: DOI `10.1016/j.autcon.2025.106571` — again, 2025 registration but listed as 2026. These are likely correct (articles registered in year X sometimes appear in volume/year X+1) but should be verified explicitly.

---

### m9. The framework description promises mathematical fusion explanation that never appears

**Location:** Section 4 opening paragraph.

The chapter introduction states the paper will be "demonstrating how raw visual and textual inputs (Layer 1: Multimodal Inputs) are mathematically fused." However, no mathematical formulation appears anywhere in the paper. The paper describes the fusion architectures in prose but presents no equations, no formal notation, and no mathematical description. If the claim to show mathematical fusion cannot be delivered, remove it from the chapter introduction.

---

### m10. Missing PRISMA-ScR compliance checklist

Standard practice in AiC scoping reviews is to include the PRISMA-ScR 22-item checklist either in the paper itself or as supplementary material, indicating which section of the paper addresses each checklist item. The paper does not include this. While AiC does not always mandate it as a separate document, reviewers familiar with scoping review standards will note its absence.

---

## PRESENTATION AND LANGUAGE ISSUES

### P1. "Chapter" vs "Section" — see M7 above.

### P2. Repeated use of "profound" as a generic intensifier
Used 4 times: "profound complexity" (§1), "profound technological disconnect" (§1), "profound advancements" (§5.1), "profound complexity" appears twice. Vary language.

### P3. "Paradigm-shifting" is used twice in quick succession (§1 and §4 introduction).

### P4. The word "critical" appears more than 10 times. It loses force. Retain for genuinely critical findings; replace with more precise adjectives elsewhere.

### P5. The abstract would benefit from a sentence explicitly stating corpus size, paradigm count, and the key gap finding — currently it reads as generic rather than result-specific.

### P6. No abstract word count is given. AiC has a 250-word abstract limit. Check compliance.

### P7. The paper's affiliation and corresponding author line is missing. Required for submission.

---

## SUMMARY SCORECARD

| Category | Status |
|---|---|
| Novelty claim defensibility | ❌ Undefended |
| Framework originality | ⚠️ Overstated |
| VLM definition | ❌ Missing |
| PRISMA-ScR compliance | ⚠️ Structural deviation |
| Eligibility criteria consistency | ❌ Two violations |
| Temporal paradigm claim | ❌ Contradicted by data |
| Framework figure | ❌ Missing |
| Chapters vs. Sections | ❌ Incorrect throughout |
| Cross-study quantitative synthesis | ⚠️ Insufficient |
| RQ internal consistency | ⚠️ RQ2 scope mismatch |
| Discussion cross-chapter synthesis | ⚠️ Absent |
| Limitations depth | ⚠️ Too brief |
| Data charting reliability | ❌ Unreported |
| Database coverage | ⚠️ IEEE Xplore missing |
| Progress monitoring coverage | ⚠️ Asymmetric |
| Language/terminology consistency | ⚠️ VLM/MLLM/LMM undefined |

---

## RECOMMENDED ACTION FOR THE AUTHOR

Before the next draft is considered for review, the following sequence is recommended:

1. Add the **prior reviews gap table** (C1) and revise the novelty claim
2. Add the **framework figure** (C7) — this is the single highest-impact addition
3. Resolve the **VLM definition** (C3) — this grounds all subsequent analysis
4. Fix the **PRISMA diagram structure** (C4) and resolve the **eligibility violations** (C5)
5. Reframe the **paradigm progression** as typological, not chronological (C6)
6. Replace all **"Chapter"** with **"Section"** (M7)
7. Add **cross-study performance synthesis** in Chapters 4 and 5 (M1)
8. Expand **Limitations** (M6) and add the missing **data charting reliability statement** (M4)
9. Fix the **bar chart x-axis** (M8)
10. Revise **RQ2** to include progress monitoring (M2)
