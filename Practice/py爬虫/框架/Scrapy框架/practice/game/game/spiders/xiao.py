import scrapy


class XiaoSpider(scrapy.Spider):
    name = "xiao"
    allowed_domains = ["www.4399.com"]
    start_urls = ["https://www.4399.com/flash/"]

    def parse(self, response):
        # txt = response.xpath("//ul[@class='n-game cf']/li/a/b/text()").extract()    # 提取内容
        list = response.xpath("//ul[@class='n-game cf']/li")
        for li in list:
            name = li.xpath("./a/b/text()").extract_first()
            categroy = li.xpath("./em/a/text()").extract_first()
            date = li.xpath("./em/text()").extract_first()

            dic = {
                "name":name,
                "categroy":categroy,
                "date":date
            }
            # 需要用yield将数据传递给管道
            yield dic       # 如果返回的是数据，直接可以认为 是给了管道pipeline


