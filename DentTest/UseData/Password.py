import random,time

#低于6位数
def ErrorPwd():
    now = time.strftime("%M%S")
    return now

#正确的密码
def Pwd():
    pwd = ["a123456"]
    for i in pwd:
        return i

#验证码不足6位
def Errorverify_5():
    verify = ['12345']
    for i in verify:
        return i

#错误验证码
def Errorverify_6():
    verify = ['123456']
    for i in verify:
        return i