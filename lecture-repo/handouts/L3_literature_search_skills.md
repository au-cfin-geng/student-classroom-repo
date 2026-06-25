# L3: Literature Search Skills

**Course: Agentic Clinical Research Studio**
**Lab 3 of 8**

---

## 1. Opening Story

Priya is eighteen months into her PhD on glioblastoma multiforme treatment response. Her supervisor has asked her to produce a structured summary of the current evidence on bevacizumab combined with standard-of-care temozolomide, specifically: what patient subgroups show a progression-free survival benefit, and what biomarkers have been investigated as predictors of response. This is a reasonable ask. She has done it before for other topics.

She spends the first afternoon running searches in PubMed, Embase, and Google Scholar. The terms she picks seem obvious at first, but the results are noisy. Some papers use "anti-VEGF" rather than "bevacizumab." Some trials report overall survival but not PFS. She refines her search three more times over two days, each time catching something she missed. She downloads forty-three papers and skims abstracts to filter down to twenty-two that look relevant. Then she opens a spreadsheet and begins manually tagging: intervention, comparator, outcome, sample size, biomarker reported, quality grade. By Friday evening she has a draft table. She is not confident she has been consistent. She re-reads her own column definitions twice.

When she finally writes the narrative summary, she feels good about it. Her supervisor reads it, then asks three questions she cannot immediately answer — one about a sub-analysis she is not sure she captured, one about a trial she may have missed, and one about whether two papers she cited are actually reporting the same cohort under different primary endpoints. Priya goes back to the literature. Another three days. The bottleneck is not intelligence or effort. It is the gap between a fluent written summary and a traceable, reproducible evidence base.

---

## 2. The Old Workflow

What a researcher without agentic AI would do:

- Translate a clinical question into search terms manually, relying on memory and trial and error
- Run separate searches in multiple databases (PubMed, Embase, Cochrane, Google Scholar) with no shared query log
- Download PDFs, rename them inconsistently, and filter by reading abstracts one at a time
- Build a tagging spreadsheet from scratch, defining columns mid-process as new patterns emerge
- Write a narrative summary that synthesises across papers without a machine-readable audit trail
- Revise the whole process when the supervisor changes the scope of the question
- Receive no warning when a claim in the summary is not directly supported by any extracted datum

---

## 3. The Agentic Workflow

The same task with a literature search skill:

- Frame the clinical question once using a PICO structure (Population, Intervention, Comparator, Outcome)
- Pass the PICO to the skill, which decomposes it into Boolean search strings for multiple databases
- Review and approve the search strings before any search is run — this is a required human checkpoint
- The skill executes the searches, collects results, and produces a structured evidence table with explicit confidence markings
- Each claim in the output is tagged with the source and a confidence level (high / moderate / low / not found)
- The complete query log, input PICO, and output table are saved as versioned artifacts
- Changing the clinical question means editing the PICO and re-running, not starting over
- Hallucinated citations are structurally impossible because the skill only extracts from papers it actually retrieved

---

## 4. Core Concept

A Claude Skill is a reusable, structured workflow. It has defined inputs, a sequence of processing steps, at least one human approval checkpoint, and structured outputs. The word "skill" here does not mean an ability the model has by default. It means a workflow you have deliberately designed, tested, and can re-run reliably. Think of it the way a good clinical protocol is different from an experienced clinician improvising: both may produce good results on a good day, but only the protocol produces traceable, reproducible results on every day.

The literature search skill described in this lab has four stages. First, PICO decomposition: the model takes your clinical question and breaks it into structured components — who the population is, what the intervention is, what it is being compared to, and what outcomes matter. This step forces precision. A vague question like "does bevacizumab help brain tumour patients" cannot be decomposed without clarification; the skill will ask you to specify. Second, search string generation: the model translates each PICO element into Boolean search strings with MeSH terms, synonyms, and field tags. You see these strings before they are used. Third, the human approval checkpoint: you review the strings, edit them if needed, and explicitly approve before the skill proceeds. Nothing is searched until you say so. Fourth, evidence extraction: the skill reads the retrieved papers, extracts structured data into a table, and marks each data point with a confidence level based on how directly the paper supports the claim.

The confidence marking is the part most researchers underestimate. When you ask a large language model to summarise the literature in free text, it produces fluent prose that blends well-supported claims, weakly supported claims, and occasionally fabricated citations in a way that is nearly impossible to distinguish by reading alone. The skill architecture breaks this by separating retrieval from synthesis. The model cannot cite what it did not retrieve. Every claim in the output table points to a specific paper, and every paper was either found by the search or it was not. The confidence markings are not the model's opinion of the science; they are the model's judgment about whether the retrieved evidence directly, partially, or only tangentially supports the claim you asked about.

The human approval checkpoint deserves particular attention because it is easy to click past. The search strings the model generates are a hypothesis about what the literature contains. They may be too broad, too narrow, missing a critical synonym, or using terminology that has shifted over time in your sub-field. You are the expert on your clinical domain. The checkpoint exists because the model is not. Spending five minutes reviewing and correcting the search strings before the skill runs will save you hours of downstream confusion. This is not a limitation of the tool; it is the intended design.

---

## 5. Clinical Example

You are investigating whether IDH mutation status modifies the survival benefit of temozolomide in lower-grade gliomas. Your clinical question is: "In adults with WHO grade 2-3 gliomas, does IDH mutation status predict overall survival benefit from temozolomide chemotherapy compared to radiotherapy alone?"

The PICO decomposition the skill produces might look like this:

- Population: adults, WHO grade 2 or 3 glioma, IDH mutation status reported
- Intervention: temozolomide chemotherapy (any schedule)
- Comparator: radiotherapy alone, or radiotherapy followed by observation
- Outcome: overall survival, progression-free survival, treatment response by IDH status (IDH-mutant vs IDH-wildtype)

From this, the skill generates search strings including terms like `("IDH mutation" OR "isocitrate dehydrogenase") AND ("temozolomide" OR "TMZ") AND ("glioma" OR "low-grade glioma" OR "anaplastic glioma") AND ("overall survival" OR "progression-free survival")` with field restrictions appropriate for PubMed.

You review these strings. You notice the skill has not included the older classification term "oligodendroglioma" which appears in earlier literature before the 2016 WHO classification revision. You add it. You approve. The skill runs.

The output evidence table has columns: first author, year, journal, study design, sample size, IDH status breakdown, primary outcome, result, direct quote supporting extraction, confidence level. A row with confidence "low" might mean the paper reported IDH status but did not stratify the survival analysis by IDH — the data is present but you would need to contact the authors or find a sub-analysis. A row with confidence "high" means the paper directly addresses the question with a pre-specified subgroup analysis. The table is your evidence base. The narrative summary you write on top of it is your interpretation. These two things are now separate and auditable.

---

## 6. In-Class Activity

**Duration: 15-20 minutes**
**Format: pairs or small groups of 2-3**

**Setup (2 minutes):** Each group selects one of the following clinical questions, or proposes a variation relevant to their own research:

- Do proton pump inhibitors modify the cardiovascular risk profile of clopidogrel in post-stent patients?
- Does time from symptom onset to thrombectomy predict functional outcome in large-vessel ischaemic stroke?
- Is dexamethasone dose associated with neurocognitive outcome in childhood acute lymphoblastic leukaemia?

**Step 1 — Manual PICO (4 minutes):** Without using any AI tool, write out your PICO for the chosen question on paper. Define each element as specifically as you can. Note any terms where you are uncertain whether synonyms exist.

**Step 2 — Skill run (6 minutes):** Open the course environment. Pass your clinical question to the literature search skill. Compare the skill's PICO decomposition to your own. Note every difference — places where the skill added something you missed, and places where you disagree with the skill's interpretation.

**Step 3 — Checkpoint review (4 minutes):** Review the search strings the skill has generated but do not approve them yet. As a group, identify at least one change you would make before approving. Make the change. Approve.

**Step 4 — Debrief (4 minutes):** Each group reports one thing the skill got right that was easy to miss manually, and one thing they had to correct. The class discusses: what knowledge did the correction require that the model could not have had?

**What to submit:** A screenshot or text export of your PICO comparison (your version vs the skill's version) and the final approved search strings, saved to your artifacts folder as `L3_pico_comparison.md`.

---

## 7. Artifact Contract

The following files must be present in your `artifacts/` directory to pass this lab. All formats are plain text or Markdown unless otherwise noted.

| File | Format | Passing criteria |
|---|---|---|
| `L3_pico_comparison.md` | Markdown | Contains your manually written PICO and the skill's PICO side by side; at least one documented difference with a brief explanation |
| `L3_search_strings_approved.md` | Markdown | The final search strings after your edits, with a one-sentence rationale for each change you made |
| `L3_evidence_table.csv` or `.md` | CSV or Markdown table | At least 5 rows; required columns: author/year, study design, sample size, primary outcome, confidence level, direct quote |
| `L3_reflection.md` | Markdown (150-250 words) | Addresses: what the skill caught that you might have missed; what required your domain knowledge to correct; one thing you would change about the skill design |

A submission that contains a narrative summary without the evidence table will not pass, even if the summary is excellent. The purpose of this lab is the structured, traceable evidence base — not the summary.

---

## 8. Common Failure Modes

**Accepting the search strings without reading them.** The checkpoint exists to be used. The most common student error is clicking through without reviewing. The skill's strings are a first draft. They will often miss sub-field terminology, older nomenclature, or abbreviations specific to your clinical area. Budget five minutes for this step.

**Confusing "confidence level" with "quality of evidence."** The confidence level in the skill's output marks how well the retrieved evidence answers your specific question. A high-quality randomised trial can have a low confidence level if it did not measure the outcome you asked about. These are different dimensions. Do not collapse them in your write-up.

**Asking a question that is too broad.** "What is the evidence on immunotherapy in cancer?" cannot be sensibly decomposed. The PICO structure will fail at the population element. If the skill returns more than a few hundred candidate papers, your question is likely under-specified. Narrow the population, the intervention, or the outcome before proceeding.

**Treating the evidence table as a finished product.** The table is your starting point, not your conclusion. Confidence markings are machine judgments. You are responsible for validating the highest-stakes extractions against the original papers. Plan to spot-check at least five rows in the final table.

**Re-running without versioning.** If you change your PICO and re-run the skill, save the new output under a new filename. Do not overwrite the original. Your ability to explain why your final table differs from your first run is part of your scientific accountability.

---

## 9. Responsible Use

The literature search skill does not search every database. It searches where it can reach, using the interfaces and credentials available in the course environment. Absence of a finding in the skill's output is not the same as absence in the literature. Before drawing a conclusion from a negative result — "there is no evidence that X predicts Y" — you are responsible for confirming that the search was adequately powered to find such evidence if it existed. This means checking that your search strings would have returned relevant papers had they been published, and that the databases searched cover the relevant literature for your clinical domain. For some specialties, conference abstracts, grey literature, or registry data are essential; the skill does not automatically search these.

Evidence synthesis has long-standing norms around reporting: PRISMA for systematic reviews, GRADE for evidence quality, CONSORT for trial reporting. These frameworks exist because the history of clinical research contains many examples of selective reporting, publication bias, and outcome switching that distorted the apparent evidence base and, in some cases, influenced clinical practice in harmful ways. Using an agentic skill to accelerate your literature search does not exempt you from these obligations. If your output will inform a systematic review, a clinical guideline, or a grant application, it should meet the same reporting standards as a manually conducted review. "The AI did the search" is not a sufficient methods section.

Finally, be explicit in any publication or report about the role of the skill in your workflow. Describe the PICO you used, the search strings that were approved, the databases that were searched, and the date the search was run. Literature searches have an expiration date; evidence published after your search date is outside your scope. A well-documented methods section that describes an agentic-assisted search is scientifically stronger than a vague description of a manual search, because it is reproducible. Lean into this. Transparency is not a vulnerability here; it is a strength.

---

## 10. Further Learning

This section does not contain fabricated citations. The following are categories and search terms for the instructor or course team to verify before distributing this handout.

**Database and methodology standards to confirm are current:**
- Search the PRISMA 2020 statement (Preferred Reporting Items for Systematic reviews and Meta-Analyses) via equator-network.org
- Confirm current GRADE handbook version via gradeworkinggroup.org
- Verify current PubMed MeSH term structure for "glioma," "IDH mutation," and "bevacizumab" to ensure examples are taxonomically accurate

**Literature to search for relevance to core concept:**
- Search: "PICO framework systematic review" in PubMed — confirm consensus on PICO as standard clinical question structure
- Search: "large language model hallucination systematic review" in PubMed and Google Scholar — evidence for the hallucination problem motivating the skill architecture
- Search: "AI-assisted literature search clinical" in PubMed — for any published evaluations of AI tools in systematic review workflows
- Search: "retrieval augmented generation clinical evidence" for technical background on why retrieval-before-synthesis reduces confabulation

**Course materials to cross-reference:**
- This lab builds directly on concepts introduced in Claude Code 101 (Anthropic's introductory documentation on structured skill design and human-in-the-loop workflows)
- The Anthropic documentation on tool use and human approval patterns in multi-step agents should be reviewed to confirm that the checkpoint architecture described in Section 4 reflects current platform behaviour
- The Anthropic prompt engineering guide contains relevant guidance on structured output formatting; reference by title only, confirm the guide is still publicly available before citing

**Clinical examples to fact-check:**
- The bevacizumab/temozolomide example in Section 1 and Section 5: verify that bevacizumab is not currently standard-of-care for GBM in the jurisdiction where the course is taught, to avoid implying clinical guidance
- The IDH mutation example in Section 5: verify that the WHO 2021 CNS tumour classification is the current standard, and that the search string example uses terms consistent with current nomenclature
- The lower-grade glioma example: confirm that "WHO grade 2-3" is still appropriate terminology post-2021 classification revision (the 2021 WHO classification introduced changes to grading criteria)

---

*Handout version: L3 — draft for instructor review. Do not distribute to students until clinical examples and references have been verified per Section 10.*
