from selenium import webdriver
from framework.browser_engine import BrowserEngine
import unittest
import time

class BaseBrowserCase(unittest.TestCase):
    def setUp(self):
        '''测试的前提工作'''
        browser = BrowserEngine()
        self.driver=browser.open_browser()
        #一一般来说尽量保持所有浏览器共用一个driver

        #self.driver = webdriver.Chrome('../tools/chromedriver.exe')
        #self.driver.maximize_window()
        #self.driver.implicitly_wait(5)

    def tearDown(self):  #测试结束后的工作，基本上是关闭浏览器
        time.sleep(5)
        self.driver.quit()