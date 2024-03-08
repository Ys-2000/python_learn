# Headers插件 自行了解安装
# Copilot
import time
import requests
import sqlalchemy
from bs4 import BeautifulSoup
import re
import pandas as pd
# 写api (url)


def parse(key):
    p = 1
    datalist = []
    while True:
        url = f"https://www.haodf.com/doctor/list-all-{key}.html"
        params = {
            "p":p
        }
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Referer": "https://www.haodf.com/doctor/list-all-neifenmike.html?p=4",
            "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        response = requests.get(url, params=params, headers=headers)
        time.sleep(2)
        # print(repr(response.text))
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find('ul', class_='fam-doc-ul js-fam-doc-ul').find_all('li', recursive=False)
        if len(lis) == 0 or p >= 5: # or p>=5设置了另一种停下来得方式  演示效果4页就够了
            return pd.DataFrame(datalist,columns=['title','doctorid','recommend','liaoxiao','taidu','speciality','wenzhen','hao'])
        for li in lis:
            title = "、".join(li.find('span',class_="ml15").text.strip().split())
            # https://www.haodf.com/doctor/11171.html
            doctorid = li.get('data-src').split('/')[-1].split('.')[0]
            recommends = re.findall(r'<span style="float: right">\n *病友推荐度\n *<span class="ml5" style="color: red">\n *([\d\.]*?) *</span>',response.text,re.S)
            recommend = recommends[0] if len(recommends) > 0 else "暂无"
            # liaoxiao = li.find('p',class_='liaoxiao').text
            liaoxiao = "".join(li.find('p',class_='liaoxiao').text.strip().split())
            taidu = "".join(li.find('p',class_='taidu').text.strip().split())
            # print(title, doctorid, recommend)
            # print(liaoxiao,taidu)
            speciality = " ".join(li.find('p',class_='mt5 doc-speciaty').text.strip().split()[1:])
            wenzhen = "".join(li.find('span',class_='wenzhen mt5').text.strip().split())
            hao = "".join(li.find('span',class_='guahao mt5').text.strip().split())
            # print(speciality,'\n',wenzhen,'\n',hao)
            # print(doctorid,speciality)
            datalist.append([title,doctorid,recommend,liaoxiao,taidu,speciality,wenzhen,hao])
        print(p,'done...')
        p += 1


# datalist = parse(key)
# pd.DataFrame(datalist,columns=['title','doctorid','recommend','liaoxiao','taidu','speciality','wenzhen','hao']).to_csv('haodf.csv',index=False,encoding='utf-8-sig')
# https://www.haodf.com/doctor/list-all-yunchanfuyingyang.html
# https://www.haodf.com/doctor/list-all-neifenmike.html

def getCategory():
    url = "https://m.haodf.com/ndoctor/ajaxfacultylist?randomNumber=08282679792896224"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Referer": "https://m.haodf.com/doctor/index.html",
        "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    response = requests.get(url,headers=headers)
    # print(response.text)  # response.text是什么数据类型？  字符串
    # print([response.text])
    data =response.json()
    for level1Item in data['data']:
        level1name = level1Item['parentName']
        for level2Item in level1Item['childFaculty']:
            level2name = level2Item['name']
            key = level2Item['key']
            # print(level1name,level2name,key)
            yield level1name,level2name,key


if __name__ == '__main__':
    for level1name,level2name,key in getCategory():
        df = parse(key)
        df.to_csv(f'haodf_{key}.csv',index=False,encoding='utf-8-sig')
        print(f'{level1name}-{level2name} done...')


# sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/test?charset=utf8mb4")
