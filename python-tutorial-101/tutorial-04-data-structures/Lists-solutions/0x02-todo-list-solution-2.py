# To-Do List Manager - Function Version
todo_list = []

def add_task(task):
    """Add a new task to the list"""
    if task in todo_list:
        print(f"❌ {task} already exists!")
    else:
        todo_list.append(task)
        print(f"✅ Added: {task}")

def remove_task(task):
    """Remove a task from the list"""
    if task in todo_list:
        todo_list.remove(task)
        print(f"❌ Removed: {task}")
    else:
        print("Task not found!")

def check_task(task):
    """Check if task exists in list"""
    if task in todo_list:
        print(f'✔️ Yes, "{task}" is on your list.')
    else:
        print(f'❌ No, "{task}" is not on your list.')

def view_list():
    """Display all tasks"""
    print("\nYour To-Do List:")
    if not todo_list:
        print("(Your list is empty)")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def main():
    """Main program loop"""
    while True:
        print("\nTo-Do List Manager")
        print("------------------")
        print("1. Add task")
        print("2. Remove task")
        print("3. Check task")
        print("4. View list")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            task = input("Enter task to add: ").strip()
            add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ").strip()
            remove_task(task)
        elif choice == "3":
            task = input("Enter task to check: ").strip()
            check_task(task)
        elif choice == "4":
            view_list()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()