#-*- coding:utf-8 -*-
'''
    ch02-demo09-string.py
    ============================
    字符串类型的截取

    @copyright: Chinasoft International · ETC
    @author: Alvin
    @date: 2018-04-08 15:43
'''

# 创建一个字符串对象
s = 'Hello Python!'

# 输出
print('%s' % s)       # 输出完整的字符串
print('%s' % s[0])    # 输出字符串中的第1个字符
print('%s' % s[2:5])  # 输出字符串第3个元素至第5个元素
print('%s' % s[6:])   # 输出从第6个元素开始到结束
print('%s' % s[6::2]) # 输出从第6个元素开始间隔2个元素至结束
print('%s' % s[-1])   # 输出最后一个元素
print(s * 2)          # 输出两次字符串
print(s + 'let`s go') # 字符串连接
print('\a')
