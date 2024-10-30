from flask import Blueprint
from flask import request
import db

task_route_registry = Blueprint('tasks', __name__)


# GET -> вземи ми всички задачи
@task_route_registry.route("/tasks", methods=["GET"])
def select_all_tasks():
    # return db.db_query("SELECT * FROM td_tasks")
    return db.select("td_tasks")

# POST -> вкарай в системата нова задача
@task_route_registry.route("/tasks", methods=["POST"])
def create_new_task():

    request_data = request.get_json()
    title = request_data["title"]
    description = request_data["desc"]

    db.insert("td_tasks", {
        "title": title,
        "summary": description
    })

    return {"result": "Create new task"}

@task_route_registry.route("/tasks", methods=["PUT"])
def update_task():

    request_data = request.get_json()
    title = request_data["title"]
    description = request_data["desc"]

    db.update("td_tasks", {
        "title": title, "summary": description
    }, {
        "id": "1"
    })

    return {"result": "Update existing task"}