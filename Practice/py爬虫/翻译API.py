# # from urllib import request
# import urllib.request
#
# url = "https://www.baidu.com/"
# resp = urllib.request.urlopen(url)
#
#
# with open("mybaidu.html",mode="w",encoding="UTF-8")as f:
#     f.write(resp.read().decode("utf-8"))
#
# print(resp.read().decode("utf-8"))

import requests
q = input("请输入内容:")
# url = f'https://www.sogou.com/web?query={q}'
url = 'https://fanyi.baidu.com/sug'
dat = {"kw": q}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

# resp = requests.get(url, headers=headers)
resp = requests.post(url, headers=headers, data=dat)
# print(resp.text)
print(resp.json())
resp.close()    # 关闭爬虫程序

