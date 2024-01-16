# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 注意：管道是默认是不生效的，需要去settings里面去开启管道
class GamePipeline:     # 随便定义一个类
    # process_item()是处理函数的专用方法(定死的)      item:数据     spider:爬虫
    def process_item(self, item, spider):
        print(item)
        print(spider.name)
        return item     # return会传到下一个管道


class NewPipeline:
    def process_item(self, item, spider):
        # print("hello,world!")
        item['test'] = "hello,world!"
        return item     # return会传到下一个管道