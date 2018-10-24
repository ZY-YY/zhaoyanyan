from pageObject.luntan_login_pagehome import login_page  #定位提交
from selenium import webdriver
from pageObject.base import BasePage  #与项目无关的方法
from selenium.webdriver.common.by import By
import time

class sousuotie_page(BasePage):
    login_page_input_st_loc = (By.CSS_SELECTOR,".scbar_txt_td input")  # 搜贴框架元素
    login_page_button_ssniu_loc = (By.CSS_SELECTOR,".scbar_btn_td button")#搜索按钮元素
    login_page_button_jinru_loc = (By.CSS_SELECTOR, ".xs3 a")#进入帖子
    login_page_button_ttt_loc = (By.CSS_SELECTOR,"")#退出按钮
    login_page_button_zhaobiaoti_loc=(By.ID,"thread_subject")
    def soukuang(self,ssnr):
        time.sleep(5)
        self.sendkeys(ssnr,*self.login_page_input_st_loc)
        print("找到了搜贴框架")
        time.sleep(2)


    def ssan(self):#搜索按钮
        time.sleep(4)
        self.click(*self.login_page_button_ssniu_loc)
        print("点击管理中心")

    def cktz(self):  # 查看帖子按钮
        time.sleep(4)
        self.click(*self.login_page_button_jinru_loc)
        print("进入帖子")
    def yz(self):#验证
        time.sleep(3)
        yza=self.login_page_button_zhaobiaoti_loc
        assert "haotest"in self.driver.title






    def exit(self):  # 退出按钮
        time.sleep(4)
        self.click(*self.login_page_button_ttt_loc)
        print("退出登陆")
