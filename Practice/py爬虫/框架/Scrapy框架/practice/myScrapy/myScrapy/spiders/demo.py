import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["demo.cn"]
    start_urls = ["https://demo.cn"]

    def parse(self, response):
        pass
