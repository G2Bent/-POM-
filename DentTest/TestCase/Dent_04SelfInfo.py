import unittest,time
from Pages.SelfInfo import SelfInfo
from BasePages.Selenium2 import browser
from BasePages.BasePage import login_url
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class SelfCase(unittest.TestCase):

    """个人中心"""
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(30)
        cls.url = "http://test.dent-lab.com/login.html"
        cls.user = "15816038158"
        cls.phone ="18814128583"
        cls.name1 = "中国恒大"
        cls.name2 = "a"
        cls.name3 = "zhongguo广州恒大拿到7冠的时候，我才发现，我追恒大已经第8年了"
        cls.image1 = "正常头像"
        cls.image2 = "超出2M头像"
        cls.image3 = "错误格式"
        cls.psw = "a123456"
        cls.epsw = "12345"
        cls.email = "648604875@qq.com"
        cls.regemail = "944921374@qq.com"
        cls.error_email = "123456qq.com"
        cls.everify_code = "123455"
        cls.everify_code2 = "12344"
        cls.title = "德雅医疗-Dent Lab"


    def login(self):
        # 声明LoginPage对象
        login_page = SelfInfo(self.driver, self.url, self.title)
        # 调用打开页面组件
        login_page.open()
        login_page.Login(self.user,self.psw)
        return login_page

    def login_email(self):
        # 声明LoginPage对象
        login_page = SelfInfo(self.driver, self.url, self.title)
        # 调用打开页面组件
        login_page.open()
        login_page.Login(self.regemail,self.psw)
        return login_page

    def test_self1(self):
        """编辑个人信息成功"""
        user_page = self.login()
        user_page.Edit()
        user_page.edituploadfile(self.image1)
        user_page.editselfname(self.name1)
        user_page.editselfsex()
        user_page.editselfbirY()
        user_page.editselfbirM()
        user_page.editselfbireD()
        user_page.saveself()

    def test_self2(self):
        """编辑个人信息上传头像不能超过2M"""
        user_page = self.login()
        user_page.Edit()
        user_page.edituploadfile(self.image2)
        time.sleep(2)
        user_page.saveself()

    def test_self3(self):
        """编辑个人信息上传头像格式不正确"""
        user_page = self.login()
        user_page.Edit()
        user_page.edituploadfile(self.image3)
        time.sleep(2)
        user_page.saveself()

    def test_self4(self):
        """编辑个人信息用户名大于16字符"""
        user_page = self.login()
        user_page.Edit()
        user_page.editselfname(self.name3)
        time.sleep(2)
        user_page.screen(self._testMethodDoc)
        user_page.saveself()

    def test_self5(self):
        """编辑个人信息用户名少于两字符"""
        user_page = self.login()
        user_page.Edit()
        user_page.editselfname(self.name2)
        time.sleep(2)
        user_page.saveself()
        user_page.error_user()
        user_page.screen(self._testMethodDoc)

    def test_self6(self):
        """修改密码原密码为空"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.savepsw()
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self7(self):
        """修改密码新密码为空"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(self.psw)
        user_page.savepsw()
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self8(self):
        """修改密码确认新密码为空"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(self.psw)
        user_page.newpsw(self.psw)
        user_page.savepsw()
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self9(self):
        """修改密码原密码错误"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(self.epsw)
        user_page.newpsw(self.psw)
        user_page.renewpsw(self.psw)
        user_page.savepsw()
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self10(self):
        """修改密码新密码格式错误"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(self.psw)
        user_page.newpsw(self.epsw)
        user_page.renewpsw(self.epsw)
        user_page.savepsw()
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self11(self):
        """修改密码密码不一致"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(self.psw)
        user_page.newpsw(self.psw)
        user_page.renewpsw(self.epsw)
        user_page.savepsw()
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self12(self):
        """修改密码成功"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(self.psw)
        user_page.newpsw(self.psw)
        user_page.renewpsw(self.psw)
        user_page.savepsw()
        user_page.screen(self._testMethodDoc)

    def test_self13(self):
        """绑定邮箱成功"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.emailtxt(self.email)
        user_page.emailverifybtn()
        user_page.emailverifytxt(self.email)
        user_page.emailsave()
        user_page.screen(self._testMethodDoc)

    def test_self14(self):
        """绑定邮箱邮箱格式错误"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.emailtxt(self.error_email)
        user_page.emailverifybtn()
        user_page.emailsave()
        user_page.screen(self._testMethodDoc)

    def test_self15(self):
        """绑定邮箱邮箱已注册"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.emailtxt(self.regemail)
        user_page.emailverifybtn()
        user_page.emailsave()
        user_page.screen(self._testMethodDoc)

    def test_self16(self):
        """绑定邮箱邮箱不能为空"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.emailsave()
        user_page.screen(self._testMethodDoc)

    def test_self17(self):
        """绑定邮箱邮箱验证码不足6位"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.emailtxt(self.email)
        user_page.emailverifybtn()
        user_page.emailverifytxt(self.everify_code2)
        user_page.emailsave()
        user_page.screen(self._testMethodDoc)

    def test_self18(self):
        """绑定邮箱邮箱验证码错误"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.emailtxt(self.email)
        user_page.emailverifybtn()
        user_page.emailverifytxt(self.everify_code)
        user_page.emailsave()
        user_page.emailtips()
        user_page.screen(self._testMethodDoc)

    def test_self19(self):
        """绑定/修改手机号为空"""
        user_page = self.login_email()
        user_page.BDPhone()
        user_page.phonebtn()
        user_page.phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self20(self):
        """绑定/修改手机验证码错误"""
        user_page = self.login_email()
        user_page.BDPhone()
        user_page.phone(self.phone)
        user_page.phonebtn()
        user_page.phonetxt(self.everify_code)
        user_page.savephone()
        user_page.phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self21(self):
        """绑定/修改手机验证码不足6位"""
        user_page = self.login_email()
        user_page.BDPhone()
        user_page.phone(self.phone)
        user_page.phonetxt(self.everify_code2)
        user_page.savephone()
        user_page.phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self22(self):
        """绑定/修改手机手机号错误"""
        user_page = self.login_email()
        user_page.BDPhone()
        user_page.phone(self.everify_code)
        user_page.phonebtn()
        user_page.phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self23(self):
        """绑定/修改手机号已经注册"""
        user_page = self.login_email()
        user_page.BDPhone()
        user_page.phone(self.user)
        user_page.phonebtn()
        user_page.phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self24(self):
        """绑定/修改手机成功"""
        user_page =self.login_email()
        user_page.phone(self.phone)
        user_page.phonebtn()
        user_page.phonetxt(self.phone)
        user_page.savephone()
        user_page.screen(self._testMethodDoc)

    def test_self25(self):
        """新增收货地址:名字为空"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addincrease()
        user_page.addtip()
        user_page.screen(self._testMethodDoc)

    def test_self26(self):
        """新增收货地址：名字错误"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addname(self.name2)
        user_page.addincrease()
        user_page.addtip()
        user_page.screen(self._testMethodDoc)

    def test_self27(self):
        """新增收货地址：手机号为空"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addname(self.name1)
        user_page.addincrease()
        user_page.addtip()
        user_page.screen(self._testMethodDoc)

    def test_self28(self):
        """新增收货地址：手机号错误"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addname(self.name1)
        user_page.addphone(self.everify_code)
        user_page.addincrease()
        user_page.addtip()
        user_page.screen(self._testMethodDoc)

    def test_self29(self):
        """新增收货地址：详细地址为空"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addname(self.name1)
        user_page.addphone(self.phone)
        user_page.addpro()
        user_page.addincrease()
        user_page.addtip()
        user_page.screen(self._testMethodDoc)

    def test_self30(self):
        """新增收货地址：新增成功"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addname(self.name1)
        user_page.addphone(self.phone)
        user_page.addpro()
        user_page.adddetail(self.name3)
        user_page.addincrease()
        time.sleep(3)
        user_page.addaddress()
        user_page.addname(self.name1)
        user_page.addphone(self.phone)
        user_page.addpro()
        user_page.adddetail(self.name3)
        user_page.addincrease()
        user_page.screen(self._testMethodDoc)

    def test_self31(self):
        """编辑收货地址：更改用户名字"""
        user_page = self.login()
        user_page.Good()
        user_page.editadd()
        user_page.editname(self._testMethodName)
        user_page.editdefault()
        user_page.editsave()
        user_page.screen(self._testMethodDoc)

    def test_self32(self):
        """编辑收货地址：更改手机号码"""
        user_page = self.login()
        user_page.Good()
        user_page.editadd()
        user_page.editphone(self.user)
        time.sleep(3)
        user_page.editsave()
        user_page.screen(self._testMethodDoc)

    def test_self33(self):
        """编辑收货地址：更改地址"""
        user_page = self.login()
        user_page.Good()
        user_page.editadd()
        user_page.editpro()
        user_page.editdetail(self.title)
        time.sleep(3)
        user_page.editsave()
        user_page.screen(self._testMethodDoc)

    def test_self34(self):
        """编辑收货地址：更改默认地址"""
        user_page = self.login()
        user_page.Good()
        user_page.editadd()
        user_page.editdefault()
        time.sleep(3)
        user_page.editsave()
        user_page.screen(self._testMethodDoc)

    def test_self35(self):
        """确认删除地址"""
        user_page = self.login()
        user_page.Good()
        user_page.deleteadd()
        user_page.screen(self._testMethodDoc)
        user_page.subdele()


    def test_self36(self):
        """取消删除地址"""
        user_page = self.login()
        user_page.Good()
        user_page.deleteadd()
        user_page.screen(self._testMethodDoc)
        user_page.cancledele()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    for i in range(1,37):
        testunit.addTest(SelfCase("test_self%s"%str(i)))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = r'..\report\\' + str(now) + '_result.html'
    fp = open(report_name, 'wb')
    Runner = HTMLTestRunner(
        stream=fp,
        title='个人中心测试报告',
        description='测试用例执行情况'
    )
    Runner.run(testunit)
    fp.close()




