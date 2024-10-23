from app import app
import db

# GET -> вземи ми всички задачи
@app.route("/tasks", methods=["GET"])
def select_all_tasks():
    return db.db_query("SELECT * FROM td_tasks")

# POST -> вкарай в системата нова задача
@app.route("/tasks", methods=["POST"])
def create_new_task():
    pass