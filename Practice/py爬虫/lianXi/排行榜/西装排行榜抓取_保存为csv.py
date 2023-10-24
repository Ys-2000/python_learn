import requests, random, csv
from bs4 import BeautifulSoup


def main():
    url = 'https://www.chinapp.com/paihang/xz'
    user_agent_list = [
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    ]
    USER_AGENT = random.choice(user_agent_list)
    header = {
        'User-Agent': USER_AGENT
    }
    response = requests.get(url,headers=header).text
    html = BeautifulSoup(response,'lxml')


    # 获取名称
    name_a = html.find('div',id='voteList_shida').find_all('img',class_='top_company_name')
    # 获取品牌简介
    jianjie_a = html.find('div',id='voteList_shida').find_all('p',class_='top_three_describe')

    # 前三品牌名称及简介
    for i, name_tag in enumerate(name_a, 1):
        name_a = name_tag.get('title')
        #这段代码添加了一个条件检查，以确保 i 不会超出 pp_jianjie 的索引范围，如果长度不匹配，它会显示一条相应的消息。这提高了代码的稳定性。
        if i <= len(jianjie_a):
            jj_a = jianjie_a[i - 1].get_text(strip=True)
        else:
            jj_a = "无品牌简介"

        dic = {
            '排名':i,
            '名称':name_a,
            '简介':jj_a
        }
        writer.writerow(dic)

    # 获取其他品牌名称
    name_b = html.find('div',id='voteList_shida').find_all('a',class_='company_logo')
    jianjie_b = html.find('div',id='voteList_shida').find_all('li')

    s = 4
    for i, name_tag in enumerate(name_b,1):
        name = name_tag.find('img').get('title')
        if i - 1 < len(jianjie_b):
            jj_b = jianjie_b[i - 1].find('p',class_='list_company_describe').get_text(strip=True)
        else:
            jj_b = "无品牌简介"
        dic = {
            '排名':s,
            '名称':name,
            '简介':jj_b
        }
        writer.writerow(dic)
        s += 1

with open('xz_排行榜.csv','w',encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["排名", "名称", "简介"])
    writer.writeheader()        # 将字段写入csv格式文件首行
    if __name__ == '__main__':
        main()





