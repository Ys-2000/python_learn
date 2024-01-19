import scrapy
from scrapy.linkextractors import LinkExtractor

class ErshoucheSpider(scrapy.Spider):
    name = "ershouche"
    allowed_domains = ["che168.com", "autohome.com.cn"]
    start_urls = ["https://www.che168.com/jinan/list/?pvareaid=100533"]
    headers = {
        "Referer": "https://www.che168.com/",
        "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    def parse(self, response, **kwargs):
        # # 之前的逻辑
        # li_list = response.xpath("//ul[@class='viewlist_ul']/li")
        # for li in li_list:
        #     title = li.xpath("./a/div[2]/h4/text()").extract_first()
        #     href = li.xpath("./a/@href").extract_first()
        #     print(title, href)
        #     yield scrapy.Request(
        #         url=response.urljoin(href),
        #         callback=self.parse_detail,      # parse_detail是详情页解析函数  def parse_detail(self, response, **kwargs):
        #         headers=self.headers,
        #     )

        # # 爬取详情页数据 先注释
        # # # scrapy 还提供了链接提取器的东西。也可以帮我们提取到页面中的超链接
        # le = LinkExtractor(restrict_xpaths=("//ul[@class='viewlist_ul']/li/a",))
        # links = le.extract_links(response)  # 提取链接
        # for link in links:
        #     # print(link.text.replace(" ","").strip(),link.url)
        #     yield scrapy.Request(
        #         url=link.url,
        #         headers=self.headers
        #         callback=self.parse_detail,      # parse_detail是详情页解析函数  def parse_detail(self, response, **kwargs):
        #     )
        print(response.url)
        page_le = LinkExtractor(restrict_xpaths=("//div[@id='listpagination']/a",))
        page_links = page_le.extract_links(response)     # 提取分页url
        for page in page_links:
            print(page.url)
            yield scrapy.Request(
                url=page.url,           # 重复的url没关系，scrapy自动的帮我们完成去除重复
                # dont_filter=True,     # 不在调度器的集合中过滤,直接扔到队列里面去,继续发送重复的请求 一般在代理中用到
                callback=self.parse     # 下一页的内容和当前页一致。 然后数据解析的过程和当前页一致
            )

    def parse_detail(self, response, **kwargs):
        print(response.url)
