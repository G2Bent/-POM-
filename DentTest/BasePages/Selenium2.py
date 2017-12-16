#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : G2Bent
# @Time    : 2017/12/15 17:15
# @Email   : 944921374@qq.com
# @File    : Selenium2.py
# @Description:
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import * #导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def browser(browser="Chrome"):
    """打开浏览器函数，Firefox，chrome，IE，phantomjs"""
    try:
        if browser == "Chrome":
            driver = webdriver.Chrome()
            return driver
        elif browser == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif browser == "IE":
            driver = webdriver.Ie()
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("找不到驱动")
    except Exception as msg:
        print("%s" % msg)

class Sele(object):

    """基于原生selenium框架做了二次封装
    启动浏览器参数化，默认启动Chrome"""
    def __init__(self,driver,base_url,pagetitle):
        self.base_url = base_url
        self.pagetitle = pagetitle
        self.driver = driver

    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    #打开页面，校验页面是否加载正确
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
    def _open(self,url,pagetitle):
        #使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window()
        #使用assert进行校验，打开的链接地址是否与配置的地址一致。调用on_page()方法
        assert self.on_page(pagetitle),"打开页面失败%s"%url

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url, self.pagetitle)
        self.driver.maximize_window()

    #重写元素定位方法
    def find_element(self,*loc):
        #return self.driver.find_element(*loc)
        try:
            #确保元素是可见的
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver,5).until(EC.visibility_of_all_elements_located(loc))
            return  self.driver.find_element(*loc)
        except:
            print("页面元素未能找到%s"%self,loc)

    #重写元素定位方法
    def find_elements(self,*loc):
        #return self.driver.find_element(*loc)
        try:
            #确保元素是可见的
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver,5).until(EC.visibility_of_all_elements_located(loc))
            return  self.driver.find_elements(*loc)
        except:
            print("页面元素未能找到%s"%self,loc)

    def click(self,localtor):
        """点击操作"""
        element = self.find_element(localtor)
        element.click()
    def send_keys(self,localtor,text):
        """发送文本"""
        element = self.find_element(localtor)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self,localtor,text,timeout=10):
        """判断文本在元素里，没定位到元素返回False，定位到元素返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(localtor,text))
        except TimeoutException:
            print("元素没有定位到:"+str(localtor))
            return False
        else:
            return result

    def is_text_in_value(self,locator,value,timeout = 10):
        '''
              判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
              result = driver.text_in_element(locator, text)
              '''
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        '''判断title完全等于'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        '''判断title包含'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        '''判断元素被选中，返回布尔值,'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        '''判断元素的状态，selected是期望的参数true/False
        返回布尔值'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self, timeout=10):
        '''判断页面是否有alert，
        有返回alert(注意这里是返回alert,不是True)
        没有返回False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator, timeout=10):
        '''元素可见返回本身，不可见返回Fasle'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(locator))
        return result

    def is_invisibility(self, locator, timeout=10):
        '''元素可见返回本身，不可见返回True，没找到元素也返回True'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.invisibility_of_element_located(locator))
        return result

    def is_clickable(self, locator, timeout=10):
        '''元素可以点击is_enabled返回本身，不可点击返回Fasle'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        '''判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return result

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        Usage:
        locator = ("id","xxx")
        driver.move_to_element(locator)
        '''
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        """
        Back to old window.
        Usage:
        driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        Forward to old window.
        Usage:
        driver.forward()
        """
        self.driver.forward()

    def close(self):
        """
        Close the windows.
        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.
        Usage:
        driver.quit()
        """
        self.driver.quit()

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self, locator):
        '''获取文本'''
        element = self.find_element(locator)
        return element.text

    def get_attribute(self, locator, name):
        '''获取属性'''
        element = self.find_element(locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        '''执行js'''
        return self.driver.execute_script(js)

    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, locator, index):
        '''通过索引,index是索引第几个，从0开始'''
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element = self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.find_element(locator)
        Select(element).select_by_value(text)

if __name__ == '__main__':
    # if下面的代码都是测试调试的代码，自测内容
    driver = browser()
    driver_n = Sele(driver)  # 返回类的实例：打开浏览器
    driver_n.open("http://www.cnblogs.com/G2Bent/")  # 打开url，顺便判断打开的页面对不对
    driver_n.js_scroll_top()
    input_loc = ("id", "kw")
    print (driver_n.get_title())
    driver.quit()
