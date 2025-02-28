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

# AMD driver download page URL
url = "https://www.amd.com/en/support/downloads/drivers.html/graphics/radeon-rx/radeon-rx-7000-series/amd-radeon-rx-7900-xt.html"

# Make the HTTP request and get the HTML content
response = requests.get(url, headers=headers)
html = response.content

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all <article> elements containing driver information
articles = soup.find_all("article", class_="container-fluid")

# Loop through articles to find one that contains "Optional"
download_link = None
for article in articles:
    if article.find("p", string=lambda text: text and "Optional" in text):
        # Find the first <a> link within the same article
        link_tag = article.find("a", href=True)
        if link_tag:
            download_link = link_tag["href"]
            break  # Stop after finding the first valid link

# Print the result
if download_link:
    print(download_link)
else:
    print("Download link not found")
