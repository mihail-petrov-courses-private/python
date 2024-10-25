from flask import Blueprint
from db import db_query

project_route_registry = Blueprint('projects', __name__)

@project_route_registry.route("/projects")
def get_all_projects():
    return db_query("SELECT * FROM td_projects")