[← Back to README](../Readme.md)

---

## 📜 JavaScript Recon

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

### Extract All URLs from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(https?://[^\"\'\`\s\<\>]+)" | sort -u | anew js_urls.txt
```

### Find API Endpoints in JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(/api/[^\"\'\`\s\<\>]+|/v[0-9]+/[^\"\'\`\s\<\>]+)" | sort -u
```

### Extract Hardcoded Credentials
```bash
cat js.txt | xargs -I@ curl -s @ | grep -iE "(password|passwd|pwd|secret|api_key|apikey|token|auth)" | sort -u
```

### Extract AWS Keys from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(AKIA[0-9A-Z]{16}|ABIA[0-9A-Z]{16}|ACCA[0-9A-Z]{16}|ASIA[0-9A-Z]{16})" | sort -u | anew aws_keys.txt
```

### Extract Google API Keys from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "AIza[0-9A-Za-z\-_]{35}" | sort -u | anew google_api_keys.txt
```

### Extract Firebase URLs from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "https://[a-zA-Z0-9-]+\.firebaseio\.com|https://[a-zA-Z0-9-]+\.firebase\.com" | sort -u | anew firebase_urls.txt
```

### Extract S3 Buckets from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "[a-zA-Z0-9.-]+\.s3\.amazonaws\.com|s3://[a-zA-Z0-9.-]+|s3-[a-zA-Z0-9-]+\.amazonaws\.com/[a-zA-Z0-9.-]+" | sort -u | anew s3_from_js.txt
```

### Extract Internal IPs from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(10\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|172\.(1[6-9]|2[0-9]|3[0-1])\.[0-9]{1,3}\.[0-9]{1,3}|192\.168\.[0-9]{1,3}\.[0-9]{1,3})" | sort -u | anew internal_ips.txt
```

### Extract Slack Webhooks from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "https://hooks\.slack\.com/services/T[a-zA-Z0-9_]+/B[a-zA-Z0-9_]+/[a-zA-Z0-9_]+" | sort -u | anew slack_webhooks.txt
```

### Extract GitHub Tokens from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(ghp_[a-zA-Z0-9]{36}|gho_[a-zA-Z0-9]{36}|ghu_[a-zA-Z0-9]{36}|ghs_[a-zA-Z0-9]{36}|ghr_[a-zA-Z0-9]{36}|github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59})" | sort -u | anew github_tokens.txt
```

### Extract Private Keys from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "-----BEGIN (RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY( BLOCK)?-----" | sort -u | anew private_keys_found.txt
```

### Extract Email Addresses from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" | sort -u | anew emails_from_js.txt
```

### Extract Hidden Subdomains from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" | sed 's|https\?://||' | cut -d'/' -f1 | sort -u | anew subdomains_from_js.txt
```

### 💀 Extract GraphQL Endpoints from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(graphql|gql|query|mutation)[^\"']*" | grep -oE "/[a-zA-Z0-9/_-]*graphql[a-zA-Z0-9/_-]*" | sort -u | anew graphql_endpoints.txt
```

### 💀 Extract JWT Tokens from JS Files
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*" | sort -u | anew jwt_tokens.txt
```

### 💀 Find Webpack Source Maps
```bash
cat js.txt | sed 's/\.js$/.js.map/' | httpx -silent -mc 200 -ct -match-string "sourcesContent" | anew sourcemaps.txt
```

### 💀 Extract Discord Webhooks from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "https://discord\.com/api/webhooks/[0-9]+/[A-Za-z0-9_-]+" | sort -u | anew discord_webhooks.txt
```

### 💀 Find Hidden Admin Routes in JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "[\"\'][/][a-zA-Z0-9_/-]*(admin|dashboard|manage|config|settings|internal|private|debug|api/v[0-9])[a-zA-Z0-9_/-]*[\"\']" | tr -d "\"'" | sort -u | anew hidden_routes.txt
```

---

[← Back to README](../Readme.md)
