# 1.使用enumerate()替代range(len())
""" 将list中的负值置为0 """
import sys

data = [1, 2, -3, -4]
# 不推荐的写法：
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0

# 推荐写法：
data = [1, 2, -3, -4]
for idx, num in enumerate(data):        # enumerate返回当前索引和当前项作为一个元组
    if num < 0:
        data[idx] = 0

# 2.使用列表推导式代替原始的for循环
""" 创建一个包含0到9之间所有平方数的列表 """
# 不推荐的写法：
squares = []
for i in range(10):
    squares.append(i*i)

# 推荐写法
# 列表推导式在底层进行了一些优化，所以大多数情况下都可以提高代码的性能，另外，它能将循环、条件和结果合并到一行代码中，减少了代码的数量和嵌套，使得代码更加紧凑且易于阅读
squares = [i*i for i in range(10)]

# 3. 使用集合（Set）存储唯一值
my_list = [1, 2, 1, 2, 3, 4, 5, 6, 7, 7, 7]
my_set = set(my_list)
print(my_set)   # my_set [1, 2, 3, 4, 5, 6, 7]

# 4. 使用双星号语法**合并字典
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged_dict = {**d1, **d2}  #使用双星号语法合并字典时，不会创建额外副本，所以能提高合并效率，并且节省内存。并且还支持同时合并多个字典
print(merged_dict)  # {'a': 1, 'b': 3, 'c': 4}

# 5. 使用内置的sorted()方法对复杂的可迭代对象进行排序
numbers = [4, 2, 8, 1, 5]
sorted_numbers = sorted(numbers)  # 默认升序排序
print(sorted_numbers)  # [1, 2, 4, 5, 8]

words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=len)  # 按字符串长度排序
print(sorted_words)  # ['date', 'apple', 'banana', 'cherry']

# 6. 处理大量数据时使用生成器（Generators）
# 列表推导式
my_list = [i for i in range(10000)]
print(sum(my_list))  # 49995000
print(sys.getsizeof(my_list), 'bytes')  # 87616 字节
# 生成器推导式
my_gen = (i for i in range(10000))
print(sum(my_gen))  # 49995000
print(sys.getsizeof(my_gen), 'bytes')  # 128 字节

# 7. 使用.get()和.setdefault()在字典中定义默认值
my_dict = {'item': 'football', 'price': 10.00}
# count = my_dict['count']  # 引发KeyError!

# 更好的写法：
# 在字典上使用.get()方法并指定默认值, 如果键不可用，它不会引发KeyError，而是返回指定的默认值，如果没有指定，则返回None。
count1 = my_dict.get('count', 0)  # 设置默认值为0

# 8. 使用f-Strings格式化字符串
name = "China"
my_string = f"Hello {name}"
print(my_string)  # Hello China
i = 10
print(f"{i} squared is {i*i}")  # 10 squared is 100
