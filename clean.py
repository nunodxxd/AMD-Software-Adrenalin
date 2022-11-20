import sys
from bs4 import BeautifulSoup

def clean(txt):
    soup = BeautifulSoup(txt, 'html.parser')
    return soup.select('#buttons > div > a')[href]


if __name__ == "__main__":
    cleaned = clean(sys.stdin.read())
    sys.stdout.write(cleaned)
    sys.stdout.flush()
