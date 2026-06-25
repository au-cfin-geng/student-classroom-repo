# L1: Prompt Contracts

**Agentic Clinical Research Studio**
**Module: Foundations of Reproducible AI-Assisted Research**

---

## 1. Opening Story

Dr. Priya Nair is nine months into her PhD in neuro-oncology. She has just finished curating a dataset of 240 glioblastoma patients and needs to summarise the clinical literature on temozolomide resistance mechanisms to contextualise her findings. She opens a chat interface to an AI assistant, types "Summarise the mechanisms of TMZ resistance in glioblastoma," and receives a polished, confident three-paragraph response. The writing is clear, the concepts are familiar, and she pastes it into her draft. Two weeks later she repeats the query in a new session before a lab meeting and gets a response that is subtly but meaningfully different — different mechanisms are emphasised, a particular signalling pathway is now described as "controversial," and the level of hedging throughout is softer. She cannot tell which response is more accurate. Both sound authoritative.

Priya raises this in a supervision meeting. Her supervisor asks her to show the original query. She cannot reconstruct exactly what she typed. She cannot reproduce which sources were implicitly relied on, which criteria were used to decide what was "key," or how certainty was communicated. Her supervisor points out that the same problem would be a fatal flaw in a clinical trial: if the protocol cannot be reproduced, the results cannot be trusted. Priya realises she has been treating an AI assistant the way a researcher might treat a knowledgeable colleague in conversation — relying on shared context, tone, and informal norms to get a useful answer. That works for informal advice. It does not work for research.

The deeper issue is not that the AI gave wrong answers. The issue is that neither response came with a specification of what the AI was allowed to assume, what sources it could draw on, what structure the output should take, or how uncertainty should be signalled. The conversation was open-ended. Open-ended conversations are fine for exploration. But the moment Priya needed to cite, audit, or reproduce a result, an open-ended conversation became a liability.

---

## 2. The Old Workflow

Without structured AI assistance, a clinical researcher addressing this task would typically:

- Formulate a natural-language question in a chat interface without a written specification
- Accept whatever format the AI chose to use, whether bullet points, paragraphs, or tables
- Have no record of what constraints the AI applied when deciding what to include or omit
- Re-run the query in a new session when they needed to update the summary, producing a structurally different output
- Manually compare the new and old responses without any formal diff or version record
- Trust that hedging phrases like "it is believed" or "evidence suggests" meant the same thing each time, without a defined uncertainty vocabulary
- Paste outputs into manuscripts without a clear statement about what the AI was and was not permitted to contribute
- Discover inconsistencies only when a reviewer or co-author pointed them out

---

## 3. The Agentic Workflow

Using a prompt contract, the same task proceeds as follows:

- Write a structured contract document specifying: (a) the exact input files or data sources the AI may read, (b) the operations it is permitted to perform, and (c) the required output format with named fields and uncertainty markers
- Version-control the contract file alongside the research data so the exact instruction set can be reproduced
- Run the contracted task against any session or model and receive structurally identical output
- Compare outputs across runs using the defined structure rather than reading prose for differences
- Communicate uncertainty through a defined vocabulary (for example: "established," "contested," "insufficient evidence") rather than informal hedging
- Include the contract file as a supplementary document when submitting or presenting the work
- Update the contract explicitly and intentionally when research questions evolve, creating a traceable change history

---

## 4. Core Concept

A prompt contract is a written specification that governs a single AI-assisted research task. It defines three things precisely: what the AI may read, what the AI may do, and what the AI must produce. Think of it as a clinical trial protocol applied to an AI query. A trial protocol does not leave the treatment regimen to the investigator's judgment on the day of administration. It specifies dose, timing, eligibility criteria, and outcome measures in advance, so that the trial can be replicated and the results can be audited. A prompt contract applies the same logic to an AI task.

The inputs section of a contract names the data the AI is permitted to access. This might be a specific set of files, a defined date range of literature, or an exact patient cohort described by inclusion and exclusion criteria. The point is not to restrict the AI arbitrarily. The point is to ensure that every run of the contract operates on the same informational basis, so that differences in output can be attributed to the data or the question rather than to uncontrolled variation in what the AI happened to retrieve or remember. When you write "the AI may read the files in /data/cohort_v3/" you are making an auditable claim about provenance.

The permissions section defines the operations the AI is authorised to perform. May it access the internet? May it generate synthetic examples? May it combine information from multiple sources, and if so, how should conflicts be handled? This is analogous to the operations section of a laboratory protocol. A researcher does not leave it to the technician's discretion whether a sample should be centrifuged or vortexed. Similarly, a prompt contract does not leave it to the AI's discretion whether to extrapolate, synthesise, or qualify. Permissions that are not granted are implicitly denied.

The outputs section specifies the exact form of the deliverable. This means file paths, field names, data types, and uncertainty vocabulary. "Provide a summary" is not a specification. "Write a JSON file to outputs/tmz_resistance_summary.json with keys: mechanisms (array of strings), certainty_level (one of: established, contested, insufficient_evidence), and review_date (ISO 8601 date)" is a specification. The difference matters because structured output can be validated, versioned, compared, and incorporated into downstream analysis programmatically. Prose cannot.

---

## 5. Clinical Example

Consider a research team investigating MGMT promoter methylation as a predictive biomarker in glioblastoma patients treated with temozolomide. They want to use an AI assistant to extract and tabulate evidence from a curated set of 15 review articles they have already downloaded and stored in /data/mgmt_reviews/.

Without a contract, a researcher might ask: "What does the evidence say about MGMT methylation predicting TMZ response?" The AI will produce a fluent response drawing on whatever it knows, mixing information from the provided articles with its training data in ways that cannot be untangled, and presenting uncertainty in informal prose that differs from session to session.

With a contract, the same task is specified as follows. Inputs: the AI may read only the files in /data/mgmt_reviews/ and nothing else — no training knowledge about the topic is to be invoked outside of interpreting the documents. Permissions: the AI may extract, quote, and tabulate claims from those documents; it may not synthesise beyond what the documents state; when documents conflict it must flag the conflict rather than resolve it. Outputs: a structured table saved to outputs/mgmt_evidence_table.csv with columns for study identifier, patient population, MGMT assay method, reported hazard ratio with confidence interval, and a certainty rating drawn from the defined vocabulary.

The resulting table is reproducible. Any team member running the same contract against the same files will produce the same structure. The certainty ratings are defined terms, not impressionistic phrases. The table can be updated by adding new articles to the input directory and re-running the contract, with the change log showing exactly which new inputs changed which rows. This is citable, auditable, and defensible to a journal reviewer or an IRB.

---

## 6. In-Class Activity

**Duration:** 15-20 minutes
**Format:** Pairs or groups of three

**Setup:** Each group selects one of the following clinical research questions:
- What is the current evidence on liquid biopsy for early glioblastoma detection?
- What imaging features on pre-operative MRI are associated with IDH mutation status in glioma?
- What are the reported rates of pseudoprogression following concurrent chemoradiotherapy in GBM?

**Step 1 (5 minutes):** Without discussing it first, each person in the group independently writes the question as they would normally ask it to an AI assistant. Write it down. Do not refine it.

**Step 2 (5 minutes):** Compare what you each wrote. Note: do the queries specify what sources the AI should use? Do they specify the output format? Do they specify how uncertainty should be expressed? What assumptions are embedded in each query that the other person did not make?

**Step 3 (8 minutes):** Together, write a prompt contract for the question. Your contract must include:
- A named input: specify exactly what the AI is allowed to read (you may invent a plausible file path or literature set for the purposes of this exercise)
- At least two explicit permissions and one explicit prohibition
- A required output format with at minimum three named fields and a defined uncertainty vocabulary of your own design

**Debrief:** One group member reads their contract aloud. The facilitator asks: if you ran this contract in six months with a different AI model, would you expect to get structurally identical output? Why or why not? What would you need to change in the contract to make that guarantee stronger?

---

## 7. Artifact Contract

The following table defines the required outputs for the L1 lab assignment. A submission is considered passing when all items in the "Pass Criterion" column are satisfied.

| Artifact | Format | Location | Pass Criterion |
|---|---|---|---|
| Prompt contract document | Markdown or plain text | `outputs/L1_prompt_contract.md` | Contains labelled sections for Inputs, Permissions, and Outputs; all three sections are non-empty |
| Uncertainty vocabulary | Inline within contract or separate JSON | `outputs/L1_prompt_contract.md` or `outputs/L1_uncertainty_vocab.json` | Defines at least three distinct certainty levels with prose descriptions of what each level means |
| Sample output | JSON or CSV as specified in your contract | `outputs/L1_sample_output.<ext>` | File matches the structure your contract specifies; all required fields present; at least one field demonstrates use of the uncertainty vocabulary |
| Reflection note | Plain text or Markdown | `outputs/L1_reflection.md` | Minimum 150 words; addresses at least one way your contract would prevent a failure mode you have personally encountered or can plausibly imagine |

---

## 8. Common Failure Modes

**Failure 1: The contract specifies format but not inputs.**
The most common omission is leaving the input unspecified. "Summarise the literature on X" with a defined output format still produces irreproducible results because the AI draws on different subsets of knowledge in different sessions. Always name the input explicitly, even if it is a set of files you will provide in the next message.

**Failure 2: Certainty vocabulary is decorative rather than operational.**
Students sometimes include an uncertainty vocabulary in their contract but then produce output where every field is rated "established" or where the ratings are inconsistent with the source material. An uncertainty vocabulary is only useful if the AI is given explicit criteria for assigning each level — for example, "use 'established' only when at least two independent RCTs report concordant findings." Without criteria, the vocabulary is cosmetic.

**Failure 3: The output specification is ambiguous about data types.**
Specifying "a table of findings" does not specify whether strings should be quoted, whether missing data should appear as null or as an empty string, whether arrays should be comma-separated within a cell or structured as separate rows. These ambiguities produce outputs that are structurally incompatible across runs. Use explicit data type annotations where precision matters.

**Failure 4: Permissions are assumed rather than stated.**
Researchers sometimes omit the permissions section on the grounds that it is obvious. It is not obvious to an AI system, and it is not obvious to a reviewer auditing the work later. If you do not state that the AI may not access the internet, you cannot later claim that the output was derived solely from your curated inputs. Permissions that are not granted in writing cannot be assumed.

**Failure 5: The contract is written once and never updated.**
A prompt contract is a living document. When the research question evolves, the input data changes, or the AI model is updated, the contract must be revised and the revision must be recorded. Treating the contract as a one-time setup step rather than a versioned protocol defeats the purpose. Keep your contract in version control alongside your data.

---

## 9. Responsible Use

Prompt contracts are a form of scientific documentation, and they carry the same responsibilities as any other methodological record. When you define what an AI may and may not do in a research task, you are making a methodological choice that affects the conclusions you can legitimately draw. A contract that permits the AI to combine your data with its training knowledge about the same population may introduce systematic biases that are invisible unless the contract is disclosed. Journals and funders are beginning to ask for disclosure of AI-assisted methods with the same specificity they expect for laboratory protocols. A well-written prompt contract is not just good practice — it is the material you will need to produce when asked.

There is also a patient safety dimension that is specific to clinical research. If a prompt contract is used to assist with evidence synthesis that will inform a clinical decision support tool, a guideline, or a regulatory submission, the contract becomes part of the chain of evidence supporting a claim about patient care. In that context, an undisclosed or ambiguous contract is not a minor administrative shortcoming. It is a potential safety issue. The discipline of writing precise contracts is the discipline of being honest about exactly what your evidence is and is not. This is foundational to clinical research integrity regardless of whether AI is involved.

Finally, it is worth being explicit about what a prompt contract does not protect you from. A well-formed contract run against poorly curated inputs will produce reproducibly wrong output. A contract that permits the AI to perform tasks beyond its reliable capability will produce consistent-looking but unreliable results. The contract governs the process. You are responsible for ensuring the inputs are valid, the task is within the AI's demonstrated capability, and the outputs are reviewed by a qualified researcher before they are used. Reproducibility is necessary but not sufficient for validity.

---

## 10. Further Learning

This section lists categories of literature to search and resources to consult before this handout is finalised for distribution. No citations in this handout should be treated as verified until independently confirmed.

**Literature to search:**
- Search "prompt engineering reproducibility" and "prompt engineering clinical AI" in PubMed and Google Scholar to identify peer-reviewed work on the reproducibility of large language model outputs in biomedical contexts
- Search "AI governance clinical research" and "generative AI research integrity" in PubMed, Nature, and The Lancet for policy statements from major journals on disclosure requirements for AI-assisted research
- Search "structured output language models" and "constrained generation clinical NLP" for technical literature on approaches to making LLM outputs structurally consistent
- Search "protocol deviation clinical trial reproducibility" for foundational literature on the role of written protocols in clinical research validity, which provides the analogy this lesson builds on
- Search "CONSORT AI" or "SPIRIT AI" for emerging reporting guidelines for AI-assisted clinical studies that may impose requirements relevant to prompt documentation

**Course resources to consult:**
- Review the official Anthropic documentation on structured outputs and tool use, available at docs.anthropic.com, for current best-practice guidance on constraining AI output formats
- This lesson's framing of contracts as a form of research protocol aligns with concepts introduced in Claude Code 101; students who have not completed that course should review its foundational material
- The concept of permissions-based AI governance is also discussed in Anthropic's published model usage policies, which are publicly available and should be reviewed for any course that covers responsible AI use

**Domain resources to confirm:**
- Confirm that the specific clinical examples (MGMT methylation, temozolomide resistance, IDH mutation MRI features) reflect current consensus before using them with students, as clinical evidence in neuro-oncology moves quickly
- Consult the WHO Classification of CNS Tumours (most recent edition) to ensure molecular marker terminology is current
- Review at least one recent systematic review on each clinical example topic to verify that the framing in Section 5 is accurate

---

*Handout version: draft for instructor review. Not for distribution until references verified.*
*Course: Agentic Clinical Research Studio — L1: Prompt Contracts*
