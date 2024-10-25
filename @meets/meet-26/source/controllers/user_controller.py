from flask import Blueprint
import db

user_route_registry = Blueprint("users", __name__)

@user_route_registry.route("/users")
def get_all_users():
    return db.db_query("SELECT * FROM td_users")