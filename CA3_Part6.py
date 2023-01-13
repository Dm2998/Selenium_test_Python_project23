#6. Write a Python program to automate the login process of eBay.ie.
#The program should open the eBay.ie website, maximize the window, enter the email.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://signin.ebay.ie/ws/eBayISAPI.dll?SignIn&ru=")
driver.maximize_window()
driver.find_element("id", "userid").send_keys("x00191146@tudublin.ie") #enter email
print(driver.title)
time.sleep(10)
driver.quit()