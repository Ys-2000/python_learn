import scrapy


class MeinvSpider(scrapy.Spider):
    name = "meinv"
    allowed_domains = ["tupianzj.com"]
    start_urls = ["https://www.tupianzj.com/bizhi/DNmeinv/"]

    def start_requests(self):
        url = self.start_urls[0]
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Cookie": "t=01439e9bd540f7144aa7c44649b8e9a3; r=1685; Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1704864241,1705390019; Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1705470447",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        yield scrapy.Request(url=url, headers=headers,callback=self.parse)


    def parse(self, response, **kwargs):
        print(response.body.decode('gbk'))
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
