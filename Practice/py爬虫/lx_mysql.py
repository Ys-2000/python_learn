import pymysql

# id = '20120002'
# user = 'Bob'
# age = 22
# db = pymysql.connect(host='localhost',user='root', password='000000', port=3306, db='spiders')
# cursor = db.cursor()                    # 创建游标
# # cursor.execute('SELECT VERSION()')      # execute 方法执行
# # data = cursor.fetchone()                # fetchone 方法获得第一条数据
# # print('Database version:', data)
# # 新增
# # sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
#
# # 修改
# sql = 'UPDATE students SET age = %ss WHERE name = %s'
# try:
#     cursor.execute(sql, (25, 'Bob'))       # execute 方法执行
#     print('成功')
#     db.commit()                             # commit 方法执行
# except:
#     print('失败')
#     db.rollback()                           # 回滚事务
# db.close()


# 动态插入
db = pymysql.connect(host='localhost',user='root', password='000000', port=3306, db='spiders')
cursor = db.cursor()
data = {
    'id': '20120002',
    'name': 'xx',
    'age': 31,
}
table = 'students'
keys = ', '.join(data.keys())       # 将字典中的键（字段名）连接成一个字符串，用于构建 SQL 语句中的字段部分。
values = ', '.join(['%s'] * len(data))  # 创建了一个包含相同数量占位符 %s 的字符串，用于构建 SQL 语句中的值部分
# # 新增sql
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# try:
#    if cursor.execute(sql, tuple(data.values())):
#        print('Successful')
#        db.commit()
# except:
#     print('Failed')
#     db.rollback()

# # 修改sql
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
# update = ','.join(["{key} = %s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values())*2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()

# # 删除sql
# condition = 'age < 10'
# sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     print('Successful')
#     db.commit()
# except:
#     print('Failed')
#     db.rollback()

# 查询sql
sql = 'SELECT * FROM students WHERE age >= 20'

# try:
#     cursor.execute(sql)
#     print('Count:', cursor.rowcount)    # 获取查询结果的条数
#     # print('One:', cursor.fetchone())    # fetchone获取结果的第一条数据，返回结果是元组形式
#     results = cursor.fetchall()         # fetchall得到结果的所有数据。然后将其结果和类型打印出来，它是二重元组，每个元素都是一条记录，我们将其遍历输出出来。
#     print('Results:', results)
#     print('Results Type:', type(results))
#     for row in results:
#         print(row)
# except:
#     print('Error')

# 查询sql 使用fetchone()循环获取
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)        # 获取查询结果的条数
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
db.close()