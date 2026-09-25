# Task 1 — To-Do List Application

**CodSoft Python Programming Internship**

## Description
A command-line To-Do List application built in Python. It allows users to
create, view, update, complete, and delete tasks. All tasks are saved
persistently to a local `tasks.json` file, so your list is still there the
next time you run the program.

## Features
- Add a new task
- View all tasks with completion status and creation timestamp
- Mark a task as complete
- Update/edit an existing task
- Delete a task
- Persistent storage using JSON (no database required)

## Requirements
- Python 3.7+
- No external libraries needed (see `requirements.txt`)

## How to Run
```bash
python todo.py
```

Then follow the on-screen menu:
```
1. View tasks
2. Add task
3. Mark task as complete
4. Update task
5. Delete task
6. Exit
```

## Files
| File | Description |
|---|---|
| `todo.py` | Main application source code |
| `requirements.txt` | Project dependencies |
| `tasks.json` | Auto-generated data file storing your tasks |
| `output/sample_run.txt` | Example of a sample program run |

## Example
```
1. [ ] Buy groceries  (added 2026-09-25 10:00)
2. [X] Finish Python assignment  (added 2026-09-25 10:05)
```

## Author
Vishal — CodSoft Python Programming Virtual Internship (Sept 2026)
