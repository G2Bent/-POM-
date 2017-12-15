import random
import string
from openpyxl import load_workbook


wb = load_workbook("dent.xlsx")
sheet = wb.get_sheet_by_name("TXT")

def GB2312():
    """
    这里使用的是2万汉字
    :return:返回随机汉字，但是陌生字会比较多
    """
    head = random.randint(0x4E00, 0x9FA5)
    return head

def GBK2312():
    """
    这里使用的是6000字汉字，用来被调用的方法
    :return: 返回随机汉字，陌生字相对会比较少
    """
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str

def Num(num):
    """
    生成随机汉字，用来被调用的方法
    :param num:调用获取汉字的方法，返回定义的个数
    :return:
    """
    s = ''
    for i in range(num):
        s = s+GBK2312()
    return s

def Length_1():
    """
    获取excel表中的字符，低于两个长度的字符，使用页面：个人昵称
    :return:返回excel表中的随机字符
    """
    name  = sheet["A"]
    for i in random.choices(name):
        return i.value

def Length_4():
    """
    正确长度的字符长度，使用页面：个人昵称
    :return:返回4个字符长度的汉字，调用随机汉字GBK2312方法
    """
    length = Num(4)
    return length

def Length_17():
    """
    超出16字符长度的汉字，使用页面包括：个人姓名编辑，增加
    :return:返回17字符长度的汉字
    """
    length = Num(17)
    return length

def Length_31():
    """
    超出30字符的汉字，使用页面包括：收货地址增加，编辑
    :return: 返回31字符长度的汉字
    """
    length = Num(31)
    return length

