import time
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver.exe")
windows = driver.window_handles
try:
    #用户登陆
    driver.implicitly_wait(5)
    driver.get("http://192.101.1.28:8088/upload/forum.php")
    list_window = driver.current_window_handle
    driver.switch_to_window(list_window)  # 激活窗口
    username = driver.find_element_by_id('ls_username')
    username.send_keys('admin')
    time.sleep(2)
    password = driver.find_element_by_id('ls_password')
    password.send_keys('haotest')
    time.sleep(2)
    password.submit()
    time.sleep(4)
    print("管理员登陆成功")




    #进行帖子搜索
    

finally:
    driver.quit()
