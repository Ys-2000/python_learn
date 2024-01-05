import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['testdb']       # 选择数据库
collection = db['qwewq']      # 选择数据库集合


# # ~~~插入数据~~~
# data = {"name": '波比', 'bwh': '{ "b": 90, "w": 59, "h": 85}' , 'age': 30}
# collection.insert_one(data)         # 插入一条数据到选择的集合中
#
# data_d = [
#     {"name": '趣第都', 'bwh': '{ "b": 90, "w": 59, "h": 85}' , 'age': 30},
#     {"name": '吉步将', 'bwh': '{ "b": 86, "w": 58, "h": 86}' , 'age': 35},
#     {"name": '萨尼哦', 'bwh': '{ "b": 80, "w": 54, "h": 80}' , 'age': 22},
#     {"name": '西梦流', 'bwh': '{ "b": 85, "w": 56, "h": 86}' , 'age': 22},
#     {"name": '松发其', 'bwh': '{ "b": 88, "w": 57, "h": 86}' , 'age': 28}
# ]
# collection.insert_many(data_d)      # 插入多条数据到选择的集合中


# # ~~~查询数据~~~
# # 查询所有数据
# result = collection.find()    # 查询指定数据，在find中输入查询的数据 例如：collection.find({'name': 'Tom'})
# for item in result:
#     print(item)


# ~~~更新数据~~~
# collection.update_one({'name': '波比'}, {'$set': {'name': '小波','age': 22}})              # 更新一条数据

# data_x = [
# {'name': '趣第都'}, {'$set': {'age': 11}},
# {'name': '吉步将'}, {'$set': {'age': 11}},
# {'name': '萨尼哦'}, {'$set': {'age': 11}},
# ]


# # 定义要更新的条件和更新的内容
# # 定义更新条件
# filter_criteria = {'name':{'$in': ['趣第都', '清步将', '萨尼哦']}}
#
# # 定义更新内容
# update_content ={'$set': {'age': 13}}
# collection.update_many(filter_criteria, update_content)         # 更新多条数据


# ~~~删除数据~~~
# collection.delete_one({'name': '松发其'})              # 删除一条数据
# data_del = {
#     'name':{'$in': ['zhansan', '测试', '小明']}
# }
# collection.delete_many(data_del)                 # 删除多条数据


# 查询所有数据
result = collection.find()    # 查询指定数据，在find中输入查询的数据 例如：collection.find({'name': 'Tom'})
for item in result:
    print(item.get('name', '/'))        # 循环输出name，如果name字段不存在输出"/"





print("操作成功")