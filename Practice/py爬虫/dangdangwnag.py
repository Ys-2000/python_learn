
"""
# 获取css中Selector解析网页
# 字典写入CSV 先定义writer，包括表头，写入表头，再写入字典
# 学习获得headers，这是一个字典类型的数据
# CSS中::attr(title)获取属性值，::text获取文本  xpath中：@class @获取，text()获取文本 @href获取链接
"""

from requests import get
import csv
from parsel import Selector

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}

# 把列表的元素取出来用for循环
with open('data.csv', 'a', encoding='utf-8-sig', newline='') as f:  # newline:换行写入

    writer = csv.DictWriter(f, fieldnames=["书名", "评论", "作者", "推荐", "出版社", "日期", "链接"])

    writer.writeheader()  # 将字段写入csv格式文件首行

    for i in range(1, 26, 1):

        # url = f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2022-0-1-{i}'
        url = f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-{i}'


        # 获取信息
        response = get(url=url, headers=headers)

        # 把获取的html字符串转换为可解析的对象
        selector = Selector(response.text)

        # 提取所有li标签
        lst = selector.css('.bang_list_mode li')

        for li in lst:
            # 提取标题 .name a --> 定位一个class类名为name下面的a标签
            # 获取a标签里面的属性 a::attr(title)
            title = li.css('.name a::attr(title)').get()  # 获取属性值用attr(标签名)
            # 提取评论
            comment = li.css('.star a::text').get()  # 获取文本用text(标签名)
            # 获取推荐数
            recommend = li.css('.tuijian::text').get()
            # 提取作者信息
            author = li.css('.publisher_info a::attr(title)').get()
            # 提取出版社信息
            press = li.css('div:nth-child(6) a::text').get()
            # 获取出版日期
            date = li.css('.publisher_info span::text').get()
            # 获取网址信息
            href = li.css('.name a::attr(href)').get()

            # print(title,comment,author,recommend,press,date,href)

            dic = {"书名": title,
                   "评论": comment,
                   "作者": author,
                   "推荐": recommend,
                   "出版社": press,
                   "日期": date,
                   "链接": href,
                   }
            writer.writerow(dic)