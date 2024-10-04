import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
dropdown_btn=driver.find_element(By.CLASS_NAME,"dropbtn")
dropdown_btn.click()
# facebook_btn=driver.find_element(By.LINK_TEXT,"Facebook")
wait=WebDriverWait(driver,10)
facebook_btn=wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'Facebook')))
facebook_btn.click()
time.sleep(5)