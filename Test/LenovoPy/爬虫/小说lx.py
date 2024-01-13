import requests
from bs4 import BeautifulSoup

# url = 'https://www.readnovel.com/ajax/user/info?_csrfToken=D7KsC4P8yj6ve6dktNLdnqLBZplRiN4KyrAmIySk&_=1570149240567'
# a = requests.get(url)
# a.encoding = 'gbk'
# b = a.text
# c = BeautifulSoup(b, 'lxml')              # 解析成lxml格式
# c.find('div', id='j-catalogWrap')
# print(c)


url = 'https://www.readnovel.com/ajax/user/info?_csrfToken=D7KsC4P8yj6ve6dktNLdnqLBZplRiN4KyrAmIySk&_=1570149240567'
res = requests.get(url)
res.encoding = 'gbk'                            # 编码是 gbk
html = res.text                                 # text 文本形式
soup = BeautifulSoup(html, 'lxml')              # 解析成lxml格式
div = soup.find('div', id='j-catalogWrap')         # find 查找
data = div.get_text()                          # 获取div表签的内容
# data = data.replace("try{mad1('gad2'):}catch(ex){} ", " ")     # replace  把"..."替换为"..."
print(data)