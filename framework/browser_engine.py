import os.path
from configparser import ConfigParser  #config是python中init读取的一个类，python自带并不是第三方
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath("."))#通过相对路径来获取绝对路径
    chrome_driver_path=dir+"/tools/chromedriver.exe"

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath("."))+"/config/config.ini"
        config.read(file_path)#读取出来

        browser=config.get("browserType","browserName")
        logger.info("You had selcet %s browser." %browser)
        url=config.get("testServer","URL")
        logger.info("The test server url is:%s" %url)

        '''
        if browser =="Firefox":
            #启动firefox实例)
            logger.info("staring firefox browser.")
            '''
        if browser=="Chrome":
            driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("starting Chrome browser.")
        elif browser=="IE":
            driver=webdriver.IE(self.chrome_driver_path)
            logger.info("starting IE browser.")
        driver.get(url)
        logger.info("Open url:%s"% url)
        driver.maximize_window()
        logger.info("Maximize the curren window.")
        driver.implicitly_wait(10)
        logger.info("set implicitly wait 10 seconds.")
        return driver
    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()

