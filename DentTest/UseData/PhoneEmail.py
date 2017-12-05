import random,time
from openpyxl import load_workbook

wb = load_workbook("dent.xlsx")
sheet = wb.get_sheet_by_name("Phone")

#手机注册
def RegPhone():
    num = ["13217665001"]
    for p in num:
        return p

#注册/绑定邮箱
def RandEmail():
    now = time.strftime("%Y%m%d%H%M%S"+"@dent.com")
    return now

#绑定手机号
def RandPhone():
    phone = ["15812487685"]
    for i in phone:
        return i

#登录手机号
def LoginPhone():
    phone = sheet["C"]
    for i in phone:
        return i.value

#邮箱登录
def LoginEmail():
    email = sheet["D"]
    for i in email:
        return i.value

#找回密码
def FindPassword():
    phone = sheet["E"]
    for i in random.sample(phone,1):
        return i.value

#错误邮箱
def ErrorEmail():
    now =time.strftime("%Y%m%d%H%M%S"+".com")
    return now

#错误手机号
def ErrorPhone():
    phone = time.strftime("155"+"%H%M%S")
    return phone

#未注册手机号码
def UnRegPhone():
    phone = time.strftime("188"+"%d%H%M%S")
    return phone









