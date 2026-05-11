# .coursekit — Instructor Reference

This hidden directory contains course infrastructure that students do not need
to interact with directly.

## What is in here

Nothing yet — this directory serves as the designated location for instructor-only
materials that may be added later, such as:

- Reference script implementations (for instructors who want to compare against student output)
- Grading rubrics and assessment notes  
- Session archive tooling
- Course calibration data

## What students see

Students work in:
- `prompts/` — the natural-language prompts that drive the lab
- `scripts/` — their working Python files (created or modified via Claude Code)
- `reports/` — written outputs produced during the lab
- `outputs/` — figures, metrics, and status files produced by scripts
- `CLAUDE.md` — the lab contract for Claude Code sessions

## Design intent

The lab is designed to feel **prompt-first**: students use natural-language prompts
in VS Code + Claude Code to direct the research workflow. The scripts in `scripts/`
are their workspace — Claude creates, modifies, and runs them based on the prompts.

The grading system (in `tests/`) checks that required artifacts exist at required
paths. It does not inspect how the scripts were written or who wrote them.

## For instructors

If you need to replace a student's broken script with a reference implementation,
place reference scripts here and copy them as needed. Do not commit reference
scripts to the visible `scripts/` directory — that would defeat the prompt-first pedagogy.
