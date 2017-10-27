class ApiOpenException(Exception):
    def __init__(self,err='验证码返回值为空，接口异常！'):
        Exception.__init__(self,err)

class ApiStateException(Exception):
    def __init__(self,err='接口返回的状态不为True！'):
        Exception.__init__(self,err)

class TimeoutException(Exception):
    def __int__(self,err = '等待超时异常'):
        Exception.__init__(self,err)

class MobileCodeNoeException(Exception):
    def __init__(self,err='获取验证码的接口异常'):
        Exception.__init__(self,err)

class Error(Exception):
    def __init__(self,err='不存在的'):
        Exception.__init__(self,err)