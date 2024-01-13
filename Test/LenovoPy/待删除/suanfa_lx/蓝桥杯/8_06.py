# def jc(n):
#     for i in range(1, n):
#         n = n * i
#
#     return n
#
#
# c = int(input('请输入：'))
# n = jc(c)
# print('%d 的阶乘是 %d' % (c, n))


# g = (x * x for x in range(10))          # 这里用（）是generator生成器 []是list列表
# # print(next(g))                          # next（）查看generator
# for i in g:
#     print(i)


def fib(max):               # 斐波拉契数列
    a, b, c = 0, 0, 1
    while a < max:
        # print(b)
        yield b
        b, c = c, b + c
        a = a + 1
    return 'done'


print(fib(6))