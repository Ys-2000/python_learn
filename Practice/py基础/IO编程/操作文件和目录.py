import os
# print(os.name)        # 查看当前操作系统，Windows返回nt，Linux返回posix
# print(os.environ)     # 查看操作系统中定义的环境变量

# # 查看当前目录的绝对路径
# print(os.path.abspath('.'))
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
# # print(os.path.join('E:/my/study/bianc/python/Practice', 'testdir'))
# # 然后创建一个目录:
# print(os.mkdir('E:/my/study/bianc/python/Practice/testdir'))
# # 删掉一个目录:
# print(os.rmdir('E:/my/study/bianc/python/Practice/testdir'))

# # 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
# print(os.path.split('E:/my/study/bianc/python/Practice/testdir'))
# # 得到文件扩展名
# print(os.path.splitext('E:/my/study/bianc/python/Practice/MySQL连接.py'))

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作

# # 对文件重命名:
# print(os.rename('test.txt', '爬取豆瓣电影Top250.py'))
# # 删除文件
# print(os.remove('爬取豆瓣电影Top250.py'))

a = [x for x in os.listdir('.') if os.path.isdir(x)]
print(a)
