from selenium import webdriver

proxy = '123.57.1.16:8029'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://httpbin.org/get')
