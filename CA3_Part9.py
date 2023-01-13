#9. write number of slicers in one page on ebay.ie
# number the slicers in one. 
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.ebay.ie/")
driver.maximize_window()
slicers = driver.find_elements("id", "s0-0-33-4-0-0[0]-2-match-media-0-ebay-carousel-list")
number_of_slicers = int(input("Enter the number of slicers is one: "))
print(len(slicers))
# for slicer in slicers:
#     slicer.click()
#     time.sleep(2)
print(driver.title)
time.sleep(10)
driver.quit()




