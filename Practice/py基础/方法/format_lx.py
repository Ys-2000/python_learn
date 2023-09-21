# format 函数是一种非常常用的字符串格式化方法，它可以用于将一个字符串中的占位符替换成具体的数值、字符串等内容，从而生成一个新的字符串。





# **基本用法**
name, age = 'John', 30
# 推荐使用 f-string 来进行字符串格式化，这种方法更为简单和高效
print(f"my name is {name},age{age}")
# print('{}, {}, {}'.format('a', 'b', 'c'))
# 如果需要在字符串中使用大括号 {}，可以使用双大括号 {{}} 来转义
# print('My name is {} and I am {{{}}} years old {{}} .'.format(name, age))

# 格式化参数
# {:<n}：左对齐，占用 n 个字符的宽度。     {:>n}：右对齐，占用 n 个字符的宽度。
# {:^n}：居中对齐，占用 n 个字符的宽度。   {:.nf}：保留 n 位小数。    {:,}：千位分隔符。

# # 左对齐，占用 10 个字符的宽度
# print('{:<10} {:<10}'.format('Name', 'Age'))
# print('{:<10} {:<10}'.format('John', 30))
# print('{:<10} {:<10}'.format('Mike', 25))

# 保留 2 位小数
# print('The value of pi is approximately {:.2f}.'.format(3.141592653589793))
# 千位分隔符
# print('The population of China is {:,}.'.format(1400000000))

# **高级格式化方法**

# print('{0}, {2}, {1}'.format('a', 'b', 'c'))            # 通过位置和名称指定参数
# print('{name}, {age}'.format(name='John', age=30))      # 使用名称参数来指定占位符对应的参数

# 使用字典和列表作为参数
mylist = ['John', 30]
print('My name is {0[0]} and I am {0[1]} years old.'.format(mylist))

mydict = {'name': 'John', 'age': 30}
print('My name is {name} and I am {age} years old.'.format(**mydict))

