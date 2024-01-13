# for i in range(1, 6):
#     print('*' * i)


# a = 1
# while a <= 5:
#     b = 1
#     while b <= a:
#         print('*', end='')
#         b = b + 1
#     print('')
#     a = a + 1

# a = int(input('请输入分数:'))
#
# if a > 100 or a < 0:
#     print('请输入100以内的数字')
# elif a >= 90:
#     print('A')
# elif a >= 80:
#     print('B')
# elif a >= 60:
#     print('C')
# else:
#     print('D')

for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    #print('d当前字母：',i)
    i = i + 2
    print(i)
