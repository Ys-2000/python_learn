from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Edge()
try:
    browser.get('https://www.baidu.com')
    # input = browser.find_element_by_id('kw')
    input = browser.find_element(By.ID,'kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)       # 等待直到特定条件满足或超时为止
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))     #等待页面加载完毕并且具有ID为'content_left'的元素出现，然后继续执行后续的操作
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
