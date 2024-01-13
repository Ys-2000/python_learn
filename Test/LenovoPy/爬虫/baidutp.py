'''
案例二：爬取百度图片
'''
import requests
import time

url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%AB%98%E6%B8%85%E5%8A%A8%E6%BC%AB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E9%AB%98%E6%B8%85%E5%8A%A8%E6%BC%AB&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=&1570267899101='
res = requests.get(url)
html = res.json()
data = html['data'][:30]
for i in data:
    di = i['di']

    hover = i['hoverURL']
    print(hover)
    res = requests.get(hover)
    photo = res.content
    fb = open('./photo/'+di+'.jpg','wb')
    fb.write(photo)
    fb.close()

    time.sleep(0.3)