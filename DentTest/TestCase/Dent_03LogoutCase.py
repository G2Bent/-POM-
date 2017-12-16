import time
import unittest

from Pages.LoginPage import LoginPage
from BasePages.Selenium2 import browser
from UseData.Open_Url import *
from UseData.Password import *
from UseData.PhoneEmail import *


class LogOutCase(unittest.TestCase):
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
        time.sleep(3)
        logout_page.logout()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# if __name__ =="__main__":
#     unittest.main()


