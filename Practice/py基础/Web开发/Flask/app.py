from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # return '<h1>Home</h1>'
    abc = 'Home,123'
    page_list = [1,2,3,4,5]
    return render_template('student.html', home = abc,page_list = page_list)

@app.route('/page/1', methods=['GET', 'POST'])
def qwe():
    aa = 'Ys'
    return render_template('/page/1.html', aa = aa,)



@app.route('/signin', methods=['GET'])
def signin_form():
    # return '''<form action="/signin" method="post">
    #           <p>账号输入框: <input name="username"></p>
    #           <p>密码输入框: <input name="password" type="password"></p>
    #           <p><button type="submit">登录</button></p>
    #           </form>'''
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    # # 需要从request对象读取表单内容：
    # if request.form['username']=='admin' and request.form['password']=='password':
    #     return '<h3>Hello, admin!</h3>'
    # return '<h3>Bad username or password.</h3>'

    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run(debug=True)