import scrapy


class MeinvSpider(scrapy.Spider):
    name = "meinv"
    allowed_domains = ["tupianzj.com"]
    start_urls = ["https://www.tupianzj.com/bizhi/DNmeinv/"]

    def parse(self, response, **kwargs):
        li_list = response.xpath("//ul[@class='list_con_box_ul']/li")
        for li in li_list:
            href = li.xpath("./a[@href]").extract_first()
            # 根据Scrapy原理此处应该把href处理成一个请求，交给引擎
            yield scrapy.Request(
                url=response.urljoin(href),      # 把相应中的url和刚刚获取到的url进行拼接
                method="get",
                callback= self.parse_detail     # 回调函数，得到响应结果后 进行处理
            )
            break

    def parse_detail(self, response, **kwargs):
        img_src = response.xpath("//div[@id='bigpic']/a/img/@src").extract_first()
        print(img_src)
