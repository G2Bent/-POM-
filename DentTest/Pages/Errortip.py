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
    wb = load_workbook("dent.xlsx")
    sheet = wb.get_sheet_by_name("Errortip")
    for i in sheet['A']:
        return i.value
    # tt =['邮箱不能为空','邮箱格式不正确','该邮箱已注册','验证码不能为空','验证码应为六位纯数字'
    #      ,'邮箱或验证码不能为空','验证码错误','手机号格式不正确','该手机号已注册',
    #      '手机号或验证码不能为空', '旧密码不能为空','新密码不能为空','密码由6-16字母(区分大小写)、数字组成',
    #      '确认密码不能为空','新密码和确认密码不一致', '确认新密码不能为空','旧密码不正确'
    #      ,'姓名由2-16位汉字、字母、数字组成','手机号不能为空','详细地址不能为空','姓名不能为空',
    #      '姓名或手机号格式不正确','手机号/邮箱不能为空','手机号/邮箱格式不正确',
    #      '该手机号未注册，无法用于密码找回','该邮箱未注册，无法用于密码找回','两次输入的密码不一致'
    #     ,'找回密码失败，请稍后再试','用户名或密码不能为空','用户名或密码错误'
    #     ,'获取验证码失败，请稍后再试','注册失败，请稍后再试','姓名不能为空']
    # for i in tt:
        # print(i.value,end="\n")
# print(error())


