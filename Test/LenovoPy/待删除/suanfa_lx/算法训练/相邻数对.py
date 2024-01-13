n = int(input())
ls = list(map(int, input().split()))
s = []
for i in range(len(ls)):
    j = int(ls[i])+1
    k = int(ls[i])-1
    if j in ls:
        s.append((ls[i], j))
    if k in ls:
        s.append((k, ls[i]))


print(int(len(s)/2))
