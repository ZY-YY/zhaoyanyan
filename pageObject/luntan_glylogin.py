from selenium import webdriver
from pageObject.base import BasePage  #与项目无关的方法
from selenium.webdriver.common.by import By
import time

class glylogin_page(BasePage):
    #定位器,通过元素属性定位元素对象，find_element_by 方法属性为元组 *为元组 **也字典 都是可变长度参数
    glylogin_page_input_glyusername_loc=(By.ID,"")#管理员用户名元素
    glylogin_page_input_glypassword_loc=(By.ID,"")#密码元素
    glylogin_page_button_loc=(By.CSS_SELECTOR,"")#点击登陆按钮元素

    def glylogin(self,gusername,gpassword):
        self.sendkeys(gusername,*self.glylogin_page_input_glyusername_loc)
        self.sendkeys(gpassword,*self.glylogin_page_input_glypassword_loc)
        time.sleep(2)
        self.click(*self.glylogin_page_button_loc)