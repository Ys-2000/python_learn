# import requests
# from bs4 import BeautifulSoup
#
# url = "http://62.234.17.32/font/cp1/index.html"
# response = requests.get(url).text
# soup = BeautifulSoup(response,"lxml")
# print(soup)
#

import requests
from lxml import html
from fontTools.ttLib import TTFont

url = "http://62.234.17.32/font/cp1/index.html"
response = requests.get(url).text
parsed_html = html.fromstring(response)

# 提取加密的字符
# encrypted_characters = parsed_html.xpath('//svgmtsi/text()')

# # 获取字体文件链接
# font_url = parsed_html.xpath('//link[@rel="stylesheet"]/@href')[0]
# font_response = requests.get(font_url)
#
# # 保存字体文件
# with open('font1.woff', 'wb') as font_file:
#     font_file.write(font_response.content)

# 解析字体文件
font = TTFont('ae0f8407.woff')
font.saveXML('font.xml')

# fonta = font.getBestCmap()      # 以字典的方式返回woff
# print(fonta)

# # 获取字体映射关系
# font_mapping = {}
# for i, char in enumerate(encrypted_characters):
#     font_mapping[char] = font.getBestCmap()[font.getGlyphID(ord(char))]
#
# # 替换加密字符为实际字符
# decrypted_text = ''.join([chr(font_mapping[char]) for char in encrypted_characters])
#
# print(decrypted_text)
