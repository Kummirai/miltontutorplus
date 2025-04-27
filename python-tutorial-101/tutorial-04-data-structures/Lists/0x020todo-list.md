# To-Do List Manager (Beginner Python Project)

# Sample program
https://www.loom.com/share/02e7d539dfa44d219416211badd9c8d3?sid=30f7f298-6de2-4d2c-badf-aa400ae5d6e8

## Project Description:
You will build a **To-Do List Manager** program using Python lists. This program will allow users to add, remove, check, and view tasks on their to-do list. The goal is to practice core list operations such as appending, removing, checking membership, and displaying items, while building a simple interactive menu.

---

## Problem Statement
Your task is to create a Python script that:

- Starts with an empty to-do list.
- Allows the user to add tasks to the list.
- Allows the user to remove completed tasks.
- Checks if a task exists in the list.
- Displays the current list of tasks.
- Provides a simple menu interface for these actions.

---

## Requirements & Tasks

### 1. Basic List Operations

#### ✅ Initialize an empty list
```python
todo_list = []
```

#### ✅ Add tasks to the list
- Prompt the user to enter a task.
- Add the task to `todo_list` if it doesn’t already exist.
- If the task is already in the list, print: `"Task already exists!"`

#### ✅ Remove tasks from the list
- Ask the user which task they want to remove.
- If the task exists, remove it and print: `"❌ Removed: [task]"`
- If it doesn’t exist, print: `"Task not found!"`

#### ✅ Check if a task exists
- Ask the user for a task to check.
- Print `"✔️ Yes, '[task]' is on your list."` or `"No, '[task]' is not on your list."`

#### ✅ Display the full to-do list
- Print all tasks in the list, numbered.

---

## Features
- Add tasks to your to-do list
- Remove completed tasks
- Check if a task exists
- View full task list
- Simple menu interface

---

## Example Usage
```
To-Do List Manager
1. Add task
2. Remove task
3. Check task
4. View list
5. Exit

Choose an option (1-5): 1
Enter task to add: Finish homework
👌 Added: Finish homework

Choose an option (1-5): 1
Enter task to add: Buy groceries
👌 Added: Buy groceries

Choose an option (1-5): 4
Your To-Do List:

1. Finish homework
2. Buy groceries

Choose an option (1-5): 2
Enter task to remove: Finish homework
❌ Removed: Finish homework

Choose an option (1-5): 3
Enter task to check: Buy groceries
✔️ Yes, "Buy groceries" is on your list.
```

