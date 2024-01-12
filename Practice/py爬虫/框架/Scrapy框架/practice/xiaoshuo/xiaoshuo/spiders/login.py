import scrapy


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["17k.com"]
    start_urls = ["https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"]

    def start_requests(self):
        # # 方案一: 直接从浏览器复制cookie信息
        # dic = {}
        # cookie = """
        # GUID=6af04b03-3f41-4168-a1ca-ced5f52d862e; sajssdk_2015_cross_new_user=1; acw_sc__v2=659f61392208ddc22c8735bfb41febdeb8de3c65; Hm_lvt_9793f42b498361373512340937deb2a0=1704943931; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F10%252F30%252F91%252F102849130.jpg-88x88%253Fv%253D1704944063470%26id%3D102849130%26nickname%3D%25E4%25B9%25A6%25E5%258F%258B833R9043b%26e%3D1720496063%26s%3D92129a48a2295771; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22102849130%22%2C%22%24device_id%22%3A%2218cf6637530843-0fe3c266204cae-26001951-2073600-18cf6637531d26%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%226af04b03-3f41-4168-a1ca-ced5f52d862e%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1704944070; ssxmod_itna=eq0xcDg7D=K7qDK40Lc7tDyDHAc4RxxiIQqQtQD/KtxnqD=GFDK40EogP4AErArKmmrpiDuGheeFbFtiE3eNa6j5+oDU4i8DCuBA3TDem=D5xGoDPxDeDADYoUDAqiOD7qDdLwHyzkDbxi3LxDbDin8pxGCDeKD0xwFDQKDu6IxKxhkiDDziloeN=0Yq8AF3bvmROmhqQ08D75pDlpxufEwn8deSOYLUKA3px0kqq0O9ryzCooDUBKsyPANdARYdQrNwihxj7WxzDhrtGZYp7ntNrhr7+DxtQ/N7Q2oHDxDigUNaYD==; ssxmod_itna2=eq0xcDg7D=K7qDK40Lc7tDyDHAc4RxxiIQqQtG9b5KiDBL10D7pP44SFB9lhP8KRl8W=DuiknGHFn=0KhHQnpkejrnDn4Fpdu/QkK1tzZch9rYcWUe82LyIdLrYwOw1/OBwfvaYa9DuhvGuhu/RYjR0LKnRxjKYmRD3jmGOt6DfpRi8LmKh=6ifmHSMoq4ZdvbaTRW6bBSWNHxuvhlnN1UPQ4ouW1da51QRymnOh7Qz=UD/ocYqbGLMWY4/Wis88Wv9USGCAvnQ3jnkk8WkYXMFgnPKUjcx4Wa18iEyUHoCH8IU1aoZzGTdhqKc0TLrQ5mQ6D==MiSwY7O8dexqjO0kDmohiewzYOcOYvEs2At8wmlq7aCm+e7YO+sQoFDIqDkAl5uWGXnNOiQKYb2k5dxwsGYFQwQrWDTt63KGx12DNZSmffDXip9rNDb+SDa7CHmB7CPxi7eGSH5PHf2YT4=iQdW4eC6QnnrSgFFOGi7mkohrGKH4XOgrnBFK0GnlkTfNYB=U+balxEDDw=44B+TbTwWrrmeduq4pI=H2QGDDjKDeL86D4euxYwjrAEo7KOiDD
        # """
        # lst = cookie.split("; ")
        # for i in lst:
        #     k, v = i.split("=", 1)
        #     dic[k.strip()] = v.strip()
        #
        # yield scrapy.Request(
        #     url = self.start_urls[0],
        #     cookies= dic,
        # )

        # 方案二: 走登录流程
        url = "https://passport.17k.com/ck/user/login"
        loginName = "18264033257"
        password = "Ys204476"
        yield scrapy.Request(
            url = url,
            method= "post",
            body=f"loginName={loginName}&password={password}",
            callback=self.parse
        )


    def parse(self, response, **kwargs):
        # 发送post请求的第一个方案(不好)
        yield scrapy.Request(
            url=LoginSpider.start_urls[0],
            callback=self.parse_detail
        )


    def parse_detail(self, response):
        print(response.text)

