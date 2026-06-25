# L2: Multi-Stakeholder Review

**Course: Agentic Clinical Research Studio**
**Lab Duration: 90 minutes**
**Core Concept: Role Prompting and Stakeholder Simulation**

---

## 1. Opening Story

Priya had been working on her PhD project for three years. Her study examined whether a machine learning model trained on multiparametric MRI could predict pseudoprogression in glioblastoma patients earlier than standard radiological review. The science was solid. Her supervisory committee had approved the protocol, her preliminary data were compelling, and she had drafted a research proposal she was genuinely proud of.

Then she submitted it to the hospital's research governance committee.

What came back was not a single rejection — it was five separate objections from five different offices, none of which had spoken to the others. The IT security team flagged that she had not specified where the model weights would be stored or how access would be logged. The data governance office noted she had not addressed how patient-linked imaging data would be de-identified before any external collaborator touched it. The clinical informatics lead questioned whether her proposed PACS integration was technically feasible without a 14-month infrastructure project. The neuro-oncology service raised concerns about how clinical staff would be expected to interpret probabilistic model outputs during a multidisciplinary team meeting. And a patient advocate, consulted late in the process, asked a question Priya had genuinely never considered: what happens when a patient asks their consultant why the AI said one thing and the scan reader said another?

Priya knew the scientific question better than anyone in that room. What she lacked was the mental scaffolding to pre-empt these concerns before they became formal objections. She had written her proposal from the perspective of a scientist. Everyone reviewing it was reading from a completely different vantage point.

---

## 2. The Old Workflow

Without agentic AI, a PhD student in Priya's position would typically:

- Write a research proposal based on the scientific question and supervisory feedback
- Submit to governance or ethics and wait weeks for a response
- Receive fragmented comments from multiple offices, often contradictory or siloed
- Revise based on what was explicitly flagged, often missing the underlying concern
- Resubmit, receive another round of comments, and repeat
- Rely on senior colleagues or supervisors who had "been through it before" to informally advise on what reviewers typically care about
- Attend journal club or departmental seminars to absorb clinical workflow concerns over time
- Learn, through experience, that IT security and clinical informatics think about the same system in fundamentally different ways
- Discover patient trust and equity concerns only after a public engagement event or complaint
- Encounter journal reviewer expectations for the first time when a manuscript was rejected

This cycle routinely adds six to eighteen months to a study timeline. More importantly, it teaches researchers to respond reactively rather than design proactively.

---

## 3. The Agentic Workflow

Using role prompting and stakeholder simulation, the same student can:

- Draft a proposal or protocol as normal, based on the scientific question
- Prompt a language model to adopt the role of a hospital IT security officer and produce a structured critique of the proposal
- Repeat the exercise with the model adopting the role of a data governance lead, a clinical informaticist, a patient advocate, a principal investigator reviewing a junior colleague's work, and a peer reviewer for a relevant clinical AI journal
- Collect all six critiques as structured artifacts
- Run a synthesis step, prompting the model to identify which concerns appear across multiple stakeholder perspectives (cross-cutting issues) and which are unique to one viewpoint
- Prioritise revisions based on the synthesis
- Re-run the simulation after revision to check whether the concerns have been addressed
- Produce a revised proposal with an appended stakeholder response matrix

This workflow compresses weeks of sequential feedback into a single working session. It does not replace real stakeholder engagement — it prepares you for it.

---

## 4. Core Concept

Role prompting is a technique in which you instruct a language model to reason and respond from within a specific professional identity, with its characteristic priorities, vocabulary, constraints, and blind spots. When you ask a model to act as a hospital IT security officer, you are not asking it to pretend or to deceive. You are asking it to activate a particular lens — a structured set of concerns that a real professional in that role would bring to any document they reviewed.

The reason this works is that language models trained on large text corpora have encountered substantial material written by, for, and about every stakeholder in a clinical research ecosystem. A model prompted as a data governance lead will draw on governance frameworks, data protection regulations, institutional data sharing agreements, and the kinds of concerns that regularly appear in ethics committee correspondence. It is not perfect — it lacks the lived experience and institutional context of a specific hospital — but it reliably surfaces the class of concern a real reviewer would raise.

What makes multi-stakeholder simulation particularly powerful is the synthesis step. Any single stakeholder critique is partial. The IT team does not see the clinical workflow problem; the patient advocate does not see the infrastructure cost problem. When you run five or six independent role-prompted critiques and then ask the model to synthesise across them, you begin to see structural tensions in your proposal that no single reviewer would have identified. A finding that cross-cutting concerns — issues raised by three or more stakeholder perspectives independently — are almost always the ones that kill studies in ethics review is a reliable pattern experienced researchers recognise.

For a medical PhD student, the most important practical output of this lab is not a cleaner proposal. It is the development of a professional habit: before you submit anything consequential, ask yourself who will read this and what they care about. Agentic role prompting makes that habit fast, structured, and iterable.

---

## 5. Clinical Example

Consider a study proposing to deploy a convolutional neural network to assist radiologists in detecting early leptomeningeal disease on MRI in patients with glioblastoma — a task that is currently inconsistent across readers and has significant prognostic implications.

A straightforward scientific framing of this proposal would describe the model architecture, the training dataset, the validation approach, and the expected clinical benefit. But run this framing through six stakeholder lenses and the picture becomes considerably richer.

The IT security officer notes that the model will need to receive DICOM images from the PACS system, process them through a computational layer not currently part of the clinical network, and return structured output — a data flow that crosses at least two trust boundaries. She wants a data flow diagram and a penetration testing plan before she will approve network access.

The data governance lead observes that the training dataset includes imaging from patients who consented to clinical care, not to AI model development. She flags that retrospective use of imaging data for model training requires a separate legal basis under applicable data protection law and that this has not been addressed.

The clinical neuroradiologist, asked to simulate a colleague reading the proposal, raises a concern about workload: if the model flags a case as suspicious, who is responsible for the follow-up imaging request, and how does that integrate with the existing reporting queue?

The patient advocate asks whether patients will be told that an AI assisted in interpreting their scan, and what recourse they have if they disagree with the AI-assisted interpretation.

The principal investigator reviewing the proposal notes that the primary outcome measure — inter-reader agreement improvement — is appropriate for a validation study but would not support a clinical implementation claim. She recommends a patient outcome endpoint for any future phase.

The journal reviewer for a clinical neuro-oncology journal notes that the paper will need to follow reporting standards for AI in medical imaging, and asks whether the model has been tested on data from a different institution.

Each of these critiques is partial. Together, they constitute a complete picture of the study's vulnerability profile. The student who has run this simulation before submitting to ethics is in a fundamentally different position to the student who has not.

---

## 6. In-Class Activity

**Title: The Stakeholder Gauntlet**
**Duration: 15-20 minutes**
**Format: Individual or pairs**

**Setup (2 minutes)**

Each student opens a one-paragraph summary of their own research project — or uses the provided glioblastoma pseudoprogression case study if they do not yet have a project. This paragraph should describe: the research question, the proposed data source, the model or analytical method, and the intended clinical use.

**Round 1: Single-stakeholder critique (5 minutes)**

Each student prompts a language model with the following structure:

> "You are a hospital data governance lead with ten years of experience reviewing clinical AI research proposals. Read the following research summary and produce a structured critique from your professional perspective. Identify your three most significant concerns, explain the regulatory or institutional basis for each, and suggest how each concern could be addressed in the proposal."

Paste in the research paragraph. Read the critique. Note the top concern.

**Round 2: A different lens (5 minutes)**

Without changing the research paragraph, change only the role in the prompt. Use one of: IT security officer, patient advocate, clinical workflow lead, or journal peer reviewer. Run the same structure. Note whether the concerns overlap with Round 1 or are entirely different.

**Group debrief (5 minutes)**

In the full group: each person names the one concern from Round 2 that surprised them most — the thing they had not thought about before running the simulation. The facilitator records these on a shared board and notes which concerns appear more than once across the group. These cross-cutting concerns are the ones worth addressing first.

**Reflection question:** What would have happened to your study if you had submitted without addressing the concern that surprised you?

---

## 7. Artifact Contract

The following files must be present in your `artifacts/L2/` directory to receive credit for this lab.

| File | Format | Passing Standard |
|---|---|---|
| `stakeholder_critiques.md` | Markdown | Contains one structured critique for each of six stakeholder roles. Each critique names at least three concerns with a rationale. No critique is a copy-paste of another. |
| `synthesis_report.md` | Markdown | Identifies at least two cross-cutting concerns (raised by three or more stakeholders independently) and at least two single-stakeholder concerns. Explains why cross-cutting concerns take priority. |
| `revised_proposal_excerpt.md` | Markdown | Contains the original paragraph plus a revised version. The revision explicitly addresses at least two concerns from the synthesis. Changes are visible and explained in a brief annotation. |
| `reflection.md` | Markdown | 150-300 words. Answers: Which stakeholder perspective was furthest from your own default thinking? What does that tell you about your blind spots as a researcher? |

A submission that includes all four files with substantive content passes. A submission where any file is a template placeholder, is fewer than 100 words (except the reflection minimum), or where critiques are clearly identical in structure and language will not pass.

---

## 8. Common Failure Modes

**Failure mode 1: All critiques sound the same**

This happens when students use a generic role description — "act as a stakeholder" — rather than a specific professional identity with defined responsibilities. Fix: write the role description with institutional specificity. "You are the data governance lead at an NHS teaching hospital, responsible for GDPR compliance and data sharing agreements" will produce a meaningfully different critique than "you are someone who reviews data."

**Failure mode 2: Critiques are too abstract to act on**

A critique that says "consider patient privacy" is not useful. A critique that says "your proposal does not specify how imaging metadata will be stripped before transfer to the external compute environment, which is required under your institution's data sharing policy" is actionable. Fix: include in your prompt the instruction to ground each concern in a specific regulatory, institutional, or professional standard, and to suggest a concrete remediation.

**Failure mode 3: The synthesis step is skipped**

Students collect six critiques and treat them as a list rather than as data to analyse. The synthesis is where the value is. Fix: run a dedicated synthesis prompt after collecting all critiques. Ask the model explicitly to identify overlap and conflict across perspectives.

**Failure mode 4: The revised proposal addresses the words, not the concern**

A student reads "patient consent" as a concern and adds the sentence "patients will provide informed consent" to their proposal. This addresses the flag without addressing the underlying issue — which may be that the consent form does not cover secondary use of data for AI training. Fix: for each concern in the synthesis, ask the model to explain what a satisfactory resolution would look like before attempting to write the revision.

**Failure mode 5: Mistaking simulation for real stakeholder feedback**

A student who has run this simulation may feel they have consulted stakeholders. They have not. Fix: use the simulation to prepare your questions for real consultations, not to replace them. The appropriate next step after this lab is to schedule brief conversations with one or two of the real stakeholders your simulation flagged as high priority.

---

## 9. Responsible Use

The power of stakeholder simulation creates a responsibility that is easy to overlook: the model's output is a plausible reconstruction of stakeholder concerns, not a verified record of any real person's views. A patient advocate prompt will surface concerns that real patient advocates commonly raise — but it cannot speak for any specific community, any specific population, or any specific patient's experience of clinical AI. Using these simulations as a substitute for genuine patient and public involvement would be a governance failure, and in some funding contexts, a reportable deviation from approved protocols. The output of this lab should be treated as preparation for stakeholder engagement, not a record of it.

There is also a subtler risk: well-structured role-prompted critiques can create an illusion of thoroughness. A proposal that has been through six simulated reviews may feel comprehensively stress-tested. But language models will systematically miss concerns that are outside their training distribution — novel regulatory developments, institution-specific policies, local political dynamics, or the informal concerns that experienced clinicians carry but rarely write down. The simulation is a floor, not a ceiling. It is particularly useful for catching the obvious gaps that first-time researchers routinely miss; it is less reliable for the idiosyncratic concerns that only real consultation will surface.

Finally, the structured critique outputs you generate in this lab should not be shared externally or presented as institutional review. They are working documents for your own preparation. If your institution asks whether your proposal has been through stakeholder consultation, the correct answer is no — you have used AI-assisted preparation tools to prepare for that consultation. Misrepresenting AI simulation outputs as actual stakeholder engagement would constitute a research integrity violation under most institutional frameworks.

---

## 10. Further Learning

This section lists categories of real literature and resources to search before releasing this handout. No citations have been fabricated. Instructors should verify and add current references before distribution.

**Literature to search:**

- Search "role prompting large language models" in Google Scholar for empirical work on how role specification affects model output quality and consistency
- Search "prompt engineering clinical AI" in PubMed and Google Scholar for peer-reviewed work on using language models in clinical research preparation
- Search "stakeholder engagement clinical AI governance" in PubMed for literature on who reviews clinical AI proposals and what concerns they raise
- Search "patient and public involvement artificial intelligence research" in PubMed for frameworks on PPI in AI-assisted clinical studies
- Search "GDPR clinical research AI" and "data governance machine learning healthcare" for regulatory literature relevant to European clinical contexts
- Search "reporting standards AI medical imaging" for current guidelines such as CLAIM, CONSORT-AI, or TRIPOD-AI, which are the basis for journal reviewer expectations in this domain
- Search "pseudoprogression glioblastoma MRI machine learning" for current clinical literature on the scientific question used in Section 5

**Course materials to reference by title:**

- This lab builds on foundational prompt engineering concepts covered in Claude Code 101 (Anthropic)
- The role prompting technique described here is elaborated in Anthropic's published documentation on model capabilities and prompting strategies — consult the current Anthropic documentation rather than paraphrasing from memory
- Instructors should review Anthropic's usage policies to ensure this lab's activities remain within recommended use cases at the time of delivery

**Institutional and governance resources:**

- Verify current NHS Health Research Authority guidance on AI in clinical research if teaching in a UK context
- Verify current guidance from the relevant national data protection authority on secondary use of clinical data for AI model training
- Check whether your institution has a specific clinical AI governance framework that should be referenced in Section 9
