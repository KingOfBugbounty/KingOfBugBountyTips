# Data

Plain data/payload lists used by the tips in [`docs/`](../docs/) and the
scripts in [`scripts/`](../scripts/).

| File | Purpose |
|:-----|:--------|
| [`SSRF-bypass-payloads.txt`](SSRF-bypass-payloads.txt) | SSRF filter-bypass payloads for `127.0.0.1`/metadata endpoints (decimal/octal/hex IP encodings, IPv6, Unicode fullwidth digits) plus a few whitelist-bypass hostnames. Referenced from [`docs/ssrf-ssti.md`](../docs/ssrf-ssti.md). |
| [`chaos-dataset-links.txt`](chaos-dataset-links.txt) | Sample input for [`scripts/download_links.py`](../scripts/download_links.py) — a list of ProjectDiscovery Chaos dataset ZIP URLs. |
| [`DoD Domains.txt`](<DoD Domains.txt>) | Flat list of in-scope `*.mil`/DoD-related hostnames, feeding the DoD VDP scope section in `Readme.md`. |

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — in particular, don't add
raw recon output against a specific live target here; this directory is for
generic, reusable payload/reference data only.
