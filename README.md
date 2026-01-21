🧠 Task Dependency Resolver (Python)
📌 Overview

The Task Dependency Resolver is a Python-based project that determines the correct execution order of tasks based on their dependencies.

In real-world projects, some tasks cannot start until others are completed. This program models that situation and outputs a valid sequence using dependency resolution logic.

🎯 Problem Statement

Given a set of tasks and their dependencies, determine the order in which tasks should be executed so that:

No task runs before its dependency

All tasks are completed successfully

🛠️ Technologies Used

Python 3

Core Python data structures (lists, dictionaries)

Graph concepts (Directed Acyclic Graph)

Topological Sorting logic

📂 Project Structure
task_resolver/
│
├── main.py          # Entry point of the program
├── resolver.py      # Core logic for dependency resolution
├── models.py        # Task data structures
├── sample_data.py   # Sample tasks and dependencies
├── README.md        # Project documentation
├── .gitignore       # Ignored files (venv, cache, etc.)
└── venv/            # Virtual environment (ignored by Git)

⚙️ How It Works

Tasks are represented as nodes

Dependencies are represented as directed edges

The program builds a dependency graph

A topological sorting algorithm is applied

The final execution order is printed

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/dopewave46/task_resolver2.git
cd task_resolver2

2️⃣ (Optional) Activate virtual environment
venv\Scripts\activate

3️⃣ Run the program
python main.py

✅ Sample Output
Task Execution Order:
1. Design Database
2. Build API
3. Create UI
4. Write Tests
5. Deploy

📘 Use Cases

Project planning

Software development pipelines

Task scheduling systems

Learning graph algorithms

🚀 Future Improvements

Add cycle detection

Take user input dynamically

Visualize task dependency graph

Convert into a web app

👨‍💻 Author

Shahid Khan
GitHub: https://github.com/dopewave46

🏁 Conclusion

This project demonstrates how dependency management works in real-world systems using Python.
It applies theoretical concepts like graphs and topological sorting in a practical way.
