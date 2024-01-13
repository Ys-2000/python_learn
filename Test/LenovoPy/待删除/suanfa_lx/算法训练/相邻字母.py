# c = input()
# # for i in c:
# # if c >= chr(65) and c <= chr(90):
# a = chr(ord(c) - 1 % 26)
# b = chr(ord(c) + 1 % 26)
# print(a, c, b)


i = input()
a = ""
b = ""
if 'a' <= i <= 'z':  # str是可以直接比较的
    a += chr(ord('a') + ((ord(i) - ord('a')) + 1) % 26)
    b += chr(ord('a') + ((ord(i) - ord('a')) - 1) % 26)
elif 'A' <= i <= 'Z':
    a += chr(ord('A') + ((ord(i) - ord('A')) + 1) % 26)
    b += chr(ord('A') + ((ord(i) - ord('A')) - 1) % 26)
else:
    a += i

print(b, i, a)