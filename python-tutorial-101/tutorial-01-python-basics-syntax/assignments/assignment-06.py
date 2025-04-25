#06 for Python Basics Syntax -->
"""
Assignment 6: List Operations
Create a program that:
1. Creates a list of 5 fruits
2. Adds a new fruit
3. Removes the second fruit
4. Prints the final list and its length
Example Output:
Original list: ['apple', 'banana', 'cherry', 'date', 'elderberry']
Updated list: ['apple', 'cherry', 'date', 'elderberry', 'fig']
List length: 5
"""
# Your code here

# 1. Create a list of 5 fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Original list:", fruits)

# 2. Add a new fruit
fruits.append('fig')

# 3. Remove the second fruit (index 1)
fruits.pop(1)

# 4. Print the final list and its length
print("Updated list:", fruits)
print("List length:", len(fruits))
