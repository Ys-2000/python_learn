import mysql.connector

# 连接数据库
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='000000',
    database='test'
)
# 创建游标
cursor = conn.cursor()

# 执行查询
query = "SELECT * FROM user LIMIT 1"
cursor.execute(query)

# 获取查询结果
result = cursor.fetchall()

# 打印结果
if result:
    print("连接成功，并查询到数据:")
    print(result)
else:
    print("连接成功，但没有查询到数据")

# 关闭游标和连接
cursor.close()
conn.close()
