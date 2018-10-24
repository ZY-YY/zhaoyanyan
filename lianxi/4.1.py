import time
from  selenium import webdriver
driver = webdriver.Chrome("../tools/chromedriver.exe")
try:
    #登陆
    driver.implicitly_wait(5)
    driver.get("http://192.101.1.28:8088/upload/forum.php")
    search_input = driver.find_element_by_id('ls_username')
    search_input.send_keys('admin')
    time.sleep(2)
    search_inputt = driver.find_element_by_id('ls_password')
    search_inputt.send_keys('haotest')
    time.sleep(2)
    search_input.submit()
    time.sleep(5)
    #发帖
    driver.get("http://192.101.1.28:8088/upload/forum.php?mod=forumdisplay&fid=2")
    time.sleep(3)
    search_input = driver.find_element_by_id('subject')
    search_input.send_keys('花花啊')
    time.sleep(2)
    search_input = driver.find_element_by_id('fastpostmessage')
    search_input.send_keys('花花149')
    time.sleep(2)
    search_input.submit()
    print("发表成功")
    time.sleep(3)
    #回帖
    search_input=driver.find_element_by_id("fastpostmessage")
    search_input.send_keys('会长高的')
    print("评论成功")
    time.sleep(2)
    search_input = driver.find_element_by_css_selector("#fastpostsubmit strong")
    print("评论提交成功")
    time.sleep(2)




finally:
    driver.quit()