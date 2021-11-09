import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.digitalseo.in/')
data = r.text
soup = BeautifulSoup(data)

for rate in soup.find_all('@'):
    print(rate.text)
