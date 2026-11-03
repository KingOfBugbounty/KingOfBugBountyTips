[← Back to README](../Readme.md)

---

## 🆕 New Oneliners 2026

### ⚡🔥⚡ TelnetPwn - CVE-2026-24061 (CVSS 9.8 - CRITICAL) ⚡🔥⚡

> **💀 GNU InetUtils Telnetd Authentication Bypass - Instant Root Shell! Under Active Exploitation! 💀**

#### ⚡ 1. Shodan Mass Telnet Discovery
```bash
# 💀 Find exposed telnet servers worldwide
shodan search "port:23 telnet" --fields ip_str,port,org | awk '{print $1":"$2}' | anew telnet_targets.txt
```

#### ⚡ 2. Nmap Telnet Service Detection + Version
```bash
# 💀 Enumerate telnet services with version detection
nmap -p23 -sV --script=telnet-ntlm-info -iL targets.txt -oG - | grep "23/open" | awk '{print $2}' | anew telnet_open.txt
```

#### ⚡ 3. Masscan Fast Telnet Sweep
```bash
# 💀 Ultra-fast telnet port discovery on large ranges
masscan -p23 --rate=10000 -iL ip_ranges.txt -oG masscan_telnet.txt && cat masscan_telnet.txt | grep "23/open" | awk '{print $4}' | anew telnet_alive.txt
```

#### ⚡ 4. GNU InetUtils Telnetd Fingerprint
```bash
# 💀 Identify GNU inetutils-telnetd specifically (vulnerable)
cat telnet_targets.txt | xargs -P30 -I@ sh -c 'echo "" | timeout 3 nc -v @ 23 2>&1 | grep -qi "GNU\|inetutils\|Ubuntu\|Debian" && echo "[GNU TELNETD] @"' | tee gnu_telnetd.txt
```

#### ⚡ 5. CVE-2026-24061 Vulnerability Check (Safe)
```bash
# 💀 Test for NEW_ENVIRON option support (vuln indicator)
cat telnet_targets.txt | xargs -P20 -I@ sh -c 'echo -e "\xff\xfa\x27\x00\x00USER\x01-f\xff\xf0" | timeout 3 nc @ 23 2>/dev/null | grep -q "login\|root\|#" && echo "[CVE-2026-24061 POTENTIAL] @"' | tee cve_2026_24061_potential.txt
```

#### ⚡ 6. Nuclei CVE-2026-24061 Scanner
```bash
# 💀 Mass scan with Nuclei template
cat telnet_targets.txt | nuclei -t http/cves/2026/CVE-2026-24061.yaml -c 50 -o cve_2026_24061_vuln.txt
```

#### ⚡ 7. Banner Grabbing + Version Extraction
```bash
# 💀 Extract telnet banners for version analysis
cat telnet_targets.txt | xargs -P50 -I@ sh -c 'echo "" | timeout 3 nc @ 23 2>&1 | head -3' | tee telnet_banners.txt | grep -iE "(inetutils|GNU|2\.[0-7])" | anew potentially_vuln_versions.txt
```

#### ⚡ 8. Subnet Telnet Hunter
```bash
# 💀 Discover telnet in internal/external subnets
prips 192.168.0.0/16 | xargs -P100 -I@ sh -c 'timeout 1 nc -zv @ 23 2>&1 | grep -q "succeeded\|open" && echo @' | anew internal_telnet.txt
```

#### ⚡ 9. Telnet + OS Fingerprint Correlation
```bash
# 💀 Correlate telnet with vulnerable OS (Debian/Ubuntu/Kali)
nmap -p23 -sV -O --script=telnet-encryption -iL telnet_targets.txt -oX telnet_scan.xml && cat telnet_scan.xml | grep -oE "(Debian|Ubuntu|Kali|Linux)" | sort | uniq -c | sort -rn
```

#### ⚡ 10. Full CVE-2026-24061 Recon Pipeline
```bash
# 💀 Complete telnet vulnerability assessment pipeline
TARGET_RANGE="192.168.1.0/24"; mkdir -p telnet_recon && cd telnet_recon; masscan -p23 --rate=5000 $TARGET_RANGE -oG masscan.txt; cat masscan.txt | grep "23/open" | awk '{print $4}' > telnet_hosts.txt; cat telnet_hosts.txt | xargs -P30 -I@ sh -c 'echo "" | timeout 3 nc @ 23 2>&1 | head -5' > banners.txt; grep -liE "(GNU|inetutils|ubuntu|debian)" banners.txt | xargs -I@ basename @ .txt > gnu_telnetd_hosts.txt; echo "[+] Found $(wc -l < telnet_hosts.txt) telnet | $(wc -l < gnu_telnetd_hosts.txt) GNU inetutils (potentially vulnerable)"
```

> **⚠️ Affected:** GNU InetUtils telnetd 1.9.3 - 2.7 (Debian/Ubuntu/Kali/Trisquel)
> **✅ Fix:** Update to GNU InetUtils 2.8+ or disable telnetd and use SSH

---

### ⚡🔥⚡ Ni8mare - CVE-2026-21858 (CVSS 10.0 - CRITICAL) ⚡🔥⚡

> **💀 Critical Unauthenticated RCE in n8n Workflow Automation - 100,000+ servers affected! Added to CISA KEV 💀**

#### ⚡ Detect n8n Instances (Shodan/Censys)
```bash
shodan search "n8n" --fields ip_str,port,hostnames | awk '{print "https://"$1":"$2}' | httpx -silent | anew n8n_targets.txt
```

#### ⚡ Fingerprint n8n Installations
```bash
cat alive.txt | httpx -silent -match-string "n8n" -match-string "workflow" -title | grep -i "n8n" | anew n8n_instances.txt
```

#### ⚡ Check Vulnerable Webhook Endpoints
```bash
cat n8n_targets.txt | xargs -I@ -P20 sh -c 'curl -s -o /dev/null -w "%{http_code}" -X POST @/webhook-test/test -H "Content-Type: multipart/form-data" 2>/dev/null | grep -qE "^(200|400|500)$" && echo "POTENTIAL: @"' | tee n8n_webhook_check.txt
```

#### ⚡ Content-Type Confusion Detection
```bash
curl -s -X POST "https://target.com/webhook/ID" -H "Content-Type: application/json" --data '{"test":1}' -w "\n%{http_code}" | tail -1 | grep -qE "^(200|400)$" && echo "Webhook accepts requests"
```

#### ⚡ Mass n8n Version Detection
```bash
cat n8n_targets.txt | httpx -silent -path /rest/settings -match-regex '"versionCli":"[0-9]+\.[0-9]+\.[0-9]+"' | anew n8n_versions.txt
```

#### ⚡ Nuclei Template Check for CVE-2026-21858
```bash
nuclei -l n8n_targets.txt -t http/cves/2026/CVE-2026-21858.yaml -c 30 -o ni8mare_vuln.txt
```

> **⚠️ Affected:** n8n < 1.121.0 | **✅ Fix:** Update to n8n 1.121.0+

---

### ⚡🔥⚡ N8n Auth RCE - CVE-2026-21877 (CVSS 10.0 - CRITICAL) ⚡🔥⚡

> **💀 Authenticated RCE via Git Node in n8n - Cloud & Self-hosted affected! 💀**

#### ⚡ Detect Git Node Enabled Instances
```bash
cat n8n_targets.txt | httpx -silent -path /rest/node-types -match-string "git" | anew n8n_git_enabled.txt
```

#### ⚡ Check n8n Authentication Endpoints
```bash
cat n8n_targets.txt | httpx -silent -path /rest/login -mc 200,401 -title | anew n8n_auth_endpoints.txt
```

> **⚠️ Affected:** n8n < 1.121.3 | **✅ Fix:** Update to n8n 1.121.3+

---

### ⚡🔥⚡ D-Link DSL RCE - CVE-2026-0625 (CVSS 9.3 - CRITICAL) ⚡🔥⚡

> **💀 Command Injection in Legacy D-Link DSL Routers - Under active exploitation! 💀**

#### ⚡ Shodan Dork for D-Link DSL Routers
```bash
shodan search "D-Link DSL" --fields ip_str,port | awk '{print $1":"$2}' | httpx -silent | anew dlink_dsl_targets.txt
```

#### ⚡ Detect Vulnerable dnscfg.cgi Endpoint
```bash
cat dlink_dsl_targets.txt | httpx -silent -path /dnscfg.cgi -mc 200,401 | anew dlink_dnscfg.txt
```

#### ⚡ Mass D-Link Fingerprint
```bash
cat alive.txt | httpx -silent -match-string "D-Link" -match-string "DSL" -title -tech-detect | anew dlink_routers.txt
```

> **⚠️ Affected:** Legacy D-Link DSL Gateway Routers (EOL) | **✅ Fix:** Replace with supported devices

---

### ⚡🔥⚡ Veeam Backup RCE - CVE-2025-59470 (CVSS 9.0 - CRITICAL) ⚡🔥⚡

> **💀 RCE via Postgres Parameter Injection in Veeam Backup & Replication 💀**

#### ⚡ Detect Veeam Backup Servers
```bash
shodan search "Veeam" --fields ip_str,port | awk '{print "https://"$1":"$2}' | httpx -silent | anew veeam_targets.txt
```

#### ⚡ Fingerprint Veeam Instances
```bash
cat alive.txt | httpx -silent -match-string "Veeam" -title -tech-detect | grep -i "veeam" | anew veeam_instances.txt
```

> **⚠️ Affected:** Veeam B&R 13.0.1.180 and earlier | **✅ Fix:** Update to 13.0.1.1071+

---

### ⚡🔥⚡ Grafana Ghost XSS - CVE-2025-4123 (HIGH SEVERITY) ⚡🔥⚡

> **💀 Zero-Day XSS in Grafana - 46,500+ instances still vulnerable! Account Takeover possible 💀**

#### ⚡ Find Grafana Instances
```bash
shodan search "Grafana" --fields ip_str,port,hostnames | awk '{print "https://"$1":"$2}' | httpx -silent | anew grafana_targets.txt
```

#### ⚡ Detect Grafana Version
```bash
cat grafana_targets.txt | httpx -silent -path /api/frontend/settings -match-regex '"version":"[0-9]+\.[0-9]+\.[0-9]+"' | anew grafana_versions.txt
```

#### ⚡ Check Open Redirect (CVE-2025-4123 vector)
```bash
cat grafana_targets.txt | xargs -I@ sh -c 'curl -sI "@/login?redirect=//" 2>/dev/null | grep -i "location" && echo "CHECK: @"' | tee grafana_redirect_check.txt
```

#### ⚡ Mass Grafana Login Page Detection
```bash
cat alive.txt | httpx -silent -path /login -match-string "Grafana" -title | anew grafana_logins.txt
```

> **⚠️ Affected:** Multiple Grafana versions | **✅ Fix:** Update to latest patched version

---

### ⚡🔥⚡ CVE-2026 Subdomain Hunting - Mass Detection Pipeline ⚡🔥⚡

> **💀 10 Oneliners to hunt CVE-2026 vulnerabilities across subdomains at scale! 💀**

#### ⚡ 1. Full Subdomain CVE-2026 Hunt Pipeline (n8n + Grafana + D-Link)
```bash
subfinder -d target.com -silent | httpx -silent -title -tech-detect | tee alive_subs.txt | while read line; do echo "$line" | grep -qiE "(n8n|grafana|d-link)" && echo "[CVE-2026 TARGET] $line"; done | anew cve2026_targets.txt
```

#### ⚡ 2. Mass n8n CVE-2026-21858 Detection on Subdomains
```bash
subfinder -d target.com -silent | httpx -silent | xargs -I@ -P30 sh -c 'curl -s "@/rest/settings" 2>/dev/null | grep -q "versionCli" && echo "[N8N FOUND] @"' | tee n8n_subs.txt | xargs -I@ nuclei -u @ -t http/cves/2026/CVE-2026-21858.yaml -silent
```

#### ⚡ 3. CVE-2026-21877 n8n Git Node RCE Subdomain Scanner
```bash
cat subdomains.txt | httpx -silent | xargs -I@ -P20 sh -c 'curl -s "@/rest/node-types" 2>/dev/null | grep -qi "git" && curl -s "@/rest/settings" 2>/dev/null | grep -qE "versionCli.*1\.(([0-9]|[0-9][0-9]|1[01][0-9]|120)\.[0-9]+)" && echo "[CVE-2026-21877 VULN] @"' | anew n8n_git_vuln.txt
```

#### ⚡ 4. Grafana CVE-2025-4123 XSS + Open Redirect Subdomain Hunt
```bash
subfinder -d target.com -silent | httpx -silent -path /api/frontend/settings -match-regex '"version":"' | tee grafana_subs.txt | xargs -I@ -P15 sh -c 'curl -sI "@/login?redirect=//evil.com" 2>/dev/null | grep -qi "location.*evil" && echo "[CVE-2025-4123 VULN] @"'
```

#### ⚡ 5. Multi-CVE-2026 Scanner with Nuclei (Parallel Templates)
```bash
subfinder -d target.com -silent | httpx -silent | nuclei -tags cve2026 -severity critical,high -c 50 -o cve2026_nuclei_results.txt
```

#### ⚡ 6. Subdomain n8n Webhook Fingerprint + CVE-2026-21858 Check
```bash
cat subdomains.txt | httpx -silent | xargs -I@ -P25 sh -c 'for path in /webhook /webhook-test /rest/workflows; do curl -s -o /dev/null -w "%{http_code}" "@$path" 2>/dev/null | grep -qE "^(200|401|403)$" && echo "[N8N ENDPOINT] @$path" && break; done' | anew n8n_webhooks.txt
```

#### ⚡ 7. CVE-2026 IoT/Router Hunt (D-Link DSL + Other Routers)
```bash
subfinder -d target.com -silent | httpx -silent -title -tech-detect | grep -iE "(d-link|router|gateway|modem|dsl)" | tee router_subs.txt | xargs -I@ -P10 sh -c 'curl -s "@/dnscfg.cgi" 2>/dev/null | grep -qi "dns" && echo "[CVE-2026-0625 POTENTIAL] @"'
```

#### ⚡ 8. Veeam CVE-2025-59470 Subdomain Detection
```bash
subfinder -d target.com -silent | httpx -silent -title -tech-detect | grep -i "veeam" | tee veeam_subs.txt | xargs -I@ -P10 sh -c 'curl -s "@/api/v1/version" 2>/dev/null | grep -qE "13\.0\.[01]\.[0-9]+" && echo "[CVE-2025-59470 VULN] @"'
```

#### ⚡ 9. Combined CVE-2026 Fingerprint + Version Extractor
```bash
subfinder -d target.com -silent | httpx -silent -json | jq -r 'select(.technologies != null) | "\(.url) \(.technologies[])"' | grep -iE "(n8n|grafana|veeam|next)" | while read url tech; do echo "[CVE-2026 CHECK] $url - $tech"; done | anew cve2026_tech_fingerprint.txt
```

#### ⚡ 10. Full CVE-2026 Recon Automation Script
```bash
domain="target.com"; mkdir -p recon_$domain && cd recon_$domain && subfinder -d $domain -silent | httpx -silent -title -tech-detect -json -o httpx_out.json && cat httpx_out.json | jq -r '.url' | nuclei -t ~/nuclei-templates/http/cves/2026/ -c 30 -o cve2026_vulns.txt && echo "[+] Found $(wc -l < cve2026_vulns.txt) CVE-2026 vulnerabilities!"
```

> **🎯 Pro Tip:** Combine with `notify` to get real-time alerts: `... | notify -silent -provider slack`

---

### ⚡🔥⚡ Advanced Reconnaissance Pipeline - 2026 Edition ⚡🔥⚡

> **🎯 10 Elite Oneliners for comprehensive reconnaissance - Multi-source enumeration, ASN discovery, JS analysis & more! 🎯**

#### ⚡ 1. Multi-Source Subdomain Discovery + Tech Fingerprinting
```bash
subfinder -d target.com -all -silent | anew subs.txt && assetfinder --subs-only target.com | anew subs.txt && amass enum -passive -norecursive -noalts -d target.com | anew subs.txt && cat subs.txt | httpx -silent -threads 200 -tech-detect -status-code -title -o alive_with_tech.txt
```
> Combines Subfinder + Assetfinder + Amass for maximum subdomain coverage, then validates with httpx + technology fingerprinting

#### ⚡ 2. ASN Enumeration + Reverse DNS Discovery
```bash
echo "target.com" | dnsx -silent -resp-only -a | xargs -I{} whois -h whois.cymru.com {} | awk '{print $1}' | grep -E "AS[0-9]+" | xargs -I{} sh -c 'whois -h whois.radb.net -- "-i origin {}" | grep -Eo "([0-9.]+){4}/[0-9]+"' | mapcidr -silent | dnsx -silent -ptr -resp-only | anew asn_discovered_hosts.txt
```
> Discovers ASN, enumerates IP blocks, performs reverse DNS to find hidden subdomains

#### ⚡ 3. URL Discovery Pipeline (Wayback + GAU + Katana)
```bash
cat alive.txt | xargs -P 50 -I{} sh -c 'echo {} | waybackurls & echo {} | gau --threads 10 --blacklist png,jpg,gif,svg,woff,ttf & echo {} | katana -d 3 -jc -kf all -silent' | uro | anew all_urls.txt
```
> Parallel URL collection from Wayback Machine, Common Crawl, AlienVault + active crawling with smart deduplication

#### ⚡ 4. JavaScript Deep Analysis + Secret Scanner
```bash
cat alive.txt | katana -silent -em js,json -jc -d 2 | httpx -silent -mc 200 | tee js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} | tee /tmp/js_$$.tmp | grep -oE "(api_key|apikey|api-key|secret|token|password|aws_access|AKIA[0-9A-Z]{16})" && cat /tmp/js_$$.tmp | grep -oE "/(api|v[0-9]|admin|internal)/[a-zA-Z0-9_/?=&-]+" | sort -u' | anew js_secrets_and_endpoints.txt
```
> Finds JS files, extracts hardcoded secrets (API keys, tokens, AWS keys) and hidden API endpoints

#### ⚡ 5. Certificate Transparency + Subdomain Permutation Attack
```bash
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | tee crt_subs.txt | dnsgen - | shuffledns -d target.com -r /usr/share/wordlists/resolvers.txt -silent -o permuted_subs.txt && cat permuted_subs.txt | httpx -silent -o alive_permuted.txt
```
> CT logs enumeration + intelligent permutation (api → api-dev, api-staging) with mass DNS resolution

#### ⚡ 6. Port Discovery + Web Services on Non-Standard Ports
```bash
cat subs.txt | naabu -silent -top-ports 1000 -exclude-cdn -c 50 | sed 's/:/ /g' | awk '{print $1":"$2}' | httpx -silent -probe -status-code -title -tech-detect -follow-redirects -random-agent -o ports_with_web_services.txt
```
> Fast port scan + discovers web apps running on unusual ports (8080, 8443, 3000, etc)

#### ⚡ 7. GitHub Dorking Automation for Target Organization
```bash
ORG="target"; for dork in "org:$ORG password" "org:$ORG api_key" "org:$ORG secret" "org:$ORG token" "org:$ORG aws_access" "org:$ORG credentials"; do echo "[+] Searching: $dork"; gh search repos "$dork" --limit 100 | grep "^$ORG" | tee -a github_secrets.txt; sleep 2; done
```
> Automated GitHub dorking for secrets, credentials and sensitive data exposure

#### ⚡ 8. Cloud Storage Discovery (S3 + Azure + GCP)
```bash
cat all_urls.txt | grep -oE '(s3\.amazonaws\.com/[a-zA-Z0-9._-]+|[a-zA-Z0-9._-]+\.s3\.amazonaws\.com|storage\.googleapis\.com/[a-zA-Z0-9._-]+|[a-zA-Z0-9._-]+\.blob\.core\.windows\.net)' | sort -u | tee cloud_buckets.txt | xargs -I{} sh -c 'curl -sI https://{} | grep -q "200\|403" && echo "[+] {} - Accessible"'
```
> Extracts and validates misconfigured cloud storage buckets from collected URLs

#### ⚡ 9. Parameter Discovery + Vulnerability Pattern Matching
```bash
cat all_urls.txt | uro | grep "=" | unfurl keys | sort -u | tee all_params.txt && cat all_urls.txt | gf xss | tee xss_params.txt && cat all_urls.txt | gf ssrf | tee ssrf_params.txt && cat all_urls.txt | gf sqli | tee sqli_params.txt && cat all_urls.txt | gf redirect | tee redirect_params.txt
```
> Extracts unique parameters and categorizes by vulnerability type (XSS, SSRF, SQLi, Redirect)

#### ⚡ 10. Continuous Recon Monitor (Cron-Ready)
```bash
DOMAIN="target.com"; DATE=$(date +%Y%m%d); mkdir -p recon_$DATE; cd recon_$DATE; subfinder -d $DOMAIN -all -silent | anew subs_$DATE.txt; cat subs_$DATE.txt | httpx -silent -threads 200 -o alive_$DATE.txt; cat alive_$DATE.txt | nuclei -t exposures/ -silent -o new_exposures_$DATE.txt; diff ../recon_$(date -d "yesterday" +%Y%m%d)/subs_*.txt subs_$DATE.txt 2>/dev/null | grep ">" | awk '{print $2}' > new_subs_$DATE.txt; [ -s new_subs_$DATE.txt ] && notify -silent -bulk < new_subs_$DATE.txt
```
> Full persistent recon pipeline - detects new assets daily and sends notifications

> **🎯 Pro Tip:** Run oneliner #10 via cron for 24/7 monitoring: `0 */6 * * * /path/to/recon_monitor.sh`

---

### ⚡🔥⚡ JavaScript Endpoint Extraction - Elite Techniques 2026 ⚡🔥⚡

> **🎯 10 Oneliners to extract endpoints, secrets and hidden APIs from JavaScript files! 🎯**

#### ⚡ 1. Mass JS File Discovery + Download Pipeline
```bash
cat alive.txt | katana -silent -em js -jc -d 3 | grep -E "\.js(\?|$)" | httpx -silent -mc 200 -content-length | awk '$NF > 500 {print $1}' | anew js_files.txt && cat js_files.txt | xargs -P 30 -I{} sh -c 'curl -sk {} -o js_downloaded/$(echo {} | md5sum | cut -d" " -f1).js 2>/dev/null'
```
> Discovers all JS files with Katana, filters by size (>500 bytes), downloads for offline analysis

#### ⚡ 2. Extract All API Endpoints from JS Files
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null' | grep -oE '["'"'"'](\/[a-zA-Z0-9_\-\.\/]+(\?[a-zA-Z0-9_\-\.=&]+)?)['"'"'"]' | sed 's/[\"'"'"']//g' | sort -u | grep -E "^/" | grep -vE "\.(css|png|jpg|svg|gif|woff|ico)$" | anew js_endpoints.txt
```
> Extracts all relative API paths from JavaScript, filters static assets

#### ⚡ 3. AWS Keys Hunter in JS Files
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "(AKIA|ABIA|ACCA|ASIA)[0-9A-Z]{16}" && echo "Found in: {}"' | tee aws_keys_js.txt
```
> Hunts for AWS Access Key IDs (AKIA, ABIA, ACCA, ASIA patterns)

#### ⚡ 4. Google API Keys + Firebase URLs Extractor
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "(AIza[0-9A-Za-z_-]{35}|[a-z0-9-]+\.firebaseio\.com|[a-z0-9-]+\.firebaseapp\.com)" && echo "[SOURCE] {}"' | tee google_firebase_keys.txt
```
> Extracts Google API keys and Firebase database/app URLs

#### ⚡ 5. S3 Bucket Discovery in JavaScript
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "([a-zA-Z0-9_-]+\.s3\.amazonaws\.com|s3\.amazonaws\.com\/[a-zA-Z0-9_-]+|[a-zA-Z0-9_-]+\.s3\.[a-z0-9-]+\.amazonaws\.com)" | sort -u' | anew s3_buckets_js.txt && cat s3_buckets_js.txt | xargs -I{} sh -c 'curl -sI https://{} 2>/dev/null | head -1 | grep -qE "200|403" && echo "[ACCESSIBLE] {}"'
```
> Finds S3 buckets in JS and validates accessibility

#### ⚡ 6. Internal IP Addresses Leakage
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "(10\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|172\.(1[6-9]|2[0-9]|3[01])\.[0-9]{1,3}\.[0-9]{1,3}|192\.168\.[0-9]{1,3}\.[0-9]{1,3})" && echo "[SOURCE] {}"' | sort -u | tee internal_ips_js.txt
```
> Discovers internal/private IP addresses leaked in JavaScript (10.x, 172.16-31.x, 192.168.x)

#### ⚡ 7. Slack Webhooks + Discord Tokens in JS
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "(https://hooks\.slack\.com/services/[A-Za-z0-9/]+|[MN][A-Za-z\d]{23,}\.[\w-]{6}\.[\w-]{27})" && echo "[SOURCE] {}"' | tee slack_discord_js.txt
```
> Extracts Slack webhook URLs and Discord bot tokens

#### ⚡ 8. GitHub Tokens + Private Keys Detection
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "(ghp_[a-zA-Z0-9]{36}|gho_[a-zA-Z0-9]{36}|ghu_[a-zA-Z0-9]{36}|ghs_[a-zA-Z0-9]{36}|ghr_[a-zA-Z0-9]{36}|github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}|-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----)" && echo "[SOURCE] {}"' | tee github_privkeys_js.txt
```
> Finds GitHub personal access tokens (all formats) and private key headers

#### ⚡ 9. Email Addresses + Hidden Subdomains in JS
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" | sort -u' | anew emails_js.txt && cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "https?://[a-zA-Z0-9._-]+\.target\.com[a-zA-Z0-9./?=_-]*"' | unfurl domains | sort -u | anew hidden_subdomains_js.txt
```
> Extracts email addresses and hidden subdomains referenced in JavaScript

#### ⚡ 10. Full JS Recon Pipeline (All-in-One)
```bash
TARGET="target.com"; mkdir -p js_recon_$TARGET && cat alive.txt | katana -silent -em js -jc -d 3 | grep -iE "\.js(\?|$)" | httpx -silent -mc 200 | anew js_recon_$TARGET/js_urls.txt && cat js_recon_$TARGET/js_urls.txt | xargs -P 30 -I{} sh -c 'curl -sk {} 2>/dev/null | tee -a js_recon_$TARGET/all_js.txt' && grep -oE "(AKIA|ABIA|ACCA|ASIA)[0-9A-Z]{16}" js_recon_$TARGET/all_js.txt > js_recon_$TARGET/aws_keys.txt; grep -oE "AIza[0-9A-Za-z_-]{35}" js_recon_$TARGET/all_js.txt > js_recon_$TARGET/google_keys.txt; grep -oE "ghp_[a-zA-Z0-9]{36}" js_recon_$TARGET/all_js.txt > js_recon_$TARGET/github_tokens.txt; grep -oE '["'"'"']/[a-zA-Z0-9_/-]+["'"'"']' js_recon_$TARGET/all_js.txt | tr -d '\"'"'"'' | sort -u > js_recon_$TARGET/endpoints.txt; echo "[+] JS Recon Complete! Check js_recon_$TARGET/"
```
> Complete JS recon pipeline: discovers JS files, downloads all, extracts AWS/Google/GitHub keys and API endpoints

> **🎯 Pro Tip:** Use `nuclei -t exposures/tokens/` on discovered secrets to validate if they're active!

---

[← Back to README](../Readme.md)
