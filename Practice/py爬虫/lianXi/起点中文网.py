import requests
from bs4 import BeautifulSoup


# 定义一个通用的爬取方法
def scrape_api(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # print(response.json())
            return response.json()              # 成功返回json数据
        print('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        print('error occurred while scraping %s', url)








def main():
    url = f"https://www.qidian.com/ajax/Free/getSysTime?_csrfToken=8hwWmbEStrilYhovGRFTsyLxTlLHBj5auKvGlzTQ"
    # header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    html = scrape_api(url)
    print(html)








if __name__ == '__main__':
    main()