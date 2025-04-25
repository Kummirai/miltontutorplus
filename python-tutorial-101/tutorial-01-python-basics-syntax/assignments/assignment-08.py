#08 for Python Basics Syntax -->
"""
Assignment 8: Dictionary Basics
Create a program that:
1. Creates a dictionary for a book (title, author, year)
2. Adds a new key 'genre'
3. Updates the year
4. Prints all book information
Example Output:
Title: Python 101
Author: John Doe
Year: 2023
Genre: Programming
"""
# Your code here

# 1. Create a dictionary for a book
book = {
    "title": "Python 101",
    "author": "John Doe",
    "year": 2021
}

# 2. Add a new key 'genre'
book["genre"] = "Programming"

# 3. Update the year
book["year"] = 2023

# 4. Print all book information
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")
print(f"Year: {book['year']}")
print(f"Genre: {book['genre']}")