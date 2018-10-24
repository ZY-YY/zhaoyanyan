from testsuites.base_testsuites import BaseBrowserCase #浏览器的打开与关闭
from pageObject.luntan_login_pagehome import login_page  #定位提交
from pageObject.luntan_default import default_page

from pageObject.luntan_toupiao import tp_page


#管理员登陆4.1

class LunTanglylogin(BaseBrowserCase):    #浏览器

    def test_luntan_glogin(self):     #测试方法必须以test开头
        home_page = login_page(self.driver)  # 初始化
        # home_page.open_url('http://192.168.43.176:8088/upload/forum.php')

        home_page.login("admin","haotest")
#进入默认模块:
        home_mrmk6=default_page(self.driver)
        home_mrmk6.morenmokuaia()
#点击发帖
        home_fatieanniu = tp_page(self.driver)
        home_fatieanniu.tpan()
#发起投票
        home_faqitoupiaoanniu = tp_page(self.driver)
        home_faqitoupiaoanniu.faqitoupiaoa()
#投票标题
        home_tpbt3 = tp_page(self.driver)
        home_tpbt3.tpbtkk("谁最瘦")
#第123框
        home_dyk = tp_page(self.driver)
        home_dyk.yi("花")

        home_derk = tp_page(self.driver)
        home_derk.er("嘘嘘")

        home_dsank = tp_page(self.driver)
        home_dsank.san("莉莉")
#点击发起
        home_faqila = tp_page(self.driver)
        home_faqila.djfq()
#选择投票对象
        home_tpdx = tp_page(self.driver)
        home_tpdx.xuanze()
#新模块发表按钮元素点击成功
        home_dian = tp_page(self.driver)
        home_dian.tijiao()

#取出主题输出
        home_quchuzhuti= tp_page(self.driver)
        home_quchuzhuti.shuchusuoyou()

