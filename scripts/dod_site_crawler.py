"""
dod_site_crawler.py

Purpose:
    Scrape the official DoD "Military Departments / DOD Websites" index page
    and print every hyperlink found, as a starting point for building/updating
    the DoD *.mil domain list used in the DoD VDP scope (see data/DoD Domains.txt
    and docs/setup.md).

Usage:
    python3 scripts/dod_site_crawler.py

Requirements:
    pip install requests beautifulsoup4

Notes:
    - Only touch defense.gov's own public index page; this is informational
      recon of a public page, not testing against DoD assets. Always follow
      the DoD VDP program rules before testing anything discovered this way:
      https://hackerone.com/deptofdefense
"""
from bs4 import BeautifulSoup
import requests
url = "https://www.defense.gov/Resources/Military-Departments/DOD-Websites/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print("The href links are :")
for link in soup.find_all('a'):
   print(link.get('href'))
