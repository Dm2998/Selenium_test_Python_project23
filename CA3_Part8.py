#8 write will open the ebay.ie website and click ebay customer service link.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.ebay.ie/")
driver.maximize_window()
driver.find_element("id", "gh-p-3").click()
print(driver.title)
time.sleep(10)
driver.quit()