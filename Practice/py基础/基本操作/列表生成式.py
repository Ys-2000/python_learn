# # 列表生成式
# print([x*x for x in range(1,11) if x % 2 == 0])
#
# print([m + n for m in 'ABC' for n in 'XYZ'])
#
# import os # 导入os模块，模块的概念后面讲到
# print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录
#
# # 列表生成式可以使用两个变量来生成list：
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# print([k + '=' + v for k, v in d.items()])
#
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])       # 把一个list中所有的字符串变成小写
#
# # 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
# print([x if x % 2 == 0 else -x for x in range(1, 11)])

# 练习
L1 = ['Hello', 'World', 18, 'Apple', None]
# isinstance判断是不是字符串，lower把字符串转换成小写
L2 = [i.lower() for i in L1 if isinstance(i, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

