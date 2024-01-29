import logging
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
import json
from os import makedirs
from os.path import exists

# 配置基本的日志设置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S')  # 自定义时间格式

# 建立存储目录
RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)    # 如何目录不存在就创建

counter = 1     # 计数

def save_data(data):        # 保存数据为JSON文件
    global counter
    name = data.get('电影名称')
    data_path = f'{RESULTS_DIR}/{counter}.{name}.json'  # 文件名
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    logging.info(f"《{name}》爬取完成!!")
    counter+=1


def request_url(url, condition,locator):     # 请求+显式等待
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.info(f"访问超时: {url}")


def Crawl_index(page):       # 主页面爬取
    url = INDEX_URL.format(page=page)
    request_url(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '#index .item'))


def parse_index():          # 主页面解析
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        detail_url = urljoin(INDEX_URL, href)
        yield detail_url


def Crawl_detail(url):       # 详情页爬取
    logging.info(f"开始爬取: {url}")
    request_url(url, condition=EC.visibility_of_element_located, locator=(By.TAG_NAME, 'h2'))



# 无头模式
options = webdriver.ChromeOptions()
options.add_argument("--headless")

browser = webdriver.Chrome(options=options)
INDEX_URL = "https://spa2.scrape.center/page/{page}"
wait = WebDriverWait(browser, 10)       # 设置显式等待

TOTAL_PAGE = 10     # 总页面数

def main():
    logging.info("程序开始运行!!")
    try:
        for page in range(1, TOTAL_PAGE+1):
            logging.info(f"开始抓取第{page}页数据! \n")
            # 主页面爬取
            Crawl_index(page)

            detail_urls = parse_index()     # 获取详情页URL  返回yield url
            for detail_url in list(detail_urls):
                # 详情页爬取
                Crawl_detail(detail_url)
                # 详情页解析
                detail_data = parse_detail()        # return dic
                # 数据存储
                save_data(detail_data)
    finally:
        logging.info("所有页面爬取完成,程序退出!!")
        browser.close()
        browser.quit()


def parse_detail():     # 详情页解析
    url = browser.current_url
    name = browser.find_element(By.CLASS_NAME,'m-b-sm').text        # 名称
    name_list = name.split(" - ")
    chinese_name = name_list[0].strip()  # 中文名
    english_name = name_list[1].strip()  # 英文名
    categories = [i.text for i in browser.find_elements(By.XPATH,"//div[@class='categories']//button/span")]        # 类型
    diqu = browser.find_element(By.XPATH,"//div[@class='m-v-sm info'][1]/span[1]").text         # 地区
    shiChang = browser.find_element(By.XPATH,"//div[@class='m-v-sm info'][1]/span[3]").text     # 时长
    sysj = browser.find_element(By.XPATH,"//div[@class='m-v-sm info'][2]/span").text            # 上映时间
    score = browser.find_element(By.XPATH,"//p[@class='score m-t-md m-b-n-sm']").text           # 评分
    jianjie = browser.find_element(By.XPATH,"//div[@class='drama']/p").text                     # 简介
    dic = {
        "URL":url,
        "电影名称":chinese_name,
        "英文名称":english_name,
        "类型":categories,
        "地区":diqu,
        "时长":shiChang,
        "上映时间":sysj,
        "评分":score,
        "剧情简介":jianjie,
    }
    return dic


if __name__ == '__main__':
    main()