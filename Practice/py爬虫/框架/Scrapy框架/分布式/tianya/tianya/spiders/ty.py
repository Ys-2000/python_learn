import scrapy


class TySpider(scrapy.Spider):
    name = "ty"
    allowed_domains = ["tianya.cn"]
    start_urls = ["https://tianya.cn"]

    def parse(self, response):
        pass
