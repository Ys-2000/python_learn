import requests
from scrapy import Selector

url = 'https://quotes.toscrape.com/'

response = requests.get(url=url).text
selector = Selector(text=response)

# # css用法
# quotes = selector.css('.quote')
# for quote in quotes:
#     text = quote.css('.text::text').extract_first()
#     author = quote.css('.author::text').extract_first()
#     tags = quote.css('.tags .tag::text').extract()
#     print(tags)


# xpath用法
quotes = selector.xpath('//div[@class="quote"]')
for quote in quotes:
    text = quote.xpath('.//span[@class="text"]/text()').extract_first()
    author = quote.xpath('.//small[@class="author"]/text()').extract_first()
    tags = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
    print(text, author, tags)
