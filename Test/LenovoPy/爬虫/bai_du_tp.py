import requests
import time

name = input('输入要爬取的数据：')
pn = int(input('需要爬取多少页：'))

for num in range(1, pn+1):
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+name+'cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word='+name+'&s=&se=&tab=&width=&height=&face=&istype=2&qc=&nc=1&fr=&expermode=&force=&pn='+str(num*30)+'&rn=30&gsm=&1570082957142='
    res = requests.get(url)
    html = res.json()
    data = html['data'][:30]
    for i in data:
        di = i['di']                                 # 命名 随便一个标签都可以

        hover = i['hoverURL']
        print(hover)
        res = requests.get(hover)                   # 请求
        photo = res.content                         # 以二进制解析
        fb = open('./photo/'+di+'.jpg', 'wb')       # 以二进制写入
        fb.write(photo)                             # write 写入
        fb.close()                                  # 结束

        time.sleep(0.3)                             # 每循环一次给一个缓存时间

