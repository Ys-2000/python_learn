#-*- coding:utf-8 -*-
'''
    ch01-demo03-greeting.py
    ========================
    演示函数编程模式
'''

# 自定义一个打招呼的函数
def greeting(nickname):
    # 输出用户姓名
    print('你好,%s' % nickname)
    pass

# 创建脚本程序入口
if __name__ == '__main__':
    # 调用函数greeting()
    greeting('翠花')