import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.freelancer.com/', 'lxml')
# r = BeautifulSoup(requests.get('http://www.digitalseo.in/').text, 'lxml')
data = r.text
soup = BeautifulSoup(data, 'lxml')

for rate in soup.find_all('@'):
    print(rate.text)
