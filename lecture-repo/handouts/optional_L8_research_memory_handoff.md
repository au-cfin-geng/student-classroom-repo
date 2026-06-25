# L8 (Extension): Research Memory & Handoff

**Course:** Agentic Clinical Research Studio
**Session Type:** Optional Extension Lab
**Estimated Time:** 90 minutes (30 min reading + 15-20 min activity + discussion)

---

## 1. Opening Story

Maya had been working on her neuro-oncology PhD for three years when her supervisor told her the good news: she would be presenting at an international conference, and a collaborating lab in Amsterdam wanted to integrate her tumour segmentation pipeline into their multi-site trial. The bad news arrived immediately after. The postdoc who had written the preprocessing scripts had graduated six months ago. The lab's previous PhD student, who had selected the specific FLAIR normalisation approach, had left a year before that. And the senior research assistant who had negotiated the imaging protocol with the MRI physicists had moved to industry.

Maya sat in front of the codebase. She knew it worked. The results in her thesis chapters proved it. But she could not answer the Amsterdam team's first question: why was the skull-stripping threshold set to 0.4 rather than the default 0.5? There was a comment in the code that said "# adjusted after MRI physics meeting" but no record of what was discussed or decided. She spent four days emailing former colleagues, digging through Slack archives, and reverse-engineering parameter choices from intermediate output files. She recovered about 70% of the reasoning. The rest she had to reconstruct by re-running experiments that had already been done two years earlier.

This is not an unusual story. It is the default experience in academic clinical research. Projects span years. Team members turn over. Meetings produce decisions that live only in the memories of the people in the room. When those people leave, the institutional knowledge evaporates. The result is wasted time, unreproducible work, and a quiet erosion of scientific confidence that rarely makes it into publications but shapes every day of doctoral research.

---

## 2. The Old Workflow

Without structured research memory, a typical PhD project manages context through informal and fragmented channels:

- Decisions are recorded (if at all) in meeting minutes that are never systematically indexed or linked to the code they affect
- Rationale for parameter choices lives in email threads, Slack messages, or the researcher's personal notebook
- Onboarding a new team member means scheduling several hours of knowledge transfer meetings with people who may no longer be available
- Code comments describe what the code does, not why a particular approach was chosen over alternatives
- When a pipeline breaks, debugging requires reconstructing the original intent from outputs rather than reading the original reasoning
- When a project resumes after a gap (summer break, parental leave, grant writing period), the researcher spends days "re-loading" their own context before they can be productive again
- Final thesis chapters may accurately describe the method but contain no record of the dead ends, the rejected alternatives, or the reasoning that led to each design choice

---

## 3. The Agentic Workflow

With structured research memory and agentic handoff documents, the same project runs differently:

- CLAUDE.md in the project root contains a living summary of the project's current state, active hypotheses, known limitations, and key decisions
- Each major decision is logged in a `decisions/` folder using a lightweight template: the question being decided, the options considered, the reasoning, and the outcome
- When a new Claude session begins, the assistant reads CLAUDE.md first and can immediately operate with full project context
- When a new team member joins, they open CLAUDE.md and can ask the AI to explain any section, trace a decision back to its origin, or identify which code files implement a given design choice
- Before any significant code change, the researcher asks Claude to draft a decision log entry capturing the intended change, the alternatives considered, and the expected effect on downstream outputs
- At the end of a working session, Claude is asked to update CLAUDE.md with a brief session summary, flagging any open questions
- When the Amsterdam collaboration team arrives, the researcher shares the repo and the handoff document; onboarding takes two hours instead of four days

---

## 4. Core Concept

CLAUDE.md is a plain text file that lives at the root of your project. In normal software development, it tells an AI assistant how the codebase works. In clinical research, it can do something far more valuable: it becomes the external memory of the project itself. It is not a README for users of your software. It is a briefing document for any future collaborator, human or AI, who needs to pick up exactly where you left off.

The key distinction in good research memory is the difference between what and why. Most code, most methods sections, and most thesis chapters explain what was done. They describe the pipeline steps, the parameter values, the statistical tests. They rarely explain why those choices were made rather than the obvious alternatives. A decision log closes this gap. It is a brief, structured record that captures the question being decided, the options that were genuinely on the table, the reasoning that tipped the balance, and the date and context in which the decision was made. Even a single paragraph per major decision transforms a codebase from an opaque artifact into an auditable research record.

Structured handoff documents extend this idea to project transitions. A handoff document is written not for the researcher who is leaving but for the person who is arriving, or for the future version of yourself returning after a six-month gap. It describes the current state of the project in terms of what is working, what is broken, what is uncertain, and what the next three highest-priority tasks are. It links to the decision logs for any recent choices that might need revisiting. It names the open questions that have not yet been answered. A good handoff document should make it possible for a competent researcher unfamiliar with the project to make a useful contribution within one working day.

When Claude is involved in daily research work, these documents do not have to be written from scratch at the end of a project phase. They can be maintained incrementally. At the end of each session, you can ask Claude to draft a brief update to CLAUDE.md that captures what changed, what was decided, and what remains open. Over weeks and months, this produces a rich, searchable project memory that no single team member's departure can destroy. The cost of maintenance is low. The cost of not maintaining it, as Maya discovered, is measured in working weeks.

---

## 5. Clinical Example

Consider a research group running a longitudinal study of treatment response in glioblastoma patients. The pipeline takes pre- and post-treatment MRI scans, segments the tumour and surrounding oedema, registers the follow-up scans to the baseline, and generates volumetric change metrics that are used to classify patients as responders or non-responders by RANO criteria.

Over three years the pipeline evolves. The original registration was rigid; after a discussion with the neuroradiology team it was switched to deformable registration to account for post-surgical cavity changes. The threshold for classifying oedema was adjusted after the team noticed systematic underestimation in patients who had received bevacizumab, which suppresses contrast enhancement and changes the appearance of oedema on T2-FLAIR. The statistical model was changed from a mixed-effects linear model to a marginal model after consulting with a biostatistician about the non-independence of sequential scans.

Without decision logs, each of these changes appears in the git history as a commit message like "update registration parameters" or "fix oedema threshold." The reasoning is gone. When a new PhD student joins to extend the pipeline to a paediatric cohort, they inherit a set of choices tuned for adult glioblastoma patients with no record of which choices are principled and which are pragmatic workarounds. They will almost certainly re-introduce errors that were already corrected, and they will spend months discovering the same failure modes that the original team already worked through.

With decision logs, the new student opens the `decisions/` folder and finds twenty entries, each with a date, a clinical context, the alternatives that were considered, and the reasoning behind the final choice. The entry on registration reads: "Switched to deformable registration on 2023-11-14 after neurorad team review showed rigid registration introduced systematic volume overestimation in patients with post-surgical cavity collapse (see analysis in `/reports/registration_comparison_2023-11.ipynb`). Deformable adds 40 min per patient to pipeline runtime; acceptable given cohort size." The new student now knows exactly why the current approach was chosen, can find the supporting analysis, and can evaluate whether the same reasoning applies to paediatric cases.

---

## 6. In-Class Activity

**Title:** Build a CLAUDE.md for a Real or Simulated Project

**Time:** 15-20 minutes

**Setup:** Work in pairs. One person takes the role of a researcher who has been working on a project for two years and is about to go on maternity leave for six months. The other takes the role of the PhD student who will cover the project in their absence.

**Instructions:**

1. (5 minutes) The "departing researcher" opens their laptop and looks at any real project folder they have available, or uses the course sample data repository. They spend five minutes writing a bullet list of everything they know about the project that is not written down anywhere: why certain files are named the way they are, which scripts are fragile and why, which parameter values were tuned by hand, which approaches were tried and abandoned.

2. (5 minutes) Both students together use Claude to draft a CLAUDE.md from that bullet list. Use a prompt like: "I am about to hand this project to a colleague. Here are the key things I know that are not in the code: [paste bullet list]. Please draft a CLAUDE.md that captures this context, including a section on key decisions and a section on known fragile points."

3. (5 minutes) The "incoming researcher" reads only the generated CLAUDE.md, not the original bullet list. They then ask Claude three questions about the project using only the CLAUDE.md as context. The pair evaluates: did the handoff document contain enough information to answer the questions? What is missing?

4. (2-3 minutes) Discuss with the group: what categories of information were hardest to capture? What would you add to the CLAUDE.md template for a clinical research project specifically?

**Reflection prompt:** How much institutional knowledge currently exists only in your own head about your current project? What would happen to your project if you had an unexpected two-month absence starting tomorrow?

---

## 7. Artifact Contract

The following files constitute a passing artifact for this lab:

| File | Format | Passing Criteria |
|---|---|---|
| `CLAUDE.md` | Markdown | Contains at minimum: project summary (2-3 sentences), current state section, key decisions section with at least two entries, known limitations section, and next steps section. Each decision entry includes the question, the alternatives considered, and the reasoning. |
| `decisions/decision_001.md` | Markdown | A decision log entry for a real or realistic choice in your pipeline. Includes: date, decision question, options considered (minimum two), rationale, outcome, and a link to any supporting analysis or reference. |
| `handoff_document.md` | Markdown | A document written for a hypothetical incoming researcher. Covers: project overview, what is currently working, what is currently broken or uncertain, the three highest-priority next tasks, and pointers to the most important decision logs. Maximum 600 words. |
| Session update (appended to CLAUDE.md) | Markdown section | A brief section added at the end of CLAUDE.md titled "Session Notes — [date]" summarising what was done in this lab session, any decisions made during the activity, and any open questions. Must be written or reviewed by Claude in the session, not retroactively composed. |

A submission that has all four files but whose CLAUDE.md contains only generic placeholder text, or whose decision logs record only what was done without explaining why, does not pass. The standard is whether an unfamiliar researcher could use these documents to resume the project productively.

---

## 8. Common Failure Modes

**Failure mode 1: The CLAUDE.md becomes a README.**
Many researchers write a CLAUDE.md that describes how to install and run the pipeline, as if it were documentation for external users. This is useful but misses the point. The CLAUDE.md should capture internal knowledge, the reasoning and history that would otherwise be lost, not public-facing instructions. If you find yourself writing installation steps, stop and ask: what would I tell a new lab member in their first one-on-one meeting that is not in any written document?

**Failure mode 2: Decision logs record what, not why.**
A decision log that says "switched from random forest to gradient boosting" is almost useless. The same log with "switched from random forest to gradient boosting after observing systematic underperformance on class-imbalanced folds in the internal validation set; gradient boosting with scale_pos_weight tuned to class ratio improved minority class recall from 0.41 to 0.68" is the foundation of reproducible science. If you cannot explain why a decision was made, that is a signal that the decision needs more documentation, not less.

**Failure mode 3: The documents are written once and never updated.**
A CLAUDE.md that reflects the state of the project six months ago is nearly as misleading as no CLAUDE.md at all. Treat it as a living document. A practical approach: at the end of every working session where a significant change was made, ask Claude to draft a three-sentence update. It takes less than two minutes and compounds over time into a complete project history.

**Failure mode 4: The handoff document assumes too much prior knowledge.**
When writing for an incoming researcher, it is tempting to write for yourself: someone who already knows the clinical context, the data quirks, the relevant literature. Force yourself to write for a competent researcher from a different clinical subdomain. If they would need to look up a term you use, define it. If a decision makes sense only in light of a specific dataset property, describe that property.

**Failure mode 5: Treating this as an administrative burden rather than a research practice.**
The researchers who benefit most from structured memory are the ones who integrate it into the rhythm of research, not the ones who try to create it in a retrospective sprint before a handoff deadline. A session update written at the end of a three-hour coding session takes five minutes. Reconstructing three years of reasoning from git commits and memory takes weeks. The asymmetry is extreme.

---

## 9. Responsible Use

Structured research memory raises a question that is easy to overlook: what should and should not be recorded in a machine-readable document that may be read by AI systems, future collaborators, or, in regulatory contexts, auditors? In clinical research, this question has real consequences. Decision logs may contain references to patient cohort characteristics, preliminary results that have not been disclosed, or assessments of data quality problems that could be misinterpreted out of context. Before recording information in CLAUDE.md or decision logs, consider who might legitimately access this repository and whether the level of detail is appropriate for that audience. Where sensitive information is genuinely necessary for project continuity, consider whether it belongs in a version-controlled file or in a separate, access-controlled record.

The use of AI to help draft decision logs and handoff documents introduces a different responsibility. Claude can summarise and structure information you provide, but it cannot verify the accuracy of the reasoning you ask it to document. If you ask Claude to draft a decision log based on your verbal description of a meeting, and your memory of that meeting is incomplete or inaccurate, the document will faithfully preserve an inaccurate record. The scientific responsibility for accuracy lies with you. Treat AI-generated documentation drafts as a starting point to be reviewed and corrected, not as an authoritative record. Sign-off on any decision log should be explicit, either by committing the file to version control under your own credentials or by adding a notation confirming that you have reviewed and verified the content.

Finally, consider the long-term governance implications of comprehensive research memory for clinical projects. Well-maintained decision logs may, in principle, be discoverable in regulatory submissions, ethics reviews, or legal proceedings related to clinical trial data. This is largely a positive development: it supports transparency and accountability. But it means that decision logs should be written to the same standard of accuracy and honesty that you would apply to any formal scientific record. Speculative entries, frustrated comments about data quality, or premature conclusions recorded as if they were established findings can create problems that extend well beyond the immediate research context.

---

## 10. Further Learning

The following are categories of literature and resources to search before finalising this handout. No paper titles, author names, or DOIs have been fabricated here. All citations should be verified independently before the course is delivered.

**Literature to search:**
- Search "research data management longitudinal clinical studies" in PubMed and Google Scholar for evidence on context loss and reproducibility problems in multi-year clinical research projects
- Search "laboratory notebook practices clinical research reproducibility" for established standards in research documentation that predate AI tools
- Search "knowledge management academic research teams" in higher education and organisational behaviour literature for frameworks on institutional knowledge loss when team members leave
- Search "FAIR data principles clinical AI" for guidance on findability and reusability standards that structured memory practices should align with
- Search "prompt engineering scientific workflow" and "AI-assisted research documentation" in arXiv and relevant informatics journals for emerging practices in AI-assisted research memory

**Course and tool references:**
- This lab builds directly on concepts introduced in Claude Code 101, particularly the use of CLAUDE.md as a context-setting document for AI-assisted workflows
- Anthropic's published documentation on context windows, session state, and how Claude reads project files is directly relevant and should be referenced from official Anthropic documentation at the time of course delivery
- The CLAUDE.md pattern is described in Anthropic's Claude Code documentation; instructors should link to the current version of that documentation rather than quoting it, as it is updated regularly

**Standards and frameworks to reference (verify current versions):**
- EQUATOR Network reporting guidelines (CONSORT, TRIPOD, STARD) as examples of structured documentation practices already expected in clinical research, which decision logs can complement
- Good Clinical Practice (GCP) guidelines for documentation standards in clinical trial contexts
- Any relevant institutional data governance policies at the institutions where this course is delivered, which may impose specific requirements on what can be recorded in version-controlled repositories

**Course materials note:**
Instructors should confirm that no section of this handout reproduces language from Anthropic's proprietary course materials. The concepts described here are original syntheses applied to clinical research contexts.
