from selenium import webdriver
import unittest
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        '''setUp()的代码，主要是测试前提准备工作'''
        self.driver=webdriver.Chrome("../tools/chromedriver.exe")#  ..代表根目录下的
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def tearDown(self):
        '''tearDown（）中的代码：主要是测试结束后的操作，这里基本上都是关闭浏览器'''
        self.driver.quit()

        # 所有的测试方法必须以test开头执行完测试方法彩继续执行tearDown中的内容