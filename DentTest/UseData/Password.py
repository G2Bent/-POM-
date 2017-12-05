import random,time

#正确的密码
def Pwd():
    pwd = ["a123456"]
    for i in pwd:
        return i

#不足6位数
def ErrorNum_5():
    i = random.randint(1,99999)
    return i

#错误验证码
def ErrorNum_6():
    i = random.randint(100000,999999)
    return i