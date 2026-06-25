"""
Agentic Clinical Research Studio — Course Dashboard
A modern long-form course reader + lab runner.
"""

from pathlib import Path
import html as _html
import json
import streamlit as st

BASE = Path(__file__).resolve().parents[2]

st.set_page_config(
    page_title="Agentic Clinical Research Studio",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS ──────────────────────────────────────────────────────────────────────
# Design goal: long-form course reader, not a developer dashboard.
# Inspired by Anthropic Academy visual principles — calm cream, large type,
# vertical reading flow — without copying any Anthropic branding.

def inject_css() -> None:
    st.markdown("""
<style>
/* ── Design tokens — unified with course-site/assets/style.css ──────────── */
/* bg:#F0F2F7  surface:#FFF  teal:#1B4C68  teal-dark:#12344A  copper:#9E5B1E */

/* ── Global ──────────────────────────────────────────────────────────────── */
html, body, .stApp {
    background: #F0F2F7 !important;
    color: #14181F !important;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    font-size: 16px !important;
    line-height: 1.70 !important;
}
.stApp > header { background: #F0F2F7 !important; border-bottom: 1px solid #C8CDD8 !important; }

/* Content column — reading width, generous padding */
.main .block-container {
    background: transparent !important;
    padding: 2.5rem 3rem 5rem 3rem !important;
    max-width: 940px !important;
}

/* Typography scale — Palatino for display, Helvetica Neue for body */
.main h1 {
    font-family: 'Palatino Linotype', Palatino, 'Book Antiqua', Georgia, serif !important;
    font-size: 2.4rem !important; font-weight: 400 !important;
    letter-spacing: -0.01em !important; color: #14181F !important;
    line-height: 1.15 !important; margin-bottom: 0.25em !important;
}
.main h2 {
    font-family: 'Palatino Linotype', Palatino, 'Book Antiqua', Georgia, serif !important;
    font-size: 1.55rem !important; font-weight: 400 !important;
    color: #14181F !important;
    margin-top: 2.2rem !important; margin-bottom: 0.4rem !important;
}
.main h3 {
    font-size: 1.02rem !important; font-weight: 700 !important;
    color: #14181F !important; letter-spacing: 0.01em !important;
    margin-top: 1.6rem !important;
}
.main p, .main li {
    font-size: 0.97rem !important; line-height: 1.75 !important; color: #414C5C !important;
}
.main strong { color: #14181F !important; }
hr { border: none !important; border-top: 1px solid #C8CDD8 !important; margin: 2rem 0 !important; }

/* ── Sidebar ─────────────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: #E8ECF2 !important;
    border-right: 1px solid #C8CDD8 !important;
    min-width: 260px !important;
    max-width: 280px !important;
}
section[data-testid="stSidebar"] > div:first-child {
    background: #E8ECF2 !important;
    padding: 1.4rem 0.6rem 2rem 0.6rem !important;
}

/* Sidebar branding — serif wordmark matching nav aesthetic */
.sidebar-wordmark {
    font-family: 'Palatino Linotype', Palatino, 'Book Antiqua', Georgia, serif !important;
    font-size: 1.0rem !important; font-weight: 400 !important; color: #14181F !important;
    letter-spacing: 0 !important; line-height: 1.3 !important;
    padding: 0 8px !important; margin-bottom: 2px !important;
    display: block !important;
}
.sidebar-tagline {
    font-size: 0.64rem !important; font-weight: 700 !important; color: #6D798C !important;
    text-transform: uppercase !important; letter-spacing: 0.14em !important;
    padding: 0 8px !important; display: block !important; margin-bottom: 14px !important;
}
.sidebar-progress-text {
    font-size: 0.72rem !important; color: #6D798C !important;
    padding: 4px 8px 0 8px !important; display: block !important;
}

/* Sidebar section headers */
.nav-section {
    font-size: 0.60rem !important; font-weight: 700 !important;
    letter-spacing: 0.20em !important; text-transform: uppercase !important;
    color: #6D798C !important; padding: 12px 8px 4px 8px !important; display: block !important;
}

/* Sidebar nav buttons */
section[data-testid="stSidebar"] .stButton { margin-bottom: 1px !important; }
section[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    border: none !important; border-radius: 3px !important;
    text-align: left !important; justify-content: flex-start !important;
    padding: 7px 14px !important; width: 100% !important;
    font-size: 0.90rem !important; font-weight: 500 !important;
    color: #414C5C !important; cursor: pointer !important;
    transition: background 0.1s !important; line-height: 1.45 !important;
    min-height: 0 !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: #D8DEE8 !important; color: #14181F !important;
}
/* Active nav button — teal, matching course-site */
section[data-testid="stSidebar"] [data-testid="baseButton-primary"] {
    background: #E0EBF4 !important;
    color: #1B4C68 !important; font-weight: 700 !important;
    border-left: 3px solid #1B4C68 !important;
    padding-left: 11px !important;
}
section[data-testid="stSidebar"] [data-testid="baseButton-primary"]:hover {
    background: #D0E3F0 !important;
}
section[data-testid="stSidebar"] hr { border-color: #C8CDD8 !important; margin: 10px 0 !important; }

/* ── Tabs ────────────────────────────────────────────────────────────────── */
[data-testid="stTabs"] [role="tablist"] {
    border-bottom: 1px solid #C8CDD8 !important; gap: 0 !important; padding-bottom: 0 !important;
}
[data-testid="stTabs"] [role="tab"] {
    color: #6D798C !important; border: none !important;
    border-bottom: 2px solid transparent !important; margin-bottom: -1px !important;
    padding: 10px 20px !important; font-size: 0.85rem !important; font-weight: 600 !important;
    letter-spacing: 0.02em !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    color: #1B4C68 !important; border-bottom-color: #1B4C68 !important;
}

/* ── Metrics ─────────────────────────────────────────────────────────────── */
[data-testid="metric-container"] {
    background: #fff !important; border: 1px solid #C8CDD8 !important;
    border-radius: 3px !important; padding: 16px 20px !important;
}
[data-testid="stMetricLabel"] {
    color: #6D798C !important; font-size: 0.70rem !important; font-weight: 700 !important;
    letter-spacing: 0.08em !important; text-transform: uppercase !important;
}
[data-testid="stMetricValue"] { color: #14181F !important; font-size: 1.5rem !important; font-weight: 600 !important; }

/* ── Code blocks ─────────────────────────────────────────────────────────── */
.stCodeBlock, .stCodeBlock pre {
    background: #EAECF2 !important; border: 1px solid #C8CDD8 !important; border-radius: 3px !important;
}
.stCodeBlock code { font-size: 0.84rem !important; line-height: 1.75 !important; }

/* ── Expanders ───────────────────────────────────────────────────────────── */
details[data-testid="stExpander"] > summary {
    background: #fff !important; border: 1px solid #C8CDD8 !important;
    border-radius: 3px !important; font-size: 0.87rem !important; font-weight: 600 !important;
    color: #414C5C !important; padding: 10px 16px !important;
}
details[data-testid="stExpander"] > div {
    background: #F0F2F7 !important; border: 1px solid #C8CDD8 !important;
    border-top: none !important; border-radius: 0 0 3px 3px !important; padding: 16px 20px !important;
}
details[data-testid="stExpander"][open] > summary { border-radius: 3px 3px 0 0 !important; }

/* ── Progress bar ────────────────────────────────────────────────────────── */
.stProgress > div { background: #DCE0E9 !important; border-radius: 2px !important; height: 4px !important; }
.stProgress > div > div { height: 4px !important; background: #1B4C68 !important; border-radius: 2px !important; }

/* ── Alerts ──────────────────────────────────────────────────────────────── */
[data-testid="stAlert"] { border-radius: 3px !important; font-size: 0.90rem !important; }

/* ── Main buttons (non-sidebar) ─────────────────────────────────────────── */
.main .stButton > button {
    background: #fff !important; color: #414C5C !important;
    border: 1px solid #C8CDD8 !important; border-radius: 3px !important;
    font-size: 0.86rem !important; font-weight: 600 !important; padding: 8px 18px !important;
    letter-spacing: 0.02em !important;
}
.main .stButton > button:hover { background: #E8ECF2 !important; color: #14181F !important; }

/* ═══════════════════════════════════════════════════
   COURSE READER COMPONENTS
   ═══════════════════════════════════════════════════ */

/* Hero — dark teal, serif heading, flat geometry matching nav */
.hero {
    background: #12344A;
    border-radius: 4px; padding: 44px 48px 40px; margin-bottom: 36px;
}
.hero-eye {
    font-size: 0.63rem; font-weight: 700; letter-spacing: 0.22em;
    text-transform: uppercase; color: #7AB0CC; margin-bottom: 14px;
}
.hero-title {
    font-family: 'Palatino Linotype', Palatino, 'Book Antiqua', Georgia, serif;
    font-size: 2.1rem; font-weight: 400; color: #F0F4F8;
    letter-spacing: -0.01em; line-height: 1.15; margin-bottom: 16px;
}
.hero-body { font-size: 0.97rem; color: #8FB5CC; line-height: 1.75; max-width: 600px; margin-bottom: 0; }

/* Narrative flow diagram */
.flow-diagram {
    display: flex; align-items: stretch; gap: 0; margin: 24px 0;
    border: 1px solid #C8CDD8; border-radius: 3px; overflow: hidden; background: #fff;
}
.flow-step {
    flex: 1; padding: 20px 14px; text-align: center; border-right: 1px solid #C8CDD8;
    position: relative;
}
.flow-step:last-child { border-right: none; }
.flow-step::after {
    content: "→"; position: absolute; right: -10px; top: 50%; transform: translateY(-50%);
    color: #6D798C; font-size: 0.85rem; z-index: 1; background: #fff; padding: 0 2px;
}
.flow-step:last-child::after { display: none; }
.flow-num {
    display: inline-flex; align-items: center; justify-content: center;
    width: 26px; height: 26px; border-radius: 50%; background: #E0EBF4;
    color: #12344A; font-size: 0.78rem; font-weight: 700; margin-bottom: 8px;
}
.flow-title { font-size: 0.80rem; font-weight: 700; color: #14181F; margin-bottom: 4px; }
.flow-body { font-size: 0.72rem; color: #6D798C; line-height: 1.48; }

/* Lab header — serif title matching course-site lab rows */
.lab-header { margin-bottom: 28px; }
.lab-eyebrow {
    font-size: 0.62rem; font-weight: 700; letter-spacing: 0.20em;
    text-transform: uppercase; color: #1B4C68; margin-bottom: 10px;
}
.lab-title {
    font-family: 'Palatino Linotype', Palatino, 'Book Antiqua', Georgia, serif;
    font-size: 2.1rem; font-weight: 400; color: #14181F;
    letter-spacing: -0.01em; line-height: 1.15; margin-bottom: 10px;
}
.lab-question { font-size: 1.05rem; color: #414C5C; line-height: 1.65; font-style: italic; margin-bottom: 16px; max-width: 680px; }
.chip-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 4px; }
.chip {
    font-size: 0.70rem; font-weight: 600; color: #414C5C;
    background: #EAECF2; border: 1px solid #C8CDD8; padding: 3px 10px; border-radius: 20px;
}
.chip.complete { background: #D1FAE5; color: #065F46; border-color: #A7F3D0; }
.chip.ext { background: #FBF0E4; color: #9E5B1E; border-color: #D9AA7A; }

/* Callout boxes — blue callout now uses course-site teal */
.callout { border-radius: 3px; padding: 16px 20px; margin: 12px 0; }
.callout-blue  { background: #E0EBF4; border: 1px solid #B5CDE6; border-left: 4px solid #1B4C68; }
.callout-amber { background: #FBF0E4; border: 1px solid #D9AA7A; border-left: 4px solid #9E5B1E; }
.callout-green { background: #F0FDF4; border: 1px solid #BBF7D0; border-left: 4px solid #16A34A; }
.callout-red   { background: #FFF1F2; border: 1px solid #FECDD3; border-left: 4px solid #E11D48; }
.callout-dark  { background: #12344A; border-radius: 4px; padding: 22px 26px; }
.callout-label { font-size: 0.60rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.16em; margin-bottom: 8px; }
.callout-blue  .callout-label { color: #1B4C68; }
.callout-amber .callout-label { color: #9E5B1E; }
.callout-green .callout-label { color: #16A34A; }
.callout-red   .callout-label { color: #BE123C; }
.callout-dark  .callout-label { color: #7AB0CC; }
.callout-body  { font-size: 0.93rem; line-height: 1.72; }
.callout-blue  .callout-body { color: #14181F; }
.callout-amber .callout-body { color: #14181F; }
.callout-green .callout-body { color: #166534; }
.callout-red   .callout-body { color: #881337; }
.callout-dark  .callout-body { color: #8FB5CC; }

/* Before / After — after card uses teal top border */
.ba-pair { display: flex; gap: 14px; flex-wrap: wrap; margin: 12px 0 16px; }
.ba-card { flex: 1; min-width: 260px; background: #fff; border: 1px solid #C8CDD8; border-radius: 3px; padding: 16px 18px; }
.ba-card.before { border-top: 2px solid #EF4444; }
.ba-card.after  { border-top: 2px solid #1B4C68; }
.ba-label { font-size: 0.60rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 10px; }
.ba-card.before .ba-label { color: #DC2626; }
.ba-card.after  .ba-label { color: #1B4C68; }
.ba-prompt { font-family: 'SFMono-Regular', 'SF Mono', Menlo, Consolas, monospace; font-size: 0.80rem; color: #414C5C; line-height: 1.65; white-space: pre-wrap; }

/* Artifact contract */
.artifact-row {
    display: flex; align-items: center; gap: 10px; padding: 9px 14px;
    border-radius: 3px; margin-bottom: 5px; background: #fff; border: 1px solid #C8CDD8;
}
.artifact-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
.artifact-dot.done    { background: #22C55E; }
.artifact-dot.missing { background: #C8CDD8; }
.artifact-path { font-family: 'SFMono-Regular', Menlo, Consolas, monospace; font-size: 0.82rem; color: #414C5C; flex: 1; }
.artifact-tag { font-size: 0.63rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.10em; padding: 2px 8px; border-radius: 3px; flex-shrink: 0; }
.artifact-tag.done    { background: #D1FAE5; color: #065F46; }
.artifact-tag.missing { background: #EAECF2; color: #6D798C; }

/* Reflection */
.reflection-item {
    background: #fff; border: 1px solid #C8CDD8; border-left: 2px solid #1B4C68;
    border-radius: 3px; padding: 13px 18px; margin-bottom: 7px;
}
.reflection-num { font-size: 0.60rem; font-weight: 700; color: #1B4C68; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 3px; }
.reflection-q { font-size: 0.93rem; color: #14181F; line-height: 1.65; }

/* Progress row */
.prog-row {
    display: flex; align-items: center; gap: 10px; padding: 10px 16px;
    background: #fff; border: 1px solid #C8CDD8; border-radius: 3px; margin-bottom: 5px;
}
.prog-dot { width: 9px; height: 9px; border-radius: 50%; flex-shrink: 0; }
.prog-dot.done    { background: #22C55E; }
.prog-dot.missing { background: #C8CDD8; }
.prog-id    { font-size: 0.76rem; font-weight: 700; color: #6D798C; width: 42px; flex-shrink: 0; font-variant-numeric: tabular-nums; }
.prog-title { font-size: 0.90rem; font-weight: 600; color: #14181F; flex: 1; }
.prog-status { font-size: 0.70rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; }
.prog-status.done    { color: #16A34A; }
.prog-status.missing { color: #6D798C; }

/* Capstone hero — teal gradient matching design system */
.capstone-hero {
    background: linear-gradient(135deg, #12344A 0%, #1B4C68 100%);
    border-radius: 4px; padding: 36px 40px; color: #fff; margin-bottom: 28px;
}
.capstone-title {
    font-family: 'Palatino Linotype', Palatino, 'Book Antiqua', Georgia, serif;
    font-size: 2.0rem; font-weight: 400; letter-spacing: -0.01em;
}
.capstone-sub { font-size: 0.95rem; color: #8FB5CC; margin-top: 8px; line-height: 1.65; }

/* Syllabus table */
.syllabus-table { width: 100%; border-collapse: collapse; font-size: 0.87rem; background: #fff; border-radius: 3px; overflow: hidden; border: 1px solid #C8CDD8; }
.syllabus-table thead tr { background: #EAECF2; }
.syllabus-table th { text-align: left; padding: 10px 14px; font-size: 0.66rem; font-weight: 700; color: #6D798C; letter-spacing: 0.10em; text-transform: uppercase; border-bottom: 1px solid #C8CDD8; }
.syllabus-table td { padding: 11px 14px; border-bottom: 1px solid #DCE0E9; color: #414C5C; vertical-align: top; }
.syllabus-table tr:last-child td { border-bottom: none; }
.syllabus-table tr:hover td { background: #F4F5F9; }
.type-badge { display: inline-block; padding: 2px 8px; border-radius: 3px; font-size: 0.66rem; font-weight: 700; }
.type-badge.core     { background: #E0EBF4; color: #1B4C68; }
.type-badge.done     { background: #D1FAE5; color: #065F46; }
.type-badge.ext      { background: #FBF0E4; color: #9E5B1E; }
.type-badge.capstone { background: #E0EBF4; color: #12344A; }

/* Further learning */
.learn-section { background: #EAECF2; border: 1px solid #C8CDD8; border-radius: 3px; padding: 16px 20px; margin: 8px 0; }
.learn-category { font-size: 0.68rem; font-weight: 700; color: #14181F; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 6px; }
.learn-item { font-size: 0.87rem; color: #414C5C; line-height: 1.65; padding: 2px 0; }

/* Mermaid diagram block */
.diagram-block { background: #EAECF2; border: 1px solid #C8CDD8; border-radius: 3px; padding: 16px 20px; margin: 12px 0; }
.diagram-label { font-size: 0.62rem; font-weight: 700; color: #6D798C; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 10px; }

</style>
""", unsafe_allow_html=True)


inject_css()

# ─── Utilities ─────────────────────────────────────────────────────────────────

def h(text: str) -> str:
    return _html.escape(str(text))

def load_json(rel: str) -> dict | None:
    p = BASE / rel
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return None
    return None

def read_text(rel: str) -> str | None:
    p = BASE / rel
    if p.exists():
        try:
            return p.read_text(encoding="utf-8")
        except Exception:
            return None
    return None

def exists(rel: str) -> bool:
    return (BASE / rel).exists()

# ─── Course data ────────────────────────────────────────────────────────────────
# Unified artifact convention (primary):
#   reports/labs/LN_*.md  |  outputs/labs/LN/status.json
# Legacy paths kept for backward compatibility.

CORE_LABS = [
    # ── L0 ──────────────────────────────────────────────────────────────────────
    {
        "id": "L0",
        "type": "core",
        "nav_label": "L0 — Welcome to Agentic Clinical Research",
        "title": "Welcome to Agentic Clinical Research",
        "subtitle": "A new way to do research — with Claude as collaborator, not just a search tool",
        "lab_question": "Why agentic clinical research, and what will this course change in my workflow?",
        "short_description": "Course orientation: what agentic research means, how the course works, and your first artifact.",
        "estimated_time": "30 min",
        "day": "Day 1",
        "clinical_bottleneck": (
            "You have a PhD research question. You open a browser, paste something into Claude.ai, "
            "read an answer, and move on. Later you cannot find that conversation. Your supervisor "
            "asks how you reached a conclusion. You have no record. This is the common starting point — "
            "and it is the problem this course is designed to solve."
        ),
        "agentic_concept": (
            "Agentic research means Claude acts as a systematic, traceable collaborator — not a search box. "
            "Every significant research action produces a committed artifact: a file in your repository with "
            "a recorded prompt, a documented assumption, and a verifiable output. "
            "The key shift: from 'I asked Claude and got an answer' to 'I ran a documented workflow that produced a reviewable artifact'."
        ),
        "how_this_differs": None,
        "before_prompt": "Claude, can you help with my brain tumour research?",
        "after_prompt": (
            "First confirm you are working from the repository root.\n"
            "You should see START_HERE.md, CLAUDE.md, app/, handouts/, prompts/.\n"
            "If you are not in the repo root, stop and tell me.\n\n"
            "Task: Create an orientation artifact for this course.\n\n"
            "Write reports/labs/L0_orientation.md:\n"
            "  - Course title and today's date\n"
            "  - One sentence: what clinical research problem are you working on?\n"
            "  - Three labs you want to try first, and why\n"
            "  - One question you have about using Claude for research\n\n"
            "Write outputs/labs/L0/status.json:\n"
            "  { \"status\": \"ok\", \"lab\": \"L0\", \"course\": \"Agentic Clinical Research Studio\" }"
        ),
        "assignment_steps": [
            "1. Paste prompts/00_start_agentic_studio.md into Claude Code to prepare the workspace.",
            "2. Once Claude confirms the workspace is ready, return to the dashboard.",
            "3. Read this lesson — understand the course structure and the agentic loop.",
            "4. Run the After prompt above to create your orientation artifact.",
            "5. Confirm both files exist in the Artifacts tab.",
        ],
        "lab_folder": "Lab00",
        "artifact_paths": [
            "Lab00/work/L0_orientation.md",
            "Lab00/work/status.json",
        ],
        "legacy_artifact_paths": [
            "lecture-repo/reports/labs/L0_orientation.md",
            "lecture-repo/outputs/labs/L0/status.json",
            "lecture-repo/outputs/status/lab_00_agentic_studio.json",
            "lecture-repo/outputs/status/stage_00_bootstrap.json",
        ],
        "reflection_questions": [
            "What is the difference between Claude answering a question in chat and producing a committed artifact?",
            "Look at reports/labs/L0_orientation.md — could a colleague reproduce your reasoning from that file alone?",
            "Which of the remaining labs seems most relevant to your current PhD research? Why?",
        ],
        "responsible_use": (
            "Claude cannot verify your institution's data governance requirements. "
            "Before using agentic workflows with real patient data, confirm your compliance obligations with your DPO or IRB."
        ),
        "extension": "Read CLAUDE.md carefully. What project-level instructions would make Claude a more useful collaborator for your own research? (Project memory is explored in depth in L8.)",
        "further_learning": [
            ("Anthropic Documentation", [
                "docs.anthropic.com — Claude's official documentation, models overview, and API guides",
                "Search: 'Claude Code documentation' — VS Code integration and agentic workflows",
                "Search: 'Anthropic prompt engineering guide' — best practices for instructing Claude",
            ]),
            ("Claude Code & Agentic Workflows", [
                "Search: 'Claude Code tutorial 2024 2025' on YouTube for setup walkthroughs",
                "Search: 'CLAUDE.md project memory' — how to write effective project context files",
            ]),
            ("Clinical AI Foundations", [
                "Search PubMed: 'responsible AI clinical research reporting guidelines'",
                "Search: 'TRIPOD-AI reporting guideline 2024' — AI/ML clinical study checklist",
                "Search: 'SPIRIT-AI trial protocol guideline' — AI clinical trial protocols",
            ]),
        ],
        "diagram": None,
        "handout_path": "lecture-repo/handouts/L0_agentic_clinical_research_studio.md",
        "guide_path": "lecture-repo/modules/L0_agentic_studio/README.md",
    },
    # ── L1 ──────────────────────────────────────────────────────────────────────
    {
        "id": "L1",
        "type": "core",
        "nav_label": "L1 — Prompt Contracts",
        "title": "Prompt Contracts",
        "subtitle": "Turning a vague request into a verifiable task",
        "lab_question": "How do I turn a vague clinical research request into a verifiable task?",
        "short_description": "Write prompts that function as mini-protocols: defined inputs, constrained actions, verifiable output schema.",
        "estimated_time": "40 min",
        "day": "Day 1",
        "clinical_bottleneck": (
            "You ask Claude to 'analyse this dataset' and receive a fluent paragraph. "
            "Two sessions later, the same request produces a different structure with different assumptions. "
            "A peer reviewer asks: 'what exactly did the analysis do?' — and you cannot answer precisely."
        ),
        "agentic_concept": (
            "A prompt contract specifies three things explicitly: what Claude may read (inputs), "
            "what Claude may do (permissions), and what it must produce (output schema — exact file paths, JSON keys, report sections). "
            "The result is reproducible and auditable — like a clinical trial protocol, not a conversational exchange. "
            "Scope: one task, one structured output."
        ),
        "how_this_differs": None,
        "before_prompt": "Look at the imaging data and tell me what you see.",
        "after_prompt": (
            "First confirm you are working from the repository root.\n"
            "You should see START_HERE.md, CLAUDE.md, app/, handouts/, prompts/.\n\n"
            "Input: Read data/sample/ — inspect the first available file.\n"
            "Permissions: Read-only. Do NOT modify any data files.\n\n"
            "Task: characterise the imaging dataset.\n\n"
            "Output contract:\n"
            "Write outputs/labs/L1/status.json with EXACTLY these keys:\n"
            "  { \"file_count\": int, \"shape\": [x,y,z], \"voxel_range\": [min,max],\n"
            "    \"modality_guess\": str, \"quality_flags\": list[str] }\n\n"
            "Write reports/labs/L1_prompt_contract.md:\n"
            "  - One paragraph on data suitability for analysis\n"
            "  - Confidence level: HIGH / MEDIUM / LOW\n"
            "  - Assumptions stated explicitly\n\n"
            "Do not fabricate values. If a value cannot be determined, write null and explain why."
        ),
        "assignment_steps": [
            "1. Open prompts/stage_02_load_visualize.md — study its contract structure.",
            "2. Paste it into Claude Code. Verify all JSON keys are present.",
            "3. Run it again in a new session — does the schema match exactly?",
            "4. Add a reflection paragraph to your report: what did the contract guarantee?",
            "5. Commit both artifacts.",
        ],
        "lab_folder": "Lab01",
        "artifact_paths": [
            "Lab01/work/L1_prompt_contract.md",
            "Lab01/work/status.json",
        ],
        "legacy_artifact_paths": [
            "lecture-repo/outputs/labs/L1/status.json",
            "lecture-repo/reports/labs/L1_prompt_contract.md",
            "lecture-repo/outputs/status/lab_01_prompt_contract.json",
        ],
        "reflection_questions": [
            "How is a prompt contract similar to a function signature? What does each component guarantee?",
            "What would a peer reviewer need to reproduce your result using only the prompt and artifact?",
            "When would you use a loose, conversational prompt rather than a contract? Give a research example.",
        ],
        "responsible_use": (
            "Output contracts help prevent hallucination by requiring specific keys with specific types. "
            "If Claude cannot determine a value, the contract forces it to write null + reason rather than fabricate a plausible number."
        ),
        "extension": "Write the same prompt contract for a different audience: a radiologist needing file format and resolution, not ML metadata. Compare the two schemas. What changed and why?",
        "further_learning": [
            ("Prompt Engineering", [
                "Search: 'Anthropic prompt engineering overview structured outputs'",
                "Search: 'JSON schema enforcement Claude API'",
                "Search: 'Anthropic prompt engineering interactive tutorial'",
            ]),
            ("Clinical Research Protocols", [
                "Search PubMed: 'clinical research protocol reproducibility AI'",
                "Search: 'CONSORT reporting guidelines checklist'",
            ]),
            ("Reproducibility in Clinical AI", [
                "Search: 'model cards AI transparency Mitchell 2019'",
                "Search: 'datasheets for datasets Gebru 2021'",
            ]),
        ],
        "diagram": """graph LR
    A[Clinical Question] --> B[Prompt Contract]
    B --> C{Claude Executes}
    C --> D[outputs/labs/L1/status.json]
    C --> E[reports/labs/L1_prompt_contract.md]
    D --> F[Validation: all keys present?]
    E --> F
    F --> G[Commit to git]""",
        "handout_path": "lecture-repo/handouts/L1_prompt_contracts.md",
        "guide_path": "lecture-repo/modules/L1_prompt_contracts/README.md",
    },
    # ── L2 ──────────────────────────────────────────────────────────────────────
    {
        "id": "L2",
        "type": "core",
        "nav_label": "L2 — Multi-Stakeholder Review",
        "title": "Multi-Stakeholder Review",
        "subtitle": "How do different people see your study idea?",
        "lab_question": "How do I make Claude review a study idea from stakeholder perspectives I may not naturally have?",
        "short_description": "Use role prompting to simulate IT, clinician, PI, governance, patient, and reviewer perspectives.",
        "estimated_time": "45 min",
        "day": "Day 1",
        "clinical_bottleneck": (
            "As a medical PhD student you understand the scientific question deeply. "
            "But you may not have the instincts of an IT security officer, a GDPR compliance lead, "
            "a hospital radiologist, or a patient considering participation. "
            "Reviewing a clinical AI idea from only your own perspective misses failure modes "
            "that become expensive — or harmful — later."
        ),
        "agentic_concept": (
            "Role prompting and stakeholder simulation. Claude adopts specific identities — each with its "
            "own knowledge base, priorities, and concerns — and produces critique from that perspective. "
            "The researcher synthesises the critiques into design improvements. "
            "This is fundamentally different from asking Claude to 'review' your work generically: "
            "a generic review stays in your own frame. Role prompting surfaces blind spots outside it."
        ),
        "how_this_differs": None,
        "before_prompt": "Can you review my clinical AI study plan and tell me if it's good?",
        "after_prompt": (
            "First confirm you are working from the repository root.\n\n"
            "Study to review: [INSERT YOUR 3-5 SENTENCE STUDY DESCRIPTION HERE]\n\n"
            "For each stakeholder, write one focused paragraph of critique:\n\n"
            "1. IT / Data Engineer — infrastructure, security, computation\n"
            "2. Clinical Workflow (nurse or radiologist) — usability, patient safety\n"
            "3. Data Governance / Privacy — GDPR/HIPAA, consent, audit\n"
            "4. Principal Investigator — scientific rigour, feasibility\n"
            "5. Journal Reviewer — methodology, reproducibility\n"
            "6. Patient Representative — understandability, benefit-risk\n\n"
            "Then write a synthesis:\n"
            "  - Top 3 risks across all perspectives\n"
            "  - Top 3 recommended improvements\n"
            "  - One assumption at least two stakeholders challenged\n\n"
            "Write to reports/labs/L2_multi_stakeholder_review.md.\n"
            "Write to outputs/labs/L2/status.json: { \"status\": \"ok\", \"lab\": \"L2\" }"
        ),
        "assignment_steps": [
            "1. Write a 3-5 sentence study description (your own or the brain imaging case).",
            "2. Paste the prompt into Claude Code.",
            "3. Read each of the six perspectives separately — which surprised you most?",
            "4. Write a revised one-paragraph study plan addressing the top 3 risks.",
            "5. Commit both artifacts.",
        ],
        "lab_folder": "Lab02",
        "artifact_paths": [
            "Lab02/work/L2_multi_stakeholder_review.md",
            "Lab02/work/status.json",
        ],
        "legacy_artifact_paths": [
            "lecture-repo/reports/labs/L2_multi_stakeholder_review.md",
            "lecture-repo/outputs/labs/L2/status.json",
            "lecture-repo/outputs/status/lab_02_multi_stakeholder_review.json",
        ],
        "reflection_questions": [
            "Which stakeholder identified the risk you had least considered? Why did you miss it?",
            "How is stakeholder simulation different from asking Claude 'what could go wrong?'",
            "In your own PhD research, which stakeholder perspective is most absent from your planning?",
        ],
        "responsible_use": (
            "Stakeholder simulation produces likely perspectives, not professional advice. "
            "Critical compliance and legal questions must be reviewed by real professionals at your institution."
        ),
        "extension": "Add a seventh role: a regulatory body evaluator (CE marking or FDA 510(k) pathway). What additional requirements does this surface?",
        "further_learning": [
            ("Stakeholder Engagement in Clinical AI", [
                "Search PubMed: 'clinical AI stakeholder co-design framework'",
                "Search: 'participatory design healthcare AI 2023 2024'",
            ]),
            ("Clinical AI Governance", [
                "Search: 'UK NICE Evidence Standards Framework AI medical devices'",
                "Search: 'WHO ethics AI health 2021'",
                "Search: 'EU AI Act medical devices compliance guide'",
            ]),
            ("Role Prompting Techniques", [
                "Search: 'Anthropic role prompting system prompt examples'",
                "Search: 'persona prompting LLM evaluation review 2024'",
            ]),
        ],
        "diagram": None,
        "handout_path": "lecture-repo/handouts/L2_multi_stakeholder_review.md",
        "guide_path": "lecture-repo/modules/L2_multi_stakeholder_review/README.md",
    },
    # ── L3 ──────────────────────────────────────────────────────────────────────
    {
        "id": "L3",
        "type": "core",
        "nav_label": "L3 — Literature Search Skills",
        "title": "Literature Search Skills",
        "subtitle": "From one-off query to a reusable research skill",
        "lab_question": "How do I turn a repeated research task into a reusable Claude Skill?",
        "short_description": "Build a reusable literature search skill: PICO decomposition, search strings, human approval checkpoint, evidence extraction with confidence marking.",
        "estimated_time": "45 min",
        "day": "Day 1",
        "clinical_bottleneck": (
            "Every few months you do a new literature search. Each time, you start from scratch: "
            "no consistent PICO structure, no documented search strings, no record of what you searched. "
            "The result is an AI summary that mixes real citations with invented ones, "
            "and no methodology you can describe to a peer reviewer."
        ),
        "agentic_concept": (
            "A Claude Skill is a reusable workflow: documented steps, defined inputs and outputs, "
            "and at least one human approval checkpoint before high-stakes actions. "
            "Unlike a one-off prompt, a skill is templated so you can run it again next month "
            "on a different clinical question and get consistent, comparable results. "
            "The literature search skill: PICO → search strings → human review → evidence extraction → structured summary."
        ),
        "how_this_differs": (
            "**How this differs from L1 (Prompt Contracts):** "
            "L1 is about one task, one output. A skill is a repeatable workflow — "
            "you run it every time you need a literature review, not just once. "
            "The key addition is the human approval checkpoint, which makes the skill a supervised process "
            "rather than a single automated step."
        ),
        "before_prompt": "Find me papers on deep learning for brain tumour segmentation and summarise them.",
        "after_prompt": (
            "First confirm you are working from the repository root.\n\n"
            "Clinical question: [INSERT YOUR CLINICAL QUESTION HERE]\n\n"
            "Step 1 — PICO Decomposition: Population, Intervention/Index, Comparator, Outcome.\n\n"
            "Step 2 — Search String Design:\n"
            "Propose three PubMed search strings of increasing specificity.\n"
            "Mark [VERIFY] for any MeSH terms you are not certain about.\n\n"
            "Step 3 — Human Approval Checkpoint:\n"
            "State: 'Please review the search strings before I proceed.'\n"
            "List your top 3 assumptions for me to verify.\n\n"
            "Step 4 — Evidence Extraction:\n"
            "Extract up to 5 papers you are confident about.\n"
            "Table: Author, Year, Population, Method, Key Result, Confidence\n"
            "Use [HIGH] if certain | [ESTIMATED] if uncertain | do NOT invent paper titles.\n\n"
            "Step 5 — Synthesis: one paragraph on evidence, gaps, uncertainties.\n\n"
            "Output:\n"
            "  skills/L3_literature_search_skill.md — reusable skill template\n"
            "  reports/labs/L3_literature_search.md — full output for this search\n"
            "  outputs/labs/L3/status.json: { \"status\": \"ok\", \"lab\": \"L3\" }"
        ),
        "assignment_steps": [
            "1. Choose a clinical question from your own research or use the brain MRI case.",
            "2. Paste the prompt into Claude Code.",
            "3. At Step 3, actually evaluate the search strings — would you modify them?",
            "4. After the full output, manually verify ONE [ESTIMATED] paper against PubMed.",
            "5. Document your verification in the report. Commit all three artifacts.",
        ],
        "lab_folder": "Lab03",
        "artifact_paths": [
            "Lab03/work/L3_literature_search_skill.md",
            "Lab03/work/L3_literature_search.md",
            "Lab03/work/status.json",
        ],
        "legacy_artifact_paths": [
            "lecture-repo/skills/L3_literature_search_skill.md",
            "lecture-repo/reports/labs/L3_literature_search.md",
            "lecture-repo/outputs/labs/L3/status.json",
        ],
        "reflection_questions": [
            "How many papers were [ESTIMATED] vs [HIGH]? What does this tell you about Claude's field coverage?",
            "What would a formal systematic review protocol require that this skill does not yet provide?",
            "How would you adapt this skill for a different clinical question in your PhD research?",
        ],
        "responsible_use": (
            "Never use Claude-generated literature summaries in a publication without independent "
            "verification of every citation. [ESTIMATED] entries are a verification queue, not confirmed facts."
        ),
        "extension": "Apply the same skill to a different clinical question. Compare confidence levels across both domains. Where can Claude be trusted vs. not?",
        "further_learning": [
            ("Systematic Review Methodology", [
                "Search: 'Cochrane handbook systematic reviews 2022'",
                "Search: 'PRISMA 2020 statement systematic reviews reporting'",
                "Search PubMed: 'PICO framework clinical question construction'",
            ]),
            ("PubMed & Search Skills", [
                "pubmed.ncbi.nlm.nih.gov/help/ — official PubMed help guide",
                "Search: 'MeSH terms PubMed tutorial NLM'",
                "Search: 'boolean operators PubMed systematic review'",
            ]),
            ("AI for Literature Review", [
                "Search: 'LLM systematic review hallucination detection 2024'",
                "Search: 'AI-assisted evidence synthesis clinical research evaluation'",
                "Search: 'Elicit Consensus Semantic Scholar AI research assistants comparison'",
            ]),
        ],
        "diagram": """graph TD
    A[Clinical Question] --> B[PICO Decomposition]
    B --> C[Search String Design]
    C --> D{Human Approval Checkpoint}
    D -- Approved --> E[Evidence Extraction]
    D -- Revise --> C
    E --> F[Structured Summary with Confidence Marks]
    F --> G[skills/L3_literature_search_skill.md]
    F --> H[reports/labs/L3_literature_search.md]""",
        "handout_path": "lecture-repo/handouts/L3_literature_search_skills.md",
        "guide_path": "lecture-repo/modules/L3_literature_search_skills/README.md",
    },
    # ── L4 ──────────────────────────────────────────────────────────────────────
    {
        "id": "L4",
        "type": "core",
        "nav_label": "L4 — Tool / MCP-Aware Workflow",
        "title": "Tool / MCP-Aware Workflow",
        "subtitle": "Connecting research context safely",
        "lab_question": "How do I safely connect Claude to files, tools, papers, and research context?",
        "short_description": "Design safe, auditable tool-use workflows: explicit context permissions, forbidden zones, approval gates, audit logging.",
        "estimated_time": "45 min",
        "day": "Day 1",
        "clinical_bottleneck": (
            "Your research context is scattered: papers in Zotero, data in a hospital share, "
            "code on GitHub, notes in Notion. Connecting all of this to Claude is technically possible "
            "but unrestricted access creates serious privacy, security, and audit risks "
            "that you may not realise until it is too late."
        ),
        "agentic_concept": (
            "Context engineering and permission design. "
            "The principle: minimal necessary access. Claude does not need everything it could access — "
            "only what this specific task requires. "
            "MCP (Model Context Protocol) is the technical standard for connecting Claude to external tools safely. "
            "A well-designed tool workflow specifies: what Claude may read, what it may write, "
            "what is forbidden, when human approval is required, and how actions are logged."
        ),
        "how_this_differs": (
            "**How this differs from L3 (Skills):** "
            "L3 is about a documented workflow pattern. L4 is about the permission and safety architecture "
            "underneath any workflow — who can access what, when, and with what audit trail. "
            "A skill can have dangerous tool access; L4 teaches you to design that access responsibly."
        ),
        "before_prompt": "Claude, access all my research files and help me with this analysis.",
        "after_prompt": (
            "First confirm you are working from the repository root.\n\n"
            "Task: design a safe context workflow for: [INSERT YOUR SPECIFIC RESEARCH TASK]\n\n"
            "Write a specification to reports/labs/L4_tool_mcp_workflow.md:\n\n"
            "1. Context inventory: what data does this task actually require?\n"
            "   Format: Source | Type | Sensitivity (public/internal/restricted)\n\n"
            "2. Allowed context: list each permitted source explicitly\n"
            "3. Forbidden context: what must Claude NOT access? Why?\n"
            "4. Write permissions: what may Claude create or modify?\n"
            "5. Human approval gates: two to three review points, with risks of skipping\n"
            "6. Audit trail: what record of actions, and who reviews it?\n"
            "7. Risk analysis: three things that could go wrong\n"
            "   Format: Risk | Probability (L/M/H) | Severity | Mitigation\n\n"
            "Write to outputs/labs/L4/status.json: { \"status\": \"ok\", \"lab\": \"L4\" }"
        ),
        "assignment_steps": [
            "1. Choose a specific research task (your own or the brain MRI case).",
            "2. Paste the prompt into Claude Code.",
            "3. Review the context inventory — did Claude identify sensitive sources?",
            "4. Review the risk analysis — which risk concerns you most?",
            "5. Add a section: what would you change from Claude's permission design?",
        ],
        "lab_folder": "Lab04",
        "artifact_paths": [
            "Lab04/work/L4_tool_mcp_workflow.md",
            "Lab04/work/status.json",
        ],
        "legacy_artifact_paths": [
            "lecture-repo/reports/labs/L4_tool_mcp_workflow.md",
            "lecture-repo/outputs/labs/L4/status.json",
        ],
        "reflection_questions": [
            "What is the difference between 'everything Claude could access' and 'everything Claude needs for this task'?",
            "Which sources in your own research would you be comfortable giving Claude access to? Which would you withhold?",
            "How would you log Claude's actions to satisfy a data governance audit at your institution?",
        ],
        "responsible_use": (
            "MCP server integrations accessing hospital systems or patient records require institutional "
            "data governance approval regardless of what is technically possible. "
            "Claude helps design the workflow; your DPO or IRB must approve it."
        ),
        "extension": "Research the MCP specification at modelcontextprotocol.io. Design a hypothetical MCP server for your research domain — specify its allowed functions and data access scope.",
        "further_learning": [
            ("Model Context Protocol", [
                "modelcontextprotocol.io — official MCP specification and server examples",
                "Search: 'Claude MCP server tutorial 2024 2025'",
                "Search: 'Anthropic tool use function calling documentation'",
            ]),
            ("Research Data Governance", [
                "Search: 'GDPR research exemptions clinical data processing'",
                "Search: 'ICH E6 GCP guideline data integrity AI'",
                "Search: 'NHS data governance framework AI research'",
            ]),
            ("AI Safety & Permissions", [
                "Search: 'principle of least privilege AI agents'",
                "Search: 'prompt injection LLM tool use security 2024'",
            ]),
        ],
        "diagram": """graph LR
    subgraph ALLOWED
        A[reports/ read-write]
        B[data/sample/ read-only]
        C[Public literature]
    end
    subgraph FORBIDDEN
        D[Patient records]
        E[Hospital systems]
        F[Credentials / keys]
    end
    ALLOWED --> G{Claude Agent}
    G --> H[Artifact output]
    G --> I[Audit log]
    H --> J[Human Review Gate]""",
        "handout_path": "lecture-repo/handouts/L4_tool_mcp_research_workflows.md",
        "guide_path": "lecture-repo/modules/L4_tool_mcp_workflows/README.md",
    },
    # ── L5 ──────────────────────────────────────────────────────────────────────
    {
        "id": "L5",
        "type": "core",
        "nav_label": "L5 — Subagents & Orchestration",
        "title": "Subagents & Workflow Orchestration",
        "subtitle": "Dividing a complex research workflow across specialised roles",
        "lab_question": "How do I orchestrate multiple roles and subagents into a small clinical research workflow?",
        "short_description": "Design a multi-agent workflow: specialised subagents for literature, methods, compliance, and translation — with handoff protocols and human checkpoints.",
        "estimated_time": "50 min",
        "day": "Day 2",
        "clinical_bottleneck": (
            "Real clinical research requires multiple kinds of expertise simultaneously: "
            "someone who knows the literature, someone who understands trial design, "
            "someone who knows compliance. "
            "A single monolithic prompt trying to do all of these at once produces "
            "shallow outputs across every dimension."
        ),
        "agentic_concept": (
            "Specialised subagents with defined scopes and explicit handoff protocols. "
            "Each agent has one role, one input domain, and one output format. "
            "A coordinating step routes tasks between agents and synthesises their outputs. "
            "The handoff protocol — what one agent passes to the next — is what makes the system coherent."
        ),
        "how_this_differs": (
            "**How this differs from L4 (Tool Workflows):** "
            "L4 is about what context Claude accesses and with what permissions. "
            "L5 is about dividing labour across multiple specialised agents, each with a different role. "
            "The same clinical question is reviewed from multiple expert positions "
            "rather than by one general agent with broad context."
        ),
        "before_prompt": "Claude, do a complete review of my study — literature, methods, compliance — all at once.",
        "after_prompt": (
            "First confirm you are working from the repository root.\n\n"
            "Study to review: [INSERT YOUR STUDY DESCRIPTION HERE]\n\n"
            "--- SUBAGENT 1: LiteratureAgent ---\n"
            "Role: systematic review specialist\n"
            "Output: 3-5 bullets on gaps, prior work, positioning. Mark [VERIFIED] or [ESTIMATED].\n\n"
            "--- SUBAGENT 2: MethodCriticAgent ---\n"
            "Role: clinical trial methodologist\n"
            "Output: top 2 methodological risks. One concrete fix for each.\n\n"
            "--- SUBAGENT 3: ComplianceAgent ---\n"
            "Role: clinical research compliance officer\n"
            "Output: top 2 compliance concerns. Name applicable frameworks (GDPR, ICH-GCP).\n\n"
            "--- DECISION MEMO ---\n"
            "  1. Summary of all three outputs\n"
            "  2. Top risk across all perspectives\n"
            "  3. Recommended next step (one specific action)\n"
            "  4. What remains unresolved\n\n"
            "Write to workflows/L5_subagent_workflow.md — the workflow design for reuse.\n"
            "Write to reports/labs/L5_subagent_workflow.md — the output for this run.\n"
            "Write to outputs/labs/L5/status.json: { \"status\": \"ok\", \"lab\": \"L5\" }"
        ),
        "assignment_steps": [
            "1. Prepare a 3-5 sentence study description (your own or the brain MRI case).",
            "2. Paste the prompt into Claude Code.",
            "3. Read each subagent output separately — does each stay within its scope?",
            "4. Does the Decision Memo faithfully represent all three perspectives?",
            "5. Write a response: which subagent raised the most important concern?",
        ],
        "lab_folder": "Lab05",
        "artifact_paths": [
            "Lab05/work/L5_subagent_workflow.md",
            "Lab05/work/L5_subagent_workflow_report.md",
            "Lab05/work/status.json",
        ],
        "legacy_artifact_paths": [
            "lecture-repo/workflows/L5_subagent_workflow.md",
            "lecture-repo/reports/labs/L5_subagent_workflow.md",
            "lecture-repo/outputs/labs/L5/status.json",
        ],
        "reflection_questions": [
            "What would be lost if you collapsed all three subagents into a single prompt?",
            "At what points does a human need to be 'in the loop' between agents?",
            "Design a fourth subagent for this workflow — what would its role, scope, and output be?",
        ],
        "responsible_use": (
            "Agent orchestration can create compounding errors: if LiteratureAgent makes an incorrect assumption, "
            "MethodCriticAgent may build on it. Human review between agent handoffs is critical "
            "when decisions affect patient care or study design."
        ),
        "extension": "Create a simple Python script in workflows/ that runs two agents in sequence, passing the first output as context to the second. Observe how context affects the second agent.",
        "further_learning": [
            ("Agentic AI Systems", [
                "Search: 'Anthropic agent orchestration multi-step tool use'",
                "Search: 'LLM multi-agent coordination research 2024'",
                "Search: 'CrewAI LangGraph agentic research workflows tutorial'",
            ]),
            ("Workflow Design", [
                "Search: 'Anthropic prompt chaining sequential reasoning'",
                "Search: 'agent handoff protocol LLM design patterns 2024'",
            ]),
        ],
        "diagram": """graph TD
    A[Study Description] --> B[LiteratureAgent]
    A --> C[MethodCriticAgent]
    A --> D[ComplianceAgent]
    B --> E{Decision Memo}
    C --> E
    D --> E
    E --> F[Human Review]
    F --> G[workflows/L5_subagent_workflow.md]
    F --> H[reports/labs/L5_subagent_workflow.md]""",
        "handout_path": "lecture-repo/handouts/L5_subagents_workflow_orchestration.md",
        "guide_path": "lecture-repo/modules/L5_subagent_workflow/README.md",
    },
]

CAPSTONE = {
    "id": "CAP",
    "type": "capstone",
    "nav_label": "🏆 Capstone",
    "title": "Capstone Mini-Project",
    "subtitle": "Apply the full agentic workflow to your own clinical research problem",
    "lab_question": "How do I apply the full workflow to my own small clinical research problem?",
    "estimated_time": "60 min",
    "day": "Day 2",
    "lab_folder": "Capstone",
    "artifact_paths": [
        "Capstone/work/capstone_report.md",
        "Capstone/work/showcase.md",
        "Capstone/work/status.json",
    ],
    "legacy_artifact_paths": [
        "lecture-repo/reports/capstone/capstone_report.md",
        "lecture-repo/outputs/capstone/status.json",
        "lecture-repo/reports/capstone_report.md",
    ],
    "handout_path": "lecture-repo/handouts/capstone_mini_project.md",
    "guide_path": "lecture-repo/modules/capstone/README.md",
}

EXTENSION_LABS = [
    {
        "id": "L6",
        "type": "extension",
        "nav_label": "Controlled Experiments",
        "title": "Controlled Experiments",
        "subtitle": "One variable at a time — the discipline that makes results citable",
        "lab_question": "How do I run a clean, one-variable experiment and report the result honestly?",
        "short_description": "Design and run a controlled experiment on the brain imaging pipeline. One variable, documented baseline, honest interpretation.",
        "estimated_time": "45 min",
        "day": "Day 2",
        "clinical_bottleneck": "AI experiments that change multiple parameters simultaneously produce uninterpretable results. 'We improved performance' is not a scientific finding if three things changed at once.",
        "agentic_concept": "Controlled comparison with documented design. The constraint 'change ONLY X' must be explicit in the prompt — without it, Claude may optimise multiple parameters simultaneously, making the result unattributable.",
        "how_this_differs": None,
        "before_prompt": "Can you try to improve the performance? Try a few different approaches.",
        "after_prompt": (
            "First confirm you are working from the repository root.\n\n"
            "Baseline: Read outputs/metrics/val_metrics.json. Record current Dice as baseline_dice.\n\n"
            "Intervention: Change ONLY threshold from 0.5 to 0.6 in scripts/run_train.py. Nothing else.\n\n"
            "Write to outputs/extensions/L6/experiment_metrics.json:\n"
            "  { baseline_dice, intervention_dice, threshold_baseline: 0.5, threshold_intervention: 0.6, change_description }\n\n"
            "Write to reports/extensions/L6_controlled_experiment.md:\n"
            "  - Single variable changed\n"
            "  - Before/after table\n"
            "  - Null hypothesis\n"
            "  - Honest interpretation (negative results are valid results)\n\n"
            "Write to outputs/extensions/L6/status.json: { \"status\": \"ok\", \"lab\": \"L6\" }"
        ),
        "assignment_steps": [
            "1. Confirm outputs/metrics/val_metrics.json exists (run make smoke-train if needed).",
            "2. Paste the prompt into Claude Code.",
            "3. Verify Claude only changed the threshold parameter.",
            "4. Write your interpretation: if the result was negative, explain why that is still valid science.",
        ],
        "lab_folder": "Extension06",
        "artifact_paths": [
            "Extension06/work/L6_controlled_experiment.md",
            "Extension06/work/experiment_metrics.json",
            "Extension06/work/status.json",
        ],
        "legacy_artifact_paths": [
            "lecture-repo/reports/extensions/L6_controlled_experiment.md",
            "lecture-repo/outputs/extensions/L6/status.json",
        ],
        "reflection_questions": [
            "Can you fully attribute the metric change to the threshold? What else could have varied?",
            "How is this controlled experiment different from hyperparameter tuning?",
            "What is the minimum number of runs needed to trust this result?",
        ],
        "responsible_use": "A single controlled comparison on a 10-slice teaching dataset is not sufficient for clinical validation. This teaches experimental design principle, not a validated clinical result.",
        "extension": "Run threshold=0.4 as a second experiment. With three data points, what pattern emerges?",
        "further_learning": [
            ("Experimental Design", [
                "Search: 'controlled experiment design clinical AI evaluation'",
                "Search: 'statistical power sample size clinical AI study'",
            ]),
        ],
        "diagram": None,
        "handout_path": "lecture-repo/handouts/optional_L6_controlled_experiments.md",
        "guide_path": "lecture-repo/modules/extensions/L6_controlled_experiments/README.md",
    },
    {
        "id": "L7",
        "type": "extension",
        "nav_label": "Clinical Translation",
        "title": "Clinical Translation",
        "subtitle": "Audience-aware writing with honesty as the design constraint",
        "lab_question": "How do I write about AI results for a clinical audience without overclaiming?",
        "short_description": "Write a clinical collaborator briefing with explicit MUST NOT honesty constraints.",
        "estimated_time": "40 min",
        "day": "Day 2",
        "clinical_bottleneck": "Research prototype results are routinely overclaimed. A Dice of 0.58 becomes 'promising for clinical application' in a briefing that omits the failure cases. This erodes trust and wastes clinical partners' time.",
        "agentic_concept": "Audience-aware writing with explicit MUST NOT constraints. These override Claude's default optimism — 'helpful' in writing often means emphasising positives and smoothing over uncertainty.",
        "how_this_differs": None,
        "before_prompt": "Write a summary of my brain tumour segmentation results for a clinical collaborator.",
        "after_prompt": (
            "First confirm you are working from the repository root.\n\n"
            "Write a clinical collaborator briefing about this brain tumour segmentation study.\n"
            "Audience: radiologist with no ML background.\n"
            "Tone: honest, specific, measured. Length: approximately 400 words.\n\n"
            "You MUST include:\n"
            "  - What the method is (plain English, no jargon)\n"
            "  - The exact Dice coefficient from outputs/metrics/val_metrics.json\n"
            "  - Specific failure cases from reports/error_analysis.md\n"
            "  - What validation is required before clinical consideration\n\n"
            "You MUST NOT:\n"
            "  - Claim the method is ready for clinical use\n"
            "  - Compare to other methods without citing them\n"
            "  - Omit the failure cases\n"
            "  - Use ML jargon without explaining it\n"
            "  - Round the Dice score above its actual value\n\n"
            "Write to reports/extensions/L7_clinical_translation.md.\n"
            "Write to outputs/extensions/L7/status.json: { \"status\": \"ok\", \"lab\": \"L7\" }"
        ),
        "assignment_steps": [
            "1. Have val_metrics.json and error_analysis.md available.",
            "2. Paste the prompt into Claude Code.",
            "3. Read the output: did it violate any MUST NOT on the first run?",
            "4. Compare to the Before-prompt output — what did the constraints change?",
        ],
        "lab_folder": "Extension07",
        "artifact_paths": [
            "Extension07/work/L7_clinical_translation.md",
            "Extension07/work/status.json",
        ],
        "legacy_artifact_paths": [
            "lecture-repo/reports/extensions/L7_clinical_translation.md",
            "lecture-repo/outputs/extensions/L7/status.json",
        ],
        "reflection_questions": [
            "Did Claude violate any MUST NOT constraint on the first run? Which ones?",
            "Why does a radiologist need a different document than an ML engineer?",
            "Name a clinical AI communication failure that honesty constraints could have prevented.",
        ],
        "responsible_use": "Clinical AI briefings that reach patient-facing contexts must be reviewed by clinical professionals. A Claude-generated briefing is a starting draft.",
        "extension": "Write the same result for four audiences: ML abstract, clinical briefing, grant committee, patient information sheet. What stays constant?",
        "further_learning": [
            ("Clinical Communication", [
                "Search: 'plain language medical research writing guidelines'",
                "Search: 'DECIDE-AI reporting guidelines AI clinical decision support'",
                "Search: 'TRIPOD-AI transparent reporting AI prediction models 2024'",
            ]),
        ],
        "diagram": None,
        "handout_path": "lecture-repo/handouts/optional_L7_clinical_translation.md",
        "guide_path": "lecture-repo/modules/extensions/L7_clinical_translation/README.md",
    },
    {
        "id": "L8",
        "type": "extension",
        "nav_label": "Research Memory & Handoff",
        "title": "Research Memory & Handoff",
        "subtitle": "Making a 3-year project recoverable at month 18",
        "lab_question": "How do I maintain research continuity across months, collaborators, and Claude sessions?",
        "short_description": "Design an evolving CLAUDE.md, write a structured project handoff document, create a decision log.",
        "estimated_time": "35 min",
        "day": "Day 2",
        "clinical_bottleneck": "Long PhD projects lose context across months. Future you — or a new collaborator — cannot reconstruct why decisions were made, what was tried, or what the current status is.",
        "agentic_concept": "Project memory and research continuity. CLAUDE.md as an evolving knowledge base updated at each milestone. Decision logs that capture 'why', not just 'what'. Structured handoff documents for any future collaborator or Claude session.",
        "how_this_differs": None,
        "before_prompt": "Claude, can you summarise what this project is about and what we've done so far?",
        "after_prompt": (
            "First confirm you are working from the repository root.\n\n"
            "Read CLAUDE.md, reports/*.md, git log (if available).\n\n"
            "Write reports/extensions/L8_research_memory.md:\n\n"
            "1. Project identity: clinical problem, method, research question\n"
            "2. Current status: complete / in progress / blocked\n"
            "3. Key decisions (decision log): Decision | Rationale | Rejected alternatives\n"
            "4. Known failure modes and open questions\n"
            "5. How to resume: exact steps for a new team member\n"
            "6. CLAUDE.md update recommendations\n\n"
            "Write to outputs/extensions/L8/status.json: { \"status\": \"ok\", \"lab\": \"L8\" }"
        ),
        "assignment_steps": [
            "1. Complete at least L0 and L5 before running this lab.",
            "2. Paste the prompt into Claude Code.",
            "3. Read the decision log — did it capture the actual decisions made in this course?",
            "4. Write one concrete addition to CLAUDE.md based on what you learned.",
        ],
        "lab_folder": "Extension08",
        "artifact_paths": [
            "Extension08/work/L8_research_memory.md",
            "Extension08/work/status.json",
        ],
        "legacy_artifact_paths": [
            "lecture-repo/reports/extensions/L8_research_memory.md",
            "lecture-repo/outputs/extensions/L8/status.json",
        ],
        "reflection_questions": [
            "What decision from this course would be hardest to reconstruct without your memory of it?",
            "How would you design a CLAUDE.md that remains useful six months from now?",
            "What is the difference between a git commit message and a decision log entry?",
        ],
        "responsible_use": "Handoff documents may contain sensitive information about research subjects or unpublished results. Treat them with the same confidentiality as other research records.",
        "extension": "Design a CLAUDE.md template for a new project in your own domain. What are the 10 most important things a new Claude session needs to know?",
        "further_learning": [
            ("Research Documentation", [
                "Search: 'electronic lab notebook research reproducibility best practices'",
                "Search: 'git commit message conventions scientific software'",
                "Search PubMed: 'research data management clinical AI reproducibility'",
            ]),
        ],
        "diagram": None,
        "handout_path": "lecture-repo/handouts/optional_L8_research_memory_handoff.md",
        "guide_path": "lecture-repo/modules/extensions/L8_research_memory_handoff/README.md",
    },
]

ALL_LABS = CORE_LABS + EXTENSION_LABS
LAB_BY_NAV = {lab["nav_label"]: lab for lab in ALL_LABS}

# ─── Navigation state ──────────────────────────────────────────────────────────

if "page" not in st.session_state:
    st.session_state.page = "🏠 Welcome"

def goto(label: str):
    st.session_state.page = label

# ─── Completion helpers ─────────────────────────────────────────────────────────

def lab_complete(lab: dict) -> bool:
    for p in lab.get("artifact_paths", []):
        if (BASE / p).exists():
            return True
    for p in lab.get("legacy_artifact_paths", []):
        if (BASE / p).exists():
            return True
    return False

def capstone_complete() -> bool:
    return lab_complete(CAPSTONE)

def count_core_complete() -> int:
    return sum(1 for lab in CORE_LABS if lab_complete(lab))

def submission_status(lab_folder: str) -> dict:
    sub_name = f"{lab_folder}Submission"
    sub = BASE / sub_name
    status_json = load_json(f"{sub_name}/status.json")
    return {
        "dir": sub.exists(),
        "submission_md": (sub / "submission.md").exists(),
        "status_json": status_json,
        "manifest": (sub / "evidence_manifest.json").exists(),
        "ready": bool(status_json.get("ready_for_review")) if status_json else False,
        "sub_name": sub_name,
    }

# ─── Sidebar ───────────────────────────────────────────────────────────────────

def _nav_btn(label: str):
    is_active = st.session_state.page == label
    key = f"nav__{label[:40].replace(' ', '_').replace('/', '_').replace('—', '_').replace('→', '')}"
    if st.sidebar.button(label, key=key, use_container_width=True,
                          type="primary" if is_active else "secondary"):
        goto(label)
        st.rerun()

n_done = count_core_complete()
with st.sidebar:
    st.markdown(
        '<span class="sidebar-wordmark">Agentic Clinical<br>Research Studio</span>'
        '<span class="sidebar-tagline">Lab Studio</span>',
        unsafe_allow_html=True,
    )
    st.progress(n_done / max(len(CORE_LABS), 1))
    st.markdown(
        f'<span class="sidebar-progress-text">{n_done} / {len(CORE_LABS)} core labs</span>',
        unsafe_allow_html=True,
    )
    st.divider()
    st.markdown('<span class="nav-section">Course</span>', unsafe_allow_html=True)
    _nav_btn("🏠 Welcome")
    _nav_btn("🚀 How to Start")
    st.markdown('<span class="nav-section">Core Labs</span>', unsafe_allow_html=True)
    for lab in CORE_LABS:
        _nav_btn(lab["nav_label"])
    st.markdown('<span class="nav-section">Final</span>', unsafe_allow_html=True)
    _nav_btn(CAPSTONE["nav_label"])
    st.markdown('<span class="nav-section">Extensions</span>', unsafe_allow_html=True)
    for lab in EXTENSION_LABS:
        _nav_btn(lab["nav_label"])
    st.markdown('<span class="nav-section">Monitor</span>', unsafe_allow_html=True)
    _nav_btn("📊 Progress & Artifacts")
    _nav_btn("📚 Resources")

# ─── Page renderers ─────────────────────────────────────────────────────────────

def render_welcome() -> None:
    st.markdown(
        '<div class="hero">'
        '<div class="hero-eye">Agentic Clinical Research Studio</div>'
        '<div class="hero-title">Clinical research with Claude as a systematic collaborator.</div>'
        '<div class="hero-body">'
        'Six core labs. One capstone. Three extensions. '
        'Learn to use Claude, VS Code, GitHub, Skills, and agentic workflows '
        'to turn clinical research bottlenecks into traceable, verifiable artifacts.'
        '</div></div>',
        unsafe_allow_html=True,
    )

    all_arts = [p for lab in ALL_LABS for p in lab["artifact_paths"]]
    present  = sum(1 for p in all_arts if (BASE / p).exists())
    n_done   = count_core_complete()
    c1, c2, c3 = st.columns(3)
    c1.metric("Core Labs", f"{n_done} / {len(CORE_LABS)}")
    c2.metric("Artifacts Created", str(present))
    next_lab = next((lab for lab in CORE_LABS if not lab_complete(lab)), None)
    c3.metric("Up Next", next_lab["id"] if next_lab else ("Capstone" if not capstone_complete() else "All done ✓"))

    st.divider()
    st.markdown("## How the course works")
    st.markdown(
        '<div class="flow-diagram">'
        '<div class="flow-step"><div class="flow-num">1</div><div class="flow-title">Read the lesson</div><div class="flow-body">Open a lab in the sidebar. Read the concept, clinical scenario, and before/after prompt comparison.</div></div>'
        '<div class="flow-step"><div class="flow-num">2</div><div class="flow-title">Copy the prompt</div><div class="flow-body">Each lab shows an After prompt. Copy it into Claude Code in VS Code.</div></div>'
        '<div class="flow-step"><div class="flow-num">3</div><div class="flow-title">Claude executes</div><div class="flow-body">Claude reads the repo, runs the workflow, and writes the output files.</div></div>'
        '<div class="flow-step"><div class="flow-num">4</div><div class="flow-title">Inspect & judge</div><div class="flow-body">Read the artifact. Is it correct? Honest? Does it answer the research question?</div></div>'
        '<div class="flow-step"><div class="flow-num">5</div><div class="flow-title">Commit & continue</div><div class="flow-body">Commit to git. Your instructor monitors progress through the commit history.</div></div>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.divider()
    st.markdown("## Course map")
    rows = ""
    for lab in CORE_LABS:
        done = lab_complete(lab)
        bc = "done" if done else "core"
        rows += (
            f'<tr><td><span class="type-badge {bc}">{"✓" if done else "○"} {h(lab["id"])}</span></td>'
            f'<td><strong>{h(lab["title"])}</strong></td>'
            f'<td style="font-style:italic;color:#6B7280">{h(lab["lab_question"])}</td>'
            f'<td style="white-space:nowrap">{h(lab["estimated_time"])}</td></tr>'
        )
    st.markdown(
        f'<table class="syllabus-table"><thead><tr><th>Lab</th><th>Title</th><th>Question</th><th>Time</th></tr></thead>'
        f'<tbody>{rows}</tbody></table>',
        unsafe_allow_html=True,
    )
    cap_done = capstone_complete()
    ext_rows = (
        f'<tr><td><span class="type-badge {"done" if cap_done else "capstone"}">{"✓" if cap_done else "○"} CAP</span></td>'
        f'<td><strong>Capstone Mini-Project</strong></td><td style="font-style:italic;color:#6B7280">Apply the full workflow to your own research problem</td><td>60 min</td></tr>'
    ) + "".join(
        f'<tr><td><span class="type-badge {"done" if lab_complete(l) else "ext"}">{"✓" if lab_complete(l) else "○"} {h(l["id"])}</span></td>'
        f'<td>{h(l["title"])}</td><td style="font-style:italic;color:#6B7280">{h(l["lab_question"])}</td><td style="white-space:nowrap">{h(l["estimated_time"])}</td></tr>'
        for l in EXTENSION_LABS
    )
    st.markdown(
        f'<table class="syllabus-table" style="margin-top:8px"><thead><tr><th>Lab</th><th>Title</th><th>Question</th><th>Time</th></tr></thead>'
        f'<tbody>{ext_rows}</tbody></table>',
        unsafe_allow_html=True,
    )

    st.divider()
    st.markdown(
        '<div class="callout callout-blue">'
        '<div class="callout-label">Start here</div>'
        '<div class="callout-body">'
        'New? Go to <strong>How to Start</strong> in the sidebar. '
        'After setup, begin with <strong>L0 — Welcome to Agentic Clinical Research</strong>.'
        '</div></div>',
        unsafe_allow_html=True,
    )


def render_how_to_start() -> None:
    st.title("How to Start")
    st.markdown("_Five steps. Steps 1–3 are one-time setup. After that, everything runs from Claude Code._")
    st.divider()
    start_text = read_text("START_HERE.md")
    if start_text:
        st.markdown(start_text)
    else:
        st.warning("START_HERE.md not found. Please check the repository root.")


def render_lab_page(lab: dict) -> None:
    done   = lab_complete(lab)
    is_ext = lab["type"] == "extension"
    eyebrow = "Extension Lab" if is_ext else f"Core Lab · {lab['day']} · {lab['estimated_time']}"

    st.markdown(
        f'<div class="lab-header">'
        f'<div class="lab-eyebrow">{h(eyebrow)}</div>'
        f'<div class="lab-title">{h(lab["title"])}</div>'
        f'<div class="lab-question">{h(lab["lab_question"])}</div>'
        f'<div class="chip-row">'
        f'<span class="chip">{h(lab["id"])}</span>'
        f'<span class="chip">⏱ {h(lab["estimated_time"])}</span>'
        + ('<span class="chip complete">✓ Complete</span>' if done else "")
        + ('<span class="chip ext">Extension</span>' if is_ext else "")
        + '</div></div>',
        unsafe_allow_html=True,
    )

    t_lesson, t_assign, t_arts, t_reflect, t_learn = st.tabs([
        "📖 Lesson", "✏️ Assignment", "📁 Artifacts", "💭 Reflection", "📚 Further Learning"
    ])

    # ── LESSON ────────────────────────────────────────────────────────────────
    with t_lesson:
        handout_text = read_text(lab["handout_path"]) if lab.get("handout_path") else None
        if handout_text:
            st.markdown(handout_text)
        else:
            st.markdown("## The Clinical Problem")
            st.markdown(
                f'<div class="callout callout-blue"><div class="callout-label">Clinical Bottleneck</div>'
                f'<div class="callout-body">{h(lab["clinical_bottleneck"])}</div></div>',
                unsafe_allow_html=True,
            )
            st.markdown("## The Agentic Concept")
            st.markdown(
                f'<div class="callout callout-dark"><div class="callout-label">{h(lab["id"])} — Core Concept</div>'
                f'<div class="callout-body">{h(lab["agentic_concept"]).replace(chr(10), "<br>")}</div></div>',
                unsafe_allow_html=True,
            )
            if lab.get("how_this_differs"):
                st.markdown(
                    f'<div class="callout callout-amber"><div class="callout-label">How this differs from previous labs</div>'
                    f'<div class="callout-body">{h(lab["how_this_differs"])}</div></div>',
                    unsafe_allow_html=True,
                )

        st.markdown("## Prompt Comparison")
        st.markdown("_The Before prompt is how most people start. The After prompt applies the concept._")
        st.markdown(
            f'<div class="ba-pair">'
            f'<div class="ba-card before"><div class="ba-label">Without this principle</div>'
            f'<div class="ba-prompt">{h(lab["before_prompt"])}</div></div>'
            f'<div class="ba-card after"><div class="ba-label">With this principle applied</div>'
            f'<div class="ba-prompt">{h(lab["after_prompt"])}</div></div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        if lab.get("diagram"):
            st.markdown("## Workflow Diagram")
            st.markdown(
                '<div class="diagram-block"><div class="diagram-label">Mermaid syntax — paste at mermaid.live to visualise interactively</div></div>',
                unsafe_allow_html=True,
            )
            st.code(lab["diagram"], language="text")
        if lab.get("responsible_use"):
            st.markdown(
                f'<div class="callout callout-red" style="margin-top:20px">'
                f'<div class="callout-label">Responsible Use</div>'
                f'<div class="callout-body">{h(lab["responsible_use"])}</div></div>',
                unsafe_allow_html=True,
            )

    # ── ASSIGNMENT ────────────────────────────────────────────────────────────
    with t_assign:
        st.markdown("## What to do")
        steps_html = "<br>".join(h(s) for s in lab["assignment_steps"])
        st.markdown(
            f'<div class="callout callout-green"><div class="callout-label">Assignment steps</div>'
            f'<div class="callout-body">{steps_html}</div></div>',
            unsafe_allow_html=True,
        )
        if lab.get("extension"):
            st.markdown("## Extension challenge _(optional)_")
            st.markdown(
                f'<div class="callout callout-amber"><div class="callout-label">Extension</div>'
                f'<div class="callout-body">{h(lab["extension"])}</div></div>',
                unsafe_allow_html=True,
            )
        guide_text = read_text(lab["guide_path"]) if lab.get("guide_path") else None
        if guide_text:
            with st.expander(f"📖 Module guide: {lab.get('guide_path', '')}"):
                st.markdown(guide_text)

        st.divider()
        st.markdown("## 📦 Finish this Lab")
        lf = lab.get("lab_folder", lab["id"])
        sub = submission_status(lf)
        sub_dir = sub["sub_name"]
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Work folder", f"{lf}/work/")
        col2.metric("submission.md", "✓ Found" if sub["submission_md"] else "○ Missing")
        col3.metric("Packaged", "✓ Yes" if sub["status_json"] else "○ No")
        col4.metric("Ready for review", "✓ Yes" if sub["ready"] else "○ No")
        st.markdown(
            f'<div class="callout callout-green"><div class="callout-label">How to finish this lab</div>'
            f'<div class="callout-body">'
            f'<strong>You do not manually package submissions.</strong> Claude does that.<br><br>'
            f'1. Do all lab work inside <code>{lf}/work/</code><br>'
            f'2. Open <code>lecture-repo/prompts/finish_lab.md</code> in VS Code<br>'
            f'3. Paste its entire contents into Claude Code<br>'
            f'4. Claude will read your work in <code>{lf}/work/</code><br>'
            f'5. Claude will package evidence into <code>{sub_dir}/</code><br>'
            f'6. Claude will draft <code>{sub_dir}/submission.md</code> based on your actual work<br>'
            f'7. You review and confirm Claude\'s draft<br>'
            f'8. Claude asks before committing — you decide when to push'
            f'</div></div>',
            unsafe_allow_html=True,
        )
        if not sub["dir"]:
            st.info(
                f"Not yet packaged. Complete your work in `{lf}/work/`, "
                f"then paste `lecture-repo/prompts/finish_lab.md` into Claude Code."
            )

    # ── ARTIFACTS ─────────────────────────────────────────────────────────────
    with t_arts:
        st.markdown("## Required artifacts")
        st.caption("Commit these files to git after completing the lab.")
        for p in lab["artifact_paths"]:
            ex = (BASE / p).exists()
            sc = "done" if ex else "missing"
            tag = "✓ Created" if ex else "○ Missing"
            st.markdown(
                f'<div class="artifact-row">'
                f'<div class="artifact-dot {sc}"></div>'
                f'<div class="artifact-path">{h(p)}</div>'
                f'<div class="artifact-tag {sc}">{tag}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
            if ex:
                pth = BASE / p
                if p.endswith(".json"):
                    data = load_json(p)
                    if data:
                        with st.expander(f"Preview {pth.name}"):
                            st.json(data)
                elif p.endswith(".md"):
                    content = read_text(p)
                    if content:
                        with st.expander(f"Preview {pth.name}"):
                            st.markdown(content[:2000] + ("…" if len(content) > 2000 else ""))
        legacy = lab.get("legacy_artifact_paths", [])
        if legacy:
            with st.expander("Legacy paths (also count toward completion)"):
                for p in legacy:
                    ex = (BASE / p).exists()
                    st.markdown(f"{'✅' if ex else '○'} `{p}`")

    # ── REFLECTION ────────────────────────────────────────────────────────────
    with t_reflect:
        st.markdown("## Reflection questions")
        st.markdown("_Include your answers in your lab report to satisfy the reflection requirement._")
        for i, q in enumerate(lab["reflection_questions"]):
            st.markdown(
                f'<div class="reflection-item">'
                f'<div class="reflection-num">Question {i+1}</div>'
                f'<div class="reflection-q">{h(q)}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

    # ── FURTHER LEARNING ──────────────────────────────────────────────────────
    with t_learn:
        st.markdown("## Further Learning")
        st.markdown(
            "_Curated starting points for going deeper. "
            "Suggested search terms are used where exact URLs may change; "
            "stable URLs are included where verified._"
        )
        for category, items in lab.get("further_learning", []):
            items_html = "".join(f'<div class="learn-item">→ {h(item)}</div>' for item in items)
            st.markdown(
                f'<div class="learn-section"><div class="learn-category">{h(category)}</div>{items_html}</div>',
                unsafe_allow_html=True,
            )


def render_capstone_page() -> None:
    cap_done = capstone_complete()
    st.markdown(
        f'<div class="capstone-hero">'
        f'<div class="capstone-title">Capstone Mini-Project</div>'
        f'<div class="capstone-sub">'
        f'{h(CAPSTONE["lab_question"])} · 60 min · Day 2 · {"Complete ✓" if cap_done else "Pending"}'
        f'</div></div>',
        unsafe_allow_html=True,
    )
    handout_text = read_text(CAPSTONE.get("handout_path", "")) if CAPSTONE.get("handout_path") else None
    if handout_text:
        st.markdown(handout_text)
    else:
        st.markdown("""
## Overview

An independent mini-project applying at least three course concepts in an integrated agentic workflow.
You define the clinical question, design the workflow, produce the artifacts, and present to a non-ML audience.

**You are not graded on model performance.** You are graded on workflow clarity, artifact quality,
human judgment, and responsible use.

## Three tiers

| Tier | Concepts | Focus |
|------|----------|-------|
| Basic | 3+ (prompt contract + stakeholder review + artifact output) | Clarity of workflow |
| Medium | 4+ (+ literature skill or tool workflow) | Methodology section |
| Advanced | 5+ (+ subagent workflow + clinical translation or handoff) | Full workflow documentation |

## Grading dimensions

1. Problem definition and clinical relevance
2. Workflow clarity and prompt craft
3. Artifact quality and completeness
4. Human judgment (do you evaluate, not just produce?)
5. Responsible use awareness
6. Showcase clarity for a non-ML audience
""")
        st.info("A capstone that honestly documents failure scores higher than one that reports improvement without explanation.")
    st.markdown("### Required artifacts")
    for p in CAPSTONE["artifact_paths"]:
        ex = (BASE / p).exists()
        sc = "done" if ex else "missing"
        tag = "✓ Created" if ex else "○ Missing"
        st.markdown(
            f'<div class="artifact-row">'
            f'<div class="artifact-dot {sc}"></div>'
            f'<div class="artifact-path">{h(p)}</div>'
            f'<div class="artifact-tag {sc}">{tag}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
    guide_text = read_text(CAPSTONE.get("guide_path", "")) if CAPSTONE.get("guide_path") else None
    if guide_text:
        with st.expander("📖 Full capstone guide"):
            st.markdown(guide_text)


def render_progress() -> None:
    n_done   = count_core_complete()
    cap_done = capstone_complete()
    st.title("Progress & Artifacts")
    st.caption("Computed live from the filesystem. Commit artifacts to git to record progress.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Core Labs", f"{n_done} / {len(CORE_LABS)}")
    c2.metric("Capstone", "Done ✓" if cap_done else "Pending")
    all_arts = [p for lab in ALL_LABS for p in lab["artifact_paths"]]
    present  = sum(1 for p in all_arts if (BASE / p).exists())
    c3.metric("Artifacts Present", f"{present} / {len(all_arts)}")
    if n_done > 0:
        st.progress(n_done / len(CORE_LABS))
    st.divider()
    st.markdown("### Core Labs")
    for lab in CORE_LABS:
        done = lab_complete(lab)
        sc = "done" if done else "missing"
        st.markdown(
            f'<div class="prog-row"><div class="prog-dot {sc}"></div>'
            f'<div class="prog-id">{h(lab["id"])}</div>'
            f'<div class="prog-title">{h(lab["title"])}</div>'
            f'<div class="prog-status {sc}">{"Complete" if done else "Pending"}</div></div>',
            unsafe_allow_html=True,
        )
    sc = "done" if cap_done else "missing"
    st.markdown(
        f'<div class="prog-row"><div class="prog-dot {sc}"></div>'
        f'<div class="prog-id">CAP</div>'
        f'<div class="prog-title">Capstone Mini-Project</div>'
        f'<div class="prog-status {sc}">{"Complete" if cap_done else "Pending"}</div></div>',
        unsafe_allow_html=True,
    )
    st.divider()
    st.markdown("### Extension Labs")
    for lab in EXTENSION_LABS:
        done = lab_complete(lab)
        sc = "done" if done else "missing"
        st.markdown(
            f'<div class="prog-row"><div class="prog-dot {sc}"></div>'
            f'<div class="prog-id">{h(lab["id"])}</div>'
            f'<div class="prog-title">{h(lab["title"])}</div>'
            f'<div class="prog-status {sc}">{"Complete" if done else "Optional"}</div></div>',
            unsafe_allow_html=True,
        )
    st.divider()
    st.markdown("### Submission packages")
    st.caption("Work in `LabXX/work/` → Finish Lab prompt → `LabXXSubmission/` → GitHub checks.")
    for lab in CORE_LABS:
        lf = lab.get("lab_folder", lab["id"])
        sub = submission_status(lf)
        if sub["ready"]:
            icon, color = "✅", "done"
        elif sub["dir"]:
            icon, color = "🔶", "missing"
        else:
            icon, color = "○", "missing"
        st.markdown(
            f'<div class="prog-row"><div class="prog-dot {color}"></div>'
            f'<div class="prog-id">{h(lab["id"])}</div>'
            f'<div class="prog-title">{icon} {lf}/ → {lf}Submission/</div>'
            f'<div class="prog-status {color}">{"Ready" if sub["ready"] else ("Started" if sub["dir"] else "Not packaged")}</div></div>',
            unsafe_allow_html=True,
        )
    st.divider()
    st.markdown("### All artifacts")
    for lab in ALL_LABS:
        with st.expander(f"{lab['id']} — {lab['title']}"):
            for p in lab["artifact_paths"]:
                ex = (BASE / p).exists()
                st.markdown(f"{'✅' if ex else '○'} `{p}`")
    st.info("**Commit your artifacts after each lab.** Your instructor monitors progress through the GitHub commit history.")


def render_resources() -> None:
    st.title("Resources")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Course documents")
        for path, desc in [
            ("START_HERE.md", "First student instruction"),
            ("ASSIGNMENT.md", "Full assignment and grading spec"),
            ("CLAUDE.md", "Project contract for Claude Code"),
            ("lecture-repo/handouts/README.md", "Handout index"),
        ]:
            st.markdown(f"{'📄' if exists(path) else '○'} **`{path}`** — {desc}")
        st.markdown("### Handouts")
        handout_dir = BASE / "lecture-repo" / "handouts"
        if handout_dir.exists():
            for f in sorted(handout_dir.glob("*.md")):
                if f.name != "README.md":
                    st.markdown(f"📖 `lecture-repo/handouts/{f.name}`")
        st.markdown("### Prompts")
        prompt_dir = BASE / "lecture-repo" / "prompts"
        if prompt_dir.exists():
            for f in sorted(prompt_dir.glob("*.md")):
                st.markdown(f"📝 `lecture-repo/prompts/{f.name}`")
    with c2:
        st.markdown("### Module guides")
        guides = [
            ("lecture-repo/modules/L0_agentic_studio/README.md", "L0"),
            ("lecture-repo/modules/L1_prompt_contracts/README.md", "L1"),
            ("lecture-repo/modules/L2_multi_stakeholder_review/README.md", "L2"),
            ("lecture-repo/modules/L3_literature_search_skills/README.md", "L3"),
            ("lecture-repo/modules/L4_tool_mcp_workflows/README.md", "L4"),
            ("lecture-repo/modules/L5_subagent_workflow/README.md", "L5"),
            ("lecture-repo/modules/capstone/README.md", "Capstone"),
            ("lecture-repo/modules/extensions/L6_controlled_experiments/README.md", "L6"),
            ("lecture-repo/modules/extensions/L7_clinical_translation/README.md", "L7"),
            ("lecture-repo/modules/extensions/L8_research_memory_handoff/README.md", "L8"),
        ]
        for path, label in guides:
            st.markdown(f"{'📖' if exists(path) else '○'} {label}: `{path}`")
    st.divider()
    st.markdown("### Run commands")
    st.code("""make dashboard         # opens dashboard at http://localhost:8501
make preflight         # structural checks — safe to run anytime
make progress          # show current lab progress (always succeeds)
make package LAB=Lab03 # package Lab03 → Lab03Submission/ (Claude runs this)
make grade             # strict grading check (instructor / CI)""", language="bash")
    st.divider()
    st.markdown("**gs@cercare-medical.com** — questions, setup issues, feedback")

# ─── Router ─────────────────────────────────────────────────────────────────────

page = st.session_state.page
if page == "🏠 Welcome":
    render_welcome()
elif page == "🚀 How to Start":
    render_how_to_start()
elif page == CAPSTONE["nav_label"]:
    render_capstone_page()
elif page == "📊 Progress & Artifacts":
    render_progress()
elif page == "📚 Resources":
    render_resources()
elif page in LAB_BY_NAV:
    render_lab_page(LAB_BY_NAV[page])
else:
    render_welcome()
