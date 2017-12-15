import unittest

from API import post
from Pages.RegisterPage import RegisterPage
from BasePages.Selenium2 import browser
from UseData.Open_Url import *
from UseData.Password import *
from UseData.PhoneEmail import *


class RegisterCase(unittest.TestCase):
    """注册"""
    def setUp(self):
        self.driver = browser()
        self.title = Title()
        self.url = RegisterURL()

    def open_dent(self):
        reg_page = RegisterPage(self.driver, self.url, self.title)
        reg_page.open()
        return reg_page

    def test_reg0(self):
        dele = post.delephone(RegPhone())
        dele2 = post.delephone(RandPhone())
        dele3 = post.delephone(RegPhone())
        print(dele,dele2,dele3)

    def test_reg1(self):
        """两次输入的密码不一致"""
        reg_page = self.open_dent()
        reg_page.input_name(RandEmail())
        reg_page.input_password(Pwd())
        reg_page.input_repassword(ErrorNum_5())
        reg_page.click_submit()
        reg_page.tip_show()

    def test_reg2(self):
        """邮箱格式不正确"""
        reg_page = self.open_dent()
        reg_page.input_username(ErrorEmail())
        reg_page.click_verify()
        reg_page.tip_show()

    def test_reg3(self):
        """手机号格式不正确"""
        reg_page = self.open_dent()
        reg_page.input_username(ErrorPhone())
        reg_page.click_verify()
        reg_page.tip_show()

    def test_reg4(self):
        """测试密码错误"""
        reg_page = self.open_dent()
        reg_page.input_name(RandEmail())
        reg_page.input_password(ErrorNum_5())
        reg_page.input_repassword(ErrorNum_5())
        reg_page.click_submit()
        reg_page.tip_show()

    def test_reg5(self):
        """账号密码为空"""
        reg_page = self.open_dent()
        reg_page.click_submit()
        reg_page.tip_show()

    def test_reg6(self):
        """验证码错误"""
        reg_page = self.open_dent()
        reg_page.input_username(RandEmail())
        reg_page.input_verify(ErrorNum_6())
        reg_page.input_password(Pwd())
        reg_page.input_repassword(Pwd())
        reg_page.click_submit()
        reg_page.tip_show()
        time.sleep(2)


    def test_reg7(self):
        """手机注册成功"""
        #声明LoginPage对象
        # 调用打开页面组件
        reg_page = self.open_dent()
        # #调用点击注册组件
        # LoginPage(self.driver,self.url,"黑格科技").click_reg()
        #调用用户名输入组件
        reg_page.input_name(RegPhone())
        #调用密码输入组件
        reg_page.input_password(Pwd())
        #确认密码
        reg_page.input_repassword(Pwd())
        #调用登录组件
        reg_page.click_submit()
        time.sleep(2)
        #注册成功，文案校验
        # assert "个人中心" in reg_page.show_()

    def test_reg8(self):
        """邮箱注册成功"""
        reg_page = self.open_dent()
        reg_page.input_name(RandEmail())
        # reg_page.input_name("648604875@qq.com")
        reg_page.input_password(Pwd())
        reg_page.input_repassword(Pwd())
        reg_page.click_submit()
        # assert "个人中心" in reg_page.show_()

    def tearDown(self):
        driver = self.driver
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        img_path = r'..\image\注册\\' + now + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()

# if __name__ == '__main__':
#     testunit = unittest.TestSuite()
#     # 将测试用例加入到测试容器中
#     for i in range(1, 9):
#         testunit.addTest(RegisterCase("test_reg%s"%str(i)))
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     report_name = r'..\report\\' + str(now) + '_result.html'
#     fp = open(report_name, 'wb')
#     Runner = HTMLTestRunner(
#         stream=fp,
#         title='注册测试报告',
#         description='测试用例执行情况'
#     )
#     Runner.run(testunit)
#     fp.close()




