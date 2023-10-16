import requests, os
from bs4 import BeautifulSoup

base_path = os.path.join('d:' + os.path.sep, '电子书', '斗破苍穹')

# 网友请求
def getHTMLtext(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
    }
    try:

        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        # r.encoding设置了 HTTP 响应的编码，以确保正确解析响应中的文本数据
        # r.apparent_encoding 是 Requests 库的一个属性，用于自动检测响应内容的编码
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('访问失败')

# 网页内容解析
def parseHTMLtext(html,down,list):
    pass

# 文件保存
def savetxt(path, txt):
    with open(path, 'ab') as f:
        f.write(txt.encode('utf-8')+'\n')
        f.close()

def main():
    url = 'https://www.555x.org/txt3869.html'
    response = getHTMLtext(url)
    html = BeautifulSoup(response,'lxml')
    # 小说名称
    name = html.find(id='info').find('h1').string
    # 作者
    zuoze = html.find(id='info').find_all('p')[0].find('a').string
    # 点击数
    dian_ji_shu = html.find(id='info').find_all('p')[1].string[3:]
    # 字数
    zi_shu = html.find(id='info').find_all('p')[2].string[3:]
    # 简介
    jian_jie = html.find(id='intro').get_text(strip=True)

    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)
    sm_path = os.path.join(base_path, '说明.txt')
    txt = f'小说名称:《{name}》\n作者:{zuoze}\n点击数:{dian_ji_shu}\n字数:{zi_shu}\n简介:{jian_jie}'
    # savetxt(sm_path, txt)


    # 获取章节
    zhang_jie = html.find(id='list').find('dl').find_all('a')[10:110]
    for zj in zhang_jie:
        href = zj['href']
        zj_name = zj['title']
        zj_url = f'https://www.555x.org{href}'
        # 解析文本
        zjdata_a = getHTMLtext(zj_url)
        bs_a = BeautifulSoup(zjdata_a, 'lxml')
        # 保存章节标题+内容
        txt_a = bs_a.find(class_='bookname').get_text(strip=True)+'\n'+bs_a.find(id='booktxt').get_text(strip=True)+'\n'
        # bta = bs_a.find(class_='bookname').get_text(strip=True)    # 标题
        if not os.path.exists(base_path):
            os.makedirs(base_path, exist_ok=True)
        zj_path = os.path.join(base_path, f'{zj_name}.txt')
        savetxt(zj_path, txt_a)
        if bs_a.find(class_='box_con').find('div',class_='bottem1').find_all('a')[2].string == '下一页':
            zj_url_b = zj_url[:-5]+'_2'+ zj_url[-5:]
            # 解析文本
            zjdata_b = getHTMLtext(zj_url_b)
            bs_b = BeautifulSoup(zjdata_b, 'lxml')
            # 第二节标题+内容
            txt_b = bs_b.find(class_='bookname').get_text(strip=True)+'\n'+bs_b.find(id='booktxt').get_text(strip=True)+'\n'
            # # 输出
            # print(bs_b.find(class_='bookname').get_text(strip=True))    # 标题
            # print(txt_b)
            if not os.path.exists(base_path):
                os.makedirs(base_path, exist_ok=True)
            zj_path = os.path.join(base_path, f'{zj_name}.txt')
            savetxt(zj_path, txt_b)
        print(f'{zj_name} 下载完成！！！')



# 主函数
if __name__ == '__main__':
    main()


