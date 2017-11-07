from selenium import webdriver
from selenium.webdriver.common.by import By
from BasePages.BasePage import BasePages
from Common.Data import *
import time

class Forgetpwd(BasePages):
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
        t1 = "该手机号未注册，无法用于密码找回";t2 = "该邮箱未注册，无法用于密码找回";
        t3 = "手机号/邮箱格式不正确";t4="手机号/邮箱不能为空";t5 = "验证码错误"
        t6 = "验证码应为六位纯数字";t7 = "密码由6-16字母(区分大小写)、数字组成"
        t8 = "两次输入的密码不一致";t9 = "手机号/邮箱不能为空";t10 = '新密码或确认密码不能为空'
        tip = self.find_element(*self.forgettip_loc).text

        if tip == t1:
            assert t1 in tip
        elif tip == t2:
            assert t2 in tip
        elif tip == t3:
            assert t3 in tip
        elif tip == t4:
            assert t4 in tip
        elif tip == t5:
            assert t5 in tip
        elif tip == t6:
            assert t6 in tip
        elif tip == t7:
            assert t7 in tip
        elif tip == t8:
            assert t8 in tip
        elif tip == t9:
            assert t9 in tip
        else:
            assert t10 in tip

    def screen(self,name):
        test_method_name = name
        self.driver.save_screenshot('..\image\忘记密码\\'+"%s.png" % test_method_name)
