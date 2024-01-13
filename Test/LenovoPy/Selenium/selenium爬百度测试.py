from selenium import webdriver
import time
driver = webdriver.Chrome()     # 运行chrome驱动

# driver.get('https://www.amazon.cn/')
# driver.find_element_by_id("searchDropdownBox").click()    # 点击分类
# driver.find_element_by_name('field-keywords').send_keys('knut python') # 搜索框输入内容
# time.sleep(2)   # 两秒后
# driver.quit()   # 关闭浏览器

# 打开百度
driver.get('http://www.baidu.com')
# 选择网页元素 百度搜索框id="kw"
element_keyword = driver.find_element_by_id('kw').send_keys('python')

# 找到搜索按钮 百度搜索按钮id="su"
element_search_button = driver.find_element_by_id('su').click()

# time.sleep(2)

ret = driver.find_element_by_id('su')

print(ret.text)

# if ret.text.startswith('宋曲'):
#     print('测试通过')
# else:
#     print('不通过')

driver.quit()

