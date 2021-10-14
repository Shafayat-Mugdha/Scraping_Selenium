from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# driver.get("https://sg.godaddy.com/offers/godaddy?isc=gofhas28&countryview=1&currencyType=SGD&gclid=Cj0KCQjwnueFBhChARIsAPu3YkR4bNh_0jCgczjAUWrdfrzVW-cozIS0Lz0g3xdbCmhcPTcdL_bxxVoaAoKVEALw_wcB&gclsrc=aw.ds")
driver.get("https://bscscan.com/token/0xec3422ef92b2fb59e84c8b02ba73f1fe84ed8d71#balances")
print(driver.title)

# search = driver.find_element_by_name("domainToCheck")
# search.send_keys("Shafayat")
# search.send_keys(Keys.RETURN)
# print(driver.page_source) # code niye ashbe page er


