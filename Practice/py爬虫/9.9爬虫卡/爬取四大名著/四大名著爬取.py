import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from os import makedirs
from os.path import exists,join
import logging


RESULTS_DIR = "./四大名著"      # 存储路径
IDX = 1         # 排序用的
book = None     # 书名

# 配置基本的日志设置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S')

INDEX_URL = "https://www.shicimingju.com/bookmark/sidamingzhu.html"   # 四大名著 url
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def parse_index():          # 主页面解析 # 获取四大名著的url
    response = requests.get(INDEX_URL, headers=headers).content.decode('utf-8')
    souup = BeautifulSoup(response, "lxml")
    div_list = souup.find("div",id="main").find_all("div", class_="book-item")
    for div in div_list:
        href = div.find("a")["href"]
        detail_url = urljoin(INDEX_URL, href)
        yield detail_url


def Crawl_detail(detail_url):
    response = requests.get(detail_url,headers=headers).content.decode('utf-8')
    return response


def parse_detail(detail_response):      # 获取书名和章节url
    soup = BeautifulSoup(detail_response,"lxml")
    book = soup.find("div",id="main_left").find("h1").text.strip()
    li_list = soup.find("div",class_="book-mulu").find("ul").find_all("li")
    logging.info(f"******正在爬取{book}******")
    for li in li_list:
        href = li.find("a")["href"]
        detail_url = urljoin(INDEX_URL, href)
        yield book, detail_url



def parse_chapter(chapter):     # 解析章节
    response = requests.get(chapter, headers=headers).text
    soup = BeautifulSoup(response,"lxml")
    text = soup.find("div",id="main").find("div", class_="card")

    title = text.find("h1").string      # 章节名称
    content = text.find("div",attrs={"class":"chapter_content"}).text    # 内容
    title= title.replace(" ", "_").replace("\t","").replace("\n","").replace("\r","").replace("·","_")
    content = content.replace(" ","")
    return title, content


def seve(IDX,book,title,content):
    book_path = join(RESULTS_DIR,book)
    exists(book_path) or makedirs(book_path)
    file_path = join(book_path,f"{IDX}.{title}.txt")
    with open(file_path, "w" ,encoding="utf-8") as f:
        f.write(title+content)
        logging.info(f"{book}-{title} 爬取完成!")



def main():
    global book
    global IDX
    detail_urls = parse_index()     # 获取4大名著url
    for detail_url in list(detail_urls):
        detail_response = Crawl_detail(detail_url)
        # book, chapter_urls = parse_detail(detail_response)        # 把四大名著链接源代码传进去 获取章节的url
        for book_name, chapter_url in parse_detail(detail_response):
            if book is None:
                book = book_name
            title, content = parse_chapter(chapter_url)     # 把章节url传给函数，返回章节标题与内容
            seve(IDX, book, title, content)         # 保存数据
            IDX += 1    # 计数
            # continue  # TEST

        book = None     # 清空书名
        IDX = 1     # 清空书名
        logging.info(f"{book}爬取完成,程序暂停3秒后继续爬取")
        time.sleep(3)
    logging.info("全部爬取完成,程序退出!")



if __name__ == '__main__':
    main()

