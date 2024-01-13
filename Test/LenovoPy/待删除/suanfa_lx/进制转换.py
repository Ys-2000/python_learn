N, M, L = input().split(' ')
list1 = input().split(' ')
box = []


def jinzhi(i):
    if M == '10':
        if L == '8':
            return oct(i)
        if L == '2':
            return bin(i)
    if M == '8':
        if L == '10':
            return int(i, 8)
        if L == '2':
            return bin(i)
    if M == '2':
        if L == '10':
            return int(i, 2)
        if L == '8':
            return oct(i)


for i in list1:
    i = int(i)
    box.append(i)
x, y = jinzhi(max(box)), jinzhi(min(box))
print(str(x)[2:], str(y)[2:])
