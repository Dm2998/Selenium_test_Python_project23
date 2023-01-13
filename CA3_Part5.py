#5 sing in with your ebay account
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.ebay.com/")
driver.maximize_window()
driver.find_element("id", "gh-ug").click()
print(driver.title)
time.sleep(10)
driver.quit()