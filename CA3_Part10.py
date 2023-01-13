import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.ebay.ie/")
driver.maximize_window()
driver.find_element("id", "gh-ac").send_keys("laptop")
driver.find_element("id", "gh-btn").click()
time.sleep(5)
driver.quit()
