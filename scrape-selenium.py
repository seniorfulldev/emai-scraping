from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver  = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.naukri.com/data-scientist-jobs?k=data%20scientist')

jobs = driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
company = driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]')

title = []
for i in range(len(jobs)):
    print(jobs[i].text)
    title.append(jobs[i].text)

data = pd.DataFrame(title)    

company_ = []
for i in range(len(company)):
    company_.append(company[i].text)

data['company'] = company_

data.to_csv('results/Job List.csv',index=False)
data

driver.close()