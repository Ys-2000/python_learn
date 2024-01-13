import scrapy


class ZhipinSpider(scrapy.Spider):
    name = "zhipin"
    allowed_domains = ["zhipin.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=&city=101120100&position=100101"]

    def parse(self, response):
        response.text
