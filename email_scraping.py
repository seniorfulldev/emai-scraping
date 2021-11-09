import re
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
from multiprocessing import Pool
from time import sleep



# starting url. replace google with your own url.
starting_url = input("Enter the website url: ") 
# a queue of urls to be crawled
unprocessed_urls = deque([starting_url])
# print("unprocessed_urls URL %s" % unprocessed_urls)
# set of already crawled urls for email
processed_urls = deque([])

# a set of fetched emails
emails = deque([])
# process urls one by one from unprocessed_url queue until queue is empty
while len(unprocessed_urls):
    # move next url from the queue to the set of processed urls
    url = unprocessed_urls.popleft()
    processed_urls.append(url)
    if starting_url not in url: 
        continue
    # extract base url to resolve relative links
    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url
    # get url's content
    print("Crawling URL %s" % url)
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        # ignore pages with errors and continue with next url
        continue

    # extract all email addresses and add them into the resulting set
    # You may edit the regular expression as per your requirement
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    for email in new_emails:
        if not email in emails and not 'x' in email:
            emails.append(email)

    
    # de = ""
    # e="8dfef8fdfde2fff9cdeaf8e3eeffe4f9e4eea3eee2e0"
    # k = int(e[:2], 16)

    # for i in range(2, len(e)-1, 2):
    #     de += chr(int(e[i:i+2], 16)^k)
    # print(de)
    # <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="543931142127353935313e352e7a373b39">[email&#160;protected]</a>

    print("emails %s" % emails)
    # create a beutiful soup for the html document
    soup = BeautifulSoup(response.text, 'lxml')
    # print("soup %s" % soup)
    # Once this document is parsed and processed, now find and process all the anchors i.e. linked urls in this document
    for anchor in soup.find_all("a"):
        # extract link url from the anchor
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        # resolve relative links (starting with /)
        if link.startswith('/'):
            link = base_url + link
            # print("pathlink %s" % path)
            processed_urls.append(link)
        elif not link.startswith('http') and '#' in link and link == "":
            # print("unpathlink %s" % path)
            # print("unpath %s" % link)
            # link = path + link
            continue
        elif '#' in link:
            continue
        # add the new url to the queue if it was not in unprocessed list nor in processed list yet
        if not link in unprocessed_urls and not link in processed_urls:
            unprocessed_urls.append(link)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")             
print("emailList %s" % emails)            