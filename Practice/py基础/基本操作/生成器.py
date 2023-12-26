L = [x*x for x in range(10)]
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
g = (x*x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# for _ in g:
#     print(next(g))
print(L)

# def fbn(max):
#     n,a,b = 0,0,1
#     while n<max:
#         yield b
#         a, b = b, a+b
#         n+=1
#     return 'done'
#
# for n in fbn(6):
#     print(n)


# 函数里面有 yield就是一个生成器函数 ，调用生成器函数会生成一个生成器对象，只有对生成器调用next()函数时才真正运行函数本体

# def odd():
#     print('step 1')
#     yield(1)
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
#
#
# g = odd()
#
# print(next(g))
# print(next(g))

