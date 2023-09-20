import flask
from flask import request

app = flask.Flask("web")
import pymysql

# 创建一个数据库
def initializeBD():
    res = False
    try:
        # 创建数据的链接对象con
        con = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="001009", db="testdb", charset="utf8")
        # 创建一个字典类型的游标cursor
        cursor = con.cursor(pymysql.cursors.DictCursor)
        # cursor执行SQL命令
        sql = "create table users (user varchar(16) primary key, pwd varchar(16), email varchar(128))"
        cursor.execute(sql)
        # 提交数据库
        con.close()
        res = True
    except Exception as err:
        print(err)
    return res

# 向数据库写入数据
def registerBD(user, pwd, email):
    initializeBD()
    res = False
    try:
        # 创建数据的链接对象con
        con = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="001009", db="testdb", charset="utf8")
        # 创建一个字典类型的游标cursor
        cursor = con.cursor(pymysql.cursors.DictCursor)
        # cursor执行SQL命令
        # sql = "insert into users (user, pwd, email) values ('" + user + "', '" + pwd + "', '" + email + "')"
        # cursor.execute(sql)
        sql = "insert into users (user, pwd, email) values (%s, %s, %s)"
        cursor.execute(sql, [user, pwd, email])
        # 提交数据库
        con.commit()
        con.close()
        res = True
    except Exception as err:
        print(err)
    return res

# 在数据库中查找数据
def readUser(user, pwd):
    try:
        # 创建数据的链接对象con
        con = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="001009", db="testdb", charset="utf8")
        # 创建一个字典类型的游标cursor
        cursor = con.cursor(pymysql.cursors.DictCursor)
        # cursor执行SQL命令
        sql = "select * from users where user='" + user + "'and pwd='" + pwd+"'"
        cursor.execute(sql)
        row = cursor.fetchone()
        # 提交数据库
        con.commit()
        con.close()
        if row:
            return True
        else:
            return False
    except Exception as err:
        return False


@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if flask.request.method == "POST":
        user = flask.request.values.get("user", "")
        pwd = flask.request.values.get("pwd", "")
        if user != "" and pwd != "":
            if readUser(user, pwd):
                msg = user + "登录成功"
            else:
                msg = user + "登录失败"
    return flask.render_template("login.html", msg=msg)


@app.route('/my/blog/<blog_id>')
def blog_detail(blog_id):
    return '您访问的博客是{}'.format(blog_id)


@app.route('/book/list')
def book_detail():
    page = request.args.get('page', default=1, type=int)
    return '你获取的是{}'.format(page)


@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if flask.request.method == "POST":
        user = flask.request.values.get("user", "")
        pwd1 = flask.request.values.get("pwd1", "")
        pwd2 = flask.request.values.get("pwd2", "")
        email = flask.request.values.get("email", "")
        if user != "" and pwd1 != "" and pwd1 == pwd2:
            if registerBD(user, pwd1, email):
                msg = user + "注册成功"
            else:
                msg = "注册失败" + user + "已经存在"
        else:
            msg = "该用户名称与密码不能空，两次密码要一致"
    return flask.render_template("register.html", msg=msg)

app.debug=True
if __name__ == "__main__":
    app.run()

