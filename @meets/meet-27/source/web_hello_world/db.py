import mysql.connector

db_instance = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="task_manager"
)

cursor = db_instance.cursor()


def select(table, columns, where_dict):

    where_query = " AND ".join([f"{column_name} = %s" for column_name in where_dict.keys()])
    where_query_values = tuple(where_dict.values()) # списък

    query = f"SELECT {columns} FROM {table} WHERE {where_query}"

    cursor.execute(query, where_query_values)

    return cursor.fetchall()


# ???? -- колони и стойности
#
def insert(table, col_value_dict):

    query_insert_col = ",".join(col_value_dict.keys())
    query_data = tuple(col_value_dict.values())
    query_count = len(query_data)

    query_insert_vals = ",".join(["%s"] * query_count)
    query = f"INSERT INTO {table}( {query_insert_col} ) VALUES( {query_insert_vals} )"

    cursor.execute(query, query_data)
    db_instance.commit()

def update(table, col_value_dict, where_dict):

    set_query = ",".join([f"{column_name} = %s" for column_name in col_value_dict.keys()])
    set_query_values = tuple(col_value_dict.values()) # списък

    where_query = " AND ".join([f"{column_name} = %s" for column_name in where_dict.keys()])
    where_query_values = tuple(where_dict.values()) # списък

    value_list = set_query_values + where_query_values
    query = f"UPDATE {table} SET {set_query} WHERE {where_query}"

    cursor.execute(query, value_list)
    db_instance.commit()

def delete(table, where_dict):
    pass