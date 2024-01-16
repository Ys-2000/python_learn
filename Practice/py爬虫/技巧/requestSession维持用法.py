import requests

# session 维持
# session.get('https://httpbin.org/cookies/set/number/123456789')
# response = session.get('https://httpbin.org/cookies')


session = requests.Session()      # 实例化session对象
# 为会话设置头部
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# 更新session对象默认请求头
session.headers.update(headers)


# 使用会话发送请求
response = session.get('https://www.tupianzj.com/bizhi/DNmeinv/')

# 解码响应内容
content = response.content.decode('gbk')

print(content)
