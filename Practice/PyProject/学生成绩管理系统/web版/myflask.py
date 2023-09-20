import flask
from flask import Flask, render_template, request, redirect
import pymysql

# 创建web应用程序
app = Flask(__name__)



def get_conn():
    # 建立与mysql连接
    conn = pymysql.connect(host="localhost", user="root", password="000000", db="web", charset="utf8")
    # c创建游标A
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):  # 关闭模块
    if cursor:
        cursor.close()
    if conn:
        conn.close()



conn, cursor = get_conn()       # 连接数据库创建游标
# 存储登陆用户的名字用户其它网页的显示
users = []



def query(sql, *args):  # 查询模块
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()     # 执行sql
    # conn.commit()             # 查询操作中是不需要执行提交事务的
    close_conn(conn, cursor)    # 关闭数据库和游标
    return res


def get_user(username, password):  # 从数据库中查询用户名和密码
    # 将传递进来的用户名和密码与表中的记录进行比对，以确定是否存在匹配的用户
    sql = "SELECT id FROM sys_user WHERE username = %s AND password = %s"
    res = query(sql,username,password)
    return res


# 写一个函数来处理浏览器发送过的请求，请求到/是自动执行这个函数
@app.route('/')  # 必须加上路由，否则访问和函数没有关联,当访问到127.0.0.1：5000/，执行函数
def index():
    return render_template('login.html')


@app.route('/login', methods=['post'])
def login():
    username = request.form.get('username')  # 接收form表单传参
    password = request.form.get('password')
    res = get_user(username, password)
    if res:
        # return render_template('student.html', msg='登录成功')
        return redirect('/student')
    else:
        return render_template('login.html', msg='登录失败')


@app.route('/student', methods=['GET', "POST"])
def student():
    # login session值
    if flask.session.get("login", "") == '':
        # 用户没有登陆
        print('用户还没有登陆!即将重定向!')
        return flask.redirect('/')
    insert_result = ''
    # 当用户登陆有存储信息时显示用户名,否则为空
    if users:
        for user in users:
            user_info = user
    else:
        user_info = ''
    # 获取显示数据信息
    if flask.request.method == 'GET':
        sql_list = "select * from students_infos"
        cursor.execute(sql_list)
        results = cursor.fetchall()
    if flask.request.method == 'POST':
        # 获取输入的学生信息
        student_id = flask.request.values.get("student_id", "")
        student_class = flask.request.values.get("student_class", "")
        student_name = flask.request.values.get("student_name", "")
        student_sex = flask.request.values.get("student_sex")

        print(student_id, student_class, student_name, student_sex)

        try:
            # 信息存入数据库
            sql = "create table if not exists students_infos(student_id varchar(10) primary key,student_class varchar(100),student_name varchar(32),student_sex VARCHAR(4));"
            cursor.execute(sql)
            sql_1 = "insert into students_infos(student_id, student_class, student_name, student_sex )values(%s,%s,%s,%s)"
            cursor.execute(sql_1, (student_id, student_class, student_name, student_sex))
            insert_result = "成功存入一条学生信息"
            print(insert_result)
        except Exception as err:
            print(err)
            insert_result = "学生信息插入失败"
            print(insert_result)
            pass
        conn.commit()
        # POST方法时显示数据
        sql_list = "select * from students_infos"
        cursor.execute(sql_list)
        results = cursor.fetchall()
    return flask.render_template('student.html', insert_result=insert_result, user_info=user_info, results=results)


if __name__ == '__main__':  # 固定的写法，程序的入口
    app.run()  # 启动应用程序，