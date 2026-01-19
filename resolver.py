def resolve_tasks(tasks):
    task_map = {task.task_id: task for task in tasks}
    visited = set()
    visiting = set()
    result = []

    def dfs(task):
        if task.task_id in visiting:
            raise Exception("Circular dependency detected!")

        if task.task_id in visited:
            return

        visiting.add(task.task_id)

        for dep_id in task.dependencies:
            dfs(task_map[dep_id])

        visiting.remove(task.task_id)
        visited.add(task.task_id)
        result.append(task)

    for task in tasks:
        if task.task_id not in visited:
            dfs(task)

    return result
