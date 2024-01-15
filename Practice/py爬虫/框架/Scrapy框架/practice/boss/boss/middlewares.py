# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from boss.request import SeleniumRequest
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
import time

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class BossSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class BossDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        # 用于自定义创建爬虫中间件函数
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        #                        # 执行XXX功能        在什么时间
        crawler.signals.connect(s.spider_close, signal=signals.spider_closed)   # 自定义创建了spider_close函数
        return s

    def process_request(self, request, spider):
        # 所有的请求都会到我这里
        # 需要进行判断，判断出是否需要selenium来处理请求
        # 开始selenum的操作，返回页面源代码组装的response
        # isinstance 判断xxx是不是xxx类型的
        if isinstance(request, SeleniumRequest):
            # selenium来处理请求
            self.web.get(request.url)
            time.sleep(10)  # 等待10s
            # 封装一个响应对象
            page_source = self.web.page_source
            return HtmlResponse(
                url = request.url,
                status = 200,
                body = page_source,
                request = request,
                encoding = "utf-8"
            )
        else:
            return None

    def spider_opened(self, spider):
        self.web = webdriver.Chrome()
        self.web.maximize_window()

    def spider_close(self, spider):     # 在爬虫关闭时自动调用该函数
        self.web.close()
