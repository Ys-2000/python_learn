#-*- coding:utf-8 -*-
'''
    ch02-demo08-reginfo.py
    ============================
    实战任务：使用命令行参数完成一个用户的注册

    @copyright: Chinasoft International · ETC
    @author: Alvin
    @date: 2018-04-08 15:43
'''

# 导入sys内置模块
import sys

# 输出命令行参数传入的数据值
print('姓名: ' + sys.argv[1])
print('年龄: ' , int(sys.argv[2]))
print('性别: %s' % sys.argv[3])
print('血型: {0}'.format(sys.argv[4]))
print('身高：%.2f' % float(sys.argv[5]))
print('电话: {0}'.format(sys.argv[6]))
