import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ErshouSpider(CrawlSpider):        # crawlSpider也继承了spider,从跟上讲ErshouSpider依然是一个Spider
    name = "ershou"
    allowed_domains = ["che168.com", "autohome.com.cn"]
    start_urls = ["https://www.che168.com/jinan/list/?pvareaid=100533"]
    # rule 规则,这里定义了一堆规则,要求必须是元组或列表
    # rule: 规则对象
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ul[@class='viewlist_ul']/li/a"), callback="parse_item", follow=False),    # follow 要不要继续往下循环找, 类似递归 详情页下不需要在找详情页啦
        Rule(LinkExtractor(restrict_xpaths="//div[@id='listpagination']/a"), follow=True), # 根据需要 自由设置collback  # follow 要不要继续往下循环找, 类似递归 分页需要继续找
    )

    def parse_item(self, response):
        # 处理详情页
        title = response.xpath("//div[@class='car-box']/h3/text()").extract_first()
        price = response.xpath("//span[@id='overlayPrice']/text()").extract_first()
        print(title,price)



        # item = {}
        # #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # #item["name"] = response.xpath('//div[@id="name"]').get()
        # #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
