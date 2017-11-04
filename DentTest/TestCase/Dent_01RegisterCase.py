import unittest,time
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from BasePages.Selenium2 import browser
from BasePages.BasePage import login_url
from selenium import webdriver
from API import post
from Pages.RandNum import PhoneNum,EmailNum
from HTMLTestRunner import HTMLTestRunner

class RegisterCase(unittest.TestCase):
    """注册"""
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.title = "德雅医疗-Dent Lab"
        cls.url = "http://test.dent-lab.com/register.html"
        cls.Pusername = "13217665001"
        cls.ErPusername1 = "1550000000"
        cls.password = "a123456"
        cls.Erpassword = "a12"
        cls.Eusername = "944921374@qq.com"
        cls.ErEusername1 = "944921374.com"

    def test_reg1(self):
        """密码不一致"""
        reg_page = RegisterPage(self.driver, self.url, self.title)
        reg_page.open()
        reg_page.input_username(self.Eusername)
        reg_page.click_verify()
        reg_page.input_verify(self.Eusername)
        reg_page.input_password(self.password)
        reg_page.input_repassword(self.Erpassword)
        reg_page.click_submit()
        assert "两次输入的密码不一致" in reg_page.show_tips()

    def test_reg2(self):
        """邮箱格式错误"""
        reg_page = RegisterPage(self.driver, self.url, self.title)
        reg_page.open()
        reg_page.input_username(self.ErEusername1)
        reg_page.click_verify()
        reg_page.input_verify(self.Eusername)
        reg_page.input_password(self.password)
        reg_page.input_repassword(self.password)
        reg_page.click_submit()
        assert "手机号/邮箱格式不正确" in reg_page.show_tips()

    def test_reg3(self):
        """测试手机号码错误"""
        reg_page = RegisterPage(self.driver, self.url, self.title)
        reg_page.open()
        reg_page.input_username(self.ErPusername1)
        reg_page.click_verify()
        assert "手机号/邮箱格式不正确" in reg_page.show_tips()

    def test_reg4(self):
        """测试密码错误"""
        reg_page = RegisterPage(self.driver,self.url,self.title)
        reg_page.open()
        reg_page.input_username(self.Eusername)
        reg_page.click_verify()
        reg_page.input_verify(self.Eusername)
        reg_page.input_password(self.Erpassword)
        reg_page.input_repassword(self.Erpassword)
        reg_page.click_submit()
        assert "密码由6-16字母(区分大小写)、数字组成" in reg_page.show_tips()

    def test_reg5(self):
        """账号密码为空"""
        reg_page = RegisterPage(self.driver, self.url, self.title)
        reg_page.open()
        reg_page.click_submit()
        assert "手机号/邮箱不能为空" in reg_page.show_tips()

    def test_reg6(self):
        """验证码错误"""
        reg_page = RegisterPage(self.driver, self.url, self.title)
        reg_page.open()
        reg_page.input_username(self.Eusername)
        # reg_page.click_verify()
        reg_page.input_verify("123455")
        reg_page.input_password(self.password)
        reg_page.input_repassword(self.password)
        reg_page.click_submit()
        assert "验证码错误" in reg_page.show_tips()

    def test_reg7(self):
        """手机注册成功"""
        #声明LoginPage对象
        reg_page = RegisterPage(self.driver,self.url,self.title)
        # 调用打开页面组件
        reg_page.open()
        # #调用点击注册组件
        # LoginPage(self.driver,self.url,"黑格科技").click_reg()
        #调用用户名输入组件
        reg_page.input_name(self.Pusername)
        #调用密码输入组件
        reg_page.input_password(self.password)
        #确认密码
        reg_page.input_repassword(self.password)
        #调用登录组件
        reg_page.click_submit()
        #注册成功，文案校验
        assert "个人中心" in reg_page.show_()

    def test_reg8(self):
        """邮箱注册成功"""
        reg_page = RegisterPage(self.driver,self.url,self.title)
        reg_page.open()
        reg_page.input_username(self.Eusername)
        reg_page.click_verify()
        time.sleep(3)
        reg_page.input_verify(self.Eusername)
        reg_page.input_password(self.password)
        reg_page.input_repassword(self.password)
        reg_page.click_submit()
        assert "个人中心" in reg_page.show_()

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        img_path = r'..\image\注册\\' + now + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    for i in range(1, 9):
        testunit.addTest(RegisterCase("test_reg%s"%str(i)))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = r'..\report\\' + str(now) + '_result.html'
    fp = open(report_name, 'wb')
    Runner = HTMLTestRunner(
        stream=fp,
        title='注册测试报告',
        description='测试用例执行情况'
    )
    Runner.run(testunit)
    fp.close()




