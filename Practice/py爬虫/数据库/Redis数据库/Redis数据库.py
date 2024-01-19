import redis

# 1) 直连模式
r = redis.Redis(host='127.0.0.1', port=6379, db=1, password='', decode_responses=True)
# decode_responses=True 表示获取到的Redis数据是否需要解码 默认是False  设置后就不需要.decode('utf-8')

r.set('name', '小明')     # 设置键值对
r.set('sex', '男')
r.set('age', 17)

# 查数据
result = r.get('name')
print(result)


# # 获取所有键
# keys = r.keys('*')  # '*' 表示获取所有键，你也可以使用其他匹配模式
# # 逐个获取键值对
# for key in keys:
#     value = r.get(key)
#     print(f"Key: {key.decode('utf-8')}, Value: {value.decode('utf-8')}")        # 输出所有键值对     # 如果设置了 decode_responses=True 就不需要写.decode('utf-8')

# r.delete('age')         # 删除键值对
# r.set('key','value')
#
# # 设置键的过期时间（单位：秒）
# r.expire('key', 60)  # 设置 'key' 在 60 秒后过期
#
# # 检查键是否存在
# exists = r.exists('age')
# print(exists)  # 输出 1（存在）或 0（不存在）
#
# value = r.get('name').decode('utf-8')       # 获取值解码为字符串
#
#
# print(value)
# print(r.keys('*'))

# r.hset('hash_key', 'field', 'value')            # 存储哈希表
# field_value = r.hget('hash_key', 'field')       # 获取哈希表的字段值
# print(field_value)
# r.hdel('hash_key', 'field')                     # 删除哈希表的字段



# # 2) 连接池模式
# #创建连接池并连接到redis，并设置最大连接数量;
# conn_pool = redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=10,password='')
# # 第一个客户端访问
# re_pool1 = redis.Redis(connection_pool=conn_pool)
#
# # 第二个客户端访问
# re_pool2 = redis.Redis(connection_pool=conn_pool)
#
# re_pool1.set('name','qwe')
# re_pool2.set('age',11)
# print(re_pool1.keys('*'))




# import redis
# try:
#     # 创建Redis连接
#     r = redis.Redis(host='127.0.0.1', port=6379)
#
#     # 测试连接
#     response = r.ping()
#     if response:
#         print("成功连接到Redis服务器")
#     else:
#         print("无法连接到Redis服务器")
#
# except redis.exceptions.ConnectionError as e:
#     print("连接错误:", str(e))