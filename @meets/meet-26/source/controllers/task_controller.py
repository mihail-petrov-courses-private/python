from flask import Blueprint
from flask import request
import db

task_route_registry = Blueprint('tasks', __name__)


# GET -> вземи ми всички задачи
@task_route_registry.route("/tasks", methods=["GET"])
def select_all_tasks():
    return db.db_query("SELECT * FROM td_tasks")

# POST -> вкарай в системата нова задача
@task_route_registry.route("/tasks", methods=["POST"])
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