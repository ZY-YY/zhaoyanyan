
'''
#爬到拉勾网招聘信息
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver.exe")
try:
    driver.implicitly_wait(5)
    driver.get("http://www.lagou.com/zhaopin/Java/?labelWords=label")
    window_list=driver.current_window_handle
    driver.switch_to.window(window_list)
    job_link=driver.find_element_by_css_selector(
        '.item_con_list li:first-child .p_top a span'
    )
    job_link.click()
    driver.switch_to.window(driver.window_handles[1])
    job_company=driver.find_element_by_css_selector('.company')
    job_name=driver.find_element_by_css_selector('.name')
    job_money=driver.find_element_by_css_selector('.salary')
    job_year=driver.find_element_by_css_selector(''
                                                 )
    print("公司：",job_company.text,
          "职位名称：",job_name.text,
          "薪资范围：",job_money.text,
          )
    driver.close()
    driver.switch_to.window(window_list)



finally:
    time.sleep(5)
    driver.quit()
'''



from selenium import webdriver
driver = webdriver.Chrome("./chromedriver.exe")
try:
    driver.implicitly_wait(5)#隐式等待
    driver.get("https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=")


finally:
    driver.quit()