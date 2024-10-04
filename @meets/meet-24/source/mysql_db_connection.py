import mysql.connector

db_instance = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="task_manager"
)
# КУРСОР - абстрактен указател за начало на операция в СИСТЕМА ЗА УПРАВЛЕНИЕ НА БАЗИ ДАННИ

print("Connected")
print(db_instance)

db_cursor = db_instance.cursor()

# Операция
db_cursor.execute("INSERT INTO td_users(username, password, first_name, last_name) VALUES(%s, %s, %s, %s)", (
    "todorm", "password1", "Todor", "Manchev"
))

# Казвам че всички операции, които съм правил до момента - трябва да влязат в базата данни ЗА ПОСТОЯННО
db_instance.commit()

print(db_cursor.rowcount)


db_cursor.execute("SELECT username FROM td_users")
collection = db_cursor.fetchall()

for element in collection:
    print(element)


