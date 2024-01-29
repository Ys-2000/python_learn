
# 按照列表中字典的key值排序
lis = [{"id":"5","name":"xiaom"},{"id":"6","name":"sss"},{"id":"3","name":"bb"}]
sorted_items = sorted(lis, key=lambda x: x['id'], reverse=False)  # reverse=True 表示逆序
print(sorted_items)







# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)) # lower()将字符串中的所有大写字母转换为小写字母


# # 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
#
# # 请用sorted()对上述列表分别按名字排序：
# def by_name(t):
#     return t[0]
# L2 = sorted(L, key=by_name, reverse=False)
# print(L2)
#
#
# # 再按成绩从高到低排序
# L3 = sorted(L2, key=lambda x: -x[1])
# print(L3)
