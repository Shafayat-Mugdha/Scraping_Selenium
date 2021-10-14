from typing import Counter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from bs4 import BeautifulSoup

# driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
# driver.get("https://bscscan.com/token/0xec3422ef92b2fb59e84c8b02ba73f1fe84ed8d71/")
# driver.maximize_window()

# Country = driver.find_element_by_xpath('//div[2]/table/tbody/tr[1]/td[1]/span/a/')
# # Country = driver.find_element_by_class_namesiframe')
# for list in Country:
#     print(list.text)


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soup_data= BeautifulSoup(thepage, "html.parser")
    return soup_data

soup = make_soup("https://bscscan.com/token/0xec3422ef92b2fb59e84c8b02ba73f1fe84ed8d71")
for record in soup.find_all('tr'):
    print(record.text)
