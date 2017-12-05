import random,time

#正确的密码
def Pwd():
    pwd = ["a123456"]
    for i in pwd:
        return i

#不足6位数
def ErrorNum_5():
    i = time.strftime("%M%S")
    return i

#错误验证码
def ErrorNum_6():
    i = time.strftime("%H%M%S")
    return i