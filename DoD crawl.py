from bs4 import BeautifulSoup
import requests
url = "https://www.defense.gov/Resources/Military-Departments/DOD-Websites/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print("The href links are :")
for link in soup.find_all('a'):
   print(link.get('href'))
