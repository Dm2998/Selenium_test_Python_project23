#1 search for a ebay website

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver.exe")           # Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.ebay.com/")           # search for a ebay website.
driver.maximize_window()                      # maximize the window.
print(driver.title)                           # print the title of the page.
time.sleep(10)                                   # wait for 10 seconds.
driver.quit()                                    # close the browser.







