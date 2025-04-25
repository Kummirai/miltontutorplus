#09 for Python Basics Syntax -->
"""
Assignment 9: Set Operations
Create a program that:
1. Creates two sets of numbers
2. Performs union, intersection, and difference
3. Prints the results
Example Output:
Set1: {1, 2, 3, 4}
Set2: {3, 4, 5, 6}
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference (1-2): {1, 2}
"""
# Your code here


# Define two sets of numbers
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Print the sets
print("Set1:", set1)
print("Set2:", set2)
# Perform union, intersection, and difference
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)
# Print the results
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)