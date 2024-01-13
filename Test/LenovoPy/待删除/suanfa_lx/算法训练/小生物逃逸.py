import math  # 用到平方的计算

n, m = map(int, input().split())
sphere = [[0] * 4] * n
creature = [[0] * 3] * m

for i in range(n):
    sphere[i] = input().split()
for j in range(m):
    creature[j] = input().split()

for k in range(m):
    count = 0
    xc = int(creature[k][0])
    yc = int(creature[k][1])
    zc = int(creature[k][2])
    for g in range(n):
        xs = int(sphere[g][0])
        ys = int(sphere[g][1])
        zs = int(sphere[g][2])
        rs = int(sphere[g][3])

        if pow(xs - xc, 2) + pow(ys - yc, 2) + pow(zs - zc, 2) <= pow(rs, 2):
            count += 1
    print(count, end=" ")
