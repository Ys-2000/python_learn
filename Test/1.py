from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service = Service(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')

# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)

print("Title:", driver.title)
