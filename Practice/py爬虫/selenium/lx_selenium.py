import time
from selenium import webdriver

# 打开百度
driver = webdriver.Edge()
url = 'https://www.baidu.com/'
driver.get(url)
driver.maximize_window()        # 将当前的浏览器窗口最大化

time.sleep(3)       # 等待3s

driver.close()      # 关闭当前活动窗口
driver.quit()       # 关闭所有窗口并退出浏览器