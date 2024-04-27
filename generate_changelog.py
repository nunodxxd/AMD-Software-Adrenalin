import sys
import os
import requests
from bs4 import BeautifulSoup
import markdownify
import hashlib

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
html = requests.get(f'https://www.amd.com/en/support/kb/release-notes/rn-rad-win-{sys.argv[1]}',headers=headers).content

soup = BeautifulSoup(html, 'html.parser')

selected_html = soup.select('div.center-container > div > div.cmp-container__content > div > div[data-cmp-data-layer]')[0].decode_contents()

"""
for x in range(1,7):
        selected_html += str(soup.select(f'#block-amd-content > article > div > div.field.field--name-body.field--type-text-with-summary.field--label-hidden.field__item > *:nth-child({x})')[0])
"""
#hash generator
exe_files = [f for f in os.listdir('./driver') if f.endswith('.exe')]

selected_html += '<h2>SHA256 checksum:</h2> <ul>' 

for file in exe_files:
    path_to_file = f'./driver/{file}'
    hasher = hashlib.sha256()
    with open(path_to_file, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    hash_value = hasher.hexdigest()
    
    selected_html += f'<li>{file}: {hash_value}</li>'

selected_html += '</ul>'

#export markdown
markdown = markdownify.markdownify(selected_html, heading_style="ATX")

print(markdown)
