def YH_tri(row_num):#返回一个杨辉三角的最后一行
    if row_num == 1:
        result = [1]
    else:
        result = [[0 for i in range(0,row_num)]for i in range(0,row_num)]
        for i in range(0,row_num):
            for j in range(0,row_num):
                result[i][0] = 1
                if i == j:
                    result[i][j] = 1
        for x in range(2,row_num):
            for y in range(1,x):
                result[x][y] = result[x-1][y-1] + result[x-1][y]
    return result[row_num-1]

n,Sum = map(int,input().split())
yh_tri = YH_tri(n)      #杨辉三角的最后一行
res = []     #保存最终结果的
used = [0 for i in range(Sum)]        #标记那些数据用过
flag = 0
def dfs(num,temp_sum):      #num是深搜到第几个了，temp_sum是目前的和
    global flag
    if flag == 1:
        return
    if temp_sum > Sum:
        return
    if num == n:
        if temp_sum == Sum:     #说明找到对的了
            for x in res:
                print(x,'',end='')
            flag = 1        #找到了也不能在这直接返回，直接返回会接着搜
        else:
            return

    for i in range(1,n+1):
        if used[i] == 0:
            used[i] = 1     #用过的数字置1
            res.append(i)
            dfs(num+1,temp_sum+yh_tri[num]*i)
            used[i] = 0     #运行到这一步说明上一个数字不行，要恢复置零
            res.pop()

if n == 1:
    print(Sum)
else:
    dfs(0,0)
