from flask import Flask
from flask import request
# import mysql.connector
import db

# трябва да си направим Flask приложение
app = Flask(__name__)

# END POINT - URL адрес със закачена за него функция
@app.route("/hello")
def hello():
    return "Hello"


# GET -> вземи ми всички задачи
@app.route("/tasks", methods=["GET"])
def select_all_tasks():
    return db.db_query("SELECT * FROM td_tasks")

# POST -> вкарай в системата нова задача
@app.route("/tasks", methods=["POST"])
def create_new_task():

    request_data = request.get_json()
    title = request_data["title"]
    description = request_data["desc"]

    db.db_insert(f"INSERT INTO td_tasks(title, summary, task_status) VALUES('{title}', '{description}', 'OPEN')")
    # db.db_into("td_tasks")
    #   .values("title", title)
    #   .values("summary", summary)
    #   .insert()

    return {"result": "Create new task"}

# from task_route import *


from project_route import *


from user_route import *

if __name__ == '__main__':
    app.run()



