from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
url = 'https://spa2.scrape.center/'
browser.get(url)
browser.maximize_window()       # 全屏
# 获取属性
logo = browser.find_element(By.CLASS_NAME, 'logo-image')
print(logo)
print(logo.get_attribute('src'))

# 获取文本值
input = browser.find_element(By.CLASS_NAME,'logo-title')
print(input.text)           # 获取文本值
print(input.id)             # 获取ID
print(input.location)       # 获取位置
print(input.tag_name)       # 获取标签
print(input.size)           # 获取大小






time.sleep(3)
browser.close()
browser.quit()