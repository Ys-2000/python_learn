import requests, uuid,random
from lxml import etree

url = 'https://www.163.com/dy/article/IKN71P0R05198CJN.html'
user_agent_list = [
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
]
USER_AGENT = random.choice(user_agent_list)
headers = {
    'User-Agent': USER_AGENT
}

response = requests.get(url, headers=headers).text
# print(response)
tree = etree.HTML(response)

div = tree.xpath("//div[@class='post_body']")[0]  # 目前不是字符串

# .// 表示在当前标签下查找
srcs = div.xpath(".//img/@src")

for src in srcs:
    # print(src)
    img_name = str(uuid.uuid4()).replace("-", "") + '.jpg'  # 随机取名字
    img_resp = requests.get(src, headers=headers)
    print(img_resp.content)
    with open(img_name, mode='wb') as f:
        f.write(img_resp.content)

