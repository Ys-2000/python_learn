import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://captcha7.scrape.center/"

#  抓不到验证码图片请求！！！

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element(By.XPATH, "//div[@class='el-tooltip username item el-input']/input").send_keys("admin")
driver.find_element(By.XPATH, "//div[@class='el-tooltip password item el-input']/input").send_keys("admin")
time.sleep(7)
# driver.find_element(By.XPATH, "//div[@class='captcha el-input']/input").send_keys("admin")    # 验证码
driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div/form/div[4]/div/button").click()

# page_source = driver.page_source
# print(page_source)


time.sleep(7)
driver.close()
# try:
#     # 设置最大等待时间为10秒，检查页面是否包含某个元素（这里以示例中的页面标题为例）
#     element_present = EC.presence_of_element_located((By.TAG_NAME, 'Scrape | Captcha'))
#     WebDriverWait(driver, 10).until(element_present)
#
#     # 页面加载完成后，获取页面源码
#     page_source = driver.page_source
#     print(page_source)
# finally:
#     driver.quit()