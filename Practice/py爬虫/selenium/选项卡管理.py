import time
from selenium import webdriver

browser = webdriver.Edge()
browser.maximize_window()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')

print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')

browser.execute_script('window.open()')
browser.switch_to.window(browser.window_handles[2])
browser.get('https://www.runoob.com/')



time.sleep(3)
browser.close()
browser.quit()
