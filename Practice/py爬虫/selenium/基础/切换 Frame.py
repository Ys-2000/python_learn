import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.maximize_window()
time.sleep(3)       # 有个弹窗 手动点一下
browser.switch_to.frame('iframeResult')     # 切换到子 Frame 里面
try:
    logo = browser.find_element(By.NAME, 'logo')
except NoSuchElementException:
    print('NO LOGO')

browser.switch_to.parent_frame()    # 切换回父级iframe

logo = browser.find_element(By.NAME,'logo')
print(logo)
print(logo.text)

time.sleep(3)
browser.close()
browser.quit()