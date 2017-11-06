from Common.Exception import *
from copy import copy
import json,urllib.request,unittest,requests

#获取注册验证码
def verify_code(code):
    TOKEN_URL = 'http://112.74.29.84:23301/api/System/gettoken'
    respone = requests.get(TOKEN_URL)
    if respone.status_code ==200:
        token_str = respone.text
        token_dict = json.loads(token_str)
        if token_dict['success'] == True:
            TOKEN = token_dict['data']['token']
            code_dict = None
            if "@" in str(code):
                #http://112.74.29.84:23301/api/User/getemailverifycode?token=ceece58d221f4549993a8cf469751fae&email=944921374@qq.com&type=2
                #http://112.74.29.84:23301/api/User/getemailverifycode?token=d63417d4c8ab4986ad37e7080d742c09&email=648604875@qq.com&type=1
                url = 'http://112.74.29.84:23301/api/User/getemailverifycode?token='+str(TOKEN)+'&email='+str(code)+'&type=1'
            else:
                url = 'http://112.74.29.84:23301/api/User/getphoneverifycode?token='+str(TOKEN)+'&phone='+str(code)+'&type=1'
            try:
                code_dict = json.loads(urllib.request.urlopen(url).read())
            except Exception as e :
                print (e)
            if code_dict != None:
                if code_dict['success'] == True:
                    return code_dict['data']['verifycode']
                else:
                    raise ApiStateException
            else:
                raise ApiOpenException

#获取德雅个人信息邮箱绑定验证码
def BD_code(code):
    TOKEN_URL = 'http://112.74.29.84:23301/api/System/gettoken'
    respone = requests.get(TOKEN_URL)
    if respone.status_code == 200:
        token_str = respone.text
        token_dict = json.loads(token_str)
        if token_dict['success'] == True:
            TOKEN = token_dict['data']['token']
            code_dict = None
            if '@' in str(code):
                url = 'http://112.74.29.84:23301/api/User/getemailverifycode?token='+str(TOKEN)+'&email='+str(code)+'&type=3'
            else:
                url = 'http://112.74.29.84:23301/api/User/getphoneverifycode?token='+str(TOKEN)+'&phone='+str(code)+'&type=3'
            try:
                code_dict=json.loads(urllib.request.urlopen(url).read())
            except Exception as e:
                print(e)
            # print(code_dict)
            if code_dict != None:
                if code_dict['success'] == True:
                    # print(code_dict['data']['verifycode'])
                    return code_dict['data']['verifycode']
                else:
                    raise ApiStateException
            else:
                raise ApiOpenException
# print(email_code("15500000000"))

def find_pwd(find):
            #http://112.74.29.84:23301/api/User/getemailverifycode?email=944921374@qq.com&type=2
            #http://112.74.29.84:23301/api/User/getphoneverifycode?phone=18814128583&type=2
    TOKEN_URL = 'http://112.74.29.84:23301/api/System/gettoken'
    respone = requests.get(TOKEN_URL)
    if respone.status_code == 200:
        token_str = respone.text
        token_dict = json.loads(token_str)
        if token_dict['success'] == True:
            TOKEN = token_dict['data']['token']
            code_dict = None
            if '@' in str(find):
                #http://112.74.29.84:23301/api/User/getemailverifycode?token=1d2f9680e0704a2e927211f0695fdc44&email=944921374@qq.com&type=2
                url = 'http://112.74.29.84:23301/api/User/getemailverifycode?token='+str(TOKEN)+'&email='+str(find)+'&type=2'
                print(url)
            else:
                url = 'http://112.74.29.84:23301/api/User/getphoneverifycode?token='+str(TOKEN)+'&phone='+str(find)+'&type=2'
            try:
                code_dict = json.loads(urllib.request.urlopen(url).read())
            except Exception as e:
                print(e)
                # print(code_dict)
            if code_dict != None:
                if code_dict['success'] == True:
                        # print(code_dict['data']['verifycode'])
                    return code_dict['data']['verifycode']
                else:
                    raise ApiStateException
            else:
                raise ApiOpenException



print(verify_code("15812487685"))



