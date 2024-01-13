import requests
# r = requests.get("https://item.jd.com/5089225.html")
# print(r.status_code)    # 状态码
# print(r.encoding)       # 编码
url = "https://item.jd.com/5089225.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
