from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
browser.get('https://www.taobao.com')
# print(browser.page_source)      #获取页面源代码
input = browser.find_element(By.ID, 'q')
input_second = browser.find_element(By.CSS_SELECTOR, '#q')
input_third = browser.find_element(By.XPATH, '//*[@id="q"]')
# print(input_first, input_second, input_third)

input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element(By.CLASS_NAME, 'btn-search')  # 找到搜索按钮
button.click()  # 点击搜索按钮
time.sleep(5)   # 等待5s
browser.close() # 关闭浏览器


