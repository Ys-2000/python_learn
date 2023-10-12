# 豆瓣
from bs4 import BeautifulSoup
import random, time, csv, requests


def main(page):
    url = f"https://movie.douban.com/top250?start={page}&filter="
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    html = requests.get(url, headers=header).text

    soup = BeautifulSoup(html, 'lxml')
    list = soup.find(class_='grid_view').find_all('li')

    for item in list:
        # .get_text() 方法可以用在标签对象本身，也可以用在其父标签对象上。
        index = item.find(class_='').string
        title = item.find(class_='title').string
        rating = item.find(class_='rating_num').string
        votes = item.find('div', class_='star').find_all('span')[-1].get_text(strip=True)[:-2]  # strip=True 是 .get_text() 方法的一个参数。它的作用是去除文本中的额外空白字符，包括换行符、空格等
        quote = item.find(class_='inq').string if item.find(class_='inq') else "无简介"
        # .split('/')使用'/' 进行分割，将字符串拆分为一个列表，获取列表中的第二个元素(索引从0开始)
        # .strip()去除字符串前后的空白字符
        coun = item.find('div', class_='bd').find_all('p')[0].get_text(strip=True).split('/')[2].strip()
        # print(f"{index}.{coun}")
        # print(f"排名:{index}|标题:{title}|评分{rating}|评价人数:{votes}|简介:{quote}|地区:{coun}")
        dic = {"排名": index,
               "标题": title,
               "评分": rating,
               "评价人数": votes,
               "地区": coun,
               "简介": quote,
               }
        writer.writerow(dic)
    print(f"页面{page}数据成功写入到豆瓣movies.csv")

page_list = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225]
with open('豆瓣movies.csv', 'w', encoding='utf-8-sig', newline='') as f:  # newline:换行写入
    writer = csv.DictWriter(f, fieldnames=["排名", "标题", "评分", "评价人数", "地区","简介"])
    writer.writeheader()  # 将字段写入csv格式文件首行
    for i in page_list:
        if __name__ == '__main__':
            print(f"正在写入{i}页数据...")
            main(i)
            sleep_time = random.uniform(1, 3)  # 生成 1 到 3 秒的随机延时
            time.sleep(sleep_time)
    print("爬取完成！！")


