import unittest,time
from Pages.ForgotPassword import Forgetpwd
from BasePages.Selenium2 import browser
from UseData.Open_Url import *
from UseData.PhoneEmail import *
from UseData.Password import *
from UseData.Txt import *
from BasePages.BasePage import login_url
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class LoginCase(unittest.TestCase):
    """登录"""
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        # cls.driver.implicitly_wait(5)
        cls.url = LoginUrl()
        cls.title = Title()

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

    def test_forget8(self):
        """找回密码成功"""
        forget_page =self.openforget()
        forget_page.find(FindPassword())
        forget_page.newpwd(Pwd())
        forget_page.renewpwd(Pwd())
        forget_page.submitbtn()

    def test_forget1(self):
        """输入未注册手机号"""
        forget_page = self.openforget()
        #调用输入手机号/邮箱
        forget_page.phone(UnRegPhone())
        #调用点击获取验证码
        forget_page.btnverify()
        self.file(self._testMethodDoc)

    def test_forget2(self):
        """输入错误手机号"""
        forget_page = self.openforget()
        forget_page.phone(ErrorPhone())
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
        forget_page.phone(LoginEmail())
        forget_page.verifytxt(ErrorNum_6())
        forget_page.newpwd(Pwd())
        forget_page.renewpwd(Pwd())
        forget_page.submitbtn()
        time.sleep(2)
        self.file(self._testMethodDoc)

    def test_forget5(self):
        """输入不足6位数验证码"""
        forget_page = self.openforget()
        forget_page.phone(LoginEmail())
        forget_page.verifytxt(ErrorNum_5())
        forget_page.newpwd(Pwd())
        forget_page.renewpwd(Pwd())
        forget_page.submitbtn()
        self.file(self._testMethodDoc)

    def test_forget6(self):
        """输入错误新密码"""
        forget_page = self.openforget()
        forget_page.phone(LoginEmail())
        forget_page.btnverify()
        forget_page.verifytxt(LoginEmail())
        forget_page.newpwd(ErrorNum_5())
        forget_page.submitbtn()
        self.file(self._testMethodDoc)

    def test_forget7(self):
        """输入错误确认新密码"""
        forget_page = self.openforget()
        forget_page.phone(LoginEmail())
        forget_page.btnverify()
        forget_page.verifytxt(LoginEmail())
        forget_page.newpwd(Pwd())
        forget_page.renewpwd(ErrorNum_5())
        forget_page.submitbtn()
        self.file(self._testMethodDoc)


    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        img_path = r'..\image\忘记密码\\' + now + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    for i in range(1, 8):
        testunit.addTest(LoginCase("test_forget%s"%str(i)))
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




