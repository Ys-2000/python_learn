import json
from selenium import webdriver
from selenium.common.exceptions import TimeoutException     # 超时等待
from selenium.webdriver.common.by import By                 # 路径定位
from selenium.webdriver.support import expected_conditions as EC    # 条件
from selenium.webdriver.support.wait import WebDriverWait           # 等待
import logging
from urllib.parse import urljoin
from os import makedirs
from os.path import exists

# 建立存储目录
RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)    # 如何目录不存在就创建

# 建立完整URL页面链接
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 10

# 设置Chrome无头模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# 开启浏览器，使用Chrom类生成一个webdriver对象并赋值为browser变量
browser = webdriver.Chrome(options=options)
# 显式等待浏览器10S（WebDriverWait对象，配置页面加载的最长等待时间）
wait = WebDriverWait(browser, TIME_OUT)

# 通过爬取方法，对任意URL进行爬取、状态监听以及异常处理
# url： 要爬取的页面url
# condition: 页面加载成功的判断条件，可以是expected_condition中的某一项，如visibility_of_elements_located、visibility_of_element_located等
# locator: 定位器，元组类型，通过配置查询条件和参数来获取列表页所有的电影信息节点
# 配合 WebDriverWait的超时配置，就可以实现10秒的页面加载监听，如果10秒之内配置条件得到满足，否则抛出TimeoutException异常

def scrape_page(url, condition, locator):
    logging.info(f'开始抓取: {url}')
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        # logging.error(f'error occurred while scraping {url}', exc_info=True)
        print(f'抓取时发生错误: {url}')


# 爬取列表页的方法，通过scrape_page方法并传入condition和locator参数完成对列表页的爬取
# visibility_of_all_elements_locate代表所有节点都加载出来才算成功
# 判断加载成功？当页面出现我们想要的内容，就代表加载成功
# 使用Selenium隐式判断条件，如每部电影的信息区块的CSS选择器#index .item
def scrape_index(page):
    url = INDEX_URL.format(page=page)
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '#index .item'))


# 解析列表页，从中提取详情页的URL
# urljoin方法: 补齐是完整的url链接地址
# yield方法： 迭代返回结果
# 通过find_elements(By.CSS_SELECTOR)方法从列表页中提取了所有电影节点，接着遍历这些节点，通过get_attribute方法提取了详情页的href属性值，再用urljoin方法合并成一个完整的URL
def parse_index():
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL, href)


# 爬取详情页并提取对应的信息
# 同样逻辑，判断条件condition传入visibility_of_element_located，即单个元素出现即可
# locator传入(By.TAG_NAME, 'h2')，即h2（电影名称对应这个节点）。
def scrape_detail(url):
    scrape_page(url, condition=EC.visibility_of_element_located,
                locator=(By.TAG_NAME, 'h2'))


# '''
# 解析详情页的方法来提取想要的信息，提取详情页的URL和电影名称、类别、封面、分数和简介等内容
# URL:  链接，直接调用Browser对象的current_url属性即可获取当前页面的URL
# name: 名称，提取h2节点内容的文本即可获取电影名称。使用find_element(By.TAG_NAME, 'h2')提取指定名称对应的节点，然后调用text属性提取节点内容文本，即电影名称
# categories: 类别，通过CSS选择器提取电影类别，对应的CSS选择器为.categories button span。可以使用find_elements(By.CSS_SELECTOR)方法提取CSS选择器对应的多个类别节点，然后遍历这些节点，调用节点的text属性获取节点内部的文本。
# cover： 封面，使用CSS选择器.cover直接获取对应的节点，但由于封面的URL对应的src这个属性，所以这里使用get_attribute方法并传src来提取
# score： 分数，CSS选择为.score。可以使用上面方法，也可以使用方法find_element(By.CLASS_NAME, 'score')，这个方法可以使用class的名称提取节点能达到同样效果，不过传入参数是class名称score而不是.score。提取节点后调用text属性提取节点文本。
# drama： 简介，对应的CSS选择器为.drama p,直接获取简介对应的节点，然后调用text属性提取文本。
# 最后把所有结果构造成一个字典返回。
# '''
def parse_detail():
    url = browser.current_url
    name = browser.find_element(By.TAG_NAME, 'h2').text
    categories = [element.text for element in browser.find_elements(By.CSS_SELECTOR, '.categories button span')]
    cover = browser.find_element(By.CSS_SELECTOR, '.cover').get_attribute('src')
    score = browser.find_element(By.CLASS_NAME, 'score').text
    drama = browser.find_element(By.CSS_SELECTOR, '.drama p').text
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


# 保存数据为JSON文件
def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            # 爬取页面列表
            scrape_index(page)
            # 解析列表页，从中提取详情页的URL列表
            detail_urls = parse_index()
            for detail_url in list(detail_urls):
                # logging.info('get detail url %s', detail_url)
                print(f"获取详细url:{detail_url}")
                # 爬取详情页并提取对应的信息
                scrape_detail(detail_url)
                # # 解析详情页的方法来提取想要的信息，提取详情页的URL和电影名称、类别、封面、分数和简介等内容，返回结果字典模式
                detail_data = parse_detail()
                # logging.info('detail data %s', detail_data)
                print(f"获取详细数据:{detail_data}")
                # 保存数据
                save_data(detail_data)
    finally:
        browser.close()
        browser.quit()


if __name__ == '__main__':
    main()