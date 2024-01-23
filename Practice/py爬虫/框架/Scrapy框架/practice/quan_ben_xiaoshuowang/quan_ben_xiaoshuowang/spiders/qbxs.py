import scrapy
from quan_ben_xiaoshuowang.items import QuanBenXiaoshuowangItem
import time,random


class QbxsSpider(scrapy.Spider):
    name = "qbxs"
    allowed_domains = ["xqb5200.com"]
    start_urls = ["https://www.xqb5200.com/38_38021/"]
    # item = QuanBenXiaoshuowangItem()
    def parse(self, response, **kwargs):
        dd_list = response.xpath("//div[@id='list']/dl/dd")[12:]
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "Hm_lvt_dfdb6e2e4cbe6169e47615f0e6c44d3d=1705641085; Hm_lvt_a71b1bc761fe3f26085e79b5fd6a7f71=1705641085; jieqiVisitInfo=jieqiUserLogin%3D1705643099%2CjieqiUserId%3D127425; clickbids=38021,109340; jieqiVisitId=article_articleviews%3D87285%7C38021%7C109340; Hm_lpvt_dfdb6e2e4cbe6169e47615f0e6c44d3d=1705644312; Hm_lpvt_a71b1bc761fe3f26085e79b5fd6a7f71=1705644312",
            "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        for index,dd in enumerate(dd_list):
            # if index % 20 == 0 and index != 0:
            #     # 每爬取20章，
            #     xm = random.uniform(1, 3)
            #     time.sleep(xm)  # 休眠5秒
            #     print(f"程序休眠{xm}秒！！！")
            zjName = dd.xpath("./a/text()").extract_first()
            href = dd.xpath("./a/@href").get()

            item = QuanBenXiaoshuowangItem()
            item['chapter_order'] = index
            item['name'] = zjName      # 存储章节名称
            if index<10:
                # self.item['name'] = zjName      # 存储章节名称
                yield scrapy.Request(
                    url=response.urljoin(href),
                    method="get",
                    headers=headers,
                    callback= self.parse_details,
                    meta={'item': item},  # 将 item 传递给回调函数
                )
            else:
                break


    def parse_details(self,response, **kwargs):
        item = response.meta['item']  # 从 meta 中获取传递的 item 对象
        text_content = response.xpath("//div[@id='content']/text()").extract()
        # 将文本列表合并为字符串
        text = ''.join(text_content)
        item['details'] = text.replace("全本小说网 www.xqb5200.com，最快更新修罗天帝 ！",'')
        yield item
        # self.item['details'] = text.replace("全本小说网 www.xqb5200.com，最快更新修罗天帝 ！",'')
        # yield self.item



