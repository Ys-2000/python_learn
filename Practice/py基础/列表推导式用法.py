'''
列表推导式（List Comprehensions）是一种简洁的方法来创建和操作列表。它允许你在一行代码中生成新的列表，通常以一种非常可读的方式。
一般的列表推导式结构如: new_list = [expression for item in iterable if condition]
expression: 定义了如何处理每个item，并将结果放入新列表。
item: 可迭代对象（通常是列表、元组、字符串等）中的每个元素。
iterable: 要遍历的可迭代对象。
condition (可选): 一个可选的条件，只有当条件为True时才会包含在新列表中。
# 以下是一些示例
'''
# 1.生成一个由1到10的平方组成的列表：
squares = [x**2 for x in range(1, 11)]
print(squares)          # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 2.从列表中过滤出偶数：

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)            # [2, 4, 6, 8, 10]

# 3.从字符串列表中过滤出长度大于等于5的字符串：
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = [word for word in words if len(word) >= 5]
print(long_words)       # ['apple', 'banana', 'cherry', 'elderberry']

# 4.使用条件表达式处理元素：
# 遍历名为numbers的列表中的每个元素x，如果x是偶数（x % 2 == 0为True），则将x的平方添加到新列表squared_and_even中，否则，直接将x添加到新列表中。
# 在这个示例中，squared_and_even将包含原始列表numbers中每个元素的平方值，但仅对偶数进行了平方操作，奇数元素保持不变。
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_and_even = [x**2 if x % 2 == 0 else x for x in numbers]     # 遍历numbers数组 如果x是偶数 求x的平分 x不是偶数直接输出
print(squared_and_even)
