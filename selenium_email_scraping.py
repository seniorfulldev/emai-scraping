import cloudscraper
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.sportsmansguide.com/productlist?k=walther-ppk', 'lxml')
# r = BeautifulSoup(requests.get('http://www.digitalseo.in/').text, 'lxml')
data = r.text
soup = BeautifulSoup(data, 'lxml')

url = "https://author.today"
scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False
    }
)
print(scraper.post(url).status_code)
print(soup)
for rate in soup.find_all('@'):
    print(rate.text)
