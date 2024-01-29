import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
try:
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')     # 打开一个新选项卡
    browser.execute_script('window.open()')     # 打开一个新选项卡
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://www.chaojiying.com/')

    # browser.execute_script('window.open()')
    browser.switch_to.window(browser.window_handles[2])
    browser.get('https://www.runoob.com/')
    print(browser.window_handles)

finally:
    time.sleep(3)
    browser.close()
    browser.quit()
