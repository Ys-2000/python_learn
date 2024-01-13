# 导包
import requests
import time
from bs4 import BeautifulSoup

# 生成含有User-Agent的request_headers
request_headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

# 声明爬取某个指定url页面的数据的方法
def get_info(url):
    # 使用requests 发送指定方法的对指定url的请求，获取返回响应的数据
    web_data = requests.get(url, headers = request_headers)
    html_text = web_data.text
    # 完成解析，解析为 soup 文档格式，可以进行定位
    soup_document = BeautifulSoup(html_text,'lxml')
    # 完成定位
    ranks = soup_document.select('span.pc_temp_num')
    titles = soup_document.select('div.pc_temp_songlist > ul > li > a')
    times = soup_document.select('span.pc_temp_tips_r > span')
    for rank, title, time in zip(ranks, titles, times):
        data = {
            # 内容的提取
            'rank' : rank.get_text().strip(),
            'singer' : title.get_text().split('-')[0].strip(),
            'song' : title.get_text().split('-')[1].strip(),
            'time' : time.get_text().strip()
        }
        print(data)


if __name__ == '__main__':
    # 1. 生成待爬取的所有页面urls list
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1,24)]
    # 2. 遍历每一个 url 完成数据的获取
    for url in urls:
        get_info(url)
        time.sleep(1)