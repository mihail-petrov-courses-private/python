from flask import Flask

# трябва да си направим Flask приложение
app = Flask(__name__)


# END POINT - URL адрес със закачена за него функция
@app.route("/hello")
def hello():
    return "Hello"


if __name__ == '__main__':
    app.run()
