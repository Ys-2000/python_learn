#-*- coding:utf-8 -*-
'''
    ch02-demo04-notes.py
    ============================
    Python中注释的使用
'''

'''
    函数名称：calcSum
    携带参数：int 参数1, int 参数2
    返回值：int
'''
def calcSum(num1, num2):
    ''' 计算两个数字之和 '''
    # 返回两个数字之和
    return num1 + num2

# 程序入口
if __name__ == '__main__':
    # 调用函数并获取结果
    result = calcSum(10, 20)
    # 输出
    print('结果为:> %d' % result )

