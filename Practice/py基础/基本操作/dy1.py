# print('hello','Ys')
# print('1 + 1 =', 1+1)

# num = input('please enter your num:')
# aa = int(num)
#
# if aa >= 10:
#     print(aa)
# else:
#     print('\'您输入的数字+1 =\n', aa+1)

# 把str变为以字节为单位的bytes,字母用ascii,中文用utf-8;
a = 'ABC中文'.encode('utf-8')
# 使用decode方法把字节转换为str,字母用ascii
d = a.decode('utf-8', errors='ignore')

u = len(a)
# # 传入errors='ignore'忽略错误的字节
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8',errors='ignore'))

# 传入errors='ignore'忽略错误的字节


print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % (d, 1000000))
print(f'Hi, {u}, you have {u:.0f}%')

# # 输出%用%%进行转义
# print('%s %%'%'70')