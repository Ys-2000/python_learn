def isTure(i):
    for j in range(n):
        if i != j and vis[j]:
            if (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]) < (r[i] + r[j]) * (r[i] + r[j]):
                return False
    return True


def dfs(step, sum):
    global ans
    if step == n:
        ans = max(ans, sum)
        return
    for i in range(n):
        if vis[i] == 0:
            tmp = r[i]
            if isTure(i) == False:
                r[i] = 0
            vis[i] = 1
            dfs(step + 1, sum + r[i] * r[i])
            vis[i] = 0
            r[i] = tmp


if __name__ == '__main__':
    PI = 3.14
    ans = 0
    x = []
    y = []
    r = []
    n = int(input())
    vis = [0 for _ in range(n)]
    for _ in range(n):
        xt, yt, rt = map(int, input().split())
        x.append(xt)
        y.append(yt)
        r.append(rt)
    dfs(0, 0)

    print(ans)
