from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

browser = webdriver.Edge()
browser.maximize_window()

try:
    browser.get('https://www.baidu.com')
    browser.get('https://www.google.com/')
except TimeoutException:            # 超时异常
    print("Time Out")
try:
    browser.find_element(By.ID, 'w2d')
except NoSuchElementException:      # 元素未找到
    print("NO Element")
finally:
    time.sleep(3)
    browser.close()
    browser.quit()



