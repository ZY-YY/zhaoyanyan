import time #导入时间方法
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver.exe")#创建一个浏览器的实例
try:
    # 操作等待时间
    driver.implicitly_wait(10)#操作等待时间10秒默认等待0.5秒，就是说执行完上面的代码等待10秒

    # 通过get方法进入百度网页
    driver.get("http://www.baidu.com")

    #激活当前窗口
    driver.switch_to.window(driver.current_window_handle)#这句话可以做省略因为只有一个窗口

    # 控制台输出信息
    print('百度首页已打开：',driver.title)

    #通过id找到文本输入框.找到的页面元素返回搜索框(就是等号前面的这个单词搜索框）百度首页只有一个搜索框
    search_input = driver.find_element_by_id('kw')#通过ID找到元素

    #找到后输入你想查询的东西如JAVA 并提交搜索
    search_input.send_keys('java')#send_keys输入本本内容就是文本输入框输入的内容
    search_input.submit()#input方法里有了内容以后就可以直接用submit方法直接提交

    #获取页面中“百度为您找到相关结果55，800，000个”相关文字的元素
    nums=driver.find_element_by_class_name('nums')#通过classname来获取对应的内容，nums是一个对象

    #在控制台打印信息
    print("-----",nums.text)#页面元素通过text属性值就可以获取他的页面内容，通过text属性就可以获取span标签中的文本内容，把nums对象的一个属性输出来
    #百度工具$为您找到相关结果约。。。
    #再次激活窗口（暂时可以不用理解，因为现在是一个敞口不需要切换）
    driver.switch_to.window(driver.current_window_handle)
    #以上代码的含义：首先打开百度页面。打开在文本款不过输入想搜的内容，检查怎么才算搜索到了，获取（百度为您找到相关结果约多少个）打印出来


    #执行脚本，显示一个框提示用户
    wait_seconds = 10  #等待的时间10
    #执行Js脚本
    driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(nums.text.replace("\n","$"),wait_seconds))#页面展示没有回车符是$符
    time.sleep(wait_seconds)#等待五秒

finally:
    driver.quit()


