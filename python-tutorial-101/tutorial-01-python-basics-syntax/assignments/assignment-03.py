#03 for Python Basics Syntax -->
"""
Assignment 3: Temperature Converter
Write a program that converts Fahrenheit to Celsius.
Formula: C = (F - 32) * 5/9
Example Output:
Enter temperature in Fahrenheit: 68
68°F is 20.0°C
"""
# Your code here

#Ask the user for temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Display the result
print(f"{fahrenheit}°F is {celsius:.1f}°C")