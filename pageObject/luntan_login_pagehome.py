from selenium import webdriver
from pageObject.base import BasePage  #与项目无关的方法
from selenium.webdriver.common.by import By
import time


class login_page(BasePage):
    #定位器,通过元素属性定位元素对象，find_element_by 方法属性为元组 *为元组 **也字典 都是可变长度参数
    login_page_input_username_loc=(By.ID,"ls_username")#用户名元素
    login_page_input_password_loc=(By.ID,"ls_password")#密码元素
    login_page_button_loc=(By.CSS_SELECTOR,".pn em")#点击登陆按钮元素



    def login(self,username,password):
        self.sendkeys(username,*self.login_page_input_username_loc)
        self.sendkeys(password,*self.login_page_input_password_loc)
        time.sleep(2)
        self.click(*self.login_page_button_loc)