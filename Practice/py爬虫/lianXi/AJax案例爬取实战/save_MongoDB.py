import requests,json,csv
import pymongo

# 连接到 MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
# 选择数据库
db = client["mydatabase"]
# 创建一个集合（也可以理解为表）
collection = db["customers"]


def main(page):
    url = f'https://spa1.scrape.center/api/movie/?limit=10&offset={page}'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    for i in response.json()['results']:
        records = {'ID': i['id'], '名称': i['name'], '类型': i['categories'], '评分': i['score']}
        collection.insert_one(records)      # 插入一条数据
        # collection.insert_many(list)      # 插入多条数据 insert_many()需要传入一个列表[{},{},{},]



if __name__ == '__main__':
    for page in range(0,91,10):
        main(page)
    # main(0)