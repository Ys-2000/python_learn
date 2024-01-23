# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuanBenXiaoshuowangItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()               # 章节名称
    details = scrapy.Field()            # 章节内容
    chapter_order = scrapy.Field()      # 章节顺序

