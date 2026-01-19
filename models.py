class Task:
    def __init__(self, task_id, name, dependencies=None):
        self.task_id = task_id
        self.name = name
        self.dependencies = dependencies or []

    def __repr__(self):
        return f"Task({self.task_id}, {self.name})"
