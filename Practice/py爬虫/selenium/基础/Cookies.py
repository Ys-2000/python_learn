import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'xxx', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())










time.sleep(3)
browser.close()
browser.quit()
