# Prompt: Start the Course Dashboard

Paste this prompt into Claude Code in VS Code to launch the course dashboard.

---

## Layer A — Run this prompt in Claude Code

> "You are the Clinical Claude course setup assistant. Read CLAUDE.md and START_HERE.md in this repository.
> 
> Then do the following:
> 
> 1. Check that a virtual environment exists at .venv/ and that requirements.txt packages are installed. If not, create the venv and run: pip install -r requirements.txt
> 2. Check that the outputs/ directory structure exists (outputs/status/, outputs/figures/, outputs/metrics/, reports/). Create any missing directories.
> 3. Check whether make preflight passes. If it fails, report which checks fail and fix what you can.
> 4. Launch the Streamlit dashboard: streamlit run app/streamlit_app.py
> 5. Confirm the dashboard is accessible at http://localhost:8501
> 
> Report your actions to the student in plain language. If anything couldn't be fixed automatically, explain what manual action is needed."

---

## Layer B — Understanding what this prompt does

This prompt uses Claude Code to:

- **Read project context** (CLAUDE.md + START_HERE.md) before taking action — this is the project memory principle from L0
- **Audit the environment** before running anything — checking prerequisites rather than assuming they exist
- **Create required directories** — the output contract infrastructure that all later labs depend on
- **Run make preflight** — the structural health check that confirms the repo is intact
- **Launch the dashboard** — your navigation console for the rest of the course

Notice that this prompt specifies exact steps (1–5) in order. It does not say "set up the course." It tells Claude what each step requires. This is a prompt contract.

---

## If the dashboard does not start

Try running it directly:

```bash
source .venv/bin/activate
streamlit run app/streamlit_app.py
```

If that fails, check:
- Python version: `python --version` (needs 3.9+)
- Streamlit installed: `pip show streamlit`
- Port in use: try `streamlit run app/streamlit_app.py --server.port 8502`
