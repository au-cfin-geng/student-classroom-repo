# M0 — Project Memory

## Module Identity

Every clinical AI project begins in the same state: scattered dependencies, undocumented assumptions, and no shared definition of "ready." Collaborators inherit codebases they did not write. Environments diverge silently. Downstream failures get misdiagnosed as modeling errors when they are, in fact, setup failures. This module addresses that problem at the source.

The Claude capability this module introduces is **project memory**: the practice of giving Claude a structured, persistent context document — `CLAUDE.md` — that defines the project, its constraints, its output contracts, and the roles of human and AI before any work begins. Paired with this is the "inspect before acting" pattern: Claude reads the project context first, reports what it finds, and waits for human acknowledgment before touching any files. The result is a working environment that is verifiable, repeatable, and honest about its own state.

---

## Before / After

**Without Claude:** A researcher opens a new repository, scans the README, tries `python scripts/run_train.py`, and gets an import error three minutes in. They diagnose package versions by trial and error. They are not sure whether `outputs/` should already exist. They run something, it writes to the wrong path, and a downstream grading check fails for reasons they cannot trace. Forty minutes of setup time produce no science.

**With Claude (this module's pattern):** The researcher opens the repo and runs a single, well-specified prompt. Claude reads `CLAUDE.md` first — learning the project purpose, its output contracts, and the naming rules before touching anything. Claude checks the environment systematically, creates missing directories, writes a structured environment report to `reports/env_check.md`, and writes a machine-readable status file to `outputs/status/stage_00_bootstrap.json`. The researcher inspects both files manually, confirms the status is `"ok"`, and knows the environment is ready. The setup took five minutes. The output is independently verifiable.

---

## The Prompt Principle: Define the Output Before Asking for the Work

The specific pattern this module teaches is **output specification in the prompt itself**. When you name the exact file path, the required JSON keys, and the minimum content of every output artifact, you are not micromanaging — you are writing a specification. The prompt becomes a contract, not a request.

**Weak prompt (before):**

> Set up this environment and make sure everything is working.

This prompt is ambiguous on every dimension that matters: what "working" means, where results go, what format they take, and how the researcher verifies success. Claude may produce a helpful summary in the terminal that vanishes the moment the session closes. Or it may write files to unexpected locations. Or it may silently skip a failing package check because the prompt did not ask it to be explicit.

**Specified prompt (after):**

> Check that numpy, matplotlib, pathlib, and json are importable and print their versions.
>
> Write a summary to `reports/env_check.md` that includes: Python version, platform, package status, and any concerns.
>
> Write a status file to `outputs/status/stage_00_bootstrap.json` with this structure:
> `{"status": "ok", "python_version": "X.Y.Z", "platform": "..."}`
> If something failed, use `"status": "error"` and include the problem.
>
> Show me the content of both files and confirm they were written successfully.

The second prompt produces an output that can be opened, inspected, version-controlled, and tested by an automated check. The first prompt produces a conversation.

---

## The Clinical Scenario in This Course

In this module, you are not yet working with imaging data. You are establishing the conditions under which imaging work can begin without ambiguity.

The lab's clinical problem is brain tumour segmentation from FLAIR MRI. That work depends on a functioning Python environment, correctly structured output directories, and a baseline verification that the toolchain is intact. Before any DICOM slice is loaded, before any Dice coefficient is computed, the lab must demonstrate that it is ready.

Your task in Mission 0 is to execute `stage_00_bootstrap.md` — the project's first prompt. You will:

1. Read `CLAUDE.md` and confirm you understand the project structure and your role versus Claude's.
2. Run the bootstrap prompt, which asks Claude to check the environment, create output directories, and write the two required artifacts.
3. Inspect both output files manually to confirm they reflect your actual machine.
4. Run `make preflight` to verify the structural checks pass.

This is the first time you will experience the core student loop: **dashboard → prompt → VS Code + Claude Code → artifact → dashboard feedback**. The loop is not a convention — it is the epistemological structure of the course. Prompts are experimental instruments. Artifacts are the evidence. The dashboard reflects what the evidence shows.

---

## Assignment

**Artifact to produce:**

| File | Required content |
|------|-----------------|
| `reports/env_check.md` | Python version, platform, package availability, any concerns |
| `outputs/status/stage_00_bootstrap.json` | `{"status": "ok", "python_version": "...", "platform": "..."}` |

**Make target to run:**

```
make preflight
```

This target runs `scripts/bootstrap.py` and then executes `tests/test_preflight.py` and `tests/test_scripts_exist.py`. All checks must pass.

**What the artifacts must contain:**

- `env_check.md` must reflect your actual machine — real Python version, real platform, real package status. It must not contain placeholder text or fabricated values.
- `stage_00_bootstrap.json` must have `"status": "ok"`. If it contains `"status": "error"`, the mission is incomplete. Diagnose the reported problem and resolve it before proceeding.
- Both files must be at the exact paths specified. The grading tests check these locations. A correctly written file at the wrong path is treated as missing.

---

## Reflection Questions

Answer these in your own words after completing the module. Write your responses in a plain text or Markdown file; you do not need to submit them for grading.

1. **What does `"status": "ok"` guarantee, and what does it not guarantee?** The status file reports that the bootstrap script ran without error. What specific claims does it make about your environment? What would it fail to detect?

2. **Why does naming the exact JSON keys (`python_version`, `platform`) matter?** Consider what happens to an automated test that checks for these keys if Claude were instead allowed to choose its own field names. What breaks, and why?

3. **CLAUDE.md is described as "project memory." What would a comparable document look like for your own current research project?** What context would Claude need before acting on your codebase that it cannot infer from the files alone?

---

## Transfer to Your Own Research

The output specification pattern is not specific to this lab. It applies to any situation where you need a reliable, verifiable artifact rather than a helpful response.

In your own research, consider applying this pattern whenever:

- You are setting up a new analysis environment (write a machine-readable readiness report before running any experiments).
- You are handing off work to a collaborator (specify exactly what files they will receive and what keys or fields they must contain).
- You are running a preprocessing step whose outputs feed downstream analysis (name the output paths and required structure in the prompt so the outputs are independently testable).
- You are writing a script that will be rerun across multiple patients or datasets (establish a status contract — every run either succeeds with verified outputs or fails explicitly with a diagnosable error).

The deeper principle: any computational step whose output you cannot inspect and verify is a source of silent error. Specifying outputs in the prompt forces both Claude and you to confront that question before the work begins, not after.

---

## Success Criteria

Work in this module is complete when:

- `make preflight` exits with no failures.
- `outputs/status/stage_00_bootstrap.json` exists and contains `"status": "ok"` with real (non-placeholder) values for `python_version` and `platform`.
- `reports/env_check.md` exists and accurately describes the actual environment — the Python version, platform, and package status must match what your machine reports, not what was expected or hoped.
- You have manually opened both files and confirmed the values are genuine.
- You can explain, in one sentence each, what `CLAUDE.md` is for and why the status file uses a machine-readable format rather than a prose summary.

Work is not complete if: the status file contains `"status": "error"` and you proceed anyway; either file is missing; the environment report contains fabricated values; or `make preflight` reports test failures that you have not investigated.
