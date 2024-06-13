import json
import os

# File to store the tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task_name):
    tasks.append({"name": task_name, "completed": False})
    save_tasks(tasks)

def view_tasks(tasks):
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. {task['name']} [{status}]")

def mark_task_completed(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(tasks, task_index)
        elif choice == "4":
            task_index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
-