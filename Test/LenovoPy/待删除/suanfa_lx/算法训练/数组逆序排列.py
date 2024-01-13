old_list = list(map(int, input().split()))

if old_list[-1] == 0:
    del old_list[-1]

if len(old_list) <= 20:
    new_list = []
    for i in range(len(old_list)):
        a = old_list.pop()
        new_list.append(a)
    print(new_list)
