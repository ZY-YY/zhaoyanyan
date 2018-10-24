from pageObject.luntan_login_pagehome import login_page  #定位提交
from selenium import webdriver
from pageObject.base import BasePage  #与项目无关的方法
from selenium.webdriver.common.by import By
import time

#删帖
class shanchutiezi_page(BasePage):
    #定位器,通过元素属性定位元素对象，find_element_by 方法属性为元组 *为元组 **也字典 都是可变长度参数
    login_page_button_morenmokuai_loc=(By.CSS_SELECTOR,".o input")#默认板块信息按钮元素
    login_page_button_shanchu_loc = (By.CSS_SELECTOR, "#mdly > p:nth-child(6) > strong:nth-child(1) > a") #删除按钮元素
    login_page_input_shanchuyuanyin_loc=(By.ID,"reason")#删除原因框架元素
    login_page_button_quedinganniu_loc = (By.ID, "modsubmit")  #确定删除按钮元素


    def chanchu(self):
        time.sleep(4)
        self.click(*self.login_page_button_morenmokuai_loc)
        print("点击小方块成功")
        time.sleep(4)
        self.click(*self.login_page_button_shanchu_loc)
        print("点击删除成功")

    def neirong(self, scyy):
        self.sendkeys(scyy, *self.login_page_input_shanchuyuanyin_loc)
        print("找到了删除原因的框架")
        time.sleep(2)
    def quedingshanchu(self):
        self.click(*self.login_page_button_quedinganniu_loc)
        time.sleep(2)
        print("确定删除")


