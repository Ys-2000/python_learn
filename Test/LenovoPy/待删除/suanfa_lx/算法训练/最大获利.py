while True:
    try:
        N, M = map(int, input().split())
        A, B, C = [], [], []
        ans = 0
        for i in range(N):
            A.append(list(map(int, input().split())))
        for i in range(N):
            B.append(list(map(int, input().split())))
        for i in range(N):
            C.append(list(map(int, input().split())))   # 完成输入
        for x in range(N):   # 大循环
            temp = []
            res = []
            for y in range(M):
                temp.append(min(A[x][y], B[x][y]))
            for z in range(M):
                res.append(temp[z] * C[x][z])
            ans += max(res)
        print(ans)
    except:
        break
