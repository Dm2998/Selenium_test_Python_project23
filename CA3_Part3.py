# 3 search for sing in and click on it
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver.exe") # Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=serv_obj)       
driver.get("https://www.ebay.com/")                # search for a ebay website
driver.maximize_window()
driver.find_element("id", "gh-ug").click()   # search for sing in and click on it
print(driver.title)
time.sleep(10)
driver.quit()