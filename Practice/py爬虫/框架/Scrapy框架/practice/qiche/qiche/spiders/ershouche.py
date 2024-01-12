import scrapy
from scrapy.linkextractors import LinkExtractor

class ErshoucheSpider(scrapy.Spider):
    name = "ershouche"
    allowed_domains = ["che168.com"]
    start_urls = ["https://www.che168.com/jinan/list/?pvareaid=100533"]

    def parse(self, response, **kwargs):
        # 之前的逻辑
        li_list = response.xpath("//ul[@class='viewlist_ul']/li")
        for li in li_list:
            title = li.xpath("./a/div[2]/h4/text()").extract_first()
            href = li.xpath("./a/@href").extract_first()
            print(title, href)
            # scrapy.Request(
            #     url=response.urljoin(href),
            #     callback=self.parse_detail      # parse_detail是详情页解析函数  def parse_detail(self, response, **kwargs):
            # )

        # # 新逻辑
        # le = LinkExtractor
