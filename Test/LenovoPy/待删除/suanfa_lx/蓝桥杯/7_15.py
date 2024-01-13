# def aaa(a1,a2):
#     print(a1+"11111"+a2)
# print(aaa(a2="4396",a1="pmp"))

# def aaa(a1="111",a2="222"):
#     print(a1,a2)
# print(aaa(a2="44396ff",a1="\n"))

# def aaa(*a1, a2=11):
#     print("参数的长度是：", len(a1), a2)
#     print("第3个参数是：", a1[2])
#
#
# print(aaa(1, 2, 666, 266, 456, "dadad", 33))

def  hello():
    print("Hello,Fishc")


aaa = hello()
print(aaa)
print(type(aaa))

# def back():
#     return 1,'中国',3.14
#
#
# print(back())

# def aaa(a1,a2):
#     return a1*a2
#
#
# a = float(input("请输入原价："))
# b = float(input("请输入折扣率："))
# c = aaa(a,b)
# print("打折后价格是：",c)


# def f1():
#     x=[5]
#     def f2():
#         x[0]*=x[0]
#         return x[0]
#     return  f2()
#
#
# print(f1())


# def f1():
#     x = 5
#     def f2():
#         nonlocal x
#         x*=x
#         return x
#     return f2()
#
# print(f1())