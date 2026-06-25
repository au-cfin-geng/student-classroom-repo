# Course Site — Local Preview

Static site for the Agentic Clinical Research Studio onboarding page.

## Preview locally

From the repo root:

```bash
python3 -m http.server 8080 -d course-site
```

Then open: http://localhost:8080

## Files

| File | Purpose |
|------|---------|
| `index.html` | Main onboarding page |
| `assets/style.css` | All styles |
| `assets/setup_prompt.txt` | Plain-text copy of the student setup prompt |

## Deployment

Published to GitHub Pages via `.github/workflows/deploy-course-site.yml` on every push to `main`.

Repository Pages settings must have source set to **GitHub Actions** (not a branch).
Check: repo Settings → Pages → Source → GitHub Actions.
