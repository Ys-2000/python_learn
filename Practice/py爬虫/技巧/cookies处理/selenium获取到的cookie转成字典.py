import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # 启用无头模式
chrome_options.add_argument("--disable-gpu")  # 禁用GPU加速，某些情况下可以减少资源消耗

driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()
driver.get("https://www.tupianzj.com/bizhi/DNmeinv/")
time.sleep(5)
cookies_dict = {item['name']: item['value'] for item in driver.get_cookies()}   # 把selenium get_cookies()获取到的cookie转换成字典格式
print(cookies_dict)

# cookie_string = ";".join([f"{key}={value}" for key, value in cookies_dict.items()]) # 把获取到的字典 转换成字符串格式
# print(cookie_string)

driver.quit()