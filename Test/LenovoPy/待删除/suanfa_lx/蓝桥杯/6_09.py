
# sum = 0
# for i in range(10000, 99999):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#
#         if str(i) == str(i)[::-1]:
#             sum += 1
# print(sum)


# sum = 0
# for i in range(21, 51):
#     if i % 2 != 0:
#         sum += 1
# print(sum)

# 立方尾不变
sum = 0
for i in range(1, 10001):
    if str(i*i*i) == str(i)[-1:]:
        sum+=1
print(sum)