import sys
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.7>
html = requests.get('https://www.amd.com/en/support/kb/release-notes/rn-rad-win-'+sys.argv[1],headers=headers).content

soup = BeautifulSoup(html, 'html.parser')
a = soup.select('a[href*="/drivers/whql"]')
link = a[0].get('href')

print(link)
