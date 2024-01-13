#-*- coding:utf-8 -*-
'''
    ch02-demo07-argv.py
    ============================
    python中的命令行参数
'''

# 导入sys内置模块
import sys

# 使用len()函数获取命令行参数的个数
print('命令行参数的个数为 %d 个参数' % (len(sys.argv)))
# 输出命令行参数名称
print('命令行参数的名称为：', sys.argv)
# 输出命令行第2个参数的名称和类型
arg2 = sys.argv[1]
print('命令行第2个参数的名称: {0}, 类型为: {1}'.format(arg2, type(arg2)))
