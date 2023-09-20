# def plus(a, b):
#     return a + b
#
#
# def compose(func, array):
#     return func(array[0], array[1])
#
# # 把函数plus当成变量传给compose
# result = compose(plus, [1, 2])
# print(result)
#
#
# # plus(a, b) 函数接受两个参数 a 和 b，然后返回它们的和。
# # compose(func, array) 函数接受一个函数 func 和一个包含两个元素的列表 array。它将列表中的前两个元素作为参数传递给函数 func 并返回结果。
# # 在主程序中，你调用 compose(plus, [1, 2])，它会将函数 plus 和列表 [1, 2] 传递给 compose 函数。compose 函数将调用 plus(1, 2) 并返回结果 3。

# def f(x):
#     return x * x
#
#
# # map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# # Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
# print(list(r))
# # try:
# #     while True:
# #         print(next(r))
# # except StopIteration:
# #     pass
#
# # list所有数字转为字符串
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# # reduce用法
# from functools import reduce
#
#
# def fn(x, y):
#    return x * 10 + y
#
#
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
#
# a = reduce(fn, map(char2num, '13579'))
# print(a)


# #练习 接受一个list并利用reduce()求积
# from functools import reduce
# def prod(L):
#     def f(x,y):
#         return x*y
#     return  reduce(f,L)
#
#     # return reduce(lambda x, y: x * y, L)      #方法二用lambda表达式
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')


# # 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# from functools import reduce
#
#
# def str2float(s):
#     # 将字符串按小数点分割成整数部分和小数部分
#     parts = s.split('.')
#     # 将整数部分和小数部分分别转换为数字
#     integer = reduce(lambda x, y: x * 10 + y, map(int, parts[0]))
#     decimal = reduce(lambda x, y: x * 10 + y, map(int, parts[1])) / (10 ** len(parts[1]))
#     # 返回整数部分和小数部分的和
#     return integer + decimal
#
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')


# # 回文数
# def is_palindrome(n):
#
#     return n == int(str(n)[::-1])
#
#
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')


# sorted函数应用
a = sorted([36, 5, -12, 9, -21], key=abs,reverse=True)
s = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)

# 练习  假设我们用一组tuple表示学生名字和成绩 请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    # t[0]按照名称排序，t[1]按照成绩排序 ，倒序添加参数：reverse=True
    return t[1]     # -t[1]可进行倒序


L2 = sorted(L,key=by_name)
print(L2)


