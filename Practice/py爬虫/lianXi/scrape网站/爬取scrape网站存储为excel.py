import requests, xlwt, os
from bs4 import BeautifulSoup


# 创建EXCEL
book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建一个新的 Excel 工作簿
sheet = book.add_sheet('scrape电影Top100', cell_overwrite_ok=True)  # 创建一个sheet页
sheet.write(0, 0, '序号')
sheet.write(0, 1, '名称')
sheet.write(0, 2, '分类')
sheet.write(0, 3, '时间')
sheet.write(0, 4, '评分')


# 保存
def save_to_excel(n,name, categories, re_data,score):
    sheet.write(n, 0, n)
    sheet.write(n, 1, name)
    sheet.write(n, 2, categories)
    sheet.write(n, 3, re_data)
    sheet.write(n, 4, score)

base_path = os.path.join('d:' + os.path.sep, '电影', 'scrape')

n = 1
for page in range(1,11):
    # 抓取封面、名称、分类、上映时间、评分
    url = f'https://ssr1.scrape.center/page/{page}'
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers).text
    # 指定解析器为lxml，用于解析 HTML 和 XML 文档
    html = BeautifulSoup(response, 'lxml')
    list = html.find(class_='el-col el-col-18 el-col-offset-3').find_all(class_='el-card item m-t is-hover-shadow')
    for i in list:
        # 提取电影名称
        name = i.find(class_='m-b-sm').string
        # 提取电影分类
        categories = [button.text.strip() for button in i.find_all('button', class_='category')]
        # 提取上映时间
        try:
            re_data = i.find_all('div', class_='info')[1].find('span').string
        except AttributeError:
            re_data = '空'
        # 提取电影评分
        # 通过strip = True参数去除文本内容中的前导和尾随空白字符
        score = i.find('p', class_='score m-t-md m-b-n-sm').get_text(strip=True)

        # 抓取封面图片
        img = [img['src'] for img in i.find_all('img',class_='cover')]
        for iurl in img:
            qwe = requests.get(iurl,headers=headers).content
            if not os.path.exists(base_path):
                os.makedirs(base_path, exist_ok=True)
            cc_path = os.path.join(base_path, f'{name}.jpg')
            with open(cc_path, 'wb') as file:
                file.write(qwe)
                print(f"{n}.正在下载电影 {name} 的封面...")
        save_to_excel(n,name,categories,re_data,score)
        n += 1


book.save('scrape电影.xls')

