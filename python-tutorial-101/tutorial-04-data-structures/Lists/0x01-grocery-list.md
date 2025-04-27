# Grocery List Manager (Python Lists Project)

## Project Description:
You will build a **Grocery List Manager** program using Python lists. This program will allow users to add, remove, and manage items in their grocery list. The goal is to practice core list operations such as appending, removing, checking membership, and displaying items.

---

## Problem Statement
Your task is to create a Python script that:

- Starts with an empty grocery list.
- Allows the user to add items to the list.
- Allows the user to remove items from the list.
- Checks if an item already exists in the list.
- Displays the current list of groceries.

---

## Requirements & Tasks

### 1. Basic List Operations

#### ✅ Initialize an empty list
```python
grocery_list = []
```

#### ✅ Add items to the list
- Prompt the user to enter an item.
- Add the item to `grocery_list` if it doesn’t already exist.
- If the item is already in the list, print: `"Item already exists!"`

#### ✅ Remove items from the list
- Ask the user which item they want to remove.
- If the item exists, remove it and print: `"Removed [item]."`
- If it doesn’t exist, print: `"Item not found!"`

#### ✅ Check if an item exists
- Ask the user for an item.
- Print `"Yes, [item] is on the list."` or `"No, [item] is not on the list."`

#### ✅ Display the full grocery list
- Print all items in the list, numbered.

**Example output:**
```
1. Milk
2. Eggs
3. Bread
```

