import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",            # change if different
            password="Cassanova911@", # replace with your MySQL password
            database="todolist"
        )
        if connection.is_connected():
            print("Connected to MySQL database: todo_app")
            return connection
    except Error as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()
