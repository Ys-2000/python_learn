import scrapy
from caipiao.items import CaipiaoItem


class ShuangseqiuSpider(scrapy.Spider):
    name = "shuangseqiu"
    allowed_domains = ["500.com"]
    start_urls = ["http://datachart.500.com/ssq/"]

    def parse(self, response, **kwargs):
        # scrapy支持xpath和css混用
        trs = response.xpath("//tbody[@id='tdata']/tr")
        for tr in trs:
            # 去除空行,空数据
            if tr.xpath("./@class").extract_first() == 'tdbck':
                continue
            # 去除空行,空数据 方法二    。。有点问题
            # if not tr.css(".chartBall01::text").extract_first():
            #     continue

            qihao = tr.xpath("./td[1]/text()").extract_first().strip()
            red_ball = tr.xpath("./td[@class='chartBall01']/text()").extract()
            blue_ball = tr.xpath("./td[@class='chartBall02']/text()").extract_first()
            # red_ball = tr.css(".chartBall01::text").extract()     # 使用css提取 效果一致
            # blue_ball = tr.css(".chartBall02::text").extract_first()     # 使用css提取 效果一致

            cai = CaipiaoItem()         # 相当于是定义一个字典cai = dict{} ，但是key是在item.py定死了
            cai['qihao'] = qihao
            cai['red_ball'] = red_ball
            cai['blue_ball'] = blue_ball
            yield cai    # 用yield将数据传递给管道pipeline



