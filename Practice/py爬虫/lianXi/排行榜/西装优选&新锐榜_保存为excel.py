import requests,random,xlwt

# 如何访问失败，可能需要尝试用浏览器访问：https://www.chinapp.com/paihang/xz

# 创建EXCEL
book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建一个新的 Excel 工作簿
sheet_a = book.add_sheet('优选榜', cell_overwrite_ok=True)  # 创建一个sheet页
sheet_a.write(0, 0, '排名')
sheet_a.write(0, 1, '名称')
sheet_a.write(0, 2, '公司名称')
sheet_a.write(0, 3, '品牌介绍')

sheet_b = book.add_sheet('新锐榜', cell_overwrite_ok=True)  # 创建一个sheet页
sheet_b.write(0, 0, '排名')
sheet_b.write(0, 1, '名称')
sheet_b.write(0, 2, '公司名称')
sheet_b.write(0, 3, '品牌介绍')

def save_to_excel(sheet,n,sort,title,company,description):
    sheet.write(n, 0, sort)
    sheet.write(n, 1, title)
    sheet.write(n, 2, company)
    sheet.write(n, 3, description)

def main():
    # favor 优选榜     acute 新锐榜
    list = ['favor', 'acute']
    for i in list:
        qwe(i)
        print('=' * 99)
    book.save('西装优选&新锐榜.xls')

def qwe(list):
    url = 'https://www.chinapp.com/paihang/getList'     # POST传参
    # favor 优选榜     acute 新锐榜
    payload = {'fid': '1065', 'votetype': f'{list}'}
    if payload['votetype'] == 'favor':
        print('***优选榜***')
    if payload['votetype'] == 'acute':
        print('***新锐榜***')
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
    ]
    header = {
        'User-Agent': random.choice(user_agent_list)
    }
    response = requests.post(url, headers=header,data=payload).json()['data']['listinfo']
    for i in response:
        sort = i['sort']                        # 排名
        title = i['title']                      # 名称
        company = i['company']                  # 公司名称
        description = i['description']          # 品牌介绍
        print(sort, title, company, description)
        n = sort
        # save_to_excel(sheet_a,n,sort,title,company,description)
        if payload['votetype'] == 'favor':
            save_to_excel(sheet_a,n,sort,title,company,description)
        elif payload['votetype'] == 'acute':
            save_to_excel(sheet_b,n,sort,title,company,description)











if __name__ == '__main__':
    main()

