import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["demo.cn"]       # 允许的域名
    start_urls = ["http://demo.cn"]     # 起始页

    def parse(self, response):      # 该方法默认是用来处理解析的
        print(response)
