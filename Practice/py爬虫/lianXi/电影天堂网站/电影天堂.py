import requests, random, time,chardet, csv
from bs4 import BeautifulSoup


def main():
    url = 'https://dytt89.com/html/bikan/index.html'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=header)
    # response.encoding = 'gb2312'  # 设置编码格式为 自动检测编码
    encoding = chardet.detect(response.content)['encoding']
    response.encoding = encoding
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)

    list = soup.find(class_='co_content8').find_all('table')
    count = 0
    for item in list:
        name = item.find_all('a', class_='ulink')[1].string  # 名称
        try:
            coun = item.find_all('td')[5].get_text(strip=True).split('◎')[4].strip()[5:]  # 地区
        except IndexError:
            coun = "空"
        try:
            sort = item.find_all('td')[5].get_text(strip=True).split('◎')[5].strip()[5:]  # 类别
        except IndexError:
            sort = "空"
        try:
            release_date = item.find_all('td')[5].get_text(strip=True).split('◎')[8].strip()[5:]  # 上映日期
        except IndexError:
            release_date = "空"
        count += 1
        dic = {"ID": count,
               "名称": name,
               "地区": coun,
               "类别": sort,
               "上映日期": release_date,
               }
        writer.writerow(dic)
        # print(f"id:{count}|名称:{name}|地区:{coun}|类别:{sort}|上映时间:{release_date}|")
    print("---页面1抓取完成---")
    count = 30
    for page in range(2, 24):
        url = f'https://dytt89.com/html/bikan/index_{page}.html'
        time.sleep(3)
        header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=header)
        # html = response.content.decode(response.apparent_encoding)        # 与下面两行功能一致 由gpt生成
        # response .encoding = response.apparent_encoding  # 设置编码格式为 自动检测编码
        response .encoding = 'gb2312'  # 设置编码格式为 自动检测编码
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        list = soup.find(class_='co_content8').find_all('table')
        for item in list:
            name = item.find_all('a', class_='ulink')[1].string     #名称
            try:
                coun = item.find_all('td')[5].get_text(strip=True).split('◎')[4].strip()[5:]    # 地区
            except IndexError:
                coun = "空"
            try:
                sort = item.find_all('td')[5].get_text(strip=True).split('◎')[5].strip()[5:]    # 类别
            except IndexError:
                sort = "空"
            try:
                release_date = item.find_all('td')[5].get_text(strip=True).split('◎')[8].strip()[5:]   # 上映日期
            except IndexError:
                release_date = "空"  # 如果出现IndexError异常，返回"空"字符串
            count += 1
            dic = {"ID": count,
                   "名称": name,
                   "地区": coun,
                   "类别": sort,
                   "上映日期": release_date,
                   }
            writer.writerow(dic)
            # print(f"id:{count}|名称:{name}|地区:{coun}|类别:{sort}|上映时间:{release_date}")
            # sleep_time = random.uniform(1, 3)  # 生成 1 到 3 秒的随机延时
            # time.sleep(sleep_time)
        print(f"---页面{page}抓取完成---")

with open('电影天堂.csv', 'w', encoding='utf-8-sig', newline='') as f:  # newline:换行写入
    writer = csv.DictWriter(f, fieldnames=["ID", "名称", "地区", "类别", "上映日期"])
    writer.writeheader()  # 将字段写入csv格式文件首行
    if __name__ == '__main__':
        main()

print("全部抓取完成！！！")