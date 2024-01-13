# sum = 0
# for i in range(1, 19001):
#     if i % 2 != 0 and i % 5 != 0 and i % 19 != 0:
#         sum = sum + 1
#         print(i)
# print(sum)


# max = 0
#
# for i in range(1, 70045):
#     if 70044 % i == 0 and 113148 % i == 0:
#         max = i
#         print(max)
#
# print(max)

# sum = 1
# num = 1
# for i in range(1,10):
#     num *= 2
#     sum += num
#
# print(sum)


import re


sum = 0
a = int(input())
for i in range(1, a+1):
    x = str(i)
    # print(type(x))

    # if str(i.find(2)) != 0:
    if x.find('2') != 0:
        sum = sum +1
print(sum)