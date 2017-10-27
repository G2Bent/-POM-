import os
from BasePages.File_Read import *

#根目录    这些应该叫做宏定义
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print(BASE_PATH)
#print(BASE_PATH)
#配置文件路径
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yaml')
print("这是config路径："+CONFIG_FILE)
#数据文件路径
DATA_PATH = os.path.join(BASE_PATH,'Excel_Data')
print("这是excel文件路径："+DATA_PATH)
#driver路径
DRIVER_PATH = os.path.join(BASE_PATH,'driver')
#日志路径
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
print(REPORT_PATH)
class Config(object):
    def __init__(self,config=CONFIG_FILE):
        self.config = YamlReader(config).data  #创建YamlReaderd对象，传入配置文件，返回数据
    def get(self,element,index=0): #相当于重写get方法
        return self.config[index].get(element)  #数据config通过这种形式获取值  字典类型的数据存在内置方法get
#
# if __name__=='__main__':
#     con = Config(config=CONFIG_FILE)
#     con.get('URL')