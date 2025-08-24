class Task:
    def __init__(self, id, title, description, status, due_date, created_at, updated_at):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"[{self.id}] {self.title} ({self.status}) - Due: {self.due_date}"

    @classmethod
    def from_row(cls, row):
        return cls(*row)
