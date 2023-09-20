from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.maximize_window()        # 将当前的浏览器窗口最大化
browser.switch_to.frame('iframeResult')     # 切换到名为'iframeResult'的iframe内部，以便查找和操作iframe内的元素。
source = browser.find_element(By.CSS_SELECTOR, '#draggable')    # 要拖拽的源元素
target = browser.find_element(By.CSS_SELECTOR,'#droppable')     # 要拖拽到的目标元素
actions = ActionChains(browser)     # 创建了一个ActionChains对象，用于执行各种用户交互操作
actions.drag_and_drop(source, target)   # 使用drag_and_drop方法指定要拖拽的源元素source和目标元素target
actions.perform()    # 执行ActionChains中的所有操作，即执行拖拽操作
time.sleep(5)   # 等待5s
browser.close()