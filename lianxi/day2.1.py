'''
#找网页中的a标签
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com")
elements = driver.find_elements_by_tag_name("a")
print('共找到a标签%d个'%len(elements))
for ele in elements:
    print(ele.text)
driver.quit()
'''





'''
#在百度页面文本框中搜索想搜所的内容 如:视频
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("http://www.baidu.com")
print("百度首页已经打开",driver.title)
elem = driver.find_element_by_link_text('视频')
elem.send_keys(Keys.RETURN)
driver.quit()
'''




'''
#在hao123页面搜所想抖索的内容，如：八卦
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("http://www.hao123.com")
print("百度首页已经打开",driver.title)
elem = driver.find_element_by_partial_link_text('八卦')
elem.send_keys(Keys.RETURN)
'''





'''
#获取所有邮箱正则方法
from selenium import webdriver
import re
driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://home.baidu.com/contact.html")
#得到页面源代码
doc = driver.page_source
emails = re.findall(r'[\w]+@[\w\.-]+',doc)  #利用正则，找出xxx@xxx.xxx的字段，保存到emails列表
#循环打印匹配的邮箱
for email in emails:
    print(email)
'''



