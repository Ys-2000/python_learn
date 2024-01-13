import math


def set_graph(position):
    graph = {}
    for perent in range(1, n + 1):
        graph[perent] = {}
    for i in range(1, n + 1):
        x1, y1, z1 = position[i]
        for j in range(i + 1, n + 1):
            x2, y2, z2 = position[j]
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) + (z1 - z2) ** 2
            graph[i][j], graph[j][i] = distance, distance
    return graph


n = int(input())
position = {}

for i in range(1, n + 1):
    position[i] = list(map(int, input().split()))

graph = set_graph(position)
yi_chu_li = [1]
ans = 0

while len(yi_chu_li) != n:
    min_distance = []
    for i in yi_chu_li:
        min_distance.append(min(graph[i].values()))
    min_tem = min(min_distance)
    min_index, min_value = min_distance.index(min_tem), min_tem
    for j in graph[yi_chu_li[min_index]]:
        if graph[i][j] == min_value:
            del graph[i][j]
            del graph[j][i]
            break
    yi_chu_li.append(j)
    ans += min_value

print('%.2f' % ans)
