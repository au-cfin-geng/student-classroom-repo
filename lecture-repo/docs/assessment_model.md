# Assessment Model — Agentic Clinical Research Studio

This document explains how submissions are evaluated in this course.

---

## What is and is not graded

**This course is NOT graded on:**
- Model performance (Dice score, BLEU, accuracy, etc.)
- Code complexity or engineering sophistication
- The number of labs completed
- Whether Claude produced an impressive-looking output

**This course IS graded on:**
- Workflow clarity: do your prompts specify scope, output format, and constraints?
- Artifact quality: does the committed file constitute a reviewable research record?
- Human judgment: did you evaluate Claude's output, not just accept it?
- Responsible use: did you acknowledge uncertainty, limitations, and data governance?
- Honest reporting: if something failed, is that failure documented?

A capstone that honestly documents a failed experiment scores higher than one that reports improvement without explanation.

---

## Two-stage assessment

### Stage 1 — Automated structural check (GitHub Actions)

Runs on every push that touches `submissions/`, `reports/`, `outputs/`, `skills/`, or `workflows/`.

Checks for each submitted lab:
1. `submissions/<lab>/submission.md` exists
2. All required section headings are present
3. `submissions/<lab>/status.json` is parseable
4. `submissions/<lab>/evidence_manifest.json` is parseable
5. If `ready_for_review: true`, all listed evidence files exist on disk

**Grader output per lab:**

| Grade | Meaning |
|-------|---------|
| Not submitted | `submissions/<lab>/` directory does not exist |
| Started | Directory exists but submission.md is absent |
| In progress | All structure present; `ready_for_review` is false |
| Pass | All structure present; `ready_for_review` is true; evidence confirmed |
| Incomplete | Claims ready but evidence files are missing on disk |

The automated check is pass/fail on structure only. It cannot assess the quality of your reasoning, the honesty of your reflection, or the validity of your conclusions.

### Stage 2 — Instructor review

The instructor reads:
- `submissions/<lab>/submission.md` — your written reflection on each section
- The committed artifacts in `reports/`, `outputs/`, `skills/`, `workflows/`
- The commit history — frequency, message quality, revision patterns

**Instructor grades:**

| Grade | Meaning |
|-------|---------|
| Pass | Structure complete; reflection demonstrates genuine engagement with the lab concept |
| Strong Pass | As above, plus clear evidence of critical judgment (verified claims, documented failures, honest limitations) |
| Showcase | As above, plus evidence of independent thinking — extended the lab, transferred to own research, identified a non-obvious failure mode |
| Needs revision | Structural issues OR reflection is superficial / uses placeholder text |

---

## Grade language

This course uses **Pass / Strong Pass / Showcase / Needs revision** — not percentages.

The goal is not to rank students against each other. It is to establish whether each student has demonstrated the four capabilities the course is designed to teach:

1. Writing prompts that function as explicit research protocols
2. Producing artifacts that constitute a reviewable record
3. Exercising human judgment on AI outputs
4. Communicating responsibly about uncertainty and limitations

---

## What happens to your submission

1. You run `python scripts/package_lab.py --lab <LAB>` — creates the submission package
2. You fill in `submissions/<lab>/submission.md` with genuine reflection
3. You run `python scripts/grade_submissions.py` to confirm structural pass
4. You commit and push — GitHub Actions checks the structure automatically
5. Instructor reviews the commit and reads the submission

The instructor will not read chat transcripts or session history. The only evidence that counts is what is committed to git.

---

## Required headings for submission.md

### Core labs (L0–L5)

```
# Lx Submission
## Clinical problem
## Agentic / Claude concept
## What was produced
## Human verification
## Limitations
## Ready for review
```

### Capstone

```
# Capstone Submission
## Research problem
## Agentic workflow used
## Evidence and artifacts
## Human verification
## Limitations
## Showcase summary
## Ready for review
```

---

## Frequently asked questions

**"Does my grade depend on whether Claude performed well?"**
No. If Claude produced a poor output, documenting that clearly and explaining why is more valuable than a polished output with no reflection.

**"What if I could not complete all required artifacts?"**
Document what you attempted, what failed, and why. An honest failure report scores better than placeholder text claiming success.

**"Do extensions count toward the grade?"**
Extension labs (L6–L8) are optional. Completing them demonstrates depth of engagement and may raise a Pass to Strong Pass or Showcase, but are not required for a Pass.

**"Can I revise a submission after committing?"**
Yes. Update `submissions/<lab>/submission.md`, re-run `package_lab.py`, and commit the revision. The commit history shows your revision process, which is itself evidence of engagement.
