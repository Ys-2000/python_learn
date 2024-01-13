# n = int(input())
# count = 0
# arr = []
# while n-1 != 0:
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = int(input())
#     for i in range(a, c+1):
#         for j in range(b, d+1):

n = int(input())
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))  # 输入矩阵的两个顶点坐标

for i in range(n):  # 一共有n个矩阵
    for j in range(a[i][0], a[i][2]):  # 顶点横坐标的范围
        for k in range(a[i][1], a[i][3]):  # 顶点纵坐标的范围
            b.append((j, k))  # 记录顶点坐标范围内的坐标

b = set(b)  # 去除重复的坐标
print(len(b))  # 输出列表的长度，即单位面积的个数




