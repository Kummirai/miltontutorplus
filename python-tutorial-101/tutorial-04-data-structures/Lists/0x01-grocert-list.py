# Grocery List Manager - Beginner Version
"""
You will build a Grocery List Manager program using Python lists. This program will allow users to add, remove, and manage items in their grocery list. The goal is to practice core list operations such as appending, removing, checking membership, and displaying items
"""
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
    if(choice == "1"):
        add_item = input("Add item: ")
        grocery_list.append(add_item)

    # Remove item

    # Check item
    
    # View list
    if(choice == "4"):
        count = 0
        for items in grocery_list:
            count= count + 1
            print(f"{count}. {items}")
    
    # Exit
   
    