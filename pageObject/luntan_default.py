from selenium import webdriver
from pageObject.base import BasePage  #与项目无关的方法
from selenium.webdriver.common.by import By
import time

class default_page(BasePage):
    #定位器,通过元素属性定位元素对象，find_element_by 方法属性为元组 *为元组 **也字典 都是可变长度参数
    login_page_button_morenmokuai_loc=(By.CSS_SELECTOR,".fl_icn a")#默认板块信息按钮元素
    login_page_input_biaoti_loc=(By.ID,"subject")#输入标题框元素
    login_page_input_neirong_loc = (By.ID, "fastpostmessage")  # 输入内容框元素
    login_page_button_fabiaotiezi_loc = (By.CSS_SELECTOR, "#fastpostsubmit > strong")  # 发表帖子按钮元素

    def default(self,biaoti,neirong):
        time.sleep(4)
        self.click(*self.login_page_button_morenmokuai_loc)
        time.sleep(2)
        self.sendkeys(biaoti,*self.login_page_input_biaoti_loc)
        time.sleep(2)
        self.sendkeys(neirong,*self.login_page_input_neirong_loc)
        time.sleep(2)
        self.click(*self.login_page_button_fabiaotiezi_loc)
        time.sleep(2)
    def morenmokuaia(self):
        time.sleep(4)
        self.click(*self.login_page_button_morenmokuai_loc)
        print("默认板块点击成功")









