from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'



from admin import admin_blue
from user import user_blue

app.register_blueprint(admin_blue)
app.register_blueprint(user_blue)


if __name__ == '__main__':
    app.run(port=5678)