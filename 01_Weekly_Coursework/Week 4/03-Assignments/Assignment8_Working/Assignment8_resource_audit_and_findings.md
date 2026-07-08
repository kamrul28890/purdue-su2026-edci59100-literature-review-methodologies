# Assignment 8 Resource Audit and Findings

## Source Folder Audit

Checked folder:
`D:\Purdue\Courses\02. Summer 2026\01. EDCI 59100-016 DIS\All Review Papers`

The folder contains 73 PDF files across four evidence groups:

- Baseline papers: sensors, hardware, manual reporting, NLP, and unimodal computer vision.
- Transition papers: transformer action recognition, video mining, synthetic data, and open-vocabulary detection.
- Core papers: VLM, CLIP, image captioning, visual-text similarity, VQA, progress reporting, safety inspection, and activity tracking.
- Gap-analysis/review papers: construction computer vision reviews, safety AI reviews, activity recognition reviews, productivity/progress monitoring reviews, and worker-centric scene understanding.

Text extraction status:

- 70 of 73 PDFs were successfully text-extracted into `Assignment8_Working\paper_text_extracts`.
- 3 PDFs did not extract through `pdftotext` even after retrying with temporary ASCII filenames:
  - `Traditional_Progress_80. Computer aided Civil Eng - 2021 - Jung - 3D convolutional neural network-based one-stage model for real-time action.pdf`
  - `Progress_43. Computer aided Civil Eng - 2025 - Zhang - Training-free few-shot construction tool and material detection using pre-trained.pdf`
  - `Progress_99. Computer aided Civil Eng - 2025 - Jeoung - Zero-shot framework for construction equipment task monitoring.pdf`
- The Zhang 2025 and Jeoung 2025 papers are still usable for Assignment 8 because they are already summarized in the Week 3 source matrix. If the final literature review later requires exact quotations from those PDFs, use OCR or replace the files with clean copies.

Conclusion: Yes, there are enough resources to write Assignment 8 here.

## Assignment 8 Requirements

Assignment title: Synthesis Matrix & Organizational Outline.

Purpose:

- Move from analyzing individual studies to organizing the literature review.
- Organize sources into a structured synthesis matrix.
- Identify and refine themes across studies.
- Develop an organizational outline for the literature review.

Required submission items:

1. Synthesis Matrix, worth 8 points.
2. Theme Development / Categorization sheet, worth 6 points.
3. Organizational Outline for Literature Review, worth 6 points.

Formatting/submission:

- Submit the synthesis matrix and theme development sheet as the working document in Excel or Google Sheets format.
- Submit the organizational outline separately in Word or Google Docs format.
- The assignment allows multiple documents.
- File naming instruction in the prompt says: `Draft Literature Review Plan_SemYR_Your LastName_Your FirstName`.

## Rubric Checklist

### 1. Synthesis Matrix, 8 points

To reach proficient:

- Use approximately 12-15 key sources.
- Select sources for relevance and pattern-building, not volume.
- Build from Week 3 Quick Article Notes / Source Evaluation Matrix.
- Add or revise a Theme/Category column.
- Add notes connecting studies.
- Compare similarities, differences, contradictions, and gaps.
- Show movement from summary toward synthesis.
- Avoid a row-by-row annotated bibliography feel.

Risk to avoid:

- Listing individual article summaries without cross-study comparison.

### 2. Theme Development, 6 points

To reach proficient:

- Identify 2-4 emerging themes.
- Give each theme a clear label.
- Define what each theme means.
- List example studies supporting each theme.
- Include tensions, contradictions, or variability within each theme.

Risk to avoid:

- Themes that overlap too much or read like article groups without explanation.

### 3. Organizational Outline, 6 points

To reach proficient:

- Provide a clear, logical structure for the literature review.
- Identify the methodology as a scoping review using PRISMA-ScR guidance.
- Align organization with the scoping review purpose.
- Use a structure that supports synthesis rather than listing studies.
- Include introduction, body organization, and conclusion placeholder.

Risk to avoid:

- A study-by-study outline disconnected from the scoping review method.

## Best 15 Sources For Assignment 8

These are the strongest sources for the current 12-15 source synthesis matrix. They give enough spread across baseline, transition, core safety, core progress, and gap analysis.

1. Zhong et al. (2019) - maps computer vision research in construction and establishes the pre-VLM baseline.
2. Sherafat et al. (2020) - reviews activity recognition for workers and equipment; useful for temporal/action-recognition baseline.
3. Nath et al. (2020) - real-time PPE detection; strong unimodal CV baseline for safety compliance.
4. Wu et al. (2021) - combines computer vision with semantic reasoning; useful bridge from detection to reasoning.
5. Liu et al. (2020) - image captioning for construction activity scenes; early bridge into language-based scene description.
6. Gil & Lee (2024) - zero-shot PPE monitoring based on image captioning; core safety VLM-adjacent paper.
7. Chen et al. (2024) - AR, deep learning, and vision-language query system for worker safety; core interactive safety paper.
8. Wang et al. (2024) - proactive safety hazard identification using visual-text semantic similarity; core safety semantics paper.
9. Chan et al. (2025) - context-aware VLM agent with domain ontology; strong source for domain knowledge and prompt/ontology integration.
10. Hussain et al. (2026) - VLM-based intelligent assistant for onsite safety inspection; strong current safety assistant paper.
11. Bui et al. (2026) - evaluates GPT-4o, Florence 2, and LLaVA-1.5 on construction worker understanding; useful benchmark and limitation paper.
12. Jung et al. (2024) - VisualSiteDiary for captioning photologs and daily reporting; core progress/reporting paper.
13. Xiao et al. (2024) - automated daily report generation from videos using ChatGPT and computer vision; core progress/reporting paper.
14. Jeoung et al. (2025) - zero-shot equipment task monitoring; important temporal and task-monitoring paper, currently usable from Week 3 notes.
15. Zhang et al. (2025) - training-free few-shot construction tool/material detection with pretrained VLM methods; important open-vocabulary/few-shot source, currently usable from Week 3 notes.

Backup/optional swaps:

- Liang et al. (2024), if the matrix needs more CLIP/few-shot object recognition evidence.
- Tohidifar et al. (2024), if the matrix needs stronger synthetic data / annotation evidence.
- Li et al. (2025), if the matrix needs a recent worker-centric scene-understanding review.
- Rabbi & Jeelani (2024), if the matrix needs a broad AI-in-construction-safety review.

## Emerging Themes

### Theme 1: From detection to semantic multimodal reasoning

Definition:
The literature shifts from detecting objects, PPE, workers, and equipment toward interpreting relationships, rules, captions, queries, and safety/progress meaning.

Supporting studies:
Zhong et al. (2019), Nath et al. (2020), Wu et al. (2021), Liu et al. (2020), Gil & Lee (2024), Wang et al. (2024), Chan et al. (2025), Hussain et al. (2026), Bui et al. (2026).

Tensions/variability:
Traditional CV is often precise for bounded detection tasks, but weak at explaining why a scene is unsafe or how site actions relate to rules. VLM-based systems add semantic interpretation but introduce risks such as hallucination, prompt sensitivity, and need for domain adaptation.

### Theme 2: Safety compliance moves from PPE detection to contextual hazard interpretation

Definition:
Safety monitoring begins with PPE/hardhat/vest detection and expands toward worker behavior, visual-text safety rules, ontology-supported compliance, and assistant-style inspection.

Supporting studies:
Nath et al. (2020), Gil & Lee (2024), Chen et al. (2024), Wang et al. (2024), Chan et al. (2025), Hussain et al. (2026), Bui et al. (2026).

Tensions/variability:
PPE detection is easier to benchmark, but contextual safety is harder because hazards depend on relationships among worker actions, equipment proximity, site conditions, and textual rules. Current VLMs can interpret richer situations, but performance varies by task category and image complexity.

### Theme 3: Progress and activity tracking require stronger temporal reasoning

Definition:
Progress-monitoring studies use captioning, video, activity recognition, and report generation to move beyond static images, but true temporal reasoning remains uneven.

Supporting studies:
Sherafat et al. (2020), Liu et al. (2020), Chen et al. (2023), Jung et al. (2024), Xiao et al. (2024), Jeoung et al. (2025), Yang et al. (2023).

Tensions/variability:
Some studies generate useful captions or daily reports from images/videos, while others classify actions or equipment tasks. However, many systems still depend on frame-level or short-clip inference rather than robust long-horizon tracking of evolving site activity.

### Theme 4: Dataset, benchmark, and deployment limitations shape the field

Definition:
Across safety and progress studies, the main barriers are limited construction-specific datasets, inconsistent evaluation metrics, scarce real-site validation, occlusion/noise, and lack of shared benchmarks.

Supporting studies:
Liu et al. (2020), Davila Delgado & Oyedele (2021), Tohidifar et al. (2024), Xin et al. (2024), Bui et al. (2026), Li et al. (2025), Rabbi & Jeelani (2024), Zhong et al. (2019).

Tensions/variability:
Synthetic data, zero-shot models, and pretrained VLMs reduce annotation burden, but they do not fully solve domain shift, real-site visual complexity, or standardized evaluation. Different studies use different metrics such as mAP, precision, recall, F1, BLEU, CIDEr, SPICE, accuracy, or user questionnaires, making direct comparison difficult.

## Recommended Matrix Columns

Use these columns in the synthesis matrix:

- Article
- Year
- Source type/category
- Construction task
- Technology/model type
- Data modality
- Temporal component
- Main finding
- Evaluation metrics
- Theme/category
- Connections to other studies
- Tensions or contradictions
- Gap/limitation
- How it supports the literature review outline

## Recommended Organizational Outline

1. Introduction
   - Define the topic: VLMs and multimodal AI for construction safety monitoring and activity tracking.
   - Define spatiotemporal reasoning in simple language: understanding what is happening, where it happens, and how it changes over time.
   - State purpose: map architectures, data modalities, safety/progress tasks, evaluation practices, deployment barriers, and gaps.
   - State review type: scoping review using PRISMA-ScR guidance.
   - Optional guiding RQs: keep the four RQs from Assignment 6.

2. Scoping Review Approach
   - Briefly describe search strategy, databases, inclusion/exclusion criteria, and charting categories.
   - Explain that the review maps heterogeneous studies rather than calculating effect sizes.

3. Theme 1: From Detection to Semantic Multimodal Reasoning
   - Compare baseline CV/sensor/NLP systems with image captioning, CLIP, VQA, and VLM agents.

4. Theme 2: Safety Compliance and Contextual Hazard Interpretation
   - Organize PPE, safety rule matching, ontology-based reasoning, visual-text similarity, AR query systems, and VLM assistants.

5. Theme 3: Activity Tracking, Progress Monitoring, and Temporal Reasoning
   - Organize video/activity recognition, equipment task monitoring, photolog captioning, and daily report generation.

6. Theme 4: Datasets, Metrics, and Field Deployment Barriers
   - Discuss data scarcity, benchmark inconsistency, domain shift, synthetic data, real-site validation, and metric fragmentation.

7. Conclusion Placeholder
   - Summarize likely insights.
   - Identify gaps and future research directions.
   - State implications for construction safety/progress monitoring.

## Can We Write Assignment 8 Now?

Yes. The available files are sufficient to write the synthesis matrix, theme sheet, and organizational outline.

The strongest path is:

1. Build a focused 15-source matrix using the recommended source list above.
2. Add synthesis columns instead of only article-note columns.
3. Use the four themes above for the theme development sheet.
4. Write the organizational outline in a separate Word document.
5. Run a final checklist against the 8+6+6 point rubric.

The only caution is that three PDFs need OCR or replacement if exact full-text verification is required later. That does not block Assignment 8 because two of the three are already represented in the prior source matrix, and Assignment 8 only requires emerging organization and synthesis rather than final full-text quotations.
