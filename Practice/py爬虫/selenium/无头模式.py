from selenium import webdriver
from selenium.webdriver import EdgeOptions

option = EdgeOptions()
option.add_argument('--headless')
browser = webdriver.Chrome(options=option)
browser.set_window_size(1366, 768)
browser.get('https://www.baidu.com')
browser.get_screenshot_as_file('preview.png')       # 获取截图


browser.close()
browser.quit()