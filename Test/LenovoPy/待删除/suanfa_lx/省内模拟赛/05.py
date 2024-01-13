s = input()
t = ""
for c in s:
    if 'a' <= c <= 'z':  # str是可以直接比较的
        t += chr(ord('a') + ((ord(c) - ord('a')) + 3) % 26)
    elif 'A' <= c <= 'Z':
        t += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
    else:
        t += c
print(t)

# ans = ""
# strq = list(input())
# for i in range(len(strq)):
#     if 97 <= ord(strq[i]) <= 119:
#         strq[i] = chr(ord(strq[i]) + 3)
#     else:
#         strq[i] = chr(ord(strq[i]) - 120 + 97)
# for i in range(len(strq)):
#     ans += strq[i]
# print(ans)

