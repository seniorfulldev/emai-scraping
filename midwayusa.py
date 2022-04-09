from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.midwayusa.com/product/1021519158?pid=575995')

source = driver.page_source
# scraping title
title_list = []
soup = bs(source, "html.parser")
for table in soup.findAll("table", class_="product-specs-table padding-none stack-l width-100"):
    for span in table.findAll("span"):
        title_list.append(span.text)
    for div in table.findAll("div", class_="product-specs-table-definition-name no-value"):
        title_list.append(div.text)
driver.close()
print(title_list)