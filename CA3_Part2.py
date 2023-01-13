##2 search for a ebay website and search for a product called hall

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Create a new instance of the Chrome driver

# Create a new instance of the Chrome driver
serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.ebay.com/")
driver.maximize_window()
driver.find_element("id", "gh-ac").send_keys("hall")  # search for a product called hall
print(driver.title)
time.sleep(10)
driver.quit()


