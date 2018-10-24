from testsuites.base_testsuites import BaseBrowserCase #浏览器的打开与关闭
from pageObject.baidu_homepage import HomePage  #定位提交
import time
import unittest

class BaiduSearch(BaseBrowserCase):#浏览器
    def test_baidu_search(self): #测试方法必须以test开头
        Home_Browser = HomePage(self.driver)#初始化
        Home_Browser.open_url('http://www.baidu.com')
        Home_Browser.search('java')

        time.sleep(2)

#继承BasePage类
# class HomePage(BasePage):
#     #定位器,通过元素属性定位元素对象，find_element_by 方法属性为元组 *为元组 **也字典 都是可变长度参数
#     home_page_input_search_loc=(By.ID,'kw')
#     home_page_button_search_loc = (By.ID, 'su')
#
#     #输入搜索内容，并提交
#     def search(self,content):
#         self.sendkeys(content,*self.home_page_input_search_loc)#元组
#         self.click(*self.home_page_button_search_loc)
if __name__ == '__main__':
    unittest.main()