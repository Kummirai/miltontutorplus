#04 for Python Basics Syntax -->
"""
Assignment 4: Simple Calculator
Create a basic calculator that can add, subtract, multiply, and divide two numbers.
Example Output:
Enter first number: 10
Enter second number: 5
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
"""
# Your code here

num1 = float(input("enter first nummber:"))
num2 = float(input("enter second number:"))

# calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2  # Assumes num2 is not zero

#the results
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")







