import requests, random
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
    header = {
        'User-Agent': random.choice(user_agent_list)
    }
    response = requests.get(url,headers=header).text
    html = BeautifulSoup(response,'lxml')

    # 前三名称
    name_a = html.find('div',id='voteList_famous').find_all('img',class_='top_company_name')
    jianjie_a = html.find('div',id='voteList_famous').find_all('p',class_='top_three_describe')
    for i,name in enumerate(name_a,1):
        name = name.get('title')
        if i <= len(jianjie_a):
            jj_a = jianjie_a[i-1].get_text(strip=True)
        else:
            jj_a = '无简介'
        # print(i,name,jj_a)
        file.write(f'排名: {i}\t名称:{name}\n简介:{jj_a}\n')
        file.write(f'{"=" * 50}\n')
    # 其他名称
    s = 4
    qwe = html.find_all('div',class_='rank_last_list')[1].find_all('li')
    for b in qwe:
        name_b = b.find('a',class_='company_logo').find('img').get('title')
        jj_b = b.find('p',class_='list_company_describe').get_text(strip=True)
        # print(s,name_b,jj_b)
        file.write(f'排名: {s}\t名称:{name_b}\n简介:{jj_b}\n')
        file.write(f'{"=" * 50}\n')
        s+=1



with open('西装人气榜.txt','w',encoding='utf-8') as file:
    if __name__ == '__main__':
        main()
        file.close()
