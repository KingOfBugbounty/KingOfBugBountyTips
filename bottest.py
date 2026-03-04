import re
import subprocess
import sys
from pathlib import Path

# ANSI colors
G, C, Y, R, RST = "\033[32m", "\033[36m", "\033[33m", "\033[31m", "\033[0m"

def validate_domain(domain: str) -> bool:
    return bool(re.match(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$',
        domain
    ))

def step(msg):  print(f"{C}[*]{RST} {msg}")
def ok(msg):    print(f"{G}[+]{RST} {msg}")
def warn(msg):  print(f"{Y}[!]{RST} {msg}")
def error(msg): print(f"{R}[-]{RST} {msg}")

def run(cmd: list) -> bool:
    """Run a single command without a shell."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 and result.stderr:
        warn(result.stderr.strip())
    return result.returncode == 0

def pipe(cmd: str) -> bool:
    """Run a shell pipeline. Only call this with validated/safe values."""
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0

def has_results(path: str) -> bool:
    p = Path(path)
    return p.exists() and p.stat().st_size > 0


domain = input("Domain to Search: ").strip().lower()

if not validate_domain(domain):
    error("Invalid domain. Only alphanumeric, hyphens, and dots allowed.")
    sys.exit(1)

base   = domain.split('.')[0]
outdir = Path(f"recon_{base}")
outdir.mkdir(exist_ok=True)

def f(name): return str(outdir / f"{base}_{name}.txt")

subfile       = f("subs")
livesubfile   = f("subs_live")
portscan      = f("portscan")
http200       = f("http200")
crawKatana    = f("crawling")
unfullDomains = f("unfullDomains")
fullDomains   = f("fulldomains")
full1         = f("fulldomains200")
crawKatanaJS  = f("crawlingJS")
nucleiResp    = f("nuclei")
xssgf         = f("gfxss")
dalfoxfile    = f("dalfox")

allports  = ("80,443,81,300,591,593,832,981,1010,1311,1099,2082,2095,2096,2480,"
             "3000,3128,3333,4243,4567,4711,4712,4993,5000,5104,5108,5280,5281,"
             "5601,5800,6543,7000,7001,7396,7474,8000,8001,8008,8014,8042,8060,"
             "8069,8080,8081,8083,8088,8090,8091,8095,8118,8123,8172,8181,8222,"
             "8243,8280,8281,8333,8337,8443,8500,8834,8880,8888,8983,9000,9001,"
             "9043,9060,9080,9090,9091,9200,9443,9502,9800,9981,10000,10250,"
             "11371,12443,15672,16080,17778,18091,18092,20720,32000,55440,55672")
blacklist = "md,jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico"
katanalist = "js,jsp,json,php,aspx,asp"

print(f"\n{G}[+]{RST} Starting recon on: {domain}")
print(f"{G}[+]{RST} Output directory:   {outdir}/\n")

# ── Step 1: Subdomain enumeration ────────────────────────────────────────────
step("Subdomain enumeration via subfinder")
run(['subfinder', '-all', '-d', domain, '-silent', '-o', subfile])
if has_results(subfile):
    ok(f"Subdomains → {subfile}")
else:
    warn("No subdomains found. Continuing anyway...")

# ── Step 2: DNS resolution filter ────────────────────────────────────────────
step("Resolving subdomains via dnsx")
if has_results(subfile):
    pipe(f"cat '{subfile}' | dnsx -silent | anew '{livesubfile}'")
    ok(f"Resolved hosts → {livesubfile}") if has_results(livesubfile) else warn("No subdomains resolved")

# ── Step 3: Port scan ─────────────────────────────────────────────────────────
step("Port scanning via naabu")
if has_results(livesubfile):
    pipe(f"cat '{livesubfile}' | naabu -silent -p {allports} | anew '{portscan}'")
    ok(f"Open ports → {portscan}") if has_results(portscan) else warn("No open ports found")

# ── Step 4: HTTP probing ──────────────────────────────────────────────────────
step("HTTP probing via httpx")
if has_results(portscan):
    pipe(f"cat '{portscan}' | httpx -silent | anew '{http200}'")
    ok(f"Live hosts → {http200}") if has_results(http200) else warn("No live HTTP hosts found")

# ── Step 4: Crawl live hosts ──────────────────────────────────────────────────
step("Crawling live hosts via katana")
if has_results(http200):
    pipe(f"cat '{http200}' | katana -d 10 -silent -o '{crawKatana}' -ef {blacklist} -em {katanalist}")
    ok(f"Crawl results → {crawKatana}") if has_results(crawKatana) else warn("Nothing crawled")

# ── Step 5: Expand domain scope ───────────────────────────────────────────────
step("Expanding domain list via unfurl")
if has_results(crawKatana):
    pipe(f"cat '{crawKatana}' | unfurl domains | anew '{unfullDomains}'")
    pipe(f"cat '{unfullDomains}' '{subfile}' | anew '{fullDomains}'")
    pipe(f"cat '{fullDomains}' | httpx -silent | anew '{full1}'")
    ok(f"Expanded live scope → {full1}") if has_results(full1) else warn("No additional hosts discovered")

# ── Step 6: Deep JS/API crawl ─────────────────────────────────────────────────
step("Deep JS/API crawl via katana")
if has_results(full1):
    pipe(f"cat '{full1}' | katana -d 10 -silent -em {katanalist} -o '{crawKatanaJS}'")
    ok(f"JS/API endpoints → {crawKatanaJS}") if has_results(crawKatanaJS) else warn("No JS/API endpoints found")

# ── Step 7: Nuclei vulnerability scan ────────────────────────────────────────
step("Nuclei vulnerability scan")
if has_results(full1):
    # -H requires the full "Header: Value" string quoted as one argument
    pipe(f"cat '{full1}' | nuclei -severity low,medium,high,critical -silent -o '{nucleiResp}' -H 'User-Agent: OFJAAAH'")
    ok(f"Nuclei results → {nucleiResp}") if has_results(nucleiResp) else ok("No vulnerabilities found by nuclei")

# ── Step 8: XSS detection (gf + dalfox) ──────────────────────────────────────
step("XSS candidate extraction via gf")
if has_results(crawKatana):
    pipe(f"cat '{crawKatana}' | gf xss | anew '{xssgf}'")
    if has_results(xssgf):
        ok(f"XSS candidates → {xssgf}")
        step("XSS exploitation check via dalfox")
        pipe(
            f"cat '{xssgf}' | dalfox pipe --skip-bav --mining-dom --deep-domxss "
            f"--ignore-return -b 'https://ofjaaaaah.xss.ht/' --follow-redirects "
            f"--silence | anew '{dalfoxfile}'"
        )
        ok(f"Dalfox results → {dalfoxfile}") if has_results(dalfoxfile) else ok("No XSS confirmed by dalfox")
    else:
        ok("No XSS candidates found by gf")

print(f"\n{G}[+]{RST} Recon complete. All results saved in: {outdir}/\n")
