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
