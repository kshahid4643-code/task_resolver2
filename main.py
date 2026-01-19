from sample_data import tasks
from resolver import resolve_tasks

def main():
    print("Task Execution Order:\n")

    try:
        ordered_tasks = resolve_tasks(tasks)
        for i, task in enumerate(ordered_tasks, start=1):
            print(f"{i}. {task.name}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
