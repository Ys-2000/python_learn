# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0 :
#         return x
#     else:
#         return -x
#
# print(my_abs("asd"))


# def power(x, n=2):
#     if n != 0:
#         s = 1
#         while n > 0:
#             n = n - 1
#             s = s * x
#         return s
#     else:
#         return "输入错误"
#
#
# print(power(2,1))

# 定义一个空的函数
# def nop():
#     pass        # pass可以用来作为占位符

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# print(add_end())

# 可变参数
# 1个*是可变参数,**关键字参数
# def calc(*numbers):
#     sum = 0
#     num = 1
#     for n in numbers:
#         sum = sum + n * n       # 参选1*参数1+参数2*参数2...
#         num = num*n             # 参数1*参数2*参数3...
#     return sum, num
#
#
# b = [1,2,3,4,5]
# print(calc(*b))     # 加*解包,把列表b中的参数依次传入







# # 关键字参数   关键字参数通过参数名来传递值 传参方式--参数名称=值
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
# edg = {'ale':'18','jiejie':'12','fofo':'21',}
# person("xiaoming", 18, ale=edg['ale'],uzi=edg['fofo'])
# person("xiaoming", 18, **edg)

# # 命名关键字参数
# def person(name, age, *, city='beijing', job='wensa'):        # * 表示从这个位置开始，后面的参数都被视为强制使用关键字传递，即必须通过参数名来传递值。
#     print(name, age, city, job)
#
#
# person('Jack', 24, city='Beijing00', job='11Engineer')