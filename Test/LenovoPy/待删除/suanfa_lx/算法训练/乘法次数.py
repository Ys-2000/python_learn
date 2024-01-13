while True:
    try:
        n = int(input())
        s = []
        res = []
        for i in range(n):
            s.append(int(input()))
        for num in s:
            temp = 0
            while num != 1:
                if num % 2 == 0:  # 偶数，可二分
                    temp += 1
                else:
                    temp += 2
                num = num // 2
            res.append(temp)
        for x in res:
            print(x)
    except:
        break
