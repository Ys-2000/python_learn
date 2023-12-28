from parsel import Selector


html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''


selector = Selector(text=html)
items = selector.css('.item-0')
# print(len(items), type(items), items)
# items2 = selector.xpath('//li[contains(@class, "item-0")]')
# print(len(items2), type(items), items2)

# for item in items:
#     text = item.xpath('.//text()').get()
#     print(text)

# result = selector.xpath('//li[contains(@class, "item-0")]//text()').get()       # .getall() 提取所有 Selector 的对应内容
# result = selector.css('.item-0 *::text').getall()   # xpath 方法改写成 css 方法

# 提取属性
# result = selector.css('.item-0.active a::attr(href)').get()
# result = selector.xpath('//li[contains(@class, "item-0") and contains(@class, "active")]/a/@href').get()

# print(result)