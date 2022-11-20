import sys
import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.amd.com/en/support')

soup = BeautifulSoup(html, 'html.parser')
a = soup.select('#buttons > div > a')
link= a[href]

sys.stdout.write(cleaned)
sys.stdout.flush()
