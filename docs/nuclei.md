[← Back to README](../Readme.md)

---

## ⚡ Nuclei Scanning

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

### Custom Tags
```bash
nuclei -l alive.txt -tags cve,rce,sqli,xss -severity critical,high -o tagged_results.txt
```

### Network Scanning
```bash
nuclei -l ips.txt -t network/ -c 25 -o network_vulns.txt
```

---

[← Back to README](../Readme.md)
