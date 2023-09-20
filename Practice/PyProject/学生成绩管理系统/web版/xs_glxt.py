from flask import Flask, render_template, request, redirect
import pymysql,flask,re,secrets

# 初始化
app = flask.Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)  # 生成一个32字节的 URL 安全随机字符串作为密钥
# 使用pymysql.connect方法连接本地mysql数据库
db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='000000', database='web', charset='utf8')
# 操作数据库，获取db下的cursor对象
cursor = db.cursor()
# 存储登陆用户的名字用户其它网页的显示
users = []


@app.route("/", methods=["GET", "POST"])
def login():
    # 增加会话保护机制(未登陆前login的session值为空)
    flask.session['login'] = ''
    if flask.request.method == 'POST':
        user = flask.request.values.get("username", "")
        pwd = flask.request.values.get("password", "")

        # 利用正则表达式进行输入判断
        result_user = re.search(r"^[a-zA-Z]+$", user)  # 限制用户名为全字母
        result_pwd = re.search(r"^[a-zA-Z\d]+$", pwd)  # 限制密码为 字母和数字的组合
        if result_user != None and result_pwd != None:  # 验证通过
            msg = '用户名或密码错误'
            # 正则验证通过后与数据库中数据进行比较
            sql1 = "select * from sys_user where username='" + \
                   user + " ' and password='" + pwd + "';"
            cursor.execute(sql1)    # 执行SQL查询
            result = cursor.fetchone()  # 获取查询结果的第一行数据
            # 匹配得到结果即管理员数据库中存在此管理员
            if result:
                # 登陆成功
                flask.session['login'] = 'OK'
                users.append(user)  # 存储登陆成功的用户名用于显示
                return flask.redirect(flask.url_for('student'))
                # return flask.redirect('/file')
        else:  # 输入验证不通过
            msg = '非法输入'
    else:
        msg = ''
        user = ''
    return flask.render_template('login.html', msg=msg, user=user)


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
        db.commit()
        # POST方法时显示数据
        sql_list = "select * from students_infos"
        cursor.execute(sql_list)
        results = cursor.fetchall()
    return flask.render_template('student.html', insert_result=insert_result, user_info=user_info, results=results)


@app.route('/updata_student', methods=['GET', "POST"])
def updata_student():
    # login session值
    if flask.session.get("login", "") == '':
        # 用户没有登陆
        print('用户还没有登陆!即将重定向!')
        return flask.redirect('/')
    insert_result = ''
    # 获取显示学生数据信息(GET方法的时候显示数据)
    if flask.request.method == 'GET':
        sql_list = "select * from students_infos"
        cursor.execute(sql_list)        # 执行操作
        results = cursor.fetchall()     # 获取执行结果
    # 当用户登陆有存储信息时显示用户名,否则为空
    if users:
        for user in users:
            user_info = user
    else:
        user_info = ''
    if flask.request.method == 'POST':
        # 获取输入的学生信息
        student_id = flask.request.values.get("student_id", "")
        student_class = flask.request.values.get("student_class", "")
        student_name = flask.request.values.get("student_name", "")
        student_sex = flask.request.values.get("student_sex", "")

        # 验证通过
        if student_id is not None:  # 验证通过
            # 获取下拉框的数据
            select = flask.request.form.get('selected_one')
            if select == '修改学生班级':
                try:
                    sql = "update students_infos set student_class=%s where student_id=%s;"
                    cursor.execute(sql, (student_class, student_id))
                    insert_result = "学生" + student_id + "的班级修改成功!"
                except Exception as err:
                    print(err)
                    insert_result = "修改学生班级失败!"
                    pass
                db.commit()
            if select == '修改学生姓名':
                try:
                    sql = "update students_infos set student_name=%s where student_id=%s;"
                    cursor.execute(sql, (student_name, student_id))
                    insert_result = "学生" + student_name + "的姓名修改成功!"
                except Exception as err:
                    print(err)
                    insert_result = "修改学生姓名失败!"
                    pass
                db.commit()

            if select == '修改学生性别':
                try:
                    sql = "update students_infos set student_sex=%s where student_id=%s;"
                    cursor.execute(sql, (student_sex, student_id))
                    insert_result = "学生性别修改成功!"
                except Exception as err:
                    print(err)
                    insert_result = "修改学生性别失败!"
                    pass
                db.commit()
            if select == '删除学生':
                try:
                    sql_delete = "delete from students_infos where student_id = %s;"
                    valuer = (student_id,)
                    cursor.execute(sql_delete, valuer)
                    db.commit()   # 在执行完数据库操作后进行提交
                    insert_result = "成功删除学生"
                except Exception as err:
                    print(err)
                    insert_result = "删除失败"
                    pass

        else:  # 输入验证不通过
            insert_result = "输入的格式不符合要求!"
        # POST方法时显示数据
        sql_list = "select * from students_infos"
        cursor.execute(sql_list)
        results = cursor.fetchall()
    return flask.render_template('updata_student.html', user_info=user_info, insert_result=insert_result,
                                 results=results)



if __name__ == '__main__':  # 固定的写法，程序的入口
    app.run()  # 启动应用程序，