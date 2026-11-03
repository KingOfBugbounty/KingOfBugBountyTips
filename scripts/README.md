# Scripts

Supporting tools for this repo's recon tips. Each file has a header comment
describing its purpose, usage, and requirements — read that before running
anything here.

| Script | What it does |
|:-------|:-------------|
| [`recon_pipeline.py`](recon_pipeline.py) | Interactive, resumable recon pipeline (subfinder → httpx → katana → nuclei → gf → dalfox → HTML report). The most actively maintained script here. |
| [`resolvhtml.go`](resolvhtml.go) | Converts `httpx -json` output into a static HTML report. Built and called by `recon_pipeline.py`. |
| [`dod_site_crawler.py`](dod_site_crawler.py) | Scrapes defense.gov's public DoD website index to help maintain the DoD domain list. |
| [`download_links.py`](download_links.py) | Generic bulk downloader for a newline-separated list of URLs (`links.txt`). Example input list: [`../data/chaos-dataset-links.txt`](../data/chaos-dataset-links.txt). |
| [`telegram_bot_draft.py`](telegram_bot_draft.py) | **Draft/incomplete.** Proof-of-concept Telegram bot sketch for triggering a scan via chat command. Not production-ready — see its header for known gaps. |

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md) before adding a new script here.
