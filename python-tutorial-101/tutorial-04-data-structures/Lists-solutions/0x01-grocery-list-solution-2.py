# Grocery List Manager - Beginner Version
grocery_list = []

while True:
    print("\nGrocery List Manager")
    print("-------------------")
    print("1. Add item")
    print("2. Remove item")
    print("3. Check item")
    print("4. View list")
    print("5. Exit")
    
    choice = input("\nChoose an option (1-5): ")
    
    # Add item
    if choice == "1":
        item = input("Enter item to add: ").strip().title()
        if item in grocery_list:
            print(f"❌ {item} already exists!")
        else:
            grocery_list.append(item)
            print(f"✅ Added: {item}")
    
    # Remove item
    elif choice == "2":
        item = input("Enter item to remove: ").strip().title()
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"❌ Removed: {item}")
        else:
            print("Item not found!")
    
    # Check item
    elif choice == "3":
        item = input("Enter item to check: ").strip().title()
        if item in grocery_list:
            print(f"✔️ Yes, {item} is on the list.")
        else:
            print(f"❌ No, {item} is not on the list.")
    
    # View list
    elif choice == "4":
        print("\nYour Grocery List:")
        if not grocery_list:
            print("(Your list is empty)")
        else:
            for i, item in enumerate(grocery_list, 1):
                print(f"{i}. {item}")
    
    # Exit
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again!")