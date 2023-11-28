import csv
import requests

def main():
    url = 'https://game.gtimg.cn/images/lol/act/jkzlk/js//10/10.3.23-S11/hex.js'
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    response = requests.get(url,headers=headers).json()
    data  = response['data']
    # print(data)
    for i in data:
        id = data[i]['id']
        name = data[i]['name']
        desc = data[i]['desc']
        print(id+'---'+name+'---'+desc)
        dic = {"id": id,
               "名称": name,
               "介绍": desc,
               }
        writer.writerow(dic)


with open('s10强化铭文.csv','w',encoding='utf-8', newline='') as f:  # newline换行
    writer = csv.DictWriter(f, fieldnames=["id", "名称", "介绍",])
    writer.writeheader()  # 将字段写入csv格式文件首行
    if __name__ == '__main__':
        main()