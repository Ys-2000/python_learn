import scrapy


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["chaojiying.com"]
    start_urls = ["https://www.chaojiying.com/User/"]

    def parse(self, response):
        print(response.text)
