import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
html = requests.get('https://www.amd.com/en/support/graphics/amd-radeon-5700-series/amd-radeon-rx-5700-series/amd-radeon-rx-5700-xt',headers=headers).content

soup = BeautifulSoup(html, 'html.parser')
#a = soup.select('#buttons > div > a')[0]
a = soup.select('amd_support_driver_list > div.views-element-container > div > div.view-content > details:nth-child(1) > div > div:nth-child(5) > div > span > div > div.driver-metadata > div.field.field--name-url.field--type-uri.field--label-hidden > a')[0]
link = a.get('href')

print(link)
