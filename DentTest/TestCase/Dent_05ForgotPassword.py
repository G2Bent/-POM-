import unittest,time
from Pages.LoginPage import LoginPage
from BasePages.Selenium2 import browser
from BasePages.BasePage import login_url
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class LoginCase(unittest.TestCase):
    """登录"""
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(30)
        cls.url = "http://test.dent-lab.com/login.html"
        cls.Pusername = "15816038158"
        cls.ErPusername1 = "15500000000"
        cls.ErPusername2 = "1550000000"
        cls.password = "a123456"
        cls.Erpassword = "a12345678"
        cls.Eusername = "944921374@qq.com"
        cls.ErEusername1 = "944921374.com"
        cls.ErEusername2 = "9449213@qq.com"
        cls.title = "德雅医疗-Dent Lab"


    def test_login1(self):
        """手机登录成功"""
        #声明LoginPage对象
        login_page = LoginPage(self.driver,self.url,self.title)
        # 调用打开页面组件
        login_page.open()
        #调用用户名输入组件
        login_page.input_username(self.Pusername)
        #调用密码输入组件
        login_page.input_password(self.password)
        #调用登录组件
        login_page.click_submit()
        assert "个人中心" in login_page.show_()



    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        img_path = r'..\image\手机登录\\' + now + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    for i in range(1, 8):
        testunit.addTest(LoginCase("test_login%s"%str(i)))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = r'..\report\\' + str(now) + '_result.html'
    fp = open(report_name, 'wb')
    Runner = HTMLTestRunner(
        stream=fp,
        title='手机登录测试报告',
        description='测试用例执行情况'
    )
    Runner.run(testunit)
    fp.close()




