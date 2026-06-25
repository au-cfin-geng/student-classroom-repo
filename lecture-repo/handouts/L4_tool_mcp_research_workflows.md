# L4: Tool & MCP-Aware Research Workflows

**Agentic Clinical Research Studio**
**Lab 4 of 8**

---

## 1. Opening Story

Maya is a third-year PhD student in neuro-oncology. Her dissertation depends on integrating three data sources: a local folder of MRI preprocessing scripts, a shared departmental database of de-identified glioblastoma cases, and a curated library of PDFs she has been collecting for two years. Her supervisor has also asked her to pull recent preprints from a public repository and compare them against her existing literature notes.

On a Tuesday morning, she sits down to draft the methods section. To do this properly she needs to open the imaging database, search her PDF library, check the GitHub repository where the lab stores analysis pipelines, and cross-reference the preprint server. She does each step manually, copying and pasting snippets into a single document, losing track of which version of a script she referenced, and accidentally including a column from the database that contains a patient identifier she thought had been removed. She does not notice this until her supervisor flags it during a lab meeting three weeks later.

The incident triggers a review with the institution's data governance office. Maya has done nothing malicious. The problem is structural: she was working across too many systems at once, without any mechanism to log what she accessed, when, or why. Her tools had no concept of what she was permitted to read versus what she was merely able to reach. The incident adds two months to her timeline. She begins to wonder whether there is a more disciplined way to work.

---

## 2. The Old Workflow

Without agentic AI, a researcher in Maya's position would typically:

- Open each data source in a separate application or browser tab
- Manually copy text, figures, or file paths from one context into another
- Rely on personal memory or informal notes to track which sources were consulted
- Have no automated record of which files were read, which were modified, and which were only browsed
- Grant themselves broad access to shared drives or databases "just in case" they needed something
- Discover permission violations or data leakage only after the fact, through review or audit
- Write methods sections that describe general practices rather than the exact sequence of operations performed
- Maintain no formal distinction between read-only sources (published papers, public datasets) and write-sensitive sources (patient records, unpublished results)

---

## 3. The Agentic Workflow

Using context engineering and permission-aware tool design, the same researcher can:

- Define a precise set of tools the AI agent is permitted to use at the start of each session
- Assign explicit read-only versus read-write permissions to each data source before work begins
- Designate forbidden zones — specific directories, tables, or identifiers the agent cannot access under any circumstances
- Set up human approval gates for any action that modifies files or accesses sensitive data
- Receive a structured audit log at the end of each session describing exactly which tools were called, in what order, and what data was returned
- Separate the task of literature synthesis (read-only, public sources) from dataset analysis (controlled access, logged) using different tool configurations
- Reproduce the exact sequence of operations later, because the agent's tool calls are recorded and replayable
- Demonstrate compliance to an ethics board or data governance office using the session log rather than memory

---

## 4. Core Concept

Context engineering is the practice of deliberately shaping what an AI agent can see and do before it begins working. It is not enough to give an agent access to your tools and ask it to be careful. In clinical research, "careful" is not a governance category. What matters is the formal structure of permissions: which tools exist, what each tool is permitted to read or write, and at which points a human must approve an action before the agent proceeds.

The Model Context Protocol (MCP) is a standard way of describing tools to an AI agent. Think of it as a formal contract between the researcher and the agent. When you define an MCP tool, you specify not just what the tool does but what it is allowed to touch. A tool that searches your PDF library can be given read-only access to that folder and nothing else. A tool that queries your imaging database can be scoped to de-identified fields only. A tool that writes output files can be restricted to a single designated output directory. The agent works within those constraints automatically, without requiring you to repeat your intentions in each prompt.

Minimal necessary access is the principle that an agent should be given only the permissions it genuinely requires to complete the current task — not the permissions it might conceivably find useful. This mirrors the data minimization principle familiar from clinical research ethics: you collect only the data you need for your stated research question. Applied to AI tools, it means a literature review agent does not need write access to your data folder. A preprocessing script runner does not need to read your email or calendar. Violations of this principle are the primary source of accidental data leakage in agentic research workflows.

Human approval gates are decision points where the agent pauses and presents a proposed action to the researcher before executing it. They are not a sign of distrust in the agent. They are a governance mechanism, equivalent to requiring a second signature on a protocol amendment. You decide in advance which categories of action require approval — deleting files, accessing patient-adjacent data, pushing changes to a shared repository — and the agent stops at those points and waits. This transforms the agent from a system that acts on your behalf into a system that acts with your authorization. The distinction matters enormously when you are later asked to explain what happened and why.

---

## 5. Clinical Example

Consider a research assistant agent configured to support a brain tumour imaging study. The study involves three data sources: a directory of anonymized DICOM files, a CSV registry of patient outcomes (de-identified per IRB protocol), and a folder of published papers on glioblastoma grading.

A well-configured tool set for this agent might look like the following. The literature search tool has read-only access to the papers folder and the ability to call a public preprint API, but no access to any local patient data. The imaging tool has read-only access to the DICOM directory and can run preprocessing scripts, but cannot write output files without triggering a human approval gate. The registry tool can query the outcomes CSV but is explicitly forbidden from accessing any column that contains dates of birth, admission dates, or any field flagged in the data dictionary as potentially re-identifying. All three tools write every call to an audit log stored in a separate, append-only directory.

When the agent begins a session, it cannot see the forbidden columns even if it tries. If it needs to write a processed image to disk, it presents the proposed file path to the researcher and waits. At the end of the session, the audit log shows every query, every file read, every write that was approved or denied. If the institution's data governance office asks what data the agent accessed on a given date, the researcher can produce a complete record in minutes.

This is not a restriction on the agent's usefulness. It is the condition under which the agent's usefulness can be trusted.

---

## 6. In-Class Activity

**Duration:** 15-20 minutes
**Format:** Pairs or small groups of three

**Setup:** Each group receives a scenario card describing a clinical research task. Example scenarios include: performing a systematic literature review on immunotherapy response in glioblastoma, extracting summary statistics from a de-identified patient registry, or comparing two versions of an analysis pipeline stored in a shared repository.

**Step 1 — Map the data landscape (5 minutes).** On paper or a shared document, list every data source the task would require. For each source, mark whether it contains identifiable or potentially re-identifying information, whether it is read-only or modifiable, and whether it is internal (institutional) or external (public).

**Step 2 — Design the permission structure (7 minutes).** For each data source, write a one-sentence permission rule. Use the format: "The [tool name] tool may [read/write/query] [specific resource] and may NOT access [forbidden zone]." Identify at least one human approval gate: an action that would require researcher confirmation before the agent proceeds.

**Step 3 — Identify the audit trail (3 minutes).** Decide what the audit log for this task should record. At minimum: which tool was called, what input was provided, what was returned, and the timestamp. Discuss: if this session log were presented to an IRB, would it be sufficient to demonstrate appropriate data handling?

**Step 4 — Report back (5 minutes).** Each group presents their permission structure in two sentences. The class discusses: where did groups draw the line between minimal necessary access and useful access? Were there disagreements?

---

## 7. Artifact Contract

The following files are required to pass Lab 4. All files should be placed in the `outputs/L4/` directory of the course repository.

| File | Format | Passing Criteria |
|------|--------|-----------------|
| `tool_permission_map.md` | Markdown table | Lists every tool used in your workflow, its permitted data sources, its forbidden zones, and its read/write status. At minimum three tools must be defined. |
| `approval_gates.md` | Markdown list | Names at least two human approval gate triggers with a one-sentence justification for each. Must reference a specific action type (e.g., file write, database query) not a general principle. |
| `session_audit_log.json` or `session_audit_log.md` | JSON or Markdown | A sample or real audit log from a tool-assisted session. Must include tool name, timestamp, input summary, and output summary for each call. Fabricated logs are not acceptable — run a real session. |
| `reflection.md` | Markdown, 200-400 words | Describes one decision you made about minimal necessary access and one instance where you added or removed a permission based on what you learned during the lab. |

---

## 8. Common Failure Modes

**Granting broad access "to avoid interruptions."** The most common mistake is configuring tools with wide permissions to minimize the number of approval gates. This defeats the purpose of the exercise and creates genuine compliance risk. Interruptions from approval gates are governance signals, not inconveniences. If a particular gate fires too frequently, the correct response is to reconsider whether the task is scoped correctly — not to remove the gate.

**Defining permissions at the folder level when file-level control is needed.** Saying "the agent can access the data folder" is insufficient when that folder contains both de-identified summary files and raw data with indirect identifiers. Permission rules should be as specific as the data requires. When in doubt, be more restrictive and expand deliberately.

**Forgetting to define forbidden zones explicitly.** It is not enough to list what the agent is allowed to access. You must also state what it is not allowed to access. Agents do not infer restrictions from omission. If a database table is off-limits, that prohibition must be written into the tool definition, not left to chance.

**Writing approval gates that are too vague to enforce.** An approval gate that says "ask before doing anything sensitive" does not function as a governance mechanism. Approval gates must be tied to specific, observable action types. "Ask before writing any file to a path outside `outputs/L4/`" is enforceable. "Be careful with data" is not.

**Treating the audit log as optional.** Some students skip the audit log step because their session "went fine." An audit log that only exists when something goes wrong is not an audit log — it is an incident report. The discipline of logging every session, regardless of outcome, is what makes the log meaningful when it is eventually needed.

---

## 9. Responsible Use

The permission structures you design in this lab are not just technical configurations. They are expressions of your ethical obligations as a clinical researcher. When you define what an AI agent is allowed to access, you are making a decision equivalent to those you make when you design a data collection protocol: what is necessary, what is proportionate, and what requires additional oversight. The fact that an agent could theoretically access something does not mean it should. Your institution's IRB, data governance office, and any applicable research ethics framework all apply to how AI agents handle data — not just to how you handle it directly.

Audit trails created by tool-aware agents have a secondary value that is easy to underestimate: they are reproducibility artifacts. A session log that records every tool call and its output is, in principle, a machine-readable methods section. Future researchers, reviewers, and regulatory bodies can inspect not just what you concluded but exactly what operations were performed to reach that conclusion. This is a significant improvement over traditional research workflows, where the methods section describes intent rather than execution. You should design your audit logs with this future reader in mind.

Finally, be aware that tool access in agentic systems can accumulate over time in ways that are not obvious. An agent that starts a session with carefully scoped permissions may, through a sequence of individually reasonable steps, end up accessing or synthesizing information in ways you did not anticipate. This is why human approval gates for write operations and data access are not a feature you add when you are worried — they are a default posture you adopt at the start, and remove only when you have a specific, documented reason to do so. The discipline is not about distrust. It is about maintaining the ability to account for your work.

---

## 10. Further Learning

This section lists resource categories to search and verify before this handout is released. Do not use citations from this list without confirming they are real, current, and accurately described.

**Literature to search:**
- Search "data minimization principle clinical research" in PubMed and Google Scholar to find current frameworks used in IRB and ethics guidance documents
- Search "audit trail electronic health records research" in PubMed for standards around logging data access in clinical contexts
- Search "model context protocol AI tools" and "MCP specification" in Google Scholar and Anthropic's public documentation to find current technical references
- Search "permission-based access control AI agents" in ACM Digital Library and arXiv for recent work on agent authorization frameworks
- Search "reproducibility clinical AI research" in PubMed and Nature for articles addressing the gap between reported and executed methods
- Search "GDPR data minimization research" and "HIPAA minimum necessary standard" for regulatory frameworks relevant to clinical data access

**Course resources to reference by title:**
- This lab builds on concepts introduced in Claude Code 101 (Anthropic)
- The MCP tool definition format is documented in Anthropic's official MCP documentation — refer students there for current syntax, as specifications evolve
- The concept of human-in-the-loop approval gates is discussed in Anthropic's published guidance on agentic systems

**Publicly known resources to verify:**
- The Model Context Protocol (MCP) specification is publicly available through Anthropic and should be linked to its current stable version at time of release
- FAIR data principles (Findable, Accessible, Interoperable, Reusable) are relevant background for the audit trail discussion — verify current citation through go-fair.org
- The CONSORT and SPIRIT reporting guidelines are relevant analogues for the argument that methods should describe execution, not just intent
