import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate"
}
html = requests.get(
    'https://www.amd.com/en/support/downloads/drivers.html/graphics/radeon-rx/radeon-rx-7000-series/amd-radeon-rx-7900-xt.html',
    headers=headers).content

# old method
soup = BeautifulSoup(html, 'html.parser')
elements = soup.select(
    'article.container-fluid > div > div:nth-child(5) > div > a')
link = elements[0]['href']
"""
soup = BeautifulSoup(html, 'html.parser')
divs = soup.find_all('div', class_='field__item')

link = None
for div in divs:
    if div.text.strip() == 'Auto-Detect and Install':
        link_div = div.find_next('div', class_='field--type-uri')
        link = link_div.find('a')['href']
        break
"""

if link:
    print(link)
else:
    print("Link não encontrado")
