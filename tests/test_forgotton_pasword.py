from selenium.webdriver.common.by import By

class Test_Forgotten_password:
    def test_forgot_passwd_btn(self):


        self.driver.find_element(By.LINK_TEXT,"Forgot password?").click()
        print("This is forgotten password btn test case")

