import requests, logging

INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

logging.basicConfig(level = logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


# 定义一个爬取列表页的方法
LIMIT = 10
def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)      # 调用scrape_api函数进行爬取列表


# 定义一个通用的爬取方法
def scrape_api(url):
    logging.info('scraping %s...', url)         # 输出要爬取的URL
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # print(response.json())
            return response.json()              # 成功返回json数据
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


# 定义一个详情页的爬取逻辑
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)

# 定义一个总的调用方法
TOTAL_PAGE = 1
def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)             # 调用scrape_index函数，成功返回外层json数据 赋值给变量index_data
        for item in index_data.get('results'):      # 循环外层列表json数据
            # print(item)
            id = item.get('id')                     # 获取外层json列表的 id
            detail_data = scrape_detail(id)         # 调用scrape_detail函数，成功返回外层json数据
            logging.info('detail data %s', detail_data)     # 输出爬取到的结果


if __name__ == '__main__':
    main()