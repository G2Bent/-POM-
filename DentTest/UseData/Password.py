import random,time
from openpyxl import load_workbook

wb = load_workbook("dent.xlsx")
sheet = wb.get_sheet_by_name("Phone")

def Pwd():
    """
    通用的正确密码
    :return:返回excel中的密码
    """
    pwd = sheet["F"]
    for i in pwd:
        return i.value

#不足6位数
def ErrorNum_5():
    """
    使用不足6位数的随机号码页面，包括：注册，登录，找回密码，修改密码，输入的验证码
    :return:返回5位数的随机号码
    """
    i = time.strftime("%M%S")
    return i

#错误验证码
def ErrorNum_6():
    """
    使用随机验证码页面，包括：注册，找回密码，绑定邮箱，绑定手机
    :return:返回6位随机数
    """
    i = time.strftime("%H%M%S")
    return i