"""
一、Python中replace()函数的语法格式:
    str.replace(old, new [, count])

    str 是要执行替换的字符串或字符串变量，各个参数的含义如下：
    old ：str中要被替换的旧字符串。
    new ：用于替换str中的新字符串。
    count ：可选参数，指定 count 后，只有 str 中前 count 个旧字符串old被替换。
    该函数执行完毕后，将生成替换后的字符串。如果原字符串中没有指定的旧字符串，则原样输出
"""

# 简单使用
str1 = "小华喜欢小刚，小刚喜欢小花，小花喜欢小华"
old_str = "喜欢"
new_str = "打了"

res1 = str1.replace("喜欢", "打了")        # 输出：小华打了小刚，小刚打了小花，小花打了小华

# 设置为1，表示替换一次
res2 = str1.replace("喜欢", "打了",1)      # 输出：小华打了小刚，小刚喜欢小花，小花喜欢小华

# #对大小写敏感
str2 = "Python is simple, python is complex, Python is open"
res3 = str2.replace("python", "java")      # 输出：Python is simple, java is complex, Python is open

print(res3)