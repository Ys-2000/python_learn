import requests,uuid
from lxml import etree
url = 'https://www.163.com/dy/article/IKN71P0R05198CJN.html'

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
response = requests.get(url,headers=headers).text

tree = etree.HTML(response)

# //标签[限定]
# //text() 所有文本
# div = tree.xpath("//div[@class='post_body']//text()")
div = tree.xpath("//div[@class='post_body']")[0]    # 目前不是字符串
# 后续操作中需要替换div对应代码中的内容

# 把div还原成代码
div_html = etree.tostring(div,encoding="utf-8").decode("utf-8")
# 对图片进行处理 把图片还原到新闻中去
# 需要拿到每张图片的下载地址。
# .// 表示在当前标签下查找
srcs = div.xpath(".//img/@src")


for src in srcs:
    # print(src)        # 下载地址
    # 下载图片
    # 准备图片存储路径
    img_name = str(uuid.uuid4()).replace("-", "") + ".jpg"  # 随机取名字
    img_resp = requests.get(src, headers=headers).content
    with open(img_name, mode='wb') as f:
        f.write(img_resp)
    print('下载完成！')
    # 每下载一张图片把div中的src替换成本地图片
    div_html = div_html.replace(src, img_name)

# 最后统一存储div的html代码
    with open('xw.md', 'w', encoding='utf-8') as f:
        f.write(div_html)

