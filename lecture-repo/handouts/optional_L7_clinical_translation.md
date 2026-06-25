# L7 (Extension): Clinical Translation

**Agentic Clinical Research Studio — Optional Extension Lab**
**Concept: Audience-Aware Writing with Explicit Honesty Constraints**

---

## 1. Opening Story

It is 11 pm on a Tuesday when Priya finishes her slide deck for Wednesday's multidisciplinary tumour board meeting. She has spent six months building a deep learning pipeline that segments glioblastoma on post-contrast MRI, and the clinical team has asked her to summarise what it can do. Her Dice similarity coefficient averages 0.71 across the test set. That sounds good — it is better than the older atlas-based method the radiologists currently use for treatment planning. She writes "demonstrates strong performance with potential for clinical integration" on the summary slide, pastes in the distribution plot, and goes to bed.

Wednesday morning, the neuro-oncology lead reads the slide and emails the hospital IT director: "The PhD student has a segmentation tool ready — can we scope a pilot?" Priya is copied on the thread. She opens it on her phone on the bus, stomach dropping. She has not mentioned that performance on cases with prior resection was 0.44. She has not mentioned that three cases in the test set were excluded because the pre-processing pipeline failed on non-standard scanner protocols. She has not explained what Dice actually measures or what a 0.71 means operationally for a radiation oncologist drawing a margin.

No one has lied. Priya is not dishonest. But the briefing she wrote was optimised for conveying progress, not for conveying the limits of that progress. The clinical team, reading it through the lens of clinical workflow rather than benchmarking practice, heard something much closer to deployment-ready than Priya intended. This gap — between what a researcher means and what a clinician hears — is one of the most consistent failure modes in translational AI research. This lab addresses it directly.

---

## 2. The Old Workflow

Without an AI assistant structured to enforce honesty constraints, a researcher preparing a clinical communication would typically:

- Open the slide deck or report template and fill in results as they appear in the methods section
- Reach for headline metrics (mean Dice, AUC, accuracy) because those are the numbers reviewers ask for
- Describe limitations in a brief, generic paragraph at the end ("future work will address edge cases")
- Use shorthand familiar from conference papers ("promising results," "competitive performance") without checking whether clinical readers share that vocabulary
- Focus narrative energy on demonstrating progress — because progress is what secures continued support
- Omit failure cases or subgroup analyses not because they are hidden, but because the researcher does not think of them as the main story
- Send the document without a structured check that the audience can act accurately on what they have read

The result is a technically accurate document that is practically misleading. No individual sentence is false. The cumulative impression is wrong.

---

## 3. The Agentic Workflow

Using an agent structured with explicit honesty constraints and audience-awareness instructions:

- Define the target audience and their decision context before drafting begins (e.g., "radiation oncologist deciding whether to request a pilot, no prior ML training")
- Load the full results — including subgroup performance, exclusion counts, and failure cases — as structured inputs the agent must reference
- Run the agent with a MUST NOT list hard-coded into the system prompt that overrides default optimism
- Generate a first draft calibrated to the clinical reader's vocabulary and decision needs
- Use a second agent pass as a "clinical reader" to flag any claim that implies readiness beyond what the data supports
- Produce a structured limitations section that is proportional in length and placement to the limitations' actual clinical significance
- Output a glossary of any technical term used, with plain-language definitions reviewed before the document leaves the lab

---

## 4. Core Concept

Agentic AI systems, left to default behaviour, are optimistic communicators. This is not a bug in the naive sense — models trained on human text learn that communication is typically a cooperative act where one emphasises what is useful, positive, or progress-indicating. In a scientific context, and especially in a clinical one, this default is dangerous. A model asked to "write a summary of these results for a clinical audience" will, without explicit constraint, produce something that reads like an abstract written for a journal that rewards novelty. It will foreground the best number. It will use hedges ("may," "could," "has potential") that read to a researcher as appropriate caution but read to a clinician as implied near-readiness.

The solution is not to ask the model to "be honest" in a general way. That instruction competes with the equally general instruction to "be helpful," and helpfulness in a communication task feels like making the results sound as good as they reasonably can. The solution is a MUST NOT list: a set of explicit, specific prohibitions that override the default. "Do not claim clinical deployment readiness" is more effective than "be appropriately cautious" because it eliminates a class of outputs rather than asking for a difficult balance. "Do not omit failure cases" forces the model to treat absence as an error, not an editorial choice. "Do not use jargon without explanation" makes the audience the arbiter of whether a word has been earned.

This approach — explicit prohibition constraints on a generative agent — maps onto a principle from responsible AI deployment: that safety constraints are most effective when they are specific, structural, and evaluated at output rather than relying on the model's internal calibration. In a clinical communication context, the constraints function as a proxy for what a good scientific communicator knows to do instinctively after years of experience watching clinicians misread prototype results. You are encoding institutional wisdom as a prompt guard.

The deeper purpose of this lab is not about prompts at all. It is about making visible a translation process that most researchers do informally, inconsistently, and without explicit reflection. When you write the MUST NOT list for a specific piece of clinical communication, you are forced to articulate exactly what you are afraid the reader will conclude incorrectly. That articulation is itself a research integrity exercise. The agent is a tool; the thinking you do to constrain it is the actual skill.

---

## 5. Clinical Example

A research group has developed a convolutional neural network to detect abnormal white matter on FLAIR MRI in patients being investigated for multiple sclerosis. On their internal test set of 200 cases from a single 3T scanner, the model achieves a sensitivity of 0.84 and specificity of 0.79 for detecting lesions above 3 mm. The group is asked to present to the neurology clinic's quality improvement committee, which is exploring whether AI tools could reduce reporting backlog.

Without honesty constraints, the summary might read: "The model demonstrates high sensitivity for MS lesion detection and may support radiologist workflow. Performance is competitive with existing automated tools in the literature."

With explicit constraints applied — do not claim clinical deployment readiness; do not omit failure cases; do not use jargon without explanation — the agent-assisted summary would instead open by stating the study's scope: single site, single scanner, single field strength, elective referral population. It would note that the model was not tested on scanner protocols differing from the training distribution. It would explain in plain language what sensitivity and specificity mean for a radiologist making a referral decision: at 0.84 sensitivity, approximately 1 in 6 lesion-positive cases would be missed by the model alone. It would state explicitly that the tool has not been evaluated for clinical use and that any deployment would require prospective validation under local ethics governance.

The second version is longer. It is less exciting to read. It is the version that allows the committee to make an accurate decision about next steps.

---

## 6. In-Class Activity

**Duration:** 15–20 minutes  
**Group size:** Pairs or groups of three

**Setup:** Each group receives a one-paragraph "results summary" written in standard academic style for a hypothetical clinical briefing. The summary describes a real-sounding but fictional AI tool (e.g., an automated polyp detector in colonoscopy images, or a chest X-ray triage classifier). The summary is technically accurate but structured to foreground best-case performance.

**Step 1 (5 minutes):** Read the summary. Without using any AI tool, each person in the group writes down three things a clinical reader might conclude from this summary that the data does not actually support.

**Step 2 (5 minutes):** As a group, draft a MUST NOT list — at least five specific prohibitions — that you would give to an agent tasked with rewriting this summary for the clinical audience. Be specific: not "avoid overclaiming" but "do not describe this tool as suitable for unsupervised triage."

**Step 3 (5 minutes):** One person in the group enters the MUST NOT list and the original summary into the agent and requests a rewrite. The group reads the output together.

**Discussion (5 minutes):** Did the agent honour all the constraints? Were there claims in the rewrite that still felt misleading despite the MUST NOT list? What constraint did you miss? What does this tell you about the difficulty of specifying honesty programmatically?

**What to bring to the debrief:** Your MUST NOT list and one sentence describing the most important constraint you identified only after seeing the agent's output.

---

## 7. Artifact Contract

The following files constitute a passing submission for this lab. All files should be committed to your lab repository in the `lab7/` directory.

| File | Format | Passing Criteria |
|---|---|---|
| `must_not_list.md` | Markdown | At minimum 5 specific, falsifiable prohibitions. Each prohibition must name a specific class of claim or omission, not a general aspiration ("do not say the model is ready for deployment" not "be cautious"). |
| `system_prompt_v1.txt` | Plain text | Full system prompt used for the first draft. Must include the MUST NOT list and explicit audience description. |
| `draft_v1.md` | Markdown | Raw output from the first agent pass. Not edited. |
| `review_notes.md` | Markdown | Your written assessment of draft_v1: which constraints were honoured, which were violated, and what was still misleading despite the constraints. Minimum 150 words. |
| `draft_v2.md` | Markdown | Revised output after prompt iteration. Must be demonstrably different from v1 in response to at least one identified failure. |
| `glossary.md` | Markdown | Plain-language definitions of every technical term used in draft_v2. Each definition must be written for a clinical reader, not a researcher. |

A submission that contains only the final polished draft without the intermediate artefacts does not pass. The process is the point.

---

## 8. Common Failure Modes

**1. The MUST NOT list is too abstract.**
"Do not overclaim" does not constrain the model. The model does not believe it is overclaiming. Effective prohibitions name specific phrases or claims: "Do not use the phrase 'promising for clinical application'"; "Do not describe performance without reporting the failure-case subgroup." Revise any prohibition that a well-intentioned model could honour while still producing a misleading document.

**2. The audience description is too generic.**
"A clinical audience" is not a constraint. "A neurosurgeon reviewing this prior to consenting a patient for a biopsy" is a constraint. The more specifically you define what the reader needs to know and what decision they are making, the more precisely the agent can calibrate vocabulary, emphasis, and level of detail. Generic audience descriptions produce generic calibration.

**3. The student edits the draft before saving it as v1.**
The artifact contract requires the raw output. If you tidy the draft before saving it, you lose your diagnostic information. You will not know what the agent got wrong, and therefore you will not know what to fix in your prompt. Treat the first draft as data, not as a document.

**4. The constraints address tone but not content.**
It is possible to produce an honest-sounding document that still omits key information. A model can write with perfect hedging language about the headline metric while never mentioning that one subgroup was excluded from analysis. Check not only whether the constraints changed the tone of the output but whether they changed what facts are present.

**5. The student concludes the exercise proves AI cannot be trusted for clinical communication.**
This is the wrong takeaway. The exercise demonstrates that an agent without explicit constraints produces what you should expect given its training: an optimistic, progress-oriented summary. The same model, with a well-constructed MUST NOT list and a clear audience description, can produce a clinically responsible document. The lesson is that the researcher bears responsibility for the constraints, not that the technology is inherently unreliable.

---

## 9. Responsible Use

The clinical translation problem this lab addresses is not new. Medical journals have editorial standards for reporting AI studies — checklists that require disclosure of training data characteristics, subgroup performance, and failure cases — precisely because the instinct to foreground positive results is universal and well-documented. When you use an agentic AI system to assist with clinical communication, you are adding a layer of automation to a process that already required careful judgment. The automation does not transfer the judgment requirement to the model. You remain responsible for the accuracy and completeness of anything that leaves your lab under your name.

There is a specific governance dimension worth naming explicitly. In many jurisdictions, communication about AI tools to clinical staff — even communication explicitly framed as research rather than product — may fall under institutional research governance policies. If your institution has a clinical AI governance committee or a research integrity office, a draft briefing document should be reviewed there before distribution to clinical stakeholders. The fact that you are describing a prototype, not a CE-marked or FDA-cleared device, does not exempt the communication from scrutiny. Clinicians act on what they read. A briefing that leads to an informal trial of an unvalidated tool in patient care has consequences that extend beyond scientific discourse.

Finally, consider the structural incentive this lab is designed to make visible: the pressure to show progress creates pressure to communicate progress optimistically. That pressure is real and it is not always conscious. The MUST NOT list is a tool for making your own motivated reasoning legible to yourself before it shapes a document. Good scientific communication is not natural, and expertise in research does not automatically transfer to expertise in responsible clinical communication. Treating this as a learnable, improvable skill — rather than a character trait — is both more accurate and more useful.

---

## 10. Further Learning

The following are categories and search terms to use when grounding this lab in current literature. No paper titles, author names, or DOIs are provided here because this document was prepared without live database access. Verify all citations independently before including them in course materials.

**Literature searches to run:**

- Search PubMed and Google Scholar: "AI clinical communication" AND ("overclaiming" OR "overstatement")
- Search PubMed: "reporting guidelines" AND "artificial intelligence" AND "medical imaging" — look for CLAIM, STARD-AI, TRIPOD-AI, and related checklists
- Search Google Scholar: "prompt engineering" AND ("clinical AI" OR "medical AI") — note publication years; this is a fast-moving area
- Search PubMed: "translational gap" AND "machine learning" AND "clinical" — studies documenting the gap between research performance and clinical utility
- Search: "AI hype" AND "clinical decision support" — there is a body of work on how AI capabilities are communicated to clinicians and policymakers

**Standards and frameworks to verify current versions:**

- CONSORT-AI reporting standard (search for current version and endorsing journals)
- SPIRIT-AI standard for clinical trial protocols involving AI
- TRIPOD-AI prediction model reporting guideline
- NHS AI Lab Skunkworks and MHRA guidance documents on communicating AI prototype performance (verify current UK guidance)
- FDA guidance documents on AI/ML-based software as a medical device (SaMD) — relevant for the governance section

**Course and documentation references:**

- Concepts in this lab relate to system prompt design and constraint specification, which are covered in Claude Code 101 (Anthropic). Refer students to the official Anthropic documentation for current model behaviour and prompt engineering guidance rather than to this handout.
- The concept of a MUST NOT list as an explicit safety constraint connects to alignment research literature; search "Constitutional AI" (Anthropic, publicly available) for the underlying approach.

**People and groups to verify are still active in this area:**

- Research groups publishing on AI clinical translation at the Alan Turing Institute, Stanford HAI, and MIT CSAIL — verify current published work rather than citing institutional affiliations
- Clinical AI governance bodies in your own jurisdiction — these change frequently and country-specific guidance is most relevant for your students

---

*This handout is part of the Agentic Clinical Research Studio optional extension series. It is intended for researchers with an active prototype result who are preparing communication for a non-technical clinical stakeholder. It is not a guide to regulatory submission or clinical trial design.*
