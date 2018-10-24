
from testsuites.base_testsuites import BaseBrowserCase #浏览器的打开与关闭
from pageObject.luntan_login_pagehome import login_page  #定位提交
from pageObject.luntan_default import default_page
from pageObject.luntan_huitie import huitie_page
from  pageObject.luntan_tuichu import tuichu_page
#登陆1.1
class Luntanlogin(BaseBrowserCase):    #浏览器

    def test_luntan_login(self):     #测试方法必须以test开头
        home_page = login_page(self.driver)  # 初始化
        # home_page.open_url('http://192.101.1.28:8088/upload/forum.php')
        home_page.login("zhaoyanyan","haotest")
#发帖1.2
        default_page1=default_page(self.driver)
        default_page1.default("你是谁","不告诉你00000000000")

#回帖1.3
        huitie_page1=huitie_page(self.driver)
        huitie_page1.huitie("成功了这次0000000000000")


#退出
        tuichu_page1=tuichu_page(self.driver)
        tuichu_page1.tuichu()





