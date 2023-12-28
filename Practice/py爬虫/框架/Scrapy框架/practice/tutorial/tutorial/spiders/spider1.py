import scrapy


class Spider1Spider(scrapy.Spider):
    # spider（爬虫）名称，需要记住，通过名字来启动爬虫：
    name = "spider1"
    # 允许爬取的域名：可更改（限制爬虫，不要爬到其他网站去了）
    allowed_domains = ["www.baidu.com"]
    # 初始request请求：
    start_urls = ["https://www.baidu.com"]

    # 解析方法
    def parse(self, response):
        print(response.text)
