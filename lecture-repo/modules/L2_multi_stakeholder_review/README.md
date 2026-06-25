# L2 — Multi-Stakeholder Review

**Concept:** Role prompting, stakeholder simulation, synthesis of competing perspectives
**Time:** 50 min · Day 1
**Prompt file:** `prompts/stage_07_challenge_plan.md`

---

## 1. Overview

Clinical research does not answer to a single constituency. A brain tumour segmentation method that satisfies a radiologist may concern a biostatistician. A result that excites a translational scientist may alarm a clinical ethicist. A metric that looks acceptable to an ML engineer may be clinically meaningless to a neuro-oncologist. Yet most agentic workflows collapse all of these perspectives into a single voice — the voice of the agent asked to assess work it helped produce.

This lab teaches investigators to use role prompting to simulate multiple expert stakeholders in sequence, then to deliberately synthesize their competing critiques into a single structured research judgment. The goal is not to find a consensus that satisfies everyone. It is to surface the genuine tensions between legitimate perspectives — and to make those tensions legible to the investigator, so they can be resolved through empirical work rather than overlooked.

---

## 2. Learning Objectives

- Write role prompts precise enough to produce perspective-specific critique, not generic hedging
- Elicit at least three structurally distinct stakeholder viewpoints from a single research artifact
- Identify where stakeholder perspectives conflict, where they converge, and what those conflicts imply for the next research step
- Produce a synthesis document that is honest about unresolved disagreements rather than smoothing them away

---

## 3. Clinical Bottleneck

Translational failure in medical AI is rarely caused by technical incompetence. It is caused by perspective blindness — the tendency of research teams to optimize for the criteria their own discipline finds legible while remaining unaware of criteria that are legible to other disciplines.

A method with strong Dice coefficients can fail translation because:
- The radiologist was not consulted on which anatomical structures matter clinically
- The biostatistician was not asked whether the validation set was representative
- The clinical deployment engineer was never shown the inference latency under realistic hospital IT constraints
- The ethics reviewer was never given the opportunity to examine demographic subgroup performance

Each of these failures is a failure of perspective, not analysis. The problem is not that the investigators lacked the information — it is that no one in the workflow occupied the role that would have prompted them to ask for it.

Agentic workflows can reproduce this failure at scale and speed: a well-instructed single-role agent will produce confident, internally consistent critiques that are nonetheless one-dimensional. Multi-stakeholder simulation is a structural remedy, not a cosmetic one.

---

## 4. Agentic Concept: Role Prompting and Perspective Synthesis

**Role prompting** is the practice of assigning Claude an explicit expert identity before asking it to evaluate a research artifact. The identity specification does three things:

1. **Shifts the prior** — a clinical deployment engineer and a biostatistician approach the same Dice score with different baseline assumptions about what it means for a method to be "ready."
2. **Activates domain vocabulary** — when Claude is told it is a regulatory affairs specialist, it draws on a different body of knowledge than when it is told it is an ML researcher. The constraint is productive, not limiting.
3. **Breaks symmetry** — a single balanced assessment tends toward the middle. Multiple role-specific assessments can diverge sharply. That divergence is information.

**Stakeholder simulation** is the full pattern: generating N role-specific assessments of the same artifact, then comparing them. The comparison step is essential. Without it, you have N parallel monologues. With it, you have a structured map of where experts agree (the findings you can rely on), where they disagree (the findings that require further evidence to resolve), and where one stakeholder identifies a risk that no other stakeholder raised (the blind spot the team was most likely to miss).

**Perspective synthesis** is the final step: writing a single document that explicitly names the convergences, names the conflicts, and proposes a research path that addresses the most consequential unresolved tensions. A good synthesis does not pretend the conflicts were resolved. It maps them precisely enough that an empirical study could, in principle, settle them.

The critical craft skill in this lab is writing role prompts that are specific enough to produce genuine divergence. "Act as a clinician" produces a clinician-flavored version of whatever Claude was already going to say. "You are a consultant neuro-oncologist reviewing whether this segmentation boundary precision is sufficient to support surgical planning in eloquent cortex adjacent tumours" produces a perspective that cannot be generated by any other role specification in the set.

---

## 5. Before / After

**Before:**
```
Review my brain segmentation model results from multiple perspectives and tell me
what different stakeholders would think.
```

Claude produces a polite, symmetrical summary. The "clinician" sounds like the "statistician" sounds like the "ethicist" — all speak in the same hedged, balanced register. The conflicts between disciplines are absent because the prompt did not force them to be present. The output is not wrong; it is merely shallow.

**After:**
```
You are running a multi-stakeholder review of a brain tumour segmentation prototype.
Read outputs/metrics/val_metrics.json and reports/train_notes.md.

Conduct THREE sequential stakeholder reviews, each from a distinct expert identity.
Do not let the identities bleed into each other.

STAKEHOLDER 1 — Neuro-oncology consultant:
  Your concern is clinical utility at the point of care.
  Assume the Dice coefficient was not designed for your use case.
  Assess: would you trust this segmentation for surgical margin planning?
  Identify: what specific additional evidence would change your assessment?

STAKEHOLDER 2 — Biostatistician (clinical trial protocol review):
  Your concern is the validity of the evidence base.
  Assess: what claims does this validation design support, and which does it not?
  Identify: what methodological changes are required before a publication claim could be made?

STAKEHOLDER 3 — Clinical AI governance officer:
  Your concern is deployment risk and oversight requirements.
  Assess: what failure modes would require human override, and how are they currently detected?
  Identify: what governance conditions must be in place before this method enters any clinical workflow?

After all three reviews:
Write a SYNTHESIS section that names:
  - Two points where all three stakeholders agree
  - Two points where stakeholders disagree, and what evidence would resolve each
  - The single most consequential unresolved tension

Write the full multi-stakeholder review to reports/lab_02_multi_stakeholder_review.md.
Write status to outputs/status/lab_02_multi_stakeholder_review.json with key: status="ok".
```

The second prompt forces genuine perspective differentiation by anchoring each role to a concrete concern that cannot be addressed by the other roles. The synthesis section makes the conflict map explicit rather than implicit.

---

## 6. Assignment

1. Confirm that `outputs/metrics/val_metrics.json` and `reports/train_notes.md` exist. If the training pipeline has not run, use the stub files provided in `reports/` — the prompt works on stubs, and the learning objective is in the role structure, not the metrics values.

2. Read the full prompt in the After section above. Before running it, write down your own prediction: where do you expect the three stakeholders to disagree most sharply?

3. Paste the prompt into Claude Code and run it. Read each stakeholder section carefully before reading the synthesis.

4. Evaluate the synthesis: does it name real conflicts, or does it smooth them away? If you think a conflict was under-stated, revise the relevant role prompt and re-run that section.

5. Add a brief investigator response at the end of `reports/lab_02_multi_stakeholder_review.md`: which conflict do you consider most important, and what is the minimum experiment needed to resolve it?

6. Verify both required artifacts exist and the JSON status file is well-formed.

7. Answer the reflection questions below before the group debrief.

---

## 7. Required Artifacts

| Path | Expected Content |
|------|-----------------|
| `outputs/status/lab_02_multi_stakeholder_review.json` | `{"status": "ok", "stakeholders": ["neuro_oncology", "biostatistics", "governance"], "conflicts_identified": <int>}` |
| `reports/lab_02_multi_stakeholder_review.md` | Three role-specific critique sections, a synthesis section naming convergences and conflicts, and an investigator response |

The synthesis section must be written by Claude on the basis of the three stakeholder sections. The investigator response section must be written by the student.

---

## 8. Reflection Questions

1. Did the three stakeholders actually disagree with each other, or did they converge on the same concerns in different language? If they converged, what does that tell you about the role prompts you used — and how would you revise them to force genuine divergence?

2. The synthesis step required Claude to identify a "single most consequential unresolved tension." Do you agree with Claude's choice? What would a different choice imply about which research step should come next?

3. Which stakeholder perspective would be hardest to simulate with a text-based AI agent — and why? What would that stakeholder need to see that is not available in a text document?

---

## 9. Success Criteria

Excellent work in this lab has the following characteristics:

- The three stakeholder sections are genuinely distinct: each raises at least one concern that the other two do not raise
- The synthesis section names specific conflicts, not paraphrases of the individual sections
- The investigator response names a concrete, runnable experiment — not a general statement that "more work is needed"
- `outputs/status/lab_02_multi_stakeholder_review.json` is valid JSON with `status: "ok"` and an accurate `conflicts_identified` count
- The student can explain, in a 90-second verbal summary, what the most important unresolved conflict is and why it matters for translation

Work that does not meet the bar typically has one of two failure modes: role collapse (all three stakeholders sound alike) or synthesis avoidance (the synthesis section lists the three stakeholders' views again rather than mapping the conflicts between them).

---

## 10. Instructor Notes

**Facilitating the group debrief.** The most productive debrief question is: "Did anyone get a synthesis where the three stakeholders disagreed about something the investigator hadn't thought about?" This surfaces cases where the role simulation added genuine epistemic value rather than just repackaging what the student already knew. Ask students to read their most surprising finding aloud.

**Common failure mode — role collapse.** When all three stakeholders sound alike, it is usually because the role specifications were too generic ("a clinician," "a statistician") and did not anchor to a specific professional concern. Coach students to add one concrete sentence per role that names a specific thing the role-holder is accountable for: surgical planning, trial validity, governance documentation. That accountability sentence is what creates genuine divergence.

**Common failure mode — synthesis avoidance.** Students who are uncomfortable with unresolved conflicts tend to write syntheses that restate each stakeholder's position rather than mapping the conflicts between positions. Prompt them: "Which two stakeholders would disagree with each other in a room, and what would each say?" The conflict has to be named explicitly, not implied.

**For advanced students.** Ask them to add a fourth stakeholder the prompt did not specify — a perspective they think is missing from the standard three. What does that reveal about who is typically absent from clinical AI review processes? This extends the exercise into research design territory: who should be in the room?

**Time management.** The three stakeholder sections typically take 15–20 minutes to generate and read carefully. The synthesis step is where students need the most time — allow 10–15 minutes for the investigator response. If the session is running short, the synthesis and investigator response can be completed asynchronously.

**Connection to later labs.** The conflict map generated in this lab is direct input for L3 (Literature Search), where students will search for evidence that resolves specific unresolved tensions identified here. Encourage students to keep their synthesis document open during L3 and treat each conflict as a search question.
