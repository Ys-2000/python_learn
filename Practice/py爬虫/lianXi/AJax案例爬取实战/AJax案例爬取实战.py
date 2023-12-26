import requests,json,csv
import pymongo


def main(page):
    url = f'https://spa1.scrape.center/api/movie/?limit=10&offset={page}'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    for i in response.json()['results']:
        # movie = i['id'], i['name'], i['categories'],i['score']
        records = {'ID': i['id'], '名称': i['name'], '类型': i['categories'], '评分': i['score']}
        i.get('id')
        # seve(records)
        writer.writerow(records)

def seve(movie):
    with open('data.csv','w',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "名称", "类型", "评分"])
        writer.writeheader()  # 将字段写入csv格式文件首行
        for i in movie:
            line = json.dumps(i, ensure_ascii=False) + '\n' # json.dumps()字典转json
            f.write(line)


with open("scrape.csv", "w", encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["ID", "名称", "类型", "评分"])
    writer.writeheader()        # 将字段写入csv格式文件首行
    if __name__ == '__main__':
        # for page in range(0,91,10):
        #     main()
        main(0)