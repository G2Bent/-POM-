from selenium import webdriver
import time,os,json

class cookie:
    driver = webdriver.Chrome()
    driver.get("http://test.dent-lab.com/login.html")
    # cookies = driver.get_cookies()
    # print(cookies)
    # for i in cookies:
    #     print(i)
    driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys("15816038158")
    driver.find_element_by_xpath('//*[@id="pwd_login"]').send_keys("a123456")
    driver.find_element_by_xpath('//*[@id="btn_login"]').click()

    cookies = driver.get_cookies()

    with open(os.getcwd()+'\cookies.json','w') as f:
        cookies = json.dumps(cookies)
        f.write(cookies)

    # with open(os.getcwd()+'\cookies.json','r') as f:
    #     cookies = f.read()
    #     cookies = json.loads(cookies)
    #     print(cookies)
    #     print(type(cookies))
    #
    # driver = webdriver.Chrome()
    # driver.get("http://test.dent-lab.com/login.html")
    # driver.delete_all_cookies()
    # for cookie in cookies:
    #     driver.add_cookie(cookie)
    # driver.refresh()