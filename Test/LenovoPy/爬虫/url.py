# 导包
import urllib3

# 1. 生成一个连接池管理器的对象，就是一个和远程http的一个连接
http = urllib3.PoolManager()
# 1- 设置User-Agent
request_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
}
# 2. 发送一个请求(使用GET方法，访问baidu的页面资源)，获取返回的响应
resp = http.request('GET', 'http://www.baidu.com/index.html', headers=request_headers)
# resp = http.request('GET', 'https://bj.xiaozhu.com/', headers=request_headers)
# resp = http.request('GET', 'https://movie.douban.com/review/best/', headers=request_headers)
# 2- 获取响应的状态码
status_code = resp.status
print(status_code)
# 2- 获取响应的数据 = 页面的源代码
html_text = resp.data
print(html_text)
# 2- 获取响应的字符编码
# encoding_type = resp.encoding
# print(encoding_type)

# 2- 手工指定编码类型
# resp.encoding = 'utf-8'
# encoding_type = resp.encoding
# print(encoding_type)
