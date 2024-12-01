from flask import Blueprint, request
import db
import uuid

user_route_registry = Blueprint("users", __name__)

# def get_database_data():
#     # ще хвърля грешка
#     raise Exception("Soemthing whent wrong with the db")



@user_route_registry.route("/users")
def get_all_users():
    return db.select("td_users")


@user_route_registry.route("/auth", methods = ['POST'])
def authenticate_user():

    body = request.get_json()
    username = body["username"]
    password = body["password"]

    result = db.select("td_users", "*", {
        "username": username,
        "password": password
    })

    if len(result) == 0:
        return {
            "message": "Wrong username or password"
        }, 400

    # UUID
    if len(result) == 1:

        try:
            token_id = uuid.uuid4().hex

            db.insert("td_tokens", {
                "token"     : token_id,
                "username"  : username
            })
        except Exception:

            db.update("td_tokens", {
                "token"     : token_id
            }, {
                "username": username
            })

        return {
            "message" : token_id
        }, 200

    return {
        "message" : "Something went wrong"
    }, 500
