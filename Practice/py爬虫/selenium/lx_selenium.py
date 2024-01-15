import time,random
from selenium import webdriver

# 打开百度
# driver = webdriver.Edge()
driver = webdriver.Chrome()
# url = 'https://www.baidu.com/'
url = 'https://www.zhipin.com/web/geek/job?query=&city=101120100&position=100101'
driver.get(url)
driver.maximize_window()        # 将当前的浏览器窗口最大化

time.sleep(random.uniform(0, 3))       # 等待3s
print(driver.page_source)
driver.close()      # 关闭当前活动窗口
driver.quit()       # 关闭所有窗口并退出浏览器