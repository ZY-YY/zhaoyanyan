from pageObject.luntan_login_pagehome import login_page  #定位提交
from selenium import webdriver
from pageObject.base import BasePage  #与项目无关的方法
from selenium.webdriver.common.by import By
import time


class tp_page(BasePage):

    login_page_button_mrbk3_loc = (By.CSS_SELECTOR,"#category_1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > h2 > a")#点击新板块
    login_page_button_ftan_loc = (By.ID,"newspecialtmp")  # 发帖按钮元素
    login_page_button_dtp_loc = (By.CSS_SELECTOR, "#editorbox > ul > li:nth-child(2) > a")  # 发起投票按钮元素
    login_page_input_tpk_loc = (By.CSS_SELECTOR,"#subject")#投票标题框
    login_page_input_diyige_loc = (By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(1) > input")#第1个框框
    login_page_input_dierge_loc = (By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(2) > input")  # 第2个框框
    login_page_input_disange_loc = (By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(3) > input")  # 第3个框框
    login_page_button_xz_loc = (By.ID,"option_1")#选择
    login_page_button_tj_loc = (By.ID, "pollsubmit")#提交
    login_page_button_fqtp_loc = (By.CSS_SELECTOR,".bw0 li:nth-child(2) a")  # 点击发起投票
    login_page_button_momorenren_loc = (By.CSS_SELECTOR,"# category_1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > h2 > a")
    login_page_button_fqtpzuihou_loc = (By.CSS_SELECTOR,".mtm .pnc")  # 点击发起投票zuihou
    login_page_button_huaming_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(1) td:nth-child(2)")  # 花名字
    login_page_button_xuming_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(3) td:nth-child(2)")  # xu名字
    login_page_button_liming_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(5) td:nth-child(2)")  # li名字
    login_page_button_hua_loc = (By.CSS_SELECTOR,".pcht tbody tr:nth-child(4) td:nth-child(2)")#花的百分比
    login_page_button_xuxu_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(4) td:nth-child(2)")  # xu的百分比
    login_page_button_lili_loc = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(6) td:nth-child(2)")  # lili的百分比
    login_page_button_biaotizhutimingcheng_loc = (By.CSS_SELECTOR,".ts span")  # 标题主题名称

    def xbk(self):
        time.sleep(4)
        self.click(*self.login_page_button_momorenren_loc)
        print("点默认板块")

    def tpan(self):
        time.sleep(4)
        self.click(*self.login_page_button_ftan_loc)
        print("点发帖")

    def toup(self):
        time.sleep(4)
        self.click(*self.login_page_button_dtp_loc)
        print("点投票")
    def faqitoupiaoa(self):
        time.sleep(4)
        self.click(*self.login_page_button_fqtp_loc)
        print("发起投票")

    def tpbtkk(self,btk):
        time.sleep(4)
        self.sendkeys(btk,*self.login_page_input_tpk_loc)
        print("投票标题框")
    def yi(self,yige):
        time.sleep(4)
        self.sendkeys(yige,*self.login_page_input_diyige_loc)
        print("第一个框")

    def er(self,erge):
        time.sleep(4)
        self.sendkeys(erge,*self.login_page_input_dierge_loc)
        print("第2个框")

    def san(self,sange):
        time.sleep(4)
        self.sendkeys(sange,*self.login_page_input_disange_loc)
        print("第3个框")
    def djfq(self):
        time.sleep(4)
        self.click(*self.login_page_button_fqtpzuihou_loc)
        print("点集发起投票")
    def xuanze(self):
        time.sleep(4)
        self.click(*self.login_page_button_xz_loc)
        print("选择投票对象")
    def tijiao(self):
        time.sleep(4)
        self.click(*self.login_page_button_tj_loc)
        print("点击提交")

    # def huahuaming(self):
    #     time.sleep(4)
    #     self.click(*self.login_page_button_huaming_loc)
    #     print("花花名")
    # def shuhua(self):
    #     time.sleep(3)
    #
    # def huabeifenbi(self):
    #     time.sleep(4)
    #     self.click(*self.login_page_button_hua_loc)
    #     print("花花的百分比")
    #
    # def xuxuming(self):
    #     time.sleep(4)
    #     self.click(*self.login_page_button_xuming_loc)
    #     print("嘘嘘名")
    # def xubeifenbi(self):
    #     time.sleep(4)
    #     self.click(*self.login_page_button_xuxu_loc)
    #     print("嘘嘘的百分比")
    #
    # def liliming(self):
    #     time.sleep(4)
    #     self.click(*self.login_page_button_liming_loc)
    #     print("莉名")
    # def libeifenbi(self):
    #     time.sleep(4)
    #     self.click(*self.login_page_button_lili_loc)
    #     print("莉的百分比")
    #
    #
    # def toupiaomiangzi(self):
    #     time.sleep(4)
    #     self.click(*self.login_page_button_biaotizhutimingcheng_loc)
    #     print("投票主题")

    def shuchusuoyou(self):#取出投票的各个名称以及比例
        time.sleep(4)
        self.print(*self.login_page_button_huaming_loc)
        self.print(*self.login_page_button_hua_loc)

        self.print(*self.login_page_button_xuming_loc)
        self.print(*self.login_page_button_xuxu_loc)

        self.print(*self.login_page_button_liming_loc)
        self.print(*self.login_page_button_lili_loc)

        self.print(*self.login_page_button_biaotizhutimingcheng_loc)








