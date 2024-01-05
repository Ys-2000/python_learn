# import sys,os
# path = r'E:\my\study\bianc\python\Practice\py爬虫\框架\Scrapy框架\practice\tutorial\tutorial'.replace('\\','/')
# sys.path.append(path)
import scrapy
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"         #爬虫的名称
    allowed_domains = ["quotes.toscrape.com"]       # 允许爬取的域名
    start_urls = ["https://quotes.toscrape.com"]    # 起始URl列表

    def parse(self, response):
        quotes = response.css(".quote")
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()               # .extract_first()是Scrapy中的一个方法，用于提取匹配到的第一个元素，如果没有匹配到任何元素，则返回None。
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()                # .extract()方法提取所有匹配的元素
            yield item
        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)        # urljoin()方法将相对URL构造成绝对的URL
        yield scrapy.Request(url=url, callback=self.parse)


