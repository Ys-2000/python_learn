import requests, time
from pyquery import PyQuery

start = time.time()        # 获取了当前的时间戳，并将其赋值给变量 start。用来记录开始计时的时间点
#确定目标
url = "https://pvp.qq.com/web201605/herolist.shtml"

#发送请求
html = requests.get(url).content   # .content用于获取响应的内容

#解析数据
doc = PyQuery(html)
items = doc('.herolist>li').items()     # 将它们作为一个可迭代对象的集合返回给 items

for item in items:
     url = item.find('img').attr('src')
     # print(url)
     urls = 'http:'+url
     # name = item.find('a').text()
     # name = item.find('img').attr('alt')
     name = item.text()

     print(name)
     url_content = requests.get(urls).content

#     #保存数据
#      with open('img/'+name+'.jpg', 'wb') as file:
#           file.write(url_content)
#           print("正在下载%s......%s"%(name, urls))
#
# print("下载完毕")
# end = time.time()
# print('图片爬取共计耗时{:.2f}秒'.format(end-start))