from Pages.LoginPage import LoginPage
from BasePages.Selenium2 import browser
from UseData.Open_Url import *
from UseData.PhoneEmail import *
from UseData.Password import *
from selenium.webdriver.common.action_chains import *
import unittest,time

class LoginOut(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.url = LoginUrl()
        cls.title = Title()

    def test_logout1(self):
        """退出成功"""
        logout_page = LoginPage(self.driver,self.url,self.title)
        logout_page.open()
        logout_page.input_username(LoginEmail())
        logout_page.input_password(Pwd())
        logout_page.click_submit()
        time.sleep(2)
        logout_page.logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ =="__main__":
    unittest.main()


