from flask import Blueprint
import db

project_route_registry = Blueprint('projects', __name__)

@project_route_registry.route("/projects")
def get_all_projects():
    return db.select("td_projects")