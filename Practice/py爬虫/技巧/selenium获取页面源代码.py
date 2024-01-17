import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # 启用无头模式
chrome_options.add_argument("--disable-gpu")  # 禁用GPU加速，某些情况下可以减少资源消耗

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.tupianzj.com/bizhi/DNmeinv/")
time.sleep(5)
content = driver.page_source
print(content)
driver.quit()