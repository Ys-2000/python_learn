import requests
from bs4 import BeautifulSoup


url = 'https://www.yuyouge.com/book/27742/13451820.html'        #
res = requests.get(url)
res.encoding = 'gbk'                            # 编码是 gbk
html = res.text                                 # text 文本形式
soup = BeautifulSoup(html, 'lxml')              # 解析成lxml格式
div = soup.find('div', id='txtContent')         # find 查找
data = div.get_text()                          # 获取div表签的内容
data = data.replace("try{mad1('gad2'):}catch(ex){} ", " ")     # replace  把"..."替换为"..."
print(data)
