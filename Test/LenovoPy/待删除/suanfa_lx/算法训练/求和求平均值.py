def x(n):
    x = sum(n)
    print('{:g}'.format(x))  # 去掉多余尾数0
    print(sum(n)/len(n))


n = [float(i) for i in input().split()]
x(n)
