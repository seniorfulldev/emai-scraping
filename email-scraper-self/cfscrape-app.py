import cfscrape
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
from collections import deque

starting_url = input("Enter the website url: ")
unprocessed_urls = deque([starting_url])
processed_urls = deque([])

def anti_bot_scraping():
    
    target_url = "https://www.freelancer.com"   # replace url with anti-bot protected website
    scraper = cfscrape.create_scraper()
    html_text = scraper.get(target_url).text
    parsed_html = BeautifulSoup(html_text, 'html.parser')
    print(parsed_html)
    
    for anchor in parsed_html.find_all("a"):
        # if starting_url not in url: 
        # continue
        # extract base url to resolve relative links
        parts = urlsplit(anchor)
        base_url = "{0.scheme}://{0.netloc}".format(parts)
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

if __name__ == '__main__':
    anti_bot_scraping()
