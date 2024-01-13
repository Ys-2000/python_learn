#-*- coding:utf-8 -*-
'''
    ch01-demo04-showtime.py
    ========================
    演示面向对象编程模式-格式化输出时间
'''

# 导入时间模块
import time

# 自定义类
class TimeUtils:

    # 自定义类成员方法格式化输出时间
    def showTime(self):
        # 创建变量获取系统当前时间
        currentDate = time.strftime('%Y-%m-%d', time.localtime())
        # 输出
        print('当前日期：', currentDate)
        pass

# 创建程序入口
if __name__ == '__main__':
    # 创建一个对象
    obj = TimeUtils()
    # 调用类成员方法
    obj.showTime()