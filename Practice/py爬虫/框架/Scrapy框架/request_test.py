import requests


url = "https://www.tupianzj.com/bizhi/DNmeinv/"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie":"t=01439e9bd540f7144aa7c44649b8e9a3; r=1685; Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1704864241,1705390019; Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1705390019",
}



response = requests.get(url, headers=headers).content.decode('gbk')     # 首先通过.content 获取原始字节串响应，然后使用.decode('gbk') 将这些字节转换为字符串。这是处理非 UTF-8 编码响应的常见方法，特别是对于一些使用特定地区编码（如中文网站常用的 gbk 或 gb2312）的网站。
# 这是处理非 UTF-8 编码响应的常见方法，特别是对于一些使用特定地区编码（如中文网站常用的 gbk 或 gb2312）的网站。
print(response)