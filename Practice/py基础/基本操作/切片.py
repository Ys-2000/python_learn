# lista = ["ale","jiejie","fofo","uzi","meako"]
#
# print(lista[:3])
# print(lista[-2:])
#
# L = list(range(1,51))
#
# # 元组和字符串都可以进行切片
# T = tuple(range(1,51))
# S = "abcdefg"
# print(T[:20:2])     # 前20个数，每两个取一个
# print(L[::5])       # 所有数，每5个取一个
# print(L[-20:-10])   # 从倒数20个开始取到倒数第10个
# print(L[:])         # 什么都不写，只写[:]就可以原样复制一个list



# 取出字符串的空格  切片+递归
def trim(s):

    if s[:1]!=' ' and s[-1:]!=' ':
        return s
    elif s[:1]==' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])

src = "123asd4156  "
# print(trim(src))
print(src.strip())          # strip()字符串切割
print(src.strip('12'))
print(src[2:6])