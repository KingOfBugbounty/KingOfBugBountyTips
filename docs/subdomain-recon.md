[← Back to README](../Readme.md)

---

## 💀 Subdomain Enumeration ☠️

<div align="center">

```
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
███████╗██║   ██║██████╔╝██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
```

**☠️ ENUMERATE EVERYTHING ☠️**

</div>

### 💀 Multi-Source Discovery (All-in-One)
```bash
# ☠️ Ultimate subdomain enumeration - All tools combined
subfinder -d target.com -all -silent | anew subs.txt
amass enum -passive -d target.com | anew subs.txt
assetfinder -subs-only target.com | anew subs.txt
chaos -d target.com -silent | anew subs.txt
findomain -t target.com -q | anew subs.txt
cat subs.txt | httpx -silent -threads 200 | anew alive.txt
```

### 💀 Certificate Transparency Logs
```bash
# ☠️ crt.sh extraction
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | httpx -silent
```

### 💀 Certstream Real-Time Monitoring - Basic
```bash
# ☠️ Monitor certificates in real-time for specific keyword
pip install certstream && python3 -c "import certstream; certstream.listen_for_events(lambda msg, ctx: print(msg['data']['leaf_cert']['subject']['CN']) if 'target' in str(msg.get('data',{}).get('leaf_cert',{}).get('subject',{}).get('CN','')) else None, url='wss://certstream.calidog.io/')"
```

### 💀 Certstream with Domain Filter
```bash
# ☠️ Real-time cert monitoring filtered by domain keywords
certstream --full | jq -r 'select(.data.leaf_cert.subject.CN != null) | .data.leaf_cert.subject.CN' | grep -iE "(target|company|brand)" | anew certstream_targets.txt
```

### 💀 Certstream to Subdomain Discovery
```bash
# ☠️ Extract all SANs (Subject Alternative Names) in real-time
certstream --full | jq -r '.data.leaf_cert.extensions.subjectAltName // empty' | tr ',' '\n' | sed 's/DNS://g' | grep -E "target\.com$" | sort -u | anew certstream_subs.txt
```

### 💀 Certstream + httpx Live Pipeline
```bash
# ☠️ Real-time cert discovery -> immediate alive check
certstream --full | jq -r '.data.leaf_cert.all_domains[]? // empty' 2>/dev/null | grep -iE "target" | sort -u | while read domain; do echo "$domain" | httpx -silent -timeout 3 | anew live_certs.txt; done
```

### 💀 Certstream Phishing Detection
```bash
# ☠️ Monitor for potential phishing domains (brand impersonation)
certstream --full | jq -r '.data.leaf_cert.subject.CN // empty' | grep -iE "(paypal|apple|google|microsoft|amazon|facebook|netflix|bank)" | grep -vE "\.(paypal|apple|google|microsoft|amazon|facebook|netflix)\.com$" | anew phishing_certs.txt
```

### 💀 Certstream with Nuclei Auto-Scan
```bash
# ☠️ Real-time cert discovery -> automatic vulnerability scan
certstream --full | jq -r '.data.leaf_cert.all_domains[]? // empty' | grep -E "\.target\.com$" | sort -u | while read domain; do echo "https://$domain" | nuclei -t /nuclei-templates/technologies/ -silent; done
```

### 💀 Certstream Mass Collector Script
```bash
# ☠️ Collect all certificates for specific TLDs
timeout 3600 bash -c 'certstream --full | jq -r ".data.leaf_cert.all_domains[]? // empty" | grep -E "\.(gov|mil|edu)$" | anew gov_mil_edu_certs.txt' &
```

### 💀 Certstream Wildcard Certificate Hunter
```bash
# ☠️ Find wildcard certificates (*.domain.com) in real-time
certstream --full | jq -r '.data.leaf_cert.subject.CN // empty' | grep "^\*\." | sed 's/^\*\.//' | sort -u | anew wildcard_domains.txt
```

### 💀 Certstream + Shodan Enrichment
```bash
# ☠️ Real-time certs -> resolve IP -> Shodan lookup
certstream --full | jq -r '.data.leaf_cert.subject.CN // empty' | grep -iE "target" | while read domain; do IP=$(dig +short "$domain" | head -1); [ -n "$IP" ] && echo "$domain,$IP,$(shodan host $IP 2>/dev/null | head -3 | tr '\n' ' ')"; done | anew cert_shodan.txt
```

### 💀 Certstream JSON Logger with Timestamp
```bash
# ☠️ Full certificate logging with timestamps for analysis
certstream --full | jq -c '{timestamp: now | strftime("%Y-%m-%d %H:%M:%S"), cn: .data.leaf_cert.subject.CN, domains: .data.leaf_cert.all_domains, issuer: .data.leaf_cert.issuer.O}' | grep -i "target" | tee -a certstream_log.json
```

### 💀 Certstream Bug Bounty Scope Monitor
```bash
# ☠️ Monitor multiple bug bounty targets simultaneously
TARGETS="hackerone|bugcrowd|intigriti|yeswehack"; certstream --full | jq -r '.data.leaf_cert.all_domains[]? // empty' | grep -iE "$TARGETS" | anew bb_new_assets.txt &
```

### 💀 Shodan + Nuclei Pipeline
```bash
# ☠️ Shodan recon -> Nuclei scan
shodan domain target.com | awk '{print $3}' | httpx -silent | nuclei -t /nuclei-templates/ -severity critical,high
```

### 💀 Clawdbot Discovery via Shodan (Mass Exploitation)

#### ⚡ 1. Find Clawdbot Instances - Basic Search
```bash
# 💀 Locate Clawdbot servers exposed on the internet
shodan search "Clawdbot" --fields ip_str,port,hostnames,org | awk '{print $1":"$2}' | anew clawdbot_targets.txt
```

#### ⚡ 2. Clawdbot HTTP Headers Discovery
```bash
# 💀 Find servers with Clawdbot in HTTP headers
shodan search "http.headers:Clawdbot" --fields ip_str,port,http.title | tee clawdbot_http.txt | wc -l && echo "targets found"
```

#### ⚡ 3. Clawdbot User-Agent Detection
```bash
# 💀 Detect Clawdbot via User-Agent strings
shodan search "http.user_agent:Clawdbot" --fields ip_str,port,org,hostnames | awk -F'\t' '{print "https://"$1":"$2" - "$3}' | anew clawdbot_ua.txt
```

#### ⚡ 4. Clawdbot + Nuclei Exploitation Pipeline
```bash
# 💀 Mass Clawdbot discovery -> httpx alive -> Nuclei scan
shodan search "Clawdbot" --fields ip_str,port --limit 1000 | awk '{print $1":"$2}' | httpx -silent | nuclei -t ~/nuclei-templates/ -severity critical,high -o clawdbot_vulns.txt
```

#### ⚡ 5. Clawdbot Server Fingerprinting
```bash
# 💀 Extract detailed server info from Clawdbot hosts
shodan search "Clawdbot" --fields ip_str,port,os,product,version,org | sort -t$'\t' -k4 | anew clawdbot_fingerprint.txt
```

#### ⚡ 6. Clawdbot ASN Distribution Analysis
```bash
# 💀 Map Clawdbot instances by ASN for targeted reconnaissance
shodan search "Clawdbot" --fields ip_str,asn,org | awk '{print $2}' | sort | uniq -c | sort -rn | head -20 | tee clawdbot_asn_stats.txt
```

#### ⚡ 7. Clawdbot Geographic Distribution
```bash
# 💀 Find Clawdbot by country for geo-targeted testing
for country in US BR DE FR GB RU CN JP KR IN; do echo "=== $country ===" && shodan search "Clawdbot country:$country" --fields ip_str,port,city --limit 100 | anew clawdbot_${country}.txt; done
```

#### ⚡ 8. Clawdbot + Port Range Scan
```bash
# 💀 Discover Clawdbot on common web ports
shodan search "Clawdbot port:80,443,8080,8443,8000,3000,5000" --fields ip_str,port,http.server | awk '{print $1":"$2}' | httpx -silent -status-code -title | anew clawdbot_webports.txt
```

#### ⚡ 9. Clawdbot SSL Certificate Analysis
```bash
# 💀 Extract Clawdbot hosts with SSL certificate info
shodan search "Clawdbot ssl:true" --fields ip_str,port,ssl.cert.subject.CN,ssl.cert.issuer.O | sort -u | anew clawdbot_ssl.txt
```

#### ⚡ 10. Clawdbot Realtime Monitor + Alert
```bash
# 💀 Continuous monitoring for new Clawdbot instances
while true; do shodan search "Clawdbot" --fields ip_str,port,timestamp --limit 50 | sort -t$'\t' -k3 -r | head -10 | anew clawdbot_new.txt && sleep 3600; done &
```

### 💀 ASN Discovery & Reverse DNS
```bash
# ☠️ Find all IPs from organization ASN
echo 'target_org' | metabigor net --org -v | awk '{print $3}' | sed 's/[[0-9]]\+\.//g' | xargs -I@ sh -c 'prips @ | hakrevdns | anew'
```

### 💀 DNS Bruteforce with Shuffledns
```bash
shuffledns -d target.com -w wordlist.txt -r resolvers.txt -silent | httpx -silent | anew
```

### 💀 Recursive Subdomain Enum
```bash
subfinder -d target.com -recursive -all -silent | dnsx -silent | httpx -silent | anew recursive_subs.txt
```

### 💀 Passive DNS - Multiple Sources
```bash
# ☠️ HackerTarget
curl -s "https://api.hackertarget.com/hostsearch/?q=target.com" | cut -d',' -f1 | anew subs.txt

# ☠️ RapidDNS
curl -s "https://rapiddns.io/subdomain/target.com?full=1" | grep -oP '(?<=target="_blank">)[^<]+' | grep "target.com" | anew subs.txt

# ☠️ Riddler.io
curl -s "https://riddler.io/search/exportcsv?q=pld:target.com" | grep -oP '\b([a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+target\.com\b' | anew subs.txt

# ☠️ AlienVault OTX
curl -s "https://otx.alienvault.com/api/v1/indicators/domain/target.com/passive_dns" | jq -r '.passive_dns[].hostname' 2>/dev/null | sort -u | anew subs.txt

# ☠️ URLScan.io
curl -s "https://urlscan.io/api/v1/search/?q=domain:target.com" | jq -r '.results[].page.domain' 2>/dev/null | sort -u | anew subs.txt
```

### 💀 GitHub Subdomain Scraping
```bash
github-subdomains -d target.com -t YOUR_GITHUB_TOKEN -o github_subs.txt
```

### 💀 Censys Subdomain Discovery
```bash
# ☠️ Using Censys API
censys search "target.com" --index-type hosts | jq -r '.[] | .name' | sort -u | anew censys_subs.txt
```

### 💀 SecurityTrails API
```bash
# ☠️ SecurityTrails subdomain enumeration
curl -s "https://api.securitytrails.com/v1/domain/target.com/subdomains" -H "APIKEY: YOUR_API_KEY" | jq -r '.subdomains[]' | sed 's/$/.target.com/' | anew subs.txt
```

### 💀 Wayback Machine Subdomains
```bash
# ☠️ Extract subdomains from Wayback Machine
curl -s "http://web.archive.org/cdx/search/cdx?url=*.target.com/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e 's/\/.*//g' | sort -u | anew wayback_subs.txt
```

### 💀 CommonCrawl Extraction
```bash
# ☠️ CommonCrawl subdomain extraction
curl -s "https://index.commoncrawl.org/CC-MAIN-2023-50-index?url=*.target.com&output=json" | jq -r '.url' | sed -e 's_https*://__' -e 's/\/.*//g' | sort -u | anew commoncrawl_subs.txt
```

### 💀 VirusTotal Subdomains
```bash
# ☠️ VirusTotal API
curl -s "https://www.virustotal.com/vtapi/v2/domain/report?apikey=YOUR_API_KEY&domain=target.com" | jq -r '.subdomains[]' 2>/dev/null | anew vt_subs.txt
```

### 💀 DNS Zone Transfer Attempt
```bash
# ☠️ Check for zone transfer vulnerability
dig axfr @ns1.target.com target.com | grep -E "^[a-zA-Z0-9]" | awk '{print $1}' | sed 's/\.$//' | anew zone_transfer.txt
```

### 💀 Reverse IP Lookup
```bash
# ☠️ Find domains on same IP
host target.com | awk '/has address/ {print $4}' | xargs -I@ sh -c 'curl -s "https://api.hackertarget.com/reverseiplookup/?q=@"' | anew reverse_ip.txt
```

### 💀 BGP/ASN Range Scanner
```bash
# ☠️ Get ASN and scan all IP ranges
whois -h whois.radb.net -- '-i origin AS12345' | grep -Eo "([0-9.]+){4}/[0-9]+" | xargs -I@ sh -c 'nmap -sL @ | grep "report for" | cut -d" " -f5' | httpx -silent | anew bgp_hosts.txt
```

### 💀 PTR Records from IP Range
```bash
# ☠️ Mass PTR lookup
prips 192.168.1.0/24 | xargs -P50 -I@ sh -c 'host @ 2>/dev/null | grep "pointer" | cut -d" " -f5' | sed 's/\.$//' | anew ptr_subs.txt
```

### 💀 All-in-One Mega Oneliner
```bash
# ☠️ THE ULTIMATE SUBDOMAIN HUNTER ☠️
(subfinder -d target.com -all -silent; amass enum -passive -d target.com; assetfinder -subs-only target.com; findomain -t target.com -q; chaos -d target.com -silent; curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g'; curl -s "https://api.hackertarget.com/hostsearch/?q=target.com" | cut -d',' -f1; curl -s "http://web.archive.org/cdx/search/cdx?url=*.target.com/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e 's/\/.*//g') | sort -u | httpx -silent -threads 100 | anew mega_subs.txt
```

### 💀 Subdomain Permutation/Bruteforce
```bash
# ☠️ Generate permutations and resolve
cat subs.txt | dnsgen - | shuffledns -d target.com -r resolvers.txt -silent | anew permutation_subs.txt
```

### 💀 DNS Wordlist Bruteforce with PureDNS
```bash
# ☠️ Fast bruteforce with PureDNS
puredns bruteforce wordlist.txt target.com -r resolvers.txt -w puredns_subs.txt
```

### 💀 TLS/SSL Certificate Grabber
```bash
# ☠️ Extract subdomains from SSL certificates
echo target.com | httpx -silent | xargs -I@ sh -c 'echo | openssl s_client -connect @:443 2>/dev/null | openssl x509 -noout -text | grep -oP "DNS:[^\s,]+" | sed "s/DNS://"' | sort -u | anew ssl_subs.txt
```

### 💀 Favicon Hash -> Shodan
```bash
# ☠️ Find related hosts via favicon hash
curl -s https://target.com/favicon.ico | md5sum | awk '{print $1}' | xargs -I@ shodan search "http.favicon.hash:@" --fields ip_str,hostnames | anew favicon_hosts.txt
```

### 💀 Google Dork Subdomain Discovery
```bash
# ☠️ Use Google dorks (manual or with tools)
# site:*.target.com -www
# inurl:target.com
```

---

## 🔐 TLS/SSL Reconnaissance (TLSX)

<div align="center">

```
████████╗██╗     ███████╗██╗  ██╗    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
╚══██╔══╝██║     ██╔════╝╚██╗██╔╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
   ██║   ██║     ███████╗ ╚███╔╝     ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
   ██║   ██║     ╚════██║ ██╔██╗     ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
   ██║   ███████╗███████║██╔╝ ██╗    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
```

**🔐 TLS/SSL Certificate Intelligence with TLSX 🔐**

</div>

### 🔐 Basic TLS Certificate Scan
```bash
# 🔐 Full TLS certificate details extraction
echo target.com | tlsx -san -cn -so -sv -ss -serial -hash md5 -jarm -ja3 -wc -tps -ve -ce -ct -cdn -silent | tee tlsx_full.txt
```

### 🔐 Subdomain Discovery via SANs
```bash
# 🔐 Extract all subdomains from certificate SANs
subfinder -d target.com -silent | tlsx -san -cn -silent -resp-only | grep -oE "[a-zA-Z0-9.-]+\.target\.com" | sort -u | anew san_subdomains.txt
```

### 🔐 Expired Certificate Hunter
```bash
# 🔐 Find hosts with expired SSL certificates
cat hosts.txt | tlsx -expired -silent -cn -so | tee expired_certs.txt
```

### 🔐 Self-Signed Certificate Detection
```bash
# 🔐 Identify self-signed certificates (potential security issue)
cat hosts.txt | tlsx -self-signed -silent -cn -so -hash sha256 | tee self_signed.txt
```

### 🔐 TLS Version Enumeration (Weak TLS)
```bash
# 🔐 Find hosts with deprecated TLS versions (TLS 1.0/1.1)
cat hosts.txt | tlsx -tls-version -silent | grep -E "(tls10|tls11)" | tee weak_tls_versions.txt
```

### 🔐 JARM Fingerprinting Pipeline
```bash
# 🔐 JARM fingerprint for server identification and correlation
subfinder -d target.com -silent | httpx -silent | tlsx -jarm -silent -json | jq -r '[.host, .jarm_hash] | @tsv' | sort -k2 | anew jarm_fingerprints.txt
```

### 🔐 Certificate Chain & Issuer Analysis
```bash
# 🔐 Analyze certificate chain and identify CA
cat hosts.txt | tlsx -so -serial -hash sha256 -ve -ce -json -silent | jq -r '[.host, .issuer_cn, .not_after, .serial] | @tsv' | anew cert_chain_analysis.txt
```

### 🔐 Mass TLS Scan with Cipher Enumeration
```bash
# 🔐 Full cipher suite enumeration + TLS version
subfinder -d target.com -silent | httpx -silent | tlsx -cipher -tls-version -silent -json | jq -r '[.host, .version, .cipher] | @tsv' | anew cipher_enum.txt
```

### 🔐 Mismatched Certificate Detection
```bash
# 🔐 Find certificates where CN doesn't match the hostname
cat hosts.txt | tlsx -mismatched -cn -san -silent | tee mismatched_certs.txt
```

### 🔐 Ultimate TLS Recon Pipeline
```bash
# 🔐 Complete TLS intelligence gathering
subfinder -d target.com -all -silent | httpx -silent -p 443,8443,4443,9443 | tlsx -san -cn -so -sv -ss -serial -expired -self-signed -mismatched -tls-version -jarm -hash sha256 -json -silent | jq -c '{host: .host, cn: .subject_cn, san: .san, issuer: .issuer_cn, expired: .expired, self_signed: .self_signed, tls: .version, jarm: .jarm_hash}' | tee tlsx_full_recon.json
```

---

## 🌐 DNS Intelligence (DNSX)

<div align="center">

```
██████╗ ███╗   ██╗███████╗██╗  ██╗    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔══██╗████╗  ██║██╔════╝╚██╗██╔╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║  ██║██╔██╗ ██║███████╗ ╚███╔╝     ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║  ██║██║╚██╗██║╚════██║ ██╔██╗     ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██████╔╝██║ ╚████║███████║██╔╝ ██╗    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
```

**🌐 DNS Reconnaissance & Intelligence Gathering with DNSX 🌐**

</div>

### 🌐 1. Mass DNS Resolution + Wildcard Filtering
```bash
# 🌐 Resolve subdomains and filter out wildcards
subfinder -d target.com -silent | dnsx -silent -a -resp-only -wd target.com | sort -u | anew resolved_ips.txt
```

### 🌐 2. Multi-Record Type DNS Enumeration
```bash
# 🌐 Query A, AAAA, CNAME, MX, NS, TXT records simultaneously
echo target.com | dnsx -silent -a -aaaa -cname -mx -ns -txt -resp | tee full_dns_records.txt
```

### 🌐 3. CNAME Extraction for Subdomain Takeover
```bash
# 🌐 Find dangling CNAMEs pointing to vulnerable services
subfinder -d target.com -silent | dnsx -silent -cname -resp-only | grep -iE "(s3|cloudfront|herokuapp|github|azure|shopify|fastly|pantheon|zendesk|readme|ghost|surge|bitbucket|wordpress|tumblr)" | anew cname_takeover_candidates.txt
```

### 🌐 4. Reverse DNS (PTR) on IP Ranges
```bash
# 🌐 Discover hidden hosts via reverse DNS lookups
prips 192.168.1.0/24 | dnsx -silent -ptr -resp-only | anew ptr_discovered_hosts.txt
```

### 🌐 5. MX Records for Email Security Analysis
```bash
# 🌐 Extract MX records to identify mail servers and SPF bypass opportunities
cat domains.txt | dnsx -silent -mx -resp | awk '{print $1, $2}' | sort -u | tee mx_records.txt && cat domains.txt | dnsx -silent -txt -resp | grep -i "spf" | anew spf_records.txt
```

### 🌐 6. NS Records + DNS Zone Transfer Check
```bash
# 🌐 Enumerate nameservers and check for misconfigured zone transfers
cat domains.txt | dnsx -silent -ns -resp-only | tee nameservers.txt && cat nameservers.txt | xargs -I@ -P10 sh -c 'host -t axfr target.com @ 2>&1 | grep -v "failed\|timed out" && echo "[ZONE TRANSFER] @"' | anew zone_transfers.txt
```

### 🌐 7. DNS Brute-force with Custom Resolvers
```bash
# 🌐 Mass DNS brute-force with custom resolver list
cat wordlist.txt | sed 's/$/.target.com/' | dnsx -silent -r resolvers.txt -rl 500 -t 200 -retry 3 -resp-only | anew bruteforced_subs.txt
```

### 🌐 8. JSON Output for Advanced Parsing
```bash
# 🌐 Full DNS recon with JSON output for pipeline integration
subfinder -d target.com -silent | dnsx -silent -a -aaaa -cname -mx -ns -txt -ptr -resp -json | jq -c '{host: .host, a: .a, aaaa: .aaaa, cname: .cname, mx: .mx, ns: .ns, txt: .txt}' | tee dns_full_recon.json
```

### 🌐 9. ASN Discovery via DNS + IP Correlation
```bash
# 🌐 Resolve domains, extract unique IPs, and identify ASN ownership
subfinder -d target.com -silent | dnsx -silent -a -resp-only | sort -u | tee target_ips.txt | xargs -I{} sh -c 'whois {} 2>/dev/null | grep -iE "(netname|orgname|asn|origin)" | head -5' | anew asn_info.txt
```

### 🌐 10. Ultimate DNS Recon Pipeline
```bash
# 🌐 Complete DNS intelligence gathering
domain="target.com"; subfinder -d $domain -all -silent | tee subs_$domain.txt | dnsx -silent -a -aaaa -cname -mx -ns -txt -resp -json -o dns_records_$domain.json; cat subs_$domain.txt | dnsx -silent -cname -resp-only | grep -iE "(s3|cloudfront|azure|github)" | anew takeover_$domain.txt; cat dns_records_$domain.json | jq -r '.a[]?' | sort -u | dnsx -silent -ptr -resp-only | anew ptr_$domain.txt; echo "[+] DNS Recon Complete: $(wc -l < subs_$domain.txt) subdomains | $(cat dns_records_$domain.json | wc -l) records"
```

> **🎯 Pro Tip:** Use custom resolvers for better performance: `dnsx -r resolvers.txt -rl 1000`

---

[← Back to README](../Readme.md)
