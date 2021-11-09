import urllib.request 
import re
from bs4 import BeautifulSoup

# URL TO SCRAP
url = "http://seniorfulldev.tech"
#Query the website and return the html to the variable 'page'
#For python 3 use urllib.request.urlopen(wiki)

page = urllib.request.urlopen(url) 
print('page = ',page) 
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page,features='html.parser')
# print('\n\nPage Scrapped !!!\n\n')


# print('\n\nTITLE OF THE PAGE\n\n')
# print(soup.title.string)

print('\n\nALL THE URLs IN THE WEB PAGE\n\n')

all_links = soup.find_all('a')
print('Total number of URLs present = ',len(all_links)) 

print('\n\nLast 5 URLs in the page are : \n')

emails = []
for url in all_links :
    if(str(url.get('href')).find('@') > 0):
        emails.append(url.get('href'))
    if(str(url.get('href')).find('/') > 0):
        part_page = urllib.request.urlopen(url.get('href')) 
        print('part_page = ',url.get('href')) 
        part_soup = BeautifulSoup(part_page,features='html.parser')
        all_part_links = part_soup.find_all('a')
        if(str(url.get('href')).find('@') > 0):
            emails.append(url.get('href'))

print('\n\nTotal Number of Email IDs Present: ', len(emails))

print('\n\nSome of the emails are: \n\n')
for email in emails:
    print(email)