# Python Lists - A Comprehensive Tutorial

"""
This tutorial will walk you through everything you need to know about Python lists.
It includes definitions, examples, and important tips.
Save this file and run parts of it in your Python environment to practice.
"""

# 1. What is a List?

"""
A list is a built-in Python data type that stores an ordered collection of items.
Lists can contain elements of different types, but usually the elements are of the same type.
"""

# Example:
my_list = [1, 2, 3, 4, 5]
print("Example List:", my_list)

# Lists can also contain strings, floats, booleans, or even other lists:
mixed_list = ["apple", 3.14, True, [1, 2, 3]]
print("Mixed List:", mixed_list)


# 2. Creating a List

# Empty list
empty_list = []
print("Empty List:", empty_list)

# List with elements
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)

# Using the list() constructor
numbers = list((1, 2, 3, 4))
print("Numbers List:", numbers)


# 3. Accessing List Items

# Access by index (indices start from 0)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])  # Negative indices count from the end

# Slicing a list
print("First two fruits:", fruits[0:2])


# 4. Modifying List Items

# Change a value
fruits[1] = "blueberry"
print("Modified Fruits List:", fruits)


# 5. Adding Items to a List

# append() - Adds an item to the end
fruits.append("orange")
print("After append:", fruits)

# insert() - Adds an item at a specific index
fruits.insert(1, "mango")
print("After insert:", fruits)

# extend() - Add elements of another list
fruits.extend(["grape", "watermelon"])
print("After extend:", fruits)


# 6. Removing Items from a List

# remove() - Removes the first matching value
fruits.remove("mango")
print("After remove:", fruits)

# pop() - Removes item at given index (or the last item if index not provided)
popped_item = fruits.pop()
print("Popped Item:", popped_item)
print("After pop:", fruits)

# del - Delete item by index
del fruits[0]
print("After del:", fruits)

# clear() - Removes all items
# fruits.clear()
# print("After clear:", fruits)


# 7. Looping Through a List

# Using for loop
for fruit in fruits:
    print("Fruit:", fruit)

# Using index
for i in range(len(fruits)):
    print(f"Fruit at index {i}: {fruits[i]}")


# 8. List Comprehensions

# Simple example
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even Squares:", even_squares)


# 9. List Methods

numbers = [5, 3, 8, 1, 2]

print("Original Numbers:", numbers)

# append()
numbers.append(10)
print("After append:", numbers)

# clear()
numbers.clear()
print("After clear:", numbers)

# copy()
numbers = [5, 3, 8, 1, 2]
copied_numbers = numbers.copy()
print("Copied Numbers:", copied_numbers)

# count()
count_of_two = numbers.count(2)
print("Count of 2:", count_of_two)

# extend()
numbers.extend([11, 12, 13])
print("After extend:", numbers)

# index()
index_of_eight = numbers.index(8)
print("Index of 8:", index_of_eight)

# insert()
numbers.insert(2, 7)
print("After insert:", numbers)

# pop()
popped = numbers.pop(2)
print(f"Popped element: {popped}")
print("After pop:", numbers)

# remove()
numbers.remove(1)
print("After remove:", numbers)

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# sort()
numbers.sort()
print("After sort:", numbers)


# 10. Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print("Element at row 1, column 2:", matrix[0][1])

# Loop through nested lists
for row in matrix:
    for num in row:
        print(num, end=' ')
    print()


# 11. Copying Lists: Shallow vs Deep Copy

import copy

# Shallow copy
list1 = [[1, 2], [3, 4]]
list2 = list1.copy()
list1[0][0] = 99
print("Shallow Copy List1:", list1)
print("Shallow Copy List2:", list2)

# Deep copy
list3 = copy.deepcopy(list1)
list1[0][0] = 100
print("Deep Copy List1:", list1)
print("Deep Copy List3:", list3)


# 12. Useful Tips

"""
- Lists are mutable (you can change their content).
- Lists can store different data types.
- Watch out when copying lists!
- Use list comprehensions for cleaner and faster code.
- Use built-in methods like append(), remove(), pop(), etc.
- List Methods: append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()
"""


# Congratulations!
print("\nYou have completed the Python Lists Tutorial!")
