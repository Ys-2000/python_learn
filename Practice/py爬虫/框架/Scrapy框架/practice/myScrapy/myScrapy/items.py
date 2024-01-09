# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ZcoolItem(scrapy.Item):
    # 在此处定义项目的字段，例如:
    imgLink = scrapy.Field() # 封面图片链接
    title = scrapy.Field() # 标题
    types = scrapy.Field() # 类型
    vistor = scrapy.Field() # 人气
    comment = scrapy.Field() # 评论数
    likes = scrapy.Field() # 推荐人数
