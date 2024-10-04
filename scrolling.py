import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
# driver.get("https://www.w3schools.com/")

driver.implicitly_wait(10)
# driver.execute_script("window.scrollBy(0,2511)","")
dropdown_btn=driver.find_element(By.CLASS_NAME,"dropbtn")


driver.execute_script("arguments[0].scrollIntoView();",dropdown_btn,)
# dropdown_btn.click()
# learnSQL=driver.find_element(By.LINK_TEXT,"Learn SQL")
# driver.execute_script("arguments[0].scrollIntoView();",learnSQL)
# time.sleep(5)
# driver.execute_script("window.scrollBy(0,2511)","")

time.sleep(5)