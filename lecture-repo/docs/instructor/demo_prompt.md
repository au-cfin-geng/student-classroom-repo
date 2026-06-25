# Kim's Claude Prompt — Full Lab Demo

## How to use

Open a terminal. Run `claude`. Paste the prompt below. That's it.

Claude will set everything up, run the student pipeline, launch the dashboard,
and then guide you through the course one screen at a time.
You just watch and ask questions.

---

## The Prompt

---

```
I need you to demo the Medical AI + Agentic Coding Lab course to me.
I am Kim — a supervisor reviewing this course before it runs with students.

I have limited time. Please work quickly and decisively.
Do not ask me anything you can figure out yourself.
If you genuinely need a decision from me, ask one short question and wait.

Here is everything you need to know:

  Course repo:    https://github.com/au-cfin-geng/student-classroom-repo
  Instructor repo: https://github.com/au-cfin-geng/teacher-ta-repo
  Tutorial site:  https://au-cfin-geng.github.io/medical-ai-agentic-course-site/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1 — FIND OR CREATE A WORKING DIRECTORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Check these locations in order for an existing clone of student-classroom-repo:
  1. Current directory and its subdirectories (find . -name "student-classroom-repo" -maxdepth 3)
  2. ~/Documents/
  3. ~/Desktop/
  4. ~/

If found: use it. Run git pull to update.
If not found: create ~/medical-ai-lab-demo/ and clone there. No need to ask.

Tell me in one line: "Working in: [path]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2 — CLONE REPOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

In the working directory, clone any repos not already present:

  git clone https://github.com/au-cfin-geng/student-classroom-repo
  git clone https://github.com/au-cfin-geng/teacher-ta-repo

Confirm both exist with their key files. One-line status per repo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3 — ENVIRONMENT SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

In student-classroom-repo/:

Check for .venv/ — if missing, create it now:

  python3 -m venv .venv
  source .venv/bin/activate        # macOS/Linux
  # or: .venv\Scripts\activate     # Windows

Then install:
  pip install --upgrade pip -q
  pip install -r requirements.txt -q

Verify with:
  python3 -c "import numpy, matplotlib, streamlit, nibabel; print('OK')"

If anything fails, diagnose and fix silently. Tell me the result in one line.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 4 — RUN THE FULL STUDENT PIPELINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Activate the venv, then run all of these in sequence.
After each command, read the key output file and print one line summary.
Do not print raw terminal output — only the human-readable insight.

make preflight
→ Tell me: "[N]/12 structural checks passed"

make fetch-sample
→ Tell me: "Downloaded [N] MRI slices from GitHub Releases — [dataset name]"

make visualize
→ Tell me: "Overlay figure saved. [N] slices, ~[X]% tumour voxels (class imbalance noted)"

make smoke-train
→ Tell me: "Baseline Dice = [X] on [N] validation slices.
            In clinical terms: [one sentence — e.g. 'the model finds roughly half the tumour on average']"

make error-analysis
→ Tell me: "Best case Dice = [X] (slice [N]) / Worst case Dice = [X] (slice [N])
            Failure hypothesis: [one sentence from reports/error_analysis.md]"

make model-swap
→ Tell me: "Improvement attempt: Dice [old] → [new] ([+/- delta]).
            [one sentence — was this real improvement or within noise?]"

make pack-report
→ Tell me: "Day 1 summary written. Key finding: [one sentence from reports/day1_summary.md]"

make challenge-plan
→ Tell me: "Research question for Day 2: [exact research question from reports/challenge_plan.md]"

make translation-memo
→ Tell me: "Clinical status: [exact status level from reports/translation_memo.md]
            Stated limitations: [count from the report]"

When all stages are done, print this summary table:

┌─────────────────────────────────────────────────────────┐
│         PIPELINE COMPLETE — KEY RESULTS                  │
├──────────────────┬──────────────────────────────────────┤
│ Baseline Dice    │ [value]                               │
│ Improved Dice    │ [value] ([delta])                     │
│ Best case        │ slice [N], Dice [value]               │
│ Worst case       │ slice [N], Dice [value]               │
│ Clinical status  │ [from translation memo]               │
│ All artifacts    │ [N]/9 stages complete                 │
└──────────────────┴──────────────────────────────────────┘

Then say: "Pipeline done. Launching the dashboard now."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5 — LAUNCH THE DASHBOARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Launch the Streamlit dashboard in the background:

  python -m streamlit run app/streamlit_app.py --server.headless true &

Wait 4 seconds, then verify it is running:
  curl -s -o /dev/null -w "%{http_code}" http://localhost:8501

If status is 200, tell me:

  ┌─────────────────────────────────────────────────────┐
  │  Dashboard is running.                               │
  │                                                      │
  │  Please open this URL in your browser now:           │
  │                                                      │
  │  → http://localhost:8501                             │
  │                                                      │
  │  Tell me when you can see the dashboard.             │
  └─────────────────────────────────────────────────────┘

Wait for my confirmation before continuing.

If port 8501 is busy, try 8502. Adjust the URL accordingly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 6 — GUIDED DASHBOARD TOUR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Once I confirm the dashboard is open, guide me through it.
For each section, tell me what to look at and what it means for the course.
Wait for me to say "next" or "ok" before moving on.

Section A — Mission sidebar (left panel)
  "Look at the left sidebar. You should see missions listed (Mission 0 through 6).
   These are the 7 research missions students complete over 2 days.
   The green checkmarks show completed missions — you should see all checked
   since we just ran the full pipeline.
   Students normally arrive to this dashboard and see all missions locked except the first one."

Section B — Current mission card (main panel)
  "The main panel shows the active mission card. It has:
   - the mission title and scientific goal
   - the Claude / agentic concept taught in this mission
   - the traditional workflow problem it solves
   - the prompt students paste into Claude Code (not here — in VS Code)
   Click through a few missions in the sidebar and notice how each one has
   a different prompt principle highlighted."

Section C — Artifacts tab
  "Click the Artifacts or Outputs tab (the name may vary).
   You should see the figures and metric files we just generated:
   - sample_overlay.png: MRI slice with tumour mask
   - loss_curve.png: training behaviour
   - error_analysis_best.png and error_analysis_worst.png: failure visualisation
   - val_metrics.json: the Dice score
   These are exactly what students produce and submit for grading."

Section D — Reports tab
  "Click to the reports section.
   You should see the written outputs:
   - error_analysis.md: the failure hypothesis
   - challenge_plan.md: the Day 2 research question
   - translation_memo.md: the clinical readiness assessment
   These are assessed by a human — not just the automated tests."

Section E — The pedagogical point
  "What you are seeing is the full student artifact trail:
   pipeline outputs + written reports + metric files.
   Grading runs pytest automatically on the JSON files.
   Human review focuses on the quality of the written reasoning.
   The key assessment question is: does the student understand WHY
   the model fails, not just what the Dice score is."

When done, say: "That's the student dashboard. Ready for the instructor view?"
Wait for my reply.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 7 — INSTRUCTOR MATERIALS (QUICK TOUR)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read each instructor file and give me a 3-sentence highlight.
Do not read them aloud word for word — extract what I actually need to know.

File 1: teacher-ta-repo/docs/instructor/agentic_clinical_ai_teaching_guide.md
Highlight: "Here is what this course is actually trying to teach, and what
instructors must not say..."
[3 sentences]

File 2: teacher-ta-repo/docs/instructor/assessment_rubric_agentic_clinical_ai.md
Highlight: "Assessment has 8 dimensions on 100 points. Here is what is
automated and what requires your judgment..."
[3 sentences — emphasise that Dice score is NOT the primary criterion]

File 3: teacher-ta-repo/docs/instructor/live_classroom_facilitation.md
Highlight: "The most important classroom moments are..."
[2 sentences — include the question to ask after Mission 3]

File 4: teacher-ta-repo/docs/instructor/learning_analytics_research_plan.md
Highlight: "This course is not currently a research study, but here is what
could be studied later..."
[2 sentences]

Then say: "Those are the instructor docs. Want me to open the tutorial website? (yes/skip)"
Wait for my reply.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 8 — TUTORIAL WEBSITE TOUR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

If I say yes:

First, try to open the live website in my browser:
  macOS:   open "https://au-cfin-geng.github.io/medical-ai-agentic-course-site/"
  Linux:   xdg-open "https://..."
  Windows: start "https://..."

Tell me: "The tutorial website is at: https://au-cfin-geng.github.io/medical-ai-agentic-course-site/
I've opened it in your browser. While it loads, here is what it contains:"

Then read these local source files and highlight each in 2-3 sentences.
Local path: [wherever medical-ai-agentic-course-site was cloned, or use teacher-ta-repo docs if site not cloned]

If medical-ai-agentic-course-site is not cloned locally, clone it now:
  git clone https://github.com/au-cfin-geng/medical-ai-agentic-course-site

Page 1: docs/getting-started/course-overview.md
"The site opens with..."

Page 2: docs/agentic-research/prompts-as-experimental-instruments.md
"The most important page in the agentic section explains..."
[walk through the vague-prompt → research-protocol transformation]

Page 3: docs/labs/mission-03-investigate-failure.md
"Each lab page has this structure: [list the 12 sections in one sentence]
Here is what Mission 3 — error analysis — asks students to do..."
[1-2 sentences on the clinical motivation and Claude method]

Page 4: docs/handouts/responsible-clinical-ai-checklist.md
"The site includes printable cheat sheets. This one is for responsible
clinical AI — students use it in Mission 6..."
[read the two checklist sections aloud briefly]

Page 5: docs/readings/anthropic-academy-reading-map.md
"The site maps Anthropic Academy courses to specific lab missions.
It does not reproduce any course content — it only references public titles.
Here is how it is framed: [read the disclaimer + Before-the-course section]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 9 — FINAL VERDICT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Print this summary — be honest and brief:

┌─────────────────────────────────────────────────────────────────┐
│  COURSE READINESS — QUICK VERDICT                                │
├──────────────────────────┬──────────────────────────────────────┤
│ Clone + install          │ ✅ Works on any machine               │
│ Teaching data            │ ✅ Downloads from GitHub Releases     │
│ Full pipeline            │ ✅ Runs end to end, all artifacts     │
│ Dashboard                │ ✅ Launches at localhost:8501         │
│ Tutorial website         │ ✅ Live at GitHub Pages               │
│ Automated grading        │ ✅ [N] tests pass                     │
├──────────────────────────┴──────────────────────────────────────┤
│  WHAT STUDENTS DO IN 2 DAYS                                      │
│                                                                  │
│  Day 0  Preflight: set up environment using one Claude prompt    │
│  Day 1  Missions 0–4: build, evaluate, fail, improve a          │
│         brain tumour segmentation model — all via prompts        │
│  Day 2  Missions 5–6: design next study, write clinical memo     │
│         Showcase: present artifacts + honest failure analysis    │
│                                                                  │
│  WHAT IS DIFFERENT FROM A NORMAL CODING LAB                     │
│                                                                  │
│  • Students write prompts, not code                              │
│  • Every mission teaches a Claude / agentic research concept     │
│  • Grading rewards scientific reasoning, not Dice score          │
│  • Mission 6 explicitly teaches responsible clinical translation │
│                                                                  │
│  ONE THING TO WATCH                                              │
│  Students who try to run make targets without reading the        │
│  prompt files first will miss the pedagogical layer entirely.   │
│  Remind them: read the prompt → paste into Claude Code →        │
│  inspect the artifact → back to dashboard.                      │
└─────────────────────────────────────────────────────────────────┘

Then ask: "Any specific part of the course you want to look at more closely?"
```

---

## What happens when Kim pastes this

| Step | What Claude does | Kim does |
|---|---|---|
| 1–3 | Finds/clones repos, sets up venv silently | Nothing |
| 4 | Runs full pipeline, prints clean summaries | Reads summaries |
| 5 | Launches dashboard | Opens http://localhost:8501 |
| 6 | Guides through dashboard section by section | Clicks around, says "next" |
| 7 | Reads instructor docs, gives 3-sentence highlights | Reads highlights |
| 8 | Opens website, tours 5 key pages | Looks at browser |
| 9 | Prints readiness verdict | Asks questions |

**Total time: ~15 minutes** (most of it is pipeline running, which Claude handles silently)

## Links

- Student repo: https://github.com/au-cfin-geng/student-classroom-repo
- Instructor repo: https://github.com/au-cfin-geng/teacher-ta-repo
- Tutorial website: https://au-cfin-geng.github.io/medical-ai-agentic-course-site/
