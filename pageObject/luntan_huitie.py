from selenium import webdriver
from pageObject.base import BasePage  #与项目无关的方法
from selenium.webdriver.common.by import By
import time

class huitie_page(BasePage):
    ht_page_input_huifuneirong_loc = (By.ID, "fastpostmessage")  # 输入回复框元素
    ht_page_button_fabiaohuifu_loc=(By.XPATH,'//*[@id="fastpostsubmit"]/strong')# 发表回复按钮元素

    def huitie(self,huifuneirong):
        self.sendkeys(huifuneirong,*self.ht_page_input_huifuneirong_loc )
        time.sleep(2)
        self.click(*self.ht_page_button_fabiaohuifu_loc)
        time.sleep(2)
        print("回复成功")
