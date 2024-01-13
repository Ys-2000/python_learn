from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://specmaplinux.shuwantech.com/_builder')

# 在百度搜索框中搜索'python'
driver.find_element_by_id('email').send_keys('Sw_admin@qq.com')
driver.find_element_by_name('password').send_keys('qwe123')

 # 点击'按钮'
driver.find_element_by_name('action').click()

# 点击'百度搜索'
# driver.find_element_by_id('su').click()

time.sleep(3)
driver.quit()
