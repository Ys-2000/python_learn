import requests


"""
# 该网站需要在请求头中给到cookie才能获取到网页源代码，如果用response.text获取到的是乱码，通过.decode('gbk')进行解码后显示页面源代码
在浏览器中右键查看网页源代码。搜索:charset  可以看到该网页的编码
"""
url = "https://www.tupianzj.com/bizhi/DNmeinv/"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "https://www.tupianzj.com/bizhi/DNmeinv/",       # 防盗链
    "Cookie":"t=01439e9bd540f7144aa7c44649b8e9a3; r=1685; Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1704864241,1705390019; Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1705390019",
}


# 首先通过.content 获取原始字节串响应，然后使用.decode('gbk') 将这些字节转换为字符串。这是处理非 UTF-8 编码响应的常见方法，特别是对于一些使用特定地区编码（如中文网站常用的 gbk 或 gb2312）的网站。
response = requests.get(url, headers=headers).content.decode('gbk')
# 这是处理非 UTF-8 编码响应的常见方法，特别是对于一些使用特定地区编码（如中文网站常用的 gbk 或 gb2312）的网站。
print(response)

