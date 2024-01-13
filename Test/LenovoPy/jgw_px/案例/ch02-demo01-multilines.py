#-*- coding:utf-8 -*-
'''
    ch02-demo01-multilines.py
    ============================
    多行输出显示
'''

# 创建三个变量
num1 = 10
num2 = 20
num3 = 30
# 源代码
# total = num1 + num2 + num3
total = num1 + \
        num2 + \
        num3
# 输出
print('结果为:> %d' % total)

