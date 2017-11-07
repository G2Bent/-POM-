import random,time

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
    return phone

#登录手机号
def LoginPhone():
    phone = ["15816038158"]
    for i in phone:
        return i

#邮箱登录
def LoginEmail():
    email = ["648604875@qq.com","944921374@qq.com"]
    for i in random.sample(email, 1):
        return i

#找回密码
def FindPassword():
    phone = ["13217665001","15816038158","648604875@qq.com","944921374@qq.com"]
    for i in random.sample(phone,1):
        return i

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









