from selenium.webdriver.common.by import By
from BasePages.BasePage import BasePages
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *

class LoginPage(BasePages):
    #定位器，通过元素属性定位元素对象
    username_loc = (By.XPATH,'//*[@id="txt_user"]')#输入手机号/邮箱
    password_loc = (By.XPATH,'//*[@id="pwd_login"]')#输入密码
    submit_loc = (By.XPATH,'//*[@id="btn_login"]')#登录按钮
    Forgetpsw_loc = (By.XPATH,'//*[@id="link_forget_pwd"]')#忘记密码
    RegisterUrl_loc = (By.XPATH,'//*[@id="register"]')#点击注册url
    tips_loc = (By.XPATH,'//*[@id="error_tips"]')#错误提示
    findtext_loc = (By.XPATH,'//*[@class="find-pwd-box"]/h1')#找回密码页面文本
    regtext_loc = (By.XPATH,'//*[@class="user-explain"]/p[2]')#点击“注册”文本
    re_loc = (By.XPATH,'//*[@class="user-title"]')#"个人中心"文本校验
    logout_loc = (By.XPATH,'//*[@id="header"]/div/div[3]/div/div/ul/li[2]/a')#退出登录
    touxiang_loc = (By.XPATH,'//*[@id="header"]/div/div[3]/div/div')#个人信息icon

    # 操作
    # 通过继承覆盖(overriding)方法：如果子类和父类的方法名相同，优先用子类自己的方法
    # 打开网页
    def open(self):
        # 调用page中的_open打开链接
        self._open(self.base_url, self.pagetitle)

    #输入用户名：调用send_keys对象，输入用户名
    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    #输入密码：调用send_keys对象，输入密码
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    #点击登录：调用click对象，点击登录
    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    # 点击登录：调用click对象，点击登录
    def click_submit_key(self):
        self.find_element(*self.submit_loc).send_keys(Keys.ENTER)

    #点击“忘记密码”：调用click对象，点击“忘记密码”
    def click_psw(self):
        self.find_element(*self.Forgetpsw_loc).click()

    #点击“注册”：调用click对象，点击“注册”
    def click_reg(self):
        self.find_element(*self.RegisterUrl_loc).click()

    #用户名或者密码不合理tip框内容提示
    def show_tips(self):
        return self.find_element(*self.tips_loc).text

    #登录成功页面中的用户ID查找
    def show_(self):
        return self.find_element(*self.re_loc).text

    #退出登录
    def logout(self):
        self.find_element(*self.touxiang_loc).click()
        self.find_element(*self.logout_loc).click()

    #跳转注册页面关键字查找
    def show_regtip(self):
        return self.find_element(*self.regtext_loc).text

    #忘记密码关键字查找
    def show_findtip(self):
        return self.find_element(*self.findtext_loc).text
