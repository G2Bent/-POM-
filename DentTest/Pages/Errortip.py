#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : G2Bent
# @Time    : 2017/12/2 10:21
# @Email   : 944921374@qq.com
# @File    : Errortip.py
# @Description:
import unittest
from openpyxl import load_workbook
from openpyxl import Workbook

def error():
    """
    错误提示的数据，这里使用xlsx保存
    :return:遍历所有的错误数据
    """
    wb = load_workbook("dent.xlsx")
    sheet = wb.get_sheet_by_name("Errortip")
    for i in sheet['A']:
        return i.value


