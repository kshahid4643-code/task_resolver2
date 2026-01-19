from models import Task

tasks = [
    Task(1, "Design Database"),
    Task(2, "Build API", dependencies=[1]),
    Task(3, "Create UI", dependencies=[2]),
    Task(4, "Write Tests", dependencies=[2]),
    Task(5, "Deploy", dependencies=[3, 4]),
]
