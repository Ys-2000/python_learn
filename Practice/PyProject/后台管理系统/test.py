from flask import Flask, render_template,request
import mysql.connector


app = Flask(__name__)

# 配置MySQL数据库
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '000000',
    'database': 'web'
}

def connect_db():
    return mysql.connector.connect(**db_config)


def insert():
    name = 'zzz'
    mobile = '123'
    password = '12345'
    conn = connect_db()  # 连接数据库
    cursor = conn.cursor()  # 创建游标
    sql = "INSERT INTO user (name,mobile,password) VALUES (%s,%s,%s)"
    val = (name,mobile,password)
    cursor.execute(sql, val)    # 指定的SQL命令执行在数据库中
    conn.commit()  # 提交事务
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接

if __name__ == '__main__':
    insert()


# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __str__(self):
#         return f"User(username={self.username}, email={self.email})"
#
#
#
# @app.route('/')
# def index():
#     return 'Welcome to the Backend Admin Panel'
#
#
# @app.route('/template/blog/<blog_id>')
# def template(blog_id):
#     uesr = User('lijiajun', 'wy15195382735@163.com')
#     person = {
#         'username': 'zhangsan',
#         'email': 'zhangsan的email'
#     }
#     return render_template('demo.html', blog_id=blog_id,user=uesr, person=person)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
