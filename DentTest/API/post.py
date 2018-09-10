import requests
import json
from Common.Exception import *

def delephone(phone):
    """
    这里是接口返回手机号码删除
    :param phone:输入手机号码
    :return:删除该手机号码
    """
    postdata = {'phone':phone}
    headers = {'content-type': 'application/json'}
    r = requests.post('http://***.74.**.**:23301/api/User/deleteuser',data=json.dumps(postdata),headers=headers)
    token_str = r.text
    token_dict = json.loads(token_str)
    if token_dict['success'] == True:
        return True
    else:
        return False


