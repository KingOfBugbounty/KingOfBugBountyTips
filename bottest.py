import json
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
    return subprocess.run(['/bin/bash', '-o', 'pipefail', '-c', cmd]).returncode == 0

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

def output_directory(domain: str) -> Path:
    return Path(f"recon_{domain}")


def file_state(paths):
    state = {}
    for path in paths:
        stat = Path(path).stat()
        state[str(path)] = [stat.st_size, stat.st_mtime_ns]
    return state


def skip_or_run(output_file: str, fn, *, inputs=(), extra_outputs=()):
    """Resume unchanged completed steps; empty dependencies clear stale results."""
    outputs = [output_file, *extra_outputs]
    marker = Path(f"{output_file}.done.json")
    try:
        if json.loads(marker.read_text()) == file_state([*inputs, *outputs]):
            ok(f"Skipping — completed ({count_lines(output_file)} results)")
            return True
    except (OSError, ValueError):
        pass

    # Unmarked files may be partial. Start clean, including append-only outputs.
    if marker.exists():
        marker.unlink()
    for output in outputs:
        if Path(output).exists():
            Path(output).unlink()
    t = time.time()
    if all(has_results(path) for path in inputs) and fn() is not True:
        raise RuntimeError(f"Step failed: {output_file}; rerun to retry")
    for output in outputs:
        Path(output).touch(exist_ok=True)
    # Atomic replacement keeps interruptions from leaving a valid-looking marker.
    pending = marker.with_suffix('.tmp')
    pending.write_text(json.dumps(file_state([*inputs, *outputs])))
    pending.replace(marker)
    elapsed(time.time() - t)
    return True


def probe_http(source: str, urls: str, records: str) -> bool:
    """Keep httpx JSONL for reports and parse URLs without GNU grep."""
    with open(records, 'w') as output:
        result = subprocess.run(['httpx', '-silent', '-json', '-l', source], stdout=output)
    if result.returncode != 0:
        return False
    seen = set()
    with open(records) as source_file, open(urls, 'w') as output:
        for line in source_file:
            if not line.strip():
                continue
            url = json.loads(line).get('url')
            if isinstance(url, str) and url and url not in seen:
                output.write(url + '\n')
                seen.add(url)
    return True


def extract_xss(source: str, output_file: str) -> bool:
    # grep (used by gf) returns 1 for a successful search with no matches.
    with open(source) as source_file:
        result = subprocess.run(['gf', 'xss'], stdin=source_file, capture_output=True, text=True)
    if result.stderr or result.returncode not in (0, 1):
        if result.stderr:
            warn(result.stderr.strip())
        return False
    Path(output_file).write_text(''.join(dict.fromkeys(result.stdout.splitlines(keepends=True))))
    return True


def main():
    # ── Setup ─────────────────────────────────────────────────────────────────────
    domain = input("Domain to Search: ").strip().lower()

    if not validate_domain(domain):
        error("Invalid domain. Only alphanumeric, hyphens, and dots allowed.")
        sys.exit(1)

    base   = domain
    outdir = output_directory(domain)
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
    skip_or_run(livesubfile, lambda: pipe(f"cat '{subfile}' | dnsx -silent | anew '{livesubfile}'"), inputs=[subfile])
    ok(f"Resolved hosts → {livesubfile} ({count_lines(livesubfile)})") if has_results(livesubfile) else warn("No subdomains resolved")

    # ── Step 4: Port scan ─────────────────────────────────────────────────────────
    step("Port scanning via naabu")
    skip_or_run(portscan, lambda: pipe(
        f"cat '{livesubfile}' | naabu -silent -p {allports} | anew '{portscan}'"
    ), inputs=[livesubfile])
    ok(f"Open ports → {portscan} ({count_lines(portscan)})") if has_results(portscan) else warn("No open ports found")

    # ── Step 5: HTTP probing ───────────────────────────────────────────────────────
    step("HTTP probing via httpx")
    skip_or_run(http200, lambda: probe_http(portscan, http200, http200json),
                inputs=[portscan], extra_outputs=[http200json])
    ok(f"Live hosts → {http200} ({count_lines(http200)})") if has_results(http200) else warn("No live HTTP hosts found")

    # ── Step 6: Crawl live hosts ───────────────────────────────────────────────────
    step("Crawling live hosts via katana")
    skip_or_run(crawKatana, lambda: pipe(
        f"cat '{http200}' | katana -d 10 -silent -o '{crawKatana}' -ef {blacklist} -em {katanalist}"
    ), inputs=[http200])
    ok(f"Crawl results → {crawKatana} ({count_lines(crawKatana)})") if has_results(crawKatana) else warn("Nothing crawled")

    # ── Step 7: Expand domain scope ────────────────────────────────────────────────
    step("Expanding domain list via unfurl")
    skip_or_run(full1, lambda: (
        pipe(f"cat '{crawKatana}' | unfurl domains | anew '{unfullDomains}'")
        and pipe(f"cat '{unfullDomains}' '{subfile}' | anew '{fullDomains}'")
        and pipe(f"cat '{fullDomains}' | httpx -silent | anew '{full1}'")
    ), inputs=[crawKatana, subfile], extra_outputs=[unfullDomains, fullDomains])
    ok(f"Expanded live scope → {full1} ({count_lines(full1)})") if has_results(full1) else warn("No additional hosts discovered")

    # ── Step 8: Deep JS/API crawl ──────────────────────────────────────────────────
    step("Deep JS/API crawl via katana")
    skip_or_run(crawKatanaJS, lambda: pipe(
        f"cat '{full1}' | katana -d 10 -silent -em {katanalist} -o '{crawKatanaJS}'"
    ), inputs=[full1])
    ok(f"JS/API endpoints → {crawKatanaJS} ({count_lines(crawKatanaJS)})") if has_results(crawKatanaJS) else warn("No JS/API endpoints found")

    # ── Step 9: Nuclei vulnerability scan ─────────────────────────────────────────
    step("Nuclei vulnerability scan")
    skip_or_run(nucleiResp, lambda: pipe(
        f"cat '{full1}' | nuclei -severity low,medium,high,critical -silent "
        f"-o '{nucleiResp}' -H 'User-Agent: OFJAAAH'"
    ), inputs=[full1])
    ok(f"Nuclei results → {nucleiResp} ({count_lines(nucleiResp)})") if has_results(nucleiResp) else ok("No vulnerabilities found by nuclei")

    # ── Step 10: XSS detection (gf + dalfox) ──────────────────────────────────────
    step("XSS candidate extraction via gf")
    skip_or_run(xssgf, lambda: extract_xss(crawKatana, xssgf), inputs=[crawKatana])
    if has_results(xssgf):
        ok(f"XSS candidates → {xssgf} ({count_lines(xssgf)})")
    else:
        ok("No XSS candidates found by gf")
    step("XSS exploitation check via dalfox")
    skip_or_run(dalfoxfile, lambda: pipe(
        f"cat '{xssgf}' | dalfox pipe --skip-bav --mining-dom --deep-domxss "
        f"--ignore-return -b 'https://ofjaaaaah.xss.ht/' --follow-redirects "
        f"--silence | anew '{dalfoxfile}'"
    ), inputs=[xssgf])
    ok(f"Dalfox results → {dalfoxfile} ({count_lines(dalfoxfile)})") if has_results(dalfoxfile) else ok("No XSS confirmed by dalfox")

    # ── Step 11: HTML report ───────────────────────────────────────────────────────
    step("Generating HTML report via resolvhtml")
    resolvhtml_bin = Path(__file__).parent / "resolvhtml"
    if not resolvhtml_bin.exists():
        src = Path(__file__).parent / "resolvhtml.go"
        if src.exists():
            ok("Building resolvhtml binary...")
            if not run(['go', 'build', '-o', str(resolvhtml_bin), str(src)]):
                raise RuntimeError('Report binary build failed')
    if has_results(http200json) and resolvhtml_bin.exists():
        if not pipe(f"cat '{http200json}' | '{resolvhtml_bin}' '{htmlreport}'"):
            raise RuntimeError('Report generation failed')
        ok(f"HTML report → {htmlreport}") if Path(htmlreport).exists() else warn("Report generation failed")
    else:
        if Path(htmlreport).exists():
            Path(htmlreport).unlink()
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


if __name__ == '__main__':
    try:
        main()
    except (OSError, RuntimeError, ValueError) as exc:
        error(str(exc))
        sys.exit(1)
