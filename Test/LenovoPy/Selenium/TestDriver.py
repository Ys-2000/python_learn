from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
import time
time.sleep(5)
driver.quit()
