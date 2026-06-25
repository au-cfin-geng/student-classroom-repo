# L5: Subagents & Workflow Orchestration

**Agentic Clinical Research Studio**
**Module 5 of 8**

---

## 1. Opening Story

Dr. Priya Nair is nine months into her PhD in neuro-oncology. Her supervisor has asked her to lead a methods section for a systematic review comparing first-line treatment protocols for glioblastoma multiforme. The review will span molecular epidemiology, clinical trial design, regulatory compliance across three jurisdictions, and patient-facing communication. Priya is competent in each of these areas individually — but they do not live in the same part of her brain, nor in the same stack of papers on her desk.

She spends the first week doing a broad literature search. By the second week, she is writing the methods section, only to realise that her inclusion criteria do not match the statistical framework she planned to use. She emails a biostatistics colleague for advice. While waiting for a reply, she begins drafting the ethics subsection, then notices that the regulatory landscape she cited is for the EU but her trial data are primarily North American. She flags this, goes back to the literature, and loses three days. The statistical advice arrives, but it assumes a different patient population than the one she described. She rewrites. Her supervisor reads a draft and asks why the plain-language summary for lay readers uses jargon that her biostatistics reviewer would not have caught.

By week six, Priya has a patchwork document assembled from four separate workflows that never fully spoke to each other. The literature review does not cleanly inform the statistical plan. The compliance notes are not integrated with the methods narrative. The lay summary was written last and does not reflect the final study design. None of this is Priya's fault. The problem is structural: clinical research workflows are genuinely multidisciplinary, and no single person — or single prompt — can hold all the expertise simultaneously without something leaking.

---

## 2. The Old Workflow

What Priya's situation looks like without agentic AI:

- Conduct a literature search using PubMed, Embase, or Cochrane; manually read and tag abstracts
- Draft inclusion/exclusion criteria in a word processor; revise iteratively as reading deepens
- Write a statistical analysis plan in a separate document; reconcile with inclusion criteria by hand
- Email domain experts (biostatistician, regulatory specialist, patient advocate) and wait for asynchronous replies
- Integrate feedback from multiple reviewers into a single document, resolving contradictions manually
- Write a plain-language summary after the technical document is finalised, often misaligned with the final version
- Run the whole sequence again if the supervisor requests a scope change
- Spend significant time on document management: version control, naming conventions, cross-referencing

---

## 3. The Agentic Workflow

The same task, redesigned around specialised subagents:

- A coordinating agent receives the research question and breaks it into discrete subtasks, each assigned to a specialised subagent
- A literature subagent retrieves, filters, and summarises relevant studies, producing a structured evidence table with defined fields
- A methods critique subagent reads the evidence table and flags methodological heterogeneity, sample size concerns, and design gaps
- A compliance subagent checks the proposed study design against regulatory requirements for each relevant jurisdiction, producing a structured annotation
- A translation subagent converts the finalised technical summary into a plain-language version suitable for a lay audience, constrained by the approved technical content
- The coordinating agent assembles all subagent outputs into a unified draft, resolves naming and formatting inconsistencies, and presents a summary of open questions
- Each handoff between agents is explicit: the output of one agent becomes a defined input to the next, with a schema that prevents misalignment
- The researcher reviews and approves each stage before the workflow advances

---

## 4. Core Concept

A subagent is an AI instance with a bounded scope. Rather than asking a single AI to be simultaneously a literature reviewer, a biostatistician, a regulatory expert, and a science communicator, you decompose the task into roles that mirror how a real expert team operates. Each subagent receives a specific input, operates under a specific set of instructions (its system prompt), and produces a specific output. It does not need to know what the other subagents are doing. Its job is narrow and well-defined.

Workflow orchestration is the layer above the subagents. An orchestrating agent — sometimes called a coordinator or router — receives the top-level task and decides which subagents to invoke, in what order, with what inputs. It is responsible for sequencing, for passing outputs from one agent as inputs to the next, and for assembling the final result. The orchestrator does not itself perform the specialised work; it manages the flow of information between specialists. This mirrors the role of a senior researcher or project manager in a clinical trial team.

The handoff protocol is the contract between agents. When the literature subagent finishes its summary, it produces a structured output — a table, a JSON object, a formatted list — that the methods critique subagent can read without ambiguity. This structure is called an artifact contract. It defines exactly what fields are present, what format they take, and what a passing output looks like. Without a clear artifact contract, agents produce outputs that the next agent cannot reliably interpret, and errors compound silently across the workflow.

What makes this approach powerful for clinical research is that it separates the question of expertise from the question of integration. You can tune each subagent's instructions to reflect genuine domain knowledge — regulatory language for the compliance agent, epidemiological conventions for the methods agent — without forcing a single system to be fluent in all of them at once. The orchestrator's job is not to be the expert in everything; it is to know who should speak next and what they need to hear.

---

## 5. Clinical Example

Consider a research team investigating the use of tumour-treating fields (TTFields) as an adjunct to temozolomide in newly diagnosed glioblastoma. The team needs to produce a structured research protocol that includes a literature synthesis, a methods critique, a regulatory compliance summary for both FDA and EMA, and a patient information sheet.

Without orchestration, a single prompt asking an AI to produce all of this at once would yield a document that is superficially complete but internally inconsistent. The regulatory section might cite trial designs that the methods critique flags as underpowered. The patient information sheet might describe a treatment schedule that was revised in the methods section but not propagated forward.

With subagent orchestration, the workflow proceeds in stages. The literature subagent is given the PICO question (Population: newly diagnosed GBM; Intervention: TTFields plus TMZ; Comparator: TMZ alone; Outcome: overall survival at 24 months) and produces a structured evidence table with columns for study design, sample size, primary endpoint, and reported hazard ratios. This table is passed to the methods critique subagent, which reads it and produces an annotation identifying heterogeneity in tumour grading criteria across studies and a note that three of the seven included trials used different Karnofsky Performance Status cut-offs. This annotation is passed to the coordinating agent, which routes it back to the literature subagent with a revised inclusion criterion. Once the evidence table stabilises, the regulatory subagent reads the finalised study design and produces a jurisdiction-specific compliance checklist. Finally, the translation subagent receives the approved protocol summary and produces a patient information sheet that uses only the terminology and claims validated by the technical review.

The research team reviews each stage. The orchestrator surfaces a summary of decisions made and open questions requiring human judgment — for example, the choice between two conflicting statistical frameworks, which the team resolves before the workflow continues. The final document is coherent because each section was produced from a defined input by a defined agent, and the integration was managed explicitly rather than left to chance.

---

## 6. In-Class Activity

**Duration:** 15-20 minutes
**Format:** Pairs or groups of three

**Scenario:** You are designing an agentic workflow to support a systematic review of AI-assisted diagnosis in diabetic retinopathy screening. The review must produce: (1) a structured evidence synthesis, (2) a methodological quality assessment, (3) a brief regulatory and ethics annotation, and (4) a plain-language summary for a patient advocacy group.

**Step 1 (5 minutes):** As a group, identify the four subagents your workflow will need. For each subagent, write one sentence describing its role, one sentence describing its input, and one sentence describing its output. Use the table template below.

| Subagent Name | Role (one sentence) | Input | Output |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

**Step 2 (5 minutes):** Draw the orchestration flow on paper or a shared screen. Show which agent runs first, what it produces, which agent receives that output, and so on. Mark any points where a human decision is required before the workflow continues.

**Step 3 (5 minutes):** Identify one handoff in your diagram that is most likely to fail silently — that is, where the output of one agent might be misread or misused by the next agent without either agent flagging an error. Write two sentences describing what could go wrong and one sentence describing how you would define the artifact contract to prevent it.

**Discussion (3-5 minutes):** Each group shares their highest-risk handoff. As a class, identify common patterns across the different workflows. What kinds of information are most likely to be lost or distorted during agent handoffs in clinical research contexts?

---

## 7. Artifact Contract

Each agent in your workflow must produce a defined artifact. The following table describes the required outputs for the in-class activity and the criteria for a passing artifact.

| Artifact | Format | Required Fields | Passing Criteria |
|---|---|---|---|
| Orchestration diagram | Hand-drawn or digital diagram | All four subagents named; directional arrows showing data flow; at least one human decision point marked | Diagram is unambiguous: a classmate can trace the path of a single piece of information from input to final output without asking the author for clarification |
| Subagent specification table | Markdown table | Subagent name, role, input description, output description | Each cell contains a complete sentence; input and output fields are specific enough that a different person could write the agent's system prompt from the table alone |
| Handoff risk annotation | Two-to-three sentences of plain text | Identification of the at-risk handoff, description of the failure mode, proposed artifact contract element | The failure mode described is specific to clinical research (not a generic software failure); the proposed fix addresses the specific risk identified |
| Coordinating agent summary | Bullet list | Summary of open questions requiring human judgment; list of decisions made autonomously by the workflow | At least one open question is identified; decisions are distinguished from open questions |

---

## 8. Common Failure Modes

**1. The omniscient orchestrator.** A common mistake is to put too much work in the orchestrating agent — asking it not only to route tasks but also to perform the specialised analysis. When the orchestrator both manages the workflow and does the substantive work, it becomes a single point of failure, and the benefits of specialisation disappear. Keep the orchestrator's role narrow: sequencing, routing, and integration only.

**2. Underspecified artifact contracts.** If you ask a literature subagent to produce a summary without specifying the exact fields, format, and level of detail required, the methods critique subagent will receive something it cannot reliably parse. The most common result is that the second agent silently reinterprets the first agent's output, introducing errors that are not visible in the final document. Always define the output schema before you run the first agent.

**3. Missing human decision points.** Workflows that run end-to-end without human checkpoints are dangerous in clinical research contexts. Clinical judgment is not just a regulatory requirement — it is also a quality control mechanism. If the literature subagent misinterprets the inclusion criteria and the workflow proceeds without review, every subsequent agent operates on a flawed foundation. Build in explicit approval gates between stages, particularly at transitions between evidence synthesis and methods design.

**4. Scope drift between agents.** Each subagent should have a clearly bounded scope. If the methods critique subagent begins making regulatory judgments because no one told it not to, its output will overlap with and potentially contradict the compliance subagent's output. Write each agent's system prompt with an explicit statement of what falls outside its scope, not just what falls within it.

**5. Provenance loss.** When the coordinating agent assembles the final document, it is easy to lose track of which subagent produced which claim, and under what constraints. In clinical research, every statement should be traceable to its source. Design your workflow so that each subagent's output is preserved separately, and the final document includes a clear log of which sections were produced by which agent and from which inputs.

---

## 9. Responsible Use

Subagent orchestration introduces a specific governance challenge that does not arise in single-prompt workflows: accountability diffusion. When a single researcher writes a methods section, it is clear who is responsible for its contents. When four subagents contribute to the same document under the direction of an orchestrating agent, the chain of intellectual responsibility must be deliberately maintained. Each agent's output should be reviewed by a researcher with domain competence in that area — not just reviewed as part of the assembled whole. The fact that a workflow produced a coherent document does not mean that each component was correct. Coherence and correctness are not the same thing, and automated workflows can be coherent while being systematically wrong.

There is also a fairness and representation concern specific to clinical research. Subagents are typically trained on published literature, which over-represents certain patient populations, study designs, and geographic contexts. A literature subagent working on a glioblastoma review will draw heavily on trials conducted in North American and European academic centres. A compliance subagent trained primarily on FDA materials may produce inadequate annotations for researchers working in other regulatory environments. These are not reasons to avoid using subagent workflows; they are reasons to document the limitations of each subagent explicitly in your methods section, as you would document the limitations of any tool.

Finally, consider the question of scientific integrity in the context of authorship and contribution. Many journals and funding bodies are developing policies on AI contribution disclosure, and the landscape is changing rapidly. If a subagent workflow produces substantial portions of a methods section or evidence synthesis, this should be disclosed in accordance with the policies of your institution, your target journal, and your funding body. The standard of transparency that applies to human research assistants also applies to AI systems performing equivalent work. This is not a constraint on using these tools — it is the condition under which using them remains scientifically honest.

---

## 10. Further Learning

**Note to instructors:** The following are categories of literature and resources to locate before distributing this handout. Do not use fabricated citations. Search the databases listed and insert verified references before release.

- Search "multi-agent systems clinical decision support" in PubMed and IEEE Xplore for peer-reviewed work on agent coordination in healthcare AI
- Search "workflow automation systematic review" and "AI-assisted evidence synthesis" in PubMed and Cochrane Library for recent methodological work on automated literature review pipelines
- Search "large language model orchestration" and "LLM agent frameworks" in arXiv (cs.AI and cs.CL sections) for technical work on orchestration architectures; verify any cited papers exist and check publication dates
- Search "AI contribution disclosure research integrity" in Google Scholar and COPE (Committee on Publication Ethics) guidelines for current policy on disclosing AI involvement in research manuscripts
- Search "artifact schema structured outputs LLM" in Anthropic documentation and associated technical blogs for current best practice on constraining agent outputs
- Anthropic documentation: review the current Claude API documentation and the Claude Code 101 course materials for accurate descriptions of subagent and orchestration capabilities; reference by title only, do not quote
- Search "patient information sheet plain language guidelines" in health literacy literature (e.g., NHS England, NIH plain language resources) for standards the translation subagent should be evaluated against
- Check PRISMA 2020 guidelines and Cochrane Handbook for Systematic Reviews for the methodological standards against which literature subagent outputs should be evaluated
- Search "glioblastoma tumour treating fields systematic review" in PubMed to verify the clinical example in Section 5 reflects the current evidence base; update the example if the literature has moved substantially
- This skill aligns with concepts covered in Claude Code 101 and the Anthropic documentation on multi-agent systems. Review these resources for accurate framing of orchestrator-subagent relationships before finalising the Core Concept section.
