from Pages.LoginPage import *
class Login_Tips(LoginPage):
    loc_result_link = (By.XPATH,'//*[@class="user-title"]')#个人中心 文案校验
    @property
    def result_links(self):
        return self.find_element(*self.loc_result_link)