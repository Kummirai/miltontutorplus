#07 for Python Basics Syntax -->
"""
Assignment 7: Tuple Unpacking
Create a program that:
1. Uses a tuple with student info (name, age, grade)
2. Unpacks the tuple into variables
3. Prints a formatted message
Example Output:
Student: Alice
Age: 20
Grade: A
"""
# Your code here

# 1. Create a tuple with student info (name, age, grade)
student = ("Alice", 20, "A")

# 2. Unpack the tuple into variables
name, age, grade = student

# 3. Print a formatted message
print(f"Student: {name}")
print(f"Age: {age}")
print(f"Grade: {grade}")