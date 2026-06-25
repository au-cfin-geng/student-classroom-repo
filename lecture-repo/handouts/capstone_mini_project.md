# Capstone: Agentic Clinical Research Mini-Project

**Course:** Agentic Clinical Research Studio
**Type:** Independent Capstone Project
**Estimated Time:** 8–12 hours across design, build, and reflection phases

---

## 1. Opening Story

Dr. Priya Nair is eighteen months into her PhD on treatment response prediction in high-grade glioma. She has learned to run survival analyses in R, she has a curated dataset from two hospital systems, and her supervisor has approved a research question: can a multi-modal feature set — combining imaging-derived texture features, genomic markers, and clinical covariates — predict six-month progression-free survival better than the current standard radiological assessment alone?

The problem is not the research question. The problem is the workflow. Every week Priya spends two to three hours searching PubMed for new papers on her subtopics, another hour reformatting extracted data tables from PDFs, another hour writing the same boilerplate statistical code she wrote last month for a slightly different cohort slice, and then another hour trying to remember which version of the analysis she ran last Tuesday and whether those results match the ones she sent her supervisor. The actual thinking — the part where she decides what comparison matters, what the result means, what the next experiment should be — is buried under coordination work. She is not moving slowly because she lacks skill. She is moving slowly because no single part of the workflow talks to any other part.

Her supervisor raises an eyebrow during their last meeting. "You have all the pieces. What would happen if they were connected?" Priya knows exactly what he means, and she also knows she has never had to design that connection herself. She has used tools. She has not designed a system.

---

## 2. The Old Workflow

What a researcher like Priya does without an integrated agentic system:

- Manually searches PubMed, Google Scholar, and bioRxiv on separate days using separate browser tabs, keeping a personal spreadsheet of papers found
- Reads abstracts individually, copies relevant passages into a notes document, and loses track of which passages came from which papers
- Downloads PDF tables manually, transcribes them into a spreadsheet, and discovers formatting inconsistencies only when running the analysis
- Writes analysis code from scratch or hunts through old notebooks for a prior version, then adapts it line by line for the new dataset
- Runs the analysis, saves results in a folder with a name like "final\_v3\_revised\_forreal", and emails a summary to her supervisor
- Receives feedback, updates the analysis manually, and repeats the cycle with no record of what changed between versions
- Writes interpretation notes separately from the results, so the connection between a result and its clinical meaning lives only in her head
- Discovers two weeks later that a preprocessing step she changed in version 3 invalidated a comparison she reported in version 2

---

## 3. The Agentic Workflow

The same research cycle, redesigned using at least three concepts from this course:

- A literature monitoring agent runs on a schedule, searches for new papers matching a structured query, and deposits structured summaries into a shared evidence file — Priya reviews the digest, not the raw flood
- A document extraction agent reads new PDFs added to a watched folder, extracts tables and key numerical results using structured prompts, and appends them to a versioned data store with provenance metadata
- An analysis orchestration agent takes a parameterized analysis specification written by Priya, calls her existing R or Python scripts with those parameters, logs all inputs and outputs, and writes a structured results file with the run configuration attached
- An interpretation agent drafts a plain-language summary of each result set, flagging comparisons that fall below a minimum effect size threshold Priya has defined, and asking her a specific question about clinical significance before finalizing
- All agents write to a shared audit log so Priya — and her supervisor — can reconstruct exactly what ran, when, and why
- Priya's time shifts from coordination to judgment: she approves literature inclusions, sets analysis parameters, and decides what the results mean

---

## 4. Core Concept

The central concept in this capstone is **workflow integration**: the deliberate design of how multiple agentic components hand work to each other, what each component is responsible for, and where human judgment must interrupt the chain before it continues.

Most early uses of AI in research treat each tool as a standalone accelerator. You ask the model to summarize a paper. You ask it to write a code snippet. You ask it to help you word a sentence. These uses are real and valuable, but they do not compose. Each interaction starts from scratch, shares no context with the last, and produces no persistent artifact that the next step can build on. When the interaction ends, the knowledge evaporates.

An integrated agentic workflow is different. Each step produces a structured artifact — a file, a database record, a log entry — that is readable by the next step. The workflow has a defined state at any moment. When something goes wrong, you can inspect the state and understand what happened. When something changes — a new dataset, a revised hypothesis, a corrected preprocessing step — you can rerun only the affected portion of the workflow while the earlier steps remain unchanged. This is not merely efficiency. It is reproducibility, and reproducibility is the minimum bar for any scientific claim.

The hardest design decision in an integrated workflow is not technical. It is determining which decisions belong to the machine and which belong to you. An agent can retrieve papers. It cannot decide which papers are worth trusting. An agent can extract a numerical result from a table. It cannot decide whether that result was measured in a way that makes it comparable to your cohort. An agent can flag a p-value below 0.05. It cannot decide whether the effect it describes would change a clinician's treatment decision. Every workflow you design must have explicit handoff points — moments where the agent stops, presents its output, and waits for your judgment before the next stage begins. Designing those handoffs thoughtfully is the intellectual core of this capstone.

---

## 5. Clinical Example

Consider a research team studying IDH-mutant glioma recurrence patterns across three treatment centres. Their integrated workflow looks like this.

A literature agent runs weekly, searching for new publications on IDH mutation status, treatment response, and recurrence timing. It deposits structured summaries — not raw papers — into a shared evidence table. Each row records the paper's source, the population studied, the primary outcome, and any numerical result the agent extracted. The team reviews this table weekly and marks rows as "included," "excluded," or "needs verification." The agent never makes inclusion decisions; it only surfaces candidates.

When new MRI-derived feature data arrives from a participating centre, an extraction agent runs a defined pipeline: it checks the file format, validates that required columns are present, applies a pre-specified normalization procedure, and writes a cleaned dataset with a provenance record showing the source file name, processing date, and any rows flagged as anomalous. A researcher inspects the anomaly flags before the data enters any analysis.

An analysis agent then takes a configuration file — written by the researcher — that specifies the outcome variable, the covariate set, the model type, and the train-test split strategy. It runs the analysis, saves results, and writes a structured summary noting the primary comparison, the effect estimate with confidence interval, the number of patients contributing to each group, and a plain-language sentence drafted for the researcher to edit. The researcher edits and approves that sentence before it goes anywhere near a draft manuscript. The system never writes claims autonomously; it drafts them for human sign-off.

---

## 6. In-Class Activity

**Duration:** 15–20 minutes, in pairs or trios

**Goal:** Design the skeleton of an integrated agentic workflow before writing any code or prompts.

**Instructions:**

1. Each group selects one clinical research bottleneck from a provided list, or proposes one from their own work. (3 minutes)

2. On paper or a shared document, draw three boxes in a row. Each box is one agent or automated step. For each box, write:
   - What it receives as input (file type, format, where it comes from)
   - What it produces as output (file type, format, where it goes)
   - What decision it is NOT allowed to make — what must wait for a human (2 minutes per box, 6 minutes total)

3. Draw the handoff points between boxes. At each handoff, write one sentence describing what the human does and what they are approving or rejecting. (3 minutes)

4. Write one sentence naming the single most important failure mode in your design. What happens to your results if step 2 produces garbage without anyone noticing? (2 minutes)

5. Share your skeleton with another group. Each group asks one question: "What would break this?" (2–3 minutes)

There is no code in this activity. The goal is to think before building. A workflow designed on paper in twenty minutes will have fewer structural errors than one written directly in code over three hours.

---

## 7. Artifact Contract

Your capstone submission consists of the following files. All artifacts are required. A submission missing any row in this table is incomplete regardless of quality elsewhere.

| Artifact | Format | Passing Standard |
|---|---|---|
| Workflow Design Document | Markdown (.md) | Contains a diagram or structured description of each agent/step, its inputs, outputs, and handoff points. Clearly identifies at least 3 course concepts used and explains why each was chosen. |
| At Least One Working Agent | Python script or Jupyter notebook (.py or .ipynb) | Runs without error on the provided sample data. Produces a structured output file. Includes inline comments explaining design decisions. |
| Sample Output Artifact | .csv, .json, or .md depending on agent type | Produced by running the agent. Filename includes a timestamp or run ID. A separate companion file (.txt or .md) explains what the output means and what a researcher should verify before trusting it. |
| Audit Log | Plain text or .jsonl | Records at minimum: run start time, input files used, parameters set, output file written, any flags or warnings generated. Must be machine-readable and human-readable. |
| Reflection Document | Markdown (.md), 400–600 words | Answers three questions: (1) What did you design that the agent cannot decide, and why? (2) What surprised you about building an integrated workflow versus using individual tools? (3) What would you do differently if you were designing this for a clinical trial rather than a research study? |

---

## 8. Common Failure Modes

**Building before designing.** The most common mistake is opening a code editor before completing a workflow diagram. Students who write code before they have decided what each step produces and what the next step expects will spend most of their time debugging integration problems, not research problems. Diagram first. Write after.

**Making every step autonomous.** Some students, excited by what agents can do, remove all human checkpoints to make the workflow feel more automated. The result is a system that produces confident-sounding outputs with no mechanism for catching the point where something went wrong. An integrated workflow without explicit human judgment checkpoints is not a research tool; it is a sophisticated way to generate plausible-looking errors at scale.

**Treating the agent's text as the finding.** An agent that drafts a results sentence is producing a draft for your review, not a conclusion. If you copy the agent's interpretation into your analysis document without editing and verifying it against your own understanding of the data, you are not doing science. You are laundering the agent's guess through your authorship.

**Ignoring provenance in output files.** If your output file does not record where the input came from, what parameters were used, and when the run happened, you cannot reproduce the result. Name files with run identifiers. Log everything. This is not optional bookkeeping; it is the minimum requirement for any result you would report to a supervisor or include in a manuscript.

**Overcomplicating the architecture.** A five-agent pipeline that mostly works is harder to debug and harder to trust than a two-agent pipeline that works reliably. Start with the minimum number of components that addresses your bottleneck. Add complexity only when you have evidence the simpler design is genuinely insufficient.

---

## 9. Responsible Use

The integration of multiple automated steps in a research workflow amplifies both capability and risk. When a single manual step produces an error, that error is typically caught at review. When a five-step automated pipeline produces an error at step two, that error propagates through steps three, four, and five before anyone sees it — and it may arrive dressed in the language of a complete, coherent analysis. Responsible workflow design therefore requires that you treat every automated step as a potential error source, not a reliable unit of computation. Build in verification steps. Test your pipeline on data whose correct answer you already know before running it on data whose answer you do not.

Scientific integrity in an agentic context extends to authorship and attribution. If your agent drafts text that appears in a manuscript, you are responsible for every claim in that text. You cannot attribute an error to the model. You cannot argue that a fabricated citation was the agent's fault. Before any agent-drafted material enters a scientific document, it must be verified against primary sources by a human who is named as an author and accepts responsibility for its accuracy. This standard is not stricter than conventional scientific practice; it is the same standard, applied carefully to a new kind of writing tool.

Governance considerations matter even at the student project scale. If your workflow touches real patient data — even de-identified cohort data provided for the course — you are working under the ethical and legal framework that governs that data. Automated workflows that log, copy, or transmit data must be reviewed against the data use agreement under which the data was provided. When in doubt, ask your supervisor or your institution's research data governance office before running any automated pipeline that touches protected data. No course deadline justifies bypassing those protections.

---

## 10. Further Learning

This section lists categories of literature to search and resources to verify before distributing this handout. Do not treat any citation here as confirmed — locate and review each source directly.

**Literature to search:**

- Search "agentic AI research workflow reproducibility" in PubMed and Google Scholar. Focus on papers from 2022 onward discussing automated literature review pipelines, agent-assisted data extraction, and reproducibility frameworks for computational research.
- Search "LLM clinical decision support governance" in PubMed. Look for consensus statements, editorial commentary, or frameworks from major clinical AI working groups on appropriate use and oversight requirements.
- Search "research workflow automation provenance tracking" in computer science and informatics literature. The concepts of data lineage and audit trails have established literature in data engineering and bioinformatics that grounds the audit log requirements in this handout.
- Search "prompt engineering reproducibility" to find papers discussing how non-deterministic outputs from language models affect scientific reproducibility, and what mitigation strategies have been proposed.
- Search "IDH glioma treatment response prediction" for current literature to validate the clinical example in Section 5. Verify any specific claims against recent systematic reviews or meta-analyses before teaching with this example.

**Course materials to reference by title only:**

- This capstone integrates skills introduced across the Agentic Clinical Research Studio module sequence.
- Foundational prompting and tool-use concepts align with material covered in Claude Code 101.
- Anthropic's publicly available documentation on responsible AI use and model capabilities should be consulted directly at anthropic.com; do not reproduce passages from that documentation in student-facing materials.

**Publicly known resources to verify:**

- The TRIPOD+AI reporting guideline (Transparent Reporting of a Multivariable Prediction Model for Individual Prognosis or Diagnosis, AI extension) — search for the most current version and verify it is still the active standard before citing it in course materials.
- The EQUATOR Network guidelines relevant to the clinical domain used in examples — verify the current URL and confirm the guideline is still maintained.
- Your institution's research data governance and ethics office policies on automated data processing — these vary by institution and must be verified locally before distributing guidance to students.
