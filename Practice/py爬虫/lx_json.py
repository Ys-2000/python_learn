import json

# str1 = '''
# [{
#     "na1me": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# }, {
#     "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# '''
# print(str)
# print(type(str))
# data = json.loads(str1)      # 将 JSON 文本字符串转为 JSON 对象
# print(data)
# print(type(data))


# print(data[0]['name'])
# print(data[0].get('name'))       # 建议使用 get 方法，如果键名不存在，不会报错会返回 None。还可以传入第二个参数（即默认值）
# print(data[0].get('age','18'))

# with open('data001.json', encoding='utf-8') as file:
#     str = file.read()
#     data = json.loads(str)
#     print(data)

# 简单写法
# data = json.load(open('data001.json', encoding='utf-8'))    # .load将JSON文本字符串转为JSON对象
# print(data)
# with open('data001.json', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(data, indent=2, ensure_ascii=False))




# json读取
# with open("data001.json",encoding="utf-8") as file:
#     str = file.read()           # 读取json文件
#     data = json.loads(str)      # 将字符串转换为列表
#     qwe = json.dumps(data)      # 调用dumps方法将JSON对象转化为字符串
# # json读取简单写法
data = json.load(open('data001.json', encoding="utf-8"))
# print(data)

# json写入
# with open('data001.json','w', encoding='utf-8',) as file:
#     file.write(json.dumps(data))    # 调用dumps方法将JSON对象转化为字符串

# json写入简单写法
a = json.dump(data, open('data001.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)










