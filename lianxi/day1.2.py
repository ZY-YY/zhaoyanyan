from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.yahoo.com/")
assert 'Yahoo'in driver.title
elem = driver.find_element_by_name("p")
elem.send_keys("seleniumhq"+ Keys.RETURN)
driver.quit()

'''
引入模块
selenium中的webdriver
在引入webdriver中的公共common。keys模块
通过webdriver.Chrome这个方法打开一个网页
通过get方法进入某一个网页
查找‘yahoo'是不是在driver这个标题中
通过 driver.find_element_by_name这个方法通过name也就是’p‘找到这个页面元素
写文本内容在输入框中，+ 点击回车
执行回车后直接退出
'''
