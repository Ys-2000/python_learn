from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

browser = webdriver.Edge()
browser.maximize_window()

try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print("Time Out")
try:
    browser.find_element(By.ID, 'wd')
except NoSuchElementException:
    print("NO Element")
finally:
    time.sleep(3)
    browser.close()
    browser.quit()



