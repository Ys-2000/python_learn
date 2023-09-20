# for循环

# lista = ["a","b","c","d"]
# for list in lista:
#     print(list)
#
# sum = 0
# for x in range(101):
#     sum = sum+x
# print(sum)

# la = list(range(11))
# la.pop(0)
#
# for x in la:
#     print(x)

# x = 1
# for x in range(1, 10):
#     if x == 6:
#         break
#     print(x)
#     x += 1
# print("END")


# while循环

# 计算100以内的奇数和
# sum = 0
# num = 1
# while num <= 100:
#     if num % 2 != 0:
#         sum += num
#     num += 1
# print(sum)


# s = 0
# r = list(range(1, 11))
#
# # for x in r:
# #     if r[5] == x:
# #         break
# #     print(x)
#
# while True:
#     s += 1
#     if s == 6:
#         break
#     print(s)

# n = 0
# while n < 100:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)

lista = []
# i = 1
# while i <= 10:
#     lista.append(i)
#     i+=2

for i in range(1,11,2):
    lista.append(i)


print(lista)