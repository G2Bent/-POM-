import random,time
from openpyxl import load_workbook

wb = load_workbook("dent.xlsx")
sheet = wb.get_sheet_by_name("Phone")

def RegPhone():
    """
    注册使用的手机号码
    :return:返回手机号码，固定手机号码
    """
    num = ["13217665001"]
    for p in num:
        return p

def RandEmail():
    """
    注册和绑定邮箱使用的邮箱账号，邮箱账号的格式为当前日期+@dent.com
    :return:返回随机的邮箱账号，实际邮箱不存在
    """
    now = time.strftime("%Y%m%d%H%M%S"+"@dent.com")
    return now

def RandPhone():
    """
    绑定页面使用的手机号码
    :return:返回手机号码
    """
    phone = ["15812487685"]
    for i in phone:
        return i

def LoginPhone():
    """
    登录页面使用到的手机号码
    :return:返回excel表中的手机号码，该手机号必须是已经注册的手机号
    """
    phone = sheet["C"]
    for i in phone:
        return i.value

def LoginEmail():
    """
    邮箱登录使用的邮箱账号
    :return:返回excel表中的邮箱账号，该邮箱必须是已经注册的邮箱
    """
    email = sheet["D"]
    for i in email:
        return i.value

def FindPassword():
    """
    忘记密码页面，找回密码使用到的邮箱
    :return:返回已经注册的邮箱账号
    """
    phone = sheet["E"]
    for i in random.sample(phone,1):
        return i.value

def ErrorEmail():
    """
    使用到的错误邮箱页面，包括：注册，登录，找回密码，绑定邮箱
    :return: 返回随机错误邮箱格式
    """
    now =time.strftime("%Y%m%d%H%M%S"+".com")
    return now

def ErrorPhone():
    """
    使用到错误手机号码页面，包括：注册，登录，找回密码，绑定手机
    :return:返回随机的错误手机格式号码
    """
    phone = time.strftime("155"+"%H%M%S")
    return phone

def UnRegPhone():
    """
    使用到未注册手机号码页面，包括：登录，找回密码，绑定手机
    :return:返回随机正确的手机格式号码
    """
    phone = time.strftime("188"+"%d%H%M%S")
    return phone

def UnRegEamil():
    """
    使用到未注册邮箱账号页面，包括：登录，找回密码，绑定邮箱
    :return:
    """
    email = time.strftime("%d%H%M%S"+'@dent.com')
    return email








