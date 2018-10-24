#getfangfa
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #导入keys类
import unittest#首先导入unittest
import time
class Baidusrarch(unittest.TestCase):  #每一个测试用例都必须继承自unittest丽提供的测试基类TestCase,括号里的动力表明继承了它
    def setUp(self):    #self代表当前
        '''setUp()的代码，主要是测试前提准备工作'''
        self.driver=webdriver.Chrome("../tools/chromedriver.exe")#   .代表当前目录  ..代表上级剥
        self.driver.implicitly_wait(5)#隐视等待
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        '''tearDown（）中的代码：主要是测试结束后的操作，这里基本上都是关闭浏览器'''
        time.sleep(3)
        self.driver.quit()

    def test_baidu_search(self):
        #所有的测试方法都必须要以test开头，test打头的才是测试方法
        self.driver.find_element_by_id("kw").send_keys("java"+Keys.RETURN)
        #找到kw这个元素框子输入java 回车键.RETURN跟enter是一个道理
        time.sleep(2)
        assert "java" in self.driver.title #结果展示
