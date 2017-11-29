import requests
import json

def delephone(phone):
    postdata = {'phone':phone}
    headers = {'content-type': 'application/json'}
    r = requests.post('http://112.74.29.84:23301/api/User/deleteuser',data=json.dumps(postdata),headers=headers)
    token_str = r.text
    token_dict = json.loads(token_str)
    if token_dict['success'] == True:
        print("删除成功！")
    else:
        print("删除失败")
