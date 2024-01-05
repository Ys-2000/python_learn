import requests
from bs4 import BeautifulSoup
import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['testdb']       # 选择数据库
collection = db['QAZXC']      # 选择数据库集合


url = 'https://quotes.toscrape.com/'
while True:
    respomse = requests.get(url=url).text
    bs = BeautifulSoup(respomse, 'lxml')
    qts = bs.find_all(class_ ='col-md-8')[1].find_all(class_ ='quote')
    for qt in qts:
        text = qt.find(class_='text').string
        author = qt.find(class_='author').string
        tags = [tag.string for tag in qt.find(class_='tags').find_all(class_='tag')]     # 列表推导式
        db = {
            'text':text,
            'author':author,
            'tags':tags,
        }
        collection.insert_one(db)
    try:
        next = bs.find(class_ ='next').find('a')['href']
        if next:
            # 检查是否存在下一页，如果有则更新URL，否则停止循环
            url = f'https://quotes.toscrape.com{next}'
    except AttributeError:
        break





# #递归爬取
# def main(url):
#     response = requests.get(url=url).text
#     bs = BeautifulSoup(response, 'lxml')
#     qts = bs.find_all(class_ ='col-md-8')[1].find_all(class_ ='quote')
#     for qt in qts:
#         text = qt.find(class_='text').string
#         author = qt.find(class_='author').string
#         tags = [tag.string for tag in qt.find(class_='tags').find_all(class_='tag')]     # 列表推导式
#         db = {
#             'text':text,
#             'author':author,
#             'tags':tags,
#         }
#         collection.insert_one(db)
#     try:
#         next = bs.find(class_='next').find('a')['href']
#         if next:
#             nexturl = f'https://quotes.toscrape.com{next}'
#     except AttributeError:
#         main(nexturl)
#
# if __name__ == '__main__':
#     url = 'https://quotes.toscrape.com/'
#     main(url)




