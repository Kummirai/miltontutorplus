#10 for Python Basics Syntax -->
"""
Assignment 10: Type Conversion
Write a program that:
1. Takes a number as string input
2. Converts it to integer and float
3. Performs calculations
4. Prints results with types
Example Output:
Enter a number: 10
As integer: 10 (type: <class 'int'>)
As float: 10.0 (type: <class 'float'>)
Integer + 5: 15
Float * 2: 20.0
"""
# Your code here
# Take a number as string input
num_str = input("Enter a number: ")
# Convert to integer and float
num_int = int(num_str)
num_float = float(num_str)
# Print the conversions with types
print(f"As integer: {num_int} (type: {type(num_int)})")
print(f"As float: {num_float} (type: {type(num_float)})")
# Perform calculations
int_result = num_int + 5
float_result = num_float * 2
# Print the results
print(f"Integer + 5: {int_result}")
print(f"Float * 2: {float_result}")
