import requests, csv
from bs4 import BeautifulSoup


def main():
    cid = 0
    for page in range(1, 11):
        url = f"https://ssr1.scrape.center/page/{page}"
        header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
        request = requests.get(url, headers=header).text
        html = BeautifulSoup(request, "lxml")
        list = html.find(class_='el-col el-col-18 el-col-offset-3').find_all(class_='el-card item m-t is-hover-shadow')
        for i in list:
            cid += 1
            ID = cid
            # 提取电影名称
            name = i.find(class_='m-b-sm').string
            # 提取电影分类
            categories = [button.text.strip() for button in i.find_all('button', class_='category')]
            # 提取电影地区
            info_span = i.find_all('div', class_='info')[0].find('span').string
            # 提取电影时长
            movie_info = i.find_all('div', class_='info')[0].find_all('span')[2].string
            # 提取上映时间
            try:
                re_data = i.find_all('div', class_='info')[1].find('span').string
            except AttributeError:
                re_data = "空"
            # 提取电影评分
            score = i.find('p', class_='score m-t-md m-b-n-sm').get_text(strip=True)
            # print(f'ID:{ID}|名称:{name}|类型:{categories}|地区:{info_span}|时长:{movie_info}|上映时间:{re_data}|评分:{score}|')
            dic = {"ID": cid,
                   "名称": name,
                   "类型": categories,
                   "地区": info_span,
                   "时长": movie_info,
                   "上映时间": re_data,
                   "评分": score,
                   }
            writer.writerow(dic)


with open("scrape.csv","w", encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["ID", "名称", "类型", "地区", "时长", "上映时间", "评分"])
    writer.writeheader()        # 将字段写入csv格式文件首行
    if __name__ == '__main__':
        main()