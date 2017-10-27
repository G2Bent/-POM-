from selenium import webdriver
from selenium.webdriver.common.by import By
from BasePages.BasePage import BasePages

class Forgetpwd(BasePages):
    Forgetpsw = (By.XPATH,'//*[@id="link_forget_pwd"]')#忘记密码按钮
    phone_loc = (By.XPATH,'//*[@id="txt_user"]')#输入手机号
    verifybtn_loc = (By.XPATH,'//*[@id="btn_verify"]')#获取验证码按钮
    verifytxt_loc = (By.XPATH,'//*[@id="txt_verify_code"]')#输入验证码
    newpwd_loc = (By.XPATH,'//*[@id="txt_new_pwd"]')#输入新密码
    renewpwd_loc = (By.XPATH,'//*[@id="txt_repeat_pwd"]')#确认新密码
    submit_loc = (By.XPATH,'//*[@id="btn_find_pwd"]')#确认按钮
