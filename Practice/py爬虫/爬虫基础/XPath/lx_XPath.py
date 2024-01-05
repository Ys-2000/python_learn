from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

# # 第⼀种⽅式，直接在python代码中解析html字符串
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

#第⼆种⽅式，读取⼀个html⽂件并解析
html = etree.parse('./test.html', etree.HTMLParser())


# result = etree.tostring(html).decode('utf-8')

# result = html.xpath('//*')
# result = html.xpath('//li//text()')[4]              # //text()获取文本
# result = html.xpath('//li/a//text()')               # 选择li节点的所有a⼦节点


# 获得 href 属性为 link4.html 的 a 节点的⽗节点的 class 属性
# result = html.xpath('//a[@href="link4.html"]/../@class')    # result = html.xpath('//a[@href="link4.html"]/parent::*/@class')   # ⽅法⼆

# 文本获取
# result = html.xpath('//li[@class="item-0"]/a/text()')      # html.xpath('//li[@class="item-0"]//text()')  # 第二中方式

# 属性获取
result = html.xpath('//li/a/@href')     # 在xpath语法中，@符号相当于过滤器，可以直接获取节点的属性值：

print(result)

