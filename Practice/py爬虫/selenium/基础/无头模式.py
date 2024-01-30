from selenium import webdriver
from selenium.webdriver import ChromeOptions
import os
# 获取当前工作目录
current_directory = os.getcwd()
print(current_directory)
# 构造相对保存路径
relative_save_path = '../img/preview.png'

# 构造绝对保存路径
absolute_save_path = os.path.join(current_directory, relative_save_path)

option = ChromeOptions()
option.add_argument('--headless')        # 启用无头模式,不会调出浏览器窗口

# # 添加实验性选项以使浏览器保持打开状态
# option.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=option)
browser.set_window_size(1366, 768)
try:
    browser.get('https://www.baidu.com')
    img = browser.get_screenshot_as_file(absolute_save_path)       # 获取截图

finally:
    browser.close()
    browser.quit()