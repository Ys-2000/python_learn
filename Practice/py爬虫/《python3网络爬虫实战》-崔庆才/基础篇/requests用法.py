import requests


# Session维持
session = requests.session()
session.get('http://httpbin.org/cookies/set/number/123456789')      # 访问这个url设置cookies名称为"number"值为"123456789"
response = session.get('http://httpbin.org/cookies')                # 获取当前的cookies
print(response.text)

# 校验是否请求成功
r = requests.get('https://static1.scrape.cuiqingcai.com/')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
if not r.status_code == requests.codes.ok:
    exit()
else:
    print('Request Successfully')





# # SSL证书验证
# resp = requests.get('https://static2.scrape.cuiqingcai.com', verify=False)  # verify默认是True，设置为False后请求时不在验证证书是否有效
# print(resp.status_code)