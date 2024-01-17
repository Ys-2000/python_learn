import requests

# session 维持
# session.get('https://httpbin.org/cookies/set/number/123456789')
# response = session.get('https://httpbin.org/cookies')


session = requests.Session()      # 实例化session对象
# 为会话设置头部
headers ={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Cookie": "Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1705457124;Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1705457124;r=1298;t=3922ad15123b5bbfd258f6239b480747",
    "Referer": "https://www.tupianzj.com/bizhi/DNmeinv/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36"
}


# 更新session对象默认请求头
session.headers.update(headers)
# 使用会话发送请求
session.get('https://www.tupianzj.com/bizhi/DNmeinv/')
response = session.get('https://www.tupianzj.com/bizhi/DNmeinv/')

# 解码响应内容
content = response.content.decode('gbk')

print(content)
