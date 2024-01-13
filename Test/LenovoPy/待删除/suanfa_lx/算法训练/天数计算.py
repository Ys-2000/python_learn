# if __name__=="__main__":
#     a=[[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]]
#     year=int(input("请输入需要判断的年："))
#     month = int(input("请输入需要判断的月："))
#     day = int(input("请输入需要判断的日："))
#     sum=0
#     if (year%4==0 and year%100!=0)or year%400==0:
#         for i in range(1,month):
#             sum=sum+a[1][i]
#     else:
#         for i in range(1,month):
#             sum=sum+a[0][i]
#     sum=sum+day
#     print("{}年{}月{}日是这一年的第：{}天".format(year,month,day,sum))


# 用户输入的部分
year, mouth, day = map(int, input().split())

# 月份转化为天数，以平年为准
mouths = (0, 31, 59, 90, 120, 151, 181, 212, 243, 173, 304, 334)
if 0 < mouth <= 12:
    sum1 = mouths[mouth - 1]
else:
    print('输入错误 !')

# 再判断是闰年还是平年
sum1 += day  # 这里sum1 就表示总天数
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    if mouth > 2:
        sum1 += 1

print(sum1)
