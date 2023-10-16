import requests
import xlwt
import os
from bs4 import BeautifulSoup


def scrape_movie_data(page):
    # 抓取封面、名称、分类、上映时间、评分
    url = f'https://ssr1.scrape.center/page/{page}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers).text
    # 指定解析器为lxml，用于解析 HTML 和 XML 文档
    html = BeautifulSoup(response, 'lxml')
    list = html.find(class_='el-col el-col-18 el-col-offset-3').find_all(class_='el-card item m-t is-hover-shadow')

    movie_data = []

    for i in list:
        # 提取电影名称
        name = i.find(class_='m-b-sm').string
        # 提取电影分类
        categories = [button.text.strip() for button in i.find_all('button', class_='category')]
        # 提取上映时间
        try:
            release_date = i.find_all('div', class_='info')[1].find('span').string
        except AttributeError:
            release_date = '空'

        # 提取电影评分
        score = i.find('p', class_='score m-t-md m-b-n-sm').get_text(strip=True)
        # 抓取封面图片
        images = [img['src'] for img in i.find_all('img', class_='cover')]

        movie_data.append((name, categories, release_date, score, images))

    return movie_data


def save_movie_data_to_excel(movie_data, output_file):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('scrape电影Top100', cell_overwrite_ok=True)
    sheet.write(0, 0, '序号')
    sheet.write(0, 1, '名称')
    sheet.write(0, 2, '分类')
    sheet.write(0, 3, '上映时间')
    sheet.write(0, 4, '评分')

    for n, (name, categories, release_date, score, _) in enumerate(movie_data, start=1):
        sheet.write(n, 0, n)
        sheet.write(n, 1, name)
        sheet.write(n, 2, ', '.join(categories))
        sheet.write(n, 3, release_date)
        sheet.write(n, 4, score)

    book.save(output_file)


def download_images(movie_data, base_path):
    n = 1
    # 下划线 _ 通常被用作一个占位符,这里没有特殊的含义，只是一个临时的变量名，通常用于表示不打算使用的值
    for name, _, _, _, images in movie_data:
        for iurl in images:
            img_data = requests.get(iurl).content
            image_filename = os.path.join(base_path, f'{name}.jpg')
            with open(image_filename, 'wb') as file:
                file.write(img_data)
                print(f"{n}. 正在下载电影 {name} 的封面...")
            n += 1


if __name__ == '__main__':
    output_file = 'scrape电影1.xls'
    movie_data = []

    for page in range(1, 11):
        movie_data.extend(scrape_movie_data(page))

    save_movie_data_to_excel(movie_data, output_file)

    base_path = os.path.join('d:' + os.path.sep, '电影', 'scrape')
    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)
    download_images(movie_data, base_path)
