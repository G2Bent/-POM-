import random
import string

def GB2312():
    head = random.randint(0x4E00, 0x9FA5)
    return head

def Num(num):
    s = ''
    for i in range(num):
        s = s+chr(GB2312())
    return s

#低于两个长度
def Length_1():
    name  = ["a","好",'@','1']
    for i in random.choices(name):
        return i

#正确长度
def Length_4():
    length = Num(4)
    return length

#长度超过16位
def Length_17():
    length = Num(17)
    return length

def Length_31():
    length = Num(31)
    return length

