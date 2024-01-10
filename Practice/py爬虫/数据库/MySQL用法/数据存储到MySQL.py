import pymysql

# 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
db = pymysql.connect(
    host='localhost',
    user='root',
    password='000000',
    database='avidol',
    port=3306,   # 默认 MySQL 端口是 3306
)

# 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
# 创建游标
cursor = db.cursor()

# # 创建一张数据表
# sql = "create table beautyGirls (name char(20) not null, age int)"

# 插入一条记录
sql = "insert into beautyGirls(name, age) values ('张三', 12)"

# # 删除一条记录
# sql = "delete from beautyGirls where age = '%d'" % (18)

try:
    cursor.execute(sql)     # 执行sql

    db.commit()  # 提交事务
except:
    # 回滚
    db.rollback()

# 最后我们关闭这个数据库的连接

cursor.close()      # 关闭游标
db.close()          # 关闭数据库