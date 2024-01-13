#-*- coding:utf-8 -*-
'''
    ch02-demo06-output.py
    ============================
    Python中的标准输出
'''

# 声明一个字符串类型数据
name = 'Teresa'
# 声明一个数字类型数据
age = 12

# 输出方式1
print('姓名: ' + name)
print('年龄: ' , age)
# 同行输出
print('姓名: ' + name, end=' ')
print('年龄：', age)

# 输出方式2
height = 1.68 # 设置一个身高浮点类型数据
print('姓名：%s, 年龄: %d, 身高: %f' %(name, age, height))
print('姓名: %10s, 年龄: %-10d, 身高: %.1f' %(name, age, height))

# 输出方式3
print('姓名: {0}'.format(name))
print('年龄: {0}, 身高: {1}'.format(age, height))
