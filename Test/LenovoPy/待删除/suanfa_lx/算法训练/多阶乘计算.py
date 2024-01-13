# x = 1
# y = int(input("请输入要计算的数:"))
# for i in range(1, y + 1):
#   x = x * i
# print(x)

def test(n):
  if n == 1:
    return 1
  else:
    return n * test(n - 1)


n = int(input("请输入一个整数："))
sum = 0
for i in range(1, n + 1):
  sum = sum + test(i)
