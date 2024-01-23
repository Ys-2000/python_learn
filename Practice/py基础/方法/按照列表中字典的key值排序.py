lis = [{"id":"5","name":"xiaom"},{"id":"6","name":"sss"},{"id":"3","name":"bb"}]
sorted_items = sorted(lis, key=lambda x: x['id'], reverse=False)  # reverse=True 表示逆序


print(sorted_items)