# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuanBenXiaoshuowangPipeline:
    def __init__(self):
        self.items = []

    def open_spider(self, spider):
        # 在爬虫启动时打开文件
        self.file = open('output.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        # 在 Spider 关闭时对列表按照 chapter_order 排序并输出
        sorted_items = sorted(self.items, key=lambda x: x['chapter_order'])

        for item in sorted_items:
            self.file.write(f"{item['name']}\n{item['details']}\n")
        self.file.close()
