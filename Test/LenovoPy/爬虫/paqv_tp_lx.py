import requests
import time
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%AB%A5%E6%A2%A6&cl=&lm=&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E7%AB%A5%E6%A2%A6&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&force=&pn=30&rn=30&gsm=&1570094095857='
res = requests.get(url)
html = res.json()
data = html['data'][:30]
for i in data:
    di = i['browserPv']

    hover = i['hoverURL']
    # print(hover)
    res = requests.get(hover)
    photo = res.content
    print(photo)
    fb = open('./photo/'+di+'.jpg', 'wb')
    fb.write(photo)
    fb.close()

    time.sleep(0.3)

