"""
download_links.py

Purpose:
    Bulk-download a list of files from URLs, one per line, into the current
    directory. Originally used to pull ProjectDiscovery Chaos dataset ZIPs
    (see data/chaos-dataset-links.txt for an example input list).

Usage:
    1. Put one URL per line in a file named "links.txt" (same directory).
    2. Run: python3 scripts/download_links.py
    Downloaded files are named after the last path segment of each URL and
    saved into the current working directory.

Requirements:
    pip install requests

Notes:
    - No retry/timeout handling — large or flaky downloads may need a more
      robust tool (e.g. `aria2c -i links.txt` or `wget -i links.txt`).
"""
import requests

def download_content(url, output_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded content from {url} saved to {output_path}")
    else:
        print(f"Failed to download content from {url}")

file_path = "links.txt"

output_directory = "."

with open(file_path, 'r') as file:
    links = file.read().splitlines()

# Loop para fazer o download de cada link
for link in links:
    filename = link.split('/')[-1]  # Obtém o nome do arquivo a partir da URL
    output_path = f"{output_directory}/{filename}"
    download_content(link, output_path)
