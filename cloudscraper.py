import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
print(scraper.get("https://www.midwayusa.com/api/product/data?id=1021519158&pid=575995").text)  # => "<!DOCTYPE html><html><head>..."