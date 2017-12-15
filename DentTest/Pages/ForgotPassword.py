from selenium import webdriver
from selenium.webdriver.common.by import By
from BasePages.Selenium2 import Sele
from Common.Data import *
from Pages.Errortip import error
import time

class Forgetpwd(Sele):
    Forgetpsw = (By.XPATH,'//*[@id="link_forget_pwd"]')#忘记密码按钮
    phone_loc = (By.XPATH,'//*[@id="txt_user"]')#输入手机号
    verifybtn_loc = (By.XPATH,'//*[@id="btn_verify"]')#获取验证码按钮
    verifytxt_loc = (By.XPATH,'//*[@id="txt_verify_code"]')#输入验证码
    newpwd_loc = (By.XPATH,'//*[@id="txt_new_pwd"]')#输入新密码
    renewpwd_loc = (By.XPATH,'//*[@id="txt_repeat_pwd"]')#确认新密码
    submit_loc = (By.XPATH,'//*[@id="btn_find_pwd"]')#确认按钮
    forgettip_loc = (By.XPATH,'//*[@id="error_tips"]')#错误提示

# 操作
    # 通过继承覆盖(overriding)方法：如果子类和父类的方法名相同，优先用子类自己的方法
    # 打开网页
    def open(self):
        # 调用page中的_open打开链接
        self._open(self.base_url, self.pagetitle)

    #点击忘记密码按钮
    def Forgetpwd(self):
        self.find_element(*self.Forgetpsw).click()
        time.sleep(2)

    #找回密码
    def find(self,phone):
        self.find_element(*self.phone_loc).send_keys(phone)
        self.find_element(*self.verifybtn_loc).click()
        time.sleep(4)
        self.find_element(*self.verifytxt_loc).send_keys(find_pwd(phone))
        time.sleep(3)

    #输入手机号
    def phone(self,phone):
        self.find_element(*self.phone_loc).send_keys(phone)

    #点击获取验证码
    def btnverify(self):
        self.find_element(*self.verifybtn_loc).click()
        time.sleep(3)

    #输入验证码
    def verifytxt(self,code):
        if '@' in code:
            self.find_element(*self.verifytxt_loc).send_keys(find_pwd(code))
        elif len(code) == 11:
            self.find_element(*self.verifytxt_loc).send_keys(find_pwd(code))
        else:
            self.find_element(*self.verifytxt_loc).send_keys(code)
        time.sleep(3)

    #输入新密码
    def newpwd(self,pwd):
        self.find_element(*self.newpwd_loc).send_keys(pwd)

    #输入确认密码
    def renewpwd(self,repwd):
        self.find_element(*self.renewpwd_loc).send_keys(repwd)

    #点击确认按钮
    def submitbtn(self):
        self.find_element(*self.submit_loc).click()

    #错误提示
    def tip(self):
        """
        这里表示忘记密码错误提示
        :return:返回错误提示和实际情况是否相同，如果不同这条测试用例则不通过
        """
        tip = self.find_element(*self.forgettip_loc).text
        if tip in error():
            assert error() in tip

    def screen(self,name):
        '''
        :param name:这里表示截图
        :return:返回忘记密码截图的图片
        '''
        test_method_name = name
        self.driver.save_screenshot('..\image\忘记密码\\'+"%s.png" % test_method_name)
