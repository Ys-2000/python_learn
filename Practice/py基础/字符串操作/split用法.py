"""
参考：https://blog.csdn.net/wangyuxiang946/article/details/131473964
语法
string.split( str, num)
参数
str ：（可选）指定分隔符，默认为空字符   这里的空字符串包括空格，换行符 \n，制表符 \t
num ：（可选）分割次数，默认 -1，即分割所有
返回值
返回分割后的字符串列表

分隔符的类型
分隔符必须是「字符串类型」或者不指定，否则会报错 TypeError: must be str or None

"""


str1 = 'a-b-c-d'
print(str1.split('-'))  # 不写第二个值时，默认值是 -1，就是从头切到尾的意思
# 指定分隔次数
print(str1.split('-', -3))  # 如果 num 为「负数」，和默认效果相同，也会从头切到尾
print(str1.split('-', 0))  # 如果 num 为 0，表示不切割，即切割0次
print("a-b-c-d切割1次:", str1.split('-', 1))  # 如果 num 为「正数」，则表示切割指定次数次
print("a-b-c-d切割2次:", str1.split('-', 2))

# 指定分隔次数后，可以将返回的结果「赋值」给「多个变量」。当然，变量的个数与分隔结果的个数要相同，数量不同会报错 ValueError: too many values to unpack
# 比如分隔1次，就会分隔成两个字符串，就用两个结果接收。
str3 = 'a b c d'
r1, r2 = str3.split(' ', 1)
print(r1)
print(r2)

# 切割URL
str2 = 'https://blog.csdn.net/wangyuxiang946/article/details/131473964'
print(str2.split('/')[-1])
