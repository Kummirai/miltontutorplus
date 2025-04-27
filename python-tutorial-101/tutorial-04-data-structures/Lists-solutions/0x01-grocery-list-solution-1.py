grocery_list = []

def add_item(item):
    if item in grocery_list:
        print(f"❌ {item} already exists!")
    else:
        grocery_list.append(item)
        print(f"✅ Added: {item}")

def remove_item(item):
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"❌ Removed: {item}")
    else:
        print("Item not found!")

def check_item(item):
    if item in grocery_list:
        print(f"✔️ Yes, {item} is on the list.")
    else:
        print(f"❌ No, {item} is not on the list.")

def show_list():
    print("\nYour Grocery List:")
    for i, item in enumerate(grocery_list, 1):
        print(f"{i}. {item}")

# Main program loop
while True:
    print("\nGrocery List Manager")
    print("-------------------")
    print("1. Add item")
    print("2. Remove item")
    print("3. Check item")
    print("4. View list")
    print("5. Exit")

    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        item = input("Enter item to add: ").strip().title()
        add_item(item)
    elif choice == "2":
        item = input("Enter item to remove: ").strip().title()
        remove_item(item)
    elif choice == "3":
        item = input("Enter item to check: ").strip().title()
        check_item(item)
    elif choice == "4":
        show_list()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")