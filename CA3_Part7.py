#7. Write a Python program to open the ebay.ie website and click on the cart icon.
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.ebay.ie/n/all-categories")
driver.maximize_window()
driver.find_element("id", "gh-cart").click() #click on cart icon
print(driver.title)
time.sleep(10)
driver.quit()