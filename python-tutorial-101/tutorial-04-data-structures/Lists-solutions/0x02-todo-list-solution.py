
## Python Implementation
todo_list = []

while True:
    print("\nTo-Do List Manager")
    print("------------------")
    print("1. Add task")
    print("2. Remove task")
    print("3. Check task")
    print("4. View list")
    print("5. Exit")
    
    choice = input("\nChoose an option (1-5): ")
    
    # Add task
    if choice == "1":
        task = input("Enter task to add: ").strip()
        if task in todo_list:
            print(f"❌ {task} already exists!")
        else:
            todo_list.append(task)
            print(f"✅ Added: {task}")
    
    # Remove task
    elif choice == "2":
        task = input("Enter task to remove: ").strip()
        if task in todo_list:
            todo_list.remove(task)
            print(f"❌ Removed: {task}")
        else:
            print("Task not found!")
    
    # Check task
    elif choice == "3":
        task = input("Enter task to check: ").strip()
        if task in todo_list:
            print(f'✔️ Yes, "{task}" is on your list.')
        else:
            print(f'❌ No, "{task}" is not on your list.')
    
    # View list
    elif choice == "4":
        print("\nYour To-Do List:")
        if not todo_list:
            print("(Your list is empty)")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
    
    # Exit
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again!")