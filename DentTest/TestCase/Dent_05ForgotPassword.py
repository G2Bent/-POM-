import unittest,time
from Pages.ForgotPassword import Forgetpwd
from BasePages.Selenium2 import browser
from BasePages.BasePage import login_url
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class LoginCase(unittest.TestCase):
    """登录"""
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        # cls.driver.implicitly_wait(5)
        cls.url = "http://test.dent-lab.com/login.html"
        cls.phone = "13217665001"
        cls.Unreg = "15500000000"
        cls.Cphone = "1581603815"
        cls.password = "a123456"
        cls.Erpassword = "a12345678"
        cls.num = "123454"
        cls.num2 = "1233"
        cls.Eusername = "944921374@qq.com"
        cls.ErEusername1 = "944921374.com"
        cls.ErEusername2 = "9449213@qq.com"
        cls.title = "德雅医疗-Dent Lab"


    def openforget(self):
        # 声明LoginPage对象
        forget_page = Forgetpwd(self.driver, self.url, self.title)
        # 调用打开页面组件
        forget_page.open()
        # 调用忘记密码按钮
        forget_page.Forgetpwd()
        return forget_page

    def file(self,name):
        file = Forgetpwd(self.driver, self.url, self.title)
        file.tip()
        file.screen(name)
        return file

    def test_forget(self):
        """找回密码成功"""
        forget_page =self.openforget()
        forget_page.phone(self.phone)
        forget_page.btnverify()
        forget_page.verifytxt(self.phone)
        forget_page.newpwd(self.password)
        forget_page.renewpwd(self.password)
        forget_page.submitbtn()

    def test_forget1(self):
        """输入未注册手机号"""
        forget_page = self.openforget()
        #调用输入手机号/邮箱
        forget_page.phone(self.Cphone)
        #调用点击获取验证码
        forget_page.btnverify()
        self.file(self._testMethodDoc)

    def test_forget2(self):
        """输入错误手机号"""
        forget_page = self.openforget()
        forget_page.phone(self.Unreg)
        forget_page.btnverify()
        self.file(self._testMethodDoc)

    def test_forget3(self):
        """不做操作"""
        forget_page = self.openforget()
        forget_page.submitbtn()
        self.file(self._testMethodDoc)

    def test_forget4(self):
        """输入错误验证码"""
        forget_page = self.openforget()
        forget_page.phone(self.phone)
        forget_page.verifytxt(self.num)
        forget_page.submitbtn()
        self.file(self._testMethodDoc)

    def test_forget5(self):
        """输入不足6位数验证码"""
        forget_page = self.openforget()
        forget_page.phone(self.phone)
        forget_page.verifytxt(self.num2)
        forget_page.submitbtn()
        self.file(self._testMethodDoc)

    def test_forget6(self):
        """输入错误新密码"""
        forget_page = self.openforget()
        forget_page.phone(self.phone)
        forget_page.btnverify()
        forget_page.verifytxt(self.phone)
        forget_page.newpwd(self.num)
        forget_page.submitbtn()
        self.file(self._testMethodDoc)

    def test_forget7(self):
        """输入错误确认新密码"""
        forget_page = self.openforget()
        forget_page.phone(self.phone)
        forget_page.btnverify()
        forget_page.verifytxt(self.phone)
        forget_page.newpwd(self.password)
        forget_page.renewpwd(self.num)
        forget_page.submitbtn()
        self.file(self._testMethodDoc)


    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        img_path = r'..\image\手机登录\\' + now + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()

# if __name__ == '__main__':
#     testunit = unittest.TestSuite()
#     # 将测试用例加入到测试容器中
#     for i in range(1, 8):
#         testunit.addTest(LoginCase("test_login%s"%str(i)))
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     report_name = r'..\report\\' + str(now) + '_result.html'
#     fp = open(report_name, 'wb')
#     Runner = HTMLTestRunner(
#         stream=fp,
#         title='手机登录测试报告',
#         description='测试用例执行情况'
#     )
#     Runner.run(testunit)
#     fp.close()




