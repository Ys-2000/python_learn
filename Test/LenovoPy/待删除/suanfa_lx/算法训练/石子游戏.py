n = int(input())
stone_list = []
score = 0

for i in range(n):
    stone_list.append(int(input()))

for j in range(n - 1):
    stone_list.sort()
    x = stone_list.pop(-1)
    y = stone_list.pop(-1)
    score += (x + 1) * (y + 1)
    stone_list.append(x + y)

print(score)

