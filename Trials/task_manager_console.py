
import os
from datetime import datetime

DATA_FILE = "tasks.txt"

def read_tasks():
    tasks = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    tasks.append({
                        'desc': parts[0],
                        'due': parts[1],
                        'done': parts[2] == 'True'
                    })
    return tasks

def write_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        for task in tasks:
            f.write(f"{task['desc']},{task['due']},{task['done']}\n")

def add_task(desc, due):
    try:
        datetime.strptime(due, "%Y-%m-%d")  # Validate date format
        with open(DATA_FILE, 'a') as f:
            f.write(f"{desc},{due},False\n")
        print("Task added.")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print(f"{'ID':<3} {'Task':<30} {'Due Date':<12} {'Done'}")
        print("-" * 55)
        for i, task in enumerate(tasks):
            print(f"{i:<3} {task['desc']:<30} {task['due']:<12} {task['done']}")

def mark_done(task_id):
    tasks = read_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
        write_tasks(tasks)
        print("Task marked as done.")
    else:
        print("Invalid task ID.")

def search_tasks(query):
    tasks = read_tasks()
    return [t for t in tasks if query.lower() in t['desc'].lower()]

def main():
    while True:
        print("\nSimple Task Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Search tasks")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            display_tasks(read_tasks())
        elif choice == '2':
            desc = input("Enter task description: ").strip()
            due = input("Enter due date (YYYY-MM-DD): ").strip()
            if desc and due:
                add_task(desc, due)
            else:
                print("Both fields required.")
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to mark as done: ").strip())
                mark_done(task_id)
            except ValueError:
                print("Invalid input. Enter a number.")
        elif choice == '4':
            query = input("Enter keyword to search: ").strip()
            display_tasks(search_tasks(query))
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
