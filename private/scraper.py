import urllib.request
from bs4 import BeautifulSoup


class Scrappy:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        data = urllib.request.urlopen(self.url)
        html = data.read()
        parser = "html.parser"
        soup = BeautifulSoup(html, parser)
        for tag in soup.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print(f"\n{url}")


link = input("Paste your link here: ")
Scrappy(link).scrape()
