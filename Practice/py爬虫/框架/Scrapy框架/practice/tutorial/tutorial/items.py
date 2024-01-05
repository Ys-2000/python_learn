# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuoteItem(scrapy.Item):
    # 采集的目标内容：名言、名人、分类标签
    # 名言：
    text = scrapy.Field()
    # 名人
    author = scrapy.Field()
    # 标签
    tags = scrapy.Field()