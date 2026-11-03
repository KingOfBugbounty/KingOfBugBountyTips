# Contributing to KingOfBugBountyTips

Thanks for wanting to add to this collection. This repo is for **educational
and authorized security testing only** — see the Security Notice in
[`Readme.md`](Readme.md) before you contribute or use anything here.

## Where things live

The README used to be a single multi-thousand-line file. It's now split by
topic under [`docs/`](docs/), with `Readme.md` acting as a short index/TOC.
Add new one-liners to the matching topic file:

| Topic | File |
|:------|:-----|
| Setup / required tools | `docs/setup.md` |
| Subdomain, TLS, DNS recon | `docs/subdomain-recon.md` |
| JavaScript recon | `docs/js-recon.md` |
| XSS | `docs/xss.md` |
| SQL injection | `docs/sqli.md` |
| SSRF / SSTI | `docs/ssrf-ssti.md` |
| Web crawling / parameter discovery | `docs/web-crawling.md` |
| Content discovery | `docs/content-discovery.md` |
| Nuclei scanning | `docs/nuclei.md` |
| API security | `docs/api-security.md` |
| Cloud security | `docs/cloud-security.md` |
| Automation / bash functions | `docs/automation.md` |
| Search engines, wordlists, learning resources | `docs/resources.md` |

If nothing fits, propose a new file rather than growing an existing one past
a few hundred lines.

### New CVE one-liners

- **Current year, newest first:** add to `docs/oneliners-2026.md`.
- **A specific month's CVE round-up** (e.g. "February 2026 CVE Discovery"):
  add to that month's file if one exists (e.g. `docs/cve-feb-2026.md`), or
  propose a new `docs/cve-<mon>-<year>.md` file for a new month rather than
  reusing an older one. Don't duplicate an entry across both a yearly and a
  monthly file — pick the one that already tracks that CVE.
- Older/superseded techniques belong in `docs/oneliners-2024-2025.md`, not
  mixed into the current year's file.

## One-liner format

Keep each entry self-contained and copy-pasteable:

````markdown
### <emoji> Short, descriptive title
```bash
# <emoji> one-line comment: what this does and why it's useful
<the actual command>
```
````

- One command block per technique — don't bundle unrelated steps.
- Use `target.com` / `target_org` / `YOUR_API_KEY` as placeholders, never a
  real domain, key, or token.
- If the technique depends on a specific tool, link it the first time it's
  used in that file (or confirm it's already listed in `docs/setup.md`).
- If it exploits a specific CVE, name the CVE ID in the title.

### Attribution

If you learned the technique from someone specific (a tweet, blog post,
talk, or tool README), credit them in the entry, e.g.:

```markdown
### 💀 Technique name
<!-- via @handle: https://link-to-source -->
```bash
...
```
```

Don't claim authorship of a technique you didn't originate — "Special
Thanks" in `Readme.md` is for well-known contributors to the field in
general; per-entry attribution is for where a specific one-liner came from.

## What NOT to commit

- No real credentials, API keys, session tokens, or cookies — not even from
  your own test environment. Use obvious placeholders (`YOUR_API_KEY`).
- No raw recon output against a specific live target (subdomain lists,
  screenshots, HTTP responses, scan results) — those are engagement
  artifacts, not generic tips, and may violate the scope/disclosure rules of
  whatever program they came from. Generic, reusable templates (including
  Nuclei templates you authored and want to name/credit) are fine.
- No destructive, DoS/DDoS, or detection-evasion-for-malicious-use content.
  Dual-use techniques (recon, fuzzing, auth testing) are welcome; techniques
  whose only use is causing harm are not.

## Scripts, templates, and data

- Standalone scripts live in [`scripts/`](scripts/), each with a header
  comment (purpose, usage, requirements) — see `scripts/README.md`. Give any
  new script the same treatment rather than adding it undocumented at the
  repo root.
- Nuclei templates and PoC fixtures (like the Swagger-UI XSS pair) live in
  [`templates/`](templates/) (`templates/nuclei/`, `templates/payloads/`) —
  see `templates/README.md`.
- Plain payload/reference data lists (SSRF bypass strings, sample URL
  lists, the DoD domain list) live in [`data/`](data/) — see
  `data/README.md`.

Don't add a new `.yaml`/`.json`/`.txt` fixture at the repo root — put it in
whichever of the above it fits, with an entry in that folder's README.

## Submitting

1. Fork the repo and branch (`git checkout -b feature/your-contribution`).
2. Add your content to the right file, following the format above.
3. Open a PR with a short description of what the technique does and, if
   relevant, where you learned it.
