# L = (x*x for x in range(10))
# for i in L:
#     print(next(L))

# def fbn(max):
#     n,a,b = 0,0,1
#     while n<max:
#         yield b
#         a,b = b, a+b
#         n+=1
#     return 'done'
#
# for n in fbn(6):
#     print(n)




# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
#
#
# g = odd()
#
# print(next(g))