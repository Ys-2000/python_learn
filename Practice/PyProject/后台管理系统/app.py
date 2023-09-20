from flask import Flask, render_template, request, redirect, session
import mysql.connector, secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)  # 生成一个32字节的 URL 安全随机字符串作为密钥
# secrets.token_hex(16)  # 生成一个16字节（128位）的随机十六进制字符串作为密钥

from flask_sqlalchemy import SQLAlchemy

# 配置MySQL数据库
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '000000',
    'database': 'web'
}

def connect_db():
    return mysql.connector.connect(**db_config)


@app.route('/')
def index():
    # return 'Welcome to the Backend Admin Panel'
    return render_template('home.html',)


@app.route('/users')
def list_users():
    conn = connect_db()
    cursor = conn.cursor()      # 创建游标
    cursor.execute('SELECT * FROM user')   # 查询
    users = cursor.fetchall()
    conn.close()    # 关闭连接
    return render_template('users.html', users=users)


def validate_registration_data(name,mobile,password,confirm_password):
    errors = []
    if not name:
        errors.append('账号不能为空')
    if not mobile.isdigit():
        errors.append('手机号必须为数字')
    if not password:
        errors.append('密码不能为空')
    if password != confirm_password:
        errors.append('密码与确认密码不一致')
    return errors


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取表单中的数据
        name = request.form['username']
        mobile = request.form['mobile']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        # 在这里可以编写验证用户名、密码和确认密码的逻辑
        validation_errors = validate_registration_data(name, mobile, password, confirm_password)
        if validation_errors:
            return render_template('register.html', errors=validation_errors)
        # 如果验证成功，可以将用户信息添加到数据库中
        conn = connect_db()  # 连接数据库
        cursor = conn.cursor()  # 创建游标
        sql = "INSERT INTO user (name,mobile,password) VALUES (%s,%s,%s)"
        val = (name, mobile, password)
        cursor.execute(sql, val)  # 指定的SQL命令执行在数据库中
        conn.commit()  # 提交事务
        cursor.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        # 注册成功后重定向到登录页面
        return redirect('/login')
    # 如果是GET请求，返回注册页面模板
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = connect_db()  # 连接数据库
    cursor = conn.cursor()  # 创建游标
    if request.method == 'POST':
        mobile = request.form['mobile']
        password = request.form['password']

        sql = 'SELECT * FROM user WHERE mobile = %s and password = %s'
        val = (mobile, password)
        cursor.execute(sql,val)
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            session['user_id'] = user[0]  # 在会话中存储用户id
            return redirect('/users')  # 重定向页面
        else:
            error = '用户名或密码不正确'
            return render_template('login.html', errors=error)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
