"""
To-Do List Application
CodSoft Python Programming Internship - Task 1

A command-line To-Do List app that lets a user create, view, update,
mark complete, and delete tasks. Tasks are stored persistently in a
local JSON file (tasks.json) so the list survives between runs.
"""

import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks():
    """Load tasks from the JSON data file. Returns an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Persist the current task list to the JSON data file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def print_header(title):
    print("\n" + "=" * 40)
    print(title.center(40))
    print("=" * 40)


def view_tasks(tasks):
    print_header("YOUR TO-DO LIST")
    if not tasks:
        print("No tasks yet. Add one from the main menu!")
        return
    for i, task in enumerate(tasks, start=1):
        status = "[X]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['title']}  (added {task['created']})")
    print("=" * 40)


def add_task(tasks):
    title = input("Enter the new task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    tasks.append({
        "title": title,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    save_tasks(tasks)
    print(f'Added: "{title}"')


def _select_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return None
    try:
        choice = int(input("Enter task number: "))
        if 1 <= choice <= len(tasks):
            return choice - 1
    except ValueError:
        pass
    print("Invalid task number.")
    return None


def mark_complete(tasks):
    idx = _select_task(tasks)
    if idx is not None:
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print(f'Marked complete: "{tasks[idx]["title"]}"')


def update_task(tasks):
    idx = _select_task(tasks)
    if idx is not None:
        new_title = input("Enter the updated task text: ").strip()
        if new_title:
            tasks[idx]["title"] = new_title
            save_tasks(tasks)
            print("Task updated.")
        else:
            print("Task cannot be empty; no changes made.")


def delete_task(tasks):
    idx = _select_task(tasks)
    if idx is not None:
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print(f'Deleted: "{removed["title"]}"')


def main_menu():
    print("""
1. View tasks
2. Add task
3. Mark task as complete
4. Update task
5. Delete task
6. Exit
""")


def main():
    tasks = load_tasks()
    print_header("TO-DO LIST APP")
    print("Manage your tasks efficiently. Data is saved automatically.")

    while True:
        main_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
