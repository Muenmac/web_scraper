# finance_data.py
# tutorial: https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/


# Import libs
from bs4 import BeautifulSoup as BS
import requests as r
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# read data from Bloomberg Website
source = "https://www.bloomberg.com/quote/SPX:IND"

browser = webdriver.Firefox(executable_path='/usr/local/share/gecko_driver/geckodriver')

try:
    browser.get(source)
    print("success")
except:
    print("WTF")
textlist = browser.find_elements_by_tag_name("span")

for text_elements in textlist:
    text = text_elements.text
    print(text)

# delay = 3
# WebDriverWait(browser, delay).until(EC.presence_of_element_located(browser.find_elements_by_id("a")))


# Parse data from website
# soup = BS(, "html.parser")
# elements = soup.select("div > span")
# print(soup.prettify())



# --------end of basic web scraping---------
# find finance data on Bloomberg website

#name_box = soup.find("h1", attrs={"class": "companyName__99a4824b"})
#name = name_box.text.strip()
#print(name)

# seems like the web page is not parsed properly since there is no companyname in xml view included.