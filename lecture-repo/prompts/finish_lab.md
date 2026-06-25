# Finish Lab — Claude-Driven Submission Prompt

Paste this entire prompt into Claude Code after completing any lab.
Claude will package the submission, draft submission.md, run checks, and ask before committing.

---

## Step 1 — Identify the lab

Which lab did you just finish?

If the student did not say, ask: "Which lab are you finishing? (Lab00, Lab01, Lab02, Lab03, Lab04, Lab05, or Capstone)"

Store the answer as LAB_ID (e.g., Lab03).

---

## Step 2 — Confirm repo root

Confirm you are working from the repository root.
You should see: `START_HERE.md`, `CLAUDE.md`, `Makefile`, `Lab00/`, `Lab01/`, `lecture-repo/`

If you are not in the repo root, stop and explain. Do not proceed.

---

## Step 3 — Inspect the work folder

List everything in `{LAB_ID}/work/`:

```bash
ls -la {LAB_ID}/work/
```

Report each file found. Note which required files are present and which are missing:

| Lab    | Required files |
|--------|---------------|
| Lab00  | `L0_orientation.md`, `status.json` |
| Lab01  | `L1_prompt_contract.md`, `status.json` |
| Lab02  | `L2_multi_stakeholder_review.md`, `status.json` |
| Lab03  | `L3_literature_search_skill.md`, `L3_literature_search.md`, `status.json` |
| Lab04  | `L4_tool_mcp_workflow.md`, `status.json` |
| Lab05  | `L5_subagent_workflow.md`, `L5_subagent_workflow_report.md`, `status.json` |
| Capstone | `capstone_report.md`, `showcase.md`, `status.json` |

If required files are missing, tell the student exactly which are missing and what to create before packaging.
Do not continue to packaging if the main report file is missing.

---

## Step 4 — Read the evidence

Read the main evidence files in `{LAB_ID}/work/`.
Understand what the student actually did. You will use this to draft submission.md.

Read at minimum:
- The primary `.md` report file (e.g., `L3_literature_search.md`)
- `status.json` if it exists
- Any additional `.md` files found

Do not invent or extrapolate. You will write only what the evidence shows.

---

## Step 5 — Package the submission

Run the packaging script:

```bash
make package LAB={LAB_ID}
```

This creates:
- `{LAB_ID}Submission/evidence_manifest.json`
- `{LAB_ID}Submission/status.json`
- `{LAB_ID}Submission/submission.md` (scaffold — only if it does not exist)

Report what was created or found. If the packaging script fails, show the error and stop.

---

## Step 6 — Draft submission.md

Read `{LAB_ID}Submission/submission.md`.

Then write a new version of `{LAB_ID}Submission/submission.md` based entirely on what you read in Step 4.

Rules for writing submission.md:
- **Do not invent.** Only describe what actually exists in `{LAB_ID}/work/`.
- **Be specific.** Name the files, describe their content, quote key outputs.
- **Be honest.** If the lab did not complete fully, say so in Limitations.
- **Do not repeat the handout.** Describe what was produced, not what the lab asked for.
- **Keep it concise.** Each section: 3–8 sentences maximum.

Section guidance (for standard labs):

### ## Clinical problem
What specific clinical research question was the student addressing in this lab?
Derive this from the report content, not the handout description.

### ## Agentic / Claude concept
What prompt pattern did the student apply? What did Claude do?
Describe the actual interaction, not the generic concept.

### ## What was produced
List each artifact in `{LAB_ID}/work/` with one-sentence description of its content.
Include file sizes or word counts if notable.

### ## Human verification
What did the student verify, correct, or judge in Claude's output?
If the evidence shows Claude made errors that were caught, say so.
If no verification happened, note that honestly.

### ## Limitations
What failed, was incomplete, or is uncertain?
If evidence files are partial, say so.
If `status.json` shows `"status": "ok"` but the report has gaps, flag them.

### ## Ready for review
Update the checklist based on actual state:
- Check `[x]` only if the artifact exists and is non-trivial
- Leave `[ ]` for items that are missing or are stubs

For Capstone, fill all sections including `## Showcase summary`.

After writing submission.md, show the student the full content.
Ask: "Does this accurately reflect your lab work? Reply YES to proceed, or tell me what to change."

Wait for the student's confirmation before continuing. Apply any requested edits.

---

## Step 7 — Update status.json

If all required evidence files exist and the student confirmed the submission reflects real work, update `{LAB_ID}Submission/status.json` to include:

```json
{
  "ready_for_review": true
}
```

Use `make package LAB={LAB_ID}` again (it will re-read evidence and update status.json), or edit status.json directly if the evidence changed.

If required files are missing, set `"ready_for_review": false` and say so clearly.

---

## Step 8 — Run progress check

```bash
make progress
```

Read the output and report to the student:
- Which labs are complete
- Which are in progress or not started
- What the grading report says about this lab

---

## Step 9 — Commit check

Show the student a summary:

> **{LAB_ID} ready to commit.**
> - Evidence in `{LAB_ID}/work/`: [list files]
> - `{LAB_ID}Submission/submission.md`: [complete / needs more work]
> - `{LAB_ID}Submission/status.json`: ready_for_review = [true/false]
> - Progress check: [pass/fail details]

Then run:

```bash
git status
```

Show the student exactly which files will be committed.

Ask: "Commit and push? (YES / NO)"

**Do NOT commit unless the student says YES.**

---

## Step 10 — Commit

If the student approves, run:

```bash
git add {LAB_ID}/work/
git add {LAB_ID}Submission/submission.md
git add {LAB_ID}Submission/evidence_manifest.json
git add {LAB_ID}Submission/status.json
git commit -m "Complete {LAB_ID} submission package"
```

Show the git commit output. Do not push unless the student explicitly asks to push.

---

## Step 11 — Final report

When done:

> **Lab packaged.**
> - Lab: {LAB_ID}
> - Evidence found: [list]
> - Missing: [list or "none"]
> - submission.md: written and reviewed
> - ready_for_review: [true/false]
> - Committed: YES / NO
>
> **Next step:** [the next lab in sequence, or Capstone if all done]

If anything failed, explain exactly what is missing and how to fix it before the student submits.

---

## Honesty requirements

- Do not mark ready_for_review=true if required artifacts are missing
- Do not write submission.md sections from imagination — only from evidence you read
- If the lab work is incomplete, say so in Limitations and set ready_for_review=false
- If the grader reports structural failures, explain them rather than suppressing them
- Never commit without student approval
