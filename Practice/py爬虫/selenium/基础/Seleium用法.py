from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     # 处理键盘操作
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time

browser = webdriver.Chrome()
browser.maximize_window()
try:
    browser.get('https://www.baidu.com')
    input_first = browser.find_element(By.NAME, 'wd')
    input_first.send_keys("iPhone")
    time.sleep(1)
    input_first.clear()
    input_first.send_keys("iPad")
    # button = browser.find_element(By.NAME, 'btn-search').click()
    input_first.send_keys(Keys.ENTER)     # 按下回车

    # lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')    # find_elements获取多个节点

    wait = WebDriverWait(browser, 10)       # 显式等待10秒
    wait.until(EC.presence_of_element_located((By.ID, 'container')))
    print(browser.current_url,"\n")
    print(browser.get_cookies(),"\n")
    # print(browser.page_source)

except NoSuchElementException:
    print("元素未找到")
finally:    # 无论是否发生异常，都会执行这个代码块
    time.sleep(3)
    browser.close()