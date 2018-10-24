from pageObject.luntan_login_pagehome import login_page  #定位提交
from selenium import webdriver
from pageObject.base import BasePage  #与项目无关的方法
from selenium.webdriver.common.by import By
import time


class Bankuaiguanli_page(BasePage):

    login_page_button_guanlizhongxin_loc = (By.CSS_SELECTOR,"# um > p:nth-child(2) > a:nth-child(16)") # 管理中心按钮元素
    login_page_input_mimakuang_loc = (By.NAME, "admin_password")  # 密码框元素
    login_page_button_tjan_loc = (By.NAME, "submit")  # 提交按钮元素
    login_page_button_lt_loc=(By.ID,"header_forum")#论坛按钮元素
    login_page_button_tjxmo_loc = (By.CSS_SELECTOR, ".addtr")  # 添加新模块按钮元素
    login_page_button_xmkqd_loc = (By.ID, "submit_editsubmit")  # 添加新模块确定按钮元素
    login_page_button_xmktc_loc = (By.ID, "submit_editsubmit")  # 新模块退出按钮元素
    #第一次退出元素没找
    login_page_button_tuichu2_loc = (By.CSS_SELECTOR,"# um > p:nth-child(2) > a:nth-child(18)")  # 退出2按钮元素
    login_page_button_xinmokuaimingcheng_loc = (By.CSS_SELECTOR, "# category_1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > h2 > a")#点击新模块名称
    login_page_input_xbkbt_loc = (By.ID,"subject")#新板块的标题框元素
    login_page_input_xbknr_loc = (By.ID, "fastpostmessage")  # 新板块的内容框元素
    login_page_button_fbtzanniu_loc = (By.ID, "fastpostsubmit")  #发表贴子按钮
    login_page_input_hfnrkz_loc = (By.ID,"fastpostmessage")#回复内容框子
    login_page_input_fbhfqr_loc = (By.NAME, "replysubmit")  # 发表回复内容确认按钮




    def glzxx(self):
        time.sleep(15)
        self.click(*self.login_page_button_guanlizhongxin_loc)
        print("点击管理中心")

    def glzxdlym(self,mimakuang):
        time.sleep(4)
        self.sendkeys(mimakuang, *self.login_page_input_mimakuang_loc)
        print("找到密码框")
    def mimatijiaoanniu(self):
        time.sleep(4)
        self.click(*self.login_page_input_tjan_loc)
        print("提交密码按钮成功")
    def luntananniua(self):
        time.sleep(4)
        self.click(*self.login_page_button_lt_loc)
        print("点击论坛按钮成功")
    def tianjiaxinmokui(self):
        time.sleep(4)
        self.click(*self.login_page_button_tjxmo_loc)
        print("添加新模块按钮元素成功")
    def xinmokuiqueding(self):
        time.sleep(4)
        self.click(*self.login_page_button_xmkqd_loc)
        print("添加新模块确定按钮元素")
    def tuichu2(self):
        time.sleep(4)
        self.click(*self.login_page_button_tuichu2_loc)
        print("退出2按钮元素")
    def xmkan2(self):
        time.sleep(4)
        self.click(*self.login_page_button_xinmokuaimingcheng_loc)
        print("新模块按钮元素点击成功")
    def xbkbtnr(self):
        time.sleep(4)
        self.sendkeys(*self.login_page_input_xbkbt_loc)
        print("新模块标题元素")

    def xbkwbnr(self):
        time.sleep(4)
        self.sendkeys(*self.login_page_input_xbknr_loc)
        print("新模块内容元素")
    def fabiaotiez(self):
        time.sleep(4)
        self.click(*self.login_page_input_fbtzanniu_loc)
        print("新模块发表按钮元素点击成功")

    def hfnrkz(self):
        time.sleep(4)
        self.sendkeys(*self.login_page_input_hfnrkz_loc)
        print("回复内容框子")
    def fbnrqr3(self):
        time.sleep(4)
        self.click(*self.login_page_input_fbhfqr_loc)
        print("新模块发表按钮元素点击成功")







