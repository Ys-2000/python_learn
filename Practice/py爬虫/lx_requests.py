import requests, re
from requests.auth import HTTPBasicAuth

# url = "https://www.baidu.com/"
# r = requests.get(url)
# print(type(r))          # 类型
# print(r.status_code)    # 状态码
# print(type(r.text))     # 响应体类型
# print(r.text[:100])     # 响应体内容
# print(r.cookies)        # cookies

# data = {
#     "name": "qwe",
#     "age": 16
# }
# req = requests.get('https://httpbin.org/get', params=data)
# print(req.text)
# print(req.json())
# print(type(req.json()))


# r = requests.get('https://ssr1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

# r = requests.get('https://scrape.center/favicon.ico')
# # print(r.text)
# # print(r.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# post 请求
# data = {'name': 'germey', 'age': '25'}
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post("https://httpbin.org/post", data=data, files=files)
# print(r.text)
# print(type(r.status_code), r.status_code)   # 返回状态码
# print(type(r.headers), r.headers)           # 返回请求头部
# print(type(r.cookies), r.cookies)           # 返回cookies
# print(type(r.url), r.url)                   # 返回URL
# print(type(r.history), r.history)           # 返回请求历史
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')     # 通过比较返回码和内置的成功的返回码，来保证请求得到了正常响应，输出成功请求的消息，否则程序终止

# session 维持
# s = requests.Session()      # 实例化session对象
# s.get('https://httpbin.org/cookies/set/number/123456789')
# r = s.get('https://httpbin.org/cookies')
# print(r.text)


# # SSL证书验证
# response = requests.get('https://ssr2.scrape.center/', verify=False,timeout=7)    # 使用 verify 参数控制是否验证证书，如果将其设置为 False，在请求时就不会再验证证书是否有效。如果不加 verify 参数的话，默认值是 True，会自动验证。
# print(response.status_code)

# # 身份认证
# r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
# print(r.status_code)


proxies = {'https': 'http://user:password@10.10.10.10:1080/',}
requests.get('https://httpbin.org/get', proxies=proxies)