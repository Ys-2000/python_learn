from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
try:
    url = 'https://spa2.scrape.center/'
    browser.get(url)
    browser.maximize_window()       # 全屏
    # 获取属性
    logo = browser.find_element(By.CLASS_NAME, 'logo-image')
    print(logo.get_attribute('src'))    # get_attribute() 获取元素的属性值例如：src，href，

    # 获取文本值
    input = browser.find_element(By.CLASS_NAME,'logo-title')
    print(input.text)           # 获取文本值
    print(input.id)             # 获取节点ID,不是元素的实际id
    print(input.location)       # 获取位置
    print(input.tag_name)       # 获取标签
    print(input.size)           # 获取大小

finally:
    time.sleep(3)
    browser.close()     # 关闭当前的浏览器窗口，但不会关闭整个浏览器进程。如果浏览器窗口是最后一个窗口，它可能会关闭整个浏览器。
    browser.quit()      # 退出整个浏览器进程，关闭所有相关的窗口和标签页。它通常在测试脚本的最后使用，以确保释放浏览器资源