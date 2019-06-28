# finance_data.py
# tutorial: https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/


# Import libs
from bs4 import BeautifulSoup as BS
import urllib.request as ul


# read data from Bloomberg Website

source = "https://www.bloomberg.com/quote/SPX:IND"
try:
    r = ul.urlopen(source)
    print("successfully read")
except:
    print("WTF")


# Parse data from website
soup = BS(r, "lxml")
print(soup.prettify())


# --------end of basic web scraping---------
# find finance data on Bloomberg website

name_box = soup.find("h1", attrs={"class": "companyName__99a4824b"})
name = name_box.text.strip()
print(name)

# seems like the web page is not parsed properly since there is no companyname in xml view included.