import requests,random,csv
from bs4 import BeautifulSoup

def main():
    url = 'https://m.hupu.com/nba/team-rank'
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
    bang_dan = html.find('div',class_='nba-content').find_all('div',class_='nba-content-wrap')
    for i in bang_dan:
        phb = i.find('div').find('div').find('span').get_text(strip=True)    # 排行榜
        # if phb == '大西洋分区':
        #     qwe = i.find_all('div', class_='nba-header-2')
        #     for a in qwe:
        #         zxc = a.find('span').get_text()
        #         print(zxc)
        # else:
        #     print(phb)
        print(f"***{phb}***")
        # 排名
        apm = i.find_all('div')[2].get('class')
        bpm = str(apm[0])
        try:
            if bpm == 'nba-item-1':
                pm = i.find_all('div',class_=f'{bpm}')
                for a in pm:
                    paiming = a.find('div').find('span').get_text(strip=True)       # 球队排名
                    name = a.find('div').find_all('span')[1].get_text(strip=True)   # 球队名称
                    s_f = a.find_all('span')[2].get_text(strip=True)                # 胜-负
                    s_l = a.find_all('span')[3].get_text(strip=True)                # 胜率/胜场差
                    jinkuang = a.find_all('span')[4].get_text(strip=True)           # 近况
                    print(paiming,name,s_f,s_l,jinkuang)

            elif bpm == 'nba-item-2':
                # 找到所有分区
                qwe = i.find_all('div', class_='nba-header-2')

                for aa in qwe:
                    # 获取分区名称
                    zxc = aa.find('span').get_text()
                    print(zxc)
                    # 获取该分区内的球队信息
                    pm = i.find_all('div', class_=f'{bpm}')
                    su = 0
                    for a in pm:
                        paiming = a.find('div').find('span').get_text(strip=True)       # 球队排名
                        name = a.find('div').find_all('span')[1].get_text(strip=True)   # 球队名称
                        s_f = a.find_all('span')[2].get_text(strip=True)                # 胜-负
                        s_l = a.find_all('span')[3].get_text(strip=True)                # 胜率/胜场差
                        jinkuang = a.find_all('span')[4].get_text(strip=True)           # 近况
                        print(paiming, name, s_f, s_l, jinkuang)
                        su += 1
                        if su >= 5:
                            break



            elif bpm == 'nba-item-3':
                pm = i.find_all('div',class_=f'{bpm}')
                for a in pm:
                    paiming = a.find('div').find('span').get_text(strip=True)           # 球队排名
                    name = a.find('div').find_all('span')[1].get_text(strip=True)       # 球队名称
                    shu_ju = a.find_all('span')[2].get_text(strip=True)                 # 数据
                    print(paiming,name,shu_ju)
            else:
                print('暂无数据！')
        except IndexError:
            print('error！！')





if __name__ == '__main__':
    main()