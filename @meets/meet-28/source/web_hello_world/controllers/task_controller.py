from flask import Blueprint
from flask import request
import db
import services.auth as auth_service

task_route_registry = Blueprint('tasks', __name__)


# GET -> вземи ми всички задачи
@task_route_registry.route("/tasks", methods=["GET"])
def select_all_tasks():
    # return db.db_query("SELECT * FROM td_tasks")
    return db.select("td_tasks")

# POST -> вкарай в системата нова задача
@task_route_registry.route("/tasks", methods=["POST"])
def create_new_task():

    request_data    = request.get_json()
    title           = request_data["title"]
    description     = request_data["desc"]
    user_token      = request_data["token"]

    # Дали token е валиден
    if not auth_service.is_token_valid(user_token):
        return {
            "message": "No permission for this operation"
        }, 403

    user_id = auth_service.get_user_id_by_token(user_token)

    db.insert("td_tasks", {
        "title"     : title,
        "summary"   : description,
        "user_id"   : user_id
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