import re
import subprocess
import sys
import time
from pathlib import Path

# ── ANSI colors ───────────────────────────────────────────────────────────────
G, C, Y, R, B, RST = "\033[32m", "\033[36m", "\033[33m", "\033[31m", "\033[34m", "\033[0m"

def validate_domain(domain: str) -> bool:
    return bool(re.match(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$',
        domain
    ))

def step(msg):   print(f"\n{C}[*]{RST} {msg}")
def ok(msg):     print(f"    {G}[+]{RST} {msg}")
def warn(msg):   print(f"    {Y}[!]{RST} {msg}")
def error(msg):  print(f"    {R}[-]{RST} {msg}")
def elapsed(s):  print(f"    {B}[~]{RST} {s:.1f}s")

def run(cmd: list) -> bool:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 and result.stderr:
        warn(result.stderr.strip())
    return result.returncode == 0

def pipe(cmd: str) -> bool:
    return subprocess.run(cmd, shell=True).returncode == 0

def has_results(path: str) -> bool:
    p = Path(path)
    return p.exists() and p.stat().st_size > 0

def count_lines(path: str) -> int:
    try:
        with open(path) as fh:
            return sum(1 for _ in fh)
    except Exception:
        return 0

def tool_exists(name: str) -> bool:
    return subprocess.run(['which', name], capture_output=True).returncode == 0

def skip_or_run(output_file: str, fn):
    """If output_file already has results, skip. Otherwise call fn() and time it."""
    if has_results(output_file):
        ok(f"Skipping — already have {count_lines(output_file)} results")
        return True
    t = time.time()
    fn()
    elapsed(time.time() - t)

# ── Setup ─────────────────────────────────────────────────────────────────────
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
gaufile       = f("gau")
portscan      = f("portscan")
http200       = f("http200")
http200json   = str(outdir / f"{base}_http200.json")
crawKatana    = f("crawling")
unfullDomains = f("unfullDomains")
fullDomains   = f("fulldomains")
full1         = f("fulldomains200")
crawKatanaJS  = f("crawlingJS")
nucleiResp    = f("nuclei")
xssgf         = f("gfxss")
dalfoxfile    = f("dalfox")
htmlreport    = str(outdir / f"{base}_report.html")

allports = ("80,443,81,300,591,593,832,981,1010,1311,1099,2082,2095,2096,2480,"
            "3000,3128,3333,4243,4567,4711,4712,4993,5000,5104,5108,5280,5281,"
            "5601,5800,6543,7000,7001,7396,7474,8000,8001,8008,8014,8042,8060,"
            "8069,8080,8081,8083,8088,8090,8091,8095,8118,8123,8172,8181,8222,"
            "8243,8280,8281,8333,8337,8443,8500,8834,8880,8888,8983,9000,9001,"
            "9043,9060,9080,9090,9091,9200,9443,9502,9800,9981,10000,10250,"
            "11371,12443,15672,16080,17778,18091,18092,20720,32000,55440,55672")
blacklist  = "md,jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico"
katanalist = "js,jsp,json,php,aspx,asp"

scan_start = time.time()

print(f"\n{G}[+]{RST} Starting recon on: {domain}")
print(f"{G}[+]{RST} Output directory:   {outdir}/")

# ── Step 1: Subdomain enumeration ─────────────────────────────────────────────
step("Subdomain enumeration via subfinder")
skip_or_run(subfile, lambda: run(['subfinder', '-all', '-d', domain, '-silent', '-o', subfile]))
ok(f"Subdomains → {subfile} ({count_lines(subfile)})") if has_results(subfile) else warn("No subdomains found")

# ── Step 2: Passive URL discovery via gau ─────────────────────────────────────
step("Passive URL discovery via gau")
if tool_exists('gau'):
    skip_or_run(gaufile, lambda: pipe(f"gau --subs {domain} | anew '{gaufile}'"))
    ok(f"Historical URLs → {gaufile} ({count_lines(gaufile)})") if has_results(gaufile) else warn("No URLs from gau")
else:
    warn("gau not found, skipping")

# ── Step 3: DNS resolution filter ─────────────────────────────────────────────
step("Resolving subdomains via dnsx")
if has_results(subfile):
    skip_or_run(livesubfile, lambda: pipe(f"cat '{subfile}' | dnsx -silent | anew '{livesubfile}'"))
    ok(f"Resolved hosts → {livesubfile} ({count_lines(livesubfile)})") if has_results(livesubfile) else warn("No subdomains resolved")

# ── Step 4: Port scan ─────────────────────────────────────────────────────────
step("Port scanning via naabu")
if has_results(livesubfile):
    skip_or_run(portscan, lambda: pipe(
        f"cat '{livesubfile}' | naabu -silent -p {allports} | anew '{portscan}'"
    ))
    ok(f"Open ports → {portscan} ({count_lines(portscan)})") if has_results(portscan) else warn("No open ports found")

# ── Step 5: HTTP probing ───────────────────────────────────────────────────────
step("HTTP probing via httpx")
if has_results(portscan):
    skip_or_run(http200, lambda: pipe(
        # single httpx run: JSON piped to tee for report, URLs extracted for pipeline
        f"cat '{portscan}' | httpx -silent -json | tee '{http200json}' "
        f"| grep -oP '\"url\":\"\\K[^\"]+' | anew '{http200}'"
    ))
    ok(f"Live hosts → {http200} ({count_lines(http200)})") if has_results(http200) else warn("No live HTTP hosts found")

# ── Step 6: Crawl live hosts ───────────────────────────────────────────────────
step("Crawling live hosts via katana")
if has_results(http200):
    skip_or_run(crawKatana, lambda: pipe(
        f"cat '{http200}' | katana -d 10 -silent -o '{crawKatana}' -ef {blacklist} -em {katanalist}"
    ))
    ok(f"Crawl results → {crawKatana} ({count_lines(crawKatana)})") if has_results(crawKatana) else warn("Nothing crawled")

# ── Step 7: Expand domain scope ────────────────────────────────────────────────
step("Expanding domain list via unfurl")
if has_results(crawKatana):
    skip_or_run(full1, lambda: (
        pipe(f"cat '{crawKatana}' | unfurl domains | anew '{unfullDomains}'"),
        pipe(f"cat '{unfullDomains}' '{subfile}' | anew '{fullDomains}'"),
        pipe(f"cat '{fullDomains}' | httpx -silent | anew '{full1}'"),
    ))
    ok(f"Expanded live scope → {full1} ({count_lines(full1)})") if has_results(full1) else warn("No additional hosts discovered")

# ── Step 8: Deep JS/API crawl ──────────────────────────────────────────────────
step("Deep JS/API crawl via katana")
if has_results(full1):
    skip_or_run(crawKatanaJS, lambda: pipe(
        f"cat '{full1}' | katana -d 10 -silent -em {katanalist} -o '{crawKatanaJS}'"
    ))
    ok(f"JS/API endpoints → {crawKatanaJS} ({count_lines(crawKatanaJS)})") if has_results(crawKatanaJS) else warn("No JS/API endpoints found")

# ── Step 9: Nuclei vulnerability scan ─────────────────────────────────────────
step("Nuclei vulnerability scan")
if has_results(full1):
    skip_or_run(nucleiResp, lambda: pipe(
        f"cat '{full1}' | nuclei -severity low,medium,high,critical -silent "
        f"-o '{nucleiResp}' -H 'User-Agent: OFJAAAH'"
    ))
    ok(f"Nuclei results → {nucleiResp} ({count_lines(nucleiResp)})") if has_results(nucleiResp) else ok("No vulnerabilities found by nuclei")

# ── Step 10: XSS detection (gf + dalfox) ──────────────────────────────────────
step("XSS candidate extraction via gf")
if has_results(crawKatana):
    if not has_results(xssgf):
        pipe(f"cat '{crawKatana}' | gf xss | anew '{xssgf}'")
    if has_results(xssgf):
        ok(f"XSS candidates → {xssgf} ({count_lines(xssgf)})")
        step("XSS exploitation check via dalfox")
        skip_or_run(dalfoxfile, lambda: pipe(
            f"cat '{xssgf}' | dalfox pipe --skip-bav --mining-dom --deep-domxss "
            f"--ignore-return -b 'https://ofjaaaaah.xss.ht/' --follow-redirects "
            f"--silence | anew '{dalfoxfile}'"
        ))
        ok(f"Dalfox results → {dalfoxfile} ({count_lines(dalfoxfile)})") if has_results(dalfoxfile) else ok("No XSS confirmed by dalfox")
    else:
        ok("No XSS candidates found by gf")

# ── Step 11: HTML report ───────────────────────────────────────────────────────
step("Generating HTML report via resolvhtml")
resolvhtml_bin = Path(__file__).parent / "resolvhtml"
if not resolvhtml_bin.exists():
    src = Path(__file__).parent / "resolvhtml.go"
    if src.exists():
        ok("Building resolvhtml binary...")
        run(['go', 'build', '-o', str(resolvhtml_bin), str(src)])
if has_results(http200json) and resolvhtml_bin.exists():
    pipe(f"cat '{http200json}' | '{resolvhtml_bin}' '{htmlreport}'")
    ok(f"HTML report → {htmlreport}") if Path(htmlreport).exists() else warn("Report generation failed")
else:
    warn("Skipping — no httpx JSON output or resolvhtml binary not built")

# ── Step 12: Notify summary ────────────────────────────────────────────────────
# Uncomment and configure provider to enable Discord/Slack/Telegram notifications
# step("Sending notification via notify")
# summary_msg = f"Recon done: {domain} | subs={count_lines(subfile)} live={count_lines(http200)} nuclei={count_lines(nucleiResp)} xss={count_lines(dalfoxfile)}"
# pipe(f"echo '{summary_msg}' | notify -provider discord -silent")

# ── Summary table ──────────────────────────────────────────────────────────────
total_secs = time.time() - scan_start
mins, secs = divmod(int(total_secs), 60)

rows = [
    ("Subdomains",       subfile),
    ("Live subdomains",  livesubfile),
    ("Historical URLs",  gaufile),
    ("Open ports",       portscan),
    ("Live HTTP hosts",  http200),
    ("Crawled URLs",     crawKatana),
    ("JS/API endpoints", crawKatanaJS),
    ("Nuclei findings",  nucleiResp),
    ("XSS candidates",   xssgf),
    ("XSS confirmed",    dalfoxfile),
]

print(f"\n{G}{'─'*46}{RST}")
print(f"{G}  Recon Summary › {domain}{RST}")
print(f"{G}{'─'*46}{RST}")
for label, path in rows:
    n = count_lines(path) if has_results(path) else 0
    color = G if n > 0 else RST
    print(f"  {label:<22} {color}{n:>6}{RST}")
print(f"{G}{'─'*46}{RST}")
print(f"  Total time:            {B}{mins}m {secs}s{RST}")
print(f"{G}{'─'*46}{RST}\n")
