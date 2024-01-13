from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 来源：https://cuiqingcai.com/2599.html

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
assert "百度" in driver.title    # 检查页面的标题是否包含字符串“百度”
elem = driver.find_element_by_name("wd")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)     # 使用 send_keys 方法模拟按下回车键
print(driver.page_source)       # 语句打印当前页面的源代码
time.sleep(3)
driver.quit()
