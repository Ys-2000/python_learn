import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()

browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()      # 后退
time.sleep(1)
browser.forward()   # 前进














time.sleep(3)
browser.close()
browser.quit()