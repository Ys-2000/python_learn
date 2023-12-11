import requests,random,base64
import ddddocr

url = 'http://bihua.org.cn/login/verify.html'
user_agent_list = [
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
]
headers = {
    'User-Agent': random.choice(user_agent_list)
}
response = requests.get(url,headers=headers)

# 下载图片
with open('img/yzm.jpg', mode='wb') as f:
    f.write(response.content)

ocr = ddddocr.DdddOcr(show_ad=False)
with open('img/yzm.jpg', mode='rb') as f:
    image = f.read()
res = ocr.classification(image)
print(res)




