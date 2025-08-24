from services.todo import ToDoList

todo = ToDoList("localhost", "root", "Cassanova911@", "todolist")

todo.add_task("Finish Python project", "To-Do app with MySQL", "pending", "2025-08-30")

for task in todo.list_tasks():
    print(task)

todo.update_task(1, "done")
