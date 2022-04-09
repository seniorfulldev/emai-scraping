# from urllib.request import urlopen
import re
from time import sleep
import requests
from lxml.html import parse
from bs4 import BeautifulSoup
import concurrent.futures
import urllib.parse
import json

import os
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# get your user key from LambdaTest platform and import using environment variables
# username = os.environ.get("LT_USERNAME")
# access_key = os.environ.get("LT_ACCESS_KEY")
 
# Username and Access Key assigned as String variables
username = "wolfman199311@gmail.com"
access_key = "qh6Q2M7fetERX1wv7mGOrldGOWmu3ejwPyzTpJ7bdSXZk3iaIl"
# URL TO SCRAP
make = "Sig Sauer"
model = "P320"
type="Barrel"
params = "Compatible Make=%s&Compatible Model=%s %s&Type=%s" %(make, make, model, type)
url1 = "https://www.midwayusa.com/s?%s" % params.replace(' ', '+')
print(url1)

class MidwayusaScraper:
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    def setUp(self):
        capabilities = {
                "build" : "midwayusa",
                "name" : "gun parts",
                "platform" : "Windows 10",
                "browserName" : "Chrome",
                "version" : "100.0",
                "selenium_version" : "4.1.2",
                "geoLocation" : "US",
                "chrome.driver" : "100.0",
                "headless" : True
            }
        self.driver = webdriver.Remote(
           command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
           desired_capabilities= capabilities)
 
    def tearDown(self):
        self.driver.quit()
 
    def scrapTopic(self,url):
        driver = self.driver
 
        # Url
        driver.get(url)
        
        source = driver.page_source
        # scraping title
        title_list = [] 
        soup = bs(source,"html.parser")
        for table in soup.findAll("table", class_="product-specs-table padding-none stack-l width-100"):
            for span in table.findAll("span"):
                title_list.append(span.text)
            for div in table.findAll("div", class_="product-specs-table-definition-name no-value"):
                title_list.append(div.text)
        return title_list
        
 

def getdata(url): 
    r = requests.get(url) 
    if r.status_code == 200:
        print("________________________%s" %url) 
        return r.text 
    return {"status": "error", "data": 'No existing data.'}   
# parsed = parse(urlopen(url))
htmldata = getdata(url1) 
soup = BeautifulSoup(htmldata, 'html.parser') 
script = soup.find_all('script')[1].text.strip()[17:-1]
list = json.loads(script)['searchResult']['products']


def getInfo(item):
    title=item['description']
    status=item['status']
    sku=item['sku']
    pid=item['id']
    link = item['link']
    id=item['familyId']
    url = "https://www.midwayusa.com%s" %link
    discountPrice=item['prices']['discountPrice']['low']
    ourPrice=item['prices']['ourPrice']['low']
    listPrice=item['prices']['listPrice']['low']
    # sleep(5) 
    print(url)
    # htmldata = getdata(link) 
    obj = MidwayusaScraper()
    obj.setUp()
    print(obj.scrapTopic(url))
    obj.tearDown()

    # print(htmldata)        
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(getInfo, list)