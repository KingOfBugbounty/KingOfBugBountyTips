[← Back to README](../Readme.md)

---

## 🕷️ Web Crawling

### Katana Deep Crawl
```bash
katana -u https://target.com -d 10 -jc -kf all -aff -silent | anew crawl.txt
```

### Gospider Full Crawl
```bash
gospider -s https://target.com -c 20 -d 5 --blacklist ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|ico)" | anew
```

### Hakrawler with Scope
```bash
echo https://target.com | hakrawler -d 5 -subs -u | anew hakrawler.txt
```

### ParamSpider Discovery
```bash
paramspider -d target.com --exclude woff,css,js,png,svg,jpg -o params.txt
```

### Waymore Historical URLs
```bash
waymore -i target.com -mode U -oU urls.txt
```

### Crawl with Headless Browser
```bash
katana -u https://target.com -headless -d 5 -jc -silent | anew headless_crawl.txt
```

### Extract Forms
```bash
katana -u https://target.com -f qurl -silent | grep "?" | anew forms.txt
```

### 💀 Katana Multi-Target Deep Crawl + JS Parsing
```bash
# ☠️ Crawl multiple targets with JavaScript parsing and form extraction
cat alive.txt | katana -d 8 -jc -kf all -aff -ef woff,css,png,svg,jpg,woff2,jpeg,gif,ico -c 50 -p 20 -silent -o katana_multi.txt
```

### 💀 Gospider Recursive + Sitemap + Robots
```bash
# ☠️ Full crawl with sitemap parsing and robots.txt extraction
gospider -S alive.txt -c 30 -d 5 -t 20 --sitemap --robots --js -a -w --blacklist ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|ico|svg)" -o gospider_output && cat gospider_output/* | grep -oE 'https?://[^"]+' | sort -u | anew gospider_urls.txt
```

### 💀 Hakrawler + Wayback + GAU Combined Crawler
```bash
# ☠️ Triple source crawling: live + wayback + gau
echo target.com | hakrawler -d 5 -subs -u > hakrawler.txt && waybackurls target.com > wayback.txt && gau target.com > gau.txt && cat hakrawler.txt wayback.txt gau.txt | sort -u | httpx -silent | anew all_crawled.txt
```

### 💀 Katana Headless + Form Autofill + Screenshot
```bash
# ☠️ Headless browser crawl with form interaction and XHR capture
katana -u https://target.com -headless -d 6 -jc -aff -xhr -form -timeout 15 -silent -nc -c 20 | anew headless_interactive.txt
```

### 💀 Cariddi Full Crawl with Secret Detection
```bash
# ☠️ Crawl with built-in secrets/endpoints/parameters extraction
cariddi -u https://target.com -d 5 -s -e -ext 1 -plain -t 50 -c 20 | tee cariddi_results.txt && grep -E "(api|secret|key|token|pass|auth)" cariddi_results.txt | anew secrets_found.txt
```

### 💀 Parallel Domain Crawler Pipeline
```bash
# ☠️ Mass parallel crawling with deduplication
cat domains.txt | parallel -j 10 "katana -u https://{} -d 5 -jc -silent" | uro | anew parallel_crawl.txt
```

### 💀 Katana + Gospider + LinkFinder Chain
```bash
# ☠️ Combined crawling + JS endpoint extraction pipeline
katana -u https://target.com -d 5 -jc -silent | grep "\.js$" | httpx -silent | xargs -I@ bash -c 'curl -s @ | grep -oE "(\/[a-zA-Z0-9_\-\/]+)" | sort -u' | anew js_endpoints.txt && gospider -s https://target.com -d 5 -c 10 --js -q | grep -oE 'https?://[^"]+' | anew combined_crawl.txt
```

### 💀 Recursive Crawl + Nuclei Auto-Scan Pipeline
```bash
# ☠️ Crawl then auto-scan discovered endpoints for vulnerabilities
katana -u https://target.com -d 6 -jc -kf all -aff -silent | tee crawl_output.txt | grep -E "\.(php|asp|aspx|jsp|do|action)(\?|$)" | nuclei -t /root/nuclei-templates/ -severity high,critical -silent -o crawl_vulns.txt
```

### 💀 Waymore + Katana Historical + Live Merge
```bash
# ☠️ Merge historical URLs with live crawl for maximum coverage
waymore -i target.com -mode U -oU waymore_urls.txt && katana -u https://target.com -d 5 -jc -aff -silent -o katana_live.txt && cat waymore_urls.txt katana_live.txt | uro | httpx -silent -mc 200,301,302,403 | anew merged_crawl.txt
```

### 💀 Multi-Crawler Output Dedup + Parameter Extraction
```bash
# ☠️ Run all crawlers and extract unique parameters
(gospider -s https://target.com -d 3 -c 10 -q; hakrawler -url https://target.com -d 3; katana -u https://target.com -d 3 -jc -silent) | sort -u | unfurl -u keys | sort | uniq -c | sort -rn | head -100 | anew top_params.txt
```

---

## 🔑 Parameter Discovery

### X8 Hidden Parameters
```bash
cat urls.txt | httpx -silent | xargs -I@ x8 -u @ -w params.txt
```

### Arjun Discovery
```bash
arjun -i urls.txt -oT arjun_params.txt --stable
```

### Custom Param Bruteforce
```bash
cat urls.txt | sed 's/$/\?FUZZ=test/' | ffuf -w params.txt:FUZZ -u FUZZ -mc 200,301,302 -ac
```

### Mine Parameters from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "[?&][a-zA-Z0-9_]+=" | cut -d'=' -f1 | tr -d '?&' | sort -u
```

### Parameter Pollution Test
```bash
cat urls.txt | qsreplace 'param=value1&param=value2' | httpx -silent -mc 200
```

---

[← Back to README](../Readme.md)
