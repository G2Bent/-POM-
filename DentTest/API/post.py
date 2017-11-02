import requests

def postphone():
    url = 'http://192.168.2.72:5001/api/User/deleteuser'
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Referer":"http://192.168.2.72:5001/swagger/",
        "Origin":"http://192.168.2.72:5001",
        "Host":"192.168.2.72:5001",
        "Content-Type":"application/json-patch+json",
        "Content-Length":"28",
        "Connection":"keep-alive",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept":"application/json",
    }

    payload = {"phone":"15816038158"}

    phone = requests.post(url,json=payload,headers=headers,verify = False)
    return phone

def postemail():
    url = 'http://192.168.2.72:5001/api/User/deleteuserbyemail'
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Referer":"http://192.168.2.72:5001/swagger/",
        "Origin":"http://192.168.2.72:5001",
        "Host":"192.168.2.72:5001",
        "Content-Type":"application/json-patch+json",
        "Content-Length":"33",
        "Connection":"keep-alive",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept":"application/json",
    }

    payload = {"email":"944921374@qq.com"}

    email = requests.post(url,json=payload,headers=headers,verify = False)
    return email