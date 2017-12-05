import random,time
from openpyxl import load_workbook

wb = load_workbook("dent.xlsx")
sheet = wb.get_sheet_by_name("Phone")

#正确的密码
def Pwd():
    pwd = sheet["F"]
    for i in pwd:
        return i.value
print(Pwd())

#不足6位数
def ErrorNum_5():
    i = time.strftime("%M%S")
    return i

#错误验证码
def ErrorNum_6():
    i = time.strftime("%H%M%S")
    return i