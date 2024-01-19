import requests
import brotli
from bs4 import BeautifulSoup
from urllib.parse import urljoin



def requ(url):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "Hm_lvt_dfdb6e2e4cbe6169e47615f0e6c44d3d=1705641085; Hm_lvt_a71b1bc761fe3f26085e79b5fd6a7f71=1705641085; jieqiVisitInfo=jieqiUserLogin%3D1705643099%2CjieqiUserId%3D127425; clickbids=38021,109340; jieqiVisitId=article_articleviews%3D87285%7C38021%7C109340; Hm_lpvt_dfdb6e2e4cbe6169e47615f0e6c44d3d=1705644312; Hm_lpvt_a71b1bc761fe3f26085e79b5fd6a7f71=1705644312",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
    response = requests.get(url=url, headers=headers)
    # 解压缩Brotli编码的内容
    decompressed_content = brotli.decompress(response.content)
    # 使用GB2312编码解码文本
    text_content = decompressed_content.decode('gb2312', errors='replace')
    return text_content


def chapter_requ(response):
    soup = BeautifulSoup(response, 'lxml')
    text = soup.find("div",id="content").get_text(strip=True)
    print(text)


# 章节页面
main_url = "https://www.xqb5200.com/38_38021/"
text_content = requ(main_url)
soup = BeautifulSoup(text_content, 'lxml')
dl = soup.find("div", id="list").find("dl")
dt_tags = dl.find_all("dt")

if len(dt_tags) > 1:
    for sibling in dt_tags[1].next_siblings:
        if sibling.name == 'dd':
            if sibling.get_text(strip=True):  # 检查dd标签是否为空
                a_tag = sibling.find("a")
                if a_tag:
                    catalog = a_tag.get_text(strip=True)
                    href = a_tag.get('href', "无")
                    next_url = urljoin(main_url, href)
                    next_response = requ(next_url)
                    print(catalog, next_url)
                    chapter_requ(next_response)
                    break
        elif sibling.name == 'dt':
            juan = sibling.get_text(strip=True) if sibling.get_text(strip=True) else ''
            print(juan)



