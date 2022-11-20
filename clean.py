import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.7>
html = requests.get('https://www.amd.com/en/support',headers=headers).content

soup = BeautifulSoup(html, 'html.parser')
a = soup.select('#buttons > div > a')[0]
link = a.get('href')

print(link)
