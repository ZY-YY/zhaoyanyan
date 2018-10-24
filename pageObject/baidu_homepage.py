from pageObject.base import BasePage  #与项目无关的方法
from selenium.webdriver.common.by import By

#继承BasePage类
class HomePage(BasePage):
    #定位器,通过元素属性定位元素对象，find_element_by 方法属性为元组 *为元组 **也字典 都是可变长度参数
    home_page_input_search_loc=(By.ID,'kw')
    home_page_button_search_loc = (By.ID, 'su')

    #输入搜索内容，并提交
    def search(self,content):
        self.sendkeys(content,*self.home_page_input_search_loc)#元组
        self.click(*self.home_page_button_search_loc)