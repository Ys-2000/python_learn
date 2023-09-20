# import random
#
# random_int = random.randint(1,100)
# f = open('E:/my/study/bianc/python/Practice/test.txt', 'a')         # w是覆盖，a是追加
# f.write('Hello, world!%s\n'%random_int)
#
# # with语句是用于管理资源的一种语法，特别适用于打开文件、数据库连接等需要显式关闭的资源。
# with open('E:/my/study/bianc/python/Practice/test.txt', 'r') as f:
#     # print(f.read(15))
#     for line in f.readlines():
#         print(line.strip()) # 把末尾的'\n'删掉

# try:
#     f = open('E:/my/study/bianc/python/Practice/test.txt', 'r')     # r是读写
#
#     print(f.read())     # read() 一次读取文件的全部内容
# finally:
#     if f:
#         f.close()       # close()关闭文件


# # StringIO
# from io import StringIO
# f = StringIO()
# f.write('hello,world!')
#
# print(f.getvalue())     # getvalue()方法用于获得写入后的str。


# BytesIO
from io import BytesIO
f = BytesIO()
f.write('你好,world!'.encode('utf-8'))

print(f.getvalue())     # getvalue()方法用于获得写入后的str。