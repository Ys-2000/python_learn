# https://cuiqingcai.com/202261.html

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Edge()
browser.maximize_window()

# # 隐式等待
# browser.implicitly_wait(10)     # implicitly_wait 方法实现了隐式等待
# browser.get('https://spa2.scrape.center/')
# input = browser.find_element(By.CLASS_NAME, ('logo-image'))
# print(input)


# 显式等待
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)








time.sleep(3)
browser.close()
browser.quit()
