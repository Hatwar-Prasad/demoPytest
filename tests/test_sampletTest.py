import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By



class Test_LoginPage:
    def test_Login(self):
        self.driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']").send_keys(
            "12456789")
        self.driver.find_element(By.XPATH, "//input[@aria-label='Password']").send_keys("245642626")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
