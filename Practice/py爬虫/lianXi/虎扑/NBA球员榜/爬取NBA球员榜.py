import requests,random,csv
from bs4 import BeautifulSoup

def main():
    url = 'https://m.hupu.com/nba/player-rank'
    user_agent_list = [
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    ]
    header = {
        'User-Agent': random.choice(user_agent_list)
    }
    response = requests.get(url,headers=header).text
    html = BeautifulSoup(response,'lxml')

    sj = html.find_all('div',class_='player-content-wrap')
    for i in sj:
        bang_dan = i.find('span').get_text(strip=True)      # 榜单
        data = i.find_all('div',class_='player-item-2')     # 球员信息
        print(bang_dan)
        for a in data:
            pm = a.find('span').string      # 排名
            name = a.find('div',class_='player-item-2-left').find_all('span')[0].string      # 姓名
            fbz = a.find('div',class_='player-item-2-left').find_all('span')[1].get_text(strip=True)      # 分、板、助
            sj = a.find_all('div')[-1].get_text(strip=True)       # 数据
            print(pm,name,fbz,sj)
            dic = {"榜单": bang_dan,
                   "排名": pm,
                   "姓名": name,
                   "分板助": fbz,
                   "数据": sj,
                   }
            writer.writerow(dic)


with open('nba榜单.csv','w',encoding='utf-8', newline='') as f:   # newline换行
    writer = csv.DictWriter(f, fieldnames=["榜单", "排名", "姓名", "分板助", "数据"])
    writer.writeheader()  # 将字段写入csv格式文件首行
    if __name__ == '__main__':
        main()