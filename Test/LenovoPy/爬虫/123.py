import requests
from bs4 import BeautifulSoup
import time


def get_data(href):
    res = requests.get(href)
    res.encoding = 'gbk'
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', id='txtContent')

    data = div.get_text()
    data = data.replace("try{mad1('gad2');} catch(ex){}　", "").replace("　　", "\n")
    return data


url = 'https://www.yuyouge.com/book/27742/'
res = requests.get(url)
res.encoding = 'gbk'
soup = BeautifulSoup(res.text, 'lxml')
ul = soup.find('ul', id='chapters-list')
li = ul.find_all('a')

fb = open("绝世武神.txt", 'w', encoding='utf-8')

for a in li:
    title = a.get_text()
    print(title)
    href = "https://www.yuyouge.com"+a['href']
    data = get_data(href)
    fb.write(title)
    fb.write('\n')
    fb.write(data)
    fb.write('\n')
    time.sleep(0.3)

fb.close()
