# hackernooon_scraper.py
# tutorial: https://hackernoon.com/introduction-to-web-scraping-using-python-89b15b57150c

import bs4
import requests as rq


# first step: getting a response from the scraped object, either get(url) or post(url+credentials) method
response = rq.get('https://www.hackthissite.org/')

if response.status_code == 200:
    print(str(response.status_code) + " --> Connection succesful")
else:
    print(str(response.status_code) + " --> Some fault, check status code")
# print(response.text)


# second step: bs4 to fetch and parse the data. bs4 uses request lib and transforms it with lmxl parser properly
soup = bs4.BeautifulSoup(response.text, "lxml")


# prettify for better readable output
# print(soup.prettify())


# read some data: select HTML Tag and CSS selector with select...
# Beware: every Tag is selected, List number in [x] necessary
title = soup.select('div')[0].getText()
linklist = soup.find_all("a")

for links in linklist:
    print(links.get("href"))
