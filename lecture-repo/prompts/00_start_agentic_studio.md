# Agentic Clinical Research Studio — Launch Prompt

Paste this entire prompt into Claude Code to start the course.

---

## Step 1 — Confirm repository root

First confirm you are working from the repository root.

You should see: `START_HERE.md`, `CLAUDE.md`, `Makefile`, `Lab00/`, `Lab01/`, `lecture-repo/`

If you are not in the repo root, stop and tell me. Do not proceed until you are in the correct directory.

---

## Step 2 — Read project context

Read `CLAUDE.md` and `START_HERE.md`. Confirm you understand:
- What course this is and what the student role is
- The agentic research loop: prompt → artifact → commit
- The lab structure: Lab00–Lab05 core, Capstone, Extension labs

---

## Step 3 — Prepare the workspace

Check the following:

**Python environment:**
- Run `python3 --version` and report the version
- Run `pip install -r lecture-repo/requirements.txt` (or confirm dependencies are already installed)
- If there are installation errors, report them clearly

**Lab working folders:**
- Confirm these exist (they should already be present in the repo):
  - `Lab00/work/`, `Lab01/work/`, `Lab02/work/`, `Lab03/work/`
  - `Lab04/work/`, `Lab05/work/`, `Capstone/work/`
- If any are missing, say so — do not create them silently

**Structural checks:**
- Run `make preflight`
- If make is not available, run: `python lecture-repo/scripts/bootstrap.py`
- Report any failures

---

## Step 4 — Start the dashboard

Start the course dashboard with:
```
make dashboard
```

Or directly:
```
streamlit run lecture-repo/app/streamlit_app.py
```

The dashboard should open at http://localhost:8501

If streamlit is not installed, install it: `pip install streamlit`

After starting the dashboard, confirm it is running.

---

## Step 5 — Create the Lab00 orientation artifact

Write `Lab00/work/L0_orientation.md` with:
- The date and course name
- One sentence: what clinical research problem are you working on? (Student fills this in — write a placeholder)
- A brief note: workspace is ready, dashboard is running

Write `Lab00/work/status.json`:
```json
{
  "status": "ok",
  "lab": "Lab00",
  "course": "Agentic Clinical Research Studio",
  "workspace_ready": true
}
```

---

## Step 6 — Report to the student

When done, say clearly:

> **Workspace ready.** Here is what was done:
> - Python [version] confirmed
> - Dependencies installed from `lecture-repo/requirements.txt`
> - Lab working folders confirmed present
> - Preflight checks passed (or: list of failures)
> - Dashboard started at http://localhost:8501
> - Lab00 orientation artifact created in `Lab00/work/`
>
> **Next step:** Return to the dashboard and select **Lab00 — Welcome to Agentic Clinical Research** in the sidebar.

If anything failed, say clearly what failed and what the student should do to fix it.

---

**Honesty requirements:**
- Do not mark the workspace as ready if there are unresolved errors
- If a package fails to install, say so — do not silently continue
- If the dashboard does not start, say so and give the error message
- The student needs an accurate picture of what is actually working
