from app import app
from db import db_query


@app.route("/projects")
def get_all_projects():
    return db_query("SELECT * FROM td_projects")