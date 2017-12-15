from openpyxl import load_workbook

wb = load_workbook("dent.xlsx")
sheet = wb.get_sheet_by_name("URL")

def RegisterURL():
    """
    注册页面的URL
    :return: 返回注册页面的URL
    """
    for url in sheet["A"]:
        return url.value

def LoginUrl():
    """
    登录页面的URL
    :return: 返回登录页面的URL
    """
    for url in sheet["B"]:
        return url.value

def LoginUrlUser():
    """
    个人中心的URL
    :return: 返回个人中心的URL
    """
    # url = ["http://test.dent-lab.com/user/userinfo.html"]
    for url in sheet["D"]:
        return url.value

def Title():
    """
    核对当前页面页面是否正确，使用当前页面的标题验证
    :return:返回当前页面的标题
    """
    for title in sheet["C"]:
        return title.value
