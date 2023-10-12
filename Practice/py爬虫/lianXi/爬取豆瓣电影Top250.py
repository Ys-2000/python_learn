import requests, random, xlwt
from bs4 import BeautifulSoup


# 创建EXCEL
book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建一个新的 Excel 工作簿
sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建一个sheet页
sheet.write(0, 0, '排名')
sheet.write(0, 1, '名称')
sheet.write(0, 2, '评分')
sheet.write(0, 3, '导演')
sheet.write(0, 4, '简介')

n = 1
def main(page):
    global n  # 使用全局变量 n
    url = f'https://movie.douban.com/top250?start='+str(page*25)+'&filter='
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    # 解析
    list = soup.find(class_='grid_view').find_all('li')
    for item in list:
        item_index = item.find(class_='').string                # 排名
        item_name = item.find(class_='title').string            # 电影名称
        item_img = item.find('a').find('img').get('src')        # 电影封面
        item_score = item.find(class_='rating_num').string      # 评分
        item_author = item.find('p').text.strip()                    # 导演
        # print(item_author)
        item_intr = item.find(class_='inq').string if item.find(class_='inq') else "无简介"              # 电影介绍
        # print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)
        save_to_excel(n,item_index,item_name,item_score,item_author,item_intr)
        n += 1  # 自增 n

# 保存
def save_to_excel(n,item_index, item_name, item_score,item_author, item_intr):
    sheet.write(n, 0, item_index)
    sheet.write(n, 1, item_name)
    sheet.write(n, 2, item_score)
    sheet.write(n, 3, item_author)
    sheet.write(n, 4, item_intr)


# 爬取url
def request_douban(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

if __name__ == '__main__':
    for i in range(0, 10):
        print(f"正在写入{i+1}页数据...")
        main(i)
    book.save('豆瓣最受欢迎的250部电影.xls')