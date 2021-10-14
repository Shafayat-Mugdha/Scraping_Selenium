from selenium import webdriver

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://portfolio.shafayat-mugdha.com/")
print(driver.title)