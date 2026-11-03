[← Back to README](../Readme.md)

---

## 📁 Content Discovery

### Ffuf Directory Bruteforce
```bash
ffuf -u https://target.com/FUZZ -w wordlist.txt -mc 200,301,302,403 -ac -c -t 100
```

### 💀 Recursive Fuzzing - ffuf Deep Scan
```bash
# ☠️ Recursive directory bruteforce with depth 3
ffuf -u https://target.com/FUZZ -w wordlist.txt -recursion -recursion-depth 3 -mc 200,301,302,403 -ac -c -t 100 -o ffuf_recursive.json -of json
```

### 💀 Feroxbuster Full Recursive Scan
```bash
# ☠️ Deep recursive scan with auto-tune and smart filtering
feroxbuster -u https://target.com -w wordlist.txt -d 5 -L 4 --auto-tune -C 404,500 --smart -o ferox_results.txt
```

### 💀 Feroxbuster Multi-Target Recursive
```bash
# ☠️ Scan multiple targets from file with recursion
cat alive.txt | xargs -I@ feroxbuster -u @ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -d 3 -t 50 --no-state -q -o ferox_@.txt
```

### 💀 ffuf + Feroxbuster Pipeline (Extensions + Recursion)
```bash
# ☠️ Find directories with ffuf, then deep scan each with feroxbuster
ffuf -u https://target.com/FUZZ -w wordlist.txt -mc 200,301,302 -ac -c -t 100 -o dirs.json -of json && cat dirs.json | jq -r '.results[].url' | xargs -I@ feroxbuster -u @ -w wordlist.txt -x php,asp,aspx,jsp,html,js -d 2 -t 30 -q
```

### 💀 Recursive Fuzzing with Extensions Mass Scan
```bash
# ☠️ ffuf recursive with multiple extensions + backup files
ffuf -u https://target.com/FUZZ -w wordlist.txt -recursion -recursion-depth 2 -e .php,.asp,.aspx,.jsp,.html,.js,.json,.xml,.bak,.old,.txt,.conf,.config,.zip,.tar.gz -mc 200,301,302,403,500 -ac -t 80 -rate 100 -o recursive_ext.json
```

### 💀 Feroxbuster Parallel Recursive Scan
```bash
# ☠️ Parallel scan with multiple wordlists and extensions
feroxbuster -u https://target.com -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -x php,asp,aspx,jsp,bak,old,zip -d 4 -t 100 -L 5 --parallel 10 --dont-extract-links -C 404 -o ferox_parallel.txt
```

### 💀 Feroxbuster Silent Recursive + Headers
```bash
# ☠️ Stealth recursive scan with custom headers and rate limiting
feroxbuster -u https://target.com -w wordlist.txt -d 3 -t 30 -r -k --random-agent -H "X-Forwarded-For: 127.0.0.1" -H "X-Custom-IP-Authorization: 127.0.0.1" --rate-limit 50 -C 400,401,403,404,500 -q -o ferox_stealth.txt
```

### 💀 Feroxbuster Extract Links + Recursive
```bash
# ☠️ Extract links from responses and add to scan queue recursively
feroxbuster -u https://target.com -w wordlist.txt -d 5 --extract-links --collect-words --collect-backups -x php,html,js,json -t 50 -o ferox_extracted.txt
```

### 💀 Feroxbuster Resume + Filter by Size
```bash
# ☠️ Smart filtering by response size and resumable state
feroxbuster -u https://target.com -w wordlist.txt -d 4 -S 0 -W 1 --filter-status 404,500 --filter-words 20 --filter-lines 5 --resume-from ferox_state.json --state-file ferox_state.json -o ferox_filtered.txt
```

### 💀 Feroxbuster API Endpoints Discovery
```bash
# ☠️ Recursive API fuzzing with JSON content-type
feroxbuster -u https://target.com/api -w /usr/share/seclists/Discovery/Web-Content/api/api-endpoints.txt -d 3 -x json -t 50 -H "Accept: application/json" -H "Content-Type: application/json" --dont-extract-links -m GET,POST -o ferox_api.txt
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

### Source Code Leak
```bash
cat urls.txt | httpx -silent -path /.svn/entries,/.bzr/README,/CVS/Root -mc 200 | anew vcs_exposed.txt
```

### Config Files
```bash
cat alive.txt | httpx -silent -path /config.json,/config.yaml,/config.yml,/settings.json,/app.config -mc 200 | anew configs.txt
```

### Database Files
```bash
cat alive.txt | httpx -silent -path /database.sql,/db.sql,/backup.sql,/dump.sql -mc 200 | anew db_files.txt
```

---

[← Back to README](../Readme.md)
