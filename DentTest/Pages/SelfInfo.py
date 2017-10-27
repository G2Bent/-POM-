from selenium.webdriver.common.by import By
from BasePages.BasePage import BasePages
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *
import os,time,random
from Common.Data import *
from selenium.webdriver.common.keys import Keys

class SelfInfo(BasePages):
    """个人中心页面 """
    Edit_loc = (By.XPATH,'//*[@id="btn_edit"]')#编辑
    AlertPsw_loc = (By.XPATH,'//*[@id="btn_edit_pwd"]')#修改密码
    BDEmail_loc = (By.XPATH,'//*[@id="btn_edit_email"]')#绑定/修改邮箱
    BDPhone_loc =(By.XPATH,'//*[@id="btn_edit_phone"]')#绑定/修改手机
    Goods_doc = (By.XPATH,'//*[@id="link-address"]')#收货地址
    Orders_loc = (By.XPATH,'//*[@id="link-order"]')#我的订单

    ''''个人信息页面'''
    edituploadfile_loc = (By.XPATH,'//*[@id="selectfiles"]')#上传按钮
    editName_loc = (By.XPATH,'//*[@id="text-uname"]')#昵称
    editSex_loc = (By.XPATH,'//*[@id="radio_male"]')#性别选择男
    editBir_year_loc = (By.XPATH,'//*[@class="sel_year"]/option[3]')#选择年
    editBir_mon_loc = (By.XPATH,'//*[@class="sel_month"]/option[5]')#选择月
    editBir_day_loc = (By.XPATH,'//*[@class="sel_day"]/option[8]')#选择日  2016-4-7
    save_loc = (By.XPATH,'//*[@id="btn_save"]')#保存按钮
    error_loc = (By.XPATH,'//*[@id="user_error_tips"]')#个人信息错误提示

    '''修改密码'''
    psw_loc = (By.XPATH,'//*[@id="txt_old_pwd"]')#原密码
    new_psw_loc = (By.XPATH,'//*[@id="txt_new_pwd"]')#新密码
    renew_psw_loc = (By.XPATH,'//*[@id="txt_repeat_pwd"]')#确认新密码
    save_pwd_loc = (By.XPATH,'//*[@id="btn_save_pwd"]')#确定按钮
    alerpsw_loc = (By.XPATH,'//*[@id="pwd_error_tips"]')#修改密码错误提示

    '''绑定/修改邮箱页面'''
    email_loc = (By.XPATH,'//*[@id="txt_email"]')#输入邮箱
    email_btn_loc = (By.XPATH,'//*[@id="btn_verify"]')#获取验证码
    email_txt_loc = (By.XPATH,'//*[@id="txt_verify_code"]')#输入验证码
    save_email_loc = (By.XPATH,'//*[@id="btn_save_email"]')#保存邮箱
    bdemail_loc = (By.XPATH,'//*[@id="email_error_tips"]')#绑定/修改邮箱错误提示

    """绑定/修改手机页面"""
    phone_loc = (By.XPATH,'//*[@id="txt_phone"]')#手机号
    phone_btn_loc = (By.XPATH,'//*[@id="btn_phone_verify"]')#获取验证码
    phone_txt_loc =(By.XPATH,'//*[@id="txt_phone_verify_code"]')#输入验证码
    save_phone_loc = (By.XPATH,'//*[@id="btn_save_phone"]')#保存手机
    phonetip_loc = (By.XPATH,'//*[@id="phone_error_tips"]')#手机号错误提示


    """收货地址页面-添加收货地址编辑页"""
    add_address_loc = (By.XPATH,'//*[@id="btn_increase_address"]')#添加收货地址
    addname_loc = (By.XPATH,'//*[@id="txt_username"]') #添加用户名
    addphone_loc = (By.XPATH,'//*[@id="txt_mobile"]')#添加手机号
    addpro_loc = (By.XPATH,'//*[@id="add-province"]/option[10]')#选择省
    addshi_loc = (By.XPATH,'//*[@id="add-city"]/option[1]')#选择市
    addqu_loc = (By.XPATH,'//*[@id="add-district"]/option[3]')#选择区
    adddetail_loc = (By.XPATH,'//*[@id="txt_detail"]')#添加详细地址
    adddefault_loc = (By.XPATH,'//*[@id="cd_default"]')#勾选默认地址
    addincrease_loc = (By.XPATH,'//*[@id="btn_save_increase"]')#确认添加
    addnametip_loc = (By.XPATH,'//*[@id="app"]/div[3]/div/div[3]/div[1]/p')#用户名错误
    addphonetip_loc = (By.XPATH,'//*[@id="app"]/div[3]/div/div[3]/div[2]/p')#手机错误
    adddetailtip_loc = (By.XPATH,'//*[@id="app"]/div[3]/div/div[3]/div[3]/p')#详细地址错误


    """收货地址页面--编辑收货地址页"""
    editadd_loc = (By.XPATH,'//*[@id="btn_edit_address"]')#点击编辑地址
    editname_loc = (By.XPATH,'//*[@id="txt_edit_username"]')#编辑用户名
    editphone_loc = (By.XPATH,'//*[@id="txt_edit_mobile"]')#编辑手机号
    editpro_loc = (By.XPATH,'//*[@id="province"]/option[19]')#选择省份
    editshi_loc = (By.XPATH,'//*[@id="city"]/option[1]')#选择市
    editqu_loc = (By.XPATH,'//*[@id="district"]/option[4]')#选择区
    editdetail_loc = (By.XPATH,'//*[@id="txt_edit_detail"]')#编辑详细地址
    editdefault_loc = (By.XPATH,'//*[@id="cd_edit_default"]')#选择默认地址
    edit_save_loc = (By.XPATH,'//*[@id="btn_save_edit"]')#编辑确认按钮
    editnametip_loc = (By.XPATH,'//*[@id="app"]/div[2]/div/div[3]/div[1]/p')#编辑名字提示
    editphonetip_loc = (By.XPATH,'//*[@id="app"]/div[2]/div/div[3]/div[2]/p')#编辑手机号提示
    editdetailtip_loc = (By.XPATH,'//*[@id="app"]/div[2]/div/div[3]/div[3]/p')#编辑详细地址提示


    """收货地址--删除收货地址"""
    delete_loc = (By.XPATH,'//*[@id="btn_delete_address"]')#删除地址
    deletesub_loc = (By.XPATH,'//*[@id="btn_alert"]')#确认删除地址
    cancledele_loc = (By.XPATH,'//*[@id="btn_cancel"]')#取消删除

    """我的订单页面"""

    """登录"""
    login= (By.XPATH,'//*[@id="txt_user"]')
    loginpsw = (By.XPATH,'//*[@id="pwd_login"]')
    loginbtn = (By.XPATH,'//*[@id="btn_login"]')

    # 操作
    # 通过继承覆盖(overriding)方法：如果子类和父类的方法名相同，优先用子类自己的方法
    # 打开网页
    def open(self):
        # 调用page中的_open打开链接
        self._open(self.base_url, self.pagetitle)

    def Login(self,username,password):
        self.find_element(*self.login).send_keys(username)
        self.find_element(*self.loginpsw).send_keys(password)
        self.find_element(*self.loginbtn).click()

    #个人中心编辑按钮
    def Edit(self):
        self.find_element(*self.Edit_loc).click()

    #个人中心修改密码
    def AlertPsw(self):
        self.find_element(*self.AlertPsw_loc).click()

    #个人中心绑定/修改邮箱
    def BDEmail(self):
        self.find_element(*self.BDEmail_loc).click()

    #个人中心绑定/修改手机
    def BDPhone(self):
        self.find_element(*self.BDPhone_loc).click()

    #个人中心收货地址按钮
    def Good(self):
        self.find_element(*self.Goods_doc).click()

    #个人中心我的订单
    def Oreder(self):
        self.find_element(*self.Orders_loc).click()

    #个人信息：上传头像
    def edituploadfile(self,image):
        self.find_element(*self.edituploadfile_loc).click()
        os.system(os.path.dirname(os.getcwd())+'\Autolt\%s.exe'%image)
        time.sleep(3)

    #个人信息：用户名
    def editselfname(self,name):
        self.find_element(*self.editName_loc).clear()
        self.find_element(*self.editName_loc).send_keys(name)

    #个人信息：性别
    def editselfsex(self):
        self.find_element(*self.editSex_loc).click()

    #个人信息：生日年份
    def editselfbirY(self):
        self.find_element(*self.editBir_year_loc).click()

    #个人信息：生日月份
    def editselfbirM(self):
        self.find_element(*self.editBir_mon_loc).click()

    #个人信息：生日日期
    def editselfbireD(self):
        self.find_element(*self.editBir_day_loc).click()
        time.sleep(3)

    #个人信息：保存
    def saveself(self):
        self.find_element(*self.save_loc).click()

    #个人信息：错误提示
    def error_user(self):
        tips = self.find_element(*self.error_loc)
        assert "昵称由2-16位汉字、字母、数字组成" in tips.text

    #修改密码：错误提示
    def error_psw(self):
        t1 ="旧密码不能为空";t2 = '新密码不能为空';t3 = '确认新密码不能为空'
        t4 = '旧密码不正确';t5 = '密码由6-16字母(区分大小写)、数字组成'
        t6 = '新密码和确认密码不一致'
        tips = self.find_element(*self.alerpsw_loc)
        tip = tips.text
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
        else:
            assert t6 in tip

    #结果截图
    def screen(self,name):
        test_method_name = name
        self.driver.save_screenshot('..\image\个人中心\\'+"%s.png" % test_method_name)

    #修改密码：输入原密码
    def psw(self,password):
        self.find_element(*self.psw_loc).send_keys(password)

    #修改密码：输入新密码
    def newpsw(self,newpassword):
        self.find_element(*self.new_psw_loc).send_keys(newpassword)

    #修改密码：输入确认密码
    def renewpsw(self,renewpassword):
        self.find_element(*self.renew_psw_loc).send_keys(renewpassword)

    #修改密码：保存密码
    def savepsw(self):
        self.find_element(*self.save_pwd_loc).click()

    #绑定/修改邮箱：输入邮箱
    def emailtxt(self,email):
        self.find_element(*self.email_loc).send_keys(email)

    #绑定/修改邮箱：点击获取验证码
    def emailverifybtn(self):
        self.find_element(*self.email_btn_loc).click()
        time.sleep(3)

    #绑定/修改邮箱：输入验证码
    def emailverifytxt(self,code):
        if "@" in code:
            self.find_element(*self.email_txt_loc).send_keys(BD_code(code))
            time.sleep(5)
        else:
            self.find_element(*self.email_txt_loc).send_keys(code)

    #绑定/修改邮箱：保存邮箱
    def emailsave(self):
        self.find_element(*self.save_email_loc).click()

    #绑定/修改邮箱：错误提示
    def emailtips(self):
        t1 ="邮箱或验证码不能为空";t2 = "邮箱格式不正确";t3 = "验证码错误"
        t4 = "验证码应为六位纯数字";t5 = "该邮箱已注册"
        tips = self.find_element(*self.bdemail_loc)
        tip = tips.text
        if tip == t1:
            assert t1 in tip
        elif tip == t2:
            assert t2 in tip
        elif tip == t3:
            assert t3 in tip
        elif tip ==t4:
            assert t4 in tip
        else:
            assert t5 in tip

    #绑定/修改手机号：输入手机号
    def phone(self,phone):
        self.find_element(*self.phone_loc).clear()
        self.find_element(*self.phone_loc).send_keys(phone)

    # 绑定/修改手机号：获取手机验证码
    def phonebtn(self):
        self.find_element(*self.phone_btn_loc).click()

    # 绑定/修改手机号：输入手机验证码
    def phonetxt(self,code):
        if len(code) == 11:
            self.find_element(*self.phone_txt_loc).send_keys(verify_code(code))
        else:
            self.find_element(*self.phone_txt_loc).send_keys(code)

    # 绑定/修改手机号：确认绑定/修改
    def savephone(self):
        self.find_element(*self.save_phone_loc).click()

    # 绑定/修改手机号，错误提示
    def phonetip(self):
        t1 = "手机号格式不正确";t2 = "手机号或验证码不能为空";t3 = "验证码应为六位纯数字"
        t4 = "验证码错误";t5 = "该手机号已注册"
        tips = self.find_element(*self.phonetip_loc)
        tip =tips.text
        if tip == t1:
            assert t1 in tip
        elif tip == t2:
            assert t2 in tip
        elif tip == t3:
            assert t3 in tip
        elif tip == t4:
            assert t4 in tip
        else:
            assert t5 in tip
    #添加收货地址:点击添加收货地址
    def addaddress(self):
        self.find_element(*self.add_address_loc).click()

    #添加收货地址:输入用户名
    def addname(self,name):
        self.find_element(*self.addname_loc).clear()
        self.find_element(*self.addname_loc).send_keys(name)

    #添加收货地址:输入手机号
    def addphone(self,phone):
        self.find_element(*self.addphone_loc).clear()
        self.find_element(*self.addphone_loc).send_keys(phone)

    #添加收货地址:增加省市区
    def addpro(self):
        self.find_element(*self.addpro_loc).click()
        self.find_element(*self.addshi_loc).click()
        self.find_element(*self.addqu_loc).click()

    #添加收货地址:输入详细地址
    def adddetail(self,detail):
        self.find_element(*self.adddetail_loc).send_keys(detail)

    #添加收货地址:默认
    def adddefault(self):
        self.find_element(*self.adddefault_loc).click()

    #添加收货地址:点击确认添加
    def addincrease(self):
        self.find_element(*self.addincrease_loc).click()

    #新增收货地址：错误提示
    def addtip(self):
        t1 = "姓名不能为空";t2 = "姓名由2-16位汉字、字母、数字组成";t3 = "手机号不能为空"
        t4 = "手机号格式不正确";t5 = "详细地址不能为空"
        tip =self.find_element(*self.addnametip_loc).text
        tip1 = self.find_element(*self.addphonetip_loc).text
        tip2 = self.find_element(*self.adddetailtip_loc).text
        if tip == t1:
            assert t1 in tip
        elif tip == t2:
            assert t2 in tip
        elif tip1 == t3:
            assert t3 in tip1
        elif tip1 == t4:
            assert t4 in tip1
        else:
            assert t5 in tip2

    #编辑收货地址:编辑收货地址
    def editadd(self):
        i = random.randint(1,4)
        self.find_elements(*self.editadd_loc)[i].click()

    # 编辑收货地址:输入用户名
    def editname(self,name):
        # self.find_element(*self.editname_loc).clear()
        self.find_element(*self.editname_loc).send_keys(Keys.CONTROL+'a')
        self.find_element(*self.editname_loc).send_keys(name)

    # 编辑收货地址:输入手机号
    def editphone(self,phone):
        self.find_element(*self.editphone_loc).send_keys(Keys.CONTROL + 'a')
        self.find_element(*self.editphone_loc).send_keys(phone)

    # 编辑收货地址:选择省份
    def editpro(self):
        self.find_element(*self.editpro_loc).click()
        self.find_element(*self.editshi_loc).click()
        self.find_element(*self.editqu_loc).click()

    # 编辑收货地址:输入详细地址
    def editdetail(self,detail):
        self.find_element(*self.editdetail_loc).send_keys(Keys.CONTROL + 'a')
        self.find_element(*self.editdetail_loc).send_keys(detail)

    # 编辑收货地址:选择默认
    def editdefault(self):
        self.find_element(*self.editdefault_loc).click()

    # 编辑收货地址:点击保存编辑
    def editsave(self):
        self.find_element(*self.edit_save_loc).click()
        time.sleep(2)

    # 编辑收货地址：错误提示
    def edittip(self):
        t1 = "姓名不能为空";t2 = "姓名由2-16位汉字、字母、数字组成";t3 = "手机号不能为空"
        t4 = "手机号格式不正确";t5 = "详细地址不能为空"
        tip = self.find_element(*self.editnametip_loc).text
        tip1 = self.find_element(*self.editphonetip_loc).text
        tip2 = self.find_element(*self.editdetailtip_loc).text
        if tip == t1:
            assert t1 in tip
        elif tip == t2:
            assert t2 in tip
        elif tip1 == t3:
            assert t3 in tip1
        elif tip1 == t4:
            assert t4 in tip1
        else:
            assert t5 in tip2

    # 删除地址
    def deleteadd(self):
        i = random.randint(1,3)
        self.find_elements(*self.delete_loc)[i].click()

    #确认删除地址
    def subdele(self):
        self.find_element(*self.deletesub_loc).click()

    #取消删除地址
    def cancledele(self):
        self.find_element(*self.cancledele_loc).click()
