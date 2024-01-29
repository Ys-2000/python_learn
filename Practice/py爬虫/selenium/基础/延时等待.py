# https://cuiqingcai.com/202261.html

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window()

# # 隐式等待
# # 如果 Selenium 没有在 DOM 中找到节点，将继续等待，超出设定时间后，则抛出找不到节点的异常。换句话说，当查找节点而节点并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是 0。
# browser.implicitly_wait(10)     # implicitly_wait 方法实现了隐式等待
# browser.get('https://spa2.scrape.center/')
# input = browser.find_element(By.CLASS_NAME, ('logo-image'))
# print(input)


# 显式等待
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)   # 指定最长等待时间

# until方法 传入等条件 # presence_of_element_located 这个条件，代表节点出现的意思，其参数是节点的定位元组，也就是 ID 为 q 的节点搜索框。
# 这样可以做到的效果就是，在 10 秒内如果 ID 为 q 的节点（即搜索框）成功加载出来，就返回该节点；如果超过 10 秒还没有加载出来，就抛出异常。
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))


# until方法 传入等条件 # element_to_be_clickable 这个条件，
# 查找按钮时查找 CSS 选择器为 .btn-search 的按钮，如果 10 秒内它是可点击的，也就是成功加载出来了，就返回这个按钮节点；如果超过 10 秒还不可点击，也就是没有加载出来，就抛出异常。
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)








time.sleep(3)
browser.close()
browser.quit()
