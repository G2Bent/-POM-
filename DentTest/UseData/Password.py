import random,time,string
from openpyxl import load_workbook

wb = load_workbook("dent.xlsx")
sheet = wb.get_sheet_by_name("Phone")

def GenWord(length):
    #随机出数字的个数
    numOfNum = random.randint(1,length-1)
    numOfLetter = length-numOfNum
    #选中numOfNum个数字
    slcNum = [random.choice(string.digits) for i in range(numOfNum)]
    #选中numOfLetter个字母
    slcLetter = [random.choice(string.ascii_letters) for i in range(numOfLetter)]

    #打乱这个组合
    slcChar = slcNum+slcLetter
    random.shuffle(slcChar)

    #生成密码
    genword = ''.join([i for i in slcChar])
    return genword

def Pwd():
    """
    通用的正确密码
    :return:返回excel中的密码
    """
    pwd = sheet["F"]
    for i in pwd:
        return i.value

def ErrorNum_5():
    """
    使用不足6位数的随机号码页面，包括：注册，登录，找回密码，修改密码，输入的验证码
    :return:返回5位数的随机号码
    """
    i = GenWord(5)
    return i

def ErrorNum_6():
    """
    使用随机验证码页面，包括：注册，找回密码，绑定邮箱，绑定手机
    :return:返回6位随机数
    """
    i = GenWord(6)
    return i