# L0: Agentic Clinical Research Studio

**Course:** Agentic Clinical Research Studio
**Session:** Lab 0 — Workspace Setup and the Agentic Mindset
**Approximate duration:** 90 minutes (30 min reading + 20 min activity + 40 min setup)

---

## 1. Opening Story

It is Thursday afternoon. Maria is a third-year PhD student in neuro-oncology. Her supervisor has asked her to prepare a preliminary analysis comparing two MRI segmentation approaches for her next committee meeting. She opens her laptop.

The segmentation script she wrote six weeks ago is somewhere in a folder called `analysis_v3_FINAL_revised`. She finds it after eight minutes of searching, but cannot remember which Python environment it requires. Her notes from the last time she ran it are in a Google Doc she shared with her supervisor, but that document has since accumulated comments, tracked changes, and a version history that tells her nothing useful about what she actually did. The script runs but produces a figure she does not recognise. She spends forty minutes trying to reconstruct what parameters she used. She eventually gives up and re-runs from scratch with defaults, unsure whether the result is meaningful.

Meanwhile, the conversation she had with Claude last week — where she worked through the statistical rationale for her comparison metric — is gone. She used the browser interface, did not save the thread, and closed the tab. The reasoning she built up over an hour of back-and-forth exists nowhere except, faintly, in her memory. By Friday evening she has something to show her supervisor, but she cannot explain exactly how she got there, and she knows she could not reproduce it.

---

## 2. The Old Workflow

What Maria does today, without an agentic setup:

- Opens a browser tab for Claude, a separate terminal for code, a Google Doc for notes, and a file explorer for data — four disconnected surfaces
- Has a useful reasoning conversation with an AI assistant, then closes the tab and loses the entire thread
- Copies code snippets from the AI into a local script by hand, often losing context about why a particular approach was chosen
- Saves analysis outputs (figures, tables, summary statistics) with inconsistent naming into a folder that grows opaque over time
- Writes a methods description from memory days after the analysis, reconstructing decisions she has already half-forgotten
- Cannot show a collaborator or ethics reviewer an unbroken chain from question to result
- Repeats earlier reasoning from scratch each new session because there is no record of what was already established

---

## 3. The Agentic Workflow

What Maria does after completing this lab:

- Opens a single terminal session in her project directory; Claude Code reads the project's CLAUDE.md and immediately knows the context, conventions, and current state of the work
- Issues a plain-English instruction; the agent reads relevant files, proposes a plan, executes steps, and writes outputs directly into the project
- Every action — file read, script run, figure saved — is traceable in the session transcript and in git commit history
- The CLAUDE.md is updated at the end of each session to capture decisions made, so the next session begins with full context restored
- Artifacts (figures, tables, processed data) are committed alongside the code that produced them and the reasoning that motivated the approach
- A collaborator joining the project can read the commit log and CLAUDE.md to understand the research trajectory without a handover meeting
- Maria can answer her supervisor's question "why did you choose that metric?" by pointing to a specific commit message and the reasoning captured in the project memory

---

## 4. Core Concept

**What makes a workflow "agentic"?**

A chat interaction is a single exchange: you write a question, the model writes a response, and the loop ends. The model has no persistent memory of your project, cannot take actions in your environment, and produces no durable artifact beyond the text on your screen. This is useful for brainstorming, but it is not research infrastructure.

An agentic workflow connects reasoning to action to artifact in a continuous loop. The model can read files in your project, execute code, write new files, and then reason about the results of those actions — all within a single session. Crucially, because every action touches the filesystem, and because you are using version control, every step leaves a traceable record. The loop looks like this: a prompt describes an intention; the agent takes an action (reading, writing, running); an artifact is produced (a figure, a processed dataset, a summary table); the artifact is committed to the repository. The next session begins by reading that record.

The CLAUDE.md file is the bridge between sessions. It is a plain text file at the root of your project that describes what the project is, what conventions you are using, what has been decided, and what remains open. Think of it as the project's working memory — not a final report, but the kind of notes a careful researcher writes so that their future self (or a new collaborator) can pick up where they left off. The agent reads CLAUDE.md at the start of every session, which means the context you build up over weeks of work is never lost to a closed browser tab.

This architecture matters for clinical research specifically because reproducibility and auditability are not optional. When your methods chapter asks "how was this threshold selected?", the answer should be traceable. When an ethics committee asks whether your preprocessing pipeline was applied consistently, the git history should confirm it. Agentic workflows do not merely make you faster — they make your work auditable in a way that isolated chat interactions never can.

---

## 5. Clinical Example

Consider a PhD project studying glioblastoma recurrence using longitudinal MRI. The researcher needs to compare tumour volumes at baseline and at three follow-up timepoints across forty patients. Each timepoint has a DICOM series, a segmentation mask, and a clinical note.

Without an agentic workspace, this project typically lives in three places: raw data on a network drive, analysis scripts in a local folder, and interpretive notes in a document. When the researcher discovers that one patient's segmentation was performed with a different protocol, tracing back which downstream results are affected requires manually inspecting files and emails.

With an agentic workspace, the project has a single root directory with a CLAUDE.md that records the segmentation protocol, the inclusion criteria, the outlier decisions made along the way, and the current state of the analysis. When the protocol discrepancy is discovered, the researcher opens the project and says: "Patient 07 used protocol B for the month-three scan. Identify which output files depend on that scan and flag them." The agent reads the dependency structure of the analysis scripts, identifies the affected outputs, and writes a summary to a file called `audit_notes/patient07_protocol_flag.md`. That file is committed. The record exists. The committee can see it.

This is not a hypothetical improvement. It is the difference between research that can be defended and research that cannot.

---

## 6. In-Class Activity

**Title:** Orientation and First Artifact
**Duration:** 15-20 minutes
**Works individually or in groups of 2-3**

**Step 1 — Start the workspace (5 min)**

Follow `START_HERE.md` steps 1–4. Paste `prompts/00_start_agentic_studio.md` into Claude Code and let it run.

Claude will confirm the Python environment, create the output directory structure, start the dashboard, and write your first orientation artifact. Read what it produces carefully — note which steps it took and which it skipped.

**Step 2 — Navigate the dashboard (5 min)**

In the course dashboard, click through each sidebar section in order:

- **Welcome** — what does the course map tell you about the order of labs?
- **How to Start** — does this match what Claude just did?
- **L0 through L5** — open each. What is the lab question for each?
- **Progress** — how many artifacts does it report? Why?

With a neighbour: which two labs look most relevant to your current research? Compare choices and discuss why.

**Step 3 — Read the L0 artifact (5 min)**

Open `reports/labs/L0_orientation.md` in VS Code. Read it.

Ask yourself: if a collaborator opened this file six months from now, what would they learn about your research direction? What is still missing? In two minutes, write one sentence that improves the orientation artifact's usefulness and ask Claude to update the file. Commit the updated file.

**Step 4 — Group debrief (3 min)**

Discuss: what surprised you about what Claude did automatically versus what required your input? What does "the artifact is the record, not the chat" mean after seeing this in practice?

**Deliverable:** `reports/labs/L0_orientation.md` exists and contains your actual research question (not a placeholder). `outputs/labs/L0/status.json` is present. Both files are committed to git.

---

## 7. Artifact Contract

The following artifacts are required to complete Lab 0.

| Artifact | Format | Location in repo | Passing criterion |
|---|---|---|---|
| Orientation report | Markdown | `reports/labs/L0_orientation.md` | Contains course name, date, your clinical research question (not placeholder), and at least one lab you plan to try |
| Completion indicator | JSON | `outputs/labs/L0/status.json` | Parseable JSON with `"status": "ok"` and `"lab": "L0"` |

Both files are created by the launch prompt in `prompts/00_start_agentic_studio.md`. You then personalise the orientation report with your real research question before committing.

A passing artifact names an actual research question you are working on — not the generic brain tumour example from the handout. The purpose of L0 is to anchor the rest of the course to your work.

---

## 8. Common Failure Modes

**1. Treating the orientation artifact as a formality.**
The L0 report is not a box to tick. It is the first entry in your research record for this course. A report that says "brain tumour segmentation" because that is what the handout example uses is useless to you two days later. Write your actual problem. If you do not have a PhD question yet, write the most specific question you can formulate right now — and note that it is provisional.

**2. Committing too infrequently.**
Committing only when something "works" means the record of your reasoning process — the attempts that failed, the parameters you tried and rejected — is lost. Commit after every meaningful decision, even if the output is preliminary. A commit message like `explore: tested threshold 0.4, result was noisy — reverting to 0.3` is valuable research documentation.

**3. Treating the agent as a search engine.**
The agentic loop only produces traceable artifacts if you ask the agent to write things down. A conversation that produces a good recommendation but no committed file is still a closed browser tab. After every significant reasoning exchange, ask the agent to write a summary to a file and commit it.

**4. Skipping L0 and starting at L1.**
Each lab in this course builds on the agentic mindset introduced in L0. Students who skip orientation tend to write prompts that produce outputs they cannot explain, skip the commit step, and arrive at the capstone without a coherent record. L0 takes thirty minutes. Do it properly.

**5. Version control anxiety leading to avoidance.**
Some researchers avoid committing because they are worried about committing the wrong thing, breaking something, or cluttering the history. In a research project (as opposed to a software product with users), a messy git history is far better than no git history. You can always clean up a history; you cannot recover reasoning that was never recorded.

---

## 9. Responsible Use

**Scientific integrity and the traceable record.**
One of the most significant risks in AI-assisted research is the gradual drift of analytical decisions away from documented rationale. When a researcher asks an AI to suggest a preprocessing step and implements it without recording the reasoning, that step becomes invisible to peer review, to ethics committees, and to future collaborators who inherit the code. The agentic workspace is designed to close this gap — but only if researchers actively use the audit trail rather than treating it as a side effect. Every committed file and every commit message is a scientific record. Write them as if they will be read by a reviewer who is trying to assess whether your methods were sound.

**Data governance and what should not enter the workspace.**
A project workspace connected to an AI agent is not automatically a safe place for patient-identifiable data. Before placing any data in a project directory that will be processed by an agent, confirm that your institutional data governance agreement covers this use case, that the data has been de-identified according to your ethics approval, and that no files will be transmitted to external services without your knowledge. For this lab, use synthetic or publicly available data only. If you are unsure whether a particular dataset is appropriate, consult your institution's research data officer before proceeding.

**Authorship, credit, and the role of the agent.**
Using an agentic workflow does not transfer authorship or intellectual responsibility to the model. The model executes; you decide. When you write a methods section, you are responsible for every step the agent took on your instruction. If the agent made a decision you did not review — chose a parameter, selected a subset, imputed a missing value — and you did not catch it, that is a methods error, not an AI error. The commit history exists partly so you can review what the agent actually did, not just what you asked it to do. Review your diffs before you commit them.

---

## 10. Further Learning

This section lists categories of literature and resources that should be searched and verified before this handout is finalised for distribution. Do not cite any source that has not been independently verified.

**Literature to search:**
- Search "reproducible research workflows computational science" in Google Scholar for foundational papers on version-controlled research practice (look for work from approximately 2014 onward)
- Search "provenance tracking clinical AI" in PubMed for recent work on audit trails in medical AI pipelines
- Search "FAIR data principles biomedical research" for the original FAIR paper and subsequent applications in clinical imaging
- Search "large language model agent tool use" in arXiv for technical foundations of agentic AI architectures
- Search "AI documentation clinical research governance" in PubMed and in regulatory body publications (FDA, EMA, MHRA) for relevant guidance documents

**Anthropic documentation and courses:**
- This lab's workspace setup aligns with concepts covered in the official Anthropic documentation for Claude Code, particularly the sections covering project memory and CLAUDE.md conventions. Verify current documentation at docs.anthropic.com before citing specific section titles, as documentation is updated frequently.
- The prompt-action-artifact loop described in Section 4 draws on concepts introduced in Claude Code 101. Students who want a deeper technical foundation should complete that course before or alongside this lab.

**Institutional and regulatory resources:**
- Verify your institution's current research data governance policy — the version available at time of course delivery should be cited, not a general reference
- Search your national research ethics body's website for current guidance on AI-assisted research methods; guidance in this area is evolving rapidly as of 2025-2026
- The Open Science Framework (osf.io) contains public pre-registration templates that are useful models for the kinds of decisions CLAUDE.md should capture
