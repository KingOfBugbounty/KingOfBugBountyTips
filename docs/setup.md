[← Back to README](../Readme.md)

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

[← Back to README](../Readme.md)
