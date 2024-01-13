n = int(input())
student_list = list(map(int, input().split()))
aunt_25 = 0
aunt_50 = 0
aunt_100 = 0
flag = 0

for i in range(n):
    if student_list[i] == 25:
        aunt_25 += 1
        continue
    if student_list[i] == 50:
        if aunt_25 >= 1:
            aunt_50 += 1
            aunt_25 -= 1
            continue
        else:
            flag = 1
            break
    if student_list[i] == 100:
        if aunt_50 >= 1 and aunt_25 >= 1:
            aunt_100 += 1
            aunt_50 -= 1
            aunt_25 -= 1
            continue

        elif aunt_25 >= 3:
            aunt_100 += 1
            aunt_25 -= 3
            continue
        else:
            flag = 1
            break
if flag == 1:
    print('NO')
else:
    print('YES')
