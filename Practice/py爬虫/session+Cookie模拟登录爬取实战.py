import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/login')  # urljoin函数将两个 URL 地址组合在一起。这个函数需要两个参数，一个是基础 URL（base URL），另一个是相对 URL（relative URL），然后它会返回一个新的 URL 地址
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

# 复杂写法
# response_login = requests.post(LOGIN_URL, data={
#     'username': USERNAME,
#     'password': PASSWORD
# },allow_redirects=False)
# cookies = response_login.cookies
# print('cookies:', cookies)
# response_index = requests.get(INDEX_URL, cookies=cookies)
# print('Response Status', response_index.status_code)
# print('Response URL', response_index.url)

# 简化写法
session = requests.session()
response_login = session.post(LOGIN_URL, data={'username': USERNAME, 'password': PASSWORD})
cookies = session.cookies
response_index = session.get(INDEX_URL, cookies=cookies)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)
