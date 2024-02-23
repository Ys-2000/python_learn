import time
import requests
from bs4 import BeautifulSoup
import json
import logging
import csv
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S')


def save_data_to_csv(dic):
    with open("data.csv", "a", encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["分类", "标题", "主播", "热度"])
        # writer = csv.DictWriter(f, fieldnames=data[0].keys() if data else [])
        if os.path.getsize("data.csv") == 0:  # 如果文件为空
            writer.writeheader()  # 写入标题
        # writer.writeheader()        # 将字段写入csv格式文件首行
        writer.writerow(dic)
        logging.info(f"{dic['主播']}--数据保存成功")


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "dy_did=f4cf8872a191a39a5adc9bc400041601; acf_did=f4cf8872a191a39a5adc9bc400041601; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1705132576,1706243552,1706751279; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1706751330",
    "Referer": "https://www.douyu.com/g_LOL",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
def request_json(url):
    resp_json = requests.get(url,headers=headers).json()
    return resp_json


def rq_fl(cate1Name,customClassId):
    params = {
        "shortName": cate1Name,
        "customClassId": customClassId,
        "offset": "0",
        "limit": "200"
    }

    # 分类的URL
    fl_url = "https://www.douyu.com/japi/weblist/apinc/getC2List"      # 分类url

    fl_json = requests.get(fl_url,headers=headers,params=params).json()['data']['list'][:30]    # 控制爬取分类数量  如爬取前30 [:30]
    for lis in fl_json:
        name = lis.get("cname2","")     # 分类的名称  打印测试用
        xuhao = lis.get("cid2","")      # 序号
        # print(name,xuhao)
        logging.info(f"开始爬取--{name}分类")
        rq_data(xuhao)  # 把序号传给rq_data函数去获取数据
        logging.info(f"{name}分类--爬取完成,程序休眠3秒")
        time.sleep(3)



def rq_data(fl):  # 获取第一页直播数据
    url = f"https://www.douyu.com/gapi/rkc/directory/mixList/2_{fl}/1"
    data = request_json(url)['data']    # 获取json数据
    pages = data['pgcnt']  # 页面数
    logging.info("正在获取第1页数据")
    get_data(data)   # 获取第一页数据
    time.sleep(3)
    if pages >= 2:
        for page in range(2,pages+1):
            url2 = f"https://www.douyu.com/gapi/rkc/directory/mixList/2_{fl}/{page}"
            data2 = request_json(url2)['data']  # 获取json数据
            logging.info(f"正在获取第{page}页数据")
            get_data(data2)  # 获取其他页数据
            time.sleep(3)
            break       # 爬取前两页


def get_data(data):     #  获取直播数据
    for i in data['rl']:
        fl = i.get('c2name_display','')  # 分类
        title = i.get('rn','')  # title
        up = i.get('nn','')  # up
        heat = i.get('ol','')  # 热度
        dic = {
            "分类":fl,
            "标题":title,
            "主播":up,
            "热度":heat,
        }
        save_data_to_csv(dic)
        # print(fl, up, title, heat)



def rq_main_fl():
    url = "https://www.douyu.com/directory"
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,"lxml")
    json_data = soup.find("script",attrs={"type":"text/javascript"}).text
    if json_data:
        # 提取 JSON 数据
        start_index = json_data.find('{')
        end_index = json_data.rfind('}') + 1
        json_str = json_data[start_index:end_index]

        # 解析 JSON 数据
        json_obj = json.loads(json_str)

        # 获取 cate1Name 和 customClassId 的值
        first_categories = json_obj.get('firstCategory', [])    # 控制爬取一级目录 如: 爬取前三  [:3]
        for category in first_categories:
            cate1Name = category.get('cate1Name', '')          # 获取分类名称
            customClassId = category.get('customClassId', '')   # 获取分类ID
            # print("分类名称:", cate1Name, "分类ID:", customClassId)
            logging.info(f"开始爬取一级目录--{cate1Name}")
            rq_fl(cate1Name, customClassId)             # 传给rq_fl函数去请求所有的分类
            logging.info(f"一级目录--{cate1Name}--爬取完成,程序休眠5秒")
            time.sleep(5)
            break       # 测试爬取一个分类


def main():
    rq_main_fl()     # 访问斗鱼主页 获取所有和分类名称ID




if __name__ == '__main__':
    main()
