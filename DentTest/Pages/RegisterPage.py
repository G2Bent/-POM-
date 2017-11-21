from selenium.webdriver.common.by import By
from BasePages.BasePage import BasePages
from Common.Data import verify_code
import time

class RegisterPage(BasePages):
    #定位器，通过元素属性定位元素对象
    username_loc = (By.XPATH,'//*[@id="txt_user"]')#输入手机号/邮箱
    verify_code_btn = (By.XPATH,'//*[@id="btn_verify"]')#点击获取验证码
    verify_code_loc = (By.XPATH,'//*[@id="txt_verify_code"]')#输入验证码
    password_loc = (By.XPATH,'//*[@id="pwd_set"]')#输入密码
    repassword_loc = (By.XPATH,'//*[@id="pwd_repeat"]')#输入确认密码
    submit_loc = (By.XPATH,'//*[@id="btn_reg"]')#注册按钮
    loginurl_loc = (By.XPATH,'//*[@id="login"]')#点击登录url
    tips_loc = (By.XPATH,'//*[@id="error_tips"]')#错误提示
    # re_loc = (By.XPATH, '//*[@class="user-title"]')  # "个人中心"文本校验

    # 操作
    # 通过继承覆盖(overriding)方法：如果子类和父类的方法名相同，优先用子类自己的方法
    # 打开网页
    def open(self):
        # 调用page中的_open打开链接
        self._open(self.base_url, self.pagetitle)

    #输入用户名：调用send_keys对象，输入手机号/邮箱
    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    #输入用户名：调用send_keys对象，输入手机号/邮箱，点击获取邮箱，输入邮箱
    def input_name(self,num):
        self.find_element(*self.username_loc).send_keys(num)
        self.find_element(*self.verify_code_btn).click()
        time.sleep(5)
        if len(num) >= 11:
            self.find_element(*self.verify_code_loc).send_keys(verify_code(num))
        else:
            self.find_element(*self.verify_code_loc).send_keys(num)

    #输入密码：调用send_keys对象，输入密码
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    # 输入确认密码：调用send_keys对象，输入确认密码
    def input_repassword(self, repassword):
        self.find_element(*self.repassword_loc).send_keys(repassword)

    #点击获取验证码：调用click对象，点击获取验证码
    def click_verify(self):
        self.find_element(*self.verify_code_btn).click()

    #输入验证码：调用send_keys对象，输入验证码
    def input_verify(self,code):
        if len(code) >= 11:
            self.find_element(*self.verify_code_loc).send_keys(verify_code(code))
        else:
            self.find_element(*self.verify_code_loc).send_keys(code)

    #点击注册：调用click对象，点击注册
    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    #点击“登录”：调用click对象，点击“登录”
    def click_login(self):
        self.find_element(*self.loginurl_loc).click()

    #用户名或者密码不合理tip框内容提示
    def show_tips(self):
        t1="两次输入的密码不一致";t2="手机号/邮箱格式不正确";
        t3= "密码由6-16字母(区分大小写)、数字组成"
        return self.find_element(*self.tips_loc).text

    #个人中心，注册成功校验
    # def show_(self):
    #     return self.find_element(*self.re_loc).text

