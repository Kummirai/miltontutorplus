#05 for Python Basics Syntax -->
"""
Assignment 5: String Manipulation
Write a program that:
1. Asks for a sentence
2. Prints the sentence in uppercase
3. Prints the sentence in lowercase
4. Prints the number of characters
Example Output:
Enter a sentence: Hello World
Uppercase: HELLO WORLD
Lowercase: hello world
Character count: 11
"""
# Your code here

#1. Ask for a sentence
sentence = input("Enter a sentence: ")

# 2. Print the sentence in uppercase
print("Uppercase:", sentence.upper())

# 3. Print the sentence in lowercase
print("Lowercase:", sentence.lower())

# 4. Print the number of characters (including spaces and punctuation)
print("Character count:", len(sentence))
