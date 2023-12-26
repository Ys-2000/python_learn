import re

# content ='Hello 123 4567 World_This is a Regex Demo'
# # print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)     # match:必须从字符串开头匹配

'''
^匹配字符串的开头，以Hello开头
\s匹配空白字符，用来匹配目标字符串的空格
\d匹配数字，3个\d匹配 123
再写1个/s匹配空格
后面的4567，依然能用4个\d 来匹配，但是这么写比较烦琐所以后面可以跟{4}代表匹配前面的规则4次，也就是匹配4个数字
后面再紧接1个空白字符，最后\w{10}匹配10个字母及下划线
'''
# print(result)
# print(result.group( ))      # group()方法输出匹配到的内容
# print(result.span( ))     # span()方法可以输出匹配的范围



content_b ='Hello 1234567 World_This is a Regex Demo'
result_b = re.match('^Hello\s(\d+)\sWorld', content_b)
# ()实际上标记了一个子表达式的开始和结束位置 被标记的每个子表达式会依次对应每一个分组 调用group方法传入分组的索引即可获取提取的结果
# print(result_b)
# print(result_b.group())      # group()方法输出匹配到的内容
# print(result_b.group(1))      # group(1)输出第一个被()里的内容
# print(result_b.span())     # span()方法可以输出匹配的范围

result_c = re.match('^Hello.*Demo$', content_b)
# print(result_c)
# print(result_c.group())
# print(result_c.span())     # span()方法可以输出匹配的范围


# result_d = re.match('^He.*(\d+).*Demo$', content_b)     # 输出7 因为在贪婪匹配下.*会匹配所以字符 而\d至少匹配一个字符
# .*是贪婪匹配   尽可能匹配多个字符
# .*？是非贪婪匹配  尽可能匹配少个字符
result_d = re.match('^He.*?(\d+).*Demo$', content_b)
print(result_d.group(1))

# search:查找任意位置的匹配项
# fullmatch:整个字符串与正则完全匹配