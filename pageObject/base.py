from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os.path
import time
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger

logger = Logger(logger="Basepage").getlog()#当前调用这个logger对象的是logger="Basepage"  实例化方法，自动调用

class BasePage(object):
    '''
      #所有页面的基类，封装了页面的公共方法,与业务无关
       bank()
       forword()
       get()
       quit()
       '''
    def print(self,*loc):
        #(输出方法）
        elem=self.find_element(*loc)
        logger.info("最后一步get the message %s ." % elem.text)

    def __init__(self,driver):
        '''写一个构造方法'''
        self.driver=driver

    def back(self):
        '''浏览器后退按钮'''
        self.driver.back()
        logger.info("Click back on current page.") #引号额你中英文都可以

    def forward(self):
        '''浏览器前进按钮'''
        self.driver.forward()

    def open_url(self,url):
        self.driver.get(url)#打开url站点

    def quit_browser(self):
        '''退出关闭浏览器'''
        self.driver.quit()

    def find_element(self,*loc):  # *代表元组 ** 代表字典
        '''定位'''
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素---",loc)

        except:
            logger.error(" 页面中未能找到 %s 元素" % (self ,loc))

    # 截屏保存图片
    def get_windows_img(self):
        '''截屏'''
        # 将file_path写死，直接保存到screenshot下
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder:/screenshots")
            # 如果执行成功就会添加快照并且保存到了:/screenshots下
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s"% e)
            # 如果出现error就没提示i没有成功的截图，同时把e日志信息打印出来

    '''输入 '''
    def sendkeys(self, text, *loc):
        el = self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
        except Exception as e:
            self.get_windows_img()

    def clear(self, *loc):
        '''清空文本框'''
        el = self.find_element(*loc)
        try:
            el.clear()
        except Exception as e:
            self.get_windows_img()



    '''点击元素'''
    def click(self, *loc):
        el = self.find_element(*loc)
        try:
            el.click()
            print('The element %s was click.' % el.text)
        except Exception as e:
            print('Failed to click the element with %s' % e)

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")  #正常是调用这个
        except Exception as e:
            logger.error("Failed to quit the browser with %s."% e)#出错就调用这个
            u""" 长按 """



