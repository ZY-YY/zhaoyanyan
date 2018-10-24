from selenium import webdriver
from pageObject.base import BasePage  #与项目无关的方法
from selenium.webdriver.common.by import By
import time

class tuichu_page(BasePage):
    tc_page_button_tuichuanniu_loc = (By.XPATH,'//*[@id="um"]/p[1]/a[5]')  # 退出按钮元素

    def tuichu(self):
        time.sleep(3)
        self.click(*self.tc_page_button_tuichuanniu_loc)
        time.sleep(3)
        print("退了")
        time.sleep(3)