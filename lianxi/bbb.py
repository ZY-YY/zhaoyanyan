from  selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from lianxi.aaa import BaseTestCase
import time

class Baidusearch(BaseTestCase):
    def test_baidu_search(self):
        '''测试方法必须要已TEST开头'''
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium"+Keys.RETURN)
        time.sleep(2)
        assert "selenium"in self.driver.title
driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.implicitly_wait(5)