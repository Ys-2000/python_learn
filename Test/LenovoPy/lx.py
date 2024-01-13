# flag = input("是否为会员 是（y）否（n）:")
# money = float(input("请输入购物金额："))
# discount = 1
# if flag == "y":
#     if money >= 200:
#         discount = 0.75
#     else:
#         discount = 0.8
# else:
#     if money >= 100:
#         discount = 0.9
# result = money * discount
# print("实际支付：%.1f" % result)


# def calculate(num1, num2, num3):
#     """
#     定义一个函数，前两个数完成加法运算，然后对第3个数，进行减法；然后调用这个函数\
#     :return:
#     """
#     result = num1 + num2 - num3
#     return result
#
#
# def main():
#     """
#     主入口函数
#     :return:
#     """
#     num1 = int(input("请输入一个数："))
#     num2 = int(input("请输入第二个数："))
#     num3 = int(input("请输入第三个数："))
#     result = calculate(num1, num2, num3)
#     print(str.format("输入三个数分别是{0},{1},{2},结果为{3}", num1, num2, num3, result))
# # 调用主入口函数，实现功能
# main()


# def square_of_sum(lists):
#     """
#     定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。
#     :param lists:数据列表
#     :return:平方和
#     """
#     result = [x**2 for x in lists]  # 列表推导式
#     return sum(result)
#
#
# print(square_of_sum([1, 2, 3, 4]))


# def avg(scores):
#     """
#     求输入成绩列表的平均成绩
#     :param scores: 成绩列表
#     :return: 平均成绩
#     """
#     return sum(scores) / len(scores)
#
#
# def main():
#     """
#     主入口函数
#     :return:
#     """
#
#     scores = []
#     scores.append(float(input("请输入java课的成绩：")))
#     scores.append(float(input("请输入C#课的成绩：")))
#     scores.append(float(input("请输入HTML课的成绩：")))
#     print(str.format("三门课总成绩为{0}，平均分为{1:3.2f}", sum(scores), avg(scores)))
#
#
# main()


# """
# 写一个函数打印一条横线
# """
#
#
# def print_line(num):
#     """
#     打印一条横线
#     :return:
#     """
#
#     print("-" * num)
#
#
# print_line(10)


# def reverse_str(string):
#     """
#     输出一个英文句子，以英文单词反转输出
#     :param string:
#     :return:
#     """
#     temp = string.split()       # split 分割字符串
#     print(temp)
#     temp.reverse()              # reverse  反转字符串
#     print(temp)
#     print(" ".join(temp))       # join 连接字符串
#
#
# reverse_str('I am a girl')

# def get_prime(num):
#     """
#     根据输入的数，求小于等于该数的所有质数
#     :param num:
#     :return:
#     """
#     result = []
#     for i in range(2, num+1):
#         flag = True
#         for j in range(2, i):
#             if i % j == 0:
#                 flag = False
#                 break
#         if flag:
#             result.append(i)
#     return result
#
#
# def main():
#     num = int(input("请输入一个数："))
#     result = get_prime(num)
#     print(result)
#
#
# main()

num=[]

for i in range(2, 100):

   for j in range(2, i):
      if(i%j==0):
        break
   else:
      num.append(i)
print(num)

