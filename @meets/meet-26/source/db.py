import mysql.connector

db_instance = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="task_manager"
)

query = db_instance.cursor()


def db_query(query_str):

    query.execute(query_str)
    return query.fetchall()


def db_insert(query_str):

    query.execute(query_str)
    db_instance.commit()
