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

username = "wolfman199311@gmail.com"
access_key = "qh6Q2M7fetERX1wv7mGOrldGOWmu3ejwPyzTpJ7bdSXZk3iaIl"


class MidwayusaScraper:
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    def setUp(self):
        capabilities = {
            "build": "midwayusa",
            "name": "gun parts",
            "platform": "Windows 10",
            "browserName": "Chrome",
            "version": "100.0",
            "selenium_version": "4.1.2",
            "geoLocation": "US",
            "chrome.driver": "100.0",
            "headless": True
        }
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            desired_capabilities=capabilities)

    def tearDown(self):
        self.driver.quit()

    def scrapTopic(self, url):
        driver = self.driver

        # Url
        driver.get(url)

        source = driver.page_source
        # scraping title
        title_list = []
        soup = bs(source, "html.parser")
        for table in soup.findAll("table", class_="product-specs-table padding-none stack-l width-100"):
            for span in table.findAll("span"):
                title_list.append(span.text)
            for div in table.findAll("div", class_="product-specs-table-definition-name no-value"):
                title_list.append(div.text)
        return title_list

url = 'https://www.midwayusa.com/product/1021519158?pid=575995'
obj = MidwayusaScraper()
obj.setUp()
print(obj.scrapTopic(url))
obj.tearDown()
