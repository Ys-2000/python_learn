import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()
try:
    browser.get('https://www.baidu.com/')
    browser.get('https://www.taobao.com/')
    browser.get('https://www.python.org/')
    time.sleep(1)
    browser.back()      # 后退
    time.sleep(1)
    browser.forward()   # 前进

finally:
    time.sleep(3)
    browser.close()
    browser.quit()