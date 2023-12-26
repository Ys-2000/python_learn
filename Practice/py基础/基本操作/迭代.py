from collections.abc import Iterable
from collections.abc import Iterator

edg = {'ale': 73, 'jiejei': 74, 'fofo': 75, 'uzi': 76, 'mekio': 77}

# # 迭代key
# for key in edg:
#     print(key)

# # 迭代value
# for v in edg.values():
#     print(v)
#
# # 同时迭代key和value
# for key,v in edg.items():       # items()方法 获取字典中的键值对
#     print(key, v)

# # 字符串也可以迭代
# for ch in 'abc':
#     print(ch)


# print(isinstance(edg, Iterable))        # 判断一个对象是不是可迭代对象，记得先导入from collections.abc import Iterable
# print(isinstance('abcd', Iterable))     # 字符串可迭代，返回Ture
# print(isinstance(15332, Iterable))      # 整数不可迭代返回False

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,v in enumerate(['a','b','c']):
    print(i,v)


# b = iter('abcd')   # Iterator判断一个对象是不是迭代器,iter把list、dict、str等Iterable变成Iterator
#
# try:
#     while True:
#         print(next(b))
# except StopIteration:
#     pass

