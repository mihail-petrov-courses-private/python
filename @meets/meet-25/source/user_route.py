from app import app
import db


@app.route("/users")
def get_all_users():
    return db.db_query("SELECT * FROM td_users")