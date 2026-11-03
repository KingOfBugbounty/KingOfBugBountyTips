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
| [Setup & Required Tools](docs/setup.md) | Full toolset + BBRF DoD scope config |
| [Subdomain & TLS/DNS Recon](docs/subdomain-recon.md) | Finding subdomains, TLSX, DNSX |
| [JavaScript Recon](docs/js-recon.md) | JS file analysis |
| [XSS Detection](docs/xss.md) | Cross-site scripting |
| [SQL Injection](docs/sqli.md) | SQLi techniques |
| [SSRF & SSTI](docs/ssrf-ssti.md) | Server-side attacks |
| [Web Crawling & Parameter Discovery](docs/web-crawling.md) | Deep crawling methods, hidden params |
| [Content Discovery](docs/content-discovery.md) | Sensitive files |
| [Nuclei Scanning](docs/nuclei.md) | Automated scanning |
| [API Security Testing](docs/api-security.md) | API vulnerabilities |
| [Cloud Security](docs/cloud-security.md) | AWS, GCP, Azure |
| [Automation Scripts & Bash Functions](docs/automation.md) | Ready-to-use scripts, shell productivity |
| [Standalone Scripts](scripts/README.md) | Recon pipeline, HTML reporter, downloader |
| [Templates](templates/README.md) | Nuclei templates & PoC payload fixtures |
| [Data](data/README.md) | Payload lists, sample URL lists, DoD domain list |
| [New Oneliners 2026](docs/oneliners-2026.md) | CVE-2026 exploits & techniques |
| [Oneliners 2024-2025](docs/oneliners-2024-2025.md) | Previous techniques |
| [February 2026 CVE Discovery](docs/cve-feb-2026.md) | Latest CVE recon oneliners |
| [Search Engines, Wordlists & Resources](docs/resources.md) | Hacker search engines, wordlists, learning resources |
| [Contributing](CONTRIBUTING.md) | How to submit a one-liner or technique |

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

## 🛠️ Setup & Required Tools

The full tool list, install scripts (Go/Python/Rust/external), system dependencies, wordlist setup, and the BBRF DoD scope command now live in a dedicated page so this index stays short:

➡️ **[docs/setup.md](docs/setup.md)**

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

Full guidelines (one-liner format, where new CVE entries go, attribution, and what not to commit) now live in **[CONTRIBUTING.md](CONTRIBUTING.md)**.

Quick version:
1. Fork the repo and create a branch (`git checkout -b feature/your-contribution`)
2. Add your one-liner to the right file under `docs/`, following the existing format, with a source/attribution if known
3. Open a PR with a clear description

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

**Last Updated:** July 2026 | **Version:** 4.6

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
