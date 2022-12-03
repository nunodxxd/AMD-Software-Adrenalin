import sys
import requests
from bs4 import BeautifulSoup
import markdownify

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
html = requests.get(f'https://www.amd.com/en/support/kb/release-notes/rn-rad-win-{sys.argv[1]}',headers=headers).content

soup = BeautifulSoup(html, 'html.parser')

selected_html = ''
for x in range(1,7):
        selected_html += str(soup.select(f'#block-amd-content > article > div > div.field.field--name-body.field--type-text-with-summary.field--label-hidden.field__item > *:nth-child({x})')[0])

markdown = markdownify.markdownify(selected_html, heading_style="ATX")

print(markdown)
