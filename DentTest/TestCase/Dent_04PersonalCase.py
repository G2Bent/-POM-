import unittest
from HTMLTestRunner import HTMLTestRunner

from Pages.PersonalPage import PersonalPage
from BasePages.Selenium2 import browser
from UseData.Open_Url import *
from UseData.Password import *
from UseData.PhoneEmail import *
from UseData.Txt import *


class PersonalCase(unittest.TestCase):

    """个人中心"""
    def setUp(self):
        self.driver = browser()
        # cls.driver.implicitly_wait(5)
        self.url = LoginUrl()
        self.title = Title()
        self.image1 = "test1"
        self.image2 = "test2"
        self.image3 = "test3"

    def login(self):
        # 声明LoginPage对象
        login_page = PersonalPage(self.driver, self.url, self.title)
        # 调用打开页面组件
        login_page.open()
        login_page.Login(LoginPhone(), Pwd())
        time.sleep(3)
        return login_page

    def login_email(self):
        # 声明LoginPage对象
        login_page = PersonalPage(self.driver, self.url, self.title)
        # 调用打开页面组件
        login_page.open()
        login_page.Login(LoginEmail(), Pwd())
        time.sleep(3)
        return login_page

    def test_self1(self):
        """编辑个人信息成功"""
        user_page = self.login()
        user_page.Edit()
        user_page.edituploadfile(self.image1)
        # user_page.editselfname(Length_4())
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

    # def test_self4(self):
    #     """编辑个人信息用户名大于16字符"""
    #     user_page = self.login()
    #     user_page.Edit()
    #     # user_page.editselfname(Length_17())
    #     time.sleep(2)
    #     user_page.screen(self._testMethodDoc)
    #     user_page.saveself()

    # def test_self5(self):
    #     """编辑个人信息用户名少于两字符"""
    #     user_page = self.login()
    #     user_page.Edit()
    #     # user_page.editselfname(Length_1())
    #     time.sleep(2)
    #     user_page.saveself()
    #     user_page.error_user()
    #     user_page.screen(self._testMethodDoc)

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
        user_page.psw(Pwd())
        user_page.savepsw()
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self8(self):
        """修改密码确认新密码为空"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(Pwd())
        user_page.newpsw(Pwd())
        user_page.savepsw()
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self9(self):
        """修改密码原密码错误"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(ErrorNum_5())
        user_page.newpsw(Pwd())
        user_page.renewpsw(Pwd())
        user_page.savepsw()
        time.sleep(3)
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self10(self):
        """修改密码新密码格式错误"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(Pwd())
        user_page.newpsw(ErrorNum_5())
        user_page.renewpsw(ErrorNum_5())
        user_page.savepsw()
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self11(self):
        """修改密码密码不一致"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(Pwd())
        user_page.newpsw(Pwd())
        user_page.renewpsw(ErrorNum_5())
        user_page.savepsw()
        user_page.error_psw()
        user_page.screen(self._testMethodDoc)

    def test_self12(self):
        """修改密码成功"""
        user_page = self.login()
        user_page.AlertPsw()
        user_page.psw(Pwd())
        user_page.newpsw(Pwd())
        user_page.renewpsw(Pwd())
        user_page.savepsw()
        user_page.screen(self._testMethodDoc)

    def test_self13(self):
        """绑定邮箱成功"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.txtuser(LoginPhone())
        user_page.txtpassword(Pwd())
        user_page.next()
        user_page.emailuni(RandEmail())
        user_page.emailsave()
        user_page.screen(self._testMethodDoc)

    def test_self14(self):
        """绑定邮箱邮箱格式错误"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.txtuser(LoginPhone())
        user_page.txtpassword(Pwd())
        user_page.next()
        user_page.emailtxt(ErrorEmail())
        user_page.emailverifybtn()
        user_page.emailsave()
        user_page.screen(self._testMethodDoc)

    def test_self15(self):
        """绑定邮箱邮箱已注册"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.txtuser(LoginPhone())
        user_page.txtpassword(Pwd())
        user_page.next()
        user_page.emailtxt(LoginEmail())
        user_page.emailverifybtn()
        user_page.emailsave()
        user_page.screen(self._testMethodDoc)

    def test_self16(self):
        """绑定邮箱邮箱不能为空"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.txtuser(LoginPhone())
        user_page.txtpassword(Pwd())
        user_page.next()
        user_page.emailsave()
        user_page.screen(self._testMethodDoc)

    def test_self17(self):
        """绑定邮箱邮箱验证码不足6位"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.txtuser(LoginPhone())
        user_page.txtpassword(Pwd())
        user_page.next()
        user_page.emailtxt(RandEmail())
        user_page.emailverifybtn()
        user_page.emailverifytxt(ErrorNum_5())
        user_page.emailsave()
        user_page.screen(self._testMethodDoc)

    def test_self18(self):
        """绑定邮箱邮箱验证码错误"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.txtuser(LoginPhone())
        user_page.txtpassword(Pwd())
        user_page.next()
        user_page.emailtxt(RandEmail())
        user_page.emailverifybtn()
        user_page.emailverifytxt(ErrorNum_6())
        user_page.emailsave()
        user_page.emailtips()
        user_page.screen(self._testMethodDoc)

    def test_self36(self):
        """绑定修改邮箱原账号错误"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.txtuser(ErrorPhone())
        user_page.txtpassword(Pwd())
        user_page.next()
        user_page.error_usertip()
        user_page.screen(self._testMethodDoc)

    def test_self37(self):
        """绑定修改邮箱输入已注册邮箱"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.txtuser(LoginEmail())
        user_page.txtpassword(Pwd())
        user_page.next()
        user_page.error_usertip()
        user_page.screen(self._testMethodDoc)

    def test_self38(self):
        """绑定修改邮箱输入邮箱账号"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.txtuser(RandEmail())
        user_page.txtpassword(Pwd())
        user_page.next()
        user_page.error_usertip()
        user_page.screen(self._testMethodDoc)

    def test_self39(self):
        """绑定修改邮箱原账号为空"""
        user_page = self.login()
        user_page.BDEmail()
        user_page.next()
        user_page.error_usertip()
        user_page.screen(self._testMethodDoc)

    def test_self40(self):
        """绑定修改手机号原账号为空"""
        user_page = self.login()
        user_page.BDPhone()
        user_page.nextphone()
        user_page.error_phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self41(self):
        """绑定修改手机号输入邮箱账号"""
        user_page = self.login()
        user_page.BDPhone()
        user_page.yphone(RandEmail())
        user_page.ypassword(Pwd())
        user_page.nextphone()
        user_page.error_phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self42(self):
        """绑定修改手机号输入已注册邮箱"""
        user_page = self.login()
        user_page.BDPhone()
        user_page.yphone(LoginEmail())
        user_page.ypassword(Pwd())
        user_page.nextphone()
        user_page.error_phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self43(self):
        """绑定修改手机号原账号错误"""
        user_page = self.login()
        user_page.BDPhone()
        user_page.yphone(ErrorPhone())
        user_page.ypassword(Pwd())
        user_page.nextphone()
        user_page.error_phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self19(self):
        """绑定/修改手机号为空"""
        user_page = self.login_email()
        user_page.BDPhone()
        user_page.yphone(LoginEmail())
        user_page.ypassword(Pwd())
        user_page.nextphone()
        user_page.phonebtn()
        time.sleep(3)
        user_page.phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self20(self):
        """绑定/修改手机验证码错误"""
        user_page = self.login_email()
        user_page.BDPhone()
        user_page.yphone(LoginEmail())
        user_page.ypassword(Pwd())
        user_page.nextphone()
        user_page.phone(RandPhone())
        user_page.phonebtn()
        user_page.phonetxt(ErrorNum_6())
        user_page.savephone()
        user_page.phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self21(self):
        """绑定/修改手机验证码不足6位"""
        user_page = self.login_email()
        user_page.BDPhone()
        user_page.yphone(LoginEmail())
        user_page.ypassword(Pwd())
        user_page.nextphone()
        user_page.phone(RandPhone())
        user_page.phonetxt(ErrorNum_5())
        user_page.savephone()
        user_page.phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self22(self):
        """绑定/修改手机手机号错误"""
        user_page = self.login_email()
        user_page.BDPhone()
        user_page.yphone(LoginEmail())
        user_page.ypassword(Pwd())
        user_page.nextphone()
        user_page.phone(ErrorPhone())
        user_page.phonebtn()
        user_page.phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self23(self):
        """绑定/修改手机号已经注册"""
        user_page = self.login_email()
        user_page.BDPhone()
        user_page.yphone(LoginEmail())
        user_page.ypassword(Pwd())
        user_page.nextphone()
        user_page.phone(LoginPhone())
        user_page.phonebtn()
        user_page.phonetip()
        user_page.screen(self._testMethodDoc)

    def test_self24(self):
        """绑定/修改手机成功"""
        user_page =self.login_email()
        user_page.BDPhone()
        user_page.yphone(LoginEmail())
        user_page.ypassword(Pwd())
        user_page.nextphone()
        user_page.phone(RandPhone())
        user_page.phonebtn()
        time.sleep(4)
        user_page.phonetxt(RandPhone())
        user_page.savephone()
        user_page.screen(self._testMethodDoc)

    def test_self25(self):
        """新增收货地址:名字为空"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addincrease()
        time.sleep(2)
        user_page.addtip()
        user_page.screen(self._testMethodDoc)

    def test_self26(self):
        """新增收货地址：名字错误"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addname(Length_1())
        user_page.addincrease()
        user_page.addtip()
        user_page.screen(self._testMethodDoc)

    def test_self27(self):
        """新增收货地址：手机号为空"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addname(Length_4())
        user_page.addincrease()
        user_page.addtip()
        user_page.screen(self._testMethodDoc)

    def test_self28(self):
        """新增收货地址：手机号错误"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addname(Length_4())
        user_page.addphone(ErrorPhone())
        user_page.addincrease()
        user_page.addtip()
        user_page.screen(self._testMethodDoc)

    def test_self29(self):
        """新增收货地址：详细地址为空"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addname(Length_4())
        user_page.addphone(LoginPhone())
        user_page.addpro()
        user_page.addincrease()
        user_page.addtip()
        user_page.screen(self._testMethodDoc)

    def test_self30(self):
        """新增收货地址：新增成功"""
        user_page = self.login()
        user_page.Good()
        user_page.addaddress()
        user_page.addname(Length_4())
        user_page.addphone(LoginPhone())
        user_page.addpro()
        user_page.adddetail(Length_17())
        user_page.addincrease()
        time.sleep(3)
        user_page.screen(self._testMethodDoc)

    def test_self31(self):
        """编辑收货地址：更改用户名字"""
        user_page = self.login()
        user_page.Good()
        user_page.editadd()
        user_page.editname(Length_4())
        user_page.editdefault()
        user_page.editsave()
        user_page.screen(self._testMethodDoc)

    def test_self32(self):
        """编辑收货地址：更改手机号码"""
        user_page = self.login()
        user_page.Good()
        user_page.editadd()
        user_page.editphone(RandPhone())
        time.sleep(3)
        user_page.editsave()
        user_page.screen(self._testMethodDoc)

    def test_self33(self):
        """编辑收货地址：更改地址"""
        user_page = self.login()
        user_page.Good()
        user_page.editadd()
        user_page.editpro()
        user_page.editdetail(Length_17())
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

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    for i in range(1,44):
        testunit.addTest(PersonalCase("test_self%s"%str(i)))
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




