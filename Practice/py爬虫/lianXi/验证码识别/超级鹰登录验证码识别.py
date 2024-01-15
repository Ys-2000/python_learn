import time,random

import ddddocr
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.chaojiying.com/user/login/'


web = webdriver.Chrome()

web.get(url)
time.sleep(random.uniform(0, 2))
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("Ys2091")
time.sleep(random.uniform(1, 2))
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("Ys204476")
img = web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img')

ocr = ddddocr.DdddOcr(show_ad=False)
verify_code = ocr.classification(img.screenshot_as_base64)
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)    # 输入验证码
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()       # 点击登录按钮
time.sleep(random.uniform(2, 3))    # 随机等待2-3秒

# web.get_cookies()拿到的cookie格式不正常：[{name:xxx,value:xxx},{},{}],需要做处理

print(web.get_cookies())
coolies = {item['name']:item['value'] for item in web.get_cookies()}
print("**"*20)
print(coolies)

time.sleep(10)
web.close()      # 关闭当前活动窗口
web.quit()       # 关闭所有窗口并退出浏览器












import requests,random,base64
# url = 'https://www.chaojiying.com/include/code/code.php?u=1'
# user_agent_list = [
#     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#     'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
#     'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
#     'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
#     'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
# ]
# headers = {
#     'User-Agent': random.choice(user_agent_list)
# }
# response = requests.get(url,headers=headers)
#
# # 下载图片
# with open('img/yzm.jpg', mode='wb') as f:
#     f.write(response.content)
#
# ocr = ddddocr.DdddOcr(show_ad=False)
# with open('img/yzm.jpg', mode='rb') as f:
#     image = f.read()
# res = ocr.classification(image)
# print(res)




