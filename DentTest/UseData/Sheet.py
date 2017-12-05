#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : G2Bent
# @Time    : 2017/12/5 13:28
# @Email   : 944921374@qq.com
# @File    : Sheet.py
# @Description:
from openpyxl import load_workbook

def Sheet(SheetName,Num):
    wb = load_workbook("dent.xlsx")
    sheet = wb.get_sheet_by_name(SheetName)
    for i in sheet[Num]:
        return i.value

def URL():
    return Sheet("URL","A")

def ErrorTip():
    return Sheet("Errortip","A")