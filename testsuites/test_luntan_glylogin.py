from testsuites.base_testsuites import BaseBrowserCase #浏览器的打开与关闭
from pageObject.luntan_login_pagehome import login_page  #定位提交
from pageObject.luntan_default import default_page
from pageObject.luntan_morenshantie import shanchutiezi_page
from pageObject.luntan_glzxjrlt import Bankuaiguanli_page


#管理员登陆2.1

class LunTanglylogin(BaseBrowserCase):    #浏览器

    def test_luntan_glogin(self):     #测试方法必须以test开头
        home_page = login_page(self.driver)  # 初始化
        # home_page.open_url('http://192.101.1.28:8088/upload/forum.php')
        home_page.login("admin","haotest")
#进入默认模块:
        home_page6=default_page(self.driver)
        home_page6.morenmokuaia()
#删除帖子：
        sctzl = shanchutiezi_page(self.driver)
        sctzl.chanchu()
        sctz2=shanchutiezi_page(self.driver)
        sctz2.neirong("写得不好")
        sctzl = shanchutiezi_page(self.driver)
        sctzl.quedingshanchu()

#进入版块管理(管理中心--论坛)
        bkgl3 = Bankuaiguanli_page(self)
        bkgl3.glzxx()#点击管理中心了
        # self.driver.switch_to.window(self.driver.window_handles[1])

#         mmk = bankuaiguanli_page(self)
#         mmk.glzxdlym("haotest")#找到密码框
#
#         tjmm1 = bankuaiguanli_page(self)
#         tjmm1.mimatijiaoanniu()#点击提交密码
#
#         ltan1 = bankuaiguanli_page(self)
#         ltan1.luntananniua()  # 点击论坛按纽
#
# #创建新板块
#         cjxbk1 = bankuaiguanli_page(self)
#         cjxbk1.tianjiaxinmokui()  # 点击新板块
#
#         xbkqr1 = bankuaiguanli_page(self)
#         xbkqr1.xinmokuiqueding()  # 点击新板块确认按钮
# #管理员退出
#         self.driver.switch_to.default_content()  # 跳出iframe模块
#         #第一次退出管理中心没退
#
#         tcdl3 = bankuaiguanli_page(self)
#         tcdl3.tuichu2()  # 退出2
#
# #普通用户登陆
#         ptyhdl2 = login_page(self)
#         ptyhdl2.login()
# #新板块发帖
#         xbkft1 = bankuaiguanli_page(self)#点击新模块按钮
#         xbkft1.xmkan2()
# # 新板块标题框
#         xbkbt2 = bankuaiguanli_page(self)
#         xbkft1.xbkbtnr("狗男女")
# # 新板块内容框
#         xbknrk = bankuaiguanli_page(self)
#         xbknrk.xbkwbnr("猫男女。。。。。。。。。。。")
# #新模块内容发表按钮
#         xmknrfban = bankuaiguanli_page(self)
#         xmknrfban.fabiaotiez()
# #回复内容文本框子
#         hfnrwbk = bankuaiguanli_page(self)
#         hfnrwbk.hfnrkz("猫男女。。。。。。。。。。。狗那女猪男女")
# #回复确认按钮
#         hfqr1 = bankuaiguanli_page(self)
#         hfqr1.fbnrqr3()

















