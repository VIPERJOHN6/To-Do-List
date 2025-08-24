# services/todo.py

import mysql.connector
from mysql.connector import Error
from models.task import Task

class ToDoList:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def add_task(self, title, description=None, status="pending", due_date=None):
        cursor = self.connection.cursor()
        sql = "INSERT INTO tasks (title, description, status, due_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (title, description, status, due_date))
        self.connection.commit()
        print(f"Task '{title}' added.")

    def list_tasks(self):
        cursor = self.connection.cursor()
        sql = "SELECT id, title, description, status, due_date, created_at, updated_at FROM tasks"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [Task.from_row(row) for row in rows]

    def update_task(self, task_id, status):
        cursor = self.connection.cursor()
        sql = "UPDATE tasks SET status = %s WHERE id = %s"
        cursor.execute(sql, (status, task_id))
        self.connection.commit()
        print(f"Task {task_id} updated to {status}.")

    def delete_task(self, task_id):
        cursor = self.connection.cursor()
        sql = "DELETE FROM tasks WHERE id = %s"
        cursor.execute(sql, (task_id,))
        self.connection.commit()
        print(f"Task {task_id} deleted.")
