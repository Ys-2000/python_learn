'''
思路:
计算的时候先从第一行开始，为第一行进行一个初始化，初始化为下一行可以选择的值的数目，即当前所能组成的摆动数列的个数。我们初始化dp[1][i] = n - i + 1;
第一行中，令 d[1][j]为：第1个数选择大于等于 j的数的方案总数。
从第二行开始：
​ 奇数行中，令 d[i][j]为：第i个数选择大于等于j的数时的方案总数。
​ 偶数行中，令 d[i][j]为：第i个数选择小于等于j的数时的方案总数。
即从第二行开始，如果行数为偶数行，那么我们当前可能的数目为：dp[i][j] = (dp[i-1][j+1] + dp[i][j-1]) % 10000;,如果为奇数行则：dp[i][j] = (dp[i-1][j-1] + dp[i][j+1]) % 10000;。
​ 然后这样的话，如果我们总的长度为奇数的话，那么就是dp[m][1],如果是偶数，则为dp[m][n]。
'''

ans = 0
m, n = map(int, input().split())
dp = [[0 for _ in range(1024)] for _ in range(1024)]

for i in range(1, n + 1):
    dp[1][i] = n - i + 1

for i in range(2, m + 1):
    if i & 1:
        for j in range(n, 0, -1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i][j + 1]) % 10000

    else:
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j + 1] + dp[i][j - 1]) % 10000

if m & 1:
    ans = dp[m][1]
else:
    ans = dp[m][n]
print(ans)
