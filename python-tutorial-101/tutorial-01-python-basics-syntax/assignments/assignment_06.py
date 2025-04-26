# Assignment 6: List Operations

def create_list():
    return ['apple', 'banana', 'cherry', 'date', 'elderberry']

def add_fruit(fruit_list, new_fruit):
    fruit_list.append(new_fruit)
    return fruit_list

def remove_second_fruit(fruit_list):
    fruit_list.pop(1)
    return fruit_list
