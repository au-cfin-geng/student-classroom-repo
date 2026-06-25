# L3 — Literature Search Skills

**Concept:** Structured queries for research synthesis  
**Time:** 35 min · Day 1

---

## Why this lab exists

Literature search is one of the most time-consuming parts of clinical research — finding relevant prior work, comparing methods, identifying gaps. Claude can provide substantial leverage here, but only if you use it correctly.

The core problem with asking Claude to "summarise the literature" is that Claude's training data has a knowledge cutoff, its coverage of recent literature is uneven, and — most importantly — it cannot reliably distinguish between what it knows precisely and what it is extrapolating. An unqualified Claude summary of a literature field will typically mix accurate citations with confident-sounding hallucinations.

This lab teaches a structured approach that addresses the problem directly: require Claude to mark its confidence per entry. An output schema that includes a `Confidence` column — with values `[VERIFIED]`, `[ESTIMATED]`, or `[GAP]` — makes Claude's uncertainty explicit and auditable. You can then verify `[ESTIMATED]` entries yourself, rather than discovering the error in front of a supervisor.

The structured table format has a second benefit: it produces output you can actually use in a grant report, a literature review section, or a methods comparison. A plain paragraph summary must be rewritten into table form anyway. Skip the intermediate step.

---

## The clinical problem this addresses

A researcher asks Claude to summarise brain tumour segmentation literature for a grant application. Claude produces a fluent two-page summary citing seven methods. Three of the citations are inaccurate — wrong years, wrong datasets, one method that doesn't exist. The researcher doesn't discover this until the grant reviewer queries the citations. The credibility damage far exceeds the time the shortcut saved.

---

## Before / After

**Before:**
```
Can you summarise recent brain tumour segmentation methods for me?
```

Claude produces a paragraph summary. The citations are embedded in prose, hard to verify, and mixed with plausible-but-wrong entries. You don't know which claims to trust.

**After:**
```
You are a medical literature analyst.

Create a structured comparison of intensity-based brain tumour segmentation methods.

Required output: a markdown table at reports/lab_03_literature_search.md with columns:
  Method | Year | Dataset | Dice (reported) | Key Limitation | Confidence

Include exactly 5 methods from 2015–2024.

For each entry:
  - Mark [VERIFIED] if you are confident in the citation
  - Mark [ESTIMATED] if you are uncertain
  - Mark [GAP] if you cannot identify a suitable method — do not invent citations

Also write a one-paragraph synthesis at skills/literature_search_skill.md summarising
what makes intensity-based methods fail in practice.

Write status to outputs/status/lab_03_literature_search.json.
```

The second prompt produces a table you can audit. `[ESTIMATED]` entries are your verification queue. `[GAP]` entries tell you where the literature is genuinely sparse (or where Claude's training didn't cover it).

---

## Clinical scenario

You need to situate your brain tumour segmentation baseline in the literature for a grant report section. You have two hours. How do you use Claude to produce a structured synthesis you can actually cite — without risking fabricated references?

---

## Assignment

1. Create the `skills/` directory if it doesn't exist: `mkdir -p skills`
2. Paste the lab prompt into Claude Code.
3. After Claude runs, count how many entries are `[ESTIMATED]` vs `[VERIFIED]`.
4. Manually verify one `[ESTIMATED]` entry using Google Scholar or PubMed. Was Claude accurate?
5. Write your findings in `reports/lab_03_literature_search.md`.

---

## Required artifacts

| Path | Contents |
|------|---------|
| `reports/lab_03_literature_search.md` | Comparison table with 5 methods + confidence column |
| `skills/literature_search_skill.md` | One-paragraph synthesis of intensity-based failure modes |
| `outputs/status/lab_03_literature_search.json` | `status: "ok"` |

---

## Reflection questions

1. How many of the 5 entries were `[ESTIMATED]`? What does that tell you about Claude's knowledge boundary in this domain?
2. When you manually verified one `[ESTIMATED]` entry — was Claude right? What does the error pattern suggest?
3. How would you adapt this workflow for your own PhD research field?

---

## The pattern generalises: Research synthesis prompts

The confidence-marking pattern applies to any synthesis task where Claude's knowledge boundary matters:

| Task | Confidence column labels |
|------|-------------------------|
| Literature comparison | [VERIFIED] / [ESTIMATED] / [GAP] |
| Method attribution | [CITED] / [APPROXIMATE] / [UNKNOWN] |
| Dataset statistics | [FROM PAPER] / [ESTIMATED] / [UNAVAILABLE] |
| Clinical guideline reference | [CURRENT GUIDELINE] / [OUTDATED] / [COUNTRY-SPECIFIC] |

In each case, you are asking Claude to be explicit about what it knows versus what it is inferring. This converts a hallucination risk into an auditable confidence level.

---

## Success criteria

- `reports/lab_03_literature_search.md` contains a table with exactly 5 methods and a Confidence column
- `skills/literature_search_skill.md` exists with a substantive synthesis paragraph
- You verified at least one `[ESTIMATED]` entry against an external source
- You understand why requiring explicit confidence markers is more valuable than a polished paragraph summary
