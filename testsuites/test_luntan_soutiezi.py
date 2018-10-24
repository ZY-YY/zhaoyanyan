from testsuites.base_testsuites import BaseBrowserCase #浏览器的打开与关闭
from pageObject.luntan_login_pagehome import login_page  #定位提交
from pageObject.luntan_default import default_page
from pageObject.base import BasePage
from pageObject.luntan_huitie import huitie_page
from  pageObject.luntan_tuichu import tuichu_page
from pageObject.luntan_morenshantie import shanchutiezi_page
from pageObject.luntan_glzxjrlt import bankuaiguanli_page
from pageObject.luntan_sousuo import sousuotie_page


class soutie(BaseBrowserCase):    #浏览器
#用户登陆3.1
    def test_luntan_glogin(self):     #测试方法必须以test开头
        home_page = login_page(self.driver)  # 初始化
        # home_page.open_url('http://192.101.1.28:8088/upload/forum.php')
        home_page.login("zhaoyanyan","haotest")

#找到搜索框
        ssk=sousuotie_page(self.driver)
        ssk.soukuang("haotest")

#找到搜索按钮
        ssk=sousuotie_page(self.driver)
        ssk.ssan()
        self.driver.switch_to.window(self.driver.window_handles[1])

#进入搜索的帖子
        jinqu = sousuotie_page(self.driver)
        jinqu.cktz()
        self.driver.switch_to.window(self.driver.window_handles[2])
#验证
        yzmm=sousuotie_page(self.driver)
        yzmm.yz()

#用户退出
        tuichu_page1=tuichu_page(self.driver)
        tuichu_page1.tuichu()

