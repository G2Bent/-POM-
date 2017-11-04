from Pages.LoginPage import LoginPage
from BasePages.Selenium2 import browser
from selenium.webdriver.common.action_chains import *
import unittest,time

class LoginOut(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        # cls.driver.implicitly_wait(5)
        cls.url = "http://test.dent-lab.com/login.html"
        cls.Pusername = "15816038158"
        cls.password = "a123456"
        cls.Eusername = "944921374@qq.com"
        cls.title = "德雅医疗-Dent Lab"

    def test_logout1(self):
        """退出成功"""
        login_page = LoginPage(self.driver,self.url,self.title)
        login_page.open()
        login_page.input_username(self.Pusername)
        login_page.input_password(self.password)
        login_page.click_submit()
        time.sleep(3)
        login_page.logout()

    def test_logout2(self):
        """退出成功"""
        login_page = LoginPage(self.driver, self.url, self.title)
        login_page.open()
        login_page.input_username(self.Eusername)
        login_page.input_password(self.password)
        login_page.click_submit()
        time.sleep(3)
        login_page.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ =="__main__":
    unittest.main()


