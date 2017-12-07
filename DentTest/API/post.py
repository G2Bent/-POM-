import requests
import json
from Common.Exception import *

def delephone(phone):
    postdata = {'phone':phone}
    headers = {'content-type': 'application/json'}
    r = requests.post('http://112.74.29.84:23301/api/User/deleteuser',data=json.dumps(postdata),headers=headers)
    token_str = r.text
    token_dict = json.loads(token_str)
    if token_dict['success'] == True:
        return True
    else:
        return False


