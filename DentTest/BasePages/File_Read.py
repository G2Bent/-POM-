#这个类是用来读取yaml配置文件的内容的
import yaml
import os
from xlrd import open_workbook

class YamlReader:
    def __init__(self,yamlf):     #创建对象时初始化yaml变量
        if os.path.exists(yamlf): #判断配置文件是否存在,后面是通过config类传值进来
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在')
        self.__data = None

    @property
    def data(self):
        if not self.__data:
            with open(self.yamlf,'rb') as f:
                self.__data = list(yaml.safe_load_all(f))  #如果string或文件包含几块yaml文档，你可以使用yaml.load_all来解析全部的文档。
                #yaml.load_all 会生成一个迭代器，你要做的就是for 读出来
            return self.__data
class SheetTypeError(Exception):
    pass

class ExcelReader(object):
    def __init__(self,excel,sheet=0,title_line = True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('excel 文件没有找到')
        self.sheet = sheet
        self.tile_line = title_line
        self.__excel_data = list() #excel中读出数据展示为list类型
    @property
    def excel_data(self):
        if not self.__excel_data:        #如果第一次访问，没有数据python中非None的数据都为true
            workbook = open_workbook(self.excel)  #打开excel表
            if type(self.sheet) not in [int ,str]:
                raise SheetTypeError('plese pass in <type int>or<type str>,not{0}',format(type(self.sheet)))
            elif type(self.sheet)==int:
                s = workbook.sheet_by_index(self.sheet) #通过索引找到sheet内容，返回一个对象
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.tile_line:   #为true的时候执行
                title = s.row_values(0)   #将第一行作为title
                for row in range(1,s.nrows):
                    self.__excel_data.append(dict(zip(title,s.row_values(row))))#s.row_values(row)获得每一行的值，其实返回的是list类型
                    #zip函数可以将两个list转换为元组，然后转换为dict
            else:
                for row in range(0,s.nrows):
                    self.__excel_data.append(s.row_values(row))  #如果为false则直接执行这里，返回的就是list类型
        print("输出excel数据")
        print(self.__excel_data)
        return self.__excel_data
