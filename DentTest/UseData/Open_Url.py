from openpyxl import load_workbook

wb = load_workbook("dent.xlsx")
sheet = wb.get_sheet_by_name("URL")

def RegisterURL():
    for url in sheet["A"]:
        return url.value

def LoginUrl():
    for url in sheet["B"]:
        return url.value

def LoginUrlUser():
    url = ["http://test.dent-lab.com/user/userinfo.html"]
    return url

def Title():
    for title in sheet["C"]:
        return title.value
